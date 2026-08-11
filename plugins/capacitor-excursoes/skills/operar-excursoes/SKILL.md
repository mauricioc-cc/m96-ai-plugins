---
name: operar-excursoes
description: Organizar a operação da Capacitor Excursões a partir do Gmail e de arquivos TXT: triar pedidos de reserva, preparar ou enviar respostas, acompanhar comprovantes e correções, manter listas de reservas, gerar listas finais de passageiros por veículo e embarque, criar textos de divulgação e fornecer links de WhatsApp com mensagens preenchidas. Usar quando Frederico pedir para trabalhar e-mails de uma excursão, atualizar passageiros ou pagamentos, montar listas para a transportadora, divulgar eventos ou preparar contatos por WhatsApp.
---

# Operação da Capacitor Excursões

Usar o Gmail como entrada principal e arquivos TXT como registro operacional. Manter o formato, a linguagem e a organização já usados por Frederico sempre que houver um exemplo ou arquivo anterior.

## Antes de operar

1. Identificar inequivocamente a excursão por evento e data.
2. Localizar a conversa completa no Gmail quando o pedido envolver reserva, pagamento, correção ou resposta.
3. Localizar o TXT operacional mais recente da excursão. Se houver mais de uma versão sem indicação clara, pedir qual é a vigente.
4. Ler:
   - `references/fluxo-e-estados.md` para classificar e atualizar atendimentos;
   - `references/emails.md` para redigir respostas;
   - `references/listas-txt.md` para manter ou consolidar listas;
   - `references/whatsapp.md` para criar links;
   - `references/divulgacao.md` para divulgar um evento.

## Fluxo principal

1. Triar e-mails da excursão nas categorias: nova reserva, comprovante, correção, dúvida, cancelamento ou não relacionado.
2. Extrair somente dados explícitos: nome completo, documento, telefone, e-mail, embarque, evento, data, pagamento, correções e autorização para grupo de WhatsApp.
3. Apontar dados ausentes, inconsistentes ou duplicados antes de confirmar ou atualizar.
4. Preparar a resposta adequada preservando o tom da Capacitor e os dados confirmados do evento.
5. Atualizar a lista operacional sem apagar notas manuais, histórico financeiro ou vínculos entre passageiros.
6. Manter o estado de cada reserva conforme `references/fluxo-e-estados.md`. Não inferir pagamento apenas pela presença de anexo.
7. Quando solicitado, consolidar a lista final por veículo, ordem da rota e ponto de embarque, com numeração contínua.
8. Antes de entregar uma lista final, conferir totais por veículo, duplicidades, documentos ausentes e lotação.
9. Entregar arquivos no formato TXT, exceto quando o usuário pedir outro formato.

## E-mail

- Mostrar destinatário, assunto e corpo completo antes de enviar, salvo autorização explícita e delimitada para envio sem revisão.
- Tratar a autorização sem revisão como válida somente para aquela execução e para o conjunto indicado.
- Responder na conversa existente quando isso mantiver o contexto.
- Nunca responder a um passageiro com dados de outras reservas.
- Não confirmar vaga, preço, prazo, ponto, horário ou pagamento que não esteja sustentado pelo cadastro do evento ou pelo histórico.
- Depois de qualquer envio, informar destinatário, assunto e resultado. Se houver falha, não afirmar que foi enviado nem repetir automaticamente quando existir risco de duplicação.

## WhatsApp

- Nunca enviar mensagem nem alegar envio pelo WhatsApp.
- Gerar somente o texto visível e um link `https://wa.me/...` que abra a composição para Frederico revisar e enviar.
- Não gerar link quando o telefone estiver ausente, inválido, ambíguo ou associado a pedido de não contato.

## Arquivos e privacidade

- Usar os modelos em `assets/templates/` ao iniciar um evento ou arquivo novo.
- Não gravar dados reais de passageiros dentro do plugin ou de seus modelos.
- Tratar nome, documento, telefone, e-mail e comprovante como dados restritos à operação.
- Evitar repetir documentos completos no chat quando uma confirmação mascarada for suficiente.
- Não substituir uma lista existente por uma reconstrução baseada apenas no Gmail sem comparar as duas fontes e apontar divergências.
- Registrar pendências como pendências; não completar dados por suposição.

## Pedidos típicos

- "Veja os e-mails do AC/DC e me diga quais reservas precisam de resposta."
- "Prepare as confirmações e me mostre antes de enviar."
- "Atualize a lista TXT com os comprovantes que chegaram hoje."
- "Gere a lista final por ônibus e ponto de embarque."
- "Crie a divulgação desta excursão e o link para eu mandar no WhatsApp."
