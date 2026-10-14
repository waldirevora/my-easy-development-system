# My Easy Development System Gate A Task Brief v1.0.1

**Versão:** 1.0.1. **Estado inicial:** Candidate.

## A. Finalidade e regras de uso

Este template ajuda a delimitar objetivo, resultado, escopo e autonomia em websites, sistemas empresariais, APIs, aplicações locais, dados, integrações e IA. Complementa [AGENTS.md](../AGENTS.md), o [Product System](../standards/product-system-v4.md) e o [Capability Routing](../standards/capability-routing-v1.md); não substitui a governança ou os Standards pertinentes.

- **Instrução simples e suficiente:** uma mensagem clara do responsável pode constituir Gate A. Dispensar o arquivo e o formulário em ajustes triviais suficientemente definidos.
- **Brief estruturado recomendado:** usar o modo completo quando múltiplos componentes, contratos, dados ou riscos exigirem delimitação adicional.
- **Lacuna material:** obter decisão antes da ação afetada, mantendo atividades independentes seguras e autorizadas.

Escolher um modo, copiar somente seu bloco e substituir os campos entre colchetes. Omitir campos inaplicáveis. Orientações fora dos blocos não precisam ser copiadas. O Codex pode preparar o brief com fatos verificados; seu preenchimento é proposta, não aprovação humana. Campo vazio, exemplo, silêncio ou aprovação técnica não concedem autorização.

## B. Modo rápido

Para tarefa simples e delimitada, usar apenas os cinco itens abaixo.

```markdown
Objetivo e resultado esperado: [o que corrigir ou produzir e qual resultado obter].
Superfície afetada: [página, arquivo ou componente e alcance].
Limites e proibições: [o que preservar e ações excluídas relevantes].
Conclusão observável: [condição verificável e conferência proporcional].
Autonomia autorizada: [atividades permitidas para executar, verificar e corrigir dentro desse alcance, sem microaprovações].
```

## C. Modo completo

Usar somente os campos pertinentes. Identificar ambientes e permissões por referência segura, nunca com valores de credenciais ou dados pessoais reais.

```markdown
Identificação da tarefa: [nome ou referência].
Contexto e baseline: [estado verificado, referências existentes e alterações preexistentes a preservar].
Problema a resolver: [comportamento atual e consequência].
Resultado esperado: [resultado de negócio ou técnico].
Escopo incluído: [alterações e atividades autorizadas].
Escopo excluído: [alterações e atividades não autorizadas].
Superfícies afetadas: [arquivos, componentes, fluxos ou contratos].
Contratos e decisões a preservar: [comportamentos, arquitetura e decisões aprovadas].
Dados, permissões e ambientes: [classificação, perfis, acesso e destinos autorizados; sem secrets].
Riscos e dependências: [impactos, reversibilidade, componentes existentes e limitações].
Entregáveis: [resultado concreto e relatório esperado].
Critérios de aceitação: [condições observáveis de sucesso, falha e limites].
Evidências e testes: [casos pertinentes, esperado, ambiente autorizado e evidência necessária].
Autonomia permitida: [análise, plano, implementação, verificações, correções, autorrevisão e documentação cobertas, sem microaprovações].
Interrupção/escalonamento: [lacunas ou mudanças materiais que bloqueiam a ação dependente].
Ações com autorização específica: [ação, alvo, ambiente, limites e referência da autorização válida; indicar pendentes ou proibidas].
Responsável pela decisão material: [pessoa ou papel e canal legítimo, quando necessário].
```

## D. Autonomia dentro do Gate A

Quando coberto pelo escopo aprovado, o Codex pode analisar, planejar, implementar, executar verificações autorizadas, corrigir defeitos, repetir testes afetados, fazer autorrevisão e preparar documentação/relatório. Não pedir aprovação por arquivo ou correção ordinária já coberta. Preservar contratos e limites; não presumir permissão para outras ações.

## E. Bloqueios e escalonamento

Quando não houver autorização prévia válida para a ação específica, solicitar decisão humana diante de mudança material de escopo ou segurança, produção, credenciais não autorizadas/ausentes, custo novo, destruição, risco de perda de dados, irreversibilidade, conflito com decisão aprovada, release/deploy ou outra ação protegida pelos Standards.

Interromper somente a ação dependente, informar motivo, impacto e alternativa segura e continuar atividades independentes autorizadas. Reutilizar decisões anteriores válidas no seu alcance; descoberta material que o ultrapasse exige nova decisão. Falha crítica conhecida bloqueia release e não pode ser dispensada por autorização genérica ou aprovação técnica.

## F. Relação com Gate B

Gate A não substitui Gate B humano para merge, push a branch protegida, release ou deploy. Testes concluídos, parecer `APPROVED` ou Security Gate favorável não autorizam essas operações. Autorização prévia válida só pode ser reutilizada para a ação, alvo, ambiente e limites concedidos, respeitando condições dos Gates e proibições expressas; não concede operações futuras genéricas.

Operações Git exigem autorização correspondente, inclusive add/commit e push remoto. Preservar Git manual quando reservado ao responsável. Preparar entrega ou relatório não autoriza versionar ou publicar.

## G. Seleção de Skills

Selecionar Standards existentes e Skills por objetivo, superfície, risco e fase, conforme Standard 03. Registrar capacidades necessárias e motivo somente quando ajudar a execução/revisão, no contexto ou relatório já previsto. Reavaliar se aparecer risco ou superfície nova; não exigir as 12 Skills nem leitura integral de todos os documentos em cada tarefa.

Usar Codex no desenvolvimento não exige `ai-engineering-production`. Essa Skill depende de componente real de IA ou necessidade especializada pertinente aos seus gatilhos. Selecionar capacidade não concede permissão de execução.

## H. Critérios de conclusão e relatório

Relatar proporcionalmente entregável, escopo efetivamente alterado, verificações executadas e resultados, limites de cobertura, segurança/regressão pertinentes, riscos, pendências e necessidade de Gate B. Identificar autorrevisão; não alegar independência inexistente. Security Gate e revisões exigidas dependem da superfície e do risco.

| Estado | O que pode ser declarado |
| --- | --- |
| Implementado | Alteração produzida; não implica testes, revisão ou aprovação. |
| Testado | Testes realmente executados e resultados registrados, com alcance e limitações. |
| Revisado | Alteração final examinada e achados tratados, identificando autorrevisão ou independência real. |
| Aprovado | Decisão humana registrada com alcance; parecer técnico não equivale a Gate B. |
| Publicado | Entrega autorizada realmente executada no destino indicado. |

Uma tarefa pode terminar pronta para revisão/aprovação, com publicação fora do escopo. Usar `PASS`, `FAIL`, `BLOCKED` e `NOT RUN` para testes conforme Product System; `NOT_APPLICABLE` justifica somente superfície inexistente: evidência essencial ausente não é `PASS`; teste necessário indisponível é bloqueado, não inaplicável. Inspeção suficiente para ajuste trivial deve ser relatada como inspeção. Não enfraquecer testes nem inventar evidências; mudança após verificação exige rever sua validade e repetir o que foi afetado.

## I. Exemplos de preenchimento

Exemplos sintéticos para copiar/adaptar, sem credenciais ou dados reais. As verificações são previstas, não resultados de testes executados.

### Exemplo 1: correção de rótulo

```markdown
Objetivo e resultado esperado: corrigir “Salavr” para “Salvar” na página existente de preferências.
Superfície afetada: somente o rótulo do botão nessa página.
Limites e proibições: preservar layout, lógica, dados e permissões; não adicionar dependências, executar Git mutável ou publicar.
Conclusão observável: texto final correto; conferir no arquivo e na página renderizada se houver efeito na leitura, registrando eventual limitação. Não exigir suíte completa sem efeito comportamental.
Autonomia autorizada: localizar, corrigir e conferir o rótulo, fazer autorrevisão e relatar o resultado, sem aprovação por arquivo.
```

### Exemplo 2: correção de autorização em API autenticada

```markdown
Identificação da tarefa: corrigir BOLA na consulta sintética GET /registros/{id}.
Contexto e baseline: API e política de acesso existentes; reproduzir em teste local isolado com usuários/tenants sintéticos.
Resultado esperado: usuário autenticado acessa somente ações e registros permitidos no componente confiável.
Escopo incluído: corrigir o controle da operação afetada e testes diretamente relacionados; preservar contratos e modelo de permissões aprovados.
Escopo excluído: produção, credenciais reais, migrations, dependências novas, mudanças globais de permissões, Git mutável e publicação.
Superfícies afetadas: GET /registros/{id}, validação de acesso e consulta pertinente; sem alteração de UI.
Dados, permissões e ambientes: dados sintéticos e acesso limitado ao ambiente local autorizado; sem chamadas a serviços reais.
Riscos e dependências: risco elevado de BOLA/IDOR e vazamento entre usuários/tenants; autenticação não substitui autorização.
Entregáveis: correção delimitada, testes pertinentes e relatório com Security Gate.
Critérios de aceitação: acesso legítimo preservado; acesso horizontal/vertical e entre tenants indevidos negado, sem exposição de registro ou alteração não autorizada.
Evidências e testes: executar positivos, troca de identificador/BOLA, chamada direta ao endpoint, negativos de privilégio/tenant e regressão afetada; registrar esperado, observado, comando e ambiente.
Autonomia permitida: investigar, planejar, corrigir no alcance aprovado, testar, repetir verificações afetadas e fazer autorrevisão sem microaprovações.
Interrupção/escalonamento: parar a ação dependente se a solução exigir produção, dado real, novo custo, migration ou mudança material fora do escopo; continuar análise segura autorizada. Não remover AuthZ para aprovar testes.
Ações com autorização específica: merge, push protegido, release e deploy permanecem pendentes de Gate B; falha crítica conhecida bloqueia release.
Responsável pela decisão material: responsável humano que aprovou a tarefa, no canal legítimo da conversa.
```

Neste segundo exemplo, avaliar `vera-architecture-security`, `software-design-solid` e `quality-engineering-testing`; acrescentar `data-persistence-engineering` se persistência/integridade forem afetadas. Não selecionar capacidades visuais ou AI Engineering apenas pelo uso do Codex.

## J. Evolução

Estado Candidate não comprova uso ou eficácia operacional. Revisar o template diante de evidências dos testes controlados e do piloto, por autorização e versionamento conforme Product System. Não criar regra nova de governança, log, formulário, sistema ou arquivo obrigatório por tarefa. A inspeção ampla desta autoria não é procedimento obrigatório para tarefas futuras.

| Versão | Estado | Registro |
| --- | --- | --- |
| 1.0 | Candidate | Modos rápido/completo, autonomia, limites, Gates, evidências e dois exemplos; validação de uso permanece posterior. |

Revisão corretiva 1.0.1 (13/10/2026): referências normativas sem versão fixa e consistência com a taxonomia de testes vigente, quando pertinente. Preserva Gates, responsabilidades e estado canônico. Ajuste documental autorizado na revisão final para publicação; não comprova nova validação operacional.
