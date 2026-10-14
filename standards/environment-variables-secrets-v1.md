# My Easy Development System Environment Variables & Secrets Standard v1.0.1

## A. Identificação e governança

| Campo | Definição |
| --- | --- |
| Nome oficial | My Easy Development System Environment Variables & Secrets Standard v1.0.1 |
| Identificador | Standard 05 |
| Versão | 1.0.1 |
| Estado canônico | Stable |
| Finalidade | Estabelecer regras operacionais para classificar, fornecer, utilizar e proteger configuração e segredos durante desenvolvimento, testes, build, integrações, distribuição e operação. |
| Aplicabilidade | Websites, aplicações web e empresariais, APIs, sistemas locais/desktop e integrações, conforme dados, exposição e arquitetura reais. |
| Independência técnica | Não determina linguagem, framework, plataforma, provedor, infraestrutura ou mecanismo universal de configuração. |

Stable identifica o estado canônico do documento. Não comprova validação operacional, segurança de um ambiente, conformidade externa ou aprovação humana de uma entrega.

**Escopo:** configuração pública e interna, credenciais técnicas, tokens temporários, material criptográfico e seus caminhos entre origem, armazenamento, consumidor e possíveis destinos de exposição. Avaliar também credenciais de desenvolvimento e entrega quando essas operações integrarem o escopo.

**Exclusões:** este Standard não cria gerenciador de segredos nem exige provedor específico. Não implementa scripts, hooks, servidores, automações, memória persistente, ai-memory ou MCP; não instala dependências nem altera arquitetura, infraestrutura ou pipelines. Sua adoção documental não autoriza ler valores de credenciais reais, alterar configuração, provisionar, rotacionar ou revogar credenciais, acessar produção ou publicar software.

### Fontes canônicas e autorização

Ler [AGENTS.md](../AGENTS.md) e as instruções aplicáveis. Este documento complementa:

| Fonte | Responsabilidade preservada |
| --- | --- |
| [Product System](product-system-v4.md), Standard 01 | Processo central, Gates A/B, autonomia, bloqueios, qualidade, revisão, evidências e evolução. |
| [Web Experience & Business Systems](web-experience-business-systems-v1.md), Standard 02 | Experiência, estados, erros seguros e proteção das informações nas interfaces web ou locais. |
| [Capability Routing Standard](capability-routing-v1.md), Standard 03 | Seleção e reavaliação do menor conjunto suficiente de capacidades. |
| [Authentication & Security Standard](authentication-security-v1.md), Standard 04 | Identidades, autenticação, autorização, credenciais de usuário, sessões, recuperação e Security Gate. |

As Skills canônicas de `.agents/skills/` fornecem procedimentos especializados conforme a seção P. Inspeção documental não equivale a ativar todas as Skills nem executar seus procedimentos.

Atuar autonomamente dentro do Gate A. Autorizações anteriores válidas permanecem suficientes dentro de seu alcance. Diante de mudança material de segurança/escopo, credencial ausente, uso de credenciais fora do alcance, produção não autorizada, custo novo ou ação irreversível, interromper a ação afetada e solicitar decisão humana conforme o Product System. Continuar atividades independentes autorizadas.

Preparação de artefato ou plano de rotação não autoriza sua execução. Merge, push a branch protegida, release e deploy seguem o Gate B. Operações Git exigem autorização correspondente; proibições explícitas da tarefa prevalecem. Resolver conflitos materiais antes da ação dependente, sem alterar outros documentos por consequência automática.

### Natureza das regras e referências verificadas

Salvo atribuição explícita, as regras deste documento são **decisões internas My Easy Development System**. **Deve** indica obrigação na superfície aplicável; **quando** delimita uma condição a avaliar; **recomenda-se** permite alternativa justificada. Recomendação técnica não é exigência legal. Requisito externo somente se aplica conforme o perfil, contrato ou política efetivamente adotados e verificados.

Referências consultadas em 2026-10-08:

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html): recomendações técnicas; consultadas seções de acesso, memória, auditoria, ciclo de vida, transporte, recuperação, CI/CD, detecção e incidentes. A consulta não incorpora todas as recomendações de infraestrutura ou automação.
- [OWASP ASVS 5.0.0](https://owasp.org/projects/asvs): referência para controles verificáveis, com consulta aos capítulos fixados [V13, configuração](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x22-V13-Configuration.md), [V11, criptografia](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x20-V11-Cryptography.md) e [V16, logs e erros](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x25-V16-Security-Logging-and-Error-Handling.md). Não se presume certificação nem atendimento integral de um nível.
- [The Twelve-Factor App, Config](https://12factor.net/config): método que separa configuração variável entre entregas do código e utiliza variáveis de ambiente. É referência de engenharia, não garantia de confidencialidade nem modelo obrigatório para todos os produtos.

Documentação oficial de Git, GitHub, Next.js, Vite e Docker é citada nas regras condicionais correspondentes. As fontes estavam acessíveis na autoria; a verificação foi seletiva. Revalidar comportamento para a versão e a configuração reais do projeto. Se uma fonte ficar indisponível, registrar a limitação e não atribuir a ela requisitos, suporte ou parâmetros não verificados. Exigência externa contratada não pode ser reduzida por exceção interna.

## B. Classificação da configuração

Classificar pelo conteúdo, finalidade, capacidade de acesso e destinatário autorizado, antes de definir armazenamento ou exposição. Uma variável de ambiente é um meio de fornecimento; não determina se o valor é público, interno ou secreto.

| Categoria | Exemplos sem valores reais | Tratamento e consequência de classificação incorreta |
| --- | --- | --- |
| Configuração pública | URL pública de API, nome exibido, identificador expressamente publicável pelo provedor. | Pode alcançar o cliente quando aprovado. Não deve conter privilégios ou dados confidenciais; classificá-la como secreta pode criar controles sem benefício. |
| Configuração interna não secreta | Nome interno de serviço, limite de conexões, endereço de componente privado. | Não concede acesso por si só, mas restringir divulgação conforme risco e arquitetura. Publicá-la indiscriminadamente pode revelar topologia ou facilitar abuso. |
| Configuração secreta | Senha técnica de banco, chave privilegiada de API, segredo de assinatura de webhook. | Restringir armazenamento, distribuição e uso; exposição pode permitir acesso, falsificação ou consumo indevido. |
| Credencial ou token temporário | Token de sessão, token de integração com expiração, credencial de job efêmero. | Proteger durante toda a validade, limitar escopo/destinatário e verificar expiração/revogação. Duração curta não torna o valor público. |
| Material criptográfico | Chave privada, chave simétrica, chave pública, certificado público. | Classificar os componentes separadamente: material privado/simétrico exige confidencialidade; parte pública pode ser divulgada, mantendo integridade e vínculo confiável. Vazamento ou troca indevida pode comprometer assinatura ou dados. |
| Dado pessoal ou confidencial que não é configuração | Cadastro, prontuário, documento de negócio, conteúdo de usuário. | Gerenciar como dado do domínio com finalidade, acesso e retenção próprios. Usar `.env` como depósito desses dados dificulta governança e pode ampliar exposição. |

Uma string de conexão com senha deve ser tratada como secreta inteira em diagnósticos e evidências. URL com token, cabeçalho de autenticação e arquivo composto também podem conter segredo, independentemente do nome.

Se a classificação estiver incerta, não publicar nem ampliar acesso; esclarecer contrato, permissões e fluxo. Um identificador publicável deve ter essa característica confirmada na documentação oficial e na configuração efetiva. Restringir origem ou domínio pode complementar um contrato, mas não transforma credencial privilegiada distribuída em segredo.

## C. Princípios de gestão de segredos

| Princípio | Regra operacional |
| --- | --- |
| Menor privilégio e necessidade de acesso | Conceder somente recursos, ações e duração necessários. Distinguir permissão de utilizar, ler, alterar e administrar o segredo. |
| Minimização | Reduzir quantidade de credenciais, cópias, consumidores e tempo de exposição. Não fornecer ao build, teste ou ferramenta segredo que não necessite. |
| Segregação | Separar credenciais e concessões por ambiente e consumidor quando pertinente; impedir alcance indevido sobre produção. |
| Ciclo de vida e revogabilidade | Definir responsável, finalidade, validade, renovação, rotação e mecanismo efetivo de invalidar acesso conforme contrato. |
| Rastreabilidade proporcional | Registrar metadados e decisões suficientes para localizar consumidor, responsável e evento, sem registrar o valor. |
| Armazenamento e transmissão protegidos | Restringir leitura/escrita, proteger cópias e usar canal autenticado e protegido na transmissão em rede. Avaliar criptografia em repouso conforme sensibilidade e ameaças. |
| Uso protegido | Limitar alcance do processo, ferramentas, herança para subprocessos, diagnóstico e retenção em memória conforme plataforma e risco. |
| Exemplos e testes seguros | Usar placeholders e marcadores sintéticos não funcionais em exemplos, documentação e fixtures. Nunca copiar credenciais reais como massa de teste. |

Preferir capacidades consolidadas já disponíveis na plataforma. Recomenda-se identidade técnica de duração limitada em vez de segredo estático amplo quando a integração suportar e o risco justificar. Não exigir serviço novo ou autenticação federada por padrão.

Variáveis de ambiente, arquivos e memória possuem limites: processos autorizados, depuradores, dumps ou administradores do dispositivo podem obter valores conforme a plataforma. Avaliar permissões e canais reais, sem prometer isolamento absoluto, limpeza garantida de memória ou segurança por renomear uma variável. Mascaramento e Base64 não substituem controle de acesso ou criptografia.

## D. Ciclo de vida

Usar o contexto e os mecanismos existentes para registrar, sem valor secreto: finalidade, classificação, responsável, consumidor, ambiente, permissões, origem autorizada, destino, forma de armazenamento e condição de renovação/revogação. Em projeto simples, um registro curto é suficiente; não criar inventário ou log separado obrigatório.

O responsável pelo serviço define necessidade, concessões e política; o operador autorizado provisiona, distribui, substitui e invalida credenciais; o executor integra configuração e verifica exposição dentro do escopo; o revisor examina controles e evidências. Papéis podem ser acumulados, com autorrevisão identificada. A responsabilidade atribuída não concede acesso fora da autorização.

| Etapa | Procedimento e condição verificável |
| --- | --- |
| 1. Identificação da necessidade | Confirmar operação, consumidor e privilégios; avaliar se configuração pública, identidade existente ou solução sem credencial atende. |
| 2. Criação ou provisionamento | Usar mecanismo consolidado do emissor/plataforma e geração apropriada à finalidade. Não criar credencial previsível, padrão reutilizável ou protocolo criptográfico próprio. |
| 3. Concessão de acesso | Identificar sujeito/processo autorizado, escopo, ambiente e duração. Revogar concessões quando vínculo ou necessidade terminarem. |
| 4. Armazenamento | Escolher mecanismo disponível com proteção suficiente, incluindo permissões, cópias e recuperação necessárias. Evitar chaves de decifragem acessíveis junto ao material protegido pelo mesmo caminho. |
| 5. Distribuição autorizada | Entregar apenas ao destinatário validado, por canal e mecanismo aprovados; evitar mensagem, arquivo compartilhado ou terminal como transporte informal. |
| 6. Utilização | Resolver no componente autorizado, verificar destino e limitar uso à operação. Não imprimir valor nem encaminhar a consumidor desnecessário. Evitar credencial técnica em URL; tokens em links exigidos pelo contrato seguem os controles específicos do Standard 04 e da seção K, com validade, escopo e prevenção de vazamento. |
| 7. Expiração e renovação | Definir validade conforme emissor, risco e disponibilidade. Verificar rejeição do acesso expirado e renovação autorizada; não assumir que apagar variável encerra a credencial. |
| 8. Rotação | Planejar substituição, consumidores afetados, propagação, testes e invalidação da versão anterior, com responsável e autorização. |
| 9. Revogação | Invalidar no componente que aceita a credencial; remover concessões e cópias desnecessárias de forma autorizada. Verificar o efeito real, incluindo acessos derivados quando pertinente. |
| 10. Exposição e encerramento | Acionar resposta da seção M; ao encerrar consumidor/ambiente, invalidar credenciais pertinentes e tratar retenção e recuperação necessárias. |

### Rotação planejada e emergencial

**Planejada:** frequência ou evento deve derivar de ameaça, requisitos de negócio, contrato e capacidades reais. Definir compatibilidade, atualização de consumidores, janela de transição, teste e retirada do acesso antigo. Não inventar intervalo universal.

**Emergencial:** exposição confirmada ou suspeita relevante exige avaliação e contenção prioritárias conforme seção M. Se houver risco de uso do segredo antigo, não manter sobreposição apenas por conveniência operacional. Registrar impacto de indisponibilidade e a decisão autorizada; não restaurar credencial comprometida como rollback.

Rotacionar uma credencial não prova revogação da anterior nem de tokens, sessões ou conexões já existentes. Ensaiar o efeito exigido pelo contrato em ambiente autorizado. Encerrar processo ou job também não invalida, por si só, acesso no emissor.

Chaves de cifragem exigem distinguir chave para novas escritas de material necessário à leitura/restauração de dados anteriores. Não destruir chave antes de avaliar dependências, backups, recuperação e retenção autorizadas. Credenciais de assinatura exigem avaliar validação de artefatos ou tokens anteriores e distribuição confiável das partes públicas. Não impor recifragem universal.

Senhas de usuários e recuperação continuam regidas pelo Standard 04. A política de rotação técnica não impõe troca periódica indiscriminada de senha humana. Operações sobre credenciais reais, inclusive testes de revogação, exigem autorização correspondente; este Standard não a fornece.

**Referência externa seletiva:** ASVS `v5.0.0-13.1.4` e `v5.0.0-13.3.4`, nível 3, tratam documentação, expiração e rotação; `v5.0.0-13.3.1`, nível 2 com condição adicional para nível 3, trata solução de gestão e exclusão de segredos do código/artefatos. Fonte: [V13 fixado](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x22-V13-Configuration.md). Esses requisitos não são incorporados integralmente nem tornam vault/HSM obrigatórios para qualquer projeto. Se um nível for contratado, verificar todas as suas condições antes de alegar atendimento.

## E. Ambientes separados

| Ambiente | Escolha e limite de acesso |
| --- | --- |
| Desenvolvimento local | Usar credencial específica, recursos de desenvolvimento e acesso restrito à necessidade. Evitar reutilizar credenciais de produção; eventual necessidade excepcional exige decisão humana, controles e escopo próprios. |
| Testes automatizados | Preferir dados sintéticos, mocks adequados ao contrato e credenciais de recursos de teste, provisionadas somente quando a integração exigir. Fixtures versionadas não devem conter credenciais funcionais. |
| Staging/homologação | Separar acessos e destinos de produção; controlar envio externo e dados. Similaridade funcional não justifica cópia de secrets ou dados pessoais produtivos. |
| Produção | Restringir concessões e intervenção aos responsáveis autorizados; validar configuração e recuperação sem imprimir valores. Acesso produtivo deve constar da autorização. |
| Ambientes efêmeros | Limitar credencial ao ambiente/job e prazo necessário; ao encerrar, verificar invalidação conforme emissor e limpar cópias autorizadas. |
| Integrações de terceiros | Separar consumidores e ambientes quando suportado; confirmar conta/projeto, escopo, destinatário, custo e ciclo de vida. Ausência de sandbox deve ser tratada explicitamente. |

Separação pode ocorrer por concessões, recursos ou contas já existentes. Projetos, serviços e infraestrutura adicionais somente quando o risco justificar e houver autorização. Nomes como `test` ou `staging` não garantem isolamento: verificar destino e permissões efetivos.

## F. Arquivos de ambiente

Arquivos `.env` são uma opção de fornecimento de configuração, não um mecanismo de segurança por si só. Não exigir sua criação quando a plataforma já fornecer mecanismo adequado. Verificar carregamento, precedência e destino conforme a tecnologia adotada; nomes iguais podem ter comportamentos diferentes entre ferramentas.

| Arquivo ou equivalente | Regra aplicável |
| --- | --- |
| `.env` | Classificar conteúdo e consumidores. Se contiver segredo real, mantê-lo fora do versionamento e dos destinos públicos; proteger acesso e cópias. Arquivo sem segredos ainda exige avaliação de informação interna. |
| `.env.local` | Tratar como configuração local conforme loader real; o sufixo não garante exclusão Git nem confidencialidade. Verificar regras existentes sem presumir comportamento automático. |
| `.env.example` | Usar somente placeholders não funcionais e exemplos públicos seguros. Documentar nome, finalidade, classificação, obrigatoriedade e origem esperada, sem dados internos desnecessários. |
| Arquivos equivalentes | Aplicar os mesmos controles a JSON, YAML, arquivos da plataforma ou outros formatos; extensão não determina proteção. |

**Exemplo exclusivamente documental:** `SERVICE_API_TOKEN=<PREENCHER_POR_MECANISMO_AUTORIZADO>` representa um placeholder, não credencial, valor padrão utilizável ou comando. A aplicação deve rejeitar placeholder em campo obrigatório. Não criar arquivos de configuração para reproduzir este exemplo.

`.gitignore` reduz inclusão acidental de arquivos não rastreados. Não protege histórico, arquivo já rastreado, inclusão forçada, cópias, backups, sincronização, processos ou acesso ao disco. O Git confirma que regras de ignore não afetam arquivos já rastreados: [documentação oficial de gitignore](https://git-scm.com/docs/gitignore).

Quando houver autorização para configurar um projeto, conferir regras efetivas, arquivos rastreados e artefatos de distribuição. Não excluir ou retirar arquivos do índice automaticamente. Nesta autoria documental, caminhos potencialmente sensíveis devem ser avaliados por existência e configuração conhecida, sem abrir, copiar ou imprimir valores.

## G. Variáveis públicas versus secrets no frontend

Qualquer configuração enviada ao navegador deve ser tratada como acessível ao destinatário. Avaliar JavaScript, bundles, source maps, HTML gerado, assets estáticos, respostas de API, arquivos de configuração publicados e telemetria. Renderização no servidor não preserva confidencialidade de valor serializado para o cliente.

Segredos de serviços devem permanecer no componente confiável autorizado, quando existente. Não colocar credencial privilegiada compartilhada em código de navegador, aplicativo móvel ou binário desktop distribuído. Minificação, ofuscação, criptografia com chave embutida e nomes sem prefixo público não garantem confidencialidade.

Tokens necessários a um cliente autenticado têm finalidade e escopo próprios, conforme Standard 04. Não são configuração pública: limitar privilégio, duração, armazenamento e destinatário, e impedir exposição desnecessária. Não confundir essa necessidade com distribuir chave privilegiada do serviço a todos os clientes.

### Convenções condicionais verificadas

| Tecnologia, somente quando adotada | Comportamento documentado e decisão |
| --- | --- |
| Next.js | Referências suportadas a variáveis `NEXT_PUBLIC_` são incorporadas ao JavaScript no build; os valores incorporados permanecem fixos nesse artefato. Usar apenas configuração intencionalmente pública. Fonte: [Environment Variables](https://nextjs.org/docs/app/guides/environment-variables). |
| Vite | Por padrão, `VITE_` expõe variáveis ao código do cliente; constantes de `import.meta.env` são substituídas no build e o prefixo é configurável. Não incluir segredos nesse caminho. Fonte: [Env Variables and Modes](https://vite.dev/guide/env-and-mode). |

Essas convenções não são regras universais. Variável sem prefixo público pode vazar por transformação de build, plugin, serialização, log ou código que a encaminhe. Conferir versão, configuração, referências e artefato efetivo. Não presumir exposição automática de toda variável prefixada sem avaliar uso e build, nem privacidade de todo valor não prefixado.

## H. Build time versus runtime

Identificar onde cada valor é resolvido: na compilação/geração, ao iniciar processo, por requisição ou por mecanismo de atualização existente. Build time pode fixar configuração em código/HTML; runtime pode utilizar ambiente, arquivo protegido ou recurso da plataforma sem incorporação ao artefato. Nenhum desses modelos elimina o risco de exposição na saída.

| Situação | Controle verificável |
| --- | --- |
| Configuração incorporada no build | Classificar como pública se alcançar artefato distribuído. Alteração da origem após build não altera o valor incorporado; regenerar quando necessário e autorizado. |
| Configuração resolvida em runtime | Conhecer quando ocorre leitura/renovação e se há cache. Mudança externa pode exigir reinício ou atualização conforme contrato, sem garantia de propagação imediata. |
| Secret utilizado somente para obter recurso no build | Restringir ao passo autorizado e verificar que conteúdo gerado, logs e caches não o retêm. Acesso temporário não garante ausência no resultado. |
| Configuração obrigatória | Validar presença, formato, tipo, destino e combinação de parâmetros no ponto adequado. Diferenciar validade estrutural de aceitação pelo serviço externo. |
| Segredo ausente, inválido ou placeholder | Impedir inicialização insegura ou desabilitar somente a função dependente, conforme contrato; não liberar operação, recorrer a produção ou usar credencial padrão. |
| Diagnóstico | Informar nome seguro da configuração, componente afetado e causa resumida; não incluir valor, string de conexão, cabeçalho ou dump de ambiente. |

Funcionalidade opcional pode ficar indisponível com mensagem clara; ausência de segredo essencial não pode produzir sucesso aparente. Testar caminho legítimo e falhas de configuração com dados sintéticos em ambiente autorizado. Preservar loader, contratos e arquitetura existentes; não impor esquema, biblioteca ou serviço de carregamento universal.

## I. Git e cadeia de desenvolvimento

Antes de qualquer versionamento autorizado, verificar os arquivos e alterações pertinentes, inclusive novos/untracked e gerados, sem mostrar valores secretos. Evitar buscas amplas que imprimam conteúdo de arquivos sensíveis, dumps completos de ambiente ou diffs brutos de achados. Inspeção autorizada deve produzir evidência sem valores sensíveis, com caminho/referência segura e categoria do problema.

| Superfície | Prevenção e detecção proporcionais |
| --- | --- |
| Commits, histórico e pull requests | Usar placeholders, regras de exclusão pertinentes e revisão do conjunto efetivo de arquivos. Repositório privado e PR restrito não autorizam armazenar credenciais reais no código. |
| Temporários e arquivos gerados | Avaliar arquivos de editor, exportações, dumps e diretórios de saída; não presumir exclusão por nome ou localização. |
| Documentação e capturas | Não copiar valores para instruções, issues, comentários, imagens ou capturas de terminal. Usar referências seguras. |
| Logs de testes e terminal | Evitar eco de comandos sensíveis, modo verboso, parâmetros com segredo e relatório de ambiente completo; registrar resultado suficiente sem payload secreto. |
| Dependências e instalação | Avaliar origem e scripts antes de execução autorizada; não conceder ao instalador credenciais desnecessárias. |
| Ferramentas que recebem o projeto | Delimitar arquivos e permissões enviados a IDEs, ferramentas externas ou serviços de análise. Não presumir que exclusão Git também exclui upload por outra ferramenta. |

Inspeção manual, buscas com saída protegida e scanners já disponíveis podem se complementar conforme risco. Não exigir scanner externo, hook novo ou instalação em todo projeto. Validar tratamento dos resultados antes de executar ferramenta que possa imprimir, persistir ou transmitir segredos. Detecção negativa não prova ausência em caminhos não examinados.

Se houver secret no histórico, apagar o arquivo atual ou adicioná-lo ao ignore não basta. Avaliar alcance e revogação/rotação autorizadas primeiro; considerar branches, tags, clones, forks, PRs, caches e cópias pertinentes. A [documentação oficial do GitHub sobre remoção de dados sensíveis](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) recomenda revogar/rotacionar a credencial e descreve riscos e coordenação da reescrita de histórico. Não executar reescrita, force push, limpeza destrutiva ou exclusão de evidências automaticamente.

## J. CI/CD, infraestrutura e distribuição

Aplicar aos mecanismos efetivamente adotados. Não impor Docker, Kubernetes, Vault, CI/CD, nuvem ou nova infraestrutura a um projeto simples.

| Superfície | Controle aplicável |
| --- | --- |
| Pipeline de build/testes | Fornecer somente credenciais do passo e ambiente necessários. Não executar código não confiável, inclusive de contribuição externa, com acesso a secrets privilegiados. |
| Execução e deploy | Separar credenciais de build, entrega e aplicação quando suas concessões diferirem; restringir destino, operação, acesso administrativo e duração. |
| Logs de CI/CD | Evitar eco, dumps, cabeçalhos e rastros sensíveis. Mascaramento é defesa adicional, não autorização para imprimir valor. |
| Artefatos e caches | Verificar pacotes, relatórios, mapas, arquivos temporários e caches relevantes; aplicar acesso/retenção apropriados. Segredos usados no processo não podem ser incorporados ao produto distribuído. |
| Containers e imagens | Se adotados, não incluir secrets em Dockerfile, arquivos copiados, metadados, argumentos inseguros ou camadas. Apagar arquivo em passo posterior não demonstra remoção de camadas anteriores. |
| Configuração de entrega | Usar referências e mecanismos protegidos existentes; manifesto versionável não deve conter valor secreto. Conferir alcance e destinatário reais. |
| Backups | Proteger acesso, armazenamento, transporte e retenção; incluir dependências de chaves na recuperação quando pertinentes. Restaurar não deve reativar automaticamente credencial revogada. |
| Máquinas locais e servidores | Restringir arquivos, identidades de execução, debug, dumps e acesso administrativo conforme plataforma; considerar cópias e sincronizações existentes. |

**Exemplo tecnológico condicional:** o [Docker documenta build secrets](https://docs.docker.com/build/building/secrets/) como alternativa aos argumentos de build e variáveis usados para transmitir segredos durante build, que podem persistir na imagem. Quando suportado e adotado, avaliar secret mounts para acesso temporário. O passo que lê o segredo ainda pode copiá-lo ou imprimi-lo; examinar saídas, logs e imagem final, sem presumir proteção automática.

**Exemplo de plataforma condicional:** em [GitHub Actions, uso de secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets), há regras específicas para forks, workflows reutilizáveis e eventos; verificar o caminho real e as permissões. A documentação alerta sobre valores expostos por linha de comando e limites do mascaramento de segredos em logs em determinados usos. Não extrapolar proteção para qualquer workflow ou conteúdo transformado.

Preparação não autoriza deploy. No Gate B, indicar destino, mecanismo de fornecimento, permissões, evidências e recuperação, sem incluir valores. Falha crítica conhecida de exposição bloqueia release; não publicar para testar controle que deveria estar validado antes.

## K. Bancos, APIs e integrações

| Integração | Regra operacional |
| --- | --- |
| Banco de dados | Credencial específica e permissões mínimas para operações da aplicação; separar administração/migração quando necessário. Proteger string de conexão, acesso de rede e backups. |
| API externa | Restringir recursos, operações, ambiente e consumidor; verificar destinatário confiável e impedir envio a endpoint arbitrário. Chave válida não autoriza todo usuário da aplicação a utilizá-la. |
| Token de serviço e service-to-service | Identificar responsável, sujeito técnico, escopo e validade; usar transporte protegido e verificar revogação no contrato real. Não compartilhar conta humana por conveniência. |
| Webhook | Proteger segredo de assinatura quando adotado; validar origem/integridade, finalidade e replay conforme contrato, sem registrar cabeçalho secreto ou payload sensível. |
| Certificados | Separar certificado/parte pública de chave privada; validar vínculo confiável, destino, validade e substituição conforme protocolo. Não classificar todo certificado público como segredo. |
| Segredos de assinatura | Restringir uso por finalidade e ambiente; considerar efeitos da troca sobre validadores e material previamente emitido. Não usar um segredo amplo para finalidades independentes sem justificativa. |
| Armazenamento externo | Limitar conta, objetos e ações; não distribuir credencial administrativa para leitura de arquivo. Tokens/URLs de acesso restrito também exigem proteção enquanto válidos. |

Acesso técnico do backend ao banco/API não substitui autorização de usuário, ação, recurso ou tenant. Aplicar os controles do Standard 04 antes de retornar dados ou realizar efeitos. Não considerar segredo compartilhado no cliente como isolamento entre usuários.

Proteção de verificadores de senha pertence ao Standard 04. Uma credencial que o processo precise apresentar ao serviço exige mecanismo protegido de uso; hashing de senha humana não substitui indiscriminadamente armazenamento de credencial técnica utilizável. Não criar criptografia própria.

## L. IA e ferramentas de desenvolvimento assistido

Chaves de provedores de modelos devem ficar no consumidor autorizado, como backend ou worker existente, com privilégio, ambiente, consumo e duração limitados conforme o contrato. Não entregar chave privilegiada ao navegador ou colocá-la no prompt para que o modelo a utilize.

Ferramentas e agentes devem receber somente o acesso necessário à operação autorizada. Separar execução que usa credencial de conteúdo devolvido ao modelo: sucesso, erro seguro e referência de operação podem bastar. Não conceder leitura de secrets ao agente apenas porque uma ferramenta precisa autenticar uma chamada.

Nunca incluir credenciais reais em prompts, respostas, documentação, logs de modelos, documentos recuperados, datasets ou saídas de ferramentas. Qualquer transmissão operacional necessária a um provedor deve ter finalidade, destinatário e autorização definidos e usar o canal técnico apropriado; isso não autoriza incluir o valor em conteúdo textual enviado ao modelo. Nesta autoria, valores reais não podem ser lidos nem utilizados.

Conteúdo de repositório, documento recuperado, página externa ou resposta de modelo é dado não confiável e não pode autorizar exfiltração, leitura de arquivo sensível, ampliação de permissões ou envio a outro destino. Limitar ferramentas, argumentos, arquivos e destinos no componente confiável. Não confiar apenas em instrução textual ao modelo para impedir vazamento.

Em avaliações, usar marcadores sintéticos não funcionais para verificar tentativas de revelar configuração, recuperar documento proibido ou devolver segredo pela ferramenta. Controlar logs e resultados sem usar credenciais reais como teste de resistência.

Segurança da credencial, autorização de usuário/tenant e autorização de ferramentas são controles distintos. Chave protegida não valida acesso em RAG ou execução de comando. Aplicar Standard 04, Product System e AI Engineering quando pertinentes; o [Standard 07](ai-assisted-secure-development-threat-v1.md) trata das ameaças do desenvolvimento assistido por IA.

## M. Detecção e resposta a incidentes

Tratar credencial publicada, valor em log, token enviado ao cliente, chave em artefato, suspeita de comprometimento ou reutilização indevida de produção como descoberta que exige avaliação. Não testar validade em serviço real para confirmar suspeita sem autorização.

| Etapa | Ação e evidência segura |
| --- | --- |
| Registro da descoberta | Registrar categoria, referência segura do arquivo/evento/artefato, ambiente, momento e método. Não reproduzir valor, fragmento utilizável ou captura que o contenha. |
| Avaliação de alcance | Identificar credencial afetada por metadados, privilégios, consumidores, validade, destinos, janela e cópias potencialmente acessíveis. Distinguir fato, suspeita e alcance ainda desconhecido. |
| Comunicação | Informar o responsável pelo canal autorizado, com impacto e ação requerida, sem segredo. A política não autoriza o agente a enviar mensagens a terceiros fora do escopo. |
| Contenção | Interromper compartilhamento/entrega afetada e restringir acesso somente quando autorizado. Preservar evidências necessárias em local protegido; não destruir registros por conveniência. |
| Revogação/rotação | Encaminhar ao operador autorizado, priorizando invalidar acesso comprometido e substituir consumidores necessários. Se a autorização faltar, registrar blocker e solicitar decisão humana antes da ação. |
| Verificação posterior | Conferir rejeição do acesso antigo, funcionamento do substituto, concessões derivadas, cópias, artefatos e logs afetados em ambiente autorizado. Não alegar remediação só pela troca do valor na configuração. |
| Prevenção de recorrência | Corrigir origem, permissões, fornecimento, publicação ou diagnóstico no escopo aprovado; repetir verificações e registrar pendências. |

A recomendação de revogação rápida da [OWASP, resposta a incidentes](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#9-incident-response) orienta prioridade, sem ampliar autorização. Acionar o plano emergencial previamente autorizado quando existir; caso contrário, obter decisão humana. Suspeita relevante não deve ser ocultada por falta de certeza, nem convertida em prova conclusiva.

Remover o segredo de log ou histórico é medida distinta de invalidar a credencial. Coordenar eventual limpeza com integridade, investigação, retenção e impacto sobre colaboradores. Não realizar force push, reescrita de histórico, alteração de credencial real, acesso produtivo ou limpeza destrutiva automaticamente. Falhas críticas conhecidas bloqueiam release conforme Product System e Standard 04.

## N. Quality Assurance e Security Gate

Selecionar verificações pelo caminho do segredo, risco e superfície alterada. Usar ambiente autorizado, marcadores sintéticos e ferramentas existentes. A ausência de uma ferramenta não elimina verificação essencial; registrar alternativa suficiente ou blocker com impacto.

| Verificação pertinente | Evidência esperada |
| --- | --- |
| Arquivos públicos e produto distribuído | Examinar destinos relevantes, incluindo bundle, HTML, assets, source maps, pacote ou binário, com procedimento que não imprima valores. Ausência de marcador sintético ou achado é limitada ao alcance examinado. |
| Git e artefatos | Conferir conjunto efetivo de arquivos, novos/untracked, saídas e histórico quando necessário e autorizado. Evidência deve identificar categoria/local, sem reproduzir credencial. |
| Segregação e privilégio | Confirmar destino, concessões e consumidor por metadados/política; testar negativa de acesso indevido quando pertinente e permitido. Nome de ambiente não é evidência suficiente. |
| Configuração ausente/inválida | Exercitar ausência, placeholder, formato incorreto e combinação inconsistente; inicialização/função protegida deve falhar de modo seguro e diagnosticável. |
| Integração indisponível ou rejeitada | Testar credencial sintética inválida, destino incorreto e falha do mecanismo de fornecimento em ambiente controlado; não recorrer a segredo padrão nem liberar operação. |
| Logs e diagnósticos | Exercitar caminhos de erro, modo de teste e rastros pertinentes; conferir que valores não alcançam logs, relatórios, capturas ou saídas. |
| Rotação/revogação previstas | Ensaiar substituição e rejeição de acesso antigo, incluindo concorrência, propagação e acesso derivado conforme contrato. Uso de credencial real exige escopo próprio. |
| Fluxos de IA | Avaliar prompts, recuperação, saídas de ferramentas e logs com marcadores sintéticos; tentativa de exfiltração não deve obter segredo ou ampliar acesso. |
| Regressão e recuperação | Reproduzir exposição/falha corrigida e validar caminho legítimo, consumidores afetados e recuperação prevista, sem reintroduzir acesso comprometido. |

### Evidências e decisão

**Inspeção** examina arquivos, contratos, metadados ou configuração autorizada. **Teste executado** exercita comportamento e registra esperado/observado. **Scanner utilizado** requer nome, versão/configuração pertinente, alcance, execução real e resultado seguro. Uma dessas atividades não prova execução das outras; scanner sem achado não comprova ausência universal de segredos.

Registrar requisito, cenário, ambiente, procedimento, esperado, observado, evidência sem valores sensíveis e limitações no contexto/relatório existente. Usar `PASS`, `FAIL`, `BLOCKED` ou `NOT RUN` para testes, conforme Product System; `NOT_APPLICABLE` justifica somente superfície inexistente. Não declarar `PASS` para teste não executado; uma inspeção pode ter resultado satisfatório dentro de seu alcance, identificada como inspeção. Controle sem superfície pode ser inaplicável; falta de autorização ou ambiente para teste necessário é blocker.

Security Review deve avaliar caminho efetivo da configuração, exposição, acesso, ciclo de vida e verificações relevantes. Identificar autor/revisor; revisão pelo executor é **autorrevisão**, sem alegação de independência. Parecer `APPROVED` requer evidência essencial suficiente e ausência de achado material impeditivo; `CHANGES_REQUIRED` exige correções no Gate A; `BLOCKED` registra condição necessária indisponível. Esses pareceres não substituem Gate B.

Falha crítica conhecida de secrets bloqueia release. Não enfraquecer teste, controle ou classificação para liberar entrega. Revisão documental deste Standard não executa testes de ambiente, scanners de credenciais ou auditoria operacional.

### Exemplos práticos

Os oito cenários abaixo descrevem verificações a planejar conforme autorização; não são testes executados nem arquitetura obrigatória. Exemplos utilizam apenas nomes, placeholders ou dados sintéticos, sem credenciais reais. Inaplicabilidade pressupõe ausência da superfície indicada e deve ser reavaliada se o cenário mudar.

#### 1. Website estático sem backend

**Risco:** publicar configuração interna, chave de administração ou arquivo indevido junto aos assets. **Escolha adequada:** distribuir somente conteúdo/configuração deliberadamente públicos; manter credencial de hospedagem no mecanismo operacional autorizado, fora do website. **Verificação:** examinar o pacote e caminhos publicados previstos, confirmando ausência de arquivos sensíveis e de marcadores sintéticos usados no ensaio. **Controles desnecessários:** criar backend, banco, vault ou ciclo de credenciais de usuário apenas para servir conteúdo estático. Credenciais de publicação exigem avaliação própria se entrega entrar no escopo.

#### 2. Aplicação web com formulário e backend

**Risco:** expor chave do serviço de envio no cliente, logar payload confidencial ou encaminhar credencial a destino arbitrário. **Escolha adequada:** usar credencial restrita no backend existente e validar operação/destino; separar configuração pública de segredo de integração. **Verificação:** exercitar envio válido e falha de configuração em teste, inspecionando resposta, bundle e logs com marcadores sintéticos; confirmar que erro não divulga configuração. **Controles desnecessários:** autenticação de usuários, MFA e persistência de cadastro quando o formulário público não possui contas nem armazena registros. Controles contra abuso do formulário continuam pertinentes.

#### 3. API com banco de dados

**Risco:** string de conexão em erro, credencial administrativa para toda operação ou teste apontando a produção. **Escolha adequada:** credencial da aplicação com concessões mínimas, ambiente separado e autorização por ação/recurso/tenant no componente confiável. **Verificação:** conferir metadados de destino/permissões e executar, em recurso de teste autorizado, operação legítima, negativa fora do escopo e erro com configuração ausente, sem logar conexão. **Controles desnecessários:** prefixos de frontend, cookies e QA visual se não houver cliente web/UI. Proteção do segredo não dispensa AuthZ.

#### 4. Frontend com variável pública de build

**Risco:** tratar nome de variável como garantia de privacidade ou promover artefato com destino público do ambiente errado. **Escolha adequada:** classificar URL pública como publicável; usar convenção `NEXT_PUBLIC_` ou `VITE_` somente se a tecnologia estiver adotada e verificada. Segredos não entram nessa variável. **Verificação:** construir em ambiente controlado com endereço sintético público e conferir valor incorporado e destino do artefato; alterar origem depois do build não deve ser apresentado como atualização desse valor. **Controles desnecessários:** rotação/revogação de credencial para uma URL sem token nem capacidade de acesso, ou infraestrutura nova apenas para esconder configuração pública.

#### 5. Integração com modelo de IA

**Risco:** chave do provedor no navegador, prompt, documento recuperado ou saída de ferramenta; abuso de consumo e acesso indevido a dados. **Escolha adequada:** credencial restrita no backend/worker existente, chamadas a destino aprovado e autorização separada para dados e ferramentas. **Verificação:** em avaliação controlada, inserir marcador sintético como informação proibida e exercitar tentativa de exfiltração, erro de configuração e saída de ferramenta; conferir logs e respostas. **Controles desnecessários:** GEO, banco vetorial, RAG ou agentes quando a tarefa é chamada direta a modelo sem essas funções. Proteção da chave não valida qualidade da resposta nem permissões.

#### 6. Pipeline de build/deploy

**Risco:** secret acessível a código de PR não confiável, impresso em log ou incluído em cache/artefato. **Escolha adequada:** limitar credenciais ao passo e destino autorizados e preservar Gate B. Se Docker estiver adotado, avaliar mecanismo de build secrets documentado, verificando saídas. **Verificação:** ensaio sem credencial produtiva deve demonstrar restrição de acesso e ausência de marcador sintético nos logs/artefatos; conferir política do workflow e destino. **Controles desnecessários:** Docker, nuvem, novo scanner ou automação de rotação apenas para cumprir o Standard. Build aprovado não autoriza deploy.

#### 7. Aplicação local/desktop distribuída

**Risco:** extração de chave compartilhada do executável, arquivo de configuração ou log local. **Escolha adequada:** não embutir credencial privilegiada; se houver integração, adotar acesso individual/delegado conforme arquitetura aprovada e proteção disponível da plataforma. Se offline sem credenciais, manter apenas configuração pertinente. **Verificação:** examinar pacote com marcadores sintéticos e testar armazenamento/erro no ambiente suportado, registrando limites diante de administrador do dispositivo. **Controles desnecessários:** cookies, servidor de identidade, backend novo ou JWT para aplicação offline que não necessita dessas funções. Ofuscação não garante confidencialidade.

#### 8. Secret encontrado em histórico Git

**Risco:** credencial permanecer utilizável e acessível em versões, clones ou PRs apesar da exclusão atual. **Escolha adequada:** registrar referência segura, avaliar alcance, comunicar ao responsável autorizado e preparar revogação/rotação e investigação; limpeza de histórico exige decisão própria. **Verificação:** após ação autorizada, confirmar invalidação no emissor e funcionamento dos consumidores substitutos; revisar cópias/destinos pertinentes sem reproduzir valor. Ensaio documental usa apenas marcador sintético não funcional. **Controles desnecessários:** force push ou reescrita automática como resposta padrão, nova infraestrutura ou teste da credencial real para provar o achado sem autorização. Exposição crítica bloqueia release.

## O. Definition of Ready e Definition of Done

### Definition of Ready

Antes da ação dependente, devem estar suficientemente definidos: objetivo e Gate A; configurações/segredos necessários e sua classificação; origem, destino, consumidor, responsável, ambiente e concessões; mecanismo existente de armazenamento/fornecimento; momento de resolução no build/runtime; riscos de exposição; verificações e recuperação pertinentes.

Identificar se a próxima atividade requer acesso real e sua autorização. Não solicitar valor de credencial para tarefa documental. Lacuna material bloqueia somente a ação dependente. Ajuste trivial sem segredo pode usar justificativa mínima e conferência direta, sem discovery ou inventário extenso.

### Definition of Done da superfície

| Condição | Evidência necessária |
| --- | --- |
| Classificação e fornecimento definidos | Configuração pública, interna e secreta diferenciadas, com consumidores, ambientes, permissões e responsabilidades suficientes. |
| Exposição avaliada | Caminhos de build/runtime, cliente, Git, logs e artefatos pertinentes examinados, com alcance e limitações explícitos. |
| Verificações essenciais concluídas | Cenários aplicáveis executados/inspecionados conforme plano, resultados aceitos e regressões tratadas; teste essencial ausente não é aprovação. |
| Security Review pertinente | Alteração final e evidências examinadas, achados tratados, Security Gate e independência/autorrevisão identificados. |
| Ciclo de vida e recuperação | Expiração, renovação, rotação/revogação e recuperação necessárias definidas e verificadas quando integrarem o escopo; operações posteriores permanecem pendentes. |
| Riscos e Gate B | Exceções, limitações, responsáveis pertinentes e ações protegidas propostas registrados no relatório/contexto autorizado, sem valores secretos. |

Cumprir também os critérios do Product System e dos Standards pertinentes. Distinguir preparação, execução autorizada e verificação pós-entrega. O Standard documental não comprova segurança de um ambiente real, inexistência de vazamentos, rotação operacional ou conformidade. Aplicação e testes controlados posteriores exigem escopo próprio, sem usar produção ou credenciais reais por consequência desta autoria.

## P. Capability Routing, exceções e evolução

### Seleção e ampliação

Aplicar Standard 03 e consultar as instruções completas das Skills efetivamente selecionadas quando não estiverem disponíveis e válidas no contexto. Não ativar todas automaticamente; segurança e validações essenciais prevalecem sobre economia artificial de contexto.

| Skill canônica | Quando consultar/aplicar |
| --- | --- |
| [vera-architecture-security](../.agents/skills/vera-architecture-security/SKILL.md) | Classificação/exposição de secrets, permissões, fronteiras de confiança, incidente ou Security Review exigirem análise especializada. |
| [release-deployment-reliability](../.agents/skills/release-deployment-reliability/SKILL.md) | Configuração de ambientes, build, empacotamento, CI/CD, distribuição, entrega ou recuperação operacional integrarem o escopo. Não exigir para análise puramente documental. |
| [ai-engineering-production](../.agents/skills/ai-engineering-production/SKILL.md) | Credenciais de modelos, workers de IA, RAG, agentes/ferramentas ou avaliações do componente efetivo de IA forem afetados. Assistência de IA na autoria não basta. |
| [data-persistence-engineering](../.agents/skills/data-persistence-engineering/SKILL.md) | Credenciais e acesso à persistência, integridade, recuperação ou dependências de chaves dos dados forem afetados; não exigir para configuração pública estática. |
| [quality-engineering-testing](../.agents/skills/quality-engineering-testing/SKILL.md) | Planejar/executar testes de configuração, falhas, exposição, contratos, abuso, rotação ou regressão pertinente. Inspeção direta pode bastar para mudança sem efeito comportamental. |
| [software-design-solid](../.agents/skills/software-design-solid/SKILL.md) | Implementar/revisar contratos de configuração, lógica de carregamento, validação e tratamento de erros de código. Não exigir para texto documental sem implementação. |

Outras capacidades somente diante de superfície demonstrada. Ampliar roteamento quando surgir segredo real potencialmente exposto, novo consumidor, dado sensível, privilégio maior, persistência, IA/ferramenta, integração externa, artefato público ou preparação de release. Reavaliar risco antes da ação dependente; mudança material fora do Gate A requer decisão humana.

### Exceções e evidências

Adaptar profundidade, mecanismo e verificação ao risco, preservando stack e arquitetura. Ausência de segredo ou superfície pode justificar inaplicabilidade; ausência de ferramenta ou autorização não permite dispensar controle essencial.

Registrar exceção relevante no contexto existente: regra, motivo, alcance, risco, controle compensatório, responsável e condição de reavaliação. Obter aprovação humana antes de alterar segurança material, governança, requisito contratado ou decisão aprovada. Simplificação rotineira dentro do Gate A não exige microaprovação. Exceção não permite expor credenciais reais em exemplos, ignorar falha crítica conhecida ou alegar conformidade externa não demonstrada.

Usar evidências resumidas e sem valores sensíveis, separando fato, inferência e recomendação. Não criar arquivo de log obrigatório por tarefa. Autorrevisão não substitui revisão independente exigida pelo projeto nem decisão humana.

### Compatibilidade e evolução

O [AI-Assisted Secure Development Threat](ai-assisted-secure-development-threat-v1.md), Candidate, detalha ameaças específicas do processo com IA. Sua ausência no inventário da autoria inicial é histórica. Conferir o inventário atual e os estados documentais; integrar novos documentos ou ajustar referências somente por revisão autorizada dos arquivos envolvidos.

Revisar este Standard diante de achado operacional, conflito, nova superfície ou mudança técnica relevante. Registrar problema, fonte, evidência, regra afetada, impacto e transição; verificar compatibilidade com AGENTS.md, Standards e Skills. Seguir o Product System: incremento maior para mudança incompatível de governança, menor para regra operacional compatível e revisão corretiva para esclarecimento sem alteração de obrigação. Não mudar regras silenciosamente mantendo a identificação de versão.

| Versão | Estado | Registro e limite de evidência |
| --- | --- | --- |
| 1.0 | Stable | Política inicial de classificação, ciclo de vida, exposição, incidentes, QA e roteamento proporcional. Fundamentação documental e referências técnicas verificadas; aplicação operacional depende de testes controlados posteriores. |

Recomenda-se revisão humana do conteúdo e posterior validação em cenários representativos de configuração pública, segredo no backend, build/runtime, Git, aplicação local e integração com IA. Atualização de catálogos/referências, automações e mudanças reais de configuração exigem escopo próprio. A autoria inicial foi limitada à criação documental deste Standard; isso não restringe as tarefas futuras autorizadas pelo Gate A.

Revisão corretiva 1.0.1 (13/10/2026): referências normativas sem versão fixa e consistência com a taxonomia de testes vigente, quando pertinente. Preserva Gates, responsabilidades e estado canônico. Ajuste documental autorizado na revisão final para publicação; não comprova nova validação operacional.
