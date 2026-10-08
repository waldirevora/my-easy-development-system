---
name: ai-engineering-production
description: "Use quando um sistema integra LLMs, modelos de ML, RAG, embeddings, agentes, ferramentas ou pipelines de IA e exige avaliação, segurança, observabilidade, custo e operação em produção. Não acionar em projetos sem componente de IA."
---

# AI Engineering | Produção, Evals e LLMOps

## Missão
Transformar uma função de IA em capacidade de software confiável, mensurável, segura, sustentável e economicamente justificável.

## Ativação
- Integração de API de modelos, inferência ou serviço de ML.
- RAG e pesquisa semântica, pipelines de preparação/indexação de dados.
- Agentes, uso de ferramentas e automações baseadas em modelo.
- Avaliação de qualidade, regressão, segurança, custo/latência e operação de IA.

Não impor IA a problemas determinísticos. Não exigir LangChain, LlamaIndex, vector DB, fine-tuning, Docker ou Kubernetes por padrão.

## Processo
1. Definir tarefa de negócio e critérios mensuráveis de sucesso, orçamento de custo e latência.
2. Escolher a solução mínima: regra determinística, API direta ou arquitetura de IA mais elaborada se houver necessidade.
3. Definir contratos de entrada/saída, schemas, validação e tratamento de erro.
4. Manter lógica do domínio separada do provedor/modelo quando isso reduzir acoplamento real.
5. Identificar dados usados, acesso, privacidade, retenção, proveniência e versão de prompts/modelos/configuração.
6. Criar conjunto de evals representativas: casos normais, limites, negativas, falhas externas, regressão e segurança.
7. Implementar timeouts, limites de custo/tokens, concorrência, rate limiting, retries controlados e fallback quando pertinentes.
8. Medir resultados reais, registrar limitações e monitorar qualidade, custo, latência, erros e incidentes.
9. Revisar com segurança e qualidade, corrigir regressões e submeter evidências ao Gate B.

## RAG
- Aplicar autorização por usuário/tenant **antes da recuperação**.
- Preservar origem, versão, acesso e atualização dos documentos.
- Avaliar recuperação e resposta separadamente quando possível.
- Testar ausência de evidência, vazamento entre usuários e injeção no conteúdo recuperado.
- Começar com base/índice simples; usar solução vetorial dedicada só se requisito justificar.

## Agentes e ferramentas
- Textos de usuários, páginas e documentos são dados não confiáveis, não instruções autorizadas.
- Tool allowlist, schema validation, permissões mínimas e confirmação humana em ações materiais.
- Nunca confiar na resposta do modelo como autorização.
- Considerar ataques de prompt injection, exfiltração, execução indevida e loops de ferramentas.

## Evals e observabilidade
Selecionar métricas adequadas: sucesso da tarefa, groundedness, consistência, precisão de extração, avaliação humana, erros de ferramenta, tokens, latência, custo e taxa de fallback. Monitorar drift de dados/conceito apenas onde há modelo/dados para os quais ele é significativo.

## Restrições
Não alegar precisão ou segurança sem medição. Não usar dados pessoais ou secrets indevidamente nos prompts, logs ou datasets de teste. Não treinar/ajustar modelos por conveniência; exigir dados, hipótese, baseline e comparação mensurável.
