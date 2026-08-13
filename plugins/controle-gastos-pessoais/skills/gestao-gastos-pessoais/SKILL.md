---
name: gestao-gastos-pessoais
description: Organizar gastos pessoais do usuário em uma planilha no Google Drive, importar lançamentos de faturas, extratos e comprovantes, categorizar despesas, acompanhar compras parceladas, consolidar gastos por período e produzir análises simples. Usar quando o usuário quiser montar ou manter um controle pessoal de despesas, registrar novos gastos, entender para onde o dinheiro está indo, consultar gastos por estabelecimento ou categoria, acompanhar parcelas futuras ou projetar valores já comprometidos em próximas faturas.
---

# Gestão de gastos pessoais

Usar Google Drive e Google Sheets como armazenamento principal do controle financeiro do próprio usuário.

O objetivo é reduzir ao mínimo o trabalho manual: sempre que possível, extrair dados de faturas, extratos, comprovantes e mensagens fornecidas pelo usuário, normalizar os lançamentos e manter a planilha atualizada.

## Princípios

- Tratar a planilha como fonte persistente de verdade dos lançamentos já consolidados.
- Nunca misturar dados de usuários diferentes.
- Não exigir que o usuário edite manualmente a planilha para o fluxo funcionar.
- Preservar o texto original do estabelecimento em um campo próprio e usar campos normalizados separadamente.
- Evitar duplicidades ao importar a mesma fatura, extrato ou comprovante mais de uma vez.
- Diferenciar claramente gasto efetivamente lançado, compra parcelada e projeção futura.
- Não apresentar projeções como se fossem cobranças já realizadas.
- Não transformar o controle de gastos em aconselhamento de investimento, crédito ou endividamento sem pedido explícito.

## Inicialização

Quando o usuário ainda não tiver uma planilha de controle:

1. Criar, no Google Drive do próprio usuário, uma pasta chamada `Controle de Gastos`, salvo se ele escolher outro nome ou local.
2. Dentro dela, criar uma planilha chamada `Controle de Gastos`.
3. Criar também uma subpasta `Comprovantes e Faturas` para armazenar arquivos usados como fonte, quando o usuário pedir que eles sejam guardados.
4. Preparar a planilha conforme `references/modelo-planilha.md`.
5. Registrar a URL ou o identificador da planilha durante a execução para reutilizá-la nas operações seguintes da conversa.
6. Se existirem várias planilhas candidatas, preferir a explicitamente indicada pelo usuário; não sobrescrever controles existentes por inferência.

## Importação de lançamentos

Aceitar como fonte, quando disponíveis:

- faturas de cartão;
- extratos bancários;
- comprovantes;
- arquivos CSV, XLSX ou PDF;
- listas ou tabelas enviadas pelo usuário;
- lançamentos informados diretamente em conversa.

Para cada item:

1. Extrair data, descrição original, valor, moeda, origem e demais dados disponíveis.
2. Identificar parcelamento quando houver indicação como `01/10`, `1 de 10`, `PARC 1/10` ou equivalente.
3. Normalizar estabelecimento sem apagar a descrição original.
4. Sugerir categoria segundo `references/categorias.md`.
5. Verificar possível duplicidade contra lançamentos já registrados.
6. Registrar somente depois de haver evidência suficiente de que o lançamento é distinto.
7. Quando a categoria estiver incerta, usar `Outros` ou manter uma marca de revisão; não inventar natureza da compra apenas pelo estabelecimento.

## Compras parceladas

Para compras parceladas, registrar:

- valor da parcela atual;
- número da parcela atual;
- total de parcelas;
- valor total da compra quando puder ser inferido com segurança;
- quantidade de parcelas restantes;
- meses/faturas futuras afetadas.

Quando o usuário pedir projeções:

- somar apenas parcelas futuras ainda previstas;
- mostrar o valor projetado por mês ou por fatura;
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
- projeção de faturas futuras baseada exclusivamente em parcelas registradas.

Para buscas por estabelecimento, considerar descrição original e nome normalizado. Quando o usuário fornecer um padrão, como prefixo ou abreviação, aplicá-lo literalmente e explicar apenas se houver ambiguidade relevante.

## Visualizações

Quando o ambiente permitir gráficos ou tabelas interativas, preferir:

- barras para gastos por categoria;
- linha ou barras para evolução mensal;
- barras por mês/fatura para projeções de parcelas;
- tabela para detalhamento de compras parceladas.

Sempre acompanhar visualizações com os totais principais em texto.

## Regras de qualidade

- Não duplicar lançamentos já presentes.
- Não alterar valores históricos sem evidência da fonte ou pedido explícito.
- Manter a descrição original da transação.
- Não inferir que um gasto pertence a determinada pessoa apenas pelo nome do cartão sem confirmação suficiente.
- Não registrar transferências entre contas próprias como despesa quando forem identificadas claramente como transferência interna.
- Estornos e reembolsos devem reduzir o gasto correspondente quando puderem ser relacionados; caso contrário, registrar separadamente.
- Para moedas diferentes, preservar o valor e a moeda originais. Converter somente quando houver taxa disponível na própria fonte ou quando o usuário pedir explicitamente.
- Informar inconsistências relevantes encontradas entre documentos e a planilha.

## Pedidos típicos

- "Crie um controle dos meus gastos no Drive."
- "Importe esta fatura para minha planilha."
- "Quanto gastei de Uber este mês?"
- "Quanto gastei com iFood?"
- "Mostre meus gastos por categoria."
- "Quais compras ainda estão parceladas?"
- "Projete minhas próximas faturas considerando só as parcelas que faltam."
- "Registre este comprovante no meu controle."
