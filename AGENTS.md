# AGENTS.md

## Objetivo

Este repositório contém o My Easy Development System.

<!-- MEDS-WORKSPACE-START -->
## Manutenção do MEDS ou desenvolvimento de projeto

Classificar o pedido antes de escrever. Manutenção explicitamente solicitada do framework pode alterar suas fontes dentro do Gate A. Pedido de aplicativo, site ou sistema é desenvolvimento de projeto: criar automaticamente `workspaces/<slug>/` a partir da raiz MEDS e trabalhar exclusivamente nessa pasta. Não usar `playground/`, mover ou excluir projetos existentes.

Derivar um slug curto do nome/objetivo: minúsculas ASCII, acentos removidos, palavras separadas por hífen, somente `[a-z0-9-]`, sem separadores de caminho, `..`, pontos ou espaços finais. Evitar nomes reservados Windows (`con`, `prn`, `aux`, `nul`, `com1` a `com9`, `lpt1` a `lpt9`), usando prefixo `projeto-`; se não restar nome, usar `projeto`. Ex.: Site de Condomínio → `workspaces/site-condominio/`. Conferir destino resolvido, symlinks e junctions antes da criação; o destino deve permanecer em `workspaces/` da instalação observada. Se já existir, analisar: retomar somente quando for o projeto solicitado; caso contrário, escolher sufixo livre (`-2`, `-3`) e informar a pasta escolhida. Não sobrescrever arquivos sem análise e justificativa.

Para desenvolvimento, a única raiz de escrita do agente é a pasta do projeto autorizado, incluindo testes, assets, documentação, temporários e evidências. Ler AGENTS, Standards, Skills e templates compartilhados é permitido; não copiá-los por rotina. Não modificar AGENTS da raiz, Standards, Skills, templates, `scripts/check.py`, configurações, outros projetos ou histórico Git do MEDS. Executar comandos a partir do projeto e conferir destinos de saída. Esta é uma regra de escopo, não isolamento de sistema operacional nem substituição do sandbox; permissões reais continuam valendo.

O Git do MEDS ignora projetos em `workspaces/`, preservando apenas `.gitkeep`. Não usar `git add -f`. Se houver arquivos de projeto já versionados, registrar o problema sem removê-los automaticamente. Cada projeto pode ter Git independente somente quando solicitado explicitamente; não inicializar repositório por rotina. Se um repositório independente mudar a descoberta de instruções ancestrais, conferir o catálogo e usar o fluxo de projeto externo autorizado, sem editar o MEDS.
<!-- MEDS-WORKSPACE-END -->

## Pedido simples e entrega local

Uma descrição em linguagem natural suficientemente clara pode constituir Gate A para criar, desenvolver, testar, revisar, corrigir e documentar localmente o projeto. Não exigir prompt técnico, formulário ou conhecimento da estrutura MEDS. Antes de implementar, sintetizar objetivo, público, tipo de aplicação, funcionalidades, requisitos não funcionais pertinentes, arquitetura/tecnologias proporcionais, identidade e recursos visuais quando aplicáveis, critérios de aceite, testes e condições de entrega. Consultar o Capability Routing existente e apenas as fontes pertinentes.

Adotar e registrar premissas razoáveis para lacunas não essenciais, no contexto ou README do projeto, sem exigir documento extra. Não fabricar endereços, preços, registros, credenciais, dados pessoais ou informações comerciais reais; dados sintéticos devem ser identificados. Lacunas críticas de operações protegidas bloqueiam somente a ação dependente: não inventar dados nem executar ações irreversíveis. Os Gates abaixo permanecem aplicáveis.

Entregar fontes, assets locais e instruções para abrir/executar o software na pasta autorizada, com premissas, funcionalidades, testes realmente executados, resultados, bloqueios e riscos residuais. Selecionar QA pelo tipo e risco, corrigir falhas e repetir verificações afetadas. QA visual requer interface renderizada e ferramenta disponível; inspeção de código não equivale a teste no navegador. Não declarar conclusão integral se validação essencial estiver indisponível. Nenhum pedido simples autoriza publicação, custo novo, credenciais reais ou Git mutável por consequência.

## Linguagem autoral

Esta é a fonte normativa principal de linguagem do MEDS. Não usar U+2013 ou U+2014 como pontuação em textos autorais: interfaces, títulos, descrições, menus, feedback, documentação, README, apresentações e respostas finais. Preferir vírgula, dois-pontos, ponto e vírgula, parênteses ou frases separadas, conforme o sentido. Revisar também strings de interface dentro do código.

Preservar operadores, sintaxe, hífens legítimos, nomes próprios confirmados, citações fiéis de terceiros e formatos técnicos obrigatórios. Exceções precisam de contexto e justificativa; não corrigir caracteres cegamente. Quando disponível, usar `scripts/check_language.py` nas fontes suportadas e revisar os textos não cobertos, inclusive a resposta final. Em projeto independente sem esse script, usar verificação equivalente autorizada ou registrar a parte automatizada como NOT RUN, mantendo revisão editorial. Código de teste, evidência histórica preservada e sintaxe técnica não devem ser confundidos com conteúdo autoral corrente. Um resultado estático não comprova qualidade editorial.

## Entrega e qualidade de interface

Para interface nova ou redesign, aplicar a exploração criativa e o aceite visual do Standard Web Experience. Registrar decisões e evidências do procedimento aplicado, não apenas nomes de Skills. A avaliação estética final continua humana; não declarar originalidade de mercado nem aprovação visual completa sem inspeção das telas renderizadas. Se o navegador estiver indisponível, registrar `BROWSER_QA: BLOCKED` e o impacto.

## Resposta final do projeto

Uma única resposta consolidada deve informar nome do projeto, pasta de entrega, funcionalidades implementadas, principais arquivos, Standards e Skills efetivamente consultados, testes realmente executados com resultados, como abrir/executar e limitações/pendências reais. Não listar capacidades apenas disponíveis nem exigir relatório extenso ou documentação excessiva em projeto pequeno.

Para testes: PASS = executado e aprovado; FAIL = executado e reprovado; BLOCKED = não executado por impedimento comprovado; NOT RUN = não executado por outro motivo. Identificar inspeções como inspeções, sem apresentá-las como execução funcional. DOM simulado e imagem isolada não substituem navegador real; não alegar QA visual de site sem ele. Não inventar evidências. Repetir testes pertinentes após correções.

## Regra principal

Antes de executar uma tarefa:

1. identificar propósito, domínio, risco e superfície afetada;
2. ativar apenas os Standards e Skills necessários;
3. evitar overengineering;
4. trabalhar autonomamente dentro do escopo aprovado;
5. testar, revisar e corrigir antes de declarar conclusão.

## Autonomous Mode

Gate A humano:
O usuário aprova objetivo, escopo e limites de autonomia. A instrução inicial pode constituir essa autorização quando for suficientemente clara.

Entre Gate A e Gate B, atuar sem microaprovações dentro do escopo autorizado:
- planejar;
- implementar;
- testar;
- revisar;
- corrigir;
- executar QA e Security Gate quando aplicável;
- atualizar documentação.

Distinguir autor e revisor quando houver capacidade real de revisão independente. Se a revisão for feita pelo executor, declarar autorrevisão, sem alegar independência.

Interromper somente a ação afetada por blocker material e registrar a decisão humana necessária. Solicitar essa decisão quando perguntas forem permitidas pelo Gate A; se estiverem proibidas, concluir as atividades independentes autorizadas. Isso se aplica quando houver:
- destruição ou migration com risco de perda de dados;
- credencial ausente ou uso de credenciais reais fora do escopo;
- custo novo;
- acesso a produção não autorizado;
- conflito material de requisitos ou com decisão aprovada;
- mudança material de escopo;
- mudança relevante de segurança;
- ação irreversível.

Bloqueio ambiental impede somente a operação afetada; aplicar o tratamento de `BLOCKED` da seção de escrita abaixo.

Gate B humano:
- apresentar resultado;
- evidências;
- testes;
- riscos residuais;
- aguardar autorização humana para merge, push a branch protegida, release ou deploy.

## Escopo de escrita no Gate A

Antes de criar, modificar ou gerar arquivos, identificar as raízes de escrita autorizadas pelo Gate A e a finalidade de cada uma. O limite vale para produto, testes, temporários, diagnósticos, hashes, manifestos, logs, backups, relatórios e evidências de autoria do agente. Autorização do workspace não implica autorização genérica para `/tmp`, `TMPDIR`, home ou outros diretórios.

Priorizar caminhos relativos; conferir `realpath`, symlinks, redirecionamentos e caminhos absolutos para impedir fuga da raiz. Distinguir escritas de autoria do agente de escritas internas inevitáveis do runtime; exceções operacionais de runtime exigem raiz, processo, finalidade e proveniência documentados e não ampliam o Gate A nem permitem acessar segredos.

Quando Gate A exigir confinamento técnico estrito, verificar, com o UID/namespace/perfil efetivos e mecanismos já existentes e permitidos, escrita positiva interna e tentativa negativa externa; registrar o alcance das sondas. As sondas externas também precisam de autorização específica para seus destinos e efeitos. Texto de prompt, `TMPDIR` ou `/tmp` privada gravável não demonstram por si só confinamento estrito.

Diante de bloqueio ambiental, não alterar sandbox nem pedir permissões; concluir as demais atividades permitidas e declarar `BLOCKED`. O Codex decide autonomamente todos os detalhes técnicos dentro do Gate A, sem microaprovações; publicação, operações destrutivas, custos, credenciais e Gate B permanecem sob autorização específica.

Usar comandos/processos novos dentro do sandbox autorizado; não enviar comandos a terminais preexistentes ou iniciados fora dele. Se o Gate A proibir novas decisões durante a execução, registrar decisões materiais pendentes sem perguntar e continuar somente as atividades independentes autorizadas.

## Routing

Consultar:
- `standards/`: aplicar apenas standards existentes e pertinentes;
- `.agents/skills/`: diretório canônico das Skills descobertas pelo Codex.

`skills/` é legado/documental, não o diretório runtime das Skills.

Não carregar todas as capacidades por padrão.
