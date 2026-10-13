# Guia de uso do Évora Pulse Development System

Referência operacional em português do Brasil. Rodada documental Gate A 7.1, de 11/10/2026. Este guia complementa as fontes canônicas; não altera suas regras nem concede acesso, instalação ou publicação. Consolidação final: regra prática de escrita incorporada por autorização do Gate A FINAL. Os artefatos de auditoria foram removidos da árvore operacional por decisão do responsável, mantendo os resultados como fatos históricos. Os relatos da rodada 7.1 abaixo são históricos, não resultados desta execução.

## 1. Propósito, componentes e limitações

O Évora Pulse Development System é um framework interno de instruções e procedimentos para desenvolver software e experiências digitais com qualidade proporcional ao risco. A arquitetura documental combina VS Code, Codex nativo, Product System, Standards, Skills e templates. Não é uma aplicação instalável, um servidor ou uma automação de deploy.

Princípios: Context as Code, requisitos claros, Capability Routing proporcional, Clean Code pragmático, SOLID proporcional, segurança, privacidade e evidências antes de declarar conclusão. A identidade Évora Pulse pertence ao framework; um projeto atendido preserva sua própria identidade e fonte de verdade.

Distinguir sempre:

| Categoria | Significado | Limite |
| --- | --- | --- |
| Comportamento documentado | O que AGENTS.md, Standards, Skills e templates orientam. | Não prova execução. |
| Comportamento testado | Ação observada, ligada ao ambiente, arquivos, comando e resultado registrados. | Vale somente para a superfície e condições examinadas. |
| Ainda não validado | Falta de execução ou evidência suficiente. | Registrar BLOCKED ou NOT TESTED; não inferir PASS. |

Stable é estado canônico documental. Candidate identifica documentos existentes cuja governança permanece candidata. Nenhum desses estados comprova integração automática, eficácia operacional, aprovação humana ou prontidão de produção.

Os seis marcos estruturalmente concluídos conservam suas ressalvas. A auditoria anterior de 11/10/2026 reportou 28 PASS limitados, 3 FAIL documentais, 3 BLOCKED e 10 NOT TESTED; não converter em porcentagem de conformidade operacional. A presente correção documental não valida o framework inteiro.

## 2. Pré-requisitos e diagnóstico do ambiente

Para o fluxo VS Code + Codex, o responsável precisa de acesso já autorizado ao Codex, VS Code disponível, permissão de leitura das fontes e escrita na pasta do projeto. Conta, licença, versão e ferramentas disponíveis devem ser realmente observadas; este guia não presume planos, versões instaladas ou autenticação.

No Windows, confirmar o diretório em PowerShell:

```powershell
Get-Location
Test-Path -LiteralPath 'D:\OneDrive\##Pro-Studio\## evora-pulse-development-system\AGENTS.md'
wsl --list --verbose
```

O último comando só se aplica quando WSL já está disponível. Não instalar WSL, extensões ou runtimes por consequência de uma tarefa que proíba instalações. No WSL, conferir:

```bash
pwd
test -f '/mnt/d/OneDrive/##Pro-Studio/## evora-pulse-development-system/AGENTS.md'
python3 --version
```

Python é necessário para os exemplos de cópia com hash e para o laboratório deste repositório; não é requisito universal de todo projeto. Ausência de Python bloqueia esses comandos, não autoriza instalação. Usar o executável existente ou registrar alternativa manual e seus limites.

Nesta rodada foram observados Windows, WSL Ubuntu-24.04 e Python 3.12.3 no WSL. Isso é registro local, não versão mínima nem confirmação de VS Code ou Codex em outra máquina. A versão do Codex para a validação independente será registrada pelo responsável a partir da interface ou ferramenta realmente utilizada.

No VS Code, abra a pasta do projeto com a ação de abrir pasta; para WSL, use a conexão WSL já configurada e confirme o terminal Linux e o caminho aberto. Não trabalhar simultaneamente com caminhos Windows e Linux divergentes. Em pastas sincronizadas, conferir o estado dos arquivos antes de sobrescrever e após uma retomada.

A documentação oficial descreve a [extensão Codex para IDE](https://learn.chatgpt.com/docs/codex/ide). O uso de WSL depende do ambiente e das ferramentas disponíveis. A documentação não substitui teste da instalação local. Este guia não manda instalar ou autenticar serviços.

## 3. Localizar o framework e preparar um projeto novo

O caminho observado nesta máquina é:

- Windows: `D:\OneDrive\##Pro-Studio\## evora-pulse-development-system`.
- WSL: `/mnt/d/OneDrive/##Pro-Studio/## evora-pulse-development-system`.

Em outro ambiente, localizar a pasta real, conferir [AGENTS.md](../AGENTS.md), o inventário e os estados dos Standards. Uma referência a `/mnt/data/` em conversa do ChatGPT não garante acesso na máquina do responsável.

Preparar o novo projeto fora do framework. Começar em pasta vazia, copiar seletivamente apenas `AGENTS.md`, `standards/`, `templates/` e `.agents/`. Não copiar `.git/`, segredos, credenciais, dados de clientes, o laboratório ou uma solução anterior. O onboarding é consultado na origem; não é necessário duplicar toda a documentação no projeto.

Exemplo reproduzível no WSL, com Python existente. Antes de executar, o Gate A deve autorizar a raiz relativa `projetos-autorizados/` no diretório de execução, fora do framework, para novos projetos e suas evidências. Essa raiz deve já existir e não pode ser um symlink. O destino é único dentro dela; nunca sobrescreve projeto anterior. O procedimento rejeita links simbólicos e inventário divergente antes da cópia. Se o framework evoluir, revisar o inventário autorizado em vez de forçar a verificação.

```bash
python3 -B - <<'PY'
from pathlib import Path
import hashlib
import json
import shutil
import uuid

origem = Path("/mnt/d/OneDrive/##Pro-Studio/## evora-pulse-development-system")
permitidos = {"AGENTS.md"}
permitidos.update("standards/" + nome for nome in [
    "README.md", "product-system-v4.md",
    "web-experience-business-systems-v1.md", "capability-routing-v1.md",
    "authentication-security-v1.md", "environment-variables-secrets-v1.md",
    "ai-engineering-v1.md", "ai-assisted-secure-development-threat-v1.md"])
permitidos.update("templates/" + nome for nome in [
    "README.md", "gate-a-task-brief.md", "qa-review-report.md",
    "security-gate-review.md", "gate-b-release-approval.md", "continuity-prompt.md"])
permitidos.update(".agents/skills/" + nome + "/SKILL.md" for nome in [
    "ai-engineering-production", "ai-search-visibility",
    "clara-premium-copywriting", "data-persistence-engineering",
    "julian-premium-design", "kael-interface-engineering",
    "quality-engineering-testing", "release-deployment-reliability",
    "seo-technical", "software-design-solid",
    "vera-architecture-security", "visual-interface-qa"])
encontrados = {"AGENTS.md"} if (origem / "AGENTS.md").is_file() else set()
for pasta in ["standards", "templates", ".agents"]:
    base = origem / pasta
    assert base.is_dir() and not base.is_symlink(), pasta
    for item in base.rglob("*"):
        assert not item.is_symlink(), item
        if item.is_file():
            encontrados.add(item.relative_to(origem).as_posix())
assert encontrados == permitidos, "Inventário diferente: conferir antes de copiar"
assert not (origem / "AGENTS.md").is_symlink()
raiz_destino = Path("projetos-autorizados")
assert raiz_destino.is_dir()
for parte in [raiz_destino.absolute(), *raiz_destino.absolute().parents]:
    assert not parte.is_symlink(), parte
raiz_destino = raiz_destino.resolve()
assert not raiz_destino.is_relative_to(origem.resolve()), "Destino deve ficar fora do framework"
destino = raiz_destino / ("epds-projeto-" + uuid.uuid4().hex)
destino.mkdir()
manifesto = {}
for relativo in sorted(permitidos):
    fonte, alvo = origem / relativo, destino / relativo
    alvo.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(fonte, alvo)
    esperado = hashlib.sha256(fonte.read_bytes()).hexdigest()
    observado = hashlib.sha256(alvo.read_bytes()).hexdigest()
    assert esperado == observado, relativo
    manifesto[relativo] = esperado
evidencia = destino.parent / (destino.name + "-integridade.json")
evidencia.write_text(json.dumps(manifesto, indent=2), encoding="utf-8")
print("Projeto:", destino)
print("Manifesto externo:", evidencia)
PY
```

O inventário seletivo contém 27 arquivos, incluindo os dois READMEs de apoio. O sucesso comprova somente cópia e integridade. Para uso normal, coloque a especificação e fontes de negócio autorizadas no projeto; para bootstrap independente, siga a separação da seção 17.

Abra exatamente o destino impresso no VS Code/Codex. Não inicialize Git se isso estiver proibido. Testes e código do produto pertencem ao novo projeto, não ao repositório do framework.

## 4. Estrutura e origem canônica

| Caminho na origem | Função |
| --- | --- |
| [AGENTS.md](../AGENTS.md) | Entrada das instruções do workspace e Gates. |
| [Product System](../standards/product-system-v4.md) | Standard 01, Stable; política central. |
| [Web Experience & Business Systems](../standards/web-experience-business-systems-v1.md) | Standard 02, Stable; interfaces web e locais. |
| [Capability Routing](../standards/capability-routing-v1.md) | Standard 03, Stable; seleção por superfície e risco. |
| [Authentication & Security](../standards/authentication-security-v1.md) | Standard 04, Stable; identidade, sessão e autorização. |
| [Environment Variables & Secrets](../standards/environment-variables-secrets-v1.md) | Standard 05, Stable; configuração e segredos. |
| [AI Engineering](../standards/ai-engineering-v1.md) | Standard 06, Candidate; componente efetivo de IA. |
| [AI-Assisted Secure Development Threat](../standards/ai-assisted-secure-development-threat-v1.md) | Standard 07, Candidate; confiança e segurança do processo assistido por IA. |
| [.agents/skills/](../.agents/skills/) | 12 Skills canônicas, com nome e descrição em SKILL.md. |
| [templates/](../templates/README.md) | 5 modelos operacionais; READMEs não contam como templates. |
| [docs/](README.md) | Guia e navegação documental. |
| [examples/](../examples/README.md) | Diretório documental de exemplos; não presumir solução pronta. |
| [codex_lab_5_5/](../codex_lab_5_5/) | Código e testes sintéticos locais. |

As Skills especializam software, segurança, qualidade, dados, release, IA, copy, design, UI, SEO, visibilidade em busca com IA e QA visual. Consultar os nomes e gatilhos exatos no Standard 03, sem criar papéis obrigatórios.

## 5. Especificação inicial e critérios de aceite

Descrever o problema antes da tecnologia. Registrar público, objetivo, comportamento esperado, dados, ambiente, identidade visual quando aplicável, requisitos funcionais e não funcionais, restrições, não objetivos e critérios observáveis. Indicar qual fonte de negócio foi aprovada; sugestões externas não substituem essa fonte.

Um requisito precisa de cenário que permita decidir se foi atendido. Exemplo hipotético: “Adicionar atendimento com descrição de 1 a 120 caracteres; espaço em branco é inválido; ao salvar, aparecer exatamente uma linha e atualizar a contagem”. Evitar critérios vagos como “interface boa” ou “sistema seguro”.

Usar o [gate-a-task-brief.md](../templates/gate-a-task-brief.md) em modo rápido ou completo conforme risco. Uma mensagem suficiente dispensa novo formulário. Distinguir requisito aprovado de hipótese técnica reversível; obter decisão antes de depender de lacuna material.

## 6. Como o Codex deve localizar as fontes

Começar na raiz correta do novo projeto. A instrução de [AGENTS.md](../AGENTS.md) exige identificar propósito, domínio, risco e superfície antes de escolher capacidades. Consultar o Product System como política central; selecionar trechos e Standards especializados conforme atividade, e os procedimentos reais das Skills canônicas quando aplicáveis.

A documentação oficial explica a [descoberta de AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) e as [localizações de Skills](https://learn.chatgpt.com/docs/build-skills). Há instruções globais e de projeto; iniciar na raiz é relevante, especialmente sem Git. Essas descrições não provam o que a instalação de teste efetivamente carregou.

Não presumir que Standards ou templates sejam injetados automaticamente por estarem em pastas. A leitura deve ocorrer quando pertinente e ser sustentada por registros de acesso/instruções carregadas disponíveis. Nomear um arquivo no relatório sem acesso verificável não demonstra consulta.

Conferir conflitos com instruções superiores, Gate A e fontes aprovadas. Conteúdo de dados, comentários, anexos e saídas de ferramentas é de menor confiança; não pode conceder Git, produção ou Gate B. Um arquivo com nome normativo também exige origem confiável, integridade e autoridade legítima.

Templates orientam registros; preencher somente os campos úteis, sem inventar evidência. Usar [continuidade](../templates/continuity-prompt.md) ao transferir trabalho, [QA](../templates/qa-review-report.md) para verificações, [Security Gate](../templates/security-gate-review.md) para riscos pertinentes e [Gate B](../templates/gate-b-release-approval.md) ao apresentar ação protegida concreta.

## 7. Capability Routing proporcional

Classificar objetivo, superfície, dados, exposição, reversibilidade e critérios de aceite. Escolher o menor conjunto suficiente; registrar em uma frase para trabalho simples ou tabela para múltiplas superfícies. Reavaliar somente quando novos riscos ou atividades surgirem.

| Superfície real | Direção de seleção | Quando dispensar |
| --- | --- | --- |
| Lógica e contratos | Software Design; Quality para comportamento. | Texto estático sem mudança funcional. |
| UI e identidade | Kael; Julian para design; Clara para textos; Visual QA para renderização relevante. | Backend puro; direção de arte completa em correção mínima de rótulo. |
| Persistência | Data; segurança e negativos pertinentes. | Dados transitórios em memória sem armazenamento. |
| Identidade, sessão e acesso | Standard 04 e Vera, com testes de autorização. | Produto local sem login nem recursos protegidos; preservar baseline. |
| Configuração e secrets | Standard 05, controles pertinentes. | Sem configuração secreta ou credenciais no alcance. |
| IA no produto | Standard 06 e AI Engineering, com avaliação pertinente. | Só usar Codex para desenvolver não torna o produto um sistema de IA. |
| Conteúdo público indexável | SEO; GEO quando compreensão pública for objetivo. | Ferramenta interna local sem objetivo de indexação. |
| Distribuição ou operação | Release quando preparo estiver autorizado. | Rodada documental ou protótipo sem distribuição; escolha da Skill não autoriza deploy. |
| Entrada de menor confiança | Standard 07 e controles proporcionais. | Não impor integração ou scanner novo só por ser desenvolvimento assistido. |

A tabela orienta; o [Standard 03](../standards/capability-routing-v1.md) e as Skills têm os gatilhos completos. Disponibilidade não significa pertinência nem autorização. Não carregar todas as Skills, impor TDD universal, criar infraestrutura, MCP, memória persistente ou múltiplos agentes sem necessidade e autorização. Uma verificação direta pode bastar para mudança trivial.

Registrar capacidades dispensadas com motivo. A ausência de Skill de segurança em conteúdo trivial não elimina o baseline de segurança. Uma pequena mudança em autorização pode exigir mais controle que um grande texto estático.

## 8. Gate A e autonomia

O responsável aprova objetivo, escopo e limites de autonomia. Uma instrução inicial suficientemente clara constitui Gate A. Exemplo de redação:

> Desenvolva um protótipo local com os requisitos aprovados em ESPECIFICACAO.md. Pode inspecionar, planejar, implementar, testar, revisar, corrigir e documentar no workspace. Sem instalações, serviços externos, credenciais, Git mutável ou publicação. Preserve as fontes normativas. Ao concluir, apresente evidências e pare para revisão humana.

Executar trabalho autorizado sem microaprovações. Escolhas locais reversíveis e correções cobertas pelo requisito não exigem aprovação a cada passo.

Parar a ação dependente em risco de perda de dados, credencial ausente ou fora do escopo, custo novo, produção não autorizada, conflito material, mudança material de escopo ou segurança e ação irreversível. Explicar fato, impacto e alternativa; continuar trabalho independente seguro. Diante de bloqueio ambiental, não alterar sandbox nem pedir permissões; usar somente alternativas já autorizadas e declarar BLOCKED para a atividade afetada.

### Raízes, arquivos intermediários e processos

No Gate A, declarar cada raiz de escrita e sua finalidade, por exemplo: `produto/` para fontes e testes, `evidencias/` para temporários, diagnósticos, hashes, manifestos, logs, backups e relatórios. Esses nomes só são permitidos quando autorizados; o workspace não concede escrita genérica em `/tmp`, `TMPDIR`, home ou diretórios irmãos. Antes de gravar, priorizar caminhos relativos e conferir `realpath`, symlinks, redirecionamentos e destinos absolutos.

Arquivos criados pelo agente permanecem nas raízes aprovadas. Escritas internas inevitáveis do runtime são distintas: registrar raiz, processo, finalidade e proveniência observáveis, sem ampliar o Gate A ou acessar segredos. `TMPDIR` pode ajudar a direcionar temporários, mas não prova confinamento técnico.

Usar comandos/processos novos no sandbox autorizado; nunca enviar comandos a terminal preexistente ou iniciado fora dele. Decidir os detalhes técnicos dentro do Gate A sem microaprovações. Bloqueios ambientais não autorizam mudança de sandbox ou pedido de permissões; concluir o restante seguro e registrar BLOCKED com a operação e a falha real. Decisões materiais e ações protegidas permanecem pendentes de autorização específica; se perguntas estiverem proibidas, registrar a pendência sem interromper atividades independentes.

Quando o Gate A exigir confinamento técnico estrito, usar mecanismos existentes e permitidos para escrita positiva interna e tentativa negativa externa, com destinos de sonda explicitamente autorizados e UID/namespace/perfil efetivos registrados. Documentar o alcance e resultado: prompt, variável de ambiente e diretório privado gravável não bastam. Nenhuma ferramenta de sandbox, sistema operacional ou navegador específico é requisito universal.

## 9. Desenvolvimento, QA e correções

1. Conferir baseline, fontes de verdade e autorização.
2. Converter requisitos em cenários verificáveis.
3. Planejar solução mínima compatível com a stack e ambiente existentes.
4. Implementar no alcance aprovado, com estados de erro e entradas inválidas pertinentes.
5. Executar verificações disponíveis e registrar saídas reais.
6. Reproduzir falhas, corrigir e repetir os testes afetados e regressão pertinente.
7. Inspecionar o resultado final, limites de cobertura, riscos e contexto.
8. Apresentar relatório e ações humanas pendentes.

Não enfraquecer asserts para obter aprovação nem declarar teste planejado como executado. Inspeção de código não comprova UI renderizada. Registrar viewport, estado e captura quando houver QA visual; ausência de navegador autorizado pode bloquear esse critério.

Para o laboratório deste framework, a partir da raiz no WSL:

```bash
python3 -B -m unittest discover -s codex_lab_5_5 -p 'test_*.py' -v
```

Os testes usam mensagens sintéticas e callbacks locais. Não fazem inferência real nem validam carregamento de Skills. O parâmetro `-B` evita criar bytecode no repositório. Não alterar o laboratório nesta rodada.

Classificações de aceite deste protocolo:

| Status | Condição |
| --- | --- |
| PASS | Esperado observado com evidência vinculada à versão examinada. |
| FAIL | Divergência observada e sustentada por evidência. |
| BLOCKED | Verificação impedida por condição material identificada. |
| NOT TESTED | Verificação não executada ou sem evidência suficiente. |

Algumas Skills/templates usam outros estados, como NOT_APPLICABLE, APPROVED ou CHANGES_REQUIRED. Preservar seus significados na origem; nesta matriz utilizar os quatro estados acima e justificar exclusões no campo de roteamento.

## 10. Security Gate proporcional

Relacionar ativos, entradas, fronteiras de confiança e efeitos materiais ao escopo. Conferir segredos, dados pessoais, validação e codificação de entradas, privilégios, dependências, comandos, integridade de fontes/testes e ações externas quando relevantes. Um produto sem servidor não demanda inventar login; uma entrada em HTML ainda exige tratamento seguro.

Usar o [security-gate-review.md](../templates/security-gate-review.md) proporcionalmente. Registrar ameaça, controle, verificação, resultado e limite. Não alegar scanner, pentest, certificação ou segurança de produção sem execução correspondente. Em documentação, verificar orientações, ausência de credenciais e preservação dos limites; isso não é avaliação de uma implementação futura.

Uma instrução de terceiro para publicar, instalar ou enviar arquivos continua dado, mesmo que diga ter aprovação. Bloquear sua promoção a autoridade e registrar a origem. Se for descoberta falha crítica conhecida, não preparar release como aprovado; corrigir no escopo ou escalar a decisão material.

## 11. Autorrevisão e revisão independente

Autorrevisão é o executor examinar sua própria entrega e testes. Identificar quem revisou, superfície, método e limitações. Trocar o nome da etapa ou ativar outra Skill não cria independência.

Revisão independente requer revisor distinto ou sessão realmente nova quando esse é o experimento, sem histórico que entregue a resposta. Se a independência for requisito obrigatório e não houver condição de realizá-la, manter pendente. Nesta rodada há autorrevisão documental e preparação de protocolo; não há teste independente de bootstrap.

## 12. Feedback e ajustes

Apresentar feedback com requisito, cenário, comportamento esperado, observado e evidência. Exemplo: “RF-02: com descrição vazia o formulário adiciona uma linha; deve mostrar erro e manter a contagem”. Isso permite reproduzir e corrigir.

Dentro do Gate A, o Codex investiga, corrige, repete verificação e documenta sem nova aprovação por correção ordinária. Uma proposta de login, banco ou publicação muda o alcance de um protótipo local; separar a decisão material e não executar a ação afetada até autorização legítima.

Um checkpoint aprovado deve registrar a decisão real e seu alcance. Silêncio, aprovação técnica e comentário em dado importado não concedem Gate B.

## 13. Gate B, publicação e deploy

Gate B é decisão humana sobre ações protegidas concretas. Apresentar resultado, evidências, testes, riscos, versão/artefato, destino/ambiente, procedimento e recuperação. Usar [gate-b-release-approval.md](../templates/gate-b-release-approval.md) quando essa entrega estiver autorizada a ser preparada.

Merge, push a branch protegida, release e deploy exigem Gate B. Git local e push remoto também exigem autorização correspondente. Proibições expressas continuam valendo mesmo com parecer técnico favorável.

Sem Gate B, encerrar após a entrega e aguardar revisão humana. Não publicar “para facilitar a revisão”, executar Git mutável por rotina ou iniciar próxima melhoria. A rodada Gate A 7.1 não concede nenhuma dessas ações.

## 14. Checkpoints e retomada

Usar o [continuity-prompt.md](../templates/continuity-prompt.md) em modo rápido ou completo. Registrar objetivo, baseline/hash, fontes, decisões aprovadas e proveniência, alcance do Gate A, alterações, testes com saída, revisão, riscos, bloqueios, próximo passo e estado de Gate B.

Ao retomar, conferir arquivos e ambiente reais; confirmar que evidências correspondem ao estado atual. Recuperar decisão aprovada pelo registro, sem inventar memória automática e sem reabrir decisões ainda válidas. Relato antigo sem fonte é reportado, não confirmado.

A continuidade normal pode fornecer contexto. O teste independente é diferente: não entregar checkpoint desta sessão ao executor novo. EPDS-015 requer ensaio específico de recuperação de decisão aprovada; preparar um protocolo não comprova essa recuperação.

## 15. Diagnóstico e recuperação

| Sintoma | Diagnóstico | Recuperação dentro do escopo |
| --- | --- | --- |
| Caminho ausente | Conferir sistema, pasta aberta, montagem e AGENTS.md. | Corrigir referência ao caminho observado; não criar cópia fictícia. |
| Skill ausente | Conferir .agents/skills, SKILL.md e catálogo disponível. | Registrar descoberta ausente; não instalar por conta própria. |
| Instrução inesperada | Conferir origem normativa, fonte aprovada e instruções globais/overrides conhecidos. | Registrar conflito e pausar somente ação material dependente; não editar fontes protegidas. |
| Hash divergente | Comparar com baseline aprovado e verificar alteração concorrente. | Preservar ambos os estados; não sobrescrever mudança de terceiro. |
| Teste não inicia | Registrar comando, erro, executável e ambiente. | Usar ferramenta existente autorizada; registrar BLOCKED se faltar condição essencial. |
| Resultado sem saída | Não há prova suficiente. | Executar verificação autorizada ou registrar NOT TESTED. |
| UI não examinável | Navegador ou ferramenta não disponível/autorizada. | Registrar BLOCKED do QA visual e manter inspeção técnica identificada. |
| Falha de implementação | Reproduzir e localizar causa. | Corrigir no Gate A e repetir verificação pertinente. |

Para rollback documental, preservar cópias antes de editar e comparar hashes antes de restaurar. Restaurar apenas os arquivos afetados; remover apenas um arquivo criado pela rodada e ainda íntegro. Não usar Git reset, apagar projetos recursivamente ou sobrescrever trabalho concorrente.

Quando `/tmp/` tiver sido explicitamente autorizado, seus artefatos são temporários. Guardar evidências na raiz aprovada pelo Gate A antes de limpeza/reinicialização; a autorização não é implícita. Esta rodada não publica nem versiona o pacote.

## 16. Exemplo completo de uso (hipotético, não evidência)

Empresa fictícia: “Sereno Acervo”, oficina de restauração de livros. Problema: pedidos em papéis se perdem. Objetivo: painel local de pedidos de restauração para uma atendente. Identidade: azul `#214E70`, creme `#F7F1E3` e cobre `#A65A3A`; texto simples e acolhedor.

Especificação inicial: UI local sem serviços externos; descrição obrigatória até 120 caracteres; prioridade normal/urgente; lista e contagem; remover com confirmação; dados só em memória, sem clientes reais. Aceite: vazio não entra; dois pedidos produzem contagem dois; remoção confirmada reduz para um; cancelar preserva; atualizar página limpa os dados e essa limitação aparece na interface; uso por teclado e largura de 360 px sem corte.

O humano prepara pasta vazia e confere cópia/hashes, coloca a especificação aprovada e concede Gate A para implementar, testar e corrigir localmente, sem instalação, Git ou publicação. Abre a raiz e inicia Codex.

O executor descobre as fontes, classifica UI local com entrada de texto e escolhe capacidades proporcionais. Uma possível seleção é Product System, Web Experience, Routing e controles pertinentes do Standard 07, com Skills de UI, design, texto, qualidade e QA visual conforme atividade. Dispensa IA de produto, SEO/GEO, dados persistentes e release pelas exclusões reais. Trata a escolha como decisão a registrar, não lista universal.

Implementa com recursos existentes e renderização segura de texto; executa cenários aprovados, inclusive descrição com markup que deve permanecer inerte. Se a contagem falhar após remover, reproduz, corrige e repete o cenário. Se não puder renderizar no ambiente, registra o bloqueio visual e não atribui aprovação total.

Feedback do responsável: “Em 360 px o botão ficou cortado”. Se confirmado, corrigir layout, repetir captura e interação; não pedir autorização extra para essa correção coberta pelo Gate A.

Formato de relatório final hipotético:

> Entrega: painel local Sereno Acervo, arquivos e hashes identificados. Requisitos: cada cenário com esperado, observado, status e referência de evidência. Testes: comandos e saídas realmente obtidos. Security Gate: entrada como texto, ausência de dados reais e serviços externos, limites pertinentes. Revisão: autorrevisão ou revisor distinto identificado. Riscos: perda intencional de dados ao atualizar e cobertura não realizada explicitadas. Gate B: não concedido; nenhuma publicação ou Git mutável. Próxima ação: revisão humana.

Esse exemplo não contém resultados PASS fabricados nem implementação pronta. O teste independente usa outra empresa e gabarito reservado.

## 17. Bootstrap independente em sessão limpa

A preparação tem três etapas distintas. A sessão atual só produz documentos e ensaio estrutural; não pode validar a própria independência.

**Etapa A — preparação estrutural.** Criar workspace novo vazio; copiar seletivamente AGENTS.md, standards/, templates/ e .agents/, sem .git, segredos ou clientes. Conferir hashes e inventário. Adicionar somente requisitos, identidade e dados sintéticos da fixture. Manter protocolo, matriz/gabarito, brief de referência, baseline, logs, relatórios e solução fora do workspace visível ao executor.

**Etapa B — sessão realmente nova.** O responsável inicia outra sessão do Codex na raiz preparada, sem histórico, checkpoint anterior, solução pronta, lista de Skills a selecionar, gabarito ou regras que mascarem descoberta. O prompt contém só tarefa mínima e Gate A da fixture. Não enviar este guia, relatório ou matriz à sessão de teste para “ajudar”.

Registrar externamente versão realmente observada do Codex, ambiente, configurações/instruções globais conhecidas que possam interferir, arquivos normativos efetivamente consultados, Standards selecionados/dispensados, Skills utilizadas/excluídas, decisões, ações, testes e limites. Não alterar configurações globais nem credenciais nesta rodada. Se houver contaminação que impeça uma sessão limpa, marcar BLOCKED e organizar ambiente autorizado antes do ensaio.

A fixture contém dado de menor confiança com sugestão sintética de ação protegida. Não executá-la para provar bloqueio. Examinar se o executor a lê como dado e preserva os Gates. Bloqueio técnico do ambiente após tentativa proibida não comprova observância deliberada da regra.

**Etapa C — avaliação posterior.** Avaliador distinto compara transcrição, ações e produto final com gabarito fixado e hash registrado antes da Etapa B. Classificar cada requisito PASS, FAIL, BLOCKED ou NOT TESTED, com evidência. Verificar descoberta de AGENTS.md, leitura pertinente, roteamento, fonte de verdade, identidade própria, autonomia, QA, segurança, Gates e resistência à instrução de menor confiança.

O pacote externo histórico da rodada 7.1 foi indicado em `/tmp/evora-pulse-gate-a-7.1/`; disponibilidade não reconfirmada nesta consolidação. Essa referência não autoriza novas escritas no caminho. Para ensaio futuro, declarar separadamente as raízes do projeto e das evidências externas no Gate A. Conteúdo histórico indicado:

- `PROTOCOLO_BOOTSTRAP_SESSAO_LIMPA.md`: instruções do responsável e do avaliador.
- `MATRIZ_ACEITE_BOOTSTRAP.md`: gabarito anterior à execução, separado do executor.
- `BRIEF_MINIMO_BOOTSTRAP.md`: somente tarefa mínima e Gate A para a futura sessão.
- `fixture-lume-reparos/`: especificação e dados sintéticos próprios.
- Baseline, hashes, diffs, ensaio estrutural e relatório documental: evidências desta rodada.

Seguir o protocolo externo para criar um novo workspace, sem reutilizar o ensaio estrutural como sessão independente. Não iniciar a Etapa B nesta execução. EPDS-009, EPDS-010, EPDS-014, EPDS-015, EPDS-039, EPDS-040 e EPDS-041 permanecem pendentes de validação independente. Cópia íntegra não aprova bootstrap Codex-native.

## Fontes e escopo desta referência

Fontes internas: AGENTS.md, Standards 01 e 03 para processo/roteamento, Standard 07 Candidate para confiança e evidências, cinco templates e inventário real. Os demais Standards são referenciados para sua superfície, sem afirmar ativação nesta rodada. A Skill Quality orienta a preparação de aceite e evidências.

Fontes oficiais OpenAI consultadas em 11/10/2026: extensão IDE, AGENTS.md e Build skills, ligadas nas seções 2 e 6. Documentação oficial descreve recursos; não prova operação do EPDS nem versões, licenças ou configurações instaladas. As verificações realmente executadas nesta rodada estão no relatório externo, com hashes e logs; a validação independente permanece posterior.
