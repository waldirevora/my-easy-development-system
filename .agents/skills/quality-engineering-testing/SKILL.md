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
- status de teste `PASS` (executado e aprovado), `FAIL` (executado e reprovado), `BLOCKED` (não executado por impedimento comprovado) ou `NOT RUN` (não executado por outro motivo);
- limites de cobertura e riscos residuais.

Registrar inspeções por método, achados e alcance; inspeção estática não substitui execução funcional. NOT_APPLICABLE justifica superfície inexistente, sem substituir teste não executado. DOM simulado e imagem isolada não substituem QA de site em navegador real. Não inventar evidências nem alegar QA visual sem navegador.

Selecionar conforme o produto:

- Site: responsividade, acessibilidade, interações, links, assets, contraste e QA no navegador disponível.
- API: endpoints, validações, contratos, tratamento de erros, testes automatizados e segurança proporcional.
- Autenticação: controle de acesso, sessão, autorização por recurso, credenciais e casos negativos.

Não afirmar aprovação geral se testes essenciais falharam ou não foram executados.

## Saída
Apresentar resumo da cobertura efetiva, falhas, correções, testes executados, bloqueios e recomendação para o Gate B. Não realizar merge, release ou deploy sem autorização.
