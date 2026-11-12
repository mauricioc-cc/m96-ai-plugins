# liva — identidade visual para produtos (v0.1)

**Status:** direção Vila aprovada; regras de implementação aprovadas como ponto de partida, sujeitas a testes.  
**Data:** 2026-11-11  
**Escopo:** aplicações da suíte liva (encomendas, visitas, serviços e futuras).  
**Marca-mãe:** M96; consulte [filosofia de produto](../filosofia-de-produto.md). A liva **não herda** a paleta noturna da identidade pessoal M96.

## Regra oficial de assinatura da marca

- Escrever a marca **sempre como `liva.`**, em letras minúsculas e com ponto final integrante da assinatura, seguindo o caráter pessoal e minimalista de `mau.`.
- O **ponto deve ter destaque cromático âmbar `#F0C78B`** no uso colorido; as letras ficam preferencialmente em verde profundo `#293D37` sobre fundo claro, ou claras sobre fundo escuro.
- Em aplicações monocromáticas, o ponto mantém a forma mas acompanha a cor única.
- Não usar `Liva`, `LIVA` ou remover o ponto em logotipos isolados; nas assinaturas de produto não remover o **ponto separador**, nem acrescentar um segundo ponto final. Em textos corridos, nomes técnicos, endereços e metadados, respeitar legibilidade e convenções técnicas sem colorização obrigatória.
- **Assinatura dos produtos:** `encomendas.liva`, `visitas.liva`, `servicos.liva` — sempre em minúsculas, com **um único ponto entre o nome do produto e `liva`**, destacado em âmbar `#F0C78B`, no espírito de `radar.mau`. **Não acrescentar ponto final depois de `liva`** nessas assinaturas compostas.
- A forma isolada da marca permanece `liva.` (com ponto final âmbar). As assinaturas compostas seguem a regra diferente acima.
- A assinatura visual **não substitui nem determina o endereço DNS real** (ex.: `encomendas.liva.bhz.br`), nem obriga o texto do domínio a ter a mesma cor.
- Manter o ponto como elemento tipográfico, não como indicador de status ou elemento funcional.

## 1. Personalidade e norte

**Promessa de comunicação (proposta, ainda não slogan registrado):** “A vida no condomínio, mais simples.”

- Acolhedora, clara, humana, leve, confiável e organizada.
- Minimalismo funcional com calor residencial; **não** é um sistema corporativo pesado e **não** é uma interface infantil.
- Priorize quem executa as operações, especialmente porteiros nas jornadas de portaria.
- Inspire-se em clareza, simplicidade e microinterações prazerosas; **não** reproduza componentes ou marcas da Apple.

## 2. Paleta Vila — referências de marca

| Token de referência | Valor HEX | Intenção |
| --- | --- | --- |
| Verde liva | `#77A899` | marca, superfícies de apoio, áreas ilustradas |
| Âmbar | `#F0C78B` | acento caloroso e detalhes, incluindo ponto do logo |
| Areia | `#F7EFE4` | superfícies suaves e acolhedoras |
| Sálvia | `#E4EDE8` | superfícies secundárias e seleção |
| Verde Profundo | `#293D37` | texto principal, ações com contraste |

**Acessibilidade precede fidelidade literal à paleta:** não use Verde liva ou Âmbar como texto pequeno sobre branco, nem presuma que Verde liva com texto branco serve para botão de uso frequente. Use Verde Profundo em texto/ação principal; avalie WCAG AA para cada combinação, inclusive estados hover, disabled, foco e dark mode. Cores semânticas (erro, alerta, sucesso, informação) devem comunicar o estado por texto e ícone, além da cor; não equipare âmbar automaticamente a sucesso.

### Tokens semânticos propostos

Veja [tokens.css](tokens.css). O arquivo é um **contrato inicial de design**, não uma folha pronta para substituir estilos do projeto inteiro. Adapte nomes ao framework existente por mapeamento centralizado, sem espalhar HEX pelo código.

- Fundo principal claro: branco quente `#FCFBF8` (token de UI complementar, não altera a paleta da marca).
- Superfícies: branco e areia, com separações sutis.
- Textos: verde profundo; hierarquia secundária sempre legível.
- Ação primária: fundo verde profundo com texto claro.
- Destaques: verde liva em fundos, contornos e detalhes, desde que legíveis.
- Links: usar um tom escuro com sublinhado ou outra indicação que não dependa apenas de cor.
- Tema: o sistema anterior de Encomendas segue a **preferência claro/escuro do dispositivo**, conforme SPEC. Construir variação escura coerente e legível; não impor sempre modo claro sem decisão específica de produto.

## 3. Tipografia

**Família preferencial:** Plus Jakarta Sans, com fontes locais/licenciadas ou carregamento com fallback apropriado. Pesos de referência: 400/500/600/700. Fallback: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`.

- Texto operacional: referência inicial 16px no corpo e 16–18px nos campos, podendo aumentar conforme contexto; evite textos importantes abaixo de 14px.
- Textos de labels, números, botões e confirmação devem continuar legíveis no celular e iPad.
- Hierarquia por peso, espaço e tamanho — não apenas por diferença sutil de cor.
- Não reduzir legibilidade para reproduzir uma composição de marketing.
- O lettering `liva.` dos estudos ainda é exploratório; não presumir que texto genérico em Plus Jakarta Sans reproduz fielmente o logo.

## 4. Marca: símbolo e assinatura

**Grafia da marca:** sempre **liva**, em minúsculas, inclusive no início de frases, em títulos, links e metadados. A assinatura textual do produto de encomendas é **encomendas.liva**.

**Direção escolhida:** casa isométrica em pequena base verde, com teto verde e abertura iluminada. Assinatura `liva.`, em verde profundo, com ponto âmbar.

- Ícone principal: casa isométrica; reforça lar, portaria e convivência.
- Logo horizontal: símbolo + wordmark `liva.`, com espaço de respiro.
- Versões: fundo claro, fundo escuro, monocromático.
- Redução extrema: símbolo simplificado inspirado na mesma casa. O kit atual é **v0.1**, passível de refinamento para evitar aparência de caixa.
- Não redesenhar o logo em cada tela; consumir ativos centralizados e manter proporções.
- Não usar a ilustração isométrica detalhada como único indicador funcional de status em tamanho pequeno.
- Ativos experimentais do kit devem ser conferidos visualmente na integração; não tratar mockups ou imagem gerada como layout pixel-perfect, arquivo vetorial definitivo ou especificação técnica de componentes.

## 5. Sistema isométrico

A isometria é a linguagem de **ilustração da marca**, não substitui toda iconografia da UI.

- Temas: casa, edifício, casas em conjunto, condomínio vertical/horizontal, portaria, pacote, visita, prestador, documento, assinatura, notificações.
- Perspectiva uniforme e volumes legíveis, cores Villa/Vila, geometria suavizada, sombra discreta, poucos detalhes, aspecto de miniatura arquitetônica.
- Evitar hiper-realismo, cenários excessivamente saturados, informação minúscula e excesso de elementos num mesmo cartão.
- Empregar em: hero, boas-vindas, estados vazios, ilustrações de ajuda, catálogo de produtos, comunicações e confirmações quando não atrasarem a ação.
- UI operacional usa ícones lineares simples e consistentes, com rótulos textuais sempre que necessários.
- Não usar uma isometria decorativa quando o espaço é necessário para dados, botões ou a assinatura do morador.

## 6. Padrões de interface

- Mobile-first; acomodar tablet/iPad e desktop com o mesmo fluxo sem cortes.
- Espaçamento generoso, cards e campos com cantos moderadamente arredondados, poucas bordas e sombras sutis.
- Áreas de toque preferencialmente >= 44×44 CSS px; campos devem manter tamanho e teclado adequados; suporte a zoom sem quebra.
- Botão primário óbvio; ação destrutiva deliberadamente diferenciada; saída discreta e não confundida com “voltar”.
- Modal: rolagem interna quando necessário, tela de fundo bloqueada, foco e teclado acessíveis, ações nunca cortadas.
- Busca, revisão humana da extração de IA, seleção manual de entregas, captura de assinatura e compartilhamento devem seguir os requisitos específicos de cada produto.
- Formulários: labels persistentes, erros próximos ao campo, foco visível e estados de carregamento claros.

## 7. Motion e feedback

- Cada operação relevante tem estados de `idle`, `loading`, `success` e `error`; nunca indicar sucesso antes de resposta confirmada do backend.
- Microinterações rápidas e discretas, com sensação agradável de conclusão; sem celebração obrigatória ou animação que retarde a próxima tarefa.
- Faixa inicial sugerida (não normativa): transições 120–220ms; confirmações 180–350ms quando não bloqueantes. Validar em aparelho real.
- Respeitar `prefers-reduced-motion` e prover feedback textual/estático equivalente.
- Nada de animações que distraiam da operação crítica ou dificultem uso repetido.

## 8. Modo escuro

A marca é **light-first visualmente**, não necessariamente light-only funcionalmente.

- Encomendas já segue tema do sistema; preservar na evolução até aprovação de mudança.
- Dark mode deve adaptar papéis semânticos de superfície, texto, contraste e foco; não inverter cores automaticamente.
- Evitar transplantar a estética escura M96 para o tema escuro liva: manter calma, neutralidade e verde liva como acento.

## 9. Checklist para agente / pull request

Antes de implementar:
1. Identifique usuário primário da jornada e o que ele precisa concluir.
2. Leia a filosofia M96 e a SPEC/AGENTS do produto, sem sobrescrevê-las.
3. Mapeie os tokens semânticos e componentes existentes; evite refatoração extensa sem necessidade.
4. Descreva o comportamento do tema claro e escuro, responsividade, estados de feedback, acessibilidade e fallback dos assets.

Critérios de aceite:
- Fluxos atuais intactos; sem perda de dados, mudanças de auth, PIN, assinatura ou regras de negócio decorrentes de tema visual.
- Contraste validado para textos, botões e estados; foco visível e navegação por teclado.
- Celular e iPad testados; teclado, modal, assinatura, busca e compartilhamento funcionando.
- Estados e preferências de movimento respeitados.
- Componentes consomem tokens, não HEX dispersos.
- Ativos corretos e leves; símbolo reconhecível em 16/24/32px, com fallback.
- Nenhum deploy em produção sem aprovação explícita e plano de rollback.

## 10. Sequência segura de migração

1. Diagnóstico do repositório e inventário de componentes atuais.
2. Introdução de tokens e fontes em branch/ambiente isolado.
3. Componentes base (fundo, texto, inputs, botões, estados).
4. Logo, favicon e ilustrações sem alterar funcionalidades.
5. Revisão visual e testes de regressão das jornadas completas, inclusive em iPad.
6. Capturas comparativas, revisão, aprovação de deploy e rollback.

Este guia documenta uma **identidade aprovada como direção**, não autoriza automaticamente mudanças na instância atualmente em uso.
