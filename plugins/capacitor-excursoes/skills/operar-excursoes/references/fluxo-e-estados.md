# Fluxo e estados da operação

## Fontes

- Gmail: solicitações, comprovantes, correções, dúvidas e cancelamentos.
- Cadastro do evento: informações comerciais e logísticas confirmadas.
- Lista operacional TXT: registro acumulado das reservas.
- Lista final TXT: manifesto entregue à transportadora.

Quando as fontes divergirem, não escolher silenciosamente. Mostrar a divergência e pedir decisão quando ela alterar vaga, pagamento, documento, veículo, horário ou embarque.

## Dados do evento

Registrar, quando disponíveis:

- nome, data, local e endereço;
- links do evento e dos ingressos;
- preço, parcelamento, prazo e instruções de pagamento;
- cidades, pontos, endereços e horários de encontro e partida;
- veículos, responsáveis e capacidade;
- regras, recomendações e informações de contato.

## Dados da reserva

Registrar por passageiro:

- identificador interno;
- nome completo;
- documento;
- telefone e e-mail;
- responsável pelo contato e grupo da reserva;
- ponto de embarque;
- estado da reserva;
- valor esperado, recebido e data;
- referência do e-mail ou comprovante;
- autorização para grupo de WhatsApp;
- correções, cancelamento e notas manuais.

## Estados provisórios

Usar estes estados como esqueleto até Frederico confirmar as regras definitivas:

- `PENDENTE_DADOS`: faltam dados necessários.
- `RESERVADO`: vaga registrada, sem pagamento confirmado.
- `AGUARDANDO_PAGAMENTO`: instruções enviadas e pagamento pendente.
- `PAGAMENTO_EM_ANALISE`: comprovante recebido, ainda não validado.
- `PAGO`: pagamento confirmado.
- `CORRECAO_PENDENTE`: há divergência que impede fechar o cadastro.
- `CANCELADO`: reserva cancelada.
- `LISTA_FINAL`: passageiro incluído no manifesto operacional.

Não presumir que "reserva confirmada" e "pagamento confirmado" são equivalentes.

## Regras de atualização

1. Vincular a mensagem à excursão correta.
2. Vincular passageiros do mesmo pedido sem fundir cadastros individuais.
3. Detectar duplicidade por combinação de evento, nome, documento, e-mail e telefone; não depender de um único campo quando houver conflito.
4. Guardar a informação anterior como nota quando uma correção material for aplicada.
5. Marcar comprovante recebido antes de marcar pagamento confirmado, salvo regra explícita de Frederico.
6. Não remover cancelados do histórico operacional; excluí-los da lista final e registrar o motivo quando informado.
