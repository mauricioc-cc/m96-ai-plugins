---
name: triagem-leads-gmail
description: Localizar, analisar, deduplicar e priorizar leads imobiliários recebidos no Gmail, além de recomendar o próximo passo e preparar contatos por e-mail, WhatsApp ou telefone. Usar quando um corretor pedir para trabalhar leads de hoje, da semana, do mês ou de outro período, descobrir quem responder primeiro, recuperar contatos antigos, preparar respostas ou solicitar autorização para uma ligação.
---

# Triagem de leads imobiliários no Gmail

Usar as ferramentas do Gmail para pesquisar, ler e criar rascunhos. Se o Gmail não estiver conectado, orientar o usuário a conectar a própria conta antes de continuar.

## Fluxo

1. Confirmar apenas o necessário quando o pedido não trouxer região, empreendimento, tipo de imóvel prioritário ou quantidade máxima de leads. Não perguntar o período quando ele estiver ausente; aplicar o padrão.
2. Interpretar o período pedido pelo usuário:
   - `hoje`: usar o dia atual no fuso do usuário;
   - `última semana`: usar os últimos 7 dias, incluindo hoje;
   - `mês`: usar o mês civil atual;
   - datas informadas: respeitar exatamente o intervalo;
   - sem período: usar os últimos 7 dias, incluindo hoje.
   Na ausência de quantidade, apresentar os 10 melhores leads.
3. Pesquisar mensagens com sinais de portal imobiliário, formulário de contato, pedido de informações, visita, proposta, financiamento, aluguel ou compra. Restringir a busca ao período combinado.
4. Shortlistar mensagens pelos resumos e ler os corpos em lote. Ler a conversa completa quando houver respostas anteriores ou quando o histórico alterar a prioridade ou a mensagem.
5. Extrair o e-mail e o telefone informados pelo próprio lead ou pelo formulário de origem. Não procurar dados de contato em fontes externas.
6. Agrupar mensagens que aparentem pertencer à mesma pessoa. Não misturar contatos homônimos sem evidência suficiente.
7. Aplicar os critérios de `references/priorizacao.md`. Basear cada pontuação em evidências presentes nas mensagens; marcar como desconhecido o que não estiver disponível.
8. Para cada lead priorizado, recomendar o próximo passo e o melhor canal disponível. Respeitar preferência expressa pelo lead. Quando não houver preferência, usar WhatsApp para contato curto e responsivo, e-mail para respostas detalhadas ou com informações que precisam permanecer organizadas, e ligação quando houver sinal claro de urgência, pedido de contato ou benefício real de conversa síncrona.
9. Exibir uma tabela concisa com: prioridade, nome ou identificador, data, imóvel/interesse, canais disponíveis, canal recomendado, próximo passo, sinais observados e motivo da posição.
10. Para cada lead priorizado com telefone válido, gerar imediatamente um rascunho curto e um link de WhatsApp preenchido conforme `references/whatsapp.md`. O link deve apenas abrir a conversa para revisão; nunca afirmar que a mensagem foi enviada.
11. Quando uma ligação for útil, oferecer opcionalmente uma mensagem para pedir autorização ou combinar horário e um link para abrir o discador, seguindo `references/ligacao.md`.
12. Depois que o usuário escolher os leads a contatar por e-mail, gerar a prévia de cada e-mail no chat seguindo `references/mensagens.md`. Mostrar destinatário, assunto e corpo completo antes de qualquer ação no Gmail.
13. Após cada prévia, oferecer três opções claras: `Enviar pelo ChatGPT`, `Editar no Gmail` ou `Ajustar aqui no chat`.
14. Se o usuário escolher `Enviar pelo ChatGPT`, enviar somente depois dessa escolha explícita. Responder na conversa existente quando isso preservar o contexto; criar novo e-mail apenas quando não houver thread adequada. Depois, confirmar o envio com destinatário e assunto.
15. Se o usuário escolher `Editar no Gmail`, criar um rascunho com exatamente a última versão exibida e fornecer o link retornado pelo Gmail. Informar claramente que o rascunho não foi enviado.
16. Se o usuário escolher `Ajustar aqui no chat`, revisar a mensagem, mostrar novamente a prévia completa e reapresentar as três opções. Não enviar nem criar rascunho antes da nova escolha.

## Regras

- Nunca enviar e-mail antes de mostrar no chat o destinatário, o assunto e o corpo completo e receber uma escolha explícita de envio.
- Para vários e-mails, aceitar envio em lote somente quando o usuário identificar claramente o conjunto já revisado, por exemplo `Enviar os cinco`.
- Nunca enviar mensagens pelo WhatsApp. Fornecer somente o texto sugerido e o link de composição.
- Nunca iniciar uma ligação. Fornecer somente a mensagem opcional de autorização e o link para abrir o discador.
- Não gerar link de WhatsApp para número incompleto, ambíguo, inválido ou de quem pediu para não ser contatado.
- Não prometer disponibilidade, preço, desconto, condição comercial, financiamento ou prazo que não conste nas mensagens.
- Não inferir renda, patrimônio, capacidade de compra ou urgência a partir de nome, endereço, profissão, domínio de e-mail ou aparência social.
- Não usar raça, etnia, nacionalidade, religião, gênero, orientação sexual, idade, deficiência, estado civil, condição familiar ou saúde para priorizar, excluir ou personalizar leads.
- Não classificar um lead como ruim apenas por escrever pouco. Usar baixa informação como incerteza, não como rejeição.
- Não expor endereços de e-mail, telefones ou trechos sensíveis na tabela além do necessário para o corretor reconhecer o contato.
- Preservar nome, imóvel, valores, datas e links exatamente como aparecem nas mensagens.
- Distinguir fatos, inferências e dados ausentes.

## Pedidos típicos

- "Veja os leads que chegaram esta semana e diga quem devo responder primeiro."
- "Encontre contatos antigos com chance de retomada e prepare cinco rascunhos."
- "Priorize quem perguntou sobre apartamentos de três quartos em Belo Horizonte."
- "Crie respostas para os dez leads mais quentes, mas não envie."
- "Mostre os melhores leads e já deixe as mensagens de WhatsApp prontas."
- "Mostre as respostas por e-mail e depois me deixe escolher entre enviar ou editar no Gmail."
- "Trabalhe os leads de hoje e sugira para quem vale pedir autorização para ligar."
