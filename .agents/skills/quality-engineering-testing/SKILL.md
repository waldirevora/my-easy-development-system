---
name: quality-engineering-testing
description: "Use ao definir, implementar, revisar e executar testes em websites, sistemas locais ou web, APIs e integrações; cobre estratégia por risco, unitários, integração, contrato, E2E, negativos, regressão e evidências reais."
---

# Quality Engineering & Testing

## Missão
Produzir evidência verificável de que a entrega atende aos requisitos e não introduz regressões materiais, utilizando o menor conjunto suficiente de testes.

## Ativação
- Mudanças funcionais ou correções de bugs.
- Integrações, APIs, autenticação, bancos, migrations e componentes de IA.
- Alterações visuais com comportamento e responsividade.
- Preparação de release e investigação de falhas.

Para alteração trivial sem impacto comportamental, usar verificação proporcional em vez de suítes completas.

## Estratégia
1. Relacionar requisitos e critérios de aceitação a cenários testáveis.
2. Classificar risco, probabilidade, impacto e componentes afetados.
3. Escolher camadas adequadas: unitário, integração, contrato, E2E, smoke, regressão e exploração manual.
4. Incluir casos normais, limites, entradas inválidas, erros externos, concorrência e abuso quando relevantes.
5. Preparar fixtures/dados sintéticos, isolamento e limpeza dos testes.
6. Rodar os testes disponíveis, investigar falhas e repetir os afetados após a correção.
7. Documentar comando, ambiente, saída e resultados, inclusive o que não foi possível executar.

## Critérios técnicos
- Testar comportamento e contratos, não detalhes frágeis de implementação.
- Testes devem ser legíveis, determinísticos e independentes sempre que viável.
- Preferir ferramentas nativas/ecossistema existentes; não instalar pacotes desnecessários.
- Não simular resultados passando artificialmente nem enfraquecer asserts.
- Não transformar testes flaky em testes ignorados sem causa documentada.
- Não utilizar secrets ou dados reais de produção como fixtures.
- Verificar autorização e isolamento multiusuário em sistemas autenticados.
- Executar evals específicas se o componente de IA exigir, em coordenação com `ai-engineering-production`.
- Para UI, coordenar testes técnicos com `visual-interface-qa`.

## Ciclo autônomo de correção
Ao identificar `FAIL`:
1. reproduzir e identificar a causa;
2. corrigir dentro do escopo autorizado;
3. repetir teste afetado e regressão relacionada;
4. encaminhar para revisão independente quando aplicável;
5. parar e sinalizar blocker quando houver risco ou mudança material de escopo.

## Evidência e relatório
Para cada cenário importante registrar:
- identificador e requisito;
- resultado esperado e observado;
- ambiente/comando;
- evidência;
- status `PASS`, `FAIL`, `BLOCKED` ou `NOT_APPLICABLE`;
- limites de cobertura e riscos residuais.

Não afirmar aprovação geral se testes essenciais falharam ou não foram executados.

## Saída
Apresentar resumo da cobertura efetiva, falhas, correções, testes executados, bloqueios e recomendação para o Gate B. Não realizar merge, release ou deploy sem autorização.
