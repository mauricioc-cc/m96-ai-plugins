# Modelo do controle de gastos

Aplicar os mesmos campos de lançamentos à aba `Lançamentos` da planilha no Drive ou ao CSV local. Essa base contém apenas gastos normalizados e vigentes; arquivos originais ficam na pasta de fontes. Não armazenar linhas brutas, estornos, reembolsos, transferências internas, ajustes, totais, projeções ou resumos como gastos.

## Lançamentos

Campos do controle:

- `ID`
- `Data do gasto`
- `Data original da compra`
- `Descrição original`
- `Estabelecimento`
- `Categoria`
- `Valor`
- `Moeda`
- `Conta/Cartão`
- `Parcela atual`
- `Total de parcelas`
- `Arquivo fonte`
- `Observações`

Quando o controle existente tiver a coluna `Tipo`, os lançamentos mantidos nela são gastos (`Despesa`). Os demais tipos são insumos para conciliação, não linhas de gasto na base principal.

O `ID` deve ser estável e servir para evitar duplicidades. Pode ser derivado de uma combinação de data do gasto, data original da compra quando houver, descrição, valor, arquivo fonte ou conta/cartão e dados de parcelamento, mas colisões devem ser verificadas antes da gravação.

`Data do gasto`, `Valor` e `Categoria` validada são obrigatórios para cada gasto. `Data original da compra` é opcional e só se aplica a compras parceladas. Preencher os demais campos quando houver informação suficiente; não inventar dados ausentes. `Conta/Cartão` é opcional e ajuda a distinguir compras semelhantes. Em `Arquivo fonte`, guardar a localização do original arquivado para lançamentos extraídos de arquivos. Gastos informados apenas em conversa podem deixar esse campo vazio.

Para a parcela `n/N`, `Data do gasto` fica no mês da compra acrescido de `n - 1` meses. Se o dia exato da parcela não constar da fonte, a data registrada é uma referência derivada e isso deve constar em `Observações`; não apresentá-la como data real da cobrança. Não criar campos de fatura, mês de competência, valor total da compra ou parcelas restantes. Calcular os dois últimos quando solicitados e quando houver dados suficientes. Em controles existentes, não retirar colunas nem alterar valores históricos silenciosamente.

No CSV, manter cabeçalho e formato consistentes entre importações, preservar os gastos vigentes e atualizar o arquivo escolhido pelo usuário. Uma nova importação não substitui o histórico sem conciliação; cópias de segurança preservam o estado anterior às correções. Consultas e análises leem esse CSV; ele não é uma exportação secundária da planilha.

## Lista própria de categorias

Manter somente nomes e critérios de classificação em uma aba `Categorias` da planilha ou em `categorias.csv` ao lado do CSV principal. Não há valores de gastos nem resumos nessa lista. Campos:

- `Categoria`
- `Critério de uso`
- `Origem da definição`

Iniciar sem categorias impostas pelo plugin. Criar ou ajustar a lista com o usuário e a partir de evidências concretas dos gastos. A categoria atribuída a cada lançamento continua na base principal.

## Parcelamentos

Calcular a visão a partir dos lançamentos quando solicitada, sem criar aba ou arquivo de parcelas. Exibir na resposta:

- compra;
- valor da parcela;
- parcela atual;
- total;
- parcelas restantes;
- valor ainda comprometido;
- último mês previsto.

## Resumos e projeções

Calcular a partir dos lançamentos quando o usuário pedir, sem criar abas, arquivos de valores consolidados ou gráficos na base:

- gasto do mês, com cada parcela no seu mês;
- gasto por categoria;
- gasto por estabelecimento;
- evolução mensal;
- parcelas futuras por mês.

Na planilha, manter somente `Lançamentos` e `Categorias`. No modo local, manter o CSV principal e `categorias.csv` como arquivos estruturados do controle.

## Metadados do controle

Manter `controle.json` na pasta escolhida, no Drive ou localmente, apenas para registrar o formato escolhido, as referências à base, às categorias e à pasta de fontes, e importações pendentes identificadas por arquivo e posição da linha ou item. Não copiar gastos, valores, descrições integrais nem resumos para esse arquivo. Resolver pendências reabrindo o original guardado; um gasto enviado só em conversa não exige arquivo ou registro permanente de pendência.
