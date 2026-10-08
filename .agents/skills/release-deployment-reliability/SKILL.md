---
name: release-deployment-reliability
description: "Use no preparo, empacotamento, CI/CD, deploy, distribuição, atualização, rollback, monitoramento e recuperação de websites, APIs, sistemas web e aplicativos locais. Acione na passagem entre ambientes ou quando houver risco operacional."
---

# Release, Deployment & Reliability

## Missão
Entregar software operável e recuperável, com segurança, rastreabilidade e evidência, independentemente da stack ou do ambiente de destino.

## Quando ativar
- Build, packaging e distribuição de aplicação web, backend ou desktop/local.
- Publicação em hosting, VPS, cloud, containers e ambientes privados.
- Configuração de CI/CD, secrets de deploy, migrations, observabilidade ou recuperação.
- Avaliação de readiness, incidentes, rollback, atualização e testes pós-deploy.

Não ativar deploy completo em ajustes de código sem intenção de distribuição.

## Processo
1. Levantar arquitetura existente, ambientes, usuários, dependências, banco, integrações e requisitos de disponibilidade.
2. Definir artefato imutável/versionado e procedimento de build reproduzível; validar dependências e scripts.
3. Conferir configuração por ambiente, segredos, TLS, privilégios de serviço, superfície de rede e acesso ao banco.
4. Planejar migrations, backup, reversão de código e recuperação de dados separadamente quando aplicável.
5. Definir gates de CI: lint, testes, segurança, build e smoke test proporcionais à criticidade.
6. Verificar plano de distribuição: deploy progressivo/atômico quando possível; installers, assinatura e atualizações seguras quando aplicativo local exigir.
7. Preparar health/readiness checks, logs, métricas, alertas e runbook proporcionais.
8. Apresentar plano, evidências, limites e riscos ao Gate B antes de merge protegido, release ou deploy.
9. Somente com autorização, executar release, verificar pós-deploy e registrar versão/rollback.

## Controles de segurança
- Nunca embutir secrets em frontend, binário distribuído, imagem/container, logs de build ou repositório.
- Revisar env vars, IAM/permissões, firewall, HTTPS e cadeia de suprimentos.
- Evitar instalar, criar ou pagar por recursos sem aprovação.
- Não expor portas ou banco de dados por conveniência.
- Não fazer deploy em produção por conta própria, mesmo que os testes passem.
- Tratar migrations irreversíveis, perda de dados e ações destrutivas como blockers.

## Recuperação
Ter um plano de restauração com responsáveis e passos verificáveis. A possibilidade de reverter o código não garante recuperação de dados. Quando o risco justificar, ensaiar backup e restore em ambiente não produtivo.

## Validação
Registrar efetivamente:
- commit/versão e artefato;
- comandos e ambiente;
- testes e scanners executados com resultados;
- integridade e configurações;
- riscos residuais e fallback;
- status `APPROVED`, `CHANGES_REQUIRED` ou `BLOCKED`.

Não declarar disponibilidade, rollback testado, backup válido ou conformidade sem evidência.
