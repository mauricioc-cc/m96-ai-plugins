# Meu Pluggy como fonte prioritária

## Configuração privada e reutilização

Usar a API `https://api.pluggy.ai`, independentemente da instalação de um MCP.
O conector MCP de documentação não substitui estas consultas financeiras.
Reutilizar `~/.config/m96/controle-gastos-pessoais/pluggy.json` no mesmo ambiente,
ou o caminho explicitamente indicado pelo usuário via `--config`. O arquivo é
privado (modo `0600`, pasta `0700`) e fica fora do repositório:

```json
{
  "clientId": "<client id>",
  "clientSecret": "<client secret>",
  "itemIds": ["<id da conexão>"]
}
```

Nunca versionar credenciais, imprimir seu conteúdo, copiá-las para fontes,
planilhas, CSVs, `controle.json` ou respostas. Ler o arquivo apenas dentro do
processo que consulta a API. Guardar nele as credenciais quando o usuário
autorizar; não sobrescrever configuração de outra pessoa. Não pedir novamente
credenciais já configuradas. O arquivo persiste neste ambiente; não supor que
exista em outro computador ou ambiente novo.

Na ausência do arquivo, oferecer conectar Meu Pluggy ou seguir apenas com comprovantes, faturas, extratos e conversa. Se o usuário escolher conectar, solicitar `clientId`, `clientSecret` e os IDs de suas conexões e explicar que serão guardados na configuração privada deste ambiente. Se preferir não conectar, continuar normalmente com as fontes manuais; não repetir a solicitação a cada importação. Falta de credenciais não é erro nem bloqueio para o controle.

`POST /auth` troca clientId/clientSecret por apiKey. Manter essa chave somente
em memória e renová-la nas próximas execuções. Não criar conexões ou solicitar
sincronizações: as consultas usam os dados já coletados pela Pluggy.
Contas Meu Pluggy não podem listar conexões com `GET /v2/items` (403); usar os
`itemIds` configurados. Se faltar um ID, solicitar somente o da nova conexão.

## Consulta e arquivamento

Executar o script a partir desta skill (Python 3, sem dependências externas):

```bash
python scripts/pluggy.py --ensure-daily
python scripts/pluggy.py --output '/pasta/do/controle/Fontes/pluggy-AAAA-MM-DDTHHMMSS.json'
```

Sem `--ensure-daily` e sem `--output`, consultar e mostrar apenas contagens, sem gravar dados. O modo diário usa o cache privado descrito abaixo. Com
`--output`, salvar um snapshot completo dos itens, contas e todas as páginas de
transações. Escolher nome único; o script recusa sobrescritas e só grava após
concluir todas as consultas. Não mudar automaticamente a base principal.
Para controle no Drive, preparar a captura em arquivo temporário privado,
enviá-la para a pasta `Fontes` já adotada e usar a referência do Drive na base.
Não considerar a importação completa se o arquivamento não terminar.

Endpoints usados:

- `GET /items/{id}`: status, produtos e data da última coleta.
- `GET /accounts?itemId=...`: contas, cartões e saldos; paginar até `totalPages`.
- `GET /v2/transactions?accountId=...`: transações de cada conta/cartão; seguir
  `next` até `null`, sem reconstruir o cursor. Não usar `/transactions`, obsoleto.

O script cobre os insumos do controle de despesas. Investimentos, identidade,
empréstimos e outros produtos não entram automaticamente nessa coleta ou na
base de despesas; só consultá-los quando necessários ao pedido do usuário.
Não persistir identidade nem saldos em linhas de gastos.

## Prioridade e conciliação

Consultar Meu Pluggy antes de importar fontes complementares, quando houver
configuração e acesso. Sua prioridade vale para o estado atual de uma mesma
transação comprovadamente identificada, não como garantia de completude.
Considerar o status do item, a última coleta, o período coberto e o status das
transações. Informar dados antigos, pendentes, falhas e páginas incompletas.
Não confundir o horário da consulta com o da atualização bancária.

Preservar arquivos/extratos e gastos informados em conversa para complementar
histórico e dados ausentes. Falha de acesso não impede usar essas fontes;
informar a indisponibilidade sem substituir dados por zeros. Não apagar gastos
porque deixaram de aparecer: janelas de histórico e consentimentos variam.

- Usar `pluggy:<itemId>:<transactionId>` como ID estável do lançamento.
- Guardar a captura JSON em `Fontes` e sua referência em `Arquivo fonte`.
  Pendências em `controle.json` podem referenciar o snapshot e ID da transação,
  sem copiar dados financeiros. Segredos ficam apenas na configuração privada.
- Reimportar o mesmo ID não cria outra despesa. Mudanças comprovadas da API
  podem atualizar o gasto após backup e validação; preservar a fonte anterior.
- Para cruzar lançamentos de arquivo com API, conferir conta/cartão, moeda,
  data, valor, descrição e parcela. Só unir correspondências inequívocas;
  semelhança de data e valor não prova duplicidade. Se houver conflito ambíguo,
  perguntar antes de alterar; preservar o ID já adotado e registrar o ID da API
  em `Observações` para reconhecer consultas seguintes.
- Incluir compras e parcelas como gastos independentemente do status `PENDING`
  ou `POSTED`. Fatura aberta não impede contabilizar uma compra informada pela
  API. O status pode constar em Observações, mas não bloqueia a importação,
  não exclui valores dos totais nem cria, sozinho, pendência de conciliação.
- Registrar parcelas futuras explicitamente retornadas pela API na própria
  Data do gasto, conforme a regra de parcelamento da skill. Não somá-las ao
  mês atual nem fabricar parcelas ausentes: parcelas contratadas informadas
  pela fonte são distintas de projeções calculadas sem lançamento na fonte.
- A mudança de `PENDING` para `POSTED` atualiza o mesmo lançamento; nunca
  incluir status, data da consulta ou fatura na chave de deduplicação.
- A categoria da API é sugestão; validar pelas categorias próprias do usuário.
- Em conta corrente, confirmar o sentido débito/crédito pelos campos da API.
  Em cartão, valores positivos aumentam a dívida; negativos reduzem a dívida.
  Não interpretar todo valor positivo como receita nem todo negativo como gasto.
- Excluir pagamentos da fatura, transferências próprias, receitas e ajustes do
  registro de despesas. Conciliar estornos conforme a skill, sem excluir gastos
  sem vínculo comprovado.
- Preservar metadados de parcelamento. Usar data original da compra somente
  quando comprovada: não deslocar novamente uma data que já represente a parcela.
  Em caso de ambiguidade, manter pendência antes de fechar o mês.

Referências oficiais: [autenticação e API](https://docs.pluggy.ai/en/reference),
[transações e paginação](https://docs.pluggy.ai/en/reference/transaction/transactions-list-by-cursor).

## Verificação diária

A chamada obrigatória em cada ativação é `python scripts/pluggy.py --ensure-daily`.
Ela guarda uma captura bruta privada em `~/.cache/m96/controle-gastos-pessoais/pluggy/`,
separada por aplicação e conjunto de itens. É um cache de fonte, não uma segunda
base de gastos. O script informa `snapshotPath`, `fetchedAt`, `dailyCacheReused` e
`lastUpdatedAt` de cada item. Não há credenciais no cache. Arquivar a captura em
`Fontes` antes da importação e usar essa referência permanente nos lançamentos;
o cache pode ser substituído na próxima consulta.

Usar o fuso do usuário em `--timezone` (padrão `America/Sao_Paulo`). Reutilizar
somente captura completa do mesmo dia; virada do dia, cache inválido ou mudança
nas conexões exigem consulta. `--ensure-daily --force` atende atualização
imediata. Falhas não substituem o cache anterior nem passam a valer como sucesso.
Ter captura recente não garante banco recente nem base conciliada: validar o
status e a coleta bancária e processar importações pendentes antes de responder.
Não forçar sincronização ou criar agendamento em segundo plano.

Em comparações, usar o mesmo intervalo de Data do gasto nos dois meses. O dia
derivado de uma parcela é referência de alocação, não prova de liquidação.
Pendências reais são dados ausentes, categorias incertas, conflitos ou estornos
sem vínculo seguro; o status `PENDING` por si só não é uma pendência.
