# Controle financeiro operacional

## Objetivo

Manter um registro interno e simples do dinheiro efetivamente recebido por excursão e dos custos mencionados explicitamente. Frederico não precisa abrir nem editar a planilha para usar o recurso; ele pode consultar os totais pelo chat.

Este controle é operacional. Não é contabilidade, conciliação bancária, fluxo de caixa formal nem apuração fiscal.

## Ativação

O financeiro é opcional e não bloqueia Gmail, TXT ou WhatsApp.

1. Confirmar a conta Google Drive que Frederico pretende usar.
2. Explicar que será criada uma única planilha privada chamada `Controle Financeiro — Capacitor Excursões`.
3. Criar a planilha somente após autorização explícita.
4. Se já existir uma planilha com esse nome, confirmar a identidade antes de reutilizá-la; não criar duplicata automaticamente.
5. Guardar no contexto disponível a referência inequívoca da planilha. Em novo contexto, localizá-la pelo nome e confirmar em caso de ambiguidade.
6. Se o Drive não estiver conectado, continuar o restante da operação e informar apenas que o financeiro ainda não está habilitado.

Para uma planilha nova, gerar e validar primeiro o arquivo de planilha e importá-lo como Google Sheets pelo Google Drive conectado. Não criar uma planilha vazia e preenchê-la de modo improvisado.

## Estrutura da planilha

### Aba `Eventos`

Uma linha por excursão:

| Coluna | Conteúdo |
|---|---|
| `evento_id` | identificador estável do evento, sem dados de passageiro |
| `evento` | nome usado por Frederico |
| `data_evento` | data da excursão |
| `status` | aberto, realizado ou cancelado |
| `passageiros` | quantidade operacional conhecida |
| `receita_recebida` | total de receitas confirmadas |
| `custos_registrados` | total de custos explícitos |
| `devolucoes` | total devolvido explicitamente |
| `saldo_operacional` | receita menos custos e devoluções |
| `valor_pendente` | estimativa identificada nas reservas, sem tratar como entrada |
| `atualizado_em` | data e hora da última atualização |

Os totais devem ser fórmulas derivadas da aba `Movimentações`, nunca números repetidos manualmente. `valor_pendente` deve permanecer separado de caixa recebido.

### Aba `Movimentações`

Uma linha por ocorrência financeira:

| Coluna | Conteúdo |
|---|---|
| `movimento_id` | chave estável usada para impedir duplicidade |
| `evento_id` | vínculo com a excursão |
| `data` | data explícita do movimento; quando ausente, usar a data da interação e marcar isso na descrição |
| `tipo` | receita, custo ou devolução |
| `descricao` | explicação curta |
| `valor` | valor positivo; o tipo define o efeito no saldo |
| `status` | confirmado ou pendente |
| `origem` | gmail, txt ou conversa |
| `origem_ref` | referência mínima à mensagem, arquivo ou interação |
| `reserva_ref` | referência operacional sem RG, CPF, telefone ou e-mail |
| `registrado_em` | data e hora do registro |

Manter valores monetários como números e datas como datas reais. Preservar cabeçalhos e fórmulas ao adicionar linhas.

## Quando registrar receita

Registrar receita confirmada somente quando houver valor e vínculo inequívoco com o evento, em pelo menos uma destas situações:

- comprovante conferido e confirmado por Frederico;
- Frederico declarar explicitamente que recebeu determinado valor;
- uma atualização de pagamento for autorizada com valor conhecido.

A etiqueta `EVENTO PG` e o símbolo `#`, sozinhos, não provam o valor recebido.

Pagamento parcial gera uma movimentação com o valor efetivamente recebido. Uma parcela posterior gera outra movimentação. Nunca lançar o preço total como receita quando apenas parte entrou.

Se houver confirmação de pagamento sem valor seguro, atualizar o fluxo operacional conforme autorizado, mas não inventar a receita. Fazer uma única pergunta curta sobre o valor quando ele for necessário para o controle.

## Quando registrar custo

Registrar custo apenas quando Frederico mencionar de modo explícito o evento, a natureza do gasto e o valor, por exemplo: fretamento, ingresso, estacionamento ou pedágio.

- Se evento ou valor estiver ambíguo, perguntar somente o dado indispensável.
- Não estimar custo a partir de preço histórico.
- Não transformar uma cotação, orçamento ou intenção em custo confirmado.
- Se o custo estiver claramente pendente, pode registrá-lo com status `pendente`, sem afetar o saldo realizado.

## Devoluções e correções

Registrar devolução apenas quando o valor e o evento estiverem explícitos. O valor permanece positivo na coluna `valor`; o tipo `devolução` faz a subtração no saldo.

Não apagar silenciosamente o histórico. Para corrigir um movimento já registrado, criar um ajuste rastreável ou atualizar a mesma origem com nota de correção, preservando o que mudou.

## Idempotência

Antes de inserir, procurar o `movimento_id` e a `origem_ref`.

- Reprocessar a mesma mensagem ou comprovante não pode duplicar um lançamento.
- Gerar a chave a partir de evento, origem, referência, tipo, data e valor conhecidos.
- Se a mesma origem reaparecer com dados diferentes, mostrar a divergência e pedir confirmação antes de alterar.
- Depois de qualquer gravação, recalcular a linha do evento e verificar se `receita - custos - devoluções = saldo_operacional`.

## Privacidade

Não armazenar na planilha RG, CPF, telefone, e-mail, dados bancários, imagem de comprovante nem texto integral de conversas. Usar apenas referências mínimas para auditoria operacional.

## Consultas pelo chat

Responder perguntas como:

- "Quanto entrou no evento do AC/DC?"
- "Quais eventos têm valor pendente?"
- "Quanto foi registrado de custo no evento?"
- "Qual é o saldo operacional registrado desta excursão?"
- "De onde veio este lançamento?"

Sempre chamar o resultado de valor ou saldo `registrado`, deixando claro quando existirem pendências, ambiguidades ou movimentos ainda não confirmados.
