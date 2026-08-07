# Envio automático de e-mails

Permitir o envio sem prévia somente como uma autorização explícita e delimitada do corretor. O padrão permanece sendo revisar cada e-mail antes do envio.

## Ativação

Ativar quando o pedido combinar claramente as duas condições:

1. dispensar a revisão, com linguagem como `não quero revisar`, `pode enviar sem me mostrar antes` ou `envie automaticamente`;
2. definir o conjunto autorizado, como os leads priorizados de hoje, os cinco selecionados ou uma lista nominal inequívoca.

Não ativar por silêncio, pressa presumida, autorização anterior ou frases vagas como `pode preparar tudo`. Se a intenção de enviar ou o conjunto estiver ambíguo, pedir somente a confirmação que falta.

A autorização vale apenas para aquela execução e aquele conjunto. Não reutilizá-la em pedidos futuros nem incluir leads descobertos depois.

## Antes e durante o envio

- Aplicar todas as regras de elegibilidade, contextualização, destinatário e conteúdo do modo revisado.
- Verificar o histórico para evitar contato duplicado ou nova mensagem quando já houve resposta adequada sem manifestação posterior.
- Usar somente o endereço validado do lead. Nunca enviar para o remetente automático do Hinc ou de outro sistema.
- Não enviar quando o endereço estiver ausente, inválido ou ambíguo; quando houver pedido para não ser contatado; ou quando informações essenciais exigirem confirmação.
- Não ampliar o conjunto autorizado para aproveitar outros leads encontrados durante a busca.
- Se uma tentativa falhar, não afirmar que foi enviada e não repetir automaticamente quando houver risco de duplicação.

## Relatório obrigatório após a execução

Depois de concluir as tentativas, informar separadamente:

### Enviados

Para cada e-mail enviado, mostrar:

- nome ou identificador do lead;
- destinatário exato;
- assunto;
- corpo integral exatamente como enviado;
- confirmação de envio retornada pelo Gmail, quando disponível.

### Não enviados

Para cada contato autorizado que não foi enviado, mostrar:

- nome ou identificador;
- motivo objetivo;
- ação necessária para permitir uma nova tentativa.

Não resumir o corpo nem omitir destinatários no relatório, mesmo em lote. O relatório serve para ciência do corretor depois do envio e não substitui a autorização explícita que ativou o modo.
