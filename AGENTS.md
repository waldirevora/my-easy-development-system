# AGENTS.md

## Objetivo

Este repositório contém o Évora Pulse Development System.

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

Interromper apenas por blocker material e solicitar nova decisão humana quando houver:
- destruição ou migration com risco de perda de dados;
- credencial ausente ou uso de credenciais reais fora do escopo;
- custo novo;
- acesso a produção não autorizado;
- conflito material de requisitos ou com decisão aprovada;
- mudança material de escopo;
- mudança relevante de segurança;
- ação irreversível.

Gate B humano:
- apresentar resultado;
- evidências;
- testes;
- riscos residuais;
- aguardar autorização humana para merge, push a branch protegida, release ou deploy.

## Routing

Consultar:
- `standards/`: aplicar apenas standards existentes e pertinentes;
- `.agents/skills/`: diretório canônico das Skills descobertas pelo Codex.

`skills/` é legado/documental, não o diretório runtime das Skills.

Não carregar todas as capacidades por padrão.
