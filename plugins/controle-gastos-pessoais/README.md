# controle-gastos-pessoais

Plugin para controle de gastos pessoais em uma planilha no Google Drive ou em um CSV local, conforme a escolha do usuário no início do controle. Meu Pluggy é a fonte prioritária para transações atuais; arquivos, extratos e conversa complementam o histórico. A base escolhida mantém somente gastos normalizados e validados. O plugin verifica e corrige inconsistências recuperáveis e consulta o usuário quando a correção é ambígua.

## Estrutura

- `.codex-plugin/plugin.json`: manifesto do plugin
- `skills/gestao-gastos-pessoais/SKILL.md`: fluxo principal
- `skills/gestao-gastos-pessoais/references/modelo-controle.md`: modelo de dados das duas opções
- `skills/gestao-gastos-pessoais/references/categorias.md`: classificação e lista própria de categorias
- `skills/gestao-gastos-pessoais/references/meu-pluggy.md`: configuração privada, consulta, prioridade e conciliação da API
- `skills/gestao-gastos-pessoais/scripts/pluggy.py`: coleta de leitura, com paginação completa, sem dependências externas

O plugin opera principalmente via conversa, sem exigir edição manual da planilha ou do CSV. A base escolhida é reutilizada nas operações seguintes; um `controle.json` na pasta registra sua localização e eventuais importações pendentes, sem copiar valores de gastos. A lista de categorias fica numa aba `Categorias` ou num `categorias.csv`, sem valores consolidados. Gastos informados apenas por conversa entram no controle sem cópia textual da mensagem.

## Meu Pluggy

A integração é opcional. Sem credenciais, o plugin oferece conectar Meu Pluggy ou continuar apenas com comprovantes, faturas e extratos. Só solicita os dados de acesso se o usuário escolher conectar e não repete a oferta a cada importação.

Guardar `clientId`, `clientSecret` e `itemIds` em `~/.config/m96/controle-gastos-pessoais/pluggy.json`, fora do repositório (pasta `0700`, arquivo `0600`). Essa configuração é reutilizada no mesmo ambiente; não é distribuída com o plugin. O esquema, sem valores reais, está em `references/meu-pluggy.md` dentro da skill. Não é necessário instalar um MCP. Contas Meu Pluggy exigem os IDs conhecidos das conexões, pois não permitem listar itens.

Verificar acesso e contagem de contas/transações:

```bash
python plugins/controle-gastos-pessoais/skills/gestao-gastos-pessoais/scripts/pluggy.py --ensure-daily
```

Para importar, usar `--output` com um nome novo na pasta `Fontes` do controle já escolhido. O script arquiva contas, item e todas as páginas de transações; não grava credenciais nem altera lançamentos. A skill faz a normalização e conciliação, usando IDs estáveis para evitar duplicatas, preservando fontes anteriores e respeitando categorias, estornos e parcelas. Atualizações de registros consolidados exigem backup e evidência. A consulta não força uma nova sincronização bancária: considerar sempre o status e a data da última coleta.

Validação automatizada:

```bash
python -m unittest discover -s plugins/controle-gastos-pessoais/tests
```

Em cada ativação com Meu Pluggy configurado, o plugin verifica uma captura completa ao menos uma vez no dia (fuso do usuário) antes de responder e concilia os dados antes das respostas sobre gastos. Cache diário não equivale a importação concluída nem a nova sincronização bancária. Use `--ensure-daily --force` para consultar novamente no mesmo dia.
