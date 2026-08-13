# Modelo da planilha

Criar preferencialmente as abas abaixo.

## Lançamentos

Colunas mínimas:

- `ID`
- `Data`
- `Descrição original`
- `Estabelecimento`
- `Categoria`
- `Valor`
- `Moeda`
- `Origem`
- `Conta/Cartão`
- `Parcela atual`
- `Total de parcelas`
- `Valor total da compra`
- `Parcelas restantes`
- `Competência/Fatura`
- `Tipo`
- `Arquivo fonte`
- `Observações`

Valores sugeridos para `Tipo`:

- `Despesa`
- `Estorno`
- `Reembolso`
- `Transferência interna`
- `Ajuste`

O `ID` deve ser estável e servir para evitar duplicidades. Pode ser derivado de uma combinação de data, descrição, valor, origem e dados de parcelamento, mas colisões devem ser verificadas antes da gravação.

## Categorias

Colunas:

- `Categoria`
- `Subcategoria`
- `Palavras-chave`
- `Estabelecimentos conhecidos`
- `Ativa`

Essa aba pode evoluir conforme o comportamento do próprio usuário.

## Parcelamentos

Pode ser uma visão derivada dos lançamentos, sem duplicar a fonte principal. Exibir:

- compra;
- valor da parcela;
- parcela atual;
- total;
- parcelas restantes;
- valor ainda comprometido;
- última competência prevista.

## Resumo

Pode conter fórmulas, tabelas dinâmicas ou gráficos para:

- gasto do mês;
- gasto por categoria;
- gasto por estabelecimento;
- evolução mensal;
- parcelas futuras por competência.

A planilha deve continuar utilizável mesmo que essa aba seja simples ou ainda não esteja configurada.
