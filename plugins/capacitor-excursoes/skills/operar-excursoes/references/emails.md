# E-mails da Capacitor

## Triagem

Classificar cada conversa em: nova reserva, comprovante, correção, dúvida, cancelamento ou não relacionada. Ler a conversa completa quando houver anexos, respostas anteriores ou mais de um passageiro.

Aplicar `gmail.md` antes de alterar etiquetas.

## Nova reserva

Conferir no e-mail:

- evento e data;
- nome completo e documento de cada passageiro;
- telefone;
- ponto de embarque;
- quantidade de pessoas.

Conferir nas fontes do evento:

- preço aplicável a cada cidade;
- parcelamento e prazo;
- horários, pontos e veículo;
- dados para pagamento, regulamento e link do grupo, quando disponíveis.

Pedir somente os dados ausentes. Quando estiver completa:

1. calcular quantidade e total;
2. manter juntos os passageiros do mesmo pedido;
3. usar o modelo já empregado naquele evento ou `../assets/templates/resposta-confirmacao-reserva.txt`;
4. mostrar a resposta completa antes do envio;
5. após o envio autorizado, aplicar a transição para `EVENTO OK` conforme o padrão confirmado.

## Comprovante

1. Relacionar o comprovante ao contato e a todos os passageiros do pedido.
2. Calcular o total esperado considerando que pessoas do mesmo grupo podem pagar de formas diferentes.
3. Extrair valor e data somente quando estiverem legíveis.
4. Tratar `EVENTO PG` como comprovante recebido.
5. Usar `pagamentos.md` antes de sugerir `#`, `/` ou `@`.
6. Mostrar exceções para conferência manual.

## Correção, troca ou cancelamento

Exigir o pedido por e-mail, como Frederico já faz. Não executar alteração recebida somente por conversa de WhatsApp. Identificar passageiro, evento, dado anterior e novo dado antes de editar a lista.

## Redação e envio

- Preservar o tom expansivo, títulos, blocos, emojis e assinatura encontrados nos modelos reais.
- Não misturar dados de eventos diferentes.
- Não reutilizar preço, horário, embarque ou link antigo sem confirmação.
- Usar revisão como padrão.
- Enviar somente após escolha explícita de Frederico.
- Depois do envio, informar destinatário, assunto e etiqueta aplicada.
