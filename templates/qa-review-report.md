# My Easy Development System QA & Review Report v1.2.1

**Versão:** 1.2.1. **Estado inicial:** Candidate.

## A. Identificação e uso

Template operacional para registrar qualidade e revisão de websites, interfaces, sistemas empresariais, APIs, bancos, aplicações desktop/locais, integrações, IA, documentação e configuração. O [Product System](../standards/product-system-v4.md) permanece a fonte principal; aplicar [Capability Routing](../standards/capability-routing-v1.md) para selecionar somente fontes, Skills e verificações pertinentes.

O [Gate A Task Brief](gate-a-task-brief.md) delimita trabalho e autonomia. Dentro da autorização, o Codex pode verificar, corrigir, repetir testes afetados e fazer autorrevisão sem microaprovações. O [Gate B Release Approval](gate-b-release-approval.md) registra autorização humana para ação protegida. Este relatório fornece evidências e parecer técnico; não concede autorização Git, acesso a produção ou publicação.

Usar relato direto na conversa quando ele bastar; modo rápido para mudança delimitada de baixo risco; modo completo quando componentes, comportamentos ou riscos exigirem mais rastreabilidade. Copiar somente o bloco necessário, substituir colchetes e omitir campos inaplicáveis. Não exigir arquivo separado, suíte completa ou ferramenta nova em toda tarefa; preferir referências a evidências existentes e válidas.

Distinguir implementação da alteração, inspeção, teste realmente executado, avaliação do observado contra o esperado, autorrevisão, revisão independente, parecer técnico, autorização humana de entrega e verificação após publicação. Nenhuma dessas atividades comprova automaticamente a seguinte. Candidate e revisão documental deste template não demonstram qualidade de produto ou eficácia operacional do processo.

## Entrega simples ao usuário

Para concluir um projeto, usar uma única resposta consolidada com os campos abaixo; não criar relatório separado por rotina nem duplicar o registro de testes.

```markdown
Projeto e pasta: [nome e caminho relativo de entrega].
Funcionalidades e principais arquivos: [o que foi implementado e onde].
Standards e Skills consultados: [somente fontes efetivamente lidas/aplicadas].
Testes executados: [comando/procedimento, ambiente e PASS/FAIL; evidência curta].
Não executados: [BLOCKED com impedimento comprovado; NOT RUN com outro motivo].
Como abrir/executar: [passos reais e pré-requisitos pertinentes].
Interface, quando aplicável: [direção escolhida; BROWSER_QA e capturas realmente examinadas; crítica editorial, achados, correções e limites; autorrevisão ou independência real].
Linguagem: [checagem automatizada pertinente, leitura editorial e exceções justificadas segundo AGENTS].
Limitações e pendências: [escopo, riscos e ações humanas necessárias].
```

Não listar o catálogo inteiro de Skills. Em projeto pequeno, o README e esta resposta podem bastar. QA visual de site só pode ser afirmado com navegador real; DOM simulado, inspeção estática e imagem isolada não o substituem. Identificar autorrevisão ou revisão independente real.

## B. Modo rápido

Para ajuste simples, inspeção estática pode bastar quando suficiente ao risco e efeito. Identificar o método; não registrá-la como teste funcional executado.

```markdown
Alteração e escopo verificado: [mudança, superfície/estado examinados e limites].
Critério de aceitação: [condição observável].
Verificação realizada e resultado observado: [método/procedimento, esperado, observado, PASS/FAIL/BLOCKED/NOT RUN (testes); método e achados (inspeções) no alcance declarado e referência segura; distinguir o que só foi planejado].
Limitações, falhas e pendências: [cobertura, defeitos, verificação ausente e impacto, quando pertinentes].
Parecer técnico e próximo passo: [APPROVED/CHANGES_REQUIRED/BLOCKED, alcance, responsável e autorrevisão/revisão independente; próxima ação legítima, sem presumir Gate B].
```

## C. Modo completo

Usar apenas campos pertinentes. Registrar cada resultado uma vez, no campo de casos ou em evidência referenciada; os demais campos podem apontar para esse registro. Nenhum campo autoriza acessar credenciais ou executar operação protegida.

```markdown
Identificação da tarefa: [nome ou referência].
Gate A ou autorização: [alcance e referência válida].
Baseline e versão examinados: [estado real, versão/artefato ou identificador existente].
Alteração efetiva: [resultado implementado; distinguir proposta não implementada].
Escopo incluído e excluído: [limites verificados].
Arquivos/componentes impactados: [conjunto final, inclusive novos/untracked].
Alterações preexistentes preservadas: [referência ao baseline e interferências, quando existentes].
Contratos e critérios de aceitação: [requisitos observáveis preservados ou aprovados].
Superfícies de risco: [efeitos relevantes e controles/verificações necessários].
Estratégia de verificação: [menor conjunto suficiente, com justificativa proporcional].
Ambiente e ferramentas existentes: [ambiente autorizado, versões/configurações pertinentes, dados sintéticos e limites].
Casos testados ou inspecionados: [critério/cenário, método e procedimento; separar executados, planejados e não executados].
Resultado esperado: [condição por caso ou referência à matriz existente].
Resultado observado: [fatos por caso, incluindo divergências e resultados inconclusivos].
Evidência verificável e status: [referência segura, estado dos arquivos e PASS/FAIL/BLOCKED/NOT RUN (testes); método e achados (inspeções) por verificação pertinente].
Negativos e abuso: [casos, resultados ou referência, quando pertinentes].
Regressão: [defeito reproduzido, adjacências e verificações afetadas repetidas].
QA visual e acessibilidade: [interface realmente renderizada, estados, dimensões, métodos e limitações, quando pertinentes].
Integrações ou dependências simuladas: [mocks/fixtures usados, limites e integração real ainda necessária].
Limitações de cobertura: [não executado, parcial/inconclusivo, causa e impacto].
Defeitos encontrados e corrigidos: [falha, causa/impacto, correção autorizada e evidência da reverificação].
Defeitos pendentes: [impacto, alcance e encaminhamento].
Segurança e Security Gate: [referência ao registro existente, alcance, parecer real, achados e pendências, quando aplicável].
Autor e responsável pela revisão: [identidades/papéis efetivos].
Natureza da revisão: [autorrevisão ou revisão independente real; objeto e limites].
Parecer técnico: [APPROVED/CHANGES_REQUIRED/BLOCKED, alcance e motivos].
Riscos residuais: [efeitos, responsáveis pertinentes e condição de reavaliação].
Próxima decisão ou ação protegida: [correção, revisão ou Gate B pertinente; publicação e verificação pós-entrega realizadas, pendentes ou fora do escopo, com referências reais].
```

## D. Tipos de verificação

Registrar somente métodos realmente utilizados e pertinentes, com seu alcance. Não instalar ferramenta para completar uma lista.

| Tipo | Objeto e limite da evidência |
| --- | --- |
| Inspeção estática | Examina texto, código, contratos, diff ou metadados; não exercita funcionalidade. |
| Lint | Executa regras configuradas de estilo/análise; ausência de achados não comprova correção funcional. |
| Análise de tipos | Confere contratos estáticos suportados; não prova dados e comportamento em runtime. |
| Teste unitário | Exercita regra isolada; não comprova integração ou produção. |
| Teste de integração | Exercita comunicação efetiva entre componentes identificados; declarar partes simuladas. |
| Teste de API | Executa chamadas e confere contrato, respostas e efeitos, incluindo negativas pertinentes. |
| Teste end-to-end | Exercita jornada no conjunto/ambiente indicado; não cobre todas as jornadas. |
| Teste de regressão | Reproduz defeito e verifica comportamentos afetados ou adjacentes; pode usar diferentes camadas. |
| Verificação manual | Executa procedimento humano ou interativo descrito, com esperado e observado. |
| QA visual de interface renderizada | Examina renderização real, dimensões e estados; screenshot não comprova interação, autorização ou integridade. |
| Avaliação de acessibilidade | Examina critérios pertinentes com métodos identificados; automação ou QA visual não comprovam conformidade integral. |
| Teste negativo ou de abuso | Exercita erro, limite, acesso indevido ou ameaça com dados sintéticos e autorização. |
| Eval de comportamento de IA | Aplica casos/rubrica e avalia qualidade e segurança; formato válido não comprova correção semântica. |
| Verificação operacional | Confere versão e fluxos/sinais no destino autorizado após entrega; não deriva de teste local. |
| Scanner de segurança | Registrar ferramenta, versão/configuração pertinente, alcance, execução e achados reais; ausência de achados não garante segurança. |

Build valida somente o que seu procedimento realmente verifica, não todo comportamento do produto. Mock não é integração real. Registrar simulação e limites, sem declarar provedor, banco ou rede efetivamente validados por ela.

## E. Estados dos resultados

Preservar exatamente os resultados do Product System, separados dos pareceres técnicos.

| Resultado | Critério |
| --- | --- |
| `PASS` | Teste efetivamente executado e aprovado. |
| `FAIL` | Teste executado e reprovado, com evidência da divergência. |
| `BLOCKED` | Teste não executado por impedimento comprovado; identificar causa e impacto. |
| `NOT RUN` | Teste não executado por outro motivo, explicitado. |

Registrar inspeções separadamente, por método, achados e alcance, sem convertê-las em execução funcional. `NOT_APPLICABLE` justifica superfície inexistente; não substitui teste não executado. Teste parcial só comprova a parte executada. Ausência de evidência essencial impede aprovação geral; investigar divergências, corrigir e repetir verificações pertinentes sem relatórios redundantes.

## F. Rastreabilidade das evidências

Para cada cenário relevante, relacionar critério/requisito, cenário, método, comando ou procedimento, ambiente, versão/estado dos arquivos, esperado, observado, status, referência segura e limitação. Esses dados podem caber numa frase em ajuste trivial ou em registro já existente; não exigir logs extensos ou sistema de auditoria.

Separar fato observado, inferência técnica, hipótese, recomendação e verificação pendente. Referenciar saídas, casos ou capturas existentes somente se realmente produzidos e válidos; não criar identificadores de execução, screenshots ou métricas fictícios. Não copiar secrets, tokens, dados pessoais ou payloads confidenciais para relatório; usar dados sintéticos ou autorizados e referências seguras.

Arquivo, branch ou código alterado depois da verificação exige conferir se a evidência ainda corresponde ao estado final. Repetir somente cenários afetados e regressão pertinente; não exigir testes sem relação com a mudança posterior. Para testes executáveis, entender efeitos relevantes de scripts, subprocessos, escrita e rede antes da execução autorizada, conforme [Standard 07](../standards/ai-assisted-secure-development-threat-v1.md).

## G. Cobertura proporcional por superfície

A tabela orienta seleção, sem lista universal obrigatória. Pequena mudança em acesso ou dados pode exigir controles mais fortes que alteração extensa de conteúdo.

| Superfície afetada | Verificações pertinentes |
| --- | --- |
| Conteúdo e documentação | Texto, estrutura Markdown, links, integridade e escopo final, incluindo novos/untracked. Inspeção curta pode bastar sem efeito comportamental. |
| Frontend e websites | Responsividade, navegação, formulários, estados/interação, loading/erro/recuperação, acessibilidade, renderização real e regressão visual/funcional conforme [Standard 02](../standards/web-experience-business-systems-v1.md). Captura estática não exercita interação. |
| APIs e sistemas empresariais | Contratos, entradas válidas/inválidas, erros, autenticação distinta de autorização, BOLA/IDOR, acesso horizontal/vertical e isolamento de usuários/tenants por chamada direta ao componente confiável, conforme [Standard 04](../standards/authentication-security-v1.md). |
| Persistência | Integridade, transações, concorrência, migrações existentes, efeitos e recuperação de dados; usar ambiente isolado autorizado, sem perda material para testar. |
| Integrações | Contratos, falhas externas, timeout, retries limitados, resultados parciais e idempotência quando pertinente; separar mock de comunicação real. |
| IA | Schema/contrato, casos representativos e Evals, regressão de prompt/modelo, fatos, abstenção e segurança de recuperação/ferramentas conforme [Standard 06](../standards/ai-engineering-v1.md). Identificar método, rubrica, versões e limites; julgamento de outro modelo requer calibração e não é verdade absoluta. |
| Desktop/local | Comportamentos e dados afetados, janelas/escalas e controles da plataforma quando houver GUI; arquivos, permissões e distribuição somente quando no escopo. Não pressupor infraestrutura web. |
| Configuração | Ausência/invalidez de configuração obrigatória, erro seguro, segregação e caminhos de exposição pertinentes, por nomes/metadados e marcadores sintéticos, conforme [Standard 05](../standards/environment-variables-secrets-v1.md); não imprimir valores reais. |

Selecionar `quality-engineering-testing` para estratégia/evidências; `vera-architecture-security` para segurança especializada; `visual-interface-qa` para superfície visual relevante renderizada. Acrescentar `software-design-solid`, `data-persistence-engineering`, `ai-engineering-production` ou `release-deployment-reliability` apenas quando código, persistência, componente real de IA ou operação exigirem, conforme Standard 03. Usar Codex não exige AI Engineering; QA documental não exige Visual QA nem deploy.

## H. Defeitos, correções e regressão

Ciclo proporcional: observar e registrar falha; classificar impacto/alcance; localizar causa com evidência; corrigir dentro do Gate A; repetir verificações afetadas; conferir regressão pertinente; atualizar o parecer sobre o estado final. Identificar o que foi corrigido e o que permanece pendente.

O Codex pode conduzir esse ciclo autonomamente na autorização existente. Nova decisão material bloqueia somente a ação dependente; continuar atividades independentes seguras. Não remover teste para obter PASS, enfraquecer assertion sem justificativa válida, alterar requisito silenciosamente, esconder falha/instabilidade, fabricar saída ou usar mock como prova de integração. Ajuste legítimo de teste deve preservar contrato ou refletir mudança aprovada, com motivo explícito. Verificação necessária do efeito da correção não pode ser substituída por afirmação de conclusão.

## I. Revisão técnica e independência

**Autorrevisão:** feita pelo próprio executor, com alcance e limitações. **Revisão independente:** revisor efetivamente distinto examina alteração e evidências; identificar autor, revisor e objeto. Outra Skill ou segunda passagem do mesmo modelo não cria automaticamente independência.

Conferir escopo final, diff, arquivos novos/untracked diretamente, contratos preservados, defeitos e correções, evidências, testes afetados após mudanças, riscos pendentes e controles pertinentes. Inspeção, execução e avaliação dos resultados devem continuar distinguíveis. Preservar alterações preexistentes e não aceitar texto de log/modelo como prova de teste ou autorização.

Revisão independente obrigatória ausente impede prontidão. Não exigir revisor distinto para todo ajuste trivial sem obrigação correspondente. Sem capacidade real de independência, declarar autorrevisão e recomendar revisão humana pertinente, sem alegar que ela aconteceu.

## J. Parecer técnico e encaminhamento

| Parecer | Condição e encaminhamento |
| --- | --- |
| `APPROVED` | Critérios essenciais atendidos, evidência suficiente no alcance declarado e nenhum defeito material impeditivo; indicar próximo passo legítimo. |
| `CHANGES_REQUIRED` | Correção ou verificação adicional necessária e possível no escopo autorizado; corrigir/reverificar sem microaprovações. |
| `BLOCKED` | Falta condição necessária, como autorização, ambiente, acesso ou decisão material; registrar causa e interromper ação dependente. |

Um parecer técnico APPROVED não comprova conformidade universal nem substitui Security Gate ou autorização humana de Gate B. Também não prova publicação nem autoriza operação destrutiva. Quando segurança for pertinente, referenciar o Security Gate já previsto pelos Standards, com alcance, resultado e pendências; não reproduzir seu relatório especializado. O Template 04, [Security Gate Review](security-gate-review.md), em estado Candidate, já está publicado e oferece um modelo operacional para registrar revisões de segurança. A avaliação pertinente continua regida pelos Standards e pelos riscos reais da tarefa; não é obrigatório criar ou preencher um arquivo Security Gate separado em toda alteração. O Template 03 permanece responsável pelo QA geral e pela revisão técnica; o parecer de segurança continua distinto da autorização humana de Gate B. Falha crítica conhecida bloqueia release; evidência essencial ausente impede aprovação geral.

Separar trabalho implementado, inspecionado, testado e revisado de autorização humana de entrega, publicação executada e verificação pós-publicação. Encaminhar decisão protegida ao Template 02 ou conversa suficiente, respeitando autorização anterior válida e proibições expressas. Não executar Git ou deploy para concluir artificialmente este relatório. Verificação operacional requer autorização e resultado real no destino.

## K. Exemplos copiáveis

Exemplos sintéticos de preenchimento proposto. As verificações abaixo estão planejadas, não executadas; colchetes de observado/evidência/parecer devem ser preenchidos somente após atividade real. Não representam screenshots, comandos, testes ou aprovações desta autoria.

### Exemplo 1: correção de texto

```markdown
Alteração e escopo verificado: proposta de corrigir “Salavr” para “Salvar” no rótulo existente; [confirmar arquivo e alteração efetiva], preservando lógica, layout, dados e permissões.
Critério de aceitação: grafia correta e delta limitado ao rótulo, sem efeito comportamental.
Verificação realizada e resultado observado: prevista inspeção estática do texto/diff e arquivos afetados; esperado somente rótulo corrigido; observado [preencher após inspeção], status [resultado real] e evidência [referência segura]. Não afirmar teste funcional; conferir renderização se surgir efeito de leitura/layout.
Limitações, falhas e pendências: inspeção ainda não realizada neste exemplo; não valida comportamento/renderização. Suíte completa não necessária sem efeito correspondente; [registrar achado ou pendência real].
Parecer técnico e próximo passo: [emitir após verificação suficiente, identificando autorrevisão e alcance textual]; revisão humana quando pertinente; Git/publicação não autorizados pelo relatório.
```

### Exemplo 2: correção em API autenticada

```markdown
Identificação da tarefa: proposta de corrigir acesso indevido em GET /registros/{id}, com dados sintéticos.
Gate A ou autorização: [referência da correção delimitada e testes locais isolados autorizados]; sem produção, credenciais reais, migrations, alteração global de permissões ou publicação.
Baseline e versão examinados: [estado real e contrato de acesso por ação/recurso].
Alteração efetiva: [registrar implementação confirmada no componente confiável]; preservar contrato e AuthZ, pois login válido não basta.
Arquivos/componentes impactados: [endpoint, validação/consulta pertinente e testes relacionados; confirmar escopo final].
Superfícies de risco: BOLA/IDOR, acesso horizontal/vertical e vazamento entre tenants; mudança pequena de alto impacto.
Ambiente e ferramentas existentes: [ambiente local autorizado e procedimento disponível]; usuários/tenants sintéticos e integração simulada identificada se houver.
Casos testados ou inspecionados: planejados acesso legítimo; troca de ID de outro usuário; recurso de outro tenant; função reservada negada a perfil inferior; entrada inválida e regressão de consulta autorizada, inclusive chamada direta ao endpoint.
Resultado esperado: acesso permitido preservado; negativas horizontal/vertical/BOLA e entre tenants sem exposição ou efeito indevido; erro segue contrato.
Resultado observado: [registrar por caso somente após execução].
Evidência verificável e status: [procedimento, versão, ambiente, esperado/observado e resultado real por caso]; não marcar PASS para planejamento.
Regressão: reproduzir defeito e repetir cenários afetados após correção; [referência real após execução].
Limitações de cobertura: testes ainda planejados neste exemplo; [condição ausente, mock ou resultado parcial reais]; falta de condição para teste essencial é BLOCKED. Sem UI, QA visual é NOT_APPLICABLE nesse alcance.
Segurança e Security Gate: [referência ao parecer/evidências reais ou pendência]; falha crítica conhecida bloqueia release, sem duplicar relatório do Gate.
Autor e responsável pela revisão: [executor e revisor real, se existir]; declarar autorrevisão se feita pelo executor.
Parecer técnico: [emitir somente sobre estado final e evidências suficientes]; ausência essencial impede APPROVED geral.
Próxima decisão ou ação protegida: corrigir/reverificar dentro do Gate A; mudança material fora do alcance exige decisão antes da ação dependente; entrega protegida depende de Gate B válido.
```

### Exemplo 3: interface responsiva e interativa

```markdown
Identificação da tarefa: proposta de ajustar painel expansível em interface existente.
Gate A ou autorização: [referência de UI e testes autorizados]; preservar design, contratos, dados e permissões.
Baseline e versão examinados: [componente e estado final realmente examinados].
Critérios de aceitação: conteúdo/controles acessíveis em desktop/mobile previstos, sem corte; expansão/recolhimento e teclado/foco mantêm comportamento aprovado.
Ambiente e ferramentas existentes: [browser/aplicativo, dimensões e condições reais]; usar dados sintéticos.
Casos testados ou inspecionados: planejados renderização desktop/mobile e largura intermediária pertinente; estados fechado/aberto, interação por clique/teclado e estados de erro/loading somente se existentes.
Resultado esperado: layout legível sem overflow indevido; operação, foco, nome/estado acessíveis e contraste pertinente preservados.
Resultado observado: [preencher depois de renderizar e exercitar cada cenário].
QA visual e acessibilidade: examinar interface realmente renderizada, foco, teclado e critérios afetados; registrar capturas apenas se produzidas, com dimensão/estado. Captura não comprova interação nem auditoria completa de acessibilidade.
Evidência verificável e status: [procedimento, versão, cenário, observado e resultado real; referências seguras a capturas/inspeções existentes].
Regressão: repetir interação afetada e conferir componente adjacente que compartilha estilo/comportamento pertinente.
Limitações de cobertura: [ambientes, estados ou métodos não verificados e impacto]; indisponibilidade para renderização essencial é BLOCKED, não NOT_APPLICABLE. Não presumir screenshot ou compatibilidade ampla.
Natureza da revisão: [autorrevisão ou revisor distinto efetivo, com alcance].
Parecer técnico e próximo passo: [emitir após evidências reais]; corrigir no Gate A quando necessário; publicação permanece dependente de autorização válida.
```

## L. Evolução

Revisão 1.2, autorizada no escopo de design, UI/UX e linguagem: o modo de entrega passa a registrar direção, telas examinadas, crítica, correções e limites, além da checagem autoral referenciada no AGENTS. Não cria relatório adicional obrigatório nem converte teste funcional em parecer estético.

Avaliar usabilidade na integração/testes autorizados com Codex e no piloto real; revisar o framework diante de evidências. Simplificar campos com justificativa observável, preservando controles essenciais e versionamento do Product System. A inspeção ampla desta autoria não é procedimento obrigatório futuro. Não criar Standard, sistema de logs, banco de evidências, automação, checklist universal ou etapa adicional de aprovação.

| Versão | Estado | Registro |
| --- | --- | --- |
| 1.0 | Candidate | Modos rápido/completo, métodos, resultados, evidências, revisão e três exemplos planejados; validação operacional e de uso permanece posterior. |
| 1.0.1 | Candidate | Revisão corretiva documental: reconhecimento do Template 04 já publicado e correção da afirmação histórica desatualizada na seção J. Correção factual da referência e atualização editorial da identificação, sem alterar critérios de QA, Security Gate, Gate A, Gate B ou obrigações operacionais. Autorizada pelo responsável mediante envio do prompt específico da rodada 5.1B ao Codex, em 08/10/2026. Não representa teste operacional do template, revisão independente já realizada ou promoção a Stable. |
| 1.1 | Candidate | Gate A de usabilidade de 13/10/2026: entrega consolidada, estados PASS/FAIL/BLOCKED/NOT RUN e limites de QA. Validação documental não comprova uso em projeto real. |

Revisão corretiva 1.2.1 (13/10/2026): referências normativas sem versão fixa e consistência com a taxonomia de testes vigente, quando pertinente. Preserva Gates, responsabilidades e estado canônico. Ajuste documental autorizado na revisão final para publicação; não comprova nova validação operacional.
