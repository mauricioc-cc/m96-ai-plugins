# Notificações de leads do Hinc ou HIncrível

Reconhecer esse formato como uma fonte frequente, mas não exclusiva, de novos leads. A marca, o idioma e pequenos trechos do modelo podem variar.

## Sinais de identificação

- Nome ou marca `Hinc` ou `HIncrível` no remetente, domínio, cabeçalho ou corpo.
- Expressões como `Nova mensagem via Central de Anúncios` ou equivalentes traduzidos.
- Assunto contendo operação, tipo do imóvel, e-mail do interessado ou identificador no formato `Lead: ...`.
- Bloco central com nome, e-mail, telefone e uma frase que descreve o interesse imobiliário.

Não exigir todos os sinais e não classificar mensagens apenas pelo nome exibido do remetente. Notificações encaminhadas podem preservar o formato mesmo quando o remetente mudou.

## Extração

Extrair do assunto e do bloco principal, quando disponíveis:

- identificador do lead;
- finalidade, como compra ou aluguel;
- nome, e-mail e telefone do interessado;
- tipo do imóvel, cidade, bairro, dormitórios, preço e outras características explicitamente informadas;
- pergunta ou observação escrita pelo lead;
- código e URL do anúncio principal, somente quando estiverem claramente associados ao interesse original.

O idioma do texto pode estar em português, inglês ou traduzido pelo cliente de e-mail. Interpretar o significado dos campos sem alterar nomes, números, códigos ou valores.

## Imóvel principal e imóveis semelhantes

- Tratar a descrição logo após os dados pessoais como o interesse principal do lead.
- Reconhecer seções como `Imóveis que encontramos em sua base com características semelhantes`, `Properties we found in your database with similar characteristics` ou equivalentes como sugestões do Hinc.
- Classificar códigos, descrições e links dentro dessa seção como `imóveis semelhantes sugeridos`, nunca como o anúncio original sem outra evidência.
- Não abrir, citar nem enviar um link sugerido como se fosse o imóvel que originou o contato.
- Usar imóveis semelhantes apenas como possíveis alternativas e somente depois de confirmar disponibilidade e pertinência. No primeiro contato, não apresentá-los automaticamente.

Se a notificação trouxer somente a descrição do interesse principal, usar essa descrição para contextualizar a mensagem sem exigir uma URL.

## Destinatário do contato

- Tratar o e-mail no bloco de dados pessoais como o endereço do lead.
- Não responder ao endereço automático que enviou a notificação do Hinc.
- Criar novo e-mail para o endereço do lead, salvo quando o cabeçalho `Reply-To` estiver claramente configurado para esse mesmo endereço.
- Na prévia, mostrar o endereço extraído para que o corretor possa conferi-lo antes de enviar ou criar o rascunho.
