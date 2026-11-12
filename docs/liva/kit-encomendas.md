# liva. — kit minimalista de objetos isométricos v0.2

**Status:** direção visual e inventário v0.2 aprovados para geração/curadoria. **Os PNGs v0.2 ainda não foram enviados ao GitHub.** Os PNGs do v0.1 continuam presentes, e não devem ser tratados como v0.2.

## Princípio visual

**Os assets da liva. devem ser objetivos, modulares e compostos pelo menor número de elementos possível.** Cada imagem representa **um objeto isolado** ou **um conceito mínimo** reconhecível. Sem ceninhas, paisagismo, bases elaboradas, mobiliário ou elementos adicionais que não expliquem a ação.

Exemplos: casa = somente casa; prédio = somente prédio; portaria = somente guarita; encomenda = somente caixa; leitura por IA = caixa + indicador de scan; entrega concluída = caixa + check.

A marca isolada é `liva.`. A assinatura de produto é `encomendas.liva`: minúsculas, apenas o ponto separador destacado em âmbar `#F0C78B`, sem ponto final adicional. **A marca é tipografia no layout (Plus Jakarta Sans), nunca lettering dentro das ilustrações.**

## Inventário v0.2 e responsabilidades

| Categoria | Caminho alvo | Conceito | Uso típico |
| --- | --- | --- | --- |
| Compartilhado | `assets/liva/shared/casa.png` | Uma casa isolada | Contexto residencial/horizontal |
| Compartilhado | `assets/liva/shared/predio.png` | Um prédio isolado | Contexto vertical |
| Compartilhado | `assets/liva/shared/portaria.png` | Uma guarita isolada | Operação de portaria |
| Encomendas | `assets/liva/products/encomendas/encomenda.png` | Uma caixa isolada | Recebimento e produto |
| Encomendas | `assets/liva/products/encomendas/leitura-ia.png` | Uma caixa + scan discreto | Processamento pela IA |
| Encomendas | `assets/liva/products/encomendas/entrega-concluida.png` | Uma caixa + check | Entrega confirmada |
| Encomendas | `assets/liva/products/encomendas/tudo-em-dia.png` | Caixa + check **temporariamente reutilizados** | Nenhuma encomenda pendente; distinguir pelo texto da UI |

Para `tudo-em-dia.png`, o v0.2 pode usar **a mesma arte** de `entrega-concluida.png`, mesmo que em dois arquivos, evitando gerar outra ilustração agora. O estado de nenhuma encomenda **jamais registrada** é diferente de ausência de pendências; o texto e os dados devem refletir isso.

## Especificação de produção

- Estilo: perspectiva isométrica uniforme, forma suave arredondada, volumes simples, luz e sombra discretas, sem hiper-realismo.
- Cores: verde liva `#77A899`, âmbar `#F0C78B`, areia `#F7EFE4`, sálvia `#E4EDE8`, verde profundo `#293D37`. Usar tons adicionais só quando essenciais para entendimento.
- Um asset por PNG, fundo verdadeiramente transparente, perfil sRGB; manter consistência visual e tamanho aparente entre arquivos.
- Sem palavras, números, logos, etiquetas legíveis ou decoração desnecessária.
- Sempre testar legibilidade em tamanhos pequenos. A imagem é ilustrativa, **não substitui ícone funcional ou rótulo textual**.

## Prompt-base v0.2

> Crie **um único objeto isométrico isolado** da identidade liva.: [OBJETO]. Perspectiva e escala consistentes com os objetos aprovados. Formas minimalistas, suavemente arredondadas, volumetria limpa, sombras discretas e paleta da liva. Apenas o objeto essencial, centralizado, reconhecível em 160px e com margens generosas. Fundo transparente. **Sem base, paisagismo, cenário, outros objetos, texto, números, lettering, logo ou efeitos decorativos.** Para estados compostos, permitir somente [OBJETO] + [MARCADOR FUNCIONAL MÍNIMO].

## Diretrizes de aplicação

- Usar imagens apenas quando oferecem contexto ou feedback (ex.: estado vazio, processamento de IA, confirmação), sem atrapalhar a rotina do porteiro.
- Botões e ações de interface usam ícones lineares convencionais e labels.
- Preservar fluxo de recebimento, revisão da IA, assinatura, filtros e compartilhamento, sem mudanças de negócio.
- Aplicar primeiro em branch de desenvolvimento, revisar acessibilidade, celular e iPad.
- Não publicar alterações em produção sem decisão explícita.

## Migração a partir do v0.1

**Situação conferida anteriormente no GitHub:** os PNGs v0.1 estão nos caminhos:
`shared/condominio.png`,
`products/encomendas/encomenda.png`,
`products/encomendas/leitura-ia.png`,
`products/encomendas/entrega-concluida.png`,
`products/encomendas/tudo-em-dia.png`.

**Estes caminhos não implicam que os arquivos sejam v0.2.** A atualização dos quatro PNGs de produto e a adição de `casa.png`, `predio.png`, `portaria.png` são pendências. O `condominio.png` antigo deve permanecer como legado até verificação de dependências; não apagar automaticamente. Confirmar arquivos novos no GitHub antes de alterá-los na aplicação.
