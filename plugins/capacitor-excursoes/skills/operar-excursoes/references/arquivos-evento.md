# Pastas e arquivos da excursão

## Estrutura confirmada

Frederico organiza as excursões localmente nesta hierarquia:

`Fre Trabalho/Capacitor Excursões/AAAA/MM-DD Artista - Local/`

Exemplo confirmado:

`Fre Trabalho/Capacitor Excursões/2026/04-28 Bad Religion - Espaço Unimed/`

Para uma excursão nova:

1. usar o ano com quatro dígitos;
2. nomear a pasta como `MM-DD Artista - Local`;
3. manter todos os TXT daquela excursão dentro dessa pasta;
4. não renomear nem mover pastas antigas automaticamente;
5. se já existir uma pasta semelhante, confirmar a pasta exata antes de gerar arquivos.

O plugin não acessa essa estrutura local por conta própria. Quando os arquivos estiverem apenas no computador, pedir que Frederico anexe os TXT necessários e entregar cópias para ele salvar na pasta correspondente.

## Nome do TXT principal

Frederico aceitou começar a padronizar os novos TXT principais neste formato:

`ARTISTA DIA-DA-SEMANA DD LOCAL.txt`

Exemplo:

`BAD RELIGION TERÇA 28 ESPAÇO UNIMED.txt`

Esse é um padrão para novos arquivos. Preservar os nomes reais dos TXT já existentes e não renomeá-los sem pedido explícito.

## TXT de informações gerais

Dentro da pasta da excursão, usar estes nomes fixos quando o respectivo conteúdo existir:

- `Preços.txt`
- `Horários.txt`
- `Locais de Embarque.txt`
- `Endereços.txt`
- `Tipo de Veículos.txt`
- `Regras.txt`

Não criar arquivos vazios apenas para completar a estrutura. Criar ou atualizar cada TXT somente com informações explícitas e confirmadas daquela excursão.

### Conteúdo esperado

- `Preços.txt`: preços por cidade ou modalidade, parcelamento, prazos e condições de pagamento que tenham sido confirmados.
- `Horários.txt`: horários de encontro, saída, chegada ou retorno.
- `Locais de Embarque.txt`: cidades e nomes dos pontos de embarque.
- `Endereços.txt`: endereços completos relacionados aos embarques ou ao evento, com identificação clara.
- `Tipo de Veículos.txt`: tipos, capacidades e divisões de veículos já definidas.
- `Regras.txt`: regulamento e orientações da excursão.

Não transferir automaticamente dados históricos de outra excursão. Quando uma resposta antiga servir como base, mostrar os dados variáveis e confirmar antes de gravar.

## Conflitos e duplicidades

- Tratar artista, data e local juntos como identidade da excursão.
- Não misturar arquivos de shows diferentes do mesmo artista.
- Se pasta, Gmail e TXT divergirem, mostrar a divergência e aguardar decisão.
- Se houver dois arquivos para a mesma finalidade, comparar ambos e perguntar qual é o vigente.
- Preservar maiúsculas, acentos e estilo encontrados nos arquivos já existentes.
