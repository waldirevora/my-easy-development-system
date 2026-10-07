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

Gate A:
- objetivo;
- escopo;
- autonomia.

Entre Gate A e Gate B:
- planejar;
- implementar;
- testar;
- revisar;
- corrigir;
- executar QA e Security Gate quando aplicável;
- atualizar documentação.

Interromper apenas por blocker material:
- perda de dados;
- migration destrutiva;
- credencial ausente;
- custo novo;
- acesso a produção não autorizado;
- conflito com decisão aprovada;
- mudança material de escopo;
- ação irreversível.

Gate B:
- apresentar resultado;
- evidências;
- testes;
- riscos residuais;
- aguardar autorização para merge, release ou deploy.

## Routing

Consultar:
- `standards/`
- `skills/`

Não carregar todas as capacidades por padrão.
