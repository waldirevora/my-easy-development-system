# My Easy Development System

O **My Easy Development System (MEDS)** é uma camada de instruções versionadas para desenvolver software com Codex. Reúne Skills, padrões de engenharia e limites de autorização para ajudar desenvolvedores e equipes a definir tarefas, escolher verificações e entregar evidências do trabalho.

É um harness de instruções, não um aplicativo com servidor próprio ou um instalador automático de agentes. Seus arquivos orientam o Codex; não comprovam autonomia irrestrita, segurança de produção ou execução correta de qualquer projeto. O nome recomendado da pasta é `my-easy-development-system`, mas a localização e o nome físico não são requisitos de funcionamento.

## Pré-requisitos

- **Para clonar:** Git e acesso autorizado ao repositório GitHub, que atualmente é **privado**. Autenticação do GitHub e autenticação do Codex são independentes.
- **Para usar as instruções:** Codex CLI ou extensão Codex compatível, já instalada e autenticada conforme a [documentação oficial](https://learn.chatgpt.com/docs/codex/cli). VS Code é opcional para o fluxo CLI e necessário para o fluxo pela extensão.
- **Para verificar ou copiar automaticamente:** Python 3 já disponível. Ele é usado pelo validador, laboratório e script de cópia; não é necessário apenas para ler as instruções.

Nesta revisão foram observados Linux, Bash, Python 3.12.3 e `codex-cli 0.162.1`. Essas são versões testadas, não versões mínimas prometidas. Confira o executável Python do seu ambiente antes de usar os exemplos; os comandos PowerShell abaixo usam `python` quando ele corresponde ao Python 3 disponível.

## Instalação rápida

Abra o terminal no **diretório pai escolhido por você**, com permissão normal de acesso. Não existe unidade, montagem WSL ou pasta de instalação obrigatória. Os comandos criam uma nova pasta; se ela já existir, confira seu conteúdo e escolha outro destino, sem sobrescrever.

Bash, inclusive WSL:

```bash
git clone https://github.com/waldirevora/my-easy-development-system.git
cd my-easy-development-system
codex --version
codex login status
codex --sandbox read-only --cd .
```

PowerShell:

```powershell
git clone https://github.com/waldirevora/my-easy-development-system.git
cd .\my-easy-development-system
codex --version
codex login status
codex --sandbox read-only --cd .
```

Execute a sequência passo a passo e prossiga somente se a etapa anterior terminar com sucesso. Não execute login, instalação ou mudança de permissões como parte de uma tarefa que não os autorize. Para usar VS Code, abra **a pasta clonada**, não seu diretório pai, e inicie a extensão Codex nela. `code .` é uma alternativa somente se o comando já estiver disponível.

O modo `read-only` limita o primeiro diagnóstico. Para desenvolvimento posterior, use a configuração de permissões autorizada para o projeto e conceda um Gate A com objetivo, arquivos e ações permitidas.

## Primeiro uso e teste rápido

Na nova sessão do Codex, abra `/skills` ou digite `$` e procure `quality-engineering-testing`. A lista pode incluir Skills globais além das 12 locais. Confira se o caminho corresponde a `.agents/skills/quality-engineering-testing/SKILL.md` desta instalação. A [documentação de Skills](https://learn.chatgpt.com/docs/build-skills) explica o seletor e a ativação por descrição.

Cole esta tarefa no Codex, como texto, sem executá-la no shell:

```text
Use $quality-engineering-testing para diagnosticar codex_lab_5_5/ai_triage.py.
Gate A: somente leitura de fontes locais e testes Python existentes com -B.
Não editar arquivos, instalar, acessar credenciais, usar serviços externos ou fazer Git mutável.
Identifique as instruções aplicáveis de AGENTS.md e a Skill usada antes do diagnóstico.
Execute os testes pertinentes e informe comando, contagem real, resultado e limites.
Se houver bloqueio, registre BLOCKED sem ampliar permissões.
```

O sucesso esperado inclui referência às regras reais de `AGENTS.md`, leitura do `SKILL.md` pertinente e execução dos 24 testes do laboratório, com resultado observado. Confira as chamadas de ferramentas da sessão: a leitura da Skill deve preceder a aplicação de seu procedimento. Uma listagem de arquivos ou a frase “usei a Skill” não prova sua invocação. A [descoberta de AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) pode sofrer influência de instruções globais e overrides; este teste verifica somente a sessão observada.

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

`meu-projeto` é um nome ilustrativo; use somente o destino autorizado. O [script de cópia](scripts/copy_harness.py) descobre sua origem pelo próprio arquivo, funciona sem `.git` e prepara 28 arquivos: `AGENTS.md`, 7 Standards e seu índice, 12 Skills, 5 templates e seu índice, mais `MEDS-LICENSE`. O objetivo do AGENTS copiado é adaptado ao projeto; as regras de autonomia, escrita e bloqueios são preservadas. `MEDS-LICENSE` licencia somente as fontes MEDS copiadas, sem definir a licença do seu produto.

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
```

O frontmatter `name` identifica cada Skill; `description` informa quando ela é pertinente. O Codex pode selecioná-la pela tarefa ou por menção explícita. O [Capability Routing](standards/capability-routing-v1.md) orienta a escolha pelo propósito, superfície e risco. Standards e templates são consultados quando necessários. As 12 Skills são instruções especializadas, não 12 subagentes simultâneos. [Consulte seus arquivos](.agents/skills/).

## Validação local

Na raiz, em Bash:

```bash
python3 -B scripts/check.py
python3 -B -m unittest discover -s codex_lab_5_5 -p 'test_*.py' -v
```

Em PowerShell, use `python -B .\scripts\check.py`. O verificador executa o laboratório e a regressão da cópia, além de conferir estrutura 7/12/5, sintaxe Python, frontmatter, cercas Markdown e destinos de links internos. Esperam-se verificações estáticas PASS e zero falhas nos testes. `-B` evita caches de bytecode. URLs externas, âncoras Markdown, descoberta Codex e desenvolvimento de um produto real não são comprovados por esse comando.

De `docs/`, a chamada Bash é `python3 -B ../scripts/check.py`; em PowerShell, `python -B ..\scripts\check.py`. Também é possível chamar o script por seu caminho absoluto real, entre aspas: ele descobre a raiz pelo próprio arquivo, independentemente do cwd. Links internos são relativos. No WSL, use a montagem real da pasta escolhida. Espaços, acentos e mudança do nome da instalação foram testados em cópias Linux; Windows e macOS nativos permanecem sem validação de execução nesta revisão.

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

As fontes MEDS usam [Apache License, Version 2.0](LICENSE), SPDX `Apache-2.0`. As atribuições externas dos Standards permanecem vinculadas às suas fontes; esta licença não relicencia documentos externos citados. Não foram identificados avisos incompatíveis ou atribuições que exijam NOTICE na árvore atual.

O repositório permanece privado. Quem tiver acesso pode propor uma alteração com problema reproduzível, escopo e evidências de teste; a aceitação exige revisão e autorização humana correspondente. Uma disponibilização pública futura é decisão separada: o histórico Git preserva mensagens e metadados anteriores ao rebranding.

Os resultados históricos e as ressalvas de bootstrap estão no [guia](docs/GUIA_DE_USO.md), incluindo o FAIL histórico 7.3-R. MEDS não tem interface web própria; QA browser de pilotos antigos permanece pendente e não é requisito da instalação documental. Preparação de arquivos, teste da cópia e testes Python não equivalem a desenvolvimento ponta a ponta comprovado.
