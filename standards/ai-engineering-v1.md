# My Easy Development System AI Engineering Standard v1.0

## A. Identificação e governança

| Campo | Definição |
| --- | --- |
| Nome oficial | My Easy Development System AI Engineering Standard v1.0 |
| Identificador | Standard 06 |
| Versão | 1.0 |
| Estado canônico | Candidate |
| Finalidade | Definir regras operacionais para projetar, desenvolver, integrar, avaliar, proteger e operar funcionalidades com IA, com evidências e controles proporcionais ao risco. |
| Aplicabilidade | APIs de modelos, inferência, geração, extração, classificação, modelos preditivos, RAG, embeddings, indexação, ferramentas, agentes e automações, somente quando presentes no projeto. |
| Independência técnica | Não determina fornecedor, linguagem, framework, plataforma ou infraestrutura. Preserva arquitetura, contratos e decisões aprovadas. |

Candidate representa política proposta para validação operacional e revisão humana. Não significa que todo software que utilize IA seja experimental ou necessariamente inseguro. Também não comprova qualidade, segurança, conformidade, prontidão de produção ou aprovação de uma entrega. O baseline dos Standards existentes permanece aplicável durante sua avaliação.

**Escopo:** decisão de usar IA, arquitetura proporcional, contratos, seleção de modelos, prompts, APIs, recuperação, ações, avaliações, dados, segurança, confiabilidade, custos, capacidade, observabilidade e evolução. Treinamento ou ajuste de modelo próprio recebe controles específicos somente quando integrar o escopo real.

**Exclusões:** este documento não implementa código, serviços, integrações, RAG, agentes, MCP, banco vetorial, memória persistente ou ai-memory. Não exige LLM, treinamento, fine-tuning, múltiplos agentes, dependências ou infraestrutura especializada. Não concede orçamento, acesso a produção, uso de credenciais reais ou autorização de chamadas pagas, Git ou publicação.

### Fontes canônicas e responsabilidades

Ler [AGENTS.md](../AGENTS.md) e as instruções aplicáveis. Este Standard complementa as fontes abaixo, sem substituí-las:

| Fonte | Responsabilidade preservada |
| --- | --- |
| [Product System v4.0](product-system-v4.md), Standard 01 | Processo central, Gates A/B, autonomia, bloqueios, qualidade, revisão, evidências e evolução. |
| [Web Experience & Business Systems v1.0](web-experience-business-systems-v1.md), Standard 02 | Interfaces web/locais, experiência, estados, acessibilidade e apresentação segura de resultados. |
| [Capability Routing Standard v1.0](capability-routing-v1.md), Standard 03 | Menor conjunto suficiente de capacidades e reavaliação por superfície, fase e risco. |
| [Authentication & Security Standard v1.1](authentication-security-v1.md), Standard 04 | Identidades, autorização por ação/recurso, isolamento, sessão, recuperação e Security Gate. |
| [Environment Variables & Secrets Standard v1.0](environment-variables-secrets-v1.md), Standard 05 | Configuração, chaves, credenciais técnicas, exposição e ciclo de vida de segredos. |

O responsável pelo produto define objetivo, aceitabilidade e decisões materiais; o executor implementa e verifica dentro do Gate A; o revisor avalia resultado e evidências; o operador autorizado conduz entrega e recuperação. Papéis podem ser acumulados. Revisão feita pelo executor é **autorrevisão**, sem alegar independência por trocar de Skill ou etapa.

Atuar autonomamente no alcance aprovado, sem microaprovações. Produção, custo novo, credenciais fora do alcance, mudança material de escopo/segurança, destruição ou ação irreversível seguem os bloqueios do Product System. Interromper a ação afetada e solicitar decisão humana, continuando atividades independentes autorizadas. Disponibilidade de API, ferramenta ou modelo não concede autorização.

Merge, push a branch protegida, release e deploy permanecem sujeitos ao Gate B; demais operações Git exigem autorização correspondente. Proibições explícitas da tarefa prevalecem. Preparar plano, prompt, agente ou artefato não autoriza executar ações externas. Resolver conflitos materiais conforme Product System antes da ação dependente.

### Natureza das regras e referências

Salvo atribuição explícita, as regras são **decisões internas My Easy Development System propostas neste Candidate**. **Deve** indica obrigação para a superfície em que a política for aplicada; **quando** exige avaliar a condição; **recomenda-se** admite alternativa justificada. Recomendações externas, requisitos contratuais/legais e comportamento técnico verificado devem ser identificados separadamente. Não transformar referência voluntária em obrigação legal universal.

Referências consultadas em 2026-10-08:

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): portal oficial que apresenta o AI RMF como voluntário. O [AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) apresenta sugestões associadas a Govern, Map, Measure e Manage, sem exigir aplicação integral. Foram verificadas essas apresentações, sem atribuição de requisitos específicos do PDF não obtido.
- [OWASP GenAI Security Project](https://genai.owasp.org/): referência de riscos e recomendações de segurança. Consultadas páginas identificadas como edição 2025 sobre [prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), [tratamento de saídas](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/), [excesso de agência](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), [vetores/embeddings](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) e [consumo sem limites](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/). Não se atribuem controles a edições não examinadas nem se presume conformidade integral.
- [OWASP API Security Top 10, edição 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/): catálogo oficial de riscos, incluindo autorização por objeto/função, consumo de recursos e consumo inseguro de APIs. Consultadas também as páginas de [BOLA](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/), [recursos](https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/) e [APIs externas](https://api-security.owasp.org/editions/2023/en/0xaa-unsafe-consumption-of-apis/).

**Limitações de acesso:** a URL indicada `https://owasp.org/www-project-api-security/` retornou 404 na consulta; foi utilizado o portal oficial acessível acima. A obtenção do PDF AI RMF 1.0 por `https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf` falhou, incluindo timeout. Não se alega leitura integral dessa publicação. As páginas acessíveis fundamentam somente os pontos efetivamente verificados.

Os exemplos não dependem de fornecedor ou biblioteca específicos; não foram necessárias alegações sobre recursos de APIs concretas. Quando um projeto adotar um recurso, consultar documentação oficial de sua versão e verificar garantias, limitações e configuração reais. Fonte indisponível exige limitação explícita, sem inventar suporte, parâmetros ou resultados. Referência técnica não demonstra implementação ou conformidade legal do produto.

## B. Princípios de engenharia de IA

| Princípio | Regra operacional |
| --- | --- |
| Problema real | Escolher IA pelo benefício demonstrável à tarefa; comparar com solução determinística ou manual suficiente. |
| Qualidade verificável | Definir resultado esperado, erros relevantes e forma de avaliação; resposta fluente não comprova correção. |
| Proporcionalidade | Aprofundar controles conforme impacto, dados, exposição e ações; poucas chamadas podem ter alto risco. |
| Simplicidade e sustentabilidade | Usar a menor solução sustentável; não antecipar agentes, RAG, treinamento ou infraestrutura sem necessidade. |
| Privacidade e segurança por design | Minimizar dados, identificar confiança e autorizar acesso antes de encaminhar conteúdo ou executar operação. |
| Domínio sob controle confiável | Regras de negócio, invariantes, permissões e efeitos materiais devem ser validados fora da inferência. |
| Observabilidade e recuperação | Tornar falha, qualidade, consumo e estado da operação observáveis, com retomada segura. |
| Controle humano | Aplicar revisão/decisão humana efetiva quando o impacto ou a governança exigir, antes do efeito protegido. |
| Dependência de fornecedor proporcional | Explicitar contratos e permitir substituição quando viável; não criar abstração para vários fornecedores sem benefício real. |
| Evolução por evidência | Alterar solução diante de avaliação, necessidade ou risco verificados, sem escolher arquitetura por tendência. |

Não impor IA a problema resolvido adequadamente com lógica determinística. Uma funcionalidade pode combinar validação determinística, inferência limitada e revisão humana; nenhuma dessas partes comprova as demais.

## C. Discovery e decisão de usar IA

Recuperar requisitos, usuários/consumidores, contratos e soluções existentes antes da decisão. Para atividade pequena, um registro curto no contexto autorizado pode bastar.

| Questão | Definição necessária |
| --- | --- |
| Problema e beneficiário | Tarefa concreta, pessoa/processo beneficiado e resultado mensurável ou avaliável por rubrica. |
| Entradas e saídas | Dados, origem, formato, volume, destinatário e efeitos do resultado. |
| Interpretação ou geração | Necessidade real de lidar com linguagem, padrões ou conteúdo variável; distinguir de cálculo/regra exata. |
| Alternativa determinística | Avaliar regra, consulta, busca simples, template ou fluxo existente, com suas limitações. |
| Qualidade e risco de erro | Erros toleráveis, consequências de falso positivo/negativo, incerteza e necessidade de revisão humana. |
| Dados e privacidade | Disponibilidade, representatividade, qualidade, direito de uso, acesso e possibilidade de envio ao provedor. |
| Operação | Latência, custo, volume, conectividade e disponibilidade necessários, sem metas universais. |
| Fallback | Alternativa manual/determinística, resposta limitada ou suspensão segura quando IA não atender. |

Justificar proporcionalmente a escolha quando IA ampliar dependências, custo ou risco. Se uma regra exata satisfizer o objetivo, mantê-la. Se houver hipótese de benefício, testar em escopo controlado antes de atribuir ganho comprovado.

Distinguir protótipo, avaliação e operação produtiva. Protótipo simples não exige benchmark extenso, mas deve ter objetivo, casos suficientes para avaliar a hipótese e limites explícitos; não pode ignorar proteção de dados ou autorização. Lacuna material bloqueia a ação dependente, sem impedir análise independente autorizada.

## D. Arquitetura da solução

Definir o fluxo mínimo entre entrada, autorização, contexto permitido, inferência, validação, regra de negócio e apresentação/efeito. Essa separação pode ser expressa no código existente; não exige serviços ou camadas novos.

| Responsabilidade | Contrato verificável |
| --- | --- |
| Entrada | Validar tipo, tamanho, formato, origem e permissão para usar dados; delimitar entrada não confiável. |
| Domínio | Preservar invariantes, cálculos exatos e decisão de acesso no componente responsável. |
| Inferência | Produzir proposta de classificação, extração, previsão ou conteúdo dentro de contrato limitado. |
| Integração | Conhecer autenticação técnica, versão, capacidades, falhas e limites da API/serviço realmente adotados. |
| Validação de saída | Verificar estrutura, semântica, evidência e compatibilidade com o uso antes de persistir, exibir ou agir. |
| Erros e estado | Diferenciar resultado válido, recusa/ausência de evidência, falha, parcial e efeito desconhecido; definir recuperação. |
| Configuração | Separar ambientes, destino e parâmetros; secrets seguem Standard 05, sem valores em prompts ou logs. |
| Versionamento | Identificar código, prompt, modelo/configuração, schema e fonte/índice relevantes à reprodução e mudança. |

Reduzir acoplamento ao provedor quando isso ajudar manutenção real, respeitando contratos específicos. Não fingir equivalência de ferramentas, formatos ou garantias entre fornecedores. Workers, filas, microserviços, containers e outros mecanismos somente por necessidade demonstrada e autorização correspondente.

Quando saída alterar dados, selecionar controles de persistência e concorrência pertinentes. Revalidar autorização e pré-condições no momento do efeito quando mudanças simultâneas puderem invalidar a proposta; resultado gerado antes não reserva privilégio nem garante estado atual.

## E. Seleção de modelos e provedores

Escolher para a tarefa e o ambiente permitidos. Não estabelecer OpenAI, DeepSeek ou outro fornecedor como obrigação universal nem declarar modelo absolutamente superior sem escopo e evidência.

| Dimensão | Avaliação necessária |
| --- | --- |
| Adequação e limitações | Conferir modalidade, idioma, entradas, contexto e capacidades documentadas; verificar casos relevantes, não apenas demonstração favorável. |
| Qualidade | Comparar alternativas viáveis com casos/rubricas da seção H e baseline pertinente. |
| Custos e consumo | Conhecer contrato de cobrança e recursos efetivamente medidos, incluindo etapas auxiliares e falhas. |
| Latência e operação | Avaliar tempos, volume, concorrência, limites, resposta parcial e disponibilidade no contexto do produto. |
| Privacidade | Verificar destino, retenção, compartilhamento, uso de dados e condições contratuais da configuração adotada. Não presumir política comum a todo plano/provedor. |
| Saída estruturada e ferramentas | Confirmar suporte, schema aceito, recusas, limitações e semântica de chamadas. Nome do recurso não comprova garantia. |
| Estabilidade | Conhecer versionamento, alias, compatibilidade, mudanças e descontinuação pertinentes à integração. |
| Dependência | Avaliar impacto de indisponibilidade/substituição, formato dos dados e custos de migração; abstrair somente quando útil. |

Registrar identificador de modelo, versão disponível, configurações relevantes e data/ambiente de avaliação. Alias que pode mudar não equivale a versão imutável. Se pesos, versão interna ou políticas não forem observáveis, registrar esse limite; não prometer reprodução exata de saída por manter o mesmo nome ou parâmetro.

Treinamento/fine-tuning somente diante de hipótese, dados autorizados, baseline, critério de ganho e análise de custo/risco. Um modelo preditivo tradicional pode atender sem LLM; uma chamada direta pode atender sem RAG. Troca de provedor/modelo exige rever qualidade, contratos, privacidade, limites e recuperação afetados.

## F. Prompts e contratos de saída

Quando houver modelo orientado por prompt, definir tarefa, contexto necessário, critérios de sucesso, formato esperado e limites de comportamento. Separar instruções da aplicação de texto/documento/saída de ferramenta não confiáveis, com origem explícita. Essa separação melhora controle e avaliação, mas não garante resistência a injection.

| Elemento | Regra verificável |
| --- | --- |
| Instruções | Descrever tarefa e limites concretos, sem delegar autorização ou invariantes ao modelo. |
| Contexto | Fornecer somente informação necessária e autorizada; não incluir segredo, dado de outro tenant ou histórico irrelevante. |
| Schema | Definir campos, tipos, obrigatoriedade, valores permitidos, limites e representação de ausência/incerteza conforme domínio. |
| Semântica | Verificar unidades, referências, relações, enumerações e evidência; JSON bem formado não prova resposta correta. |
| Saída inválida | Rejeitar, limitar resposta ou encaminhar para revisão; correção/retry deve ser limitada e não liberar efeitos indevidos. |
| Versão | Registrar alteração significativa de prompt/schema e sua relação com modelo/configuração e casos de regressão. |

Quando a plataforma oferecer saída estruturada, consultar documentação e testar limites efetivos, incluindo recusa, interrupção e campo não suportado. Não presumir aderência ao schema ou correção factual em todas as respostas. Para modelos sem prompt, aplicar contratos equivalentes a features, tipos e saída preditiva.

Conteúdo gerado deve receber tratamento apropriado ao destino, como texto seguro, codificação contextual ou consulta parametrizada. Não executar SQL, comando, caminho ou markup apenas porque veio no formato esperado. Modelo não pode determinar permissão, alterar contrato confiável ou instruir o sistema a ignorar validação.

Mudança de prompt exige repetir avaliações afetadas e regressão pertinente. Não ajustar critérios silenciosamente para aprovar respostas novas. Versionamento deve ser proporcional, nos mecanismos existentes; não exigir armazenamento permanente de todos os prompts/respostas.

## G. Integração com APIs de modelos

Aplicar somente à integração efetiva. Autenticação técnica e API keys seguem Standard 05; permissões de usuário/recurso seguem Standard 04. Chave válida do provedor não autoriza qualquer operação da aplicação.

| Aspecto | Controle operacional |
| --- | --- |
| Configuração e destino | Validar ambiente, endpoint e parâmetros necessários; enviar dados/credenciais somente ao destino aprovado. |
| Timeout | Definir limite por chamada e orçamento total do fluxo conforme risco; não permitir espera sem limite operacional. |
| Rate limit e concorrência | Respeitar limites documentados e do produto; limitar trabalho simultâneo, volume e consumo pertinente. |
| Retries e backoff | Repetir somente falhas elegíveis, com tentativas/tempo limitados e atraso adequado ao contrato, evitando amplificação durante indisponibilidade. |
| Resposta incompleta | Distinguir finalização válida de truncamento, interrupção, recusa ou parte ausente conforme protocolo; não aceitar fragmento como operação concluída. |
| Cancelamento | Utilizar quando suportado; verificar efeito real. Parar a espera local não comprova interrupção no provedor nem ausência de cobrança/efeito. |
| Falha parcial | Identificar etapas concluídas, pendentes e de resultado desconhecido; reconciliar antes de repetir efeito material. |
| Consumo | Limitar entrada/saída, etapas e recursos conforme documentação e metas do produto; medir quando necessário. |
| Diagnóstico | Registrar etapa, categoria de erro, versão e referência segura; evitar segredo, payload pessoal e dump de contexto. |

HTTP de sucesso não prova conteúdo correto. Validar resposta antes de uso e diferenciar erro técnico de ausência de evidência. Avaliar falhas do SDK e retries já configurados para que camadas não multipliquem tentativas inadvertidamente.

Não repetir automaticamente ação financeira, publicação, exclusão ou outra operação com efeito material e resultado incerto. Definir idempotência ou reconciliação conforme contrato. Troca automática de provedor somente se previamente autorizada e avaliada para dados, custo, qualidade e compatibilidade; fallback não autoriza novo destino.

## H. Qualidade, avaliação e Evals

Evals são avaliações planejadas do comportamento de IA para uma tarefa. Relacionar casos a requisitos, riscos e critérios de aceite antes de concluir quando pertinente. Não exigir uma métrica universal ou benchmark extenso para hipótese simples.

| Dimensão | Casos e critério de avaliação |
| --- | --- |
| Representatividade | Entradas e segmentos relevantes, incluindo idiomas, formatos, classes e volumes previstos. |
| Qualidade semântica | Utilidade, fidelidade ao pedido e adequação por rubrica explícita; distinguir estilo de correção. |
| Fatos e evidência | Comparar afirmações verificáveis com fonte autorizada ou referência conhecida; detectar invenção e referência sem suporte. |
| Extração | Comparar campos esperados, omissões e inclusões incorretas, incluindo unidades e relações. |
| Classificação/previsão | Avaliar erro por classe/faixa pertinente e consequência de falsos positivos/negativos; médias podem ocultar falha crítica. |
| Formato | Validar schema, campos obrigatórios e limites sem confundir formato com semântica. |
| Ausência de informação | Exercitar pergunta sem suporte, dados incompletos/ambíguos e abstenção/encaminhamento esperados. |
| Negativos e limites | Entrada inválida, extensa, fora do domínio, parcial ou contraditória; comportamento seguro e resposta útil quando possível. |
| Adversariais e autorização | Injection direta/indireta, tentativa de exfiltração, acesso cruzado e ferramenta indevida; verificar controles efetivos. |
| Falhas e regressão | Provedor indisponível, timeout, versão/prompt/fonte alterados e defeitos anteriores, incluindo caminho legítimo. |

### Tipos de evidência

| Tipo | Uso e limitação |
| --- | --- |
| Teste determinístico | Valida contrato, regra, autorização e efeito observável com esperado definido. Não prova toda a qualidade semântica. |
| Avaliação humana | Aplica rubrica com avaliador identificado e contexto suficiente; registrar divergências e critérios. |
| Avaliação automatizada | Aplica comparação, regra ou métrica definida; conferir adequação ao objetivo e falhas de cobertura. |
| Avaliação assistida por outro modelo | Julgamento auxiliar que exige calibração com casos/referências humanas pertinentes; verificar viés, variação, desacordo e manipulação por conteúdo avaliado. Não é verdade absoluta. |
| Métrica operacional | Observação de erros, consumo, latência, aceitação ou qualidade em uso; não equivale a teste controlado nem prova causal de ganho. |

Usar dados sintéticos ou autorizados, com proveniência e acesso. Em treinamento/ajuste, separar dados usados para desenvolvimento dos usados para avaliação e evitar vazamento entre conjuntos, incluindo relações temporais/grupos relevantes. Não calibrar e aprovar pelo mesmo conjunto sem declarar limitação; reservar casos suficientes para verificar generalização quando necessária.

Definir rubrica, referência, limites de aceite e tratamento de desacordo conforme criticidade. Métrica assistida por IA deve ter versão do avaliador/prompt, condições e calibração verificadas; alterar avaliador pode alterar a medição. Confiança declarada pelo próprio modelo não é probabilidade calibrada de correção.

Resultados podem variar entre execuções. Definir repetição/amostragem proporcional e registrar configuração, versão, condições e variação relevante. Não afirmar determinismo por parâmetro isolado nem escolher somente resposta favorável. Avaliação sintética controlada não prova desempenho em toda a população real.

Registrar casos, esperado/rubrica, observado, método, ambiente, resultado, correções e limites no contexto autorizado. Mudança de modelo, prompt, schema, dados ou recuperação exige reavaliação afetada. Ausência de evidência essencial permanece pendente, sem alegar qualidade comprovada pela existência de prompts.

## I. RAG e recuperação de conhecimento

Aplicar recuperação quando a tarefa exigir conhecimento externo ao contexto disponível do modelo, com fontes autorizadas e necessidade de atualização/proveniência. Busca lexical simples, semântica ou híbrida deve ser escolhida por evidência de relevância; embeddings e banco vetorial não são obrigatórios.

| Etapa | Controle verificável |
| --- | --- |
| Seleção de fontes | Definir origem, direito de uso, classificação, responsável, confiabilidade, público permitido e condição de atualização. |
| Ingestão | Validar conteúdo/formatos e escopo; preservar origem e evitar mistura indevida de usuários/tenants. Documentos continuam não confiáveis para instruções. |
| Segmentação e metadados | Preservar significado, relações, referência, versão e permissões necessárias aos trechos; definir estratégia conforme documentos, não por tamanho universal. |
| Embeddings/indexação | Quando adotados, registrar modelo/configuração e compatibilidade do índice; proteger material derivado conforme sensibilidade da fonte. Não presumir anonimização por transformar texto em vetor. |
| Recuperação | Restringir candidatos por autorização confiável de usuário/tenant antes da recuperação e antes de entregar conteúdo ao modelo. IDs/filtros do cliente não concedem acesso. |
| Atualização e obsolescência | Propagar mudança de conteúdo, exclusão e revogação a índice, caches e fontes; definir validade e tratamento de versões conflitantes. |
| Geração e referências | Utilizar somente contexto permitido e verificar se afirmação/referência corresponde à fonte. Citação produzida pelo modelo não comprova suporte. |
| Ausência de resposta | Declarar informação insuficiente, pedir dado permitido ou encaminhar, sem preencher lacuna com fato inventado. |

No componente confiável, obter sujeito e concessões válidos, aplicar escopo ao mecanismo de busca e verificar resultados permitidos antes de uso. Não recuperar documentos de todos os tenants para pedir ao modelo que esconda os proibidos. Filtragem posterior ao envio já não preserva confidencialidade. Serviços e caches compartilhados devem manter isolamento em conteúdo, metadados, referências, contagens e histórico pertinentes.

Definir efeito de alteração de permissão durante fluxo, job ou sessão conforme contrato; impedir uso indevido de contexto anteriormente obtido quando a concessão deixar de ser válida. Autorização textual no prompt não substitui acesso efetivo a documentos.

Avaliar recuperação e geração separadamente quando aplicáveis: localizar evidência relevante e autorizada; depois verificar fidelidade, resposta e ausência de invenção. Incluir documento obsoleto, fonte conflitante, falta de resultado, injection e acesso cruzado. RAG não garante fatos corretos nem neutraliza injection.

## J. Agentes, ferramentas e automações

Escolher o menor grau de autonomia suficiente. Usar agente quando seleção dinâmica de etapas/ações trouxer benefício demonstrado; fluxo previsível pode ser determinístico com chamada limitada de IA.

| Forma | Distinção operacional |
| --- | --- |
| Assistente que responde | Produz conteúdo consultivo, sem presumir poder de executar operação externa. |
| Fluxo determinístico que chama IA | Código define sequência e permissões; inferência fornece resultado limitado a um contrato. |
| Agente que seleciona ações | Modelo propõe ferramenta/próxima etapa, sujeito a validação e autorização confiáveis. |
| Automação que executa operações externas | Realiza efeitos conforme fluxo autorizado; pode conter IA ou ser determinística. Execução exige controles independentemente do rótulo. |

Para ferramentas efetivas, definir objetivo, conjunto permitido, ação/recurso, sujeito, ambiente, argumentos/schema, limites de chamadas, duração e custo, estado e recuperação. A lista de ferramentas oferecida ao modelo não substitui autorização no executor.

| Controle | Resultado esperado |
| --- | --- |
| Permissão e argumentos | Validar função, recurso, campos, caminho/destino e contexto confiável antes da chamada. Não aceitar tenant/papel autoatribuído pelo modelo. |
| Limites | Aplicar orçamento total de etapas/tempo/consumo e concorrência no componente responsável; interromper loop sem progresso ou limite excedido. |
| Estado e idempotência | Identificar operação, passos e efeitos confirmados; evitar duplicidade em retry/retomada quando relevante. Persistir estado somente se recuperação exigir. |
| Falhas | Diferenciar erro, parcial e resultado desconhecido; reconciliar antes de repetir efeito e encaminhar quando necessário. |
| Aprovação humana | Para ação material, apresentar alvo/efeito concretos e bloquear execução até decisão válida conforme seção P. |
| Observabilidade | Registrar versão, ferramenta, etapa, resultado e referência segura, sem credencial/payload confidencial desnecessário. |

Preferir funções restritas ao domínio a shell aberto ou acesso arbitrário à rede/arquivos. Execução de comandos, quando necessária e autorizada, exige restrição de operação, argumentos, caminhos, permissões e destino; texto de modelo não deve ser concatenado como comando confiável.

MCP é opção de integração, não requisito nem concessão de confiança. Não exigir múltiplos agentes, memória persistente, framework de agentes ou servidor novo. A avaliação deve demonstrar que autonomia adicional atende objetivo sem ultrapassar autorização.

## K. Segurança, confiança e uso de ferramentas

Aplicar Standards 01, 04 e 05 às fronteiras efetivas. Conteúdo de usuário, repositório, documento recuperado, API externa, ferramenta e modelo é não confiável para conceder instrução ou acesso. Nem resposta gerada nem prompt de sistema autoriza leitura, execução, exclusão, publicação ou gasto.

| Risco pertinente | Controle a verificar |
| --- | --- |
| Prompt/tool-output injection | Distinguir dados de instruções e limitar influência sobre fluxo; autorização, validação e limites permanecem fora do modelo. Testar conteúdo malicioso em entradas e saídas de ferramentas. |
| Exfiltração e vazamento | Minimizar contexto, restringir arquivos/destinos, proteger segredo e impedir que saída, link, log ou ferramenta compartilhe dado proibido. |
| Execução indevida | Validar saída pelo uso, não executar código/comando/consulta livre e restringir ferramentas conforme J. |
| Abuso de recursos | Aplicar limites de entrada, resposta, etapas, concorrência e orçamento; evitar retries/loops que amplifiquem custo e indisponibilidade. |
| Acesso horizontal/vertical | Validar usuário, ação, recurso e campos no componente confiável, inclusive chamada direta fora da UI ou do fluxo de agente. |
| Isolamento multitenant | Cobrir recuperação, persistência, cache, histórico, ferramentas, jobs e resultados pertinentes; credencial técnica ampla não eleva acesso do solicitante. |
| Prompts e documentos | Não armazenar secrets no prompt nem confiar em sigilo do prompt como defesa; restringir distribuição de documentos internos e suas referências. |
| Integrações e dependências | Verificar origem, versões, permissões, dados/modelos e scripts pertinentes; não confiar em pacote ou URL sugeridos pelo modelo sem validação. |

**Recomendação externa:** a [OWASP sobre prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) descreve entradas diretas e indiretas e mitigação por limites de privilégio e aprovação de alto risco. Proteção textual, RAG ou fine-tuning isolados não comprovam prevenção. As regras de componente confiável deste Standard são decisões internas compatíveis com essa orientação.

Tratamento de saída, excesso de agência, vazamento na recuperação e abuso de API devem ter testes negativos proporcionais. Não substituir validação por pedir a outro modelo que aprove a ação. Identificar ameaças, controles, alcance examinado e riscos residuais; falhas críticas conhecidas bloqueiam release conforme Product System.

Esta seção cobre a funcionalidade de IA do produto. O futuro AI-Assisted Secure Development Threat Standard poderá aprofundar ameaças de desenvolvimento assistido por IA; sua ausência não suspende controles existentes nem exige duplicar seu catálogo futuro aqui.

## L. Dados, privacidade e governança

Definir finalidade, classificação, origem, acesso, destinatários, necessidade, retenção e exclusão dos dados usados em inferência, recuperação, avaliação ou treinamento. Minimizar antes de enviar ao provedor; não coletar/persistir informação pessoal por conveniência de contexto.

| Superfície | Decisão necessária |
| --- | --- |
| Provedor externo | Confirmar necessidade, autorização, destino e condições aplicáveis de uso, retenção e compartilhamento para o serviço/configuração adotados. |
| Histórico de conversas | Manter somente se requisito justificar, com acesso, isolamento, retenção e exclusão definidos; não exigir armazenamento permanente. |
| Fontes, índices e derivados | Preservar classificação/permissões e tratar exclusão/atualização em documentos, trechos, embeddings e caches quando existentes. |
| Logs e telemetria | Preferir metadados e agregações úteis; payload apenas quando necessário e autorizado, com proteção e retenção próprias. Nunca registrar credenciais. |
| Evals | Preferir dados sintéticos ou autorizados; proteger rótulos, referências e casos que possam conter dados sensíveis. |
| Treinamento/ajuste | Avaliar origem, direito de uso, minimização, vazamento e limites de remoção no modelo; apagar dataset não prova remoção da influência nos pesos. |

Identificar com o responsável requisitos legais/contratuais aplicáveis, incluindo LGPD/GDPR quando pertinentes, sem presumir aplicação universal ou conformidade automática. Se forem necessárias decisões jurídicas específicas, verificá-las antes da ação dependente. Este Standard não constitui auditoria legal.

Usar referências seguras e evidências sem valores sensíveis. Consentimento ou contrato, quando pertinente, não dispensa minimização, acesso e segurança. Credencial real não deve entrar em prompt, documento, dataset, log ou resposta conforme Standard 05; esta autoria não utiliza nem acessa esses valores.

## M. Confiabilidade e recuperação

Definir estado, resposta e próximo passo observáveis para falhas pertinentes. Escolher fallback determinístico, resposta limitada, encaminhamento humano, fila existente ou nova tentativa limitada conforme produto e autorização, sem impor infraestrutura adicional.

| Condição | Comportamento seguro |
| --- | --- |
| Provedor indisponível ou timeout | Limitar espera, informar indisponibilidade e acionar alternativa aprovada; não inventar resultado nem multiplicar chamadas. |
| Rate limit | Respeitar contrato e orçamento total, reduzir/rejeitar trabalho ou adiar se o fluxo permitir; não repetir indefinidamente. |
| Resposta inválida/incompleta | Rejeitar uso incompatível e corrigir/repetir somente com limite; não executar efeito com fragmento não validado. |
| Informação insuficiente | Abster-se ou pedir informação permitida; não apresentar palpite como fato confirmado. |
| Resultado inconsistente | Aplicar validação de domínio/evidência e encaminhar dúvida material; nova geração não é prova de verdade. |
| Falha de ferramenta | Registrar passo e efeito conhecido; reconciliar resultado incerto e evitar duplicidade antes de retomada. |
| Fonte desatualizada | Identificar validade, limitar resposta ou recuperar versão autorizada atual; não mascarar obsolescência. |
| Queda de qualidade após mudança | Interromper ampliação ou recuperar versão avaliada quando autorizado/compatível; rever contratos, dados e riscos. |

Resposta consultiva, execução iniciada e operação confirmada são estados distintos. Não apresentar resultado incerto como concluído. Reversão de código/modelo não desfaz automaticamente ação externa, dado persistido ou divulgação; recuperação deve contemplar esses efeitos e seguir autorizações do Product System.

Testar falha e retomada em ambiente controlado. Alternativa humana só é efetiva se houver responsável e caminho utilizável; mensagem genérica sem encaminhamento não comprova recuperação. Não usar secret padrão ou retirar autorização para manter disponibilidade.

## N. Custos, latência e capacidade

Estabelecer orçamento e limites proporcionais antes de operação com consumo relevante. Basear decisões em contrato atual, volume previsto e medição autorizada; não inventar preço, benchmark ou meta universal.

| Dimensão | Medição/controle pertinente |
| --- | --- |
| Recursos e custo por operação | Considerar inferência, tokens/recursos efetivos, recuperação, embeddings, ferramentas, armazenamento e retries quando presentes. Distinguir estimativa, uso observado e cobrança confirmada. |
| Orçamento | Definir responsável, limite e reação a aproximação/excesso conforme escopo; alerta isolado não impede gasto. Verificar mecanismo de contenção e suas limitações. |
| Latência percebida | Medir fluxo completo e etapas relevantes; streaming só é opção quando suportado e compatível com validação, sem mostrar parcial como conclusão. |
| Volume, concorrência e throughput | Avaliar carga representativa, filas existentes, limites de chamadas e recursos; não inferir capacidade por uma requisição bem-sucedida. |
| Limites por usuário/tenant | Aplicar quando risco de abuso, justiça de uso ou orçamento justificar, no componente confiável. |
| Caching | Usar somente se preservar autorização, isolamento, validade, exclusão e compatibilidade de versões/contexto. Revalidar acesso ao servir resultado. |
| Disponibilidade | Avaliar efeito de chamadas extensas, saturação e falha externa sobre outras funções; aplicar degradação segura e limites. |

Registrar ambiente, versão, carga, tamanho de entrada/saída, condições de execução e método antes de declarar eficiência comprovada. Otimização de contexto, modelo ou cache deve ser reavaliada para qualidade e segurança; redução de custo não justifica retirar dado essencial, autorização ou privacidade.

Nova chamada paga, recurso ou ampliação material de consumo exige autorização correspondente. Esta autoria documental não executa medição de API nem gera custo de integração. Testes futuros devem ter orçamento e destino explícitos no Gate A.

## O. Observabilidade e LLMOps/MLOps proporcionais

Manter informação suficiente para localizar componente, reproduzir avaliação dentro dos limites e detectar falha/regressão, usando mecanismos existentes. Não exigir plataforma de experiment tracking, model registry ou pipeline de treinamento para simples inferência por API.

| Informação pertinente | Registro mínimo útil |
| --- | --- |
| Identificação | Versão do componente/código, modelo/identificador disponível e configuração relevante, sem secret. |
| Prompt e contrato | Versão significativa de prompt/schema e conjunto de avaliações afetado, quando necessários. |
| Fontes e índice | Origem/versão, atualização e configuração da recuperação quando houver RAG. |
| Qualidade | Resultado de rubrica/métrica, abstenções, falhas representativas e regressão pertinente, com método e cobertura. |
| Operação | Categoria de erro, etapa, latência, consumo, limite e referência segura de operação quando úteis. |
| Incidente e evolução | Sintoma, versão afetada, impacto, decisão autorizada, correção/recuperação e verificações posteriores. |

Distinguir inferência via API de treinamento ou ajuste próprio. Para API, registrar o que é observável sem presumir acesso a dados de treinamento/pesos. Para modelo próprio, quando adotado, registrar proveniência/versões de dados, features, pré-processamento, configuração de treinamento, artefato, avaliação e compatibilidade de inferência. Conferir que transformação e contrato usados em produção correspondem ao modelo avaliado.

Monitorar degradação de dados/conceito e qualidade quando houver evidência e relevância; alteração na distribuição não prova automaticamente queda de desempenho. Definir sinais, condição de investigação e responsável. Rótulos tardios ou ausência de verdade observável limitam a avaliação operacional e devem ser declarados.

Mudança controlada deve relacionar versão anterior/proposta, motivos, casos de comparação, privacidade, risco e recuperação. Liberação gradual ou comparação paralela são opções somente quando adequadas e autorizadas; não duplicar envio de dados/custos por conveniência. Reavaliação, aprovação e distribuição seguem os Gates, sem treinamento ou publicação automáticos por métrica isolada.

## P. Human-in-the-loop e decisões de alto impacto

Exigir revisão/decisão humana efetiva antes de efeito material quando houver risco financeiro relevante, exclusão/modificação irreversível, mudança de privilégios, divulgação confidencial, decisão sensível com impacto relevante em pessoas ou ação operacional externa material. Considerar criticidade, reversibilidade, requisitos aplicáveis e autorização existente, sem exigir confirmação de cada consulta rotineira permitida.

Resposta consultiva pode orientar pessoa; execução modifica estado ou envia informação. Identificar essa diferença no contrato e na interface quando houver. Título de assistente, confiança do modelo ou aviso visual não constitui aprovação.

O controle humano deve apresentar proposta concreta com ação, alvo, alcance, consequência, informação/evidência suficiente e incerteza pertinente. No componente confiável, verificar sujeito autorizador, concessões e decisão vinculada à proposta antes de executar. Negação, expiração ou ausência de decisão não libera a operação. Mudança material de alvo, argumentos, permissões ou estado exige reavaliação e decisão apropriada; não reutilizar aprovação de outra ação.

Registrar decisão e efeito por referência segura, sem payload confidencial desnecessário. Não aceitar conteúdo recuperado ou saída do modelo como confirmação humana. Se não houver revisor ou condição necessária para a decisão, manter ação pendente e oferecer alternativa segura.

Preservar Gates A/B do desenvolvimento. Autorização operacional de uma ação no produto não substitui Gate B para publicação; aprovação de deploy não concede ao agente do produto operações financeiras ou divulgação irrestrita. Usar autorizações anteriores válidas dentro do alcance, sem microaprovações, e consultar o responsável diante de mudança material conforme Product System.

## Q. QA, Security Gate e Definition of Ready/Done

### Verificações e evidências

Relacionar contratos, casos da seção H e riscos das seções I a P às verificações da tarefa. Incluir, quando pertinentes, entrada/saída válida e inválida, evals representativas, regressão, injection direta/tool-output, isolamento, privacidade, falha do provedor, custo/limites, integridade, recuperação e observabilidade.

Testar autorização por chamada direta ao componente confiável, sem depender da recusa textual do modelo ou de controle visual. Verificar recuperação com fontes permitidas, ferramentas com argumentos negados, mudança de permissão, dados ausentes e resultado de efeito desconhecido conforme o contrato. Incluir caminho legítimo para evitar que segurança seja simulada por inutilizar a função.

Usar ferramentas existentes, dados sintéticos ou autorizados e escopo de teste explícito. Nesta autoria, verificações são documentais; não usar credenciais reais ou APIs pagas para representar execução. Não exigir todas as camadas, scanner externo ou instalação por padrão.

Registrar requisito/caso, versão, método, ambiente, esperado/rubrica, observado, evidência, cobertura e limitação. Distinguir inspeção, teste determinístico, eval humana/automatizada e scanner realmente executado. Usar `PASS`, `FAIL`, `BLOCKED` ou `NOT_APPLICABLE` conforme Product System. Não marcar `PASS` para teste não executado; ausência de ambiente/autorização para verificação essencial é blocker, não inaplicabilidade.

### Security Gate

Security Review deve relacionar controles a implementação/configuração e evidências reais, identificar achados e riscos residuais e conferir autorização, dados, ferramentas, secrets e consumo pertinentes. Seleção de Vera, existência de prompt ou recusa de um caso isolado não comprovam segurança.

Identificar autor/revisor e declarar autorrevisão quando aplicável; outro modelo/Skill não cria independência. Se revisão independente for requisito obrigatório, sua ausência impede prontidão. Corrigir no Gate A e repetir verificações afetadas antes de concluir.

Parecer `APPROVED` exige critérios pertinentes atendidos e evidência essencial suficiente no alcance declarado. `CHANGES_REQUIRED` indica defeito/evidência insuficiente corrigível no escopo; `BLOCKED` identifica decisão, autorização, ambiente ou outra condição necessária ausente. Falha crítica conhecida bloqueia release. O parecer não autoriza Gate B nem demonstra conformidade integral.

### Condições de realização

| Estado | Condição verificável |
| --- | --- |
| Ready | Objetivo/Gate A, benefício de IA, entradas/saídas, regra determinística, dados/permissões, risco, contrato, configuração, limites, fallback e avaliações estão suficientes para a próxima etapa. Lacuna material bloqueia somente a ação dependente. |
| Implementado | Integração/funcionalidade prevista existe e foi inspecionada, preservando contratos e limites; não implica qualidade avaliada ou publicação. |
| Avaliado | Verificações/evals essenciais foram executadas e aceitas conforme critérios, com versões, métodos, cobertura e limites registrados. |
| Security Review realizada | Alteração final e controles pertinentes examinados, Security Gate registrado, achados tratados e independência/autorrevisão identificadas. |
| Pronto para aprovação | Critérios essenciais satisfeitos, revisões exigidas concluídas, riscos residuais e recuperação definidos e evidências reunidas para Gate B. |
| Publicado quando autorizado | Entrega autorizada executada, com versão, ambiente e procedimento registrados; não equivale a verificação operacional. |
| Verificado operacionalmente | Fluxos críticos, configuração, qualidade/sinais, limites e recuperação pertinentes conferidos no destino autorizado, com resultados reais e limitações. |

Aplicar também as Definitions do Product System e Standards pertinentes. Ajuste trivial pode usar análise/verificação curta; mudança de ferramenta, autorização ou contexto sensível exige profundidade adequada. Não declarar qualidade/segurança comprovadas apenas por prompt, schema, demo favorável ou aprovação documental deste Candidate.

### Exemplos práticos

Os oito cenários são orientações para aplicação e verificações futuras, não implementações, testes executados ou exigências de fornecedor/infraestrutura. Usar dados sintéticos ou autorizados, sem credenciais reais nos exemplos. Controles dispensáveis pressupõem ausência da superfície e devem ser reavaliados se ela mudar.

#### 1. Classificação de solicitações comerciais com IA

**Objetivo:** sugerir categoria de atendimento para textos variados. **Riscos:** classificação incorreta, distribuição desigual de erros, dados pessoais e confiança não calibrada. **Seleção técnica:** comparar regras simples com inferência limitada a categorias permitidas; manter roteamento material e revisão de dúvida no domínio. **Verificações:** casos por classe, ambiguidade, fora do domínio, formato inválido, falsos positivos/negativos e regressão; critério de aceite definido antes de aprovar. **Controles dispensáveis:** RAG, embeddings, agente, banco vetorial e treinamento próprio se a chamada direta atender. A sugestão não concede privilégio nem confirma ação comercial.

#### 2. Resumo de documento

**Objetivo:** produzir síntese fiel de documento autorizado fornecido na tarefa. **Riscos:** omissão relevante, invenção, exposição ao provedor e injection no texto. **Seleção técnica:** inferência sobre conteúdo mínimo permitido, preservando referência e limites; revisão humana conforme impacto. **Verificações:** comparar resumo com fonte, ausência de evidência, documento extenso/incompleto e instrução maliciosa; conferir que conteúdo proibido não foi enviado. **Controles dispensáveis:** índice/RAG persistente, memória permanente ou ferramentas externas quando o documento já integra o contexto autorizado. O resumo não substitui análise especializada exigida pelo uso.

#### 3. Extração estruturada de informações

**Objetivo:** extrair campos definidos de documento para revisão. **Riscos:** JSON válido com dado inventado, unidade incorreta, campo omitido e persistência indevida. **Seleção técnica:** contrato/schema, representação de ausência e validação semântica; usar saída estruturada somente se suportada e verificada. **Verificações:** valores de referência sintéticos, campos ausentes, schema inválido, recusa/interrupção e erro de unidade; autorização e regra de domínio antes de salvar se houver persistência. **Controles dispensáveis:** agentes, RAG ou fine-tuning sem necessidade demonstrada. Formato correto não é aprovação do conteúdo.

#### 4. Chat com base de conhecimento via RAG

**Objetivo:** responder com documentos atualizáveis permitidos ao usuário. **Riscos:** acesso entre tenants, fonte obsoleta, referência inventada e injection indireta. **Seleção técnica:** busca simples inicial ou lexical/semântica/híbrida conforme evidência, com proveniência e autorização antes da recuperação; contexto enviado ao modelo contém somente resultados permitidos. **Verificações:** medir recuperação e geração separadamente; testar documento relevante, sem resultado, revogação, fonte antiga e tentativa de outro tenant por chamada direta. **Controles dispensáveis:** banco vetorial, embeddings ou multiagentes quando busca simples for suficiente. Pedir ao modelo que oculte documento proibido é inadequado.

#### 5. Integração de IA com API externa

**Objetivo:** interpretar solicitação e consultar informação em serviço aprovado. **Riscos:** endpoint/argumento indevidos, segredo exposto, dado externo incorreto e retry com efeito não previsto. **Seleção técnica:** fluxo determinístico com saída limitada, validação de argumento, destino aprovado e credencial no componente autorizado. **Verificações:** chamada legítima em ambiente permitido, argumento rejeitado, resposta externa maliciosa/inválida, timeout, rate limit e logs sem valores sensíveis. **Controles dispensáveis:** agente autônomo, MCP, RAG ou fila nova se a sequência for fixa e a consulta simples. Credencial técnica não substitui acesso do solicitante ao recurso.

#### 6. Agente com ferramenta de consulta e ação controlada

**Objetivo:** consultar estado autorizado e propor alteração delimitada. **Riscos:** escolha indevida de ferramenta, escalada, duplicidade, loop e execução sem aprovação. **Seleção técnica:** ferramentas restritas, autorização por ação/recurso, argumentos validados, orçamento de etapas e aprovação humana real antes de efeito material. **Verificações:** negar ferramenta/recurso proibidos, injection na saída da consulta, limite excedido, decisão ausente/expirada, alvo alterado e retomada sem duplicar efeito. **Controles dispensáveis:** múltiplos agentes, shell aberto, memória persistente e MCP obrigatório. Confirmação visual sem bloqueio no executor é insuficiente.

#### 7. Aplicação que usa modelo preditivo tradicional

**Objetivo:** estimar demanda a partir de dados históricos autorizados. **Riscos:** vazamento entre treino/avaliação, features indisponíveis no momento da previsão, degradação e uso de previsão como certeza. **Seleção técnica:** comparar baseline determinístico e modelo adequado, versionar dados/features/artefato e manter pré-processamento compatível; treinamento apenas se integrar o escopo aprovado. **Verificações:** avaliação temporal/grupos pertinente, erro nos segmentos relevantes, entradas ausentes, compatibilidade de inferência e monitoramento de degradação quando justificável. **Controles dispensáveis:** prompts, LLM, RAG, agente e plataforma complexa de registro para pipeline simples. Previsão não autoriza decisão material automática.

#### 8. Aplicação com API de IA indisponível

**Objetivo:** preservar tarefa principal durante falha do provedor. **Riscos:** espera ilimitada, tempestade de retries, custo excessivo e operação duplicada/desconhecida. **Seleção técnica:** timeout e retries limitados, fallback determinístico/encaminhamento humano aprovado e estado explícito. **Verificações:** simular indisponibilidade, atraso, rate limit, retorno parcial e recuperação; confirmar orçamento total, diagnóstico seguro e ausência de sucesso aparente. **Controles dispensáveis:** segundo provedor, fila nova ou múltiplos agentes se alternativa simples atender. Troca de destino sem análise/autorização de dados e custo é inadequada.

## R. Capability Routing, exceções e evolução

### Seleção e reavaliação

Aplicar Standard 03 e consultar instruções completas das capacidades efetivamente selecionadas quando não estiverem disponíveis e válidas no contexto. A leitura integral na autoria deste documento é excepcional, não requisito para todas as tarefas futuras. Não ativar todas as Skills por padrão nem omitir capacidade crítica por economia de contexto.

| Skill canônica | Quando consultar/aplicar |
| --- | --- |
| [ai-engineering-production](../.agents/skills/ai-engineering-production/SKILL.md) | Projeto, integração, recuperação, agente, evals ou operação de componente efetivo de IA exigirem engenharia especializada. |
| [vera-architecture-security](../.agents/skills/vera-architecture-security/SKILL.md) | Dados sensíveis, confiança, autorização, ferramentas, secrets, exposição ou Security Review forem afetados. |
| [quality-engineering-testing](../.agents/skills/quality-engineering-testing/SKILL.md) | Planejar/executar testes, avaliações, falhas, abuso, contratos ou regressão da superfície pertinente. |
| [software-design-solid](../.agents/skills/software-design-solid/SKILL.md) | Implementar/revisar lógica, APIs, contratos e responsabilidades de código; não exigir em texto documental sem implementação. |
| [data-persistence-engineering](../.agents/skills/data-persistence-engineering/SKILL.md) | Persistência, índices, fontes armazenadas, transações, isolamento ou recuperação de dados forem afetados; não exigir por chamada sem armazenamento. |
| [release-deployment-reliability](../.agents/skills/release-deployment-reliability/SKILL.md) | Build, configuração, empacotamento, distribuição, entrega, recuperação ou verificação operacional integrarem o escopo; preparação não autoriza deploy. |

Acrescentar `kael-interface-engineering` para implementação de UI, `julian-premium-design` para direção/UX, `clara-premium-copywriting` para texto e `visual-interface-qa` para mudança visual relevante renderizada, somente quando interface/experiência entrar no escopo. Consultar procedimentos pelo inventário canônico do Standard 03. Essa relação não exige direção de arte completa em correção pontual.

`seo-technical` depende de conteúdo público indexável; `ai-search-visibility` depende de objetivo de descoberta/compreensão pública por busca com IA. Não selecioná-las apenas porque existe modelo, RAG ou agente interno. Assistência de IA ao desenvolvimento também não significa que o produto integra IA.

Ampliar roteamento diante de novo dado sensível, permissão, persistência, provedor, ferramenta, comando, ação material, interface, exposição, preparação de release ou risco não previsto. Registrar motivo e mudanças no contexto existente. Se houver mudança material fora do Gate A, solicitar decisão antes da ação afetada.

### Exceções, evidências e validação futura

Adaptar profundidade de discovery, avaliação, documentação e mecanismo ao risco. Não dispensar autorização confiável, proteção de secrets/dados, integridade ou evidências essenciais. Falta de ferramenta/ambiente não transforma verificação necessária em inaplicável.

Registrar exceção relevante com regra, motivo, alcance, risco, controle compensatório, responsável e condição de reavaliação, conforme Product System. Obter aprovação humana quando alterar segurança material, governança, requisito contratado ou decisão aprovada. Exceção interna não elimina exigência externa aplicável, libera falha crítica ou concede ação protegida.

Usar relatório/contexto autorizados, sem criar log obrigatório ou persistir conversas por padrão. Separar observado, inferido e recomendado; identificar autorrevisão e suas limitações. Aprovação documental pode recomendar revisão humana mantendo Candidate; não comprova funcionalidade de IA nem promove estado automaticamente.

O futuro **AI-Assisted Secure Development Threat Standard** complementará ameaças específicas quando efetivamente criado/aprovado. Não estava materializado no inventário da autoria e não é dependência obrigatória existente. Inspecionar inventário real ao retomar; atualizar roteamento/referências de outros documentos somente mediante escopo próprio.

Recomenda-se validação operacional controlada posterior, com escopo, ambiente, orçamento e autorização definidos, cobrindo casos representativos de classificação, extração, RAG com acesso, ferramenta com ação, modelo tradicional e falha externa. Examinar qualidade, omissões/excessos de controles, limites, Gates e recuperação. Resultados devem orientar revisão da política; não implementar funcionalidades para declarar esta autoria validada.

### Versionamento

Evoluir por achado de uso, conflito, referência técnica alterada ou nova superfície comprovada. Identificar regra, fonte, evidência, impacto, compatibilidade e transição; seguir Product System para aprovação e versionamento: maior para incompatibilidade de governança, menor para regra operacional compatível e corretiva para esclarecimento sem mudança de obrigação. Não mudar regra ou estado silenciosamente mantendo sua identificação.

| Versão | Estado | Registro e limite de evidência |
| --- | --- | --- |
| 1.0 | Candidate | Política inicial de engenharia de IA proporcional, contratos, evals, recuperação, ferramentas, segurança, operação e exemplos. Revisão documental e fontes verificadas; validação operacional e decisão de adoção permanecem posteriores. |

Eventual passagem a Stable exige revisão autorizada, evidências suficientes de aplicação e decisão humana conforme governança. Não inferir essa passagem de teste isolado ou parecer técnico. Esta entrega cria somente o Standard autorizado, sem implementar IA, iniciar outro documento ou executar versionamento; aguarda revisão humana do conteúdo.
