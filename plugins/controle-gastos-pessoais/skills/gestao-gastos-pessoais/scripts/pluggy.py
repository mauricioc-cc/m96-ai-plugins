#!/usr/bin/env python3
"""Consulta de leitura da Pluggy; credenciais privadas, fora do repositório."""

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo


DEFAULT_CONFIG = Path.home() / ".config/m96/controle-gastos-pessoais/pluggy.json"
DEFAULT_CACHE = Path.home() / ".cache/m96/controle-gastos-pessoais/pluggy"
BASE_URL = "https://api.pluggy.ai"


class PluggyError(Exception):
    pass


class Client:
    def __init__(self, config):
        self.item_ids = config["itemIds"]
        if not self.item_ids or not all(isinstance(i, str) and i for i in self.item_ids):
            raise PluggyError("Configure ao menos um itemId válido.")
        result = self.request("/auth", payload={
            "clientId": config["clientId"], "clientSecret": config["clientSecret"]
        })
        self.api_key = result["apiKey"]

    def request(self, path, payload=None):
        # A chave nunca é enviada a URLs de paginação fornecidas por outro host.
        if not path.startswith("/") or path.startswith("//") or "://" in path:
            raise PluggyError("Caminho de API inválido.")
        headers = {"Content-Type": "application/json"}
        if hasattr(self, "api_key"):
            headers["X-API-KEY"] = self.api_key
        req = urllib.request.Request(
            BASE_URL + path, headers=headers,
            data=json.dumps(payload).encode() if payload is not None else None,
        )
        # Não seguir redirects com a chave da API.
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                return None
        try:
            with urllib.request.build_opener(NoRedirect).open(req, timeout=45) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            # Corpos e headers de erro podem conter dados privados.
            raise PluggyError(f"HTTP {exc.code} em {path.split('?')[0]}; conteúdo omitido.") from None
        except (urllib.error.URLError, TimeoutError):
            raise PluggyError("Falha de conexão com a Pluggy; tente novamente.") from None

    def collect(self, endpoint, **params):
        query = urllib.parse.urlencode(params)
        cursor = endpoint.startswith("/v2/")
        path = endpoint + "?" + query
        rows, seen = [], set()
        page = 1
        while path:
            if path in seen:
                raise PluggyError("A API repetiu uma página; coleta interrompida.")
            seen.add(path)
            data = self.request(path)
            rows.extend(data["results"])
            if cursor:
                following = data["next"]
                if following is not None and (not isinstance(following, str) or not following.startswith("?")):
                    raise PluggyError("Cursor de paginação inválido.")
                path = endpoint + following if following is not None else None
            else:
                if page >= data["totalPages"]:
                    break
                page += 1
                path = endpoint + "?" + query + "&page=" + str(page)
        return rows

    def snapshot(self):
        items = []
        for item_id in self.item_ids:
            item = self.request("/items/" + urllib.parse.quote(item_id, safe=""))
            accounts = self.collect("/accounts", itemId=item_id)
            transactions = []
            for account in accounts:
                transactions.extend(self.collect("/v2/transactions", accountId=account["id"]))
            items.append({"item": item, "accounts": accounts, "transactions": transactions})
        return {
            "source": "meu-pluggy", "schemaVersion": 1,
            "fetchedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "items": items,
        }


def save_snapshot(path, snapshot):
    # Exclusivo: não sobrescrever uma fonte já arquivada.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(snapshot, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    except BaseException:
        Path(path).unlink(missing_ok=True)
        raise


def ensure_daily(config, cache_dir, timezone="America/Sao_Paulo", force=False, now=None):
    """Só reutilizar captura completa do mesmo dia, usuário e conjunto de itens."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    zone = ZoneInfo(timezone)
    scope = json.dumps([config["clientId"], sorted(config["itemIds"])], sort_keys=True)
    fingerprint = hashlib.sha256(scope.encode()).hexdigest()
    cache_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(cache_dir, 0o700)
    path = cache_dir / (fingerprint + ".json")
    if not force:
        try:
            snapshot = json.loads(path.read_text(encoding="utf-8"))
            fetched = datetime.datetime.fromisoformat(snapshot["fetchedAt"])
            entries = snapshot["items"]
            valid = (
                snapshot["source"] == "meu-pluggy" and snapshot["schemaVersion"] == 1
                and fetched <= now and fetched.astimezone(zone).date() == now.astimezone(zone).date()
                and len(entries) == len(config["itemIds"])
                and sorted(e["item"]["id"] for e in entries) == sorted(config["itemIds"])
                and all(isinstance(e["accounts"], list) and isinstance(e["transactions"], list) for e in entries)
            )
            if valid:
                return snapshot, path, True
        except (OSError, ValueError, KeyError, TypeError):
            pass  # Cache ausente/inválido nunca conta como atualização bem-sucedida.
    snapshot = Client(config).snapshot()
    # Só substituir o cache após concluir a coleta, sem marcar falhas como sucesso.
    fd, temporary = tempfile.mkstemp(prefix=".pluggy-", dir=cache_dir)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(snapshot, stream, ensure_ascii=False)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)
    return snapshot, path, False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output", type=Path, help="JSON original na pasta Fontes já escolhida; não pode existir.")
    parser.add_argument("--ensure-daily", action="store_true", help="Consultar ao menos uma vez por dia; reutilizar captura completa de hoje.")
    parser.add_argument("--force", action="store_true", help="Ignorar cache de hoje e consultar novamente (com --ensure-daily).")
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--timezone", default="America/Sao_Paulo", help="Fuso do usuário para a virada do dia.")
    args = parser.parse_args()
    try:
        with args.config.open(encoding="utf-8") as stream:
            config = json.load(stream)
        cache_path, reused = None, False
        if args.ensure_daily:
            snapshot, cache_path, reused = ensure_daily(config, args.cache_dir, args.timezone, args.force)
        else:
            snapshot = Client(config).snapshot()
        if args.output:
            save_snapshot(args.output, snapshot)
        # Apenas contagens na saída; nunca tokens, saldos ou documentos pessoais.
        print(json.dumps({
            "source": snapshot["source"], "fetchedAt": snapshot["fetchedAt"],
            "items": [{"status": entry["item"].get("status"),
                       "lastUpdatedAt": entry["item"].get("lastUpdatedAt"),
                       "accounts": len(entry["accounts"]),
                       "transactions": len(entry["transactions"])} for entry in snapshot["items"]],
            "saved": bool(args.output),
            "dailyCacheReused": reused,
            "snapshotPath": str(cache_path) if cache_path else None,
        }, ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError, PluggyError) as exc:
        # Erros de configuração também não expõem conteúdo nem valores de credenciais.
        message = str(exc) if isinstance(exc, PluggyError) else "Verifique a configuração privada e o caminho de saída (sem sobrescrita)."
        print(message, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
