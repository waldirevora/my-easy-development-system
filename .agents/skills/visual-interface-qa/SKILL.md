---
name: visual-interface-qa
description: "Use para auditoria visual independente de websites, aplicativos web ou sistemas locais com interface renderizada, incluindo hierarquia, composição, responsividade, estados, legibilidade, acessibilidade visual e sinais de template genérico."
---

# Visual & Interface QA | Revisão independente

## Missão
Avaliar a experiência realmente renderizada, separadamente da implementação, para identificar problemas de estética, usabilidade e qualidade visual que testes de código não capturam.

## Quando ativar
- Entrega ou alteração visual relevante em website, portal, dashboard ou UI local.
- Verificação de responsividade, fluxos críticos, estados e consistência de design.
- Revisão de direção de arte premium e sinais de layout genérico/AI slop.

Não ativar para API sem UI ou alterações técnicas sem impacto visual.

## Independência
Preferir revisor distinto do executor e acesso a evidências reais (browser, screenshots, aplicativo em execução). Se não houver ambiente para visualizar a interface, declarar a limitação; não inventar que a inspeção foi realizada.

## Procedimento
1. Recuperar briefing, identidade, requisitos, estados e critérios de aceitação.
2. Examinar interface realmente renderizada em dimensões representativas: desktop, tablet, mobile quando web; janelas relevantes em desktop/local.
3. Conferir navegação e fluxos principais, inclusive loading, vazio, erro, confirmação e validação de formulário.
4. Avaliar hierarquia, espaçamento, tipografia, contraste, imagens, alinhamento, densidade, consistência e leitura.
5. Identificar problemas de overflow, corte, layout shift, foco visível, navegação por teclado e acessibilidade visual básica.
6. Verificar se o produto aparenta template genérico: cards repetitivos sem propósito, gradients/efeitos gratuitos, ícones redundantes, composição previsível e inconsistência de marca.
7. Registrar achados reproduzíveis com severidade, contexto, evidência e sugestão concreta.
8. Encaminhar correções ao responsável apropriado (Kael, Julian ou Clara), reinspecionar partes afetadas e registrar resultado.

## Severidade
- `BLOCKER`: impede tarefa crítica, conteúdo essencial ou acesso esperado.
- `HIGH`: falha relevante de legibilidade, contraste, responsividade ou hierarquia.
- `MEDIUM`: inconsistência visível com impacto moderado.
- `LOW`: refinamento cosmético sem impacto relevante.

## Limites
- QA visual não substitui testes funcionais, segurança, auditoria completa de acessibilidade ou performance.
- Não declarar WCAG 2.2 AA sem avaliação adequada.
- Não aprovar tela apenas com base no código, no mockup ou em suposições.

## Entrega
Relatório sucinto com telas/ambientes avaliados, achados, evidências, severidade, estado de correção e decisão `APPROVED`, `CHANGES_REQUIRED` ou `BLOCKED`. Não autorizar deploy no lugar do usuário.
