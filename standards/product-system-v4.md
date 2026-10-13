# My Easy Development System Product System v4.1

## A. Identificação e governança

| Campo | Definição |
| --- | --- |
| Nome oficial | My Easy Development System Product System v4.1 |
| Versão | 4.1 |
| Estado canônico | Stable |
| Finalidade | Estabelecer o processo operacional para planejar, desenvolver, revisar, testar, entregar e manter software com Codex nativo. |
| Aplicabilidade | Qualquer linguagem, framework, sistema operacional ou ambiente de execução, respeitando a stack e a governança do projeto. |

Stable representa uma decisão canônica do projeto. Não comprova automaticamente validação operacional, execução de testes, aprovação humana ou prontidão de qualquer produto.

**Escopo:** websites institucionais, landing pages, sistemas web, aplicações empresariais, backends, APIs, integrações, sistemas locais e desktop, persistência de dados e soluções com IA quando aplicável. Abrange criação, manutenção, correção, refatoração e preparação de entrega.

**Exclusões:** este Standard não determina stack, arquitetura obrigatória, ferramenta de gestão, provedor, infraestrutura ou certificação. Não concede acesso a produção, credenciais, orçamento nem autorização de publicação. Procedimentos especializados pertencem às Skills e aos Standards existentes e pertinentes.

### Relação com as fontes canônicas

1. Ler `AGENTS.md` e as instruções aplicáveis ao escopo antes de agir. Preservar as decisões e os limites aprovados pelo responsável.
2. Usar este Product System como processo central, em coerência com `AGENTS.md`; ele não substitui nem amplia a autorização humana.
3. Consultar `standards/` e aplicar somente documentos existentes e pertinentes. Resolver conflitos materiais com o responsável antes da ação afetada.
4. Selecionar Skills em `.agents/skills/`, diretório runtime canônico. `skills/` é legado/documental e não deve ser usado como origem runtime.
5. Usar as Skills para execução especializada; não interpretar sua disponibilidade como obrigação de ativar todas.

Na inspeção de origem da versão 4.0, `standards/` continha somente `README.md`, sem controles especializados materializados. Referências a Standards futuros neste documento indicam pontos de evolução, não dependências já implementadas. Em cada tarefa, verificar o inventário atual.

### Responsabilidades

| Papel | Responsabilidade verificável |
| --- | --- |
| Responsável humano | Aprovar objetivo, escopo e limites no Gate A; resolver decisões materiais; avaliar o Gate B e autorizar ações protegidas. |
| Executor/autor | Obter contexto, selecionar capacidades, implementar, testar, corrigir, preservar o escopo e apresentar evidências e limitações reais. |
| Revisor | Examinar requisitos, alterações e evidências; registrar achados e parecer dentro da especialidade, sem substituir aprovação humana. |
| Responsável operacional | Quando designado e autorizado, executar entrega, verificar o ambiente de destino e conduzir recuperação e manutenção. |

Papéis podem ser acumulados conforme o contexto. Se o executor realizar a revisão, registrar **autorrevisão** e suas limitações. Não alegar independência por trocar de etapa, ferramenta ou Skill.

## B. Princípios de engenharia

| Princípio | Regra de execução |
| --- | --- |
| Correção funcional | Relacionar cada comportamento alterado a um requisito e verificar o resultado esperado, inclusive erros e limites pertinentes. |
| Simplicidade e manutenção | Escolher a menor solução sustentável, compreensível por quem dará manutenção; remover complexidade sem função demonstrada. |
| Clean Code | Usar nomes do domínio, responsabilidades claras, fluxo legível e tratamento explícito de erros; explicar regras não óbvias. |
| KISS e YAGNI | Resolver a necessidade atual; não implementar extensões hipotéticas, camadas ou serviços por antecipação. |
| DRY proporcional | Consolidar duplicação significativa quando a regra compartilhada estiver clara; evitar abstração prematura entre comportamentos distintos. |
| SOLID quando aplicável | Aplicar SRP, OCP, LSP, ISP e DIP quando orientação a objetos e complexidade justificarem; não exigir classes, interfaces ou injeção de dependência para funções simples. |
| Coesão e baixo acoplamento | Agrupar responsabilidades relacionadas, explicitar contratos e efeitos colaterais e reduzir dependências entre domínio e detalhes externos quando houver benefício real. |
| Segurança e privacidade por design | Identificar dados, permissões e limites de confiança antes de expor operações; coletar e compartilhar somente o necessário. |
| Testabilidade | Tornar comportamentos e contratos observáveis; permitir isolamento de dependências quando necessário, sem criar arquitetura apenas para testes. |
| Rastreabilidade e evidências | Vincular decisões, alterações e resultados aos critérios de aceitação; registrar o que foi efetivamente observado. |
| Documentação proporcional | Registrar o necessário para compreender, operar e retomar o trabalho; atualizar a fonte canônica em vez de duplicar narrativas. |
| Controle de dependências | Antes de adicionar pacote, verificar necessidade, origem, manutenção, licença, compatibilidade e impacto de instalação, segurança e operação. Preservar versões e arquivos de resolução existentes quando pertinentes. |
| Compatibilidade | Inspecionar a stack, convenções, versões suportadas e contratos atuais; justificar qualquer alteração e consultar o responsável se material. |

Design Patterns, microserviços, containers, Kubernetes e frameworks não são requisitos. Usá-los somente diante de necessidade demonstrada e dentro do escopo autorizado. Não fazer reescritas ou instalações por conveniência.

## C. Context as Code

Antes da implementação, recuperar contexto dos arquivos, código, testes e decisões existentes. Distinguir fatos verificados, decisões aprovadas e hipóteses. Conversas ajudam a interpretar a tarefa; decisões duráveis devem permanecer em uma fonte canônica autorizada.

Manter um registro conciso, no artefato de contexto já adotado pelo projeto, contendo:

| Informação | Conteúdo mínimo |
| --- | --- |
| Objetivo e requisitos | Problema, usuários ou consumidores, comportamento necessário e itens fora do escopo. |
| Critérios de aceitação | Condições observáveis de sucesso, falha e limites relevantes. |
| Arquitetura e restrições | Decisões aprovadas, contratos, stack, ambientes permitidos e limites de autonomia. |
| Dependências e riscos | Serviços, dados, acesso, versões relevantes, impactos e medidas de mitigação. |
| Estado atual e alterações | Situação verificada, arquivos afetados e comportamentos implementados. |
| Testes e evidências | Cenários, comandos, ambiente, resultados, revisões e limitações. |
| Pendências e próximos passos | Trabalho restante, blockers, decisões humanas e estado de aprovação. |

Atualizar esse registro quando uma decisão material mudar, após validação relevante e antes de transferir ou encerrar o trabalho. Ao retomar, conferir o estado real dos arquivos e do ambiente; não confiar apenas no relato anterior.

Não criar uma estrutura documental nova por padrão. Preferir referências a requisitos, testes e decisões existentes. Se a autorização limitar a escrita, preservar o contexto no arquivo permitido quando pertinente ou no relatório de entrega. Não copiar secrets, dados pessoais desnecessários ou saídas sensíveis para documentos. Remover informação superada ou marcar sua substituição de forma explícita.

## D. Ask-Before-Assume

Decidir autonomamente quando a escolha estiver dentro do Gate A, for reversível, tiver baixo impacto e respeitar contratos, stack e decisões existentes. Exemplos: nomes coerentes, organização local de código, uso de utilitário existente e correção de falha coberta pelo requisito.

Para ambiguidades não materiais, adotar a interpretação mais simples compatível com o contexto, registrar a hipótese se afetar a avaliação e prosseguir. Não usar ausência de resposta como aprovação de uma decisão material.

Consultar o responsável antes da ação dependente quando houver:

- Mudança relevante de escopo, critério de aceitação, comportamento contratado ou decisão arquitetural aprovada.
- Alteração relevante de segurança, permissões, exposição, retenção ou tratamento de dados.
- Novo custo, risco financeiro ou impacto operacional material, inclusive indisponibilidade não prevista.
- Operação destrutiva, migração irreversível, risco material de perda de dados ou outra ação irreversível.
- Necessidade de credencial ausente, uso de credenciais reais fora do escopo ou acesso a produção não autorizado.

Apresentar a decisão pendente, o motivo, os impactos e a menor alternativa viável. Continuar somente atividades independentes e seguras já autorizadas. Autorizações anteriores válidas não precisam ser solicitadas novamente; uma mudança material exige nova decisão.

## E. Capability Routing

Antes de carregar capacidades, classificar propósito, domínio, tipo de aplicação, superfície afetada, complexidade, risco e necessidade de especialização. Identificar dados, interface, integrações, exposição e ambientes envolvidos.

Selecionar o menor conjunto suficiente de Standards existentes e Skills. Ler as instruções selecionadas, registrar a justificativa de forma breve e reavaliar a seleção se a superfície mudar. Ler um catálogo para inspeção não significa ativar todas as capacidades em toda tarefa.

### Catálogo das 12 Skills canônicas

| Skill | Selecionar quando |
| --- | --- |
| `software-design-solid` | Implementar, revisar ou refatorar lógica, módulos, serviços e APIs. |
| `vera-architecture-security` | Arquitetura, APIs, autenticação, autorização, dados sensíveis, integrações ou limites de confiança exigirem análise especializada. |
| `quality-engineering-testing` | Planejar ou executar testes de comportamento, contratos, integrações, regressão e preparação de release. |
| `data-persistence-engineering` | Alterar modelo, schema, consultas, transações, concorrência, migrações ou recuperação de dados. |
| `release-deployment-reliability` | Preparar build, empacotamento, distribuição, configuração de ambientes, deploy, atualização ou recuperação. |
| `julian-premium-design` | Definir ou revisar direção de arte, UX, hierarquia, sistema visual ou experiência. |
| `kael-interface-engineering` | Implementar ou corrigir interfaces web ou locais, interação, estados e acessibilidade técnica. |
| `visual-interface-qa` | Revisar mudança visual relevante em interface realmente renderizada. |
| `clara-premium-copywriting` | Criar ou revisar conteúdo público, texto de marca e microcopy de produto. |
| `seo-technical` | Trabalhar em páginas públicas indexáveis, rotas, metadados, rastreamento e indexação. |
| `ai-search-visibility` | Melhorar identidade factual e compreensão de conteúdo público por sistemas de busca com IA. |
| `ai-engineering-production` | Integrar ou operar modelos, RAG, embeddings, agentes, ferramentas ou pipelines de IA. |

### Exemplos de seleção

- **Website institucional ou landing page:** Julian para direção visual, Kael para UI e Clara para texto quando essas superfícies forem alteradas; Quality para comportamento e Visual QA para mudança visual relevante. SEO para páginas indexáveis e AI Search Visibility para identidade factual pública. Vera se houver formulários, dados ou integrações com risco; Release quando houver preparação de publicação.
- **API:** Software Design, Quality e Vera; Data quando houver persistência e Release na preparação de entrega. Não selecionar capacidades visuais sem UI.
- **Sistema autenticado:** Software Design, Vera e Quality para regras, autorização e isolamento; adicionar Data, Kael e Visual QA conforme a superfície. Não tratar controles no frontend como autorização efetiva.
- **Aplicação local/desktop:** Software Design e Quality; Data se houver arquivos ou banco persistente, Kael para GUI e Julian/Visual QA conforme mudança de experiência. Vera conforme dados, permissões, integrações e exposição; Release para instalador, distribuição ou atualização. Não exigir infraestrutura web.
- **Sistema com IA:** AI Engineering, Software Design, Quality e Vera conforme integração, dados e ferramentas; Data para persistência/indexação e Release para operação. AI Search Visibility não substitui engenharia de IA interna e não se aplica automaticamente a RAG.

Para uma correção pequena, selecionar apenas as capacidades relacionadas à alteração. Um futuro Standard especializado poderá detalhar o roteamento; sua ausência não impede aplicar estas regras.

## F. Ciclo de desenvolvimento

Aplicar as etapas abaixo com profundidade proporcional. Em mudanças triviais, reunir etapas no mesmo registro e executar verificações diretas, preservando autorização, segurança e evidência.

| Etapa | Ação e condição de saída |
| --- | --- |
| 1. Compreensão da necessidade | Identificar problema, resultado desejado, usuários e limites; confirmar autorização suficiente no Gate A. |
| 2. Discovery proporcional | Inspecionar governança, stack, código, dados, contratos e estado atual; separar fatos e hipóteses. |
| 3. Requisitos e critérios de aceitação | Definir comportamentos e condições verificáveis; resolver ambiguidades materiais antes da implementação dependente. |
| 4. Avaliação de arquitetura e riscos | Mapear responsabilidades, limites de confiança, impactos e compatibilidade; selecionar controles e capacidades pertinentes. |
| 5. Planejamento incremental | Dividir o trabalho em incrementos verificáveis, indicar arquivos/superfícies e testes previstos, sem antecipar funcionalidades. |
| 6. Implementação | Alterar somente o escopo autorizado, preservar contratos e seguir convenções da stack. |
| 7. Testes e correções | Executar cenários pertinentes, diagnosticar falhas, corrigir e repetir verificações afetadas e regressão relacionada. |
| 8. Revisão técnica e de segurança | Revisar alteração final e evidências; realizar Security Review e Visual Review quando aplicáveis; tratar achados. |
| 9. Documentação e evidências | Atualizar contexto autorizado e instruções afetadas; registrar resultados, decisões, limitações e pendências. |
| 10. Preparação de entrega | Verificar escopo final, integridade, prontidão e recuperação aplicáveis; preparar artefato e procedimento quando autorizados. |
| 11. Aprovação humana | Apresentar Gate B com resultado e evidências; aguardar autorização para ações protegidas. |
| 12. Deploy/distribuição | Executar somente a ação e o destino autorizados, conforme procedimento preparado. |
| 13. Verificação pós-entrega e manutenção | Verificar versão e fluxos no destino permitido, observar falhas, registrar estado e encaminhar correções ou recuperação autorizadas. |

Se a tarefa terminar na preparação, marcar publicação e verificação pós-entrega como pendentes ou fora do escopo. Não executá-las para completar artificialmente o ciclo.

## G. Autonomous Development Mode

### Gate A humano

Obter autorização suficiente sobre objetivo, escopo, limites de autonomia, critérios de aceitação, restrições e riscos conhecidos. A instrução inicial pode constituir o Gate A quando clara. Registrar lacunas; solicitar decisão somente quando material para o trabalho.

Identificar ambientes e ações permitidos. Não deduzir autorização de produção, publicação, despesas ou credenciais a partir de uma autorização para desenvolver.

### Escopo de escrita no Gate A

Antes de criar, modificar ou gerar arquivos, identificar as raízes de escrita autorizadas pelo Gate A e a finalidade de cada uma. O limite vale para produto, testes, temporários, diagnósticos, hashes, manifestos, logs, backups, relatórios e evidências de autoria do agente. Autorização do workspace não implica autorização genérica para `/tmp`, `TMPDIR`, home ou outros diretórios.

Priorizar caminhos relativos; conferir `realpath`, symlinks, redirecionamentos e caminhos absolutos para impedir fuga da raiz. Distinguir escritas de autoria do agente de escritas internas inevitáveis do runtime; exceções operacionais de runtime exigem raiz, processo, finalidade e proveniência documentados e não ampliam o Gate A nem permitem acessar segredos.

Quando Gate A exigir confinamento técnico estrito, verificar, com o UID/namespace/perfil efetivos e mecanismos já existentes e permitidos, escrita positiva interna e tentativa negativa externa; registrar o alcance das sondas. As sondas externas também precisam de autorização específica para seus destinos e efeitos. Texto de prompt, `TMPDIR` ou `/tmp` privada gravável não demonstram por si só confinamento estrito.

Diante de bloqueio ambiental, não alterar sandbox nem pedir permissões; concluir as demais atividades permitidas e declarar `BLOCKED`. O Codex decide autonomamente todos os detalhes técnicos dentro do Gate A, sem microaprovações; publicação, operações destrutivas, custos, credenciais e Gate B permanecem sob autorização específica.

Usar comandos/processos novos dentro do sandbox autorizado; não enviar comandos a terminais preexistentes ou iniciados fora dele. Se o Gate A proibir novas decisões durante a execução, registrar decisões materiais pendentes sem perguntar e continuar somente as atividades independentes autorizadas.

### Execução autônoma

Dentro do Gate A, planejar, implementar, testar, diagnosticar, corrigir, reexecutar testes, revisar e documentar sem microaprovações. Utilizar QA e Security Gate quando aplicáveis. Parar a ação afetada se surgir um limite da seção H.

### Ciclo de revisão

| Estado | Critério | Próxima ação |
| --- | --- | --- |
| `APPROVED` | Critérios pertinentes atendidos, evidências suficientes e ausência de achado material impeditivo na revisão identificada. | Preparar Gate B; não interpretar o parecer como autorização de publicação. |
| `CHANGES_REQUIRED` | Há defeito, regressão, inconsistência ou evidência insuficiente corrigível dentro do escopo autorizado. | Corrigir, repetir testes e reinspecionar a alteração; retornar à revisão sem microaprovações. |
| `BLOCKED` | Uma decisão material, autorização, credencial, ambiente ou condição externa necessária impede avanço seguro. | Registrar causa, impacto e decisão necessária; não executar a ação bloqueada. |

Identificar o objeto, o autor do parecer e as limitações de cada revisão. Uma revisão parcial pode aprovar sua superfície sem aprovar a entrega inteira. Testes essenciais falhos ou não executados impedem alegação de aprovação geral.

### Gate B humano

Apresentar resultado, arquivos/superfícies afetados, evidências, testes e resultados, revisões, riscos residuais, pendências e ações protegidas propostas. Indicar o que está pronto para aprovação e o que ainda depende de validação.

Operações Git locais, como `git add` e `git commit`, são permitidas somente mediante autorização correspondente, inclusive quando previamente autorizadas no Gate A. Dentro desse alcance, não é necessário solicitar nova autorização para cada operação. Commit local não é operação de push.

Em projetos que reservam o Git manual ao responsável, o Codex não deve executar `git add` ou `git commit`, devendo entregar as alterações e evidências para que o responsável realize essas operações.

Push remoto exige autorização humana correspondente. Merge, push a branch protegida, release e deploy exigem autorização humana no Gate B; aplicar o Gate B às demais operações remotas quando a governança do projeto exigir. Proibições explícitas da tarefa prevalecem; não executar operações de versionamento só porque o trabalho passou na revisão.

Registrar a decisão humana e seu alcance. Autonomia de execução não equivale a autorização irrestrita, e `APPROVED` técnico não substitui Gate B.

## H. Limites e bloqueios

Interromper a ação afetada e registrar a decisão humana necessária antes dos casos abaixo. Solicitar essa decisão quando o Gate A permitir perguntas; se as proibir, registrar a pendência e continuar somente as atividades independentes autorizadas:

- Destruição ou operação com risco material de perda de dados.
- Migração irreversível ou alteração cuja recuperação não esteja adequadamente definida.
- Acesso a produção não autorizado, mesmo para investigação ou verificação.
- Criação de novos custos ou recursos pagos.
- Uso de credenciais reais fora do escopo, alteração de credenciais sem autorização ou necessidade de credencial ausente.
- Mudança material de requisitos, escopo ou critérios de aceitação.
- Mudança relevante de segurança ou constatação de falha crítica material de autenticação, autorização, secrets ou injeção.
- Qualquer ação irreversível não autorizada.
- Conflito material com decisão previamente aprovada.

Registrar o estado como `BLOCKED` para a ação impedida, a evidência disponível sem dados sensíveis, o impacto e as alternativas seguras. Falha crítica conhecida bloqueia release; não enfraquecer controles para liberar entrega. Conter ou corrigir somente dentro da autorização existente.

Continuar atividades independentes e seguras se ainda contribuírem para o objetivo aprovado. Não pedir microaprovação para uma correção ordinária coberta pelo Gate A. Não ocultar blocker nem tratar espera, ausência de resposta ou ferramenta disponível como autorização.

## I. Qualidade e testes

Relacionar critérios de aceitação a cenários e selecionar o menor conjunto suficiente por probabilidade, impacto e superfície afetada. Usar ferramentas nativas e do ecossistema já disponíveis; não instalar dependências sem necessidade e autorização compatíveis.

| Camada ou tipo | Aplicação proporcional |
| --- | --- |
| Unitários | Regras de domínio, cálculos, transformações e limites isoláveis. |
| Integração | Comunicação entre módulos, persistência, serviços e falhas parciais. |
| Contratos | Compatibilidade de APIs, schemas, eventos e consumidores afetados. |
| End-to-end e smoke | Jornadas críticas e funcionamento do conjunto no ambiente pertinente. |
| Regressão | Comportamentos adjacentes e reprodução do defeito corrigido. |
| Cenários negativos | Entradas inválidas, limites, indisponibilidade, timeout, erro externo e recuperação. |
| Abuso e segurança | Acesso horizontal/vertical, isolamento entre usuários/tenants, injeções, consumo indevido e outros riscos identificados. |
| Acessibilidade e QA visual | Teclado, foco, nomes acessíveis, estados, legibilidade, contraste e renderização em dimensões relevantes de UI web ou local. |
| Avaliações de IA | Casos representativos e adversariais, regressão, falha externa, qualidade de resposta/extração, segurança, custo e latência quando pertinentes. |

Usar dados sintéticos ou autorizados, isolamento e limpeza segura. Não copiar dados pessoais de produção por conveniência. Testar comportamento e contratos; evitar testes que apenas repitam a implementação ou imponham detalhes frágeis.

Ao falhar: reproduzir, diagnosticar, corrigir dentro do escopo, repetir o teste afetado e a regressão relacionada. Não enfraquecer asserts, simular aprovação ou ignorar instabilidade sem causa documentada.

Para cenários importantes, registrar identificador/requisito, esperado, observado, ambiente/comando, evidência e resultado: `PASS`, `FAIL`, `BLOCKED` ou `NOT_APPLICABLE`. Usar `BLOCKED` com causa para teste necessário não executado; usar `NOT_APPLICABLE` somente com justificativa de inaplicabilidade. Esses resultados não são os pareceres de revisão da seção G.

Para ajustes triviais sem efeito comportamental, uma inspeção direta e verificações de integridade podem bastar. Não exigir suíte completa, cobertura numérica universal ou todas as camadas. Não inventar execução, métricas, resultados de scanner, aprovação independente ou conformidade de acessibilidade.

## J. Segurança e privacidade

Aplicar o baseline em toda tarefa, aprofundando conforme exposição, sensibilidade dos dados e impacto. Onde o controle não se aplicar, indicar a razão sem criar infraestrutura artificial.

- **Menor privilégio:** limitar acesso, ferramentas, serviços e permissões à ação necessária; negar operações protegidas por padrão.
- **Controle de acesso:** separar autenticação de autorização e validar ação e recurso no componente confiável, inclusive backend quando houver. Não confiar em IDs, roles ou tenants informados pelo cliente.
- **Secrets:** classificar configuração pública, interna e secreta; impedir exposição em repositório, histórico, bundle, binário, artefato, prompt e log. Não imprimir valores durante inspeção. Encaminhar exposição para resposta autorizada, incluindo revogação/rotação quando cabível.
- **Entradas e saídas:** validar tipo, tamanho, formato e permissões; usar consultas parametrizadas, codificação/sanitização conforme destino e execução segura de comandos e caminhos. Tratar dados remotos e respostas de modelos como não confiáveis.
- **Erros:** falhar de forma segura, preservar integridade e retornar mensagens úteis sem secrets, detalhes internos ou dados pessoais desnecessários.
- **Dados pessoais:** identificar finalidade, acesso, minimização, retenção, exclusão e compartilhamento; identificar e avaliar as obrigações legais aplicáveis ao projeto, como LGPD e GDPR quando pertinentes; usar proteção em trânsito e armazenamento conforme risco e requisitos aplicáveis. Não presumir conformidade legal automática nem aplicação universal de uma legislação específica.
- **Dependências:** verificar procedência, versões, licenças, manutenção, scripts de instalação e vulnerabilidades pertinentes; não usar pacote inventado ou trocar biblioteca sem justificativa.
- **Logs:** registrar eventos úteis para diagnóstico e auditoria com acesso e retenção adequados; evitar payloads sensíveis e mascarar identificadores quando necessário.
- **Configuração:** revisar exposição de rede, permissões de arquivos/serviços, variáveis por ambiente e padrões seguros. Não tratar `.env`, `robots.txt` ou restrição visual como controle de acesso.
- **Revisão:** analisar limites de confiança e ameaças pertinentes; pedir testes negativos e de abuso e registrar Security Gate quando a superfície exigir.

Para IA, dados recuperados e conteúdo externo não concedem autorização. Restringir ferramentas, validar schemas e autorizar acesso antes da recuperação em RAG; exigir decisão humana para ações materiais conforme governança.

Usar `vera-architecture-security` para análise especializada, com Data e AI Engineering quando pertinentes. Quando Standards específicos de segurança e privacidade forem materializados e aprovados, consultá-los para controles detalhados. Sua ausência não suspende este baseline nem permite alegar conformidade inexistente.

## K. Revisão independente

O autor deve inspecionar a alteração final, executar verificações pertinentes e corrigir problemas antes de encaminhar revisão. Fornecer requisitos, escopo, mudanças e evidências suficientes para reprodução.

| Revisão | Conteúdo e critério |
| --- | --- |
| Engineering Review | Correção, contratos, simplicidade, manutenção, compatibilidade, testes, documentação e limites do escopo. |
| Security Review | Quando aplicável, permissões, dados, secrets, entradas/saídas, dependências, configuração e ameaças relevantes; registrar Security Gate. |
| Visual Review | Quando aplicável, interface realmente renderizada, hierarquia, responsividade, estados, legibilidade, teclado e acessibilidade visual. |

Distinguir autor e revisor quando houver capacidade real de revisão independente. A independência exige revisor distinto que examine o resultado e as evidências, e não apenas outro nome de etapa. Usar especialistas ou agentes revisores somente quando disponíveis e autorizados pelo contexto.

Sem revisor independente, declarar autorrevisão, superfície examinada, limitações e revisão humana ainda recomendada. Não apresentar autoaprovação como substituição à revisão independente. Se ela for critério obrigatório do projeto, sua ausência impede marcar a tarefa como pronta.

Solicitar retrabalho por requisito não atendido, regressão, complexidade injustificada, controle ausente, evidência insuficiente ou falha visual relevante. Registrar achado reproduzível, severidade, impacto e critério de correção. Reinspecionar a versão corrigida e repetir verificações afetadas. Falhas críticas de segurança bloqueiam release.

## L. Release, deploy e operação

A implementação detalhada deve ser conduzida por `release-deployment-reliability`, selecionada quando houver preparação de entrega, distribuição ou risco operacional. Preparação não autoriza publicação.

Antes de propor release, verificar os itens pertinentes:

| Item | Evidência ou decisão necessária |
| --- | --- |
| Build e artefato | Procedimento reproduzível, dependências resolvidas, artefato versionado e integridade identificável; não alegar build se não executado. |
| Configuração por ambiente | Destino, variáveis, secrets, permissões, rede e integrações conferidos sem expor valores sensíveis. |
| Testes de release | Testes necessários aprovados, smoke do artefato e verificações de segurança proporcionais; limitações explícitas. |
| Versionamento | Versão e referência de origem disponíveis, alterações e compatibilidade documentadas; nenhum commit ou push automático. |
| Migrações | Pré-condições, ordem, compatibilidade, impacto em locks/indisponibilidade e estratégia de recuperação; testar com dados sintéticos representativos. |
| Backup e recuperação | Responsável, procedimento, acesso e retenção definidos; ensaiar restauração em ambiente não produtivo quando o risco exigir. |
| Rollback | Definir gatilhos, responsável e passos de reversão; distinguir rollback de código de recuperação efetiva dos dados. |
| Monitoramento e logs | Sinais de saúde, erros, disponibilidade e desempenho pertinentes, com alertas e acesso proporcionais. |
| Documentação operacional | Instruções de entrega, verificação, diagnóstico e recuperação suficientes para o operador. |
| Distribuição local | Sistemas suportados, permissões, instalação, atualização, desinstalação e preservação de dados; assinatura e proteção da atualização quando exigidas pelo contexto. |

Não exigir containers, nuvem, CI/CD ou monitoramento complexo em produtos que não necessitem deles. Não embutir secrets em artefatos distribuídos. Não afirmar backup válido ou rollback testado sem evidência.

No Gate B, identificar versão/artefato, ambiente, procedimento, riscos, recuperação e ação solicitada. Executar apenas após autorização correspondente. Se mudança ou falha material alterar o plano aprovado, interromper a ação afetada e obter nova decisão.

Após entrega autorizada, verificar a versão no destino, configuração e fluxos críticos, observar sinais pertinentes e registrar resultado real. Acesso a produção para essa verificação também precisa estar autorizado. Em falha, aplicar recuperação previamente autorizada ou solicitar decisão. Manutenção deve tratar incidentes, dependências e regressões pelo mesmo ciclo proporcional.

## M. Definition of Ready e Definition of Done

### Definition of Ready

Iniciar a implementação quando:

- Objetivo, escopo e limites do Gate A estiverem suficientemente claros.
- Critérios de aceitação forem verificáveis e ambiguidades materiais estiverem resolvidas.
- Contexto, stack, contratos e superfícies relevantes tiverem sido inspecionados.
- Riscos e restrições conhecidos estiverem identificados, com capacidades pertinentes selecionadas.
- Dependências e ambiente necessários à próxima etapa estiverem disponíveis ou sua limitação estiver explícita.
- Plano de implementação e validação for proporcional ao trabalho.

Não exigir discovery extenso para iniciar uma correção simples. Um blocker de etapa posterior não impede trabalho independente autorizado, mas deve ser registrado.

### Definition of Done e estados de entrega

| Estado | Condição verificável |
| --- | --- |
| Implementado | Alterações previstas realizadas e inspecionadas; não implica testes, revisão ou publicação. |
| Testado | Verificações necessárias executadas com resultados registrados e aceitos; verificações parciais devem ser identificadas como parciais. |
| Revisado | Revisões pertinentes realizadas sobre a alteração final, achados tratados e limitações/independência registradas. |
| Pronto para aprovação | Critérios atendidos, validações essenciais satisfatórias, revisões exigidas concluídas, contexto atualizado e pacote de Gate B disponível, com riscos residuais e pendências explícitos. |
| Aprovado pelo responsável | Decisão humana registrada com alcance, condições e ações autorizadas; não implica execução da entrega. |
| Publicado/distribuído | Entrega autorizada executada e versão/destino registrados; não implica validação operacional automática. |
| Verificado pós-entrega | Verificações autorizadas no destino concluídas e resultados, limitações e eventuais incidentes registrados. |

Declarar conclusão em relação ao escopo aprovado. Uma tarefa de desenvolvimento pode terminar pronta para aprovação, mantendo publicação pendente. Se o objetivo incluir entrega e verificação autorizadas, essas atividades integram sua Definition of Done.

Não considerar implementação concluída equivalente a produção validada. Não marcar entrega pronta com falha essencial, revisão obrigatória ausente ou blocker material. Um parecer técnico `APPROVED` pode recomendar Gate B sem antecipar a decisão humana.

## N. Evidências e rastreabilidade

Entregar um registro proporcional com:

- Objetivo, alcance aprovado e critérios atendidos ou pendentes.
- Arquivos/superfícies alterados e comportamento resultante; verificar ausência de alterações fora do escopo, inclusive arquivos novos.
- Decisões relevantes, justificativas, hipóteses remanescentes e referências canônicas.
- Testes/verificações executados, ambiente, comandos ou procedimento manual, esperado, observado e resultado real.
- Evidências pertinentes, como saída resumida, relatório, screenshot de UI, identificação/integridade de artefato ou referência de versão disponível.
- Limitações de execução e cobertura, falhas e riscos residuais com impacto.
- Revisões, responsável pelo parecer, independência ou autorrevisão, achados e estado final.
- Estado do Gate B, ações autorizadas, ações pendentes e próximos passos.

Usar arquivos e mecanismos existentes e autorizados. Não criar logs extensos ou duplicar documentação para preencher checklist. Preservar evidências sensíveis em local permitido e restrito; resumir sem expor secrets.

Conferir integridade diretamente quando o arquivo for novo e não rastreado. Em repositório Git, `git status` e `git diff --check` ajudam a inspecionar o estado, mas `git diff --check` sozinho não valida arquivos untracked. Não executar operações de versionamento fora da autorização.

Separar resultado observado, inferência e recomendação. Nunca inventar execução, métricas, aprovações, acesso a ambiente ou estado operacional.

## O. Exceções e proporcionalidade

Para mudanças pequenas e reversíveis, combinar etapas, usar registro curto e verificações diretas. Selecionar somente testes e revisões que respondam ao risco real. Simplificação rotineira justificada não exige microaprovação se permanecer no Gate A.

Manter sempre os controles essenciais: escopo autorizado, preservação de dados, proteção de secrets, controle de acesso aplicável, verificação da alteração e relato honesto. Pequeno volume de código não significa baixo risco em autenticação, dados ou operação.

Registrar exceção relevante com regra afetada, motivo, alcance, risco, controle compensatório, responsável e condição de reavaliação. Se a exceção modificar governança, segurança material ou decisão aprovada, obter decisão humana antes da ação. Uma exceção local não altera silenciosamente este Standard nem autoriza ações protegidas.

Quando ferramenta, ambiente ou revisor estiver indisponível, declarar a limitação e usar alternativa suficiente somente se compatível com os critérios e o risco. Não substituir validação essencial por suposição ou reclassificar falta de execução como inaplicabilidade.

## P. Evolução do Standard

Revisar o Product System quando houver problema operacional recorrente, conflito canônico, nova superfície relevante ou necessidade comprovada de ajustar o processo.

1. Identificar problema, regra afetada e evidência que justifica a proposta.
2. Inspecionar `AGENTS.md`, Standards e Skills existentes; avaliar duplicações, compatibilidade e impacto nos projetos em andamento.
3. Definir escopo da revisão e obter autorização para alterar os arquivos pertinentes. A revisão deste Standard não autoriza alterar outros documentos.
4. Propor alteração explícita, verificar consistência e testar procedimentos quando aplicável; declarar limites de validação operacional.
5. Registrar versão, mudanças de regras, justificativa, impacto e decisão humana no mecanismo autorizado do projeto. Mudanças de governança exigem aprovação explícita antes de sua adoção.
6. Atualizar referências somente no escopo autorizado e comunicar transição, preservando decisões anteriores até substituição aprovada.

Usar incremento maior para mudança incompatível de governança, incremento menor para regra operacional compatível e revisão corretiva para esclarecimento sem mudança de obrigação. Não modificar regras silenciosamente mantendo a mesma identificação de versão.

Standards especializados futuros devem detalhar roteamento, controles de domínio, qualidade, segurança ou operação sem duplicar o processo central nem enfraquecer os Gates. Sua criação e adoção exigem escopo e revisão próprios. O estado Stable permanece uma classificação canônica e deve ser distinguido das evidências operacionais disponíveis.

### Registro da revisão operacional

| Versão | Mudança e autorização | Limite de evidência |
| --- | --- | --- |
| 4.0 | Edição anterior conservada no histórico Git do framework. | Estado canônico documental não comprova operação. |
| 4.1 | Regra operacional compatível de raízes de escrita, autoria agente/runtime, confinamento condicional, bloqueios e processos novos. Autorizada expressamente no Gate A FINAL; arquivo `product-system-v4.md` e arquitetura preservados. | Incorporação e verificações locais concluídas na consolidação Gate A FINAL; os artefatos de auditoria foram removidos da árvore operacional por decisão do responsável. Não concede Gate B nem valida isolamento universal. Referências anteriores a v4.0 continuam identificando a edição histórica. |
