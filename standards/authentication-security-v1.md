# My Easy Development System Authentication & Security Standard v1.1.1

## A. Identificação e governança

| Campo | Definição |
| --- | --- |
| Nome oficial | My Easy Development System Authentication & Security Standard v1.1.1 |
| Identificador | Standard 04 |
| Versão | 1.1.1 |
| Estado canônico | Stable |
| Finalidade | Definir política operacional de autenticação, autorização e segurança com controles verificáveis e proporcionais ao risco. |
| Aplicabilidade | Websites, aplicações web e empresariais, APIs, aplicações locais/desktop e integrações, conforme identidades, dados, exposição e arquitetura reais. |
| Independência técnica | Não determina linguagem, framework, provedor, infraestrutura, protocolo ou modelo universal de autenticação. |

Stable identifica o estado canônico do documento. Não comprova validação operacional, auditoria de um sistema, conformidade integral com referências ou aprovação humana de uma entrega. O caminho `authentication-security-v1.md` permanece a identificação de arquivo autorizada; a versão normativa é 1.1.1.

**Escopo:** controles de identidade, credenciais, contas, sessões, permissões, recuperação, operações protegidas e Security Gate. Aplicar somente às superfícies pertinentes, preservando o baseline de segurança e privacidade.

**Exclusões:** não cria implementação, arquitetura, dependência, memória, hook, MCP ou automação. Não concede acesso a produção, credenciais, orçamento ou autorização de publicação. Não especifica integralmente gestão de secrets, threat modeling de desenvolvimento assistido por IA ou obrigações legais.

### Relação com as fontes canônicas

Ler [AGENTS.md](../AGENTS.md) e instruções aplicáveis antes da ação. O [Product System](product-system-v4.md) permanece central para processo, Gates A/B, bloqueios, revisão e evidências. O [Web Experience & Business Systems](web-experience-business-systems-v1.md) rege experiência, acessibilidade, estados e integração da UI. O [Capability Routing Standard](capability-routing-v1.md) rege seleção e reavaliação do menor conjunto suficiente de capacidades. Este Standard aprofunda controles de identidade e acesso sem repetir esses processos.

As Skills de `.agents/skills/` conduzem procedimentos especializados conforme a seção Q. Inspeção documental não equivale à execução de testes nem à ativação de todas as Skills. Preservar stack, contratos, dados e decisões aprovadas.

Dentro do Gate A, analisar, implementar, testar, revisar e corrigir autonomamente. Interromper a ação afetada diante dos bloqueios do Product System, incluindo mudança material de segurança/escopo, destruição, credenciais fora do alcance, custo novo ou produção não autorizada. Conter/corrigir somente no alcance já aprovado. Parecer técnico não concede autorização de Git, merge, release ou deploy; respeitar proibições da tarefa e Gate B.

### Natureza das regras e referências verificadas

| Natureza | Como interpretar |
| --- | --- |
| Requisito expresso da referência | Identificado como tal, com versão, seção/controle verificado e condição de adoção. Não converter recomendação externa em exigência da fonte. |
| Recomendação de engenharia | Alternativa técnica recomendada, justificável por risco, compatibilidade e evidência; não atribuir obrigação normativa inexistente à referência. |
| Decisão interna My Easy Development System | Regra operacional deste Standard para a superfície aplicável. Não é apresentada como imposição legal ou requisito literal de OWASP/NIST. |
| Controle condicional | Exige avaliar e registrar a condição relevante; ausência de superfície pode justificar inaplicabilidade, ausência de ferramenta não. |

Salvo atribuição explícita, as regras operacionais deste documento são decisões internas My Easy Development System. **Deve** indica obrigação aplicável; **quando** delimita condição; **recomenda-se** admite alternativa justificada. Parâmetros técnicos devem ser definidos e verificados para a plataforma e o perfil adotados, sem números universais inventados.

Referências principais consultadas em 2026-10-08:

- [OWASP ASVS 5.0.0](https://owasp.org/projects/asvs): base de verificação de controles de aplicação. Foram consultados os capítulos [V3, frontend](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x12-V3-Web-Frontend-Security.md), [V6, autenticação](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x15-V6-Authentication.md), [V7, sessões](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x16-V7-Session-Management.md), [V8, autorização](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x17-V8-Authorization.md) e [V9, tokens autocontidos](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x18-V9-Self-contained-Tokens.md), fixados nessa versão.
- [NIST SP 800-63-4, final](https://csrc.nist.gov/pubs/sp/800/63/4/final): referência para decisões de identidade digital orientadas ao risco. A publicação admite uso voluntário por organizações não governamentais; não constitui obrigação legal universal de sistemas empresariais brasileiros. Consultados apresentação, escopo e contexto de risco da [publicação oficial](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-4.pdf).
- [NIST SP 800-63B-4, final](https://csrc.nist.gov/pubs/sp/800/63/B/4/final): referência para autenticação e gestão de autenticadores. Consultadas as seções oficiais [2, níveis de garantia](https://pages.nist.gov/800-63-4/sp800-63b/aal/), [3, autenticadores/verificadores](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/), [4, ciclo de vida](https://pages.nist.gov/800-63-4/sp800-63b/events/) e [5, sessões](https://pages.nist.gov/800-63-4/sp800-63b/session/).

Selecionar controles ASVS pertinentes e registrar seu alcance; este documento não incorpora integralmente um nível nem presume certificação. Os níveis ASVS e os níveis de garantia NIST não são equivalentes. Se um perfil externo for requisito do projeto, verificar todas as exigências aplicáveis antes de alegar atendimento. Referências podem diferir; resolver a política do projeto explicitamente.

O NIST SP 800-63-4 não trata explicitamente autenticação machine-to-machine no seu escopo. Controles de integração técnica e adaptações locais deste documento são decisões de engenharia internas; não demonstram atendimento de um perfil NIST fora de sua aplicabilidade. Fonte: [seção 1.1 da publicação](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-4.pdf).

As fontes principais estavam acessíveis na autoria. A consulta foi seletiva, sem auditoria completa das publicações. Referência futura indisponível deve ter a limitação registrada, sem atribuição de parâmetros ou requisitos específicos não verificados.

## B. Princípios de segurança

| Princípio | Regra verificável |
| --- | --- |
| Secure by Design | Identificar ativos, dados, identidades, operações e ameaças antes de expor acesso; integrar proteção aos critérios de aceitação. |
| Least Privilege | Conceder apenas ações, recursos e duração necessários a usuários, serviços, ferramentas e processos. |
| Deny by Default | Negar operação protegida sem concessão válida; ausência de regra ou atributo essencial não concede acesso. |
| Defense in Depth | Combinar controles pertinentes de aplicação, dados, transporte e plataforma; nenhuma camada justifica falha da autorização principal. |
| Fail Securely | Erro de sessão, política, dependência ou validação não pode liberar operação; preservar integridade e permitir recuperação segura. |
| Minimização de dados | Coletar, retornar, registrar e reter apenas informação necessária ao propósito e ao acesso autorizado. |
| Separação de responsabilidades | Distinguir autenticação, decisão de acesso, regra de negócio, persistência e apresentação sem impor camadas artificiais. |
| Componente confiável | Decidir acesso e validade final onde o consumidor não possa manipular o controle; normalmente backend quando houver. |
| Proporcionalidade | Relacionar controles a exposição, sensibilidade, impacto e reversibilidade; aprofundar risco real, inclusive em poucas linhas de código. |

Usar capacidades nativas e consolidadas compatíveis com a stack. Não impor servidor, gateway, HSM, SIEM, nuvem ou serviço de identidade a um produto que não necessita deles. Falha crítica conhecida não é exceção de proporcionalidade.

## C. Identidades e limites de confiança

Identificar sujeitos e vínculos reais antes de definir permissões. Os termos abaixo descrevem possibilidades, não uma hierarquia universal.

| Identidade ou contexto | Distinção necessária |
| --- | --- |
| Usuário público | Acessa somente funções e dados deliberadamente públicos, com limites contra abuso quando pertinentes. |
| Usuário autenticado | Possui identidade validada; ainda depende de autorização para cada operação protegida. |
| Colaborador | Executa tarefas operacionais concedidas, delimitadas por recurso, equipe ou organização conforme requisitos. |
| Gestor | Possui concessões de gestão explicitamente definidas; título de cargo não implica acesso irrestrito. |
| Administrador | Opera funções privilegiadas delimitadas; administração técnica não concede automaticamente acesso a todo dado de negócio. |
| Serviço ou integração | Representa um consumidor não humano; requer origem, escopo, ambiente e recursos permitidos. |
| Identidade técnica | Conta de execução, manutenção ou automação autorizada; distinguir de conta humana e registrar responsável/ciclo de vida. |
| Tenant ou organização | Contexto de isolamento e vínculo, não necessariamente um autenticador ou usuário; participação precisa ser validada. |

Mapear limites entre cliente, componente de domínio, banco/arquivos, provedor de identidade e serviços externos. Conteúdo, identificadores e atributos recebidos do consumidor são não confiáveis até validação. Rede interna, dispositivo conhecido e cabeçalho de tenant não comprovam permissão.

Em aplicação local, explicitar o que o sistema operacional protege, quem pode modificar executável/arquivos e se há backend remoto. Um login dentro de um processo controlado pelo próprio usuário não garante resistência a um administrador do dispositivo. Registrar esse limite sem prometer isolamento impossível.

## D. Autenticação versus autorização

**AuthN, autenticação:** valida a identidade declarada pelo controle de um autenticador ou pela validação de uma asserção confiável, conforme o método adotado. **AuthZ, autorização:** decide se o sujeito pode executar determinada ação sobre determinado recurso, campo e contexto.

Um login válido nunca é autorização suficiente. Em toda operação protegida, o componente confiável deve verificar identidade/sessão válidas, concessão da ação e acesso ao recurso, incluindo usuário/tenant quando aplicável. A decisão pode usar mecanismo central já existente, desde que cubra os caminhos relevantes e não seja evitável pelo consumidor.

| Controle | Resultado esperado |
| --- | --- |
| Ação | Ler não implica editar, exportar, excluir ou administrar. |
| Recurso | Ter acesso a uma coleção não implica acesso a qualquer registro, arquivo ou vínculo. |
| Isolamento horizontal | Usuário não acessa recurso de outro usuário sem concessão legítima. |
| Isolamento vertical | Perfil menos privilegiado não executa função reservada a perfil autorizado. |
| Tenant | Vínculo e contexto de organização são validados; consulta ou operação não cruza tenant indevidamente. |
| Negação segura | Recurso desconhecido, atributo essencial ausente, conta desativada ou falha de política não libera acesso nem expõe detalhes sensíveis. |

BOLA/IDOR ocorre quando referências a objetos permitem acesso sem autorização adequada. ID imprevisível pode reduzir descoberta, mas não substitui o controle. Testar troca de identificadores e chamadas diretas, conforme a seção O.

**Rastreabilidade externa seletiva:** o ASVS 5.0.0 exige verificação de acesso por função em `v5.0.0-8.2.1`, por objeto em `v5.0.0-8.2.2` e aplicação das regras em camada confiável em `v5.0.0-8.3.1`. Esses controles foram verificados no [capítulo V8](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x17-V8-Authorization.md); citá-los não demonstra implementação ou conformidade do produto.

## E. Cadastro, convite e gestão de contas

Definir quem pode criar conta, como a identidade é vinculada e quais concessões iniciais são permitidas. Não exigir registro público em sistema administrado internamente.

| Fluxo, quando existente | Controle operacional |
| --- | --- |
| Registro público | Validar entradas, limitar automação relevante e impedir escolha de papel privilegiado/tenant não autorizado. Definir estado inicial e condições de ativação. |
| Cadastro administrativo | Autorizar o operador para criar conta e atribuir apenas papéis que possa conceder; impedir uso de campos ocultos/editáveis para elevar privilégio. |
| Convite | Vincular convite a destinatário, organização e concessões aprovadas; usar código/token imprevisível, validade definida, uso único e revogação. Consumo concorrente não pode duplicar acesso. |
| Verificação de contato | Exigir quando contato sustentar recuperação, comunicação sensível ou requisito do produto. Confirmar controle do canal não comprova identidade civil, cargo ou elegibilidade. |
| Ativação/desativação | Aplicar transição autorizada e efetiva no acesso; desativar deve impedir novas sessões e uso de acesso anteriormente concedido. |
| Mudança de papel | Validar autor, destinatário, escopo e papéis concedíveis; impedir autoelevação indevida e propagar alteração aos controles ativos. |
| Contas inativas | Definir revisão, suspensão ou encerramento por risco e política real, com comunicação e retenção pertinentes. Inatividade não autoriza exclusão arbitrária de dados. |

Não enviar senha permanente por convite nem manter contas/senhas padrão utilizáveis. Preferir ativação que permita ao titular estabelecer seu autenticador. Gestão administrativa não deve exigir que o operador conheça a senha do usuário. Fluxos excepcionais de suporte precisam de concessão, evidência e limites próprios.

## F. Autenticadores e credenciais

Escolher métodos conforme população, exposição, dados, recuperação e requisitos de garantia. Não impor senha, passkey, federação ou serviço de identidade a todos os produtos.

### Senhas e verificadores

Quando o produto verificar senhas, deve armazenar verificadores resistentes a ataques offline com salt e função apropriada de hashing de senhas. Não armazenar senha em texto puro, usar criptografia reversível como substituto nem usar hash rápido isolado como verificador. Proteger cópias, logs e backups do verificador. Quando houver rede, solicitar e transmitir credenciais por canal autenticado e protegido, validando a identidade do destino; não desabilitar validação de certificado para contornar falhas de TLS.

**Recomendação de engenharia:** usar biblioteca consolidada da plataforma. Considerar Argon2id para novos verificadores quando compatível; alternativas como scrypt ou PBKDF2 dependem de suporte e requisitos específicos. Avaliar bcrypt existente como legado, incluindo limites de entrada. Definir parâmetros conforme recomendações verificadas e medição no ambiente alvo; registrar algoritmo, versão, salt e custo necessários à verificação/atualização. Não atribuir aprovação NIST automática a um algoritmo. Referência adicional: [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).

**Requisitos externos distintos, verificados:**

| Referência | Política de comprimento expressa |
| --- | --- |
| NIST SP 800-63B-4, seção 3.1.1.2 | Exige mínimo de 15 caracteres para senha como fator único; permite mínimo de oito quando a senha for usada somente como parte de MFA. Recomenda permitir comprimento máximo de pelo menos 64 caracteres. |
| ASVS 5.0.0, `v5.0.0-6.2.1` e `v5.0.0-6.2.9` | O primeiro controle, nível 1, exige ao menos oito e recomenda fortemente quinze; o segundo, nível 2, exige permitir ao menos 64. Não são os mesmos requisitos do NIST. |

Fontes: [NIST, verificadores de senha](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/) e [ASVS V6](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x15-V6-Authentication.md). Esses parâmetros pertencem aos perfis de referência, não são impostos indiscriminadamente a autenticadores locais de ativação ou sistemas legados por este Standard.

**Decisão interna:** documentar limites de senha e sua justificativa antes de implementar. Recomenda-se usar o perfil NIST acima como referência de engenharia para novos fluxos de senha online, avaliando compatibilidade e risco. Não reduzir requisito externo contratado por conveniência; exceção interna não comprova atendimento desse perfil.

Não impor mistura artificial de classes de caracteres nem troca periódica indiscriminada. Exigir troca diante de evidência de comprometimento e tratar eventual política externa aplicável explicitamente. Verificar senhas comuns/comprometidas no estabelecimento ou troca com mecanismo que não divulgue o secret; não enviar a senha integral a serviço de consulta. Não truncar silenciosamente. Permitir gerenciadores e entrada compatível, conforme a seção N. O NIST expressa proibição de composição artificial e troca periódica, além de consulta a lista de valores comuns/comprometidos, na [seção 3.1.1.2](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/).

### Outros métodos, quando adotados

| Método | Critérios operacionais |
| --- | --- |
| Passkeys | Avaliar suporte, vínculo ao serviço/conta, registro, perda, sincronização e recuperação. Verificar características do autenticador; o rótulo passkey não comprova sozinho MFA ou um nível de garantia. |
| Federação | Validar asserção/token e vínculo à transação conforme o protocolo e a documentação oficial adotados, incluindo origem confiável, destinatário, validade e integridade. Mapear identidade externa e permissões locais de forma explícita; não confiar em atributos editáveis. |
| Credenciais de serviço | Usar identidade própria, escopo mínimo, separação de ambientes, responsável, armazenamento protegido e revogação/rotação conforme risco. Não reutilizar conta humana nem distribuir secret compartilhado irrestrito. |
| Credencial comprometida | Suspender ou revogar acesso e recuperar de forma autorizada; identificar sessões/tokens relacionados e registrar resposta sem reproduzir o secret. |

Biometria, quando usada, deve seguir as garantias da plataforma e do método, com minimização de dados. Não criar verificador criptográfico ou protocolo próprio por conveniência. Credenciais que um cliente local precisar utilizar devem aproveitar proteção disponível da plataforma, sem alegar que um secret embutido em binário é confidencial.

## G. Login e proteção contra ataques

Definir defesa para cada caminho de login e recuperação, considerando credential stuffing, brute force, automação e enumeração. Caminho alternativo não pode contornar os controles principais.

- Aplicar rate limiting e resposta adaptativa proporcionais a conta, origem, serviço e risco, combinando sinais quando necessário. Documentar limites, janela, recuperação e consequências; IP isolado não cobre ataque distribuído e pode atingir usuários em rede compartilhada.
- Evitar bloqueio permanente acionável por terceiro. Usar atraso, desafio, restrição temporária ou outro mecanismo justificado, com retomada legítima e teste de negação de serviço contra a conta.
- Evitar revelar existência de conta por mensagem, código de resposta, conteúdo ou diferença observável de fluxo/tempo quando isso expuser risco. Dar orientação útil sem divulgar motivo sensível a público não autenticado.
- Validar entradas e reduzir consumo antes de trabalho custoso quando viável; não enfraquecer verificadores ou tratamento seguro de erros para aumentar throughput.
- Registrar sinais suspeitos com minimização, conforme seção M. CAPTCHA pode complementar, mas não é defesa exclusiva e deve ter alternativa acessível.

**Rastreabilidade externa:** `v5.0.0-6.1.1` e `v5.0.0-6.3.1` relacionam documentação e aplicação de controles contra ataques, incluindo prevenção de bloqueio malicioso de contas, no [ASVS V6](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x15-V6-Authentication.md). Os valores operacionais devem resultar do contexto, não de números atribuídos sem verificação.

## H. MFA e autenticação reforçada

Avaliar MFA por identidade e operação: exposição pública, privilégios administrativos, sensibilidade, consequências de tomada de conta e meios de recuperação. Não exigir MFA universal sem essa avaliação.

| Situação | Decisão de proteção |
| --- | --- |
| Administração de alto impacto | Exigir MFA adequado ou controle compensatório formalmente justificado/aprovado conforme risco; não aceitar acesso privilegiado apenas por localização de rede. |
| Alteração de contato, autenticador ou recuperação | Exigir reautenticação suficiente e verificar segurança do novo vínculo; proteção precisa ser efetiva antes da mudança. |
| Exportação ampla, operação irreversível ou dado altamente sensível | Avaliar autenticação recente e step-up, além de autorização da ação. Confirmação visual não basta. |
| Indício de conta/sessão comprometida | Aplicar desafio, restrição ou revogação conforme o plano autorizado, evitando liberar acesso sob dúvida material. |
| Recuperação de MFA | Aplicar fluxo de garantia apropriada da seção K; não permitir simples reset de senha para remover o fator. |

Reautenticação confirma novamente a identidade; step-up aumenta a garantia exigida para o contexto. Dois segredos do mesmo tipo não constituem automaticamente fatores distintos. Recomenda-se mecanismo resistente a phishing quando o risco justificar, especialmente em operações privilegiadas.

**Requisito externo condicional:** no perfil NIST AAL2, exige-se prova de dois fatores distintos e oferta de opção resistente a phishing; no AAL3, há exigência de resistência a phishing e chave não exportável. Fonte: [NIST SP 800-63B-4, seção 2](https://pages.nist.gov/800-63-4/sp800-63b/aal/). Não alegar AAL por selecionar MFA sem verificar as demais condições do perfil, inclusive recuperação e sessão.

## I. Sessões, cookies e tokens

Escolher o modelo existente ou a menor solução suficiente. Não impor JWT, sessão distribuída, armazenamento central ou federação. Documentar criação, limites, renovação, revogação, sessões concorrentes e efeitos das mudanças de conta/permissão.

| Evento ou mecanismo | Controle esperado |
| --- | --- |
| Criação | Emitir sessão após autenticação válida; usar identificador imprevisível quando opaco e verificação no componente confiável. Não aceitar identificador arbitrário fornecido pelo cliente como sessão autenticada. |
| Fixação e rotação | Gerar novo identificador/token após autenticação e reautenticação, invalidando o anterior; avaliar elevação de privilégio e outras transições. Tratar concorrência sem manter caminho de acesso indevido. |
| Expiração | Definir duração absoluta e inatividade conforme risco/perfil; aplicar limites no componente confiável. Expiração do cookie ou aviso na UI não garante término da sessão. |
| Renovação | Validar sessão, conta, permissões e condições do contrato; renovação silenciosa não pode prolongar acesso além de limite que exija nova autenticação. |
| Revogação | Invalidar acesso por compromisso, desativação, encerramento ou decisão autorizada. Definir propagação e verificar efeito real em sessões/tokens já emitidos. |
| Logout | Encerrar a sessão no componente responsável e limpar estado pertinente do cliente; nova chamada com a sessão encerrada deve ser rejeitada. Distinguir logout local, outras sessões e sessão do provedor federado. |
| Armazenamento | Evitar localização exposta a scripts, logs, URLs, histórico ou sincronização indevida; justificar arquitetura e controles do cliente. Não tratar localStorage como armazenamento seguro de secret. |

**Referências:** o ASVS `v5.0.0-7.2.4` verifica novo token após autenticação/reautenticação; `v5.0.0-7.4.1` verifica impedimento de uso após término e `v5.0.0-7.4.2` término das sessões em conta desativada/excluída. Fonte: [ASVS V7](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x16-V7-Session-Management.md). O NIST distingue limites de sessão e validade de tokens de acesso na [seção 5](https://pages.nist.gov/800-63-4/sp800-63b/session/). Não supor que sair da tela ou do provedor revoga todos os acessos.

### Cookies e CSRF, quando houver browser

Para cookie de sessão, usar `Secure` em transporte HTTPS e `HttpOnly` quando o valor não precisar ser acessível a scripts. Selecionar `SameSite` conforme fluxo, especialmente em federação ou uso entre sites; limitar domínio e caminho ao necessário. Se `SameSite=None` for necessário, manter transporte seguro e proteção apropriada. Validar configuração real no browser e componente confiável. Fonte de critérios: [ASVS V3, seção 3.3](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x12-V3-Web-Frontend-Security.md).

Quando o navegador enviar credenciais automaticamente, avaliar CSRF em ações sensíveis, inclusive caminhos de autenticação. Usar defesa verificada compatível, como token antifalsificação ou validação de origem/cabeçalhos com garantias apropriadas; não confiar somente no botão ou em SameSite. CORS não é autorização, e permitir leitura entre origens não prova proteção contra requisição forjada. Para API sem credenciais enviadas automaticamente, justificar a análise de CSRF; não aplicar controles de browser a integração puramente service-to-service.

### Tokens de acesso/atualização e JWT, quando adotados

Separar finalidade de token de acesso, atualização e sessão. Restringir escopo, destinatário, duração e uso; proteger token de atualização e definir revogação. Avaliar rotação e detecção de reutilização conforme modelo, incluindo concorrência legítima. Token inválido, expirado ou revogado não pode renovar acesso.

Para JWT, validar assinatura ou MAC com chave confiável e algoritmos permitidos, rejeitando algoritmo não autorizado e `none`. Verificar emissor, audiência, tipo/finalidade, validade e condições temporais exigidas pelo contrato antes de aceitar claims. Não obter chaves de fonte arbitrária indicada pelo próprio token nem usar mera decodificação como validação. Referência técnica: [ASVS V9](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x18-V9-Self-contained-Tokens.md).

Definir como revogação, logout e mudança de permissão alcançam tokens autocontidos: expiração isolada não garante revogação imediata. Se o contrato exigir término imediato, escolher mecanismo que o realize; registrar limitações e riscos, sem apresentar token ainda aceito como sessão encerrada. Claims de papel não podem manter privilégios obsoletos indefinidamente. Não impor JWT a produtos cuja sessão simples já satisfaça os requisitos.

## J. Autorização em APIs e operações empresariais

Aplicar a decisão da seção D a todos os caminhos protegidos, incluindo API, jobs e serviços que operem em nome de usuários. RBAC pode expressar concessões por papel; ABAC pode considerar atributos de sujeito, recurso e contexto quando necessário. Não impor ambos nem uma hierarquia universal.

| Superfície | Controle verificável |
| --- | --- |
| Registros e campos | Validar acesso de leitura/escrita a registro e propriedades permitidas; filtrar campos retornados e rejeitar atributos protegidos recebidos. |
| Multitenant | Validar vínculo e contexto; restringir consultas, mutações, cache, índices, arquivos e resultados ao tenant autorizado. Troca de contexto requer nova avaliação de acesso. |
| Operações administrativas | Exigir concessão específica, autenticação reforçada conforme H e evidência proporcional. Privilégio técnico não significa permissão de negócio irrestrita. |
| Importação | Autorizar função, destino e registros; validar conteúdo e escopo por item. Não aceitar papel/tenant arbitrário vindo de planilha ou payload. |
| Exportação | Autorizar dados, campos, volume e destino; proteger artefato e download resultante. Job assíncrono deve respeitar permissões ao executar e disponibilizar resultado. |
| Arquivos/anexos | Autorizar upload, listagem, leitura, alteração e download; identificador/caminho não substitui permissão. Acesso por URL deve manter proteção adequada ao risco. |
| Delegação para serviço | Preservar o sujeito/contexto autorizado; credencial técnica ampla não pode elevar acesso do usuário que iniciou a operação. |
| IDs e escopos recebidos | Validar forma, existência e relação autorizada; não aceitar roles, dono ou tenant apenas porque vieram assinados pelo cliente ou ocultos no formulário. |

Verificar autorização antes de retornar dados ou realizar efeitos. Mudança de permissão precisa alcançar requisições, sessões e operações pendentes conforme contrato; definir prevenção de condições de corrida em ações críticas. Usar transação ou verificação junto à operação quando a integridade exigir, sem impor tecnologia universal.

Controles de UI orientam a experiência, mas não substituem backend. Testar acesso direto a endpoints, métodos alternativos, recursos relacionados e arquivos; recurso não autorizado não pode vazar em erro, contagem, busca ou exportação. Não alegar isolamento por testar apenas um menu oculto.

## K. Recuperação de acesso e ciclo de vida

O fluxo de recuperação deve preservar o grau de confiança definido e não oferecer um desvio trivial do método principal. Documentar recuperação de senha separadamente de perda de MFA, troca de contato e encerramento.

| Etapa ou evento | Regra operacional |
| --- | --- |
| Solicitação | Responder sem enumeração indevida e limitar automação/envios. Solicitação isolada não deve mudar credenciais, bloquear a conta ou encerrar sessão legítima. |
| Código/token emitido | Gerar de modo criptograficamente seguro, vincular a conta e finalidade, proteger armazenamento e transporte, definir validade curta apropriada e uso único. Invalidar após consumo; concorrência não pode permitir segundo uso. |
| Link de recuperação | Usar destino confiável configurado, sem confiar em host/cabeçalho arbitrário para gerar link; evitar vazamento do token em logs, analytics ou conteúdo de terceiros. |
| Troca de senha | Autorizar por autenticador atual ou fluxo de recuperação válido; aplicar política de senha. Não conceder sessão privilegiada automaticamente pelo pedido de reset. |
| Sessões após recuperação | Revogar acessos potencialmente comprometidos e aplicar a política documentada; definir opção/necessidade de encerrar outras sessões conforme risco. Em compromisso confirmado, não manter acesso suspeito por conveniência. |
| Contato ou autenticador | Reautenticar conforme H, verificar o novo vínculo e comunicar mudança por canal previamente confiável quando pertinente, sem aceitar atributo autoatribuído como prova. |
| Recuperação de MFA | Usar autenticador alternativo, código de recuperação ou suporte com prova apropriada e auditável. Não remover MFA somente porque um email foi recebido ou uma senha foi trocada. |
| Desativação/encerramento | Invalidar acesso e vínculos pertinentes, tratar credenciais técnicas associadas e preservar/excluir dados conforme política autorizada. Reativação exige decisão apropriada, não reutilização automática de convite antigo. |

Não usar perguntas de segurança ou informações públicas como prova suficiente. Não divulgar senha anterior nem permitir a administrador estabelecer senha permanente conhecida por ele. Limitar privilégios do suporte e oferecer canal seguro para contestar evento suspeito.

**Referência de engenharia adicional:** [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) recomenda respostas consistentes, proteção contra automação e tokens imprevisíveis, protegidos, expirantes e de uso único. **Requisito externo condicional:** o NIST distingue métodos de recuperação e suas exigências conforme garantia e prevê notificação em recuperação, na [seção 4](https://pages.nist.gov/800-63-4/sp800-63b/events/). Não afirmar atendimento de AAL elevado por um link de email isolado; verificar o fluxo completo do perfil escolhido.

## L. Proteção das operações e dados

Complementar o baseline do Product System nas operações de identidade/acesso. A tabela apresenta decisões internas condicionais às superfícies reais, sem pretender catálogo completo de ameaças. O [Standard 07](ai-assisted-secure-development-threat-v1.md) aprofunda ameaças do processo de desenvolvimento assistido por IA.

| Ameaça/superfície | Controle e condição de verificação |
| --- | --- |
| XSS | Codificar saída pelo contexto, renderizar texto como texto e sanitizar HTML quando necessário. Evitar execução de conteúdo não confiável; avaliar CSP como defesa adicional em web. HttpOnly não impede toda ação indevida de script. |
| CSRF | Quando credenciais forem enviadas automaticamente, validar defesa antifalsificação no componente confiável, conforme I; confirmação visual não comprova origem da requisição. |
| SQL Injection | Parametrizar consultas e validar parâmetros estruturais permitidos. ORM não elimina risco de construção insegura de consulta. |
| Injeção de comandos | Evitar shell quando possível; usar API/argumentos seguros e restringir comando, caminho e permissões. Não concatenar entrada não confiável. |
| Mass assignment | Permitir somente campos editáveis; dono, tenant, papel e propriedades privilegiadas devem derivar de decisão confiável. |
| Upload inseguro | Autorizar usuário/destino, limitar tamanho/tipo conforme necessidade, verificar conteúdo pertinente e impedir execução/acesso público indevidos. Não confiar apenas em extensão ou tipo declarado. Avaliar análise adicional conforme risco. |
| Manipulação de identificadores | Verificar ação e recurso, inclusive anexos e caminhos, antes do efeito ou retorno; aplicar isolamento em todas as relações relevantes. |
| Exposição de dados | Minimizar respostas, erros, cache, URLs, downloads e telemetria; proteger trânsito e armazenamento conforme classificação. Não enviar dado proibido para depois ocultá-lo. |
| Falha de integração | Validar origem, contrato, integridade e autorização; tratar timeout, repetição e resultado incerto sem duplicar efeitos ou liberar acesso por falha do provedor. |
| Abuso de recursos | Definir limites de entrada, volume, concorrência e consumo conforme risco; medir controles e falhas pertinentes, sem impor valores universais. |

Classificar dados e avaliar requisitos legais aplicáveis com o responsável, sem alegar conformidade automática. Não copiar dados pessoais de produção para testes nem imprimir secrets durante inspeção. Conteúdo externo ou de IA não concede permissões de acesso ou execução.

## M. Logs, auditoria e resposta

Definir eventos necessários à detecção, investigação e rastreabilidade. Profundidade deve refletir exposição, sensibilidade e criticidade; projeto simples não exige SIEM ou plataforma complexa.

| Evento pertinente | Informação mínima útil |
| --- | --- |
| Autenticação e tentativa suspeita | Data/hora, referência segura de sujeito/fluxo, resultado e sinal de risco necessário. |
| Negação de autorização | Ação, recurso referenciado de forma segura, contexto autorizado e resultado; evitar payload ou dado protegido. |
| Privilégios e administração | Operador, alvo, mudança concedida/revogada, escopo e decisão, quando auditabilidade for necessária. |
| Recuperação e autenticadores | Solicitação/consumo, vínculo removido/adicionado e resultado, sem códigos/tokens. |
| Revogação e incidente | Motivo seguro, acessos afetados, medidas autorizadas e estado de recuperação. |

Não registrar senhas, tokens completos, cookies de sessão, secrets, códigos de recuperação ou dados pessoais desnecessários. Usar referências técnicas seguras para correlacionar eventos. Proteger contra log injection, acesso indevido, alteração e exclusão não autorizada; definir retenção, acesso e capacidade de recuperação conforme risco. Monitorar falha do registro sem divulgar dados ou liberar operação protegida.

Diante de incidente, identificar evidência e alcance, preservar informação necessária em local autorizado, notificar o responsável pelos canais aprovados e propor contenção/recuperação. Não alterar credenciais, destruir dados ou acessar produção sem autorização correspondente. Rotação/revogação necessária deve ter responsável e verificação de efeito. Não tratar suspeita como prova conclusiva nem alegar scanner/teste que não foi executado.

## N. Experiência segura e acessível

Aplicar os critérios do Web Experience às jornadas de identidade e operações sensíveis. Segurança não deve criar barreiras de uso sem benefício justificado.

- Formular login com rótulos, nomes acessíveis, teclado/foco e orientação clara. Permitir gerenciadores, preenchimento automático e colagem; não exigir memorização ou transcrição artificial sem alternativa adequada.
- Mascarar senha por padrão e oferecer visualização temporária acessível quando pertinente. Não expor valor em mensagens ou estado compartilhado.
- Dar mensagem útil sem enumerar contas ou revelar informações internas. Diferenciar erro de campo e falha de serviço quando seguro.
- Comunicar expiração de sessão e caminho de retomada; preservar trabalho somente onde for seguro, sem persistir automaticamente dados sensíveis no cliente.
- Explicar recuperação, fatores aceitos, alternativa acessível e forma de contestar mudança. CAPTCHA não pode ser único caminho disponível.
- Em operação sensível, mostrar alvo, alcance e consequência e pedir confirmação/reautenticação conforme risco. Não apresentar dark patterns, consentimento enganoso ou urgência artificial.
- Após logout ou troca de contexto, remover dados visíveis e impedir exposição residual em navegação/cache conforme arquitetura e sensibilidade. Conferir comportamento real, inclusive em dispositivo compartilhado.

Verificar UI renderizada e jornadas pertinentes conforme Standard 02, sem alegar conformidade de acessibilidade apenas pela presença de atributos. Segurança no frontend acompanha a decisão confiável; não substitui autorização. Referência externa de usabilidade de senha: o NIST exige suporte a gerenciadores/autofill e recomenda permitir colagem na [seção 3.1.1.2](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/).

## O. Testes e Security Gate

Planejar cenários por controle, superfície e ameaça. Usar dados sintéticos ou autorizados, ambiente permitido e testes proporcionais; não executar ataque em produção ou contra serviço externo sem escopo correspondente.

| Cenário, quando pertinente | Evidência esperada |
| --- | --- |
| Login válido/inválido | Identidade correta acessa somente concessões previstas; credencial errada, conta desativada e fluxo alternativo não liberam acesso. |
| Sessão e fixação | Identificador anterior ao login não preserva acesso; expiração, renovação e reautenticação obedecem ao contrato no componente confiável. |
| Logout e revogação | Chamada direta com sessão encerrada é negada; outros tokens/sessões têm efeito documentado e verificado, incluindo federação quando adotada. |
| Recuperação | Pedido não enumera indevidamente nem altera conta sozinho; token expirado, alterado, de outra conta ou já usado é rejeitado. |
| Escalada horizontal/vertical | Trocar usuário, recurso, método ou função não permite acesso de outro sujeito ou privilégio reservado. |
| BOLA/IDOR e multitenant | Registro, anexos, consulta, mutação, cache e exportação permanecem no usuário/tenant permitido, inclusive com ID legítimo de outro contexto. |
| Administração e API direta | Operação administrativa sem concessão é negada mesmo fora da UI; erro e resposta não vazam o dado. |
| CSRF | Requisição de origem/credencial automaticamente enviada inadequadas não executa ação; fluxo legítimo continua funcional. |
| Rate limiting e automação | Limites funcionam sob tentativas relevantes; retomada legítima é possível e terceiro não bloqueia permanentemente a conta por simples repetição. |
| MFA e step-up | Fluxo incompleto, fator inválido ou reset de senha não substitui garantia exigida; operação sensível exige proteção definida. |
| Reutilização de tokens | Replay proibido e renovação com token inválido/revogado são rejeitados; rotação e concorrência seguem modelo documentado. |
| Concorrência/permissões | Convite/reset de uso único não tem duplo consumo; revogação e mudança de papel impedem operação indevida em sessão ou job existente conforme contrato. |
| Dados e entradas | Campos protegidos, upload, consulta, comando e saída não confiáveis são tratados nos caminhos afetados. |
| Regressão | Reproduzir defeito corrigido e rever controles/fluxos adjacentes, inclusive caminho legítimo e recuperação de erro. |

### Decisão do Security Gate

O revisor deve relacionar controles aplicáveis a implementação/configuração efetivas e resultados reais. Reunir escopo, riscos, regras de acesso, cenários executados, achados, correções, testes repetidos e limitações. Inspeção de código e teste têm alcances distintos; uma lista de controles selecionados não comprova funcionamento.

Registrar resultado de cada verificação importante conforme o Product System: `PASS`, `FAIL`, `BLOCKED` ou `NOT RUN` para testes. `NOT_APPLICABLE` justifica somente superfície inexistente. Nunca marcar `PASS` para teste não executado. Ambiente indisponível é blocker com impacto, não inaplicabilidade. Usar o registro existente e autorizado; não criar log obrigatório novo.

| Parecer | Condição e próxima ação |
| --- | --- |
| APPROVED | Controles e critérios pertinentes atendidos, evidência essencial suficiente e nenhum achado material impeditivo no alcance examinado; apresentar Gate B, sem autorizar publicação. |
| CHANGES_REQUIRED | Defeito, controle ausente, regressão ou evidência insuficiente corrigível no Gate A; corrigir e repetir verificações afetadas. |
| BLOCKED | Decisão, autorização, credencial, ambiente ou condição externa impede avanço seguro; registrar causa e parar a ação afetada. |

Falhas críticas conhecidas de autenticação, autorização, secrets ou injeção bloqueiam release. Validação essencial ausente impede aprovação geral. Conter e corrigir somente dentro da autorização existente, sem contornar controle ou enfraquecer teste.

Identificar autor e revisor. Preferir revisão realmente independente quando disponível e autorizada; na revisão feita pelo executor, declarar **autorrevisão** e limitações. Outra Skill ou etapa não cria independência. Se revisão independente for critério obrigatório, sua ausência impede prontidão.

### Exemplos práticos de aplicação

Os exemplos delimitam cenários, escolhas e verificações possíveis. Não constituem resultados executados, arquitetura fictícia obrigatória ou prova de segurança de um sistema real.

#### 1. Website público sem login

**Contexto:** conteúdo deliberadamente público, sem conta nem área protegida. **Escolha:** não criar cadastro, MFA ou sessão autenticada. Avaliar integridade da publicação, conteúdo não confiável, exposição e abuso de formulário se existir. **Verificação:** confirmar que apenas conteúdo autorizado é público e que nenhum secret foi distribuído; testar formulário somente quando presente. **Inaplicável nesse cenário:** recuperação de conta, BOLA de registros privados e revogação de sessão de usuário. Administração da hospedagem continua sujeita aos controles de suas identidades, se entrar no escopo.

#### 2. Área de pacientes e administrador

**Contexto:** pacientes consultam seus registros; administrador executa tarefas concedidas. **Escolha:** autorização por ação/recurso, recuperação protegida, sessões revogáveis e avaliação de MFA/step-up para operações de alto impacto. Administração técnica não concede automaticamente acesso a todo dado sensível. **Verificação:** paciente não lê registro/anexo de outro paciente por ID; conta sem concessão não exporta dados; logout/desativação impedem acesso. **Inaplicável sem requisito:** cadastro público e livre atribuição de papel. Testar com dados sintéticos.

#### 3. Sistema empresarial com gerentes e colaboradores

**Contexto:** equipes e ações de gestão definidas pelo negócio. **Escolha:** papéis ou atributos expressam concessões reais; gestor só atua nos recursos autorizados, com conta individual e mudança de papel controlada. **Verificação:** colaborador não promove a própria conta; gerente sem vínculo não consulta outra equipe; redução de privilégio alcança operações ativas conforme contrato. **Inaplicável sem necessidade:** hierarquia universal, federação obrigatória ou MFA para toda ação rotineira. Avaliar MFA nas concessões de alto impacto.

#### 4. API multitenant com BOLA/IDOR

**Contexto:** consumidor autenticado troca ID para acessar registro de outra organização. **Escolha:** validar ação, objeto e vínculo de tenant no componente confiável e nos caminhos de dados; identificação imprevisível não é correção suficiente. **Verificação:** leitura, edição, busca, anexos e exportação de outro tenant são negadas por chamada direta; fluxo autorizado continua funcional. **Inaplicável sem browser:** defesa por cookie/CSRF de sessão web. JWT não é obrigatório. Falha crítica conhecida bloqueia release enquanto não corrigida e validada.

#### 5. Aplicação local/desktop

**Contexto:** uso individual em dispositivo gerenciado, com arquivos locais e sem serviço remoto. **Escolha:** avaliar identidade/permissões do sistema operacional, exposição dos arquivos e necessidade real de login próprio; usar proteção da plataforma e acesso mínimo. **Verificação:** arquivos e operações ficam restritos conforme modelo local; nenhuma credencial é embutida no artefato; UI não expõe informação residual. **Inaplicável nesse contexto:** cookies web, JWT, multitenancy e servidor de identidade obrigatório. Não prometer proteção contra quem controla administrativamente o dispositivo. Integração remota exige reavaliação.

#### 6. Integração service-to-service

**Contexto:** serviço importa registros de organização autorizada. **Escolha:** identidade técnica por consumidor/ambiente, credencial protegida, autorização por operação/tenant, transporte confiável e falhas/retries controlados. Definir revogação e efeito sobre chamadas pendentes. **Verificação:** credencial revogada ou de outro ambiente não opera; tentativa fora do escopo é negada; repetição não duplica efeito material. **Inaplicável sem usuário/browser:** formulário de login, CAPTCHA, cookie de sessão e MFA interativo em toda chamada. Método técnico, como certificado ou token, depende da arquitetura aprovada.

## P. Definition of Ready e Definition of Done

### Definition of Ready

Antes da implementação dependente, devem estar suficientemente definidos:

- Identidades, vínculos e permissões por ação/recurso relevantes, com limites de confiança identificados.
- Requisitos de autenticação, garantia, sessão, recuperação e ciclo de contas na superfície alterada.
- Dados, exposição, ameaças e restrições reais; decisão sobre MFA/step-up quando pertinente.
- Contratos, stack, componentes confiáveis e critérios de aceitação, com controles/testes previstos e ambientes autorizados.

Não exigir programa completo de IAM para correção delimitada. Lacuna material bloqueia a ação dependente; atividade independente autorizada pode continuar. Inaplicabilidade, como sessão autenticada em página pública sem login, deve ser justificada proporcionalmente.

### Definition of Done da superfície de segurança

| Condição | Evidência necessária |
| --- | --- |
| Implementação validada | Controle efetivo examinado no componente responsável, incluindo configuração e contratos afetados. |
| Testes pertinentes | Positivos, negativos, abuso e regressão essenciais executados e aceitos; ausência/falha permanece pendente. |
| Security Review | Revisão sobre alteração final, com achados tratados, Security Gate e independência/autorrevisão identificados. |
| Riscos residuais | Limitações, exceções e decisões relevantes registradas no contexto autorizado, com impacto e responsável quando necessário. |
| Gate B preparado | Resultado, alcance, evidências e ações protegidas propostas apresentados ao responsável, sem executar publicação por conta própria. |

Cumprir também a Definition of Done do Product System e do Web Experience quando aplicável. Aprovação de login não comprova autorização, integridade, acessibilidade ou prontidão operacional de toda a aplicação.

Revisão documental deste Standard verifica texto, fontes, coerência e escopo. Não audita sistema real, não executa os cenários exemplificados e não comprova implementação dos controles. Aplicação operacional exige testes controlados posteriores do projeto, conforme o escopo autorizado.

## Q. Exceções, Capability Routing e evolução

### Seleção de capacidades

Usar o Standard 03 para selecionar o menor conjunto suficiente e consultar instruções completas das Skills aplicadas. A tabela não impõe pacote obrigatório nem múltiplos agentes.

| Skill canônica | Selecionar quando |
| --- | --- |
| [vera-architecture-security](../.agents/skills/vera-architecture-security/SKILL.md) | Identidade, autorização, dados sensíveis, integração, confiança ou revisão especializada de segurança forem afetados. |
| [quality-engineering-testing](../.agents/skills/quality-engineering-testing/SKILL.md) | Planejar/executar testes funcionais, negativos, abuso, contratos ou regressão da superfície. |
| [software-design-solid](../.agents/skills/software-design-solid/SKILL.md) | Implementar/revisar lógica, serviços, APIs e responsabilidades de código; não exigir em análise puramente documental. |
| [data-persistence-engineering](../.agents/skills/data-persistence-engineering/SKILL.md) | Dados de contas, permissões, sessões ou recuperação afetarem modelo, consulta, transação, concorrência ou persistência. |
| [kael-interface-engineering](../.agents/skills/kael-interface-engineering/SKILL.md) | Implementar/corrigir UI de autenticação, estados, interação ou acessibilidade; não exigir para backend sem UI. |
| [release-deployment-reliability](../.agents/skills/release-deployment-reliability/SKILL.md) | Preparar artefato, configuração, distribuição, recuperação ou verificação operacional; preparação não autoriza deploy. |

Outras Skills entram somente diante de condição pertinente, como Visual QA para mudança visual relevante ou AI Engineering para componente efetivo de IA. Inspecionar uma Skill para complementaridade documental não ativa sua execução especializada.

Ampliar roteamento quando surgirem autenticação/autorizações novas, dados sensíveis, persistência, serviços externos, comandos/ferramentas, vulnerabilidade, risco de isolamento, mudança de UI ou preparação de release. Segurança crítica prevalece sobre economia de contexto. Mudança material fora do Gate A exige decisão humana antes da ação afetada.

### Exceções e evidências

Adaptar profundidade de avaliação, documentação e testes ao risco. Controle sem superfície pode ser inaplicável; impossibilidade de executá-lo não comprova inaplicabilidade. Não dispensar autorização confiável, proteção de secrets, integridade e validação essencial para acelerar entrega.

Registrar exceção relevante com regra, motivo, alcance, risco, controle compensatório, responsável e condição de reavaliação. Obter aprovação humana quando modificar segurança material, requisito contratado, governança ou decisão aprovada; simplificação rotineira no Gate A não exige microaprovação. Exceção interna não altera norma externa nem comprova conformidade; também não libera release com falha crítica conhecida.

Preferir o contexto e relatório existentes, com fatos observados separados de inferências/recomendações. Não criar arquivo de log por tarefa, copiar secrets ou inventar evidência, auditoria independente ou conformidade.

### Relação com Standards especializados e evolução

Na autoria inicial, os Standards 05 e 07 ainda não estavam materializados. Hoje, [Environment Variables & Secrets](environment-variables-secrets-v1.md) detalha configuração e segredos, e [AI-Assisted Secure Development Threat](ai-assisted-secure-development-threat-v1.md), Candidate, trata das ameaças do desenvolvimento assistido por IA. Consultar essas fontes conforme a superfície, preservando o baseline e seus estados documentais.

Inspecionar inventário real ao retomar. Referências históricas não suspendem controles atuais. Atualizar referências e roteamento somente mediante revisão autorizada dos arquivos envolvidos; a criação inicial deste Standard não autorizava modificar as demais fontes.

Revisar diante de achado operacional, conflito, mudança de referência técnica ou nova superfície comprovada. Identificar regra, fonte, evidência, impacto e transição; testar procedimentos quando pertinente e distinguir validação documental de operacional. Seguir o versionamento do Product System: maior para incompatibilidade de governança, menor para regra operacional compatível e corretiva para esclarecimento sem mudança de obrigação. Não mudar regras silenciosamente mantendo a identificação de versão.

| Versão | Estado | Registro |
| --- | --- | --- |
| 1.1 | Stable | Criação inicial neste repositório com a identificação autorizada v1.1; política proporcional de AuthN/AuthZ, sessões, recuperação, testes e Security Gate. Não pressupõe versão 1.0 anterior nem validação operacional já realizada. |

Recomenda-se revisão humana do conteúdo e, posteriormente, aplicação controlada em cenários representativos com evidências reais. Eventual atualização de catálogos/referências de outros documentos exige escopo próprio. Não iniciar outro Standard, implementação ou versionamento como consequência automática desta entrega.

Revisão corretiva 1.1.1 (13/10/2026): referências normativas sem versão fixa e consistência com a taxonomia de testes vigente, quando pertinente. Preserva Gates, responsabilidades e estado canônico. Ajuste documental autorizado na revisão final para publicação; não comprova nova validação operacional.
