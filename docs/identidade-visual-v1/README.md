# Identidade pessoal — sistema v1.0

16 de outubro de 2026. Primeira especificação operacional construída a partir da direção aprovada por Mau. As medidas e componentes desta versão são decisões de implementação tomadas sob a autorização para concluir o sistema; não são novas aprovações individuais de cada medida.

## Arquivos e uso

- [Guia visual offline](guia-visual.html): exemplos com fontes incorporadas, formulário demonstrativo local, capa e documento claro.
- [tokens.css](tokens.css): fontes locais, cores, medidas e componentes básicos. Copiar junto de `fonts/` e `grain.svg`; aplicar a classe `m96` ao contêiner. Para documento claro, adicionar `data-theme="light"`.
- [tokens.json](tokens.json): valores para outras ferramentas.
- [grain.svg](grain.svg): textura neutra repetível, sem gradiente.
- `fonts/`: arquivos reais Barlow e Barlow Condensed, com a licença OFL.
- [Referência aprovada](../assets/identidade-visual/estudo-aprovado-v1.jpg).
- [Contexto e decisões](../identidade-visual.md).

O guia é uma demonstração local. As notas adicionadas nele existem apenas enquanto a página está aberta, sem envio ou persistência. Esta entrega não publica um site nem altera projetos existentes.

## 1. O que torna a identidade reconhecível

Cidade quase vazia de madrugada vista de um abrigo, asfalto molhado e luz distante. A tecnologia real dos anos 80 aparece na materialidade fosca, na divisão funcional e na contenção dos sinais. O sistema permanece independente do Retrovisor.

Quatro características sustentam a família: títulos condensados; grande respiro; superfícies escuras foscas; pequenos rastros vermelhos interrompidos. Não é obrigatório usar todos os recursos em todas as peças. Interface de trabalho prioriza leitura e função; wallpaper pode concentrar a atmosfera na imagem.

## 2. Cor

Preservar os seis HEX da paleta aprovada. As cores abaixo de apoio são derivações funcionais, não substituições da paleta.

| Papel | Escuro | Claro |
| --- | --- | --- |
| Fundo | Noite #0B1018 | Farol #E2E6EB |
| Superfície | Asfalto #202A35 | Papel #F5F3EE |
| Texto | Farol #E2E6EB | Noite #0B1018 |
| Texto secundário | #AEB8C4 | #465463 |
| Ação preenchida | Lanterna #C92C38 | #B32430 |
| Texto sobre ação | #FFFFFF | #FFFFFF |
| Link sublinhado | #7AC0CC | #17616E |
| Contorno funcional | #718090 | #697887 |
| Foco | Farol #E2E6EB | Noite #0B1018 |
| Sucesso | #8FC5B0 | #245F49 |
| Aviso | Âmbar #CE902F | #6D4A0A |
| Erro | #FF9AA4 | #B32430 |

Predominam fundos neutros; o vermelho concentra ações ou um gesto de assinatura. Em uma peça de atmosfera, buscar aproximadamente 80–90% de área neutra e 10–20% de luz/imagem/acentos, sem tratar isso como obrigação matemática. Não distribuir vermelho, azul e âmbar igualmente por padrão.

Petróleo #258D9E é adequado para detalhes e áreas gráficas; não usar como texto pequeno em Asfalto. Vermelho de marca não representa erro automaticamente. Estados sempre recebem texto ou outro sinal além da cor. Links são sublinhados.

### Contrastes de referência

| Par | Razão aproximada |
| --- | --- |
| Farol sobre Noite | 15,21:1 |
| Farol sobre Asfalto | 11,60:1 |
| Branco sobre Lanterna | 5,38:1 |
| Âmbar sobre Asfalto | 5,30:1 |
| Link claro #7AC0CC sobre Asfalto | 7,09:1 |
| Petróleo original sobre Asfalto | 3,73:1 — evitar texto pequeno |

As combinações funcionais de texto e controle foram calculadas na validação desta versão. Fotografias, transparências e novas combinações exigem checagem própria. O cálculo não equivale a uma auditoria completa de acessibilidade de futuros produtos.

## 3. Tipografia

Barlow Condensed 600: títulos. Barlow 400: texto corrido. Barlow 500: controles, rótulos e metadados; 600 para destaque pontual no texto. A Barlow de largura normal dá continuidade à mesma família sem comprimir parágrafos.

| Uso | Tamanho | Entrelinha | Peso |
| --- | --- | --- | --- |
| Título principal | 40px no celular até 64px em telas maiores | 1,08 | Condensed 600 |
| Título de seção | 32–40px | 1,08 | Condensed 600 |
| Subtítulo | 24px | 1,15 | Condensed 600 |
| Texto de interface | 16px | 1,55 | Barlow 400 |
| Texto de leitura | 17–18px | 1,65 | Barlow 400 |
| Rótulos curtos | 12px | 1,4 | Barlow 500 |
| Texto secundário | 14px | 1,5 | Barlow 400 |

Títulos: espaçamento de letras -0,01em. Maiúsculas apenas em rótulos curtos, com +0,08em. Texto corrido em caixa normal, largura de até 65 caracteres. Nunca aplicar condensação por transformação horizontal. Usar negrito real, sem distorção, desfoque ou textura nas letras. Alternativas de sistema: Arial para corpo e Arial Narrow para títulos, com ajuste de quebra de linha; a aparência pode variar até a fonte carregar.

## 4. Composição

Unidade de espaçamento: 4px. Escala: 4, 8, 12, 16, 24, 32, 48, 64px. Margens externas: 20–24px no celular e 32–64px em telas maiores. Conteúdo geral com largura máxima sugerida de 1120px; leitura limitada a 65ch. Grid de 4 colunas no celular e 12 em telas maiores, com intervalo de 16–24px. Recolher para uma coluna quando conteúdo ou controles deixarem de caber confortavelmente.

Usar assimetria para hierarquia, não para desalinhar controles. Em capas e fundos, permitir que 40–60% da composição seja campo quieto. Em ferramentas densas, adaptar o respiro à tarefa. Preferir separadores e listas a empilhar cartões decorativos.

## 5. Materialidade

Textura base: `grain.svg`, escala nativa 160px, opacidade de 0,04. Pode subir a 0,06 em capas e fundos, sem cobrir letras ou controles. No exemplo CSS fica atrás do conteúdo. Documento claro de leitura não precisa de textura. Não ampliar o grão para parecer concreto ou papel de lixa.

Superfícies opacas. Raio padrão de 2px nos controles, até 4px em superfícies quando necessário. Divisões funcionais de 1px. Evitar brilho ornamental em bordas, sombras de halo, scanlines contínuas, aberração cromática no texto e filtros VHS sobre toda a interface. Gradiente não é ferramenta padrão; uma fotografia pode conter transições ópticas naturais de luz.

## 6. Gesto gráfico e imagens

O rastro é formado por duas faixas vermelhas desiguais: 40px e 96px de comprimento, 4px de espessura, intervalo de 8px e deslocamento vertical de 5px. Em capa pode ser ampliado proporcionalmente. É um recurso de composição opcional, não um logotipo, botão ou indicador de progresso. Usar uma vez por composição, em geral junto de uma borda ou recorte. Versão monocromática assume a cor do texto local.

Imagens: cidade cotidiana, enquadramento protegido, vazios, chuva, reflexos e luzes pequenas. Preservar informação nas sombras e o vermelho profundo. Evitar HDR excessivo, skyline turístico e saturação uniforme. Uma faixa panorâmica pode ocupar cerca de um quinto da altura de uma capa. Imagem usada em produção deve ter origem e direitos identificados. A referência gerada não documenta um lugar real.

Ícones funcionais: uma única família por produto, traço simples de 1,5–2px, tamanhos 20 ou 24px, nomes acessíveis. Não incluir ícones apenas para preencher espaço. O gesto gráfico acima é distinto dos ícones funcionais.

## 7. Interface e movimento

- Botão primário: vermelho, texto branco, altura mínima de 44px, raio 2px, peso 500. Secundário: fundo transparente e contorno funcional.
- Campo: rótulo visível, texto de pelo menos 16px, altura mínima de 44px; erro em texto junto do campo. Placeholder não substitui rótulo.
- Foco: contorno de 2px com afastamento de 4px. Não remover o foco do teclado.
- Seleção: linha vermelha e texto com estado explícito; componentes reais devem expor seu estado por semântica adequada.
- Desabilitado: sem interação, opacidade 0,45; não usar esse aspecto para informações essenciais.
- Carregamento: indicar “Carregando…” junto à ação e anunciar mudança quando necessário; não inventar percentuais.
- Sucesso, aviso e erro: texto legível com ícone ou palavra, além da cor. Âmbar em avisos; vermelho de marca continua disponível em ações.
- Transições: 140ms, curva cubic-bezier(.2,0,0,1), apenas onde ajudam a perceber resposta. Respeitar movimento reduzido. Sem loops ambientais por padrão e sem sons automáticos.

Os exemplos do guia são base visual e semântica para adaptação; não constituem uma biblioteca completa de todos os componentes de produto.

## 8. Templates por formato

**Wallpaper de celular:** composição vertical, imagem concentrada na metade inferior e espaço superior para relógio. Usar a proporção e resolução do dispositivo; não embutir horário, logo ou frase por padrão. **Desktop:** recorte amplo com área quieta para ícones. Não esticar foto vertical. **Watch face:** aplicar as cores em opções nativas disponíveis; testar sol direto e contraste. Não presumir que mostradores nativos aceitam fontes externas ou qualquer HEX.

**Documento:** capa pode ser escura; páginas de leitura em Papel/Farol com Noite no texto. A4 com margens de 20–24mm, corpo 11–12pt e entrelinha 1,45–1,6. **Apresentação:** formato 16:9, margem de 5% da largura, títulos 32–44pt e corpo a partir de 20pt; fotografias e rastros preservam as mesmas proporções visuais. **Imagem social:** adaptar corte ao destino, mantendo respiro e assinatura opcional. Não exportar uma interface inteira como capa.

## 9. Assinatura

“m96”, “mau.” ou nenhuma, conforme o projeto. Usar Barlow 500 sem efeitos como tratamento inicial de assinatura, subordinado ao título do projeto. Área livre de pelo menos uma altura da letra; em imagens, 16px no mínimo para legibilidade. Não foi criado um símbolo obrigatório. As marcas não precisam aparecer juntas. Esta escolha intencional não bloqueia a versão 1.0.

## 10. Estado da entrega

A versão 1.0 fecha a base visual reutilizável: paleta, tipografia, métricas, textura, gesto gráfico, cor funcional, componentes fundamentais, movimento e modelos de composição. O guia offline usa fontes incorporadas para evitar a falha observada no primeiro comparativo. Não depende de Adobe ou chamadas de rede para renderizar.

Escolhas futuras de conteúdo e produtos, exportações para dispositivos específicos, um eventual logotipo e componentes particulares são extensões desta base. Não estão sendo declarados como assets finais já produzidos. Novos produtos precisam de validação no contexto real.

### Validação executada

Combinações funcionais de contraste calculadas, fontes reais abertas e verificadas com suporte aos caracteres portugueses e sintaxe JavaScript conferida. A instalação do navegador de teste falhou no ambiente de execução; a revisão visual responsiva e a interação em navegador permanecem sem validação automatizada. Não confundir os exemplos com uma auditoria completa de acessibilidade ou uma biblioteca de produto pronta para produção.

Fontes: Jeremy Tribby, [Barlow](https://github.com/jpt/barlow), SIL Open Font License 1.1; a licença acompanha os arquivos. Manter a licença ao redistribuir as fontes.
