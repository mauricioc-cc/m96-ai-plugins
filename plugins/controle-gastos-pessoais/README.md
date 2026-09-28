# controle-gastos-pessoais

Plugin para controle de gastos pessoais em uma planilha no Google Drive ou em um CSV local, conforme a escolha do usuário no início do controle. Arquivos recebidos são guardados como fontes; a base escolhida mantém somente gastos normalizados e validados. O plugin verifica e corrige inconsistências recuperáveis e consulta o usuário quando a correção é ambígua.

## Estrutura

- `.codex-plugin/plugin.json`: manifesto do plugin
- `skills/gestao-gastos-pessoais/SKILL.md`: fluxo principal
- `skills/gestao-gastos-pessoais/references/modelo-controle.md`: modelo de dados das duas opções
- `skills/gestao-gastos-pessoais/references/categorias.md`: classificação e lista própria de categorias

O plugin opera principalmente via conversa, sem exigir edição manual da planilha ou do CSV. A base escolhida é reutilizada nas operações seguintes; um `controle.json` na pasta registra sua localização e eventuais importações pendentes, sem copiar valores de gastos. A lista de categorias fica numa aba `Categorias` ou num `categorias.csv`, sem valores consolidados. Gastos informados apenas por conversa entram no controle sem cópia textual da mensagem.
