# My Easy Development System Capability Routing Standard v1.2.1

## A. Identificação e governança

| Campo | Definição |
| --- | --- |
| Nome oficial | My Easy Development System Capability Routing Standard v1.2.1 |
| Identificador | Standard 03 |
| Versão | 1.2.1 |
| Estado canônico | Stable |
| Finalidade | Definir como identificar, selecionar, consultar e reavaliar capacidades para executar tarefas com qualidade, segurança e contexto proporcional. |
| Aplicabilidade | Criação, análise, manutenção, correção, refatoração, revisão e preparação de entrega de software e experiências digitais. |
| Independência técnica | Aplicável a qualquer linguagem, framework, plataforma e ambiente, preservando a stack e a arquitetura existentes. |

Stable é uma classificação canônica. Não comprova aprovação humana da entrega, integração automática com o Codex ou validação operacional do roteamento.

**Escopo:** política de seleção de Standards existentes, Skills canônicas e verificações pertinentes ao objetivo, à superfície, à fase e ao risco da tarefa. Complementa o [Product System](product-system-v4.md) e o [Web Experience & Business Systems](web-experience-business-systems-v1.md).

**Exclusões:** não cria um sistema independente de agentes, pipeline obrigatório, automação de seleção, memória persistente, ai-memory, MCP, cache externo, indexador, servidor, hooks ou dependências. Não define stack, concede acesso, autoriza custos ou altera a arquitetura. Não exige orquestração nem participação de múltiplos agentes.

### Autoridade e fontes

Ler [AGENTS.md](../AGENTS.md) e as instruções aplicáveis ao escopo antes da ação. O Product System permanece a política central de processo, autorização, segurança, testes, revisão e entrega. O Web Experience acrescenta critérios para interfaces e experiências web ou locais. Este Standard detalha a seleção; as Skills fornecem os procedimentos especializados.

O diretório runtime canônico é `.agents/skills/`. `skills/` é legado/documental. Disponibilidade não significa pertinência, execução ou autorização. Instruções e proibições explícitas da tarefa delimitam o Gate A. O roteamento não pode ampliar esse alcance nem enfraquecer os controles centrais.

Resolver conflitos materiais conforme o Product System antes da ação afetada. Selecionar uma capacidade de release, por exemplo, não autoriza publicação. Merge, push a branch protegida, release e deploy permanecem sujeitos ao Gate B; operações Git exigem a autorização correspondente e respeitam proibições da tarefa.

Neste documento, **deve** estabelece obrigação na superfície aplicável, **quando** exige avaliar a condição e **recomenda-se** permite alternativa justificada. As indicações de seleção dependem da atividade real, não apenas do nome do produto.

## B. Princípio de roteamento proporcional

**Selecionar o menor conjunto suficiente de capacidades para cumprir os requisitos e controlar os riscos reais da tarefa.**

O menor conjunto pode envolver várias Skills. Segurança, integridade dos dados, qualidade e critérios de aceitação prevalecem sobre economia artificial de contexto. Não exigir todas as Skills por padrão nem eliminar uma capacidade crítica porque seu documento aumenta a leitura.

Para decidir, relacionar cada capacidade à superfície, ao risco ou à verificação que ela atende. Usar orientação especializada onde houver necessidade demonstrada. A ausência de uma Skill selecionada não dispensa o baseline do Product System nem a verificação da alteração.

Operar de forma simples: classificar, avaliar riscos, consultar fontes pertinentes, aplicar instruções selecionadas e reavaliar diante de descobertas. Em ajuste trivial, essas decisões podem caber em uma frase e uma verificação direta.

## C. Classificação da tarefa

Para interface nova ou redesign, rotear a exploração criativa para Julian conforme seção C do Web Experience; traduzir a direção em implementação por Kael e texto por Clara, com Quality para comportamentos e Visual QA para crítica renderizada. Capacidade selecionada, fonte lida, decisão aplicada e evidência examinada são estados distintos: vincular no registro existente as decisões relevantes às telas e verificações. Não basta listar Skills ou dizer que o resultado é premium. Usar a política de linguagem do AGENTS. Isso não ativa todas as 12 Skills, nem cria aprovação intermediária obrigatória.

Classificar a próxima atividade com informação suficiente para decidir. Usar o contexto existente; não criar formulário obrigatório ou discovery extenso para correções simples.

| Dimensão | Informação necessária |
| --- | --- |
| Objetivo | Problema, público ou consumidor e resultado esperado. |
| Tipo de produto | Website, aplicação, API, sistema empresarial, produto local ou combinação pertinente. |
| Superfície afetada | Conteúdo, UI, lógica, contratos, dados, integrações, permissões, configuração ou entrega. |
| Natureza da alteração | Criação, correção, refatoração, investigação, revisão, migração ou preparação operacional. |
| Dados envolvidos | Dados públicos, pessoais, confidenciais, secrets, origem, armazenamento e acesso pertinentes. |
| Exposição externa | Acesso público ou restrito, rede, clientes, serviços externos e limites de confiança. |
| Risco e impacto | Consequência de falha, reversibilidade, usuários e componentes atingidos. |
| Fase | Discovery, planejamento, arquitetura, implementação, testes, revisão, release ou pós-entrega. |
| Critérios de aceitação | Comportamentos e condições observáveis, inclusive falhas e limites relevantes. |

### Pedido curto e brief proporcional

Primeiro distinguir manutenção do MEDS de desenvolvimento de projeto conforme AGENTS. No MEDS, pedidos de produto têm destino padrão `workspaces/<slug>/`; em um projeto externo preparado, a raiz autorizada é a do próprio projeto. Não copiar instruções compartilhadas nem editar o framework ao desenvolver um projeto interno.

Converter a descrição em brief suficiente: objetivo, público, tipo de aplicação, funcionalidades, requisitos não funcionais pertinentes, arquitetura e tecnologias proporcionais, identidade visual/recursos quando necessários, critérios de aceite, testes e entrega local. Não exigir formulário ou prompt técnico. Escolhas reversíveis e lacunas não essenciais podem usar premissas explícitas; não inventar dados comerciais reais, pessoais, endereços, preços, registros ou credenciais. Lacuna crítica bloqueia só a operação protegida dependente, preservando Gates e trabalho independente.

Exemplo: “Crie um site premium para um condomínio de luxo em Osasco, com imagens originais e formulário de contato.” Selecionar experiência web, design, copy, UI e qualidade conforme as atividades; SEO apenas para páginas indexáveis. Verificar ferramenta autorizada de imagens, integrar assets locais e validar o formulário. Sem destino real de envio, documentar a pendência e não apresentar simulação como mensagem enviada. Não presumir endereço, preço, banco, login, IA no produto ou deploy.

Escolher QA pela superfície: site (responsividade, acessibilidade, interações, links, assets, contraste e navegador real quando disponível); API (endpoints, validações, contratos, erros, testes automatizados e segurança proporcional); autenticação (acesso, sessão, autorização por recurso, credenciais e negativos). DOM simulado, inspeção estática e imagem isolada não substituem QA no navegador. Registrar testes como PASS/FAIL/BLOCKED/NOT RUN segundo o Product System e repetir os afetados após correções.

### Categorias operacionais

| Categoria | Distinção relevante para a seleção |
| --- | --- |
| Website e conteúdo público | Informação editorial/comercial; SEO depende de indexabilidade e GEO do objetivo de compreensão pública. |
| Aplicação web | Interações e regras de negócio; avaliar contratos, estados, acessibilidade e recuperação. |
| API/backend | Operações e consumidores; avaliar autorização, entradas/saídas, compatibilidade e falhas sem pressupor UI. |
| Sistema autenticado | Sessão, perfis e recursos protegidos; autenticação não garante autorização. |
| Sistema empresarial | Cadastros, consultas, indicadores e fluxos operacionais; integridade e isolamento dependem do domínio. |
| Aplicação local/desktop | GUI ou execução local, arquivos e permissões da plataforma; não pressupõe servidor ou infraestrutura web. |
| Persistência de dados | Modelo, arquivos persistentes, schema, consultas, transações, concorrência e recuperação efetivamente afetados. |
| Integrações | Serviços, webhooks, importações ou sincronizações; avaliar contratos, confiança e falhas parciais. |
| Sistema com IA | Uso efetivo de modelos, RAG, embeddings, agentes, ferramentas ou pipelines; exige avaliação pertinente ao componente. |
| Preparação de release | Build, artefato, distribuição, configuração, atualização, publicação ou recuperação no escopo aprovado. |

Uma tarefa pode pertencer a mais de uma categoria. Um cadastro empresarial pode combinar UI web, autenticação, API e persistência. Classificar a superfície alterada dentro do produto: corrigir um rótulo nesse sistema não equivale a redesenhar sua autorização.

## D. Avaliação de risco

Avaliar consequência de falha, exposição, probabilidade pertinente, reversibilidade e meios de verificação. Não usar pontuação numérica complexa nem quantidade de linhas como medida de criticidade.

| Dimensão de risco | Pergunta que orienta o roteamento |
| --- | --- |
| Segurança e autorização | A alteração afeta identidade, sessão, acesso por ação/recurso, perfis ou isolamento? |
| Dados pessoais e confidenciais | Pode ampliar coleta, exposição, compartilhamento, retenção ou acesso indevido? |
| Persistência e integridade | Pode perder, duplicar, corromper ou sobrescrever registros ou arquivos relevantes? |
| Contratos e compatibilidade | Pode quebrar consumidores, formatos, versões suportadas ou comportamento contratado? |
| Disponibilidade | Pode interromper jornada, gerar consumo excessivo, locks ou falha de recuperação? |
| Dependências | Envolve pacote, provedor, instalação, versão, script ou cadeia de suprimentos? |
| Visual e experiência | Pode prejudicar legibilidade, acessibilidade, fluxo, responsividade ou design aprovado? |
| Infraestrutura e publicação | Muda exposição de rede, configuração, ambiente, artefato ou procedimento de entrega? |
| IA e ferramentas externas | Envolve saída não confiável, recuperação de dados, comandos, exfiltração, custo ou ação material? |

**Trabalho simples e reversível:** superfície delimitada, sem impacto relevante em acesso, dados, contratos ou operação; usar leitura e validação diretas. **Trabalho com risco relevante:** aprofundar as dimensões afetadas e selecionar especialistas e testes suficientes. **Trabalho crítico:** tratar risco material de segurança, perda de dados, indisponibilidade ou ação irreversível com controles e decisões humanas previstos no Product System.

Uma alteração pequena em autenticação ou autorização pode exigir controles mais fortes que uma alteração extensa de conteúdo estático. Se faltar informação para excluir um risco relevante, consultar código, contrato ou instrução pertinente antes de reduzir a seleção. Dúvida material não pode ser convertida em baixo risco por conveniência.

## E. Inventário de capacidades

O inventário abaixo corresponde às 12 Skills existentes em `.agents/skills/`, cujos arquivos `SKILL.md` são as fontes dos procedimentos. Os rótulos curtos servem apenas para tornar a matriz legível; não representam novas Skills, agentes ou papéis obrigatórios.

| Nome exato e fonte | Rótulo | Finalidade e gatilhos de seleção | Exemplos de não aplicação | Relações pertinentes |
| --- | --- | --- | --- | --- |
| [software-design-solid](../.agents/skills/software-design-solid/SKILL.md) | Software Design | Código correto e sustentável; lógica de negócio, módulos, serviços, APIs, refatoração, acoplamento e revisão técnica com Clean Code e SOLID proporcionais. | Conteúdo ou mudança puramente visual sem alteração de lógica. Não impor classes, padrões ou camadas. | Quality para comportamento; Vera para confiança; Data para persistência. |
| [vera-architecture-security](../.agents/skills/vera-architecture-security/SKILL.md) | Vera | Arquitetura e segurança; APIs, login/sessão, autorização, dados sensíveis, secrets, integrações, infraestrutura exposta, vulnerabilidades e IA com acesso a dados/ferramentas. Threat modeling proporcional e Security Gate. | Não impor revisão profunda sem impacto de segurança; o baseline continua aplicável. | Quality para negativos/abuso; Data para acesso e integridade; AI Engineering para IA. |
| [quality-engineering-testing](../.agents/skills/quality-engineering-testing/SKILL.md) | Quality | Estratégia e evidência por risco; mudanças funcionais, bugs, APIs, integrações, autenticação, migrations, IA, responsividade com comportamento, release e investigação de falhas. | Ajuste trivial sem efeito comportamental pode usar verificação direta; não exigir suíte completa. | Especialista da superfície; Visual QA para UI; AI Engineering para evals. |
| [data-persistence-engineering](../.agents/skills/data-persistence-engineering/SKILL.md) | Data | Dados íntegros e recuperáveis; modelos, schemas, consultas, índices, migrations, importações, sincronizações, transações, concorrência, retenção, exclusão e backup/restore. | Alteração estática sem impacto em armazenamento. Integração sem persistência não basta. | Vera para acesso; Quality para integridade; Release para operação/migração. |
| [release-deployment-reliability](../.agents/skills/release-deployment-reliability/SKILL.md) | Release | Entrega operável e recuperável; build, empacotamento, distribuição, CI/CD, configuração, deploy, atualização, readiness, incidentes, rollback e pós-entrega. | Análise documental ou ajuste limitado a código sem intenção de distribuição. Não ativar deploy completo por rotina. | Quality para smoke/regressão; Vera para configuração/secrets; Data para recuperação. |
| [ai-engineering-production](../.agents/skills/ai-engineering-production/SKILL.md) | AI Engineering | IA confiável e mensurável; API de modelos/ML, inferência, RAG, embeddings, indexação, agentes, ferramentas, evals, segurança, observabilidade, custo e latência. | Texto comercial que menciona IA; problema determinístico sem componente de IA. Não impor arquitetura ou fornecedor de IA. | Vera para confiança e ferramentas; Quality para evals; Data para base/índice persistente; Release para operação. |
| [clara-premium-copywriting](../.agents/skills/clara-premium-copywriting/SKILL.md) | Clara | Conteúdo e UX writing ancorados em fatos; marca, páginas públicas, ofertas, headlines, CTAs, formulários, erros, estados vazios, onboarding e tom de voz. | Backend ou refatoração sem texto visível. Não inventar provas, métricas ou funcionalidades. | Julian para hierarquia; Kael para implementação; SEO/GEO para conteúdo público; Visual QA para leitura. |
| [julian-premium-design](../.agents/skills/julian-premium-design/SKILL.md) | Julian | Direção de arte e UX; nova interface, redesign, sistema visual, arquitetura da informação, responsividade e problemas de hierarquia, composição ou identidade. | Backend puro; correção pontual que preserva design aprovado não exige direção de arte completa. | Clara para narrativa; Kael para UI; Visual QA para revisão renderizada. |
| [kael-interface-engineering](../.agents/skills/kael-interface-engineering/SKILL.md) | Kael | Implementação de UI web/local; componentes, layouts, navegação, formulários, interação, estados, responsividade, acessibilidade técnica e motion proporcional. | Backend, dados ou infraestrutura sem interface. | Julian e Clara quando design/copy exigirem definição; Quality para fluxos; Visual QA para mudança visual relevante; Vera para segurança. |
| [seo-technical](../.agents/skills/seo-technical/SKILL.md) | SEO | Descoberta técnica de páginas públicas indexáveis; criação/reformulação/migração, URLs, redirects, canonicals, metadados, semântica, sitemap, robots, dados estruturados e rastreamento. | Dashboard privado, API interna ou aplicação local sem páginas públicas. | Clara, Julian/Kael e GEO conforme conteúdo e estrutura; Release quando houver publicação. |
| [ai-search-visibility](../.agents/skills/ai-search-visibility/SKILL.md) | GEO | Identidade factual e compreensão pública por busca com IA; entidade, serviços, contatos publicados, páginas estratégicas, fatos verificáveis e consistência entre páginas. | Backend, sistema privado, inferência ou RAG interno. Não prometer citação, ranking ou recomendação. | Clara para clareza; SEO para acesso técnico; não substitui AI Engineering. |
| [visual-interface-qa](../.agents/skills/visual-interface-qa/SKILL.md) | Visual QA | Examinar interface realmente renderizada; mudança visual relevante, responsividade, estados, fluxos, hierarquia, legibilidade, acessibilidade visual e consistência. Preferir revisor distinto. | API sem UI ou alteração técnica sem efeito visual. Código e mockup não comprovam inspeção renderizada. | Kael para correções; Julian/Clara para design/texto; Quality para comportamento. |

Relação entre Skills indica colaboração possível, não ativação automática de toda a cadeia. Consultar instruções de uma capacidade relacionada quando sua condição ocorrer. Não transformar a ausência de revisor independente em alegação de independência pela troca de Skill.

## F. Roteamento de Standards

| Fonte existente | Quando e como consultar |
| --- | --- |
| [Product System](product-system-v4.md) | Política central em toda tarefa do sistema. Recuperar regras aplicáveis de contexto, autonomia, limites, segurança, qualidade e evidências; aprofundar ciclo, revisão e entrega conforme a atividade. |
| [Web Experience & Business Systems](web-experience-business-systems-v1.md) | Quando interface ou experiência estiver no escopo, inclusive GUI local. Consultar critérios das superfícies afetadas, como conteúdo, estados, acessibilidade, regras de negócio e QA. Não exigir leitura de SEO para UI privada sem descoberta pública. |
| [Capability Routing Standard](capability-routing-v1.md) | Quando for necessário determinar ou reavaliar a seleção. Usar inventário, matriz, exclusões e gatilhos pertinentes, sem releitura integral automática. |
| [Authentication & Security](authentication-security-v1.md), Standard 04, Stable | Quando identidade, AuthN, AuthZ, permissões por ação/recurso, sessões, controle de acesso, isolamento entre usuários/tenants ou segurança de dados estiverem envolvidos. Preservar a distinção entre autenticação e autorização e a validação no componente confiável; consultar somente as orientações pertinentes à superfície. |
| [Environment Variables & Secrets](environment-variables-secrets-v1.md), Standard 05, Stable | Quando configuração, variáveis de ambiente, chaves, credenciais, exposição de secrets, separação de ambientes ou seus fluxos de consumo forem pertinentes. Consultar classificação e proteção aplicáveis sem exigir leitura de valores reais de secrets. |
| [AI Engineering](ai-engineering-v1.md), Standard 06, Candidate | Quando houver funcionalidade efetiva de IA no produto ou necessidade especializada pertinente, como modelos, provedores, contratos de saída, RAG, Evals, ferramentas ou operação. O uso do Codex como executor de desenvolvimento não torna AI Engineering obrigatório. |
| [AI-Assisted Secure Development Threat](ai-assisted-secure-development-threat-v1.md), Standard 07, Candidate | Para controles pertinentes à segurança do processo de desenvolvimento assistido por IA: fronteiras de confiança, entradas não confiáveis, prompt/tool-output injection, comandos e ferramentas, dependências, integridade de testes, evidências e autorizações. Aplicar proporcionalmente à superfície e ao risco, sem exigir ferramentas novas. |
| [standards/README.md](README.md) e estrutura de `standards/` | Apoio ao inventário. Conferir arquivos reais; o README atual é descritivo e não constitui catálogo detalhado nem prova de existência de Standards planejados. |

Os Standards 01 a 07 estão materializados no inventário conferido para esta revisão. Verificar o inventário real ao iniciar ou retomar o trabalho; a presença de um arquivo não permite inferir estado Stable. Preservar os estados declarados nas fontes: os Standards 06 e 07 permanecem Candidate. Candidate não significa inexistência; documentos nesse estado podem orientar o trabalho dentro de seu alcance e governança. Existência documental não comprova eficácia operacional nem ativação automática de Skills. O relato histórico de inventário do Product System descreve sua autoria, não o estado atual de `standards/`.

Selecionar somente os Standards pertinentes ao objetivo, à superfície, ao risco e à fase, sem leitura integral de todos os sete por padrão. Não duplicar integralmente suas regras nem presumir a existência de Standards futuros. Quando novos Standards forem efetivamente criados e aprovados para seu alcance, incorporar sua seleção mediante revisão autorizada da governança e deste roteamento. A ausência de documento futuro não suspende os controles centrais.

## G. Estratégia de leitura e contexto

1. **Recuperar o mínimo necessário:** instrução da tarefa, Gate A, `AGENTS.md`, estado real da superfície e critérios de aceitação. Localizar fontes por índices, estrutura, nomes, descrições e referências disponíveis.
2. **Selecionar antes de expandir:** cruzar classificação e riscos com o inventário. Consultar referências específicas de código, testes, contratos e seções normativas; não carregar todas as capacidades preventivamente.
3. **Ler para aplicar:** ao selecionar uma Skill para uso operacional, ler suas instruções completas antes de aplicá-la, caso ainda não estejam disponíveis e válidas no contexto. Descrição e título orientam seleção, mas não substituem suas obrigações. Seguir referências adicionais necessárias à atividade.
4. **Expandir por necessidade:** aprofundar leitura diante de ambiguidade, dependência, conflito, risco ou informação insuficiente. Ler o documento integral quando a coerência global ou a obrigação da tarefa exigir. Nunca omitir instrução obrigatória para reduzir contexto.
5. **Reutilizar e revalidar:** aproveitar fatos e instruções já verificados na execução enquanto válidos. Revalidar arquivos alterados, versões, permissões, ambiente, contratos e decisões cujo estado possa ter mudado, especialmente após retomada ou mudança de escopo. Relato anterior não substitui conferência do estado real.

**Seleção documental** é localizar, ler ou comparar uma fonte para decidir pertinência ou consistência. **Ativação operacional** é aplicar suas instruções à tarefa. Inspecionar o conteúdo das 12 Skills na autoria deste Standard é uma atividade excepcional de compatibilidade, não ativação de todas nem procedimento integral obrigatório para cada tarefa futura.

Uma referência no documento não carrega nem executa uma Skill por si só. Não presumir descoberta, roteamento, retenção de contexto ou revisão automáticos do Codex sem verificação no ambiente. Esta política pode ser aplicada pelo executor com os recursos já disponíveis, sem infraestrutura adicional. Não promete percentual de redução de tokens nem limite fixo de leitura.

## H. Matriz prática de roteamento

Rótulos de Skills correspondem exclusivamente à seção E. **PS** é Product System, **WE** é Web Experience e **CR** é este Standard, conforme a seção F. PS rege todos os cenários; CR orienta a decisão ou reavaliação, sem impor releitura. WE aplica-se às superfícies de experiência.

As linhas descrevem atividades exemplificadas, não pacotes obrigatórios para qualquer produto da categoria. Skills principais atendem a superfície indicada; condicionais entram somente diante da condição. Capacidades normalmente desnecessárias pressupõem ausência de efeito nessa superfície e devem ser reavaliadas se surgir risco.

| Tipo de tarefa | Skills principais | Skills condicionais | Standards pertinentes | Normalmente desnecessárias | Risco que altera a seleção |
| --- | --- | --- | --- | --- | --- |
| Alteração simples de texto visível | Clara; correção literal pode usar orientação editorial e conferência direta. | Kael se mudar estrutura/estado; Visual QA se impacto visual relevante; SEO/GEO se descoberta ou fatos públicos afetados. | PS, WE, CR | Data, AI Engineering, Release, direção de arte completa. | Promessa factual, consentimento, erro de segurança ou texto que altera entendimento da ação. |
| Nova landing page pública | Julian, Clara, Kael, Visual QA; SEO para página indexável. | Quality para interações; GEO para identidade/descoberta por IA; Vera para coleta/integração; Release para publicação no escopo. | PS, WE, CR | Data sem armazenamento; AI Engineering sem modelo integrado. | Formulário, dado pessoal, integração, efeito de conversão contratado ou exposição. |
| Refatoração de interface existente | Kael, Quality; Visual QA para mudança visual relevante. | Software Design para lógica/contratos; Julian para UX/sistema visual; Clara para copy; Vera/Data se suas superfícies mudarem. | PS, WE, CR | SEO/GEO em UI privada; Release sem distribuição. | Regressão de foco, fluxo, responsividade, permissão ou comportamento adjacente. |
| Cadastro autenticado com persistência | Software Design, Vera, Data, Quality; Kael se UI incluída. | Visual QA para alteração visual relevante; Clara para mensagens; Julian para UX novo; Release para entrega. | PS, CR; WE se UI/experiência | SEO/GEO da área privada; AI Engineering sem IA. | Isolamento entre usuários, validação, duplicidade, concorrência e perda de dados. |
| API com autorização | Software Design, Vera, Quality. | Data para acesso/consulta persistente afetados; Release para preparação operacional. | PS, CR | Clara, Julian, Kael, Visual QA, SEO/GEO sem UI pública. | Acesso horizontal/vertical, tenant, entrada não confiável e quebra de consumidores. |
| Migração de banco de dados | Data, Quality. | Vera para acesso/dados sensíveis; Software Design para contrato/código; Release para execução e recuperação operacional. | PS, CR; WE se experiência afetada | Direção visual, copy, SEO/GEO, AI Engineering sem impacto nessas áreas. | Irreversibilidade, locks, indisponibilidade, compatibilidade e recuperação não comprovada. |
| Aplicação desktop/local com GUI | Kael, Quality; Software Design para lógica; Visual QA para mudança visual relevante. | Julian/Clara para UX/texto; Data para arquivos/banco; Vera para permissões/dados/integração; Release para instalador/atualização. | PS, WE, CR | SEO/GEO sem páginas públicas; AI Engineering sem IA. | Acesso a arquivos, escala de janela, perda de trabalho, execução de comandos e atualização. |
| Dashboard empresarial autenticado, alteração de UI | Kael, Quality; Visual QA para mudança visual relevante. | Julian para nova hierarquia; Software Design/Data para cálculos/consultas; Vera para dados/permissões/exposição; Clara para significado dos indicadores. | PS, WE, CR | SEO/GEO da área privada; AI Engineering sem modelo; Release sem entrega. | Dados sensíveis, exportação, isolamento, dado atrasado apresentado como atual ou indicador incorreto. |
| Integração com modelo de IA | AI Engineering, Software Design, Quality; Vera para dados, provedor e limites de confiança. | Data para base/índice/histórico persistente; Kael/Visual QA para UI; Release para operação. | PS, CR; WE se UI/experiência | GEO pela mera existência de IA; SEO sem página indexável. | Prompt/tool injection, vazamento, autorização em RAG, custo, falha externa e ação material. |
| Correção de vulnerabilidade em código | Vera, Software Design, Quality. | Data, AI Engineering, Kael/Visual QA ou Release conforme origem, efeito e entrega autorizada. | PS, CR; WE se interface afetada | Copy, direção de arte, SEO/GEO sem efeito nessas superfícies. | Falha crítica conhecida, credencial exposta, exploração, contenção ou produção fora do Gate A. |
| Preparação de deploy | Release, Quality. | Vera para configuração, secrets/exposição; Data para migration/restore; SEO para publicação indexável; Visual QA para superfície visual pendente. | PS, CR; WE se experiência pertinente | Redesign, reescrita de copy e AI Engineering sem componente alterado. | Ambiente errado, secrets, migration, indisponibilidade, rollback e autorização do destino. |
| Correção pequena em código, baixo risco | Software Design; Quality se bug ou comportamento afetado. | Skill da superfície se descoberta justificar; verificação direta pode bastar sem efeito comportamental. | PS, CR; WE somente se experiência | Vera aprofundada, Data, Release, design e IA sem condição aplicável. | Descoberta de acesso, dado persistente, contrato ou efeito funcional antes desconhecido. |

## I. Seleção por fase

Reavaliar a seleção conforme a atividade mudar, sem impor pipeline de agentes ou repetir toda a leitura. Manter instruções já consultadas e válidas; deixar de usar operacionalmente capacidades sem contribuição à fase não elimina controles ou achados anteriores.

| Fase | Foco da seleção |
| --- | --- |
| Discovery | Compreender objetivo, estado, superfícies e riscos; consultar especialistas para esclarecer questões reais, sem ativar todo o inventário. |
| Planejamento | Relacionar incrementos, critérios, dependências e verificações às capacidades suficientes. |
| Arquitetura | Software Design para responsabilidades/contratos; Vera para confiança; Data e AI Engineering quando essas decisões existirem. Não exigir redesenho arquitetural para ajuste local. |
| Implementação | Aplicar a Skill da superfície: lógica, UI, texto, persistência ou integração; preservar decisões aprovadas. |
| Testes | Quality conforme comportamento, contratos e risco; especialistas para integridade, autorização ou evals; Visual QA quando a renderização precisar de exame. |
| Revisão | Selecionar Engineering, Security e Visual Review conforme a seção M e reunir evidências, com independência real ou autorrevisão declarada. |
| Preparação de release | Release quando artefato, configuração, distribuição ou recuperação integrarem o escopo; adicionar capacidades das pendências reais. |
| Verificação pós-entrega | Release e verificações de comportamento, segurança, dados e experiência afetados, somente no destino e alcance autorizados. |

Release pode ser desnecessária na correção inicial de um rótulo e tornar-se pertinente quando a preparação de publicação integrar o escopo. Essa mudança de fase não concede autorização para deploy. Não executar fases fora do Gate A para completar artificialmente o ciclo.

## J. Gatilhos de ampliação do roteamento

Reavaliar antes da ação dependente quando ocorrer qualquer condição abaixo. Selecionar capacidades adicionais somente quando sua contribuição for justificada.

| Descoberta | Reavaliação necessária |
| --- | --- |
| A superfície aumenta | Reclassificar arquivos, usuários, contratos e critérios; escolher especialistas das novas superfícies. |
| Surge autenticação, autorização ou dado sensível | Avaliar Vera e testes negativos/abuso com Quality; Data conforme armazenamento. |
| Entra persistência | Avaliar Data, integridade, concorrência e recuperação; Vera e Release conforme impacto. |
| Surge integração externa | Avaliar Software Design, Vera e Quality para contrato/confiança/falhas; Data se persistir. |
| É identificada vulnerabilidade | Aplicar análise de Vera e Security Gate pertinente, com correção/testes autorizados e bloqueio de release diante de falha crítica conhecida. |
| A alteração exige UI renderizada ou QA visual | Avaliar Kael e Visual QA; Julian/Clara se o achado for de direção ou texto. Falta de ambiente não elimina a necessidade. |
| Passa a existir preparação de release | Selecionar Release e conferir autorização, destino, readiness e recuperação. |
| Entram IA, RAG ou execução de ferramentas | Selecionar AI Engineering quando houver componente de IA; Vera para confiança/comandos; Data e Quality conforme dados e avaliação. |
| A investigação revela risco não previsto | Aprofundar fontes relevantes, rever controles e testes e registrar a mudança de seleção. |

Descoberta dentro do Gate A permite ajustar o roteamento e trabalhar autonomamente. Se envolver mudança material fora do Gate A, conflito aprovado, custo novo, produção não autorizada ou outro bloqueio do Product System, interromper a ação afetada e solicitar decisão humana antes de executá-la. Continuar atividades independentes e seguras já autorizadas. Registrar o motivo e o alcance, sem transformar mudança ordinária de Skill em microaprovação.

## K. Roteamento negativo

Excluir capacidades sem condição aplicável, mantendo o baseline e as verificações essenciais:

- Não ativar SEO em dashboard privado nem por usar tecnologia web.
- Não ativar GEO para RAG interno; descoberta pública e engenharia de IA têm finalidades distintas.
- Não ativar AI Engineering apenas porque a copy comercial menciona IA ou porque o trabalho é executado com assistência de IA.
- Não ativar Data para texto, estilo ou arquivo de código estático sem relação com armazenamento de dados do produto.
- Não exigir Visual QA para backend puro sem efeito em interface; se a resposta alterar um estado visível, avaliar esse efeito.
- Não exigir Release para análise documental ou alteração sem preparação de distribuição no escopo.
- Não exigir direção de arte completa para correção pontual que preserva design aprovado.
- Não ativar Software Design para conteúdo ou ajuste puramente visual sem lógica a revisar.
- Não exigir revisão profunda de segurança ou suíte completa em ajuste trivial sem risco correspondente; verificar a alteração diretamente.

As exclusões são condicionais. Não permitem ignorar risco descoberto, instrução obrigatória, integração efetiva ou critério de aceitação. Também não autorizam tratar um teste necessário indisponível como inaplicável.

## L. Segurança e capacidades críticas

O roteamento não substitui Security Gate nem os limites e bloqueios do Product System. Aplicar seu baseline em toda tarefa; selecionar Vera para análise especializada quando o risco justificar, mesmo que a mudança funcional seja pequena.

Autenticação não garante autorização. Validar permissões por ação e recurso no componente confiável, inclusive backend quando houver. Em aplicação local, identificar o componente responsável pelo domínio e acesso; restrição visual não garante proteção. Não confiar em IDs, roles ou tenants editáveis pelo cliente.

Mudanças em dados, secrets, execução de comandos e limites de confiança exigem avaliação apropriada. Selecionar Data para integridade/persistência, AI Engineering para modelos/RAG/ferramentas e Release para exposição/configuração conforme as superfícies reais. Resposta do modelo, documento recuperado ou serviço externo não concede autorização.

Falhas críticas materiais conhecidas de autenticação, autorização, secrets ou injeção não podem ser ignoradas e bloqueiam release. Conter e corrigir somente dentro da autorização existente; alteração de credenciais, acesso a produção, destruição ou ação material exige a decisão prevista no Product System. Não enfraquecer controles para reduzir contexto, passar testes ou liberar entrega.

Preservar Gates A/B. Aprovação técnica de roteamento ou Security Gate não autoriza versionamento, merge, release ou deploy fora do alcance humano aprovado.

## M. Revisão e QA

Selecionar verificações pelo requisito, pela alteração final e pelo risco. Roteamento seletivo não dispensa verificações essenciais. A seleção de uma Skill não constitui evidência de que teste ou revisão foi executado.

| Atividade | Critério de seleção e evidência |
| --- | --- |
| Engineering Review | Inspecionar correção, contratos, simplicidade, compatibilidade, testes, documentação e escopo. Software Design quando houver código/lógica; em alteração documental ou editorial, inspeção pertinente sem exigir essa Skill. |
| Security Review | Vera quando permissões, dados, secrets, entrada/saída, dependências, configuração ou confiança exigirem análise especializada. Registrar controles, testes e decisão do Security Gate pertinente. |
| Visual Review | Visual QA para mudança visual relevante ou critério de experiência renderizada; examinar telas/janelas e estados pertinentes. Julian/Clara conforme achados de direção/texto. Código ou mockup não substitui renderização. |
| Testes funcionais e regressão | Quality para comportamentos, fluxos, contratos e integrações; incluir reprodução do defeito, caminho esperado e adjacências afetadas. Ajuste trivial sem efeito comportamental pode usar conferência direta. |
| Testes negativos e abuso | Quality com Vera e especialistas quando houver entradas inválidas, falhas externas, permissões, isolamento, injeções, concorrência, ferramentas ou outro risco identificado. Testar chamadas diretas ao componente confiável quando pertinente. |

Preferir revisor distinto quando houver capacidade real disponível e autorizada. Se o executor revisar, declarar **autorrevisão**, superfície e limitações. Outra etapa, ferramenta ou Skill não cria independência. Quando revisão independente for critério obrigatório, sua ausência impede prontidão, conforme o Product System. Não criar pipeline obrigatório de múltiplos agentes.

Usar os resultados de teste `PASS`, `FAIL`, `BLOCKED` e `NOT RUN` conforme o Product System. Teste essencial indisponível é pendência com causa e impacto; não é aprovação. Os pareceres `APPROVED`, `CHANGES_REQUIRED` e `BLOCKED` devem identificar objeto e alcance. Corrigir e repetir verificações afetadas antes de concluir. QA visual não substitui funcional, segurança, avaliação completa de acessibilidade ou performance.

## N. Decisões e evidências

Registrar de forma curta no contexto ou relatório já previsto pelo Product System:

| Informação | Conteúdo proporcional |
| --- | --- |
| Classificação | Objetivo, fase, tipo de produto e superfícies afetadas. |
| Riscos relevantes | Consequências e limites que justificam aprofundamento ou verificação direta. |
| Capacidades selecionadas | Standards pertinentes e Skills efetivamente usadas, com justificativa sucinta. |
| Condicionais | Capacidade adicional e condição concreta de entrada, quando útil ao plano. |
| Mudanças de roteamento | Descoberta, alteração da seleção e eventual decisão humana necessária. |
| Limitações | Fonte, ambiente, ferramenta, teste ou revisão indisponível; impacto e pendência. |

Não criar arquivo de log obrigatório por tarefa, duplicar documentos ou registrar secrets/dados pessoais desnecessários. Para mudança trivial, basta algo como: “Correção de rótulo na UI existente, sem alteração de lógica; orientação editorial e conferência renderizada; sem necessidade de Data ou Release neste escopo”.

Separar seleção prevista, instrução consultada, procedimento aplicado e resultado observado. Registrar testes e revisões pelos mecanismos existentes, com evidência suficiente para o alcance declarado. Reutilizar fatos verificados na execução não equivale a implementar memória persistente.

## O. Exemplos completos

### 1. Alteração de copy em website

**Tarefa:** tornar claro um parágrafo de serviço público, preservando oferta, rota e layout. **Roteamento adequado:** PS, critérios de conteúdo do WE e CR para seleção; Clara para clareza e fatos, com conferência do texto final em contexto renderizado. Kael se a estrutura mudar; SEO se metadados/semântica de descoberta forem afetados; GEO se identidade factual e descoberta por IA entrarem no objetivo. Visual QA se houver impacto visual relevante.

**Roteamento inadequado:** ativar Data, AI Engineering, Release ou direção de arte completa sem alteração nessas superfícies, ou ignorar uma promessa nova por ser “só texto”. Validar fidelidade factual, leitura e ausência de efeito não previsto.

### 2. API com BOLA/IDOR

**Tarefa:** corrigir acesso a registro de outro usuário pela troca de identificador. **Roteamento adequado:** PS e CR; Vera para autorização por recurso no componente confiável, Software Design para correção e Quality para testes positivos, acesso horizontal/vertical e regressão. Data quando consulta ou isolamento persistente forem afetados. WE somente se houver efeito de experiência; Release quando preparação de entrega autorizada entrar no escopo.

**Roteamento inadequado:** tratar login ou botão oculto como controle suficiente, dispensar Vera por poucas linhas alteradas ou selecionar capacidades visuais sem UI. A falha crítica conhecida bloqueia release; conter/corrigir respeitando o Gate A.

### 3. Cadastro empresarial com banco de dados

**Tarefa:** implementar cadastro autenticado com unicidade e edição concorrente. **Roteamento adequado:** PS, WE e CR; Software Design para regras, Vera para autorização/isolamento, Data para constraints/transações/concorrência, Kael para formulário e Quality para sucesso, inválidos, duplicidade, conflitos e regressão. Visual QA para a interface alterada; Clara para mensagens ou Julian para nova UX conforme necessidade.

**Roteamento inadequado:** selecionar apenas Kael e validar somente no cliente; ativar SEO/GEO na área privada ou AI Engineering sem IA. Migration e entrega acrescentam Data/Release e avaliação de recuperação; operação destrutiva exige a autorização pertinente.

### 4. Dashboard autenticado

**Tarefa:** reorganizar indicadores existentes sem alterar consultas ou permissões. **Roteamento adequado:** PS, WE e CR; Julian para hierarquia, Kael para composição, Visual QA para leitura/renderização e Quality para filtros e estados afetados. Conferir significado, unidade, período e atualização dos indicadores. Vera se aparecer exposição de dados/permissões; Software Design/Data se cálculo ou consulta mudar.

**Roteamento inadequado:** ativar SEO/GEO por ser web, Data apenas porque o dashboard exibe dados ou AI Engineering por mostrar métricas comerciais de IA. Se a tela expuser dado protegido, reavaliar segurança antes de avançar.

### 5. Interface desktop

**Tarefa:** corrigir formulário cortado em janela menor, preservando design. **Roteamento adequado:** PS, WE e CR; Kael para layout e acessibilidade, Visual QA no aplicativo renderizado em janelas/escalas pertinentes e Quality para teclado e comportamento afetado. Julian se a solução exigir mudança real de hierarquia; Data/Vera se surgirem efeitos em arquivos ou permissões.

**Roteamento inadequado:** impor servidor, SEO/GEO ou redesign completo. Release só entra se houver empacotamento, distribuição ou atualização no escopo. Validar controles acessíveis sem perda de conteúdo ou operação.

### 6. Integração com modelo de IA

**Tarefa:** adicionar resposta baseada em documentos restritos por tenant. **Roteamento adequado:** PS e CR, WE se houver UI; AI Engineering para recuperação/resposta, contratos e evals, Vera para autorização antes da recuperação e limites de confiança, Data para base/índice persistente, Software Design para integração e Quality para regressão, ausência de evidência, falha externa, isolamento e injeção. Release quando operação integrar o escopo.

**Roteamento inadequado:** usar GEO como engenharia de RAG, confiar no modelo para decidir acesso ou adicionar banco vetorial/framework sem requisito. Validar qualidade, segurança, custo e latência pertinentes com dados sintéticos ou autorizados; ações materiais continuam sujeitas à governança.

### 7. Preparação de release

**Tarefa:** preparar artefato e procedimento para entrega de alteração aprovada no desenvolvimento. **Roteamento adequado:** PS e CR; Release para build/configuração/recuperação e Quality para smoke e verificações necessárias. Vera para secrets/exposição, Data para migration/restore e WE/Visual QA para experiência afetada conforme o produto. Identificar versão, destino, evidências, riscos e procedimento para Gate B.

**Roteamento inadequado:** fazer deploy porque o build passou, alegar rollback testado sem ensaio ou iniciar redesign/copy fora do escopo. Preparação concluída não comprova publicação nem verificação pós-entrega.

### 8. Correção simples em código existente

**Tarefa:** corrigir transformação determinística que formata incorretamente um valor, sem persistência ou controle de acesso. **Roteamento adequado:** PS e CR; Software Design para alteração mínima e Quality para reproduzir o defeito, limites pertinentes e regressão próxima. WE/Kael/Visual QA somente se o efeito em interface exigir sua participação.

**Roteamento inadequado:** ativar todas as Skills, criar camadas ou executar suíte integral sem justificativa; também é inadequado dispensar teste de comportamento por ser uma linha. Se a investigação revelar autorização ou armazenamento afetado, reclassificar e ampliar o roteamento.

## P. Definition of Ready e Done do roteamento

### Definition of Ready

O roteamento está suficientemente preparado para a próxima atividade quando objetivo/Gate A e critérios estão claros, superfícies e riscos relevantes foram identificados, fontes pertinentes foram localizadas e o conjunto suficiente foi selecionado. Antes de aplicar uma Skill, suas instruções completas devem estar consultadas e válidas. Dependências, verificações e limitações da etapa precisam estar explícitas.

Não exigir análise extensa para ajuste trivial. Uma lacuna posterior não impede atividade independente autorizada; lacuna material da próxima ação deve ser resolvida antes dela.

### Definition of Done

O roteamento pode ser considerado validado **para a tarefa e o alcance examinados** quando:

- A seleção final cobre requisitos, superfícies e riscos descobertos, com ampliações justificadas e sem capacidade crítica omitida.
- As instruções pertinentes foram aplicadas e as verificações essenciais da tarefa foram executadas com resultados aceitos.
- As revisões exigidas ocorreram, com achados tratados, independência ou autorrevisão identificada e limitações registradas.
- Decisões e evidências suficientes estão no contexto/relatório autorizado, prontas para Gate B quando pertinente.

Esses critérios complementam a Definition of Done do Product System. Não autorizam declarar prontidão com teste essencial ausente, revisão obrigatória indisponível ou blocker material. Em ajuste trivial, inspeção e registro mínimo podem cumprir os critérios.

A validação documental deste Standard não demonstra operação automática do mecanismo, eficácia generalizada ou economia de contexto. A política ainda requer testes controlados posteriores no projeto, com tarefas representativas e evidências de seleção, reavaliação e cobertura. Aprovação desta autoria e estado Stable não substituem essa validação operacional.

## Q. Exceções, compatibilidade e evolução

Revisão 1.2, autorizada no escopo de design e UI/UX: explicita a ligação entre fonte criativa, decisão aplicada e evidência renderizada, sem ativar todas as capacidades por padrão ou exigir microaprovações.

Adaptar profundidade de leitura, registro e verificação ao risco, preservando autorização, segurança, integridade e critérios essenciais. Simplificação rotineira dentro do Gate A não exige microaprovação. Exceção relevante deve identificar regra, motivo, alcance, risco, controle compensatório, responsável e condição de reavaliação no contexto autorizado, conforme o Product System.

Exceção não altera silenciosamente governança nem permite ignorar falha crítica ou instrução obrigatória. Conflito material, mudança relevante de segurança ou decisão arquitetural aprovada exige resolução humana antes da ação dependente. Não ampliar arquitetura, tooling ou arquivos por conveniência de roteamento.

Evoluir somente diante de necessidade comprovada, conflito ou achado de uso. Quando novas Skills ou Standards forem efetivamente aprovados, inspecionar suas fontes e limites, avaliar sobreposição e atualizar o inventário, matriz e referências mediante escopo autorizado. Não presumir capacidade futura nem editar outros documentos por consequência sem autorização própria.

Aplicar a política de versionamento do Product System: incremento maior para incompatibilidade de governança, menor para regra operacional compatível e revisão corretiva para esclarecimento sem mudança de obrigação. Registrar versão, mudança, justificativa, impacto e decisão humana no mecanismo autorizado; não manter a mesma versão ao alterar regras silenciosamente.

| Versão | Estado | Mudança e limite de evidência |
| --- | --- | --- |
| 1.0 | Stable | Definição inicial da política de roteamento proporcional, inventário das 12 Skills, matriz, exclusões e critérios de revisão. Fundamentada na inspeção das fontes existentes; validação operacional controlada permanece posterior. |
| 1.0.1 | Stable | Revisão corretiva de consistência documental: atualização do inventário e da matriz após a publicação dos Standards 04 a 07, com reconhecimento das fontes existentes e correção de referências históricas. Sem criação de obrigação operacional, alteração de Gates ou mudança arquitetural. Aprovada expressamente pelo responsável na conversa de 08/10/2026, para edição das seções A, F e Q. A alteração é documental e não demonstra ativação automática de Skills ou eficácia operacional do roteamento. |
| 1.1 | Stable | Gate A de usabilidade de 13/10/2026: brief por pedido curto, distinção de escopo, destino workspaces e QA proporcional. Preserva 7/12/5 e Gates; testes documentais não comprovam nova sessão Codex. |

Recomenda-se que a validação futura examine ajustes triviais, interfaces públicas/privadas, APIs, dados, aplicações locais, IA e preparação de release. Avaliar omissões, excessos, gatilhos de ampliação, respeito aos Gates e limitações de execução; corrigir a política por revisão autorizada. Essa recomendação não instala mecanismo nem inicia testes ou novo Standard fora do escopo aprovado.

Revisão corretiva 1.2.1 (13/10/2026): referências normativas sem versão fixa e consistência com a taxonomia de testes vigente, quando pertinente. Preserva Gates, responsabilidades e estado canônico. Ajuste documental autorizado na revisão final para publicação; não comprova nova validação operacional.
