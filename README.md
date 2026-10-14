# My Easy Development System

O **My Easy Development System (MEDS)** é uma camada de instruções versionadas para desenvolver software com Codex. Reúne Skills, padrões de engenharia e limites de autorização para ajudar desenvolvedores e equipes a definir tarefas, escolher verificações e entregar evidências do trabalho.

É um harness de instruções, não um aplicativo com servidor próprio ou um instalador automático de agentes. Seus arquivos orientam o Codex; não comprovam autonomia irrestrita, segurança de produção ou execução correta de qualquer projeto. O nome recomendado da pasta é `my-easy-development-system`, mas a localização e o nome físico não são requisitos de funcionamento.

## Pré-requisitos

- **Para clonar:** Git e acesso autorizado ao repositório GitHub. Enquanto ele for privado, é necessária permissão do proprietário. Autenticação do GitHub e autenticação do Codex são independentes.
- **Para usar:** Codex Desktop ou Codex CLI disponível e autenticado; a extensão de IDE também pode ser usada. Se ainda não estiver instalado, siga a [documentação oficial](https://learn.chatgpt.com/docs/quickstart) antes dos passos abaixo. VS Code e WSL não são obrigatórios.
- **Para verificar ou copiar automaticamente:** Python 3 já disponível. Ele é usado pelo validador, laboratório e script de cópia; não é necessário apenas para ler as instruções.

Na revisão histórica foram observados Linux, Bash, Python 3.12.3 e `codex-cli 0.162.1`; não são versões mínimas prometidas. Confira o executável Python do seu ambiente; os exemplos PowerShell usam `python` quando ele corresponde ao Python 3 disponível.

## Início rápido: descreva seu projeto

Obtenha o repositório pelo GitHub com acesso autorizado (clone ou download e extração). Escolha uma pasta local; não há instalação global do MEDS nem necessidade de copiar Standards, templates ou as 12 Skills para cada projeto interno.

### Codex Desktop

1. Abra a pasta obtida do MEDS no Codex Desktop.
2. Inicie uma conversa **local**, com permissão de escrita para desenvolver o projeto.
3. Envie um pedido curto, por exemplo:

> Crie um site premium para um condomínio de luxo em Osasco, com imagens originais e formulário de contato.

4. O Codex deve criar `workspaces/site-condominio/`, desenvolver, testar e documentar ali. O nome pode receber um sufixo para preservar outra pasta existente.
5. Encontre a pasta informada na entrega, abra-a no editor ou no Codex e siga seu README para executar.

A interface pode variar por versão; consulte o [início rápido oficial](https://learn.chatgpt.com/docs/quickstart). Imagens, navegador e runtimes dependem das ferramentas realmente disponíveis e autorizadas. Lacunas e testes impedidos devem aparecer na entrega.

### Codex CLI

Se `codex` ainda não estiver disponível, instale e autentique conforme o [guia oficial do CLI](https://learn.chatgpt.com/docs/codex/cli). No terminal do diretório pai escolhido, com Git disponível e acesso ao repositório:

```sh
git clone https://github.com/waldirevora/my-easy-development-system.git
cd my-easy-development-system
codex
```

Os comandos funcionam em Bash ou PowerShell; execute passo a passo. Se já obteve o MEDS, apenas entre na pasta e execute `codex`. Envie o mesmo pedido na conversa, sem colá-lo como comando de shell. Use permissões autorizadas para escrita; uma sessão somente leitura permite diagnóstico, mas bloqueia criação de arquivos.

### Descoberta, escopo e Git

O Codex lê AGENTS da raiz do projeto até o diretório de trabalho, considerando instruções globais e overrides. Veja [AGENTS.md oficial](https://learn.chatgpt.com/docs/agent-configuration/agents-md). As Skills são descobertas em `.agents/skills/` nos ancestrais até a raiz do repositório; sua seleção usa nome e descrição. Veja [Skills oficiais](https://learn.chatgpt.com/docs/build-skills). Trabalhar dentro de `workspaces/` no checkout MEDS mantém essas fontes na cadeia ancestral. Em extração sem Git, comece pela raiz MEDS e confira o catálogo antes de retomar numa subpasta.

Desenvolvimento escreve somente no projeto escolhido e lê as instruções compartilhadas. Manutenção do framework precisa ser explicitamente solicitada. Essa regra de escopo não substitui o sandbox. O resultado inclui fontes, assets e instruções de execução do projeto; nenhum deploy é automático.

O Git do MEDS ignora todo o conteúdo de `workspaces/`, exceto `.gitkeep`, que mantém a pasta versionável. Projetos locais permanecem no disco, fora dos commits do MEDS. Ignorar não retira arquivos já versionados: registre o caso sem removê-los. Git próprio só deve ser criado quando você solicitar explicitamente; uma nova raiz Git pode mudar a descoberta ancestral, exigindo conferir instruções/Skills e preparar o projeto independente.

Um projeto externo não descobre uma pasta MEDS irmã. Para esse caso, use o procedimento abaixo; não há integração global automática. Veja o [guia](docs/GUIA_DE_USO.md) para retomada, QA e diagnóstico.


Para conferir a descoberta na sessão, abra `/skills` ou o seletor disponível e verifique se os caminhos apontam a `.agents/skills/` desta instalação. Catálogo disponível não prova execução: observe a leitura do SKILL.md antes do procedimento. A validação de uma nova sessão deve ser registrada separadamente dos testes Python.

## Usar em outro projeto

Clonar o MEDS não ativa sua governança num repositório arbitrário. Para um **projeto novo**, autorize uma pasta de destino ausente ou vazia, fora da instalação MEDS, cujo diretório pai já exista. A partir da raiz MEDS, em Bash:

```bash
python3 -B scripts/copy_harness.py "../meu-projeto"
cd "../meu-projeto"
codex --sandbox read-only --cd .
```

Em PowerShell:

```powershell
python -B .\scripts\copy_harness.py "..\meu-projeto"
cd "..\meu-projeto"
codex --sandbox read-only --cd .
```

`meu-projeto` é um nome ilustrativo; use somente o destino autorizado. O [script de cópia](scripts/copy_harness.py) descobre sua origem pelo próprio arquivo, funciona sem `.git` e prepara 28 arquivos: `AGENTS.md`, 7 Standards e seu índice, 12 Skills, 5 templates e seu índice, mais `MEDS-LICENSE`. O AGENTS copiado usa a raiz do projeto externo e remove o bloco específico da instalação MEDS, evitando criar workspaces recursivos; as regras de autonomia, escrita e bloqueios são preservadas. `MEDS-LICENSE` licencia somente as fontes MEDS copiadas, sem definir a licença do seu produto.

A sessão `read-only` acima serve para conferir as instruções e o catálogo. Para desenvolver depois dessa conferência, encerre-a e execute `codex` na raiz do destino, com escrita autorizada para o projeto. No Desktop, abra essa mesma raiz e confira as permissões da conversa local.

O script recusa destino ocupado, links simbólicos e fontes essenciais ausentes. Não copia Git, configurações privadas, caches ou laboratório. Depois, adicione os requisitos do produto e confira a descoberta em uma nova sessão na **raiz do destino**. A preparação de arquivos é verificável; o carregamento pelo Codex precisa de evidência própria. O [guia](docs/GUIA_DE_USO.md) detalha a árvore resultante, conflitos e limites do teste.

Para um projeto existente, não use essa cópia sobre seus arquivos: compare e integre as instruções numa alteração revisável, preservando AGENTS e Skills preexistentes. Esse procedimento manual precisa ser validado no projeto específico; não há instalação global ou integração automática com pastas irmãs.

## Estrutura e escolha de Skills

```text
AGENTS.md                    instruções locais e Gates
LICENSE                      Apache-2.0
standards/                   7 Standards e README
.agents/skills/               12 pastas com SKILL.md
templates/                   5 templates e README
docs/GUIA_DE_USO.md           guia operacional
examples/README.md           índice documental, sem aplicação pronta
scripts/                     verificador, cópia e testes da cópia
codex_lab_5_5/               função sintética e 24 testes
workspaces/.gitkeep          marcador; projetos locais ignorados pelo Git
```

O frontmatter `name` identifica cada Skill; `description` informa quando ela é pertinente. O Codex pode selecioná-la pela tarefa ou por menção explícita. O [Capability Routing](standards/capability-routing-v1.md) orienta a escolha pelo propósito, superfície e risco. Standards e templates são consultados quando necessários. As 12 Skills são instruções especializadas, não 12 subagentes simultâneos. Julian, Kael, Clara e Vera são nomes de especialidades; não há agentes autônomos separados configurados nas fontes versionadas. [Consulte seus arquivos](.agents/skills/).

## Validação local

Na raiz, em Bash:

```bash
python3 -B scripts/check.py
python3 -B -m unittest discover -s codex_lab_5_5 -p 'test_*.py' -v
```

Em PowerShell, use `python -B .\scripts\check.py`. O verificador executa o laboratório, a regressão da cópia e os testes de workspaces/Git, além de conferir estrutura 7/12/5, sintaxe Python, frontmatter, cercas Markdown e destinos de links internos. Testes Git são omitidos sem Git/checkout, com motivo explícito. Esperam-se verificações estáticas PASS e zero falhas nos testes. `-B` evita caches de bytecode. URLs externas, âncoras Markdown, descoberta Codex e desenvolvimento de um produto real não são comprovados por esse comando.

De `docs/`, a chamada Bash é `python3 -B ../scripts/check.py`; em PowerShell, `python -B ..\scripts\check.py`. Também é possível chamar o script por seu caminho absoluto real, entre aspas: ele descobre a raiz pelo próprio arquivo, independentemente do cwd. Links internos são relativos. No WSL, use a montagem real da pasta escolhida. Espaços, acentos e mudança do nome da instalação foram testados em cópias Linux; Windows e macOS nativos permanecem sem validação de execução nesta revisão.

## Direção criativa e linguagem

Interfaces novas e redesigns consideram três direções distintas antes da implementação, conforme o [Web Experience](standards/web-experience-business-systems-v1.md). A escolha é autônoma dentro do Gate A e precisa chegar às telas, não apenas ao relatório. Não existe paleta ou layout MEDS para projetos de clientes. O aceite visual exige renderização, inspeção crítica, correção e reinspeção; testes funcionais não comprovam originalidade.

A política única de linguagem está em [AGENTS.md](AGENTS.md). `scripts/check.py` verifica também os textos Markdown do framework. Para um projeto, execute `python -B scripts/check_language.py` seguido dos caminhos autorizados de HTML, Markdown, JS e CSS a verificar, a partir da raiz MEDS. O scanner separa prosa de sintaxe técnica nas superfícies suportadas; revisão editorial e exceções contextualizadas continuam necessárias. Não corrige textos automaticamente nem examina projetos por padrão.

O scanner é lexical, não uma análise completa de toda linguagem. Markdown inline técnico e cercas de código não textual são preservados; cercas de texto/Markdown continuam verificadas. HTML considera texto e atributos autorais; JS considera literais; CSS considera conteúdo gerado. Valores construídos dinamicamente e formatos não suportados exigem revisão específica. Exceção pontual de Markdown pode ser documentada na mesma linha com `<!-- meds-language-exception: motivo verificável -->`; não usar isso para omitir defeitos de redação.

## Autonomia e segurança

**Gate A** aprova objetivo, escopo, raízes de escrita e ações permitidas. Dentro dele, o Codex planeja, executa, testa, revisa e corrige sem microaprovações. Temporários também exigem uma raiz autorizada; o workspace não concede escrita genérica em outros diretórios.

**Gate B** é a autorização humana para merge, push protegido, release ou deploy. Operações Git, novas credenciais e gastos exigem autorização correspondente. Diante de bloqueio ambiental ou mudança material, registrar a operação afetada e continuar o restante autorizado; não ampliar sandbox nem contornar autenticação. As regras completas estão em [AGENTS.md](AGENTS.md) e no [guia](docs/GUIA_DE_USO.md).

## Diagnóstico rápido

| Sintoma | Verificação e próximo passo |
| --- | --- |
| `codex` não encontrado | Confira o ambiente escolhido e a documentação oficial; registre BLOCKED se instalação estiver fora do escopo. |
| Diretório errado | Use `pwd` ou `Get-Location`; confira AGENTS e `.agents/skills/`. Em checkout Git, `git rev-parse --show-toplevel` identifica a raiz. |
| Skills ausentes | Abra o seletor, confira os caminhos locais e reinicie uma sessão na raiz; não presuma descoberta por arquivos numa pasta irmã. |
| Python ausente | Confira o executável disponível; leitura e uso das instruções continuam possíveis, mas validação/cópia automática ficam BLOCKED. |
| Clone privado negado | Confirme acesso autorizado ao GitHub; não coloque tokens na URL ou em mensagens. |
| Rede/DNS indisponível | Registre a falha; uma cópia local existente ainda pode executar validações sem rede. |
| Escrita ou runtime bloqueado | Registre o comando e a restrição do host; não remova proteção para concluir o teste. |

## Licença, contribuição e limites de evidência

As fontes MEDS usam [Apache License, Version 2.0](LICENSE), SPDX `Apache-2.0`. Preserve a licença e os avisos de atribuição ao redistribuir, e identifique arquivos modificados. A cópia do harness conserva a licença em `MEDS-LICENSE` e identifica a adaptação do AGENTS. A licença do produto desenvolvido é uma decisão separada. As referências externas dos Standards permanecem vinculadas às suas fontes; esta licença não relicencia documentos externos citados.

O [OWASP ASVS](https://owasp.org/projects/asvs), citado nos Standards, declara CC BY-SA 4.0. Preserve as referências e confira os termos da fonte antes de incorporar ou adaptar seu conteúdo em uma redistribuição. Não foram encontrados componentes de terceiros incorporados que tragam obrigação identificada de um arquivo NOTICE; essa inspeção não comprova titularidade de direitos autorais.

Quem tiver acesso pode propor uma alteração com problema reproduzível, escopo e evidências de teste; a aceitação exige revisão e autorização humana correspondente. A disponibilização pública é decisão separada: o histórico Git preserva mensagens, identidade anterior e metadados de autoria. O proprietário precisa avaliar essa exposição antes de publicar.

Os resultados históricos e as ressalvas de bootstrap estão no [guia](docs/GUIA_DE_USO.md), incluindo o FAIL histórico 7.3-R. MEDS não tem interface web própria; QA browser de pilotos antigos permanece pendente e não é requisito da instalação documental. Preparação de arquivos, teste da cópia e testes Python não equivalem a desenvolvimento ponta a ponta comprovado.

A [revisão final para publicação](docs/REVISAO_PUBLICACAO.md) registra o inventário, os ajustes, o alcance da inspeção de segurança e histórico, os testes locais e as decisões pendentes. Sua autorrevisão técnica não autoriza mudar visibilidade, executar Git mutável ou publicar.
