# WhatsApp para leads

Gerar uma mensagem que facilite uma resposta genuína. Não prometer taxa de resposta nem usar pressão, manipulação ou falsa urgência.

## Elegibilidade do contato

- Usar somente o telefone fornecido pelo lead ou pelo formulário de contato ligado à consulta imobiliária.
- Não gerar link quando houver pedido de descadastramento, recusa de contato ou dúvida sobre a origem do número.
- Remover espaços, parênteses, hífens e outros sinais do telefone.
- Preservar o código de país quando estiver informado.
- Para telefone brasileiro sem código de país, aceitar apenas 10 ou 11 dígitos e prefixar `55`.
- Para telefone já iniciado por `55`, aceitar 12 ou 13 dígitos.
- Quando o número não atender a essas condições, identificá-lo como não validado e não criar link.

## Redação

- Escrever em português brasileiro natural, cordial e direto.
- Manter entre 35 e 70 palavras, preferencialmente em 2 a 4 frases curtas.
- Identificar o corretor pelo nome quando essa informação estiver disponível.
- Mencionar o imóvel, anúncio, bairro ou preferência que originou o contato.
- Responder brevemente à pergunta do lead quando houver uma resposta confirmada.
- Encerrar com uma única pergunta simples, específica e fácil de responder.
- Preferir perguntas que avancem a conversa, como confirmar se o interesse continua ou escolher entre dois próximos passos realmente disponíveis.
- Evitar mensagens genéricas, textos longos, excesso de emojis, linguagem artificial, pressão e frases como "última oportunidade".
- Não mencionar que o lead foi pontuado, priorizado ou analisado por IA.

## Link

1. Converter o telefone validado para apenas dígitos no padrão internacional, sem `+`.
2. Codificar integralmente a mensagem em URL encoding UTF-8.
3. Montar `https://wa.me/TELEFONE?text=MENSAGEM_CODIFICADA`.
4. Entregar, para cada lead, o texto visível e um link Markdown identificado como `Abrir no WhatsApp`.
5. Informar que o link abre uma composição para revisão e não envia a mensagem.
