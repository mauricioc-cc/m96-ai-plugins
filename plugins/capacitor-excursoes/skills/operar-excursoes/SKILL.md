---
name: operar-excursoes
description: Adaptar-se ao ambiente real da Capacitor Excursões e organizar sua operação a partir do Gmail e dos arquivos TXT existentes: reconhecer etiquetas por evento, triar e responder reservas com os modelos usados por Frederico, acompanhar comprovantes e pagamentos, manter as três listas de passageiros, preparar arquivos para a transportadora e para a chamada, gerar links de WhatsApp com mensagens preenchidas e manter um controle financeiro operacional opcional no Google Sheets. Usar quando Frederico quiser ambientar o plugin, trabalhar e-mails de uma excursão, atualizar reservas ou pagamentos, organizar passageiros, registrar valores recebidos ou custos explícitos, consultar totais por evento ou preparar comunicações sem mudar seu fluxo atual.
---

# Operação da Capacitor Excursões

Usar o Gmail como entrada principal e os TXT existentes como registro operacional. Adaptar-se ao ambiente encontrado; não exigir reorganização prévia. Manter o financeiro como uma camada interna e opcional do mesmo fluxo.

## Ambientação obrigatória

Antes da primeira operação em uma conta ou conjunto de arquivos, ler `references/adaptacao-ambiente.md` e:

1. Confirmar que o Gmail conectado é a conta operacional pretendida.
2. Reconhecer as etiquetas reais dos eventos sem criar, renomear ou excluir nada.
3. Solicitar o TXT vigente quando ele estiver somente no computador. Usar armazenamento conectado apenas quando Frederico indicar a pasta.
4. Aprender o formato dos arquivos fornecidos antes de propor qualquer atualização.
5. Confirmar a fonte atual das informações do evento. Não impor um cadastro novo enquanto essa preferência não estiver definida.
6. Oferecer uma única vez a ativação do controle financeiro. Criar ou reutilizar a planilha somente após autorização e confirmação da conta Google Drive.

Repetir somente a parte da ambientação afetada quando mudar a conta, a pasta, o evento, o padrão dos arquivos ou a planilha financeira.

## Referências

- Ler `references/gmail.md` para triagem, respostas e etiquetas.
- Ler `references/fluxo-e-estados.md` para o fluxo confirmado.
- Ler `references/pagamentos.md` para comprovantes e símbolos.
- Ler `references/financeiro.md` para receitas, custos, devoluções e Google Sheets.
- Ler `references/emails.md` para redigir e enviar.
- Ler `references/listas-txt.md` para atualizar as três listas.
- Ler `references/whatsapp.md` para gerar links.
- Ler `references/divulgacao.md` para reaproveitar divulgações existentes.

## Fluxo principal

1. Identificar inequivocamente a excursão por evento e data.
2. Ler a conversa completa quando envolver reserva, pagamento, correção, cancelamento ou valor financeiro.
3. Extrair somente dados explícitos: passageiros, documentos, telefone, embarque, valores e alterações.
4. Comparar o e-mail com o TXT operacional vigente; apontar ausências, duplicidades e divergências.
5. Preparar a resposta com o modelo já usado naquele evento ou com o modelo do plugin quando não houver exemplo.
6. Mostrar destinatário, assunto e corpo completo antes de enviar.
7. Após autorização, enviar e atualizar etiquetas conforme o comportamento confirmado da conta.
8. Atualizar o TXT preservando estilo, ordem, códigos, notas e histórico relevante.
9. Quando o financeiro estiver habilitado, registrar sem duplicidade somente receitas confirmadas, custos explícitos e devoluções explícitas.
10. Gerar as listas da transportadora e da chamada somente quando solicitado.
11. Entregar um resumo objetivo do que mudou e do que continua pendente.

## Limites

- Não afirmar que tem acesso a arquivos locais que não foram anexados nem expostos por armazenamento conectado.
- Não reconstruir nem substituir um TXT existente apenas com base no Gmail sem comparar as fontes.
- Não criar uma organização paralela para substituir as pastas e arquivos de Frederico.
- Não marcar pagamento integral apenas porque há comprovante.
- Não tratar a etiqueta `EVENTO PG` como prova de valor recebido.
- Não inventar receitas, custos ou datas; perguntar somente quando o dado for indispensável.
- Não chamar o controle interno de contabilidade, lucro ou conciliação bancária. Usar `saldo operacional registrado`.
- Não bloquear a operação caso o Google Drive não esteja conectado ou o financeiro não tenha sido ativado.
- Não decidir automaticamente rebaixamento na ordem, troca de veículo ou van extra; mostrar evidências e pedir confirmação.
- Não processar correções ou cancelamentos originados apenas no WhatsApp. Seguir a prática atual de exigir o pedido por e-mail.
- Nunca enviar pelo WhatsApp. Fornecer somente texto e link de composição.
- Não inserir dados reais de passageiros, dados bancários ou credenciais nos arquivos do plugin nem na planilha financeira.

## Pedidos típicos

- "Aprenda como estão organizados meu Gmail e os arquivos do AC/DC."
- "Veja quais reservas do AC/DC ainda precisam de resposta."
- "Prepare as respostas usando o modelo desse evento."
- "Confira os comprovantes, atualize a lista e registre o que entrou."
- "Mostre quem está sem pagar ou fora do grupo."
- "Quanto entrou e quanto foi registrado de custo neste evento?"
- "Gere a lista da agência e a chamada do grupo."
