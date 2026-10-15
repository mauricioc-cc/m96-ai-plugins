import contextlib
import datetime
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "skills/gestao-gastos-pessoais/scripts/pluggy.py"
spec = importlib.util.spec_from_file_location("pluggy", SCRIPT)
pluggy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pluggy)


class PluggyTests(unittest.TestCase):
    def daily_snapshot(self, at):
        return {"source": "meu-pluggy", "schemaVersion": 1, "fetchedAt": at,
                "items": [{"item": {"id": "item"}, "accounts": [], "transactions": []}]}

    def test_daily_reuses_same_local_day_without_authentication(self):
        config = {"clientId": "test", "itemIds": ["item"]}
        at = datetime.datetime(2026, 10, 16, 1, tzinfo=datetime.timezone.utc)
        with tempfile.TemporaryDirectory() as directory, patch.object(pluggy, "Client") as factory:
            factory.return_value.snapshot.return_value = self.daily_snapshot(at.isoformat())
            pluggy.ensure_daily(config, Path(directory), now=at)
            _, _, reused = pluggy.ensure_daily(config, Path(directory), now=at + datetime.timedelta(hours=1))
            self.assertTrue(reused)
            self.assertEqual(factory.call_count, 1)

    def test_daily_refreshes_at_sao_paulo_midnight(self):
        config = {"clientId": "test", "itemIds": ["item"]}
        at = datetime.datetime(2026, 10, 16, 2, 59, tzinfo=datetime.timezone.utc)
        with tempfile.TemporaryDirectory() as directory, patch.object(pluggy, "Client") as factory:
            factory.return_value.snapshot.return_value = self.daily_snapshot(at.isoformat())
            pluggy.ensure_daily(config, Path(directory), now=at)
            _, _, reused = pluggy.ensure_daily(config, Path(directory), now=at + datetime.timedelta(minutes=1))
            self.assertFalse(reused)
            self.assertEqual(factory.call_count, 2)

    def test_force_refresh_and_corrupt_cache(self):
        config = {"clientId": "test", "itemIds": ["item"]}
        at = datetime.datetime(2026, 10, 16, 1, tzinfo=datetime.timezone.utc)
        with tempfile.TemporaryDirectory() as directory, patch.object(pluggy, "Client") as factory:
            factory.return_value.snapshot.return_value = self.daily_snapshot(at.isoformat())
            _, path, _ = pluggy.ensure_daily(config, Path(directory), now=at)
            pluggy.ensure_daily(config, Path(directory), force=True, now=at)
            path.write_text('{invalid')
            pluggy.ensure_daily(config, Path(directory), now=at)
            self.assertEqual(factory.call_count, 3)

    def test_failed_refresh_preserves_previous_cache_and_retries(self):
        config = {"clientId": "test", "itemIds": ["item"]}
        at = datetime.datetime(2026, 10, 16, 1, tzinfo=datetime.timezone.utc)
        with tempfile.TemporaryDirectory() as directory, patch.object(pluggy, "Client") as factory:
            factory.return_value.snapshot.return_value = self.daily_snapshot(at.isoformat())
            _, path, _ = pluggy.ensure_daily(config, Path(directory), now=at)
            previous = path.read_bytes()
            factory.return_value.snapshot.side_effect = pluggy.PluggyError("HTTP 500")
            for _ in range(2):
                with self.assertRaises(pluggy.PluggyError):
                    pluggy.ensure_daily(config, Path(directory), now=at + datetime.timedelta(days=1))
            self.assertEqual(path.read_bytes(), previous)
            self.assertEqual(factory.call_count, 3)

    def test_changed_connections_do_not_reuse_daily_cache(self):
        at = datetime.datetime(2026, 10, 16, 1, tzinfo=datetime.timezone.utc)
        with tempfile.TemporaryDirectory() as directory, patch.object(pluggy, "Client") as factory:
            factory.return_value.snapshot.return_value = self.daily_snapshot(at.isoformat())
            pluggy.ensure_daily({"clientId": "test", "itemIds": ["item"]}, Path(directory), now=at)
            pluggy.ensure_daily({"clientId": "test", "itemIds": ["other"]}, Path(directory), now=at)
            self.assertEqual(factory.call_count, 2)

    def client(self, responses):
        client = object.__new__(pluggy.Client)
        calls = []

        def request(path):
            calls.append(path)
            return responses.pop(0)

        client.request = request
        return client, calls

    def test_cursor_preserves_server_query_and_collects_all_pages(self):
        client, calls = self.client([
            {"results": [{"id": "a"}], "next": "?accountId=acc&after=x%2By%3D"},
            {"results": [{"id": "b"}], "next": None},
        ])
        self.assertEqual(len(client.collect("/v2/transactions", accountId="acc")), 2)
        self.assertEqual(calls[1], "/v2/transactions?accountId=acc&after=x%2By%3D")

    def test_account_page_pagination(self):
        client, calls = self.client([
            {"results": [{"id": "a"}], "totalPages": 2},
            {"results": [{"id": "b"}], "totalPages": 2},
        ])
        self.assertEqual(len(client.collect("/accounts", itemId="item")), 2)
        self.assertEqual(calls[1], "/accounts?itemId=item&page=2")

    def test_repeated_cursor_fails_instead_of_infinite_loop(self):
        client, _ = self.client([
            {"results": [], "next": "?after=same"},
            {"results": [], "next": "?after=same"},
        ])
        with self.assertRaises(pluggy.PluggyError):
            client.collect("/v2/transactions", accountId="acc")

    def test_foreign_cursor_rejected(self):
        client, _ = self.client([{"results": [], "next": "https://other.test/?after=x"}])
        with self.assertRaises(pluggy.PluggyError):
            client.collect("/v2/transactions", accountId="acc")

    def test_snapshot_does_not_persist_authentication(self):
        client, _ = self.client([
            {"id": "item", "status": "UPDATED"},
            {"results": [{"id": "acc"}], "totalPages": 1},
            {"results": [{"id": "tx"}], "next": None},
        ])
        client.item_ids = ["item"]
        client.api_key = "private-test-token"
        snapshot = client.snapshot()
        self.assertEqual(snapshot["items"][0]["transactions"][0]["id"], "tx")
        self.assertNotIn(client.api_key, json.dumps(snapshot))

    def test_private_snapshot_and_refusal_to_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "snapshot.json"
            pluggy.save_snapshot(path, {"original": True})
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
            with self.assertRaises(FileExistsError):
                pluggy.save_snapshot(path, {"replacement": True})
            self.assertEqual(json.loads(path.read_text()), {"original": True})

    def test_incomplete_collection_leaves_no_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "config.json"
            config.write_text('{}')
            output = Path(directory) / "snapshot.json"
            with patch("sys.argv", ["pluggy.py", "--config", str(config), "--output", str(output)]), \
                 patch.object(pluggy, "Client") as factory, \
                 contextlib.redirect_stderr(io.StringIO()):
                factory.return_value.snapshot.side_effect = pluggy.PluggyError("HTTP 500")
                self.assertEqual(pluggy.main(), 1)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
