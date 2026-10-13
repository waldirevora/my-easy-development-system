# My Easy Development System

Framework para orientar desenvolvimento com VS Code, Codex nativo, Product System, Standards e Skills. Reúne instruções versionáveis, roteamento por propósito e risco, execução autônoma com Gate A e Gate B, segurança proporcional e evidências de qualidade. A sigla técnica **MEDS** significa **My Easy Development System**; o slug e nome recomendado da pasta são `my-easy-development-system`.

## Comece por aqui

Não existe diretório de instalação obrigatório. Escolha qualquer pasta com as permissões normais de acesso, no Windows, WSL, Linux ou macOS. Este repositório não instala Git, Python, VS Code ou Codex.

1. Abra um terminal no diretório **pai escolhido por você**.
2. Clone o repositório existente com Git já disponível:

   ```bash
   git clone https://github.com/waldirevora/my-easy-development-system.git
   ```

3. Entre na pasta criada, relativamente ao diretório pai. Em Bash:

   ```bash
   cd my-easy-development-system
   ```

   Em PowerShell:

   ```powershell
   cd .\my-easy-development-system
   ```

4. Abra essa pasta no VS Code/Codex e leia [AGENTS.md](AGENTS.md). A descoberta das instruções e de [.agents/skills/](.agents/skills/) depende da configuração efetiva do Codex; confira o catálogo e as instruções carregadas.
5. Para trabalhar **no MEDS**, use seus arquivos locais. Para usar sua governança **em outro repositório**, copie seletivamente `AGENTS.md`, `LICENSE`, `standards/`, `templates/` e `.agents/skills/` para uma raiz de projeto autorizada, seguindo o [guia operacional](docs/GUIA_DE_USO.md). Uma pasta irmã arbitrária não é fonte automática de Skills. Não copie `.git/`, credenciais, caches ou dados de clientes.
6. Descreva problema, requisitos, aceite e limites no Gate A, usando uma instrução suficiente ou o [brief](templates/gate-a-task-brief.md). Trabalhe no escopo aprovado e apresente evidências antes de ações protegidas.

Os comandos abaixo são relativos à raiz validada. O [verificador](scripts/check.py) descobre a raiz pela localização do próprio arquivo, usando `AGENTS.md` e `.agents/skills/` como marcadores; não depende do nome físico da pasta ou do diretório de execução. No WSL, a montagem de uma pasta Windows depende da unidade e configuração locais: use a localização real escolhida por você.

Consulte o [guia completo](docs/GUIA_DE_USO.md) para implementação, QA, Security Gate, feedback, checkpoints, recuperação e teste de bootstrap em sessão limpa.

## Fontes e estrutura

| Fonte | Papel |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Instruções do workspace e limites de autonomia. |
| [standards/](standards/README.md) | 7 Standards: 5 Stable e 2 Candidate, conforme seus próprios cabeçalhos. |
| [.agents/skills/](.agents/skills/) | 12 Skills canônicas, cada uma com `SKILL.md`. Consultar apenas as pertinentes. |
| [templates/](templates/README.md) | 5 modelos de brief, QA, segurança, aprovação e continuidade. |
| [docs/](docs/README.md) | Guia operacional e limites da validação. |
| [codex_lab_5_5/](codex_lab_5_5/) | Laboratório Python com testes locais determinísticos; não comprova integração com Codex. |

## Governança e limites

O Gate A pode ser concedido pela instrução inicial suficientemente clara. Dentro dele, planejar, implementar, testar, corrigir, revisar e documentar sem microaprovações. Parar a ação dependente diante de mudança material, custo novo, credencial fora do alcance, produção não autorizada, risco de perda de dados ou ação irreversível.

Gate B humano é necessário para merge, push a branch protegida, release ou deploy. Git local e outros pushes também exigem autorização correspondente; proibições explícitas prevalecem. Aprovação técnica não autoriza publicação.

Os documentos descrevem o comportamento esperado. Presença de arquivos, estado Stable, cópia seletiva e testes do laboratório não demonstram descoberta, roteamento ou uso efetivo de Skills pelo Codex. O bootstrap independente exige uma sessão nova sem histórico anterior e avaliação por evidências; esta rodada documental apenas prepara seu protocolo. Os seis marcos estruturalmente concluídos conservam suas ressalvas.

A auditoria anterior de 11/10/2026 reportou 28 PASS limitados, 3 FAIL documentais, 3 BLOCKED e 10 NOT TESTED. Esses números não representam uma porcentagem de conformidade operacional. A correção de onboarding, guia e identificação do legado não aprova integralmente o framework.

Estado consolidado: **encerrado com ressalvas, pronto para uso interno**. A governança de escrita foi incorporada, com Product System 4.1, 24 testes Python e 18 verificações documentais aprovados na consolidação. QA em navegador real permanece **BLOCKED**; a integração externa opcional permanece pendente. Bootstrap 7.2 e retomada 7.4 conservam **PASS limitado histórico**; o **FAIL histórico 7.3-R permanece preservado**. Os relatos de rodadas anteriores acima são históricos. Os artefatos dessas auditorias foram removidos da árvore operacional por decisão do responsável; seus resultados permanecem registrados como históricos. Publicar este código-fonte não concede Gate B, deploy ou homologação universal.

## Verificação local disponível

Em Bash, a partir da raiz, com Python 3 já disponível:

```bash
python3 -B -m unittest discover -s codex_lab_5_5 -p 'test_*.py' -v
python3 -B scripts/check.py
```

O verificador confere o inventário 7/12/5, sintaxe Python, frontmatter das Skills, cercas de código Markdown e destinos dos links internos; depois executa a suíte existente. Não verifica URLs externas ou renderização de UI. Em PowerShell, se `python` for o interpretador Python 3 observado, use `python -B .\scripts\check.py`; adapte apenas o executável ao ambiente disponível.

Registre ambiente, comando, resultado e saída reais. Não instalar dependências apenas para produzir um parecer positivo. Para executar desde um subdiretório, ajuste somente o caminho relativo até o script, por exemplo `python3 -B ../scripts/check.py` em `docs/`.

## Licença e histórico

Este projeto é disponibilizado sob a **Apache License, Version 2.0**, SPDX **Apache-2.0**. O texto integral está em [LICENSE](LICENSE), copiado sem alterações da licença Apache-2.0 distribuída pelo pacote `base-files` do sistema e conferido com a [fonte oficial Apache](https://www.apache.org/licenses/LICENSE-2.0). As referências externas dos Standards continuam atribuídas às suas fontes; a licença deste repositório não relicencia os documentos externos citados. A inspeção dos arquivos atuais não identificou avisos incompatíveis ou material incorporado que exija `NOTICE`.

O rebranding atualiza a árvore atual. Mensagens, identidades anteriores e metadados de autoria permanecem no histórico Git preservado. A adoção da licença não altera a visibilidade do repositório; uma futura publicação pública exige decisão separada e revisão do histórico.
