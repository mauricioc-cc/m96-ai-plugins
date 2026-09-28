---
name: gestao-gastos-pessoais
description: Manter um registro validado de gastos pessoais em uma planilha no Google Drive ou em um CSV local, conforme a escolha do usuário. Guardar arquivos de origem, normalizar lançamentos, construir categorias próprias, conciliar estornos, evitar duplicatas e consultar gastos e parcelas.
---

# Gestão de gastos pessoais

Usar como base principal dos gastos **uma** das opções escolhidas pelo usuário ao iniciar o controle: uma planilha no Google Drive ou um arquivo CSV local. Reutilizar essa escolha nas operações seguintes; não perguntar a cada importação nem manter as duas bases sincronizadas. Se já houver um controle indicado pelo usuário, continuar nele sem criar outro.

O objetivo é reduzir ao mínimo o trabalho manual: extrair dados dos insumos fornecidos, normalizar os lançamentos e manter a base escolhida atualizada, principalmente com data do gasto, valor e categoria.

## Princípios

- Tratar a planilha ou o CSV escolhido como fonte persistente de verdade dos lançamentos já consolidados.
- Nunca misturar dados de usuários diferentes.
- Não exigir que o usuário edite manualmente a planilha ou o CSV para o fluxo funcionar.
- Guardar os arquivos recebidos como fonte para consulta posterior e consolidar seus gastos na base principal. Um gasto informado apenas em conversa entra na base sem exigir cópia textual da mensagem.
- Preservar o texto original do estabelecimento em um campo próprio e usar campos normalizados separadamente.
- Evitar duplicidades ao importar a mesma fatura, extrato ou comprovante mais de uma vez.
- Manter na base principal somente os lançamentos de gastos resultantes da normalização: sem linhas originais duplicadas, totais, resumos, gráficos ou projeções. Guardar a lista de categorias separada dos lançamentos.
- Diferenciar claramente gasto efetivamente lançado, compra parcelada e projeção futura.
- Não apresentar projeções como se fossem cobranças já realizadas.
- Não transformar o controle de gastos em aconselhamento de investimento, crédito ou endividamento sem pedido explícito.

## Inicialização e localização do controle

Quando ainda não houver um controle escolhido, perguntar ao usuário se prefere planilha no Google Drive ou CSV local. Pedir a localização necessária uma vez na inicialização e reutilizá-la depois. Se houver mais de um controle candidato ou a localização anterior não estiver disponível, pedir que o usuário identifique o controle, sem refazer a escolha do formato nem criar outro por inferência. A troca de formato só ocorre quando o usuário a solicitar.

- **Planilha no Drive:** criar, no Drive do próprio usuário, uma pasta `Controle de Gastos` e uma planilha com o mesmo nome, salvo se ele escolher outro nome ou local. A planilha tem somente as abas `Lançamentos` e `Categorias`, sem gráficos ou abas de resumo. Criar uma subpasta `Fontes` para os arquivos recebidos. Registrar a URL ou o identificador da planilha e da pasta de fontes para reutilização.
- **CSV local:** pedir ao usuário que escolha uma pasta acessível para o controle; pode sugerir uma pasta `Controle de Gastos`. Nela, criar o CSV principal de lançamentos, um `categorias.csv` para a lista própria do usuário e uma subpasta `Fontes` para os arquivos recebidos. Registrar os caminhos para reutilização. Não escolher sozinho um diretório local.

Usar o mesmo modelo de lançamentos nas duas opções, conforme `references/modelo-controle.md`. Na pasta escolhida, manter um `controle.json` apenas com a opção de armazenamento, os identificadores ou caminhos da base, da lista de categorias e da pasta de fontes, e referências às importações pendentes. Ele não contém lançamentos nem valores financeiros. Em uma conversa futura, reutilizar esse arquivo quando a pasta estiver acessível; se não for possível localizar o controle com segurança, pedir sua localização. Em controles existentes, identificar a estrutura real e reutilizar a pasta de fontes já adotada antes de acrescentar campos, criar pastas ou migrar dados.

## Importação de lançamentos

Aceitar como fonte, quando disponíveis:

- faturas de cartão;
- extratos bancários;
- comprovantes;
- arquivos CSV, XLSX ou PDF;
- listas ou tabelas enviadas pelo usuário;
- lançamentos informados diretamente em conversa.

Para cada item:

1. Se o insumo for um arquivo recebido, guardar o original sem alterá-lo na pasta de fontes do controle escolhido e registrar sua localização. Reutilizar a cópia já arquivada quando o mesmo arquivo for enviado de novo. Se o insumo for apenas texto enviado na conversa, não exigir arquivo nem cópia textual.
2. Extrair a data da compra ou transação, descrição original, valor, moeda e demais dados disponíveis. Para uma parcela, preservar também a `Data original da compra` quando conhecida e calcular a `Data do gasto` do seu mês conforme a regra de parcelamento abaixo.
3. Identificar parcelamento quando houver indicação como `01/10`, `1 de 10`, `PARC 1/10` ou equivalente.
4. Normalizar estabelecimento sem apagar a descrição original e validar a categoria segundo `references/categorias.md`, mesmo quando a fonte já trouxer uma categoria.
5. Conciliar possíveis estornos e reembolsos, depois verificar duplicidade contra a base principal, inclusive quando o mesmo arquivo for enviado novamente.
6. Registrar somente os gastos distintos e não anulados na planilha ou no CSV escolhido, vinculando cada lançamento extraído de arquivo à localização do original guardado. Não gravar linhas da fonte sem normalização, pagamentos de fatura como novo gasto nem totais da fonte.
7. Se faltar data, valor ou categoria confiável, pedir os dados necessários ao usuário antes de gravar o lançamento. Para um arquivo recebido, registrar em `controle.json` a referência ao arquivo, as linhas ou itens pendentes e o motivo, sem copiar valores ou lançamentos brutos; retomar pelo original arquivado e retirar a pendência quando resolvida. Para um gasto informado apenas em conversa, não guardar cópia textual: se a conversa não puder ser retomada, pedir que o usuário informe o gasto novamente. Informar as pendências sem apresentar a importação como completa.

Não excluir arquivos de origem após a importação. Se não for possível arquivar um arquivo recebido, informar o problema e resolver o destino da fonte antes de considerar a importação concluída.

## Categorias do usuário

Manter uma lista própria de categorias em `Categorias` na planilha ou em `categorias.csv` ao lado do CSV de lançamentos. Ela contém nomes e critérios de classificação, sem valores financeiros, totais ou gráficos. Não preencher a lista com uma taxonomia genérica por padrão. Acrescentar ou ajustar categorias a partir das escolhas do usuário e de evidências concretas nas descrições dos gastos, conforme `references/categorias.md`.

## Estornos e reembolsos

Um estorno ou reembolso anula um gasto somente quando seu valor absoluto é idêntico ao do lançamento e há evidência de que se referem à mesma transação. Nesse caso, não registrar o estorno ou reembolso como gasto e retirar o gasto anulado da base principal. Antes de retirar um gasto já registrado, criar uma cópia recuperável do controle; os arquivos de origem preservam a evidência da conciliação. Se houver vários gastos candidatos, vínculo incerto ou valor diferente, perguntar ao usuário antes de alterar o registro. Não transformar uma devolução parcial em anulação total.

## Validação e correção do controle

Ao abrir um controle existente e antes e depois de cada importação ou correção, validar a estrutura e os lançamentos contra `references/modelo-controle.md`:

- a aba `Lançamentos` ou o CSV principal contém somente gastos normalizados, sem linhas originais repetidas, totais, subtotais, resumos, projeções ou visualizações;
- as estruturas auxiliares são a lista de categorias e o `controle.json` de localização e pendências; não há gráficos nem abas ou arquivos de valores consolidados mantidos pelo plugin;
- cada gasto tem data, valor e categoria validada que conste na lista própria do usuário; descrição original e referência ao arquivo recebido são preservadas quando disponíveis;
- IDs e outros dados da fonte não apontam para duplicatas comprovadas; gastos iguais em data e valor podem ser compras distintas;
- estornos e reembolsos de mesmo valor são conciliados somente quando o vínculo com o gasto é comprovado.

Quando encontrar inconsistência, criar primeiro uma cópia recuperável do controle atual. Corrigir automaticamente apenas o que puder ser identificado sem ambiguidade, incluindo duplicatas comprovadas e estruturas de resumo ou gráficos gerados pelo plugin. Não apagar lançamentos apenas por semelhança. Para categorias, vínculos de estorno ou linhas cuja natureza seja incerta, apresentar os casos ao usuário e aguardar a resposta antes de modificar essas linhas. Validar novamente após a correção e informar o que foi alterado e o que ficou pendente.

## Compras parceladas

Para compras parceladas, registrar o valor da parcela atual, seu número `n`, o total `N` e, quando conhecida, a data original da compra. Calcular, sem armazenar em colunas próprias, o valor total estimado da compra e as parcelas restantes quando houver dados suficientes.

Para consolidar **gastos por mês** (cartão e conta juntos), salvo pedido explícito por outro critério:

- usar a data da transação para débitos da conta e a data da compra para pagamentos à vista no cartão;
- atribuir a parcela `n/N` ao mês da compra acrescido de `n - 1` meses, inclusive quando a compra ocorreu em ano anterior. Gravar esse mês na única coluna `Data do gasto` da parcela. Se a fonte não informar o dia da parcela, usar como referência o dia da compra no mês calculado (ou o último dia, se o mês for mais curto) e indicar em `Observações` que o dia foi derivado;
- somar apenas o valor de cada parcela efetivamente registrada no seu mês: não lançar o valor integral da compra no mês inicial, não reunir todas as parcelas na data original e não somar novamente o pagamento da fatura;
- não armazenar mês de competência, fatura de cobrança ou data de pagamento no registro de gastos. O arquivo de origem permanece disponível para conferência;
- excluir do total os gastos anulados por estorno ou reembolso conforme a regra acima. Cobranças recorrentes que exibem `n/N` sem representar uma compra parcelada, como uma tarifa mensal, exigem classificação própria, não o deslocamento automático pela fórmula acima.

Se a fonte não permitir distinguir compra, parcela e cobrança com segurança, indicar a lacuna antes de apresentar um total mensal como fechado. Não incluir parcelas futuras apenas previstas nos gastos já realizados.

Quando o usuário pedir projeções:

- somar apenas parcelas futuras ainda previstas;
- mostrar o valor projetado por mês;
- separar projeção de parcelas de outros gastos recorrentes ou variáveis;
- informar quando uma projeção depende de hipóteses.

## Consultas e análises

Responder consultas como:

- total gasto em um período;
- gastos por categoria;
- gastos por estabelecimento;
- gastos com uma descrição específica;
- maiores despesas;
- comparação entre períodos;
- total já comprometido em parcelas futuras;
- projeção de gastos futuros baseada exclusivamente em parcelas registradas.

Para buscas por estabelecimento, considerar descrição original e nome normalizado. Quando o usuário fornecer um padrão, como prefixo ou abreviação, aplicá-lo literalmente e explicar apenas se houver ambiguidade relevante.

Calcular totais, comparações e projeções a partir dos lançamentos quando o usuário pedir, sem gravar resumos, tabelas agregadas ou gráficos na planilha ou no CSV principal.

## Regras de qualidade

- Não duplicar lançamentos já presentes.
- Não alterar valores históricos sem evidência da fonte ou pedido explícito.
- Manter a descrição original da transação.
- Não inferir que um gasto pertence a determinada pessoa apenas pelo nome do cartão sem confirmação suficiente.
- Não registrar transferências entre contas próprias como despesa quando forem identificadas claramente como transferência interna.
- Não registrar estornos, reembolsos, transferências internas ou ajustes como novos gastos. Conciliar estornos e reembolsos conforme a regra de anulação; quando não houver vínculo seguro, pedir orientação ao usuário.
- Para moedas diferentes, preservar o valor e a moeda originais. Converter somente quando houver taxa disponível na própria fonte ou quando o usuário pedir explicitamente.
- Em consultas e resumos, não somar moedas diferentes num mesmo total sem uma conversão autorizada. Apresentar totais separados por moeda; se a moeda de algum lançamento for desconhecida, esclarecer antes de incluí-lo num total monetário.
- Informar inconsistências relevantes encontradas entre os insumos e a base principal.

## Pedidos típicos

- "Crie um controle dos meus gastos no Drive."
- "Crie um controle dos meus gastos em um CSV local."
- "Importe esta fatura para minha planilha."
- "Quanto gastei de Uber este mês?"
- "Quanto gastei com iFood?"
- "Mostre meus gastos por categoria."
- "Quais compras ainda estão parceladas?"
- "Projete meus gastos dos próximos meses considerando só as parcelas que faltam."
- "Registre este comprovante no meu controle."
