# Gmail por evento

## Etiquetas existentes

Usar os nomes reais encontrados na conta. O padrão relatado é:

- `EVENTO`: reserva ainda não respondida;
- `EVENTO OK`: reserva respondida;
- `EVENTO PG`: comprovante recebido.

Não tratar essas etiquetas como estados financeiros completos. Um e-mail em `EVENTO PG` ainda pode corresponder a pagamento parcial ou pendente de conferência.

## Triagem

1. Restringir a busca ao evento e ao período pedido.
2. Shortlistar por remetente, assunto e resumo.
3. Ler a conversa completa antes de classificar.
4. Separar reserva, comprovante, correção, cancelamento, dúvida e mensagem não relacionada.
5. Detectar quando comprovante e correção aparecem no mesmo e-mail.
6. Não usar a presença de anexo como única evidência de comprovante.

## Operação segura

- Ler e resumir sem alterar etiquetas.
- Antes da primeira mudança na conta, mostrar as etiquetas de origem e destino.
- Aplicar mudanças somente após a ação correspondente ter ocorrido.
- Depois de enviar resposta de reserva, usar o comportamento confirmado para `EVENTO OK`.
- Ao receber comprovante, usar `EVENTO PG` conforme o padrão confirmado, sem marcar pagamento integral automaticamente.
- Não criar etiquetas de evento por iniciativa própria.
- Relatar mensagens alteradas, etiquetas aplicadas e exceções.

## Ambiguidade

Quando duas excursões tiverem nomes semelhantes, usar também data, local e conteúdo da conversa. Não mover e-mail quando o evento não estiver inequívoco.
