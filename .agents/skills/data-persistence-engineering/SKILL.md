---
name: data-persistence-engineering
description: "Use em modelagem, consultas, persistência, schemas, migrations, transações, concorrência, integridade, performance de banco, backup/restore e governança de dados em sistemas web, locais ou APIs."
---

# Data & Persistence Engineering

## Missão
Manter dados corretos, íntegros, recuperáveis e acessíveis somente por operações autorizadas, escolhendo tecnologias e estruturas proporcionais ao problema.

## Ativação
- Novo modelo de dados ou alteração de schema.
- SQL/NoSQL, ORM, índices e queries críticas.
- Migrations, importações, sincronizações e integrações.
- Transações, concorrência, consistência, histórico e auditoria.
- Backups, recuperação, retenção e exclusão de dados.

Não ativar para alterações sem impacto em persistência.

## Processo
1. Mapear entidades, relações, dados sensíveis, regras e invariantes.
2. Identificar banco/stack existente e preservar contratos e registros.
3. Propor mudanças mínimas e compatíveis, com constraints, índices e validações justificados.
4. Definir migration, pré-condições, ordem, estimativa de risco, backup e recuperação.
5. Proteger acesso por credenciais restritas, rede adequada e autorização na aplicação.
6. Testar integridade, transações, concorrência, reversão/recuperação e impacto em dados existentes.
7. Registrar evidência, limitações e plano de operação.

## Boas práticas
- Queries parametrizadas, sem concatenar entrada não confiável.
- Constraints no banco para invariantes que devem sobreviver à aplicação.
- Índices fundamentados em consultas reais; evitar otimização especulativa.
- Transações explícitas em operações que devem ser atômicas.
- Identificar riscos de race condition, lost update, duplicidade e retries.
- Usar paginação e limites em consultas potencialmente caras.
- Tratar diferenças entre SQLite, PostgreSQL, MySQL e bancos não relacionais sem impor uma stack.
- Não copiar dados pessoais de produção para ambientes de teste por conveniência.
- Determinar retenção, acesso e exclusão conforme contexto legal e de negócio.

## Migrations seguras
Antes de mudança com dados existentes:
- verificar compatibilidade da aplicação e reversibilidade;
- distinguir rollback de código de recuperação efetiva dos dados;
- planejar backup e **testar restauração quando o risco exigir**;
- estimar downtime, locks e impacto operacional;
- avaliar migração gradual quando necessária;
- bloquear migração destrutiva ou irreversível sem aprovação humana.

## Testes mínimos proporcionais
- inserção, leitura, atualização e exclusão autorizadas;
- constraints e validação de entradas inválidas;
- migração com base sintética representativa;
- transações e erros parciais;
- concorrência/idempotência quando aplicáveis;
- integridade após rollback ou estratégia alternativa;
- isolamento por usuário/tenant quando relevante.

## Saída
Apresentar alterações de schema, scripts/migrations, impacto, estratégia de backup/restore, testes efetivamente rodados, riscos residuais e dependências de release. Não afirmar zero perda de dados sem evidências; não executar mudança destrutiva ou em produção sem autorização.
