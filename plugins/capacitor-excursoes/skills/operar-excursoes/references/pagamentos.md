# Pagamentos e comprovantes

## Símbolos

- `#`: pago total.
- `/`: pago parcial.
- `@`: não pago.

Usar exatamente o estilo do TXT real, inclusive textos como `OK PAGO`, valor e data.

## Reserva com várias pessoas

Relacionar o pagamento ao pedido original, que contém os dados de todos os passageiros. Calcular o total esperado por passageiro e pelo grupo. Permitir que pessoas do mesmo grupo usem modalidades diferentes, registrando a divisão conforme o padrão encontrado.

## Conferência

1. Confirmar evento e pagador.
2. Localizar os passageiros associados.
3. Calcular o valor esperado com os preços confirmados do evento.
4. Ler valor e data do comprovante quando legíveis.
5. Comparar recebido e esperado.
6. Classificar como candidato a total, parcial ou pendente.
7. Mostrar a sugestão para Frederico confirmar antes de editar o TXT.

Frederico normalmente faz conferência visual rápida. Quando percebe comportamento fora do comum, consulta o extrato. Próximo ao evento, revisa em lote os pagamentos. O plugin deve destacar casos para essa conferência, não alegar acesso ao extrato.

## Ordem e veículo

Mostrar reservas em ordem de chegada junto com pagamento e capacidade. Não mover automaticamente quem demorou a pagar. Sinalizar quem está pendente ou parcial e deixar Frederico decidir se a pessoa perde posição ou vai para veículo extra.

## Valores

Os preços históricos por cidade servem apenas como contexto. Sempre confirmar os valores da excursão atual antes de calcular ou responder.
