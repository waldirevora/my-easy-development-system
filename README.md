# Évora Pulse Development System

Framework interno para orientar desenvolvimento com VS Code, Codex nativo, Product System, Standards e Skills Évora Pulse. Reúne instruções versionáveis, roteamento por propósito e risco, execução autônoma com Gate A e Gate B, segurança proporcional e evidências de qualidade.

## Comece por aqui

1. Confira o ambiente já disponível: Windows ou WSL, VS Code e acesso autorizado ao Codex. Use um terminal coerente com a pasta aberta; confirme o diretório antes de agir. Este repositório não instala essas ferramentas.
2. Localize o framework e leia [AGENTS.md](AGENTS.md). Nesta máquina, o caminho Windows é `D:\OneDrive\##Pro-Studio\## evora-pulse-development-system`; no WSL, `/mnt/d/OneDrive/##Pro-Studio/## evora-pulse-development-system`. Em outra máquina, use o caminho realmente observado.
3. Prepare um projeto novo em uma pasta vazia, fora do framework, copiando seletivamente `AGENTS.md`, `standards/`, `templates/` e `.agents/`. Não copie `.git/`, credenciais, segredos ou dados de clientes. Confira hashes dos arquivos. O [guia operacional](docs/GUIA_DE_USO.md) contém um procedimento reproduzível.
4. Descreva o problema, público, requisitos, critérios de aceite e restrições. Aprove objetivo, escopo e limites no Gate A, usando uma instrução suficiente ou o [brief de Gate A](templates/gate-a-task-brief.md).
5. Abra a raiz do novo projeto no VS Code e inicie uma nova conversa no Codex. Trabalhe dentro do Gate A; apresente resultado, testes, revisão e riscos antes de qualquer ação protegida.

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

Estado consolidado: **encerrado com ressalvas, pronto para uso interno**. A governança de escrita foi incorporada, com Product System 4.1, 24 testes Python e 18 verificações documentais aprovados na consolidação. QA em navegador real permanece **BLOCKED**; Habblaud é integração opcional pendente. Bootstrap 7.2 e retomada 7.4 conservam **PASS limitado histórico**; o **FAIL histórico 7.3-R permanece preservado**. Os relatos de rodadas anteriores acima são históricos. Os artefatos dessas auditorias foram removidos da árvore operacional por decisão do responsável; seus resultados permanecem registrados como históricos. Publicar este código-fonte não concede Gate B, deploy ou homologação universal.

## Verificação local disponível

No WSL, a partir da raiz, com Python já disponível:

```bash
python3 -B -m unittest discover -s codex_lab_5_5 -p 'test_*.py' -v
```

Registre ambiente, comando, resultado e saída reais. No Windows, use o interpretador Python já existente e observado, sem presumir que `python` esteja instalado. Não instalar dependências apenas para produzir um parecer positivo.
