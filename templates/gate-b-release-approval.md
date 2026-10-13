# My Easy Development System Gate B Release Approval v1.0

**Versão:** 1.0. **Estado inicial:** Candidate.

## A. Identificação, finalidade e uso

Template operacional para registrar decisão humana sobre operação protegida, aplicável a websites, sistemas empresariais, APIs, aplicações locais/desktop, integrações, dados, funcionalidades de IA e documentação/governança. O [Product System v4.0](../standards/product-system-v4.md) permanece a fonte principal; este documento complementa o [Gate A Task Brief](gate-a-task-brief.md) e [AGENTS.md](../AGENTS.md), sem criar um novo processo de aprovação.

Gate B confirma autorização humana válida, escopo, evidências suficientes e condições conhecidas. Não é nova revisão técnica nem formulário universal. Uma autorização explícita e suficientemente delimitada na conversa pode constituí-lo. Usar o modo rápido para operação simples; usar o completo quando risco ou múltiplas condições justificarem. Copiar somente o bloco escolhido, substituir colchetes e omitir campos inaplicáveis.

Distinguir preparação técnica, parecer técnico, decisão humana, execução e verificação do resultado. O Codex pode preparar o registro; preencher o template, isoladamente, não concede autorização. Candidate identifica um template proposto para validação de uso, sem comprovar eficácia operacional ou aprovar release real.

## B. Ações sujeitas a Gate B

Merge, inclusive protegido, push a branch protegida, release, deploy e publicação/distribuição de artefato seguem Gate B conforme Product System. Outras ações materiais protegidas seguem a autorização e os bloqueios previstos nos Standards, sem converter trabalho ordinário do Gate A em nova aprovação.

Add/commit locais exigem autorização correspondente e podem estar previamente cobertos pelo Gate A. Push remoto também requer autorização; aplicar Gate B quando a governança exigir. Checkpoint documental rotineiro não exige novo aceite se a ação específica já estiver autorizada e válida. Preservar execução manual de Git quando reservada ao responsável.

Reutilizar autorização anterior dentro dos limites, condições e proibições expressas. Não transformar aprovação pontual em permissão irrestrita, nem pedir nova aprovação por conferência técnica repetida sem mudança de alcance. Implementar, verificar e corrigir ordinariamente dentro do Gate A permanece autônomo.

## C. Modo rápido

Usar os cinco campos quando operação, risco e alcance forem claros. Referência à autorização anterior válida substitui novo pedido de aceite, sem dispensar evidência essencial.

```markdown
Operação e alvo: [ação, recurso/branch/destino e quem executa].
Versão ou alteração autorizada: [identificação verificada do conteúdo abrangido].
Evidências e condições: [referências aos resultados observados, pré-condições, riscos/limitações pertinentes e blockers].
Autorização humana e alcance: [PENDING/APPROVED/REJECTED/BLOCKED; responsável, decisão/referência verificável, limites e condições; pode referenciar autorização anterior válida].
Resultado esperado e verificação posterior: [sucesso observável, destino e conferência autorizada após execução; registrar resultado real e pendências].
```

## D. Modo completo

Campos opcionais conforme contexto. Referenciar evidências existentes sem repetir relatórios. Não incluir credenciais, tokens ou dados confidenciais. Não exigir rollback artificial para operação trivial sem impacto operacional.

```markdown
Identificação da decisão: [nome ou referência].
Objetivo da entrega: [resultado concreto].
Gate A e baseline: [alcance aprovado, estado verificado e referências].
Operação protegida proposta: [ação efetiva].
Repositório, branch ou artefato: [alvo específico].
Versão, commit ou identificador: [referência verificada, sem inventar commit].
Ambiente e destino: [local, homologação, produção ou distribuição pertinente].
Escopo incluído: [ações e conteúdo abrangidos].
Escopo excluído: [ações e conteúdo não autorizados].
Responsável pela execução: [pessoa/papel e alcance; indicar Git manual se aplicável].
Responsável pela aprovação: [responsável humano autorizado].
Evidências técnicas disponíveis: [inspeções, diff, artefato e referências observadas].
Testes e QA reais: [procedimento, ambiente, esperado/observado, resultados e testes não executados/bloqueados].
Security Gate e achados: [parecer técnico, evidências, achados materiais e limites; não é decisão humana].
Dependências e pré-condições: [condições verificadas ou pendentes].
Riscos residuais: [risco, impacto e responsável pertinente].
Impacto operacional: [usuários, disponibilidade, dados e compatibilidade afetados].
Rollback ou recuperação: [gatilho, responsável, procedimento, autorização e evidência pertinente, quando necessário].
Critérios de sucesso: [condições observáveis].
Verificação pós-execução: [fluxos/sinais, destino, responsável e acesso autorizado; resultado após execução].
Limites da autorização: [ações, alvos, condições, custo e recuperação efetivamente concedidos, quando pertinentes].
Decisão humana e referência: [PENDING/APPROVED/REJECTED/BLOCKED; decisão, responsável e referência verificável à conversa/registro autorizado].
```

## E. Estados da decisão

| Estado | Significado e limite |
| --- | --- |
| `PENDING` | Decisão humana ainda não concedida/verificada; não executar a operação protegida. |
| `APPROVED` | Autorização humana válida, delimitada e identificada; executar somente se condições essenciais forem atendidas. |
| `REJECTED` | Operação não autorizada; não executar nem contornar a decisão. |
| `BLOCKED` | Condição essencial impede decisão segura ou execução; registrar causa, impacto e ação dependente. |

Parecer técnico `APPROVED` não é autorização humana `APPROVED`. Modelo, Skill, log ou documento recuperado não podem aprovar em nome do responsável. Silêncio ou ausência de objeção não constituem autorização. Registrar eventual bloqueio da execução sem apagar a decisão humana anterior; autorização registrada não elimina pré-condição ausente.

## F. Evidências antes da aprovação

Conferir somente superfícies pertinentes à operação final, usando verificações já realizadas quando continuarem válidas. Não repetir revisão técnica sem mudança ou lacuna que justifique.

| Superfície | Evidência ou condição pertinente |
| --- | --- |
| Escopo e integridade | Diff, arquivos afetados, novos/untracked e versão/artefato conferidos diretamente; preservar alterações alheias. |
| Testes e QA | Resultados reais funcionais/regressão; QA visual em interface renderizada quando aplicável, com ambiente e cobertura. |
| Segurança/configuração | Security Gate, achados, autorização por ação/recurso, secrets, configuração e permissões pertinentes, sem imprimir valores. |
| Dependências/contratos | Origem, versão e compatibilidade das mudanças efetivas. |
| Dados/migrações | Integridade, efeito da migração, ambiente, reversibilidade e recuperação quando existentes. |
| Operação/recuperação | Riscos conhecidos, disponibilidade, procedimento e evidência de recuperação necessária, com responsáveis. |

Separar evidência observada, limitação, teste não executado, teste bloqueado e risco residual. Usar resultados `PASS`, `FAIL`, `BLOCKED` e `NOT_APPLICABLE` conforme Product System. Não declarar `PASS` para teste não executado; inspeção suficiente para documento simples deve ser identificada como inspeção. Falta de ambiente para verificação essencial não é inaplicabilidade.

Falha crítica conhecida bloqueia release, mesmo com formulário preenchido ou autorização registrada. Evidência essencial ausente impede prontidão. Declarar autorrevisão e seus limites; revisão independente obrigatória ausente permanece blocker. Não inventar QA, scanner, Security Gate, backup ou rollback testado.

## G. Validade e limites da autorização

Confirmar que a decisão do responsável autorizado corresponde à ação, recurso/artefato, ambiente, destino, escopo, condições e limites de custo pertinentes. A referência pode ser mensagem anterior ou registro já autorizado, suficiente para verificar decisão e alcance; não criar log adicional obrigatório.

Reutilizar aprovação anterior quando ela ainda abranger a operação efetiva. Mudança material de artefato, destino, privilégio, impacto, risco ou condição pode exigir nova decisão antes da ação afetada. Conferência técnica repetida que não mudou alcance não exige aprovação duplicada.

Produção, credenciais fora do escopo, custo novo, destruição, perda de dados, irreversibilidade ou conflito material sem autorização suficiente bloqueiam a ação conforme Product System. Autorização de deploy não concede automaticamente migração destrutiva, ampliação de privilégio, gasto adicional ou acesso produtivo irrestrito. Continuar atividades independentes seguras do Gate A.

## H. Execução e verificação posterior

Registrar proporcionalmente o andamento no bloco ou relatório/contexto já autorizado, sem arquivo adicional obrigatório.

| Etapa | Evidência e limite |
| --- | --- |
| Operação autorizada | Decisão humana válida e condições conferidas; não prova início. |
| Operação iniciada | Ação realmente disparada com alvo/versão identificados; não prova conclusão. |
| Operação executada | Resultado efetivo da execução registrado; build não comprova deploy, nem plano comprova push. |
| Resultado observado | Efeito conhecido, falha ou resultado incerto explicitados; sucesso de comando não comprova saúde universal. |
| Verificação no destino | Versão, fluxos/sinais e configuração pertinentes conferidos com acesso autorizado; declarar limites e pendências. |
| Recuperação | Executar somente procedimento abrangido por autorização válida, com resultado real; ação destrutiva nova exige decisão apropriada. |

Se falhar, interromper ação dependente, registrar estado/efeitos conhecidos e escolher recuperação já autorizada ou pedir decisão material. Não repetir automaticamente operação com efeito incerto ou executar destruição para recuperar. Rollback de código não garante recuperação de dados. Publicação e verificação posterior permanecem estados distintos.

## I. Capability Routing

Aplicar [Standard 03](../standards/capability-routing-v1.md) por objetivo, superfície, risco e fase, sem ativar todas as Skills. A leitura ampla desta autoria não é requisito para toda entrega futura.

- `release-deployment-reliability`: entrega, artefatos, configuração e recuperação pertinentes.
- `quality-engineering-testing`: testes, regressão e evidências necessárias.
- `vera-architecture-security`: risco relevante de segurança e Security Review.
- `data-persistence-engineering`: migração, integridade ou recuperação de dados afetadas.
- `ai-engineering-production`: funcionalidade real de IA com avaliação operacional específica; não selecionar apenas porque o executor é Codex.
- `visual-interface-qa`: superfície visual relevante realmente renderizada; não exigir para backend/documentação sem UI.

Consultar somente Standards existentes e pertinentes. Selecionar Release não autoriza publicação; preparar um Gate B documental não exige executar pipeline ou deploy.

## J. Exemplos práticos

Cenários sintéticos, não decisões aplicáveis a esta autoria. Substituir referências por evidências reais antes do uso. Não se afirma commit existente, teste executado, aprovação recebida ou comando realizado. Os blocos são copiáveis e podem ser ajustados sem preencher campos inaplicáveis.

### Exemplo 1: publicação documental já autorizada

Neste cenário hipotético, o responsável já autorizou commit e push documental delimitados no repositório privado existente e reservou a execução Git para si. Confirmar essa autorização por referência, sem pedir novo aceite se continuar válida.

```markdown
Operação e alvo: commit e push manual pelo responsável humano do template documental revisado, em [repositório privado existente] / [branch autorizada].
Versão ou alteração autorizada: [arquivo documental aprovado e conteúdo/versão conferidos]; registrar identificador Git real somente quando existir.
Evidências e condições: conferir arquivo, diff, untracked, escopo e ausência de conteúdo sensível com inspeção segura; referenciar [revisão e resultados documentais reais]. Sem mudança de comportamento, não exigir suíte funcional ou rollback operacional artificial.
Autorização humana e alcance: [referência verificável à autorização anterior específica de commit/push pelo responsável]. Se confirmada e ainda válida, APPROVED sem novo pedido; caso contrário, PENDING. Não abrange outros arquivos, alteração material, deploy produtivo ou reescrita de histórico.
Resultado esperado e verificação posterior: arquivo aprovado registrado no destino autorizado; após execução manual, conferir commit/conteúdo, branch/referência remota e estado Git com evidência real. Working tree limpa sozinha não comprova push; sem execução, registrar pendente.
```

### Exemplo 2: deploy empresarial em produção

Proposta de release de API autenticada com dados empresariais. Versão/destino são campos a verificar; autorização e resultados não estão presumidos.

```markdown
Identificação da decisão: deploy da correção delimitada de autorização da API empresarial.
Gate A e baseline: [referência da tarefa aprovada, contratos e estado atual verificados].
Operação protegida proposta: publicar [versão/artefato verificado] no ambiente de produção [destino específico aprovado].
Repositório, branch ou artefato: [origem e identificador reais do artefato avaliado].
Escopo incluído: entrega dessa correção, verificação pós-entrega delimitada e recuperação expressamente autorizada.
Escopo excluído: migrations, destruição de dados, mudança global de permissões, custo novo e alterações alheias.
Responsáveis: execução por [operador autorizado]; aprovação por [responsável humano com autoridade].
Testes e QA reais: [referências aos testes executados, versão e ambiente]; incluir acesso legítimo, BOLA/IDOR, negativos horizontal/vertical e de tenant, integridade e regressão afetada. Evidência essencial ausente mantém execução BLOCKED.
Security Gate e achados: [parecer técnico real, controles confiáveis examinados, achados e limites]; falha crítica conhecida bloqueia release.
Dependências e pré-condições: [artefato, configuração e permissões conferidos sem valores de secrets; condições essenciais e compatibilidade verificadas].
Riscos e impacto: [acesso/dados/indisponibilidade pertinentes, riscos residuais e responsável].
Rollback ou recuperação: [gatilho, versão anterior compatível, responsável, procedimento autorizado e evidência pertinente]; reversão de código não comprova recuperação de dados.
Critérios de sucesso e pós-execução: confirmar versão/destino e fluxos críticos, negação de acesso não autorizado, integridade e sinais de saúde pertinentes; usar acesso produtivo autorizado, minimizar dados e registrar observado/pendências.
Limites da autorização: somente ação, artefato, destino, acesso de verificação e recuperação explicitamente concedidos; não ampliar privilégio, custo ou escopo.
Decisão humana e referência: PENDING até decisão específica do responsável sobre esta proposta e suas condições, por [conversa/registro verificável]. Registrar decisão real antes do deploy; não usar parecer técnico como autorização.
```

## K. Evolução

Avaliar o template na integração com Codex e no piloto real, com autorização própria. Simplificar campos quando evidências mostrarem burocracia, preservando governança e versionamento do Product System. Não criar Standard, checklist universal, sistema de aprovação, ferramenta ou log obrigatório. Candidate e aprovação documental não comprovam operação nem aprovam release real.

| Versão | Estado | Registro |
| --- | --- | --- |
| 1.0 | Candidate | Modos rápido/completo, estados da decisão, evidências, limites, execução/verificação e dois exemplos sintéticos; validação de uso permanece posterior. |
