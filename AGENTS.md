# AGENTS.md

## Objetivo

Este repositório contém o My Easy Development System.

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
