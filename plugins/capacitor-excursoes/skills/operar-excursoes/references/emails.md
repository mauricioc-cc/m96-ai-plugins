# E-mails da Capacitor

## Classificação

Classificar cada conversa em uma categoria principal:

- nova reserva;
- comprovante de pagamento;
- correção de dados;
- dúvida;
- cancelamento ou desistência;
- não relacionado à excursão.

Ler a conversa completa quando houver mensagens anteriores, anexos, correções ou mais de um passageiro.

## Nova reserva

Conferir:

- excursão e data;
- nome completo e documento de cada passageiro;
- telefone;
- ponto de embarque;
- quantidade de vagas;
- disponibilidade e condições confirmadas no cadastro do evento.

Se faltar dado essencial, pedir apenas o que falta. Se estiver completa, usar `../assets/templates/resposta-confirmacao-reserva.txt` como base e preencher somente informações confirmadas.

## Comprovante

1. Confirmar a excursão e o grupo de passageiros ao qual o comprovante se refere.
2. Extrair valor, data e identificação somente quando legíveis.
3. Registrar como recebido antes de confirmar como pago, até que a regra de validação seja definida.
4. Preparar confirmação curta ou pedido de esclarecimento.
5. Verificar se o e-mail também contém correções.

## Correção

Repetir de forma objetiva o dado anterior e o novo dado. Não alterar documento, nome, embarque ou quantidade de vagas quando a mensagem for ambígua.

## Redação

- Preservar o tom cordial, expansivo e característico da Capacitor.
- Manter títulos, blocos e destaques usados nos modelos TXT.
- Reaproveitar as informações completas da excursão sem misturar eventos.
- Calcular quantidade e total explicitamente; mostrar a conta quando houver parcelamento ou valor diferente.
- Usar placeholders quando qualquer dado comercial ou logístico ainda não estiver confirmado.
- Não copiar dados bancários, documentos empresariais, telefones ou endereços de um evento fictício para outro.

## Envio

Usar revisão como padrão. Enviar sem prévia somente se Frederico:

1. disser explicitamente que não quer revisar;
2. definir o conjunto exato de mensagens;
3. autorizar o envio naquela execução.

Depois, relatar enviados e não enviados separadamente.
