# My Easy Development System Web Experience & Business Systems v1.2

## A. Identificação, escopo e aplicação

| Campo | Definição |
| --- | --- |
| Nome oficial | My Easy Development System Web Experience & Business Systems v1.2 |
| Identificador | Standard 02 |
| Versão | 1.2 |
| Estado canônico | Stable |
| Finalidade | Estabelecer critérios operacionais de engenharia, design, experiência e qualidade para interfaces orientadas a objetivos editoriais, comerciais e operacionais. |
| Aplicabilidade | Websites institucionais premium, landing pages, páginas comerciais, portais, aplicações web, dashboards, sistemas empresariais, interfaces administrativas e interfaces locais/desktop, conforme a superfície. |
| Independência técnica | Aplicável sem determinar linguagem, framework, biblioteca, ferramenta de design, arquitetura ou ambiente de execução. |

Stable é uma decisão canônica. Não comprova validação operacional, certificação, conformidade, aprovação humana ou prontidão de um produto.

### Classificação da experiência

Classificar cada superfície antes de definir controles. Um mesmo produto pode combinar tipos, como portal público e área autenticada.

| Tipo | Objetivo predominante | Aplicação específica |
| --- | --- | --- |
| Website público editorial/comercial | Informar, estabelecer confiança e permitir uma decisão ou conversão legítima. | Narrativa, identidade, conteúdo verificável e caminhos comerciais; SEO somente nas páginas públicas indexáveis e AI Search Visibility conforme objetivo de descoberta. |
| Aplicação web | Realizar tarefas interativas sujeitas a regras de negócio. | Jornadas, contratos, dados, permissões, estados e recuperação de falhas; descoberta pública apenas nas superfícies pertinentes. |
| Sistema interno | Executar trabalho operacional com eficiência e integridade. | Densidade útil, cadastros, consultas e ações coerentes com o perfil; sem obrigação de narrativa comercial, prova social ou indexação. |
| Interface local/desktop | Executar tarefas no ambiente local e, quando previsto, conectado. | Janelas, escala de exibição, teclado, convenções da plataforma e estados de arquivos/conectividade; sem pressupor infraestrutura web. |

### Relação com o sistema e limites

O [Product System v4.0](product-system-v4.md) permanece a fonte central de processo, governança, Gates, engenharia, resultados de testes e entrega. Este Standard acrescenta critérios de experiência e interface; não reproduz o ciclo central nem amplia autorização.

Usar as Skills canônicas em `.agents/skills/` para procedimentos especializados, conforme a seção Q. Consultar Standards especializados existentes e pertinentes; referências a documentos futuros indicam evolução, sem criar dependência de documento ausente. Resolver conflito material conforme o Product System antes da ação afetada.

Não abrange especificação completa de autenticação, segurança, persistência, implantação ou engenharia de IA. Também não exige ferramenta, dependência, infraestrutura, recurso comercial ou funcionalidade empresarial universal.

**Leitura normativa:** “deve” indica critério obrigatório para a superfície aplicável; “quando” estabelece condição que precisa ser avaliada; “recomenda-se” admite alternativa justificada. Registrar inaplicabilidade de controles relevantes no contexto autorizado, sem produzir checklist extenso para ajustes simples.

## B. Princípios de experiência

Relacionar as decisões de experiência ao objetivo real do usuário e aos critérios de aceitação. Avaliar se a pessoa consegue compreender a situação, escolher uma ação, executá-la e reconhecer o resultado.

| Princípio | Regra verificável |
| --- | --- |
| Clareza e previsibilidade | Rótulos, sequência e efeitos das ações devem corresponder à tarefa; mudanças relevantes de contexto precisam ser comunicadas. |
| Hierarquia da informação | Conteúdo e ação principais devem ser reconhecíveis sem competir com elementos secundários. |
| Usabilidade | O fluxo deve poder ser concluído com os meios de entrada previstos, incluindo recuperação das falhas pertinentes. |
| Redução de fricção | Solicitar somente informações e etapas necessárias; evitar repetição de dados já disponíveis quando seu reaproveitamento for seguro. |
| Consistência | Ações equivalentes devem compartilhar nomenclatura, posição esperada e comportamento entre telas. |
| Identidade visual | Preservar a marca e as convenções aprovadas, com variações justificadas pelo conteúdo e pela tarefa. |
| Acessibilidade | Tornar informação e operação perceptíveis e utilizáveis por diferentes capacidades, conforme a seção I. |
| Feedback e recuperação | Informar andamento, resultado e próxima ação; impedir que a pessoa confunda falha com sucesso. |
| Performance percebida | Manter resposta compreensível durante espera, sem mascarar indisponibilidade ou resultado incerto. |
| Orientação ao objetivo | Priorizar compreensão, conclusão e qualidade da tarefa; efeitos e métricas de engajamento precisam ter relação demonstrável com esse objetivo. |

Verificar os princípios em jornadas representativas. Preferências do autor ou beleza isolada não bastam para aceitar um fluxo que dificulte o trabalho.

## C. Direção de arte e design premium

Premium significa qualidade e intencionalidade, não necessariamente luxo, ornamentação ou complexidade. Definir ou recuperar uma direção visual proporcional antes de implementar mudanças relevantes. Em correções pequenas, o sistema existente pode fornecer essa direção.

| Dimensão | Diretriz operacional |
| --- | --- |
| Tipografia | Definir papéis para títulos, corpo, rótulos e dados; conferir legibilidade, extensão de linha, quebras e caracteres do conteúdo real. |
| Composição | Organizar a tela pela importância e relação entre informações; conferir equilíbrio e densidade adequados ao objetivo. |
| Espaçamento | Utilizar ritmo consistente; proximidade deve expressar agrupamento, sem comprimir leitura ou desperdiçar espaço operacional. |
| Grid e alinhamento | Adotar referências coerentes de alinhamento e adaptação; verificar continuidade entre seções, componentes e telas. |
| Imagens e ícones | Usar ativos pertinentes, autorizados e coerentes com a narrativa; conferir recorte, resolução e função. Não fabricar cases ou provas visuais. |
| Contraste | Verificar texto, controles e estados em seus fundos reais; preservar leitura inclusive sobre imagens. |
| Cores e identidade | Definir papéis de marca, superfície, ação e estado; não depender somente de cor para comunicar significado. |
| Hierarquia visual | Distinguir conteúdo, ação principal e apoio por composição, tipo e contraste, evitando competição generalizada. |
| Componentes reutilizáveis | Reaproveitar padrões existentes e consolidar repetições significativas; permitir variações necessárias sem abstração antecipada. |
| Coerência entre páginas | Conferir navegação, cabeçalhos, controles, linguagem, densidade e estados; coerência não exige páginas idênticas. |

Evitar interfaces genéricas, excesso de cards iguais sem função, gradientes gratuitos, animações decorativas e aparência padronizada de conteúdo gerado por IA. Um card, gradiente ou composição recorrente pode ser apropriado quando sua função for demonstrável. Não transformar gosto pessoal em proibição universal.

Websites podem adotar composição editorial; sistemas operacionais devem privilegiar leitura, precisão e eficiência. Mudanças materiais de identidade precisam respeitar a decisão aprovada. Encaminhar direção a Julian, implementação a Kael e revisão renderizada a Visual QA quando essas capacidades forem pertinentes.

### Exploração criativa e identidade contextual

Antes de implementar interface nova ou redesign, considerar pelo menos três direções materialmente diferentes. Comparar conceito, tipografia, paleta, composição, ritmo, hierarquia, tratamento de imagens, navegação e interação. Não basta recolorir o mesmo layout. Registrar brevemente no contexto existente as alternativas, a direção escolhida e por que atende público, posicionamento, objetivo, personalidade, clareza, diferenciação, viabilidade e acessibilidade. Decidir no Gate A sem microaprovações; não construir três sites. Em correção localizada, recuperar a exploração vigente e avaliar apenas o delta.

Não há uma estética MEDS para clientes. Marfim, verde, dourado, serifada, fotografia ampla, duas colunas, cards, gradientes, badges, glassmorphism ou animações não são receitas nem proibições universais. Justificar o uso pelo conteúdo e pela tarefa, sem reutilizar automaticamente o projeto anterior. Composição editorial, assimetria, variação de densidade e tipografia expressiva só são úteis quando preservam leitura, hierarquia, navegação, contraste, responsividade e performance.

Definir tokens de fundo, superfície, texto, destaque, ação, estados, bordas e feedback. Escolher fontes por personalidade, hierarquia, legibilidade, pares, carregamento e fallback; avaliar licença e uso offline antes de exigir fontes externas. Cada interação deve orientar navegação, exploração, feedback ou produtividade. Respeitar movimento reduzido. Sistemas administrativos e sites comerciais têm prioridades diferentes.

### Produção dos recursos visuais

Quando o projeto solicitar imagens, verificar as ferramentas realmente disponíveis e autorizadas. Gerar imagens originais quando houver ferramenta adequada; se não houver, usar alternativas proporcionais como SVG/CSS e registrar a limitação. SVG desenhado não deve ser apresentado como imagem gerada por IA. Não exigir imagens em produtos que não precisam delas, nem instalar ferramentas ou contratar serviços sem autorização.

Salvar assets dentro da pasta do projeto, com caminhos relativos e sem URLs externas obrigatórias. Manter direção visual consistente, formatos, proporções, recortes e resolução adequados ao uso. Geração e otimização são etapas distintas: depois de gerar, conferir dimensões e peso, reduzir/comprimir quando ferramentas existentes permitirem e evitar arquivos excessivamente pesados. Informar quando a otimização não foi possível; não alegar medição inexistente.

Criar textos alternativos conforme função (decorativos com alternativa vazia), respeitar licenças e direitos de uso e registrar origem/licença quando pertinente. Identificar imagens conceituais ou ilustrativas quando puderem ser confundidas com imóvel, produto, pessoa ou prova comercial real. Conferir carregamento e composição no navegador; imagem isolada não valida o site.

## D. Arquitetura da informação

Organizar páginas, conteúdo e funcionalidades pelos conceitos do domínio e pelas tarefas prioritárias. Antes de criar navegação relevante, identificar entradas, destinos, relações, ações principais e informação necessária à decisão.

- Usar agrupamentos e rótulos compreensíveis para o público; evitar nomes internos sem significado para quem utiliza.
- Tornar perceptíveis a localização, o item ativo e o caminho de retorno quando a profundidade exigir. Breadcrumbs são condicionais à estrutura.
- Manter hierarquia entre páginas, seções e funcionalidades. Rotas diretamente acessadas devem oferecer contexto suficiente.
- Em sites comerciais, conectar oferta, evidência disponível e próxima ação. Conversão pode ser contato, leitura, solicitação ou contratação, conforme o objetivo aprovado.
- Em sistemas, priorizar tarefas frequentes ou críticas e evitar navegação baseada apenas na organização técnica dos módulos.
- Adotar busca, filtros e ordenação quando volume e diversidade tornarem a localização difícil; não acrescentá-los a conjuntos simples sem benefício.
- Comunicar alterações de contexto, como organização, unidade ou projeto ativo, quando afetarem dados e operações.
- Definir comportamento de voltar, atualizar, acessar link direto e restaurar navegação conforme a plataforma.

Estados de navegação devem refletir permissões conhecidas sem expor recursos sensíveis. Diferenciar destino inexistente de acesso indisponível somente quando isso for seguro. Menu oculto não é controle de autorização.

Verificar a arquitetura com tarefas representativas: encontrar informação, localizar registro, iniciar ação e retornar sem perda indevida de contexto.

## E. Conteúdo e UX Writing

Textos devem ser claros, específicos, consistentes com o domínio e compatíveis com o espaço disponível. Informar o necessário à decisão no ponto em que será usado.

| Situação | Critério de texto |
| --- | --- |
| Oferta e benefícios | Descrever resultado concreto desejado pelo cliente, destinatário e limites conhecidos; tecnologias podem explicar o serviço, mas não substituir seu valor. |
| CTA | Nomear a ação e seu efeito esperado; não prometer acesso, preço, prazo ou gratuidade inexistentes. |
| Formulário | Identificar campo, obrigatoriedade, formato, restrições e finalidade quando necessária; placeholder não substitui rótulo. |
| Erro | Identificar o problema de forma segura, orientar correção ou alternativa e preservar informação útil. |
| Estado vazio | Distinguir ausência inicial, nenhum resultado e indisponibilidade; oferecer próxima ação pertinente. |
| Confirmação | Identificar ação, alvo e consequência, incluindo irreversibilidade ou abrangência quando relevantes. |
| Sucesso | Informar o que foi concluído e o próximo passo; não confirmar persistência apenas porque o envio começou. |
| Onboarding | Orientar a primeira tarefa e oferecer ajuda contextual; evitar tutorial obrigatório sem necessidade. |

Não inventar depoimentos, métricas, resultados, clientes, certificados, prêmios, funcionalidades, cases ou provas sociais. Vincular alegações relevantes a informação confirmada e autorizada. Na preparação, identificar claramente fatos pendentes; não publicar marcadores como conteúdo final.

Evitar superlativos vazios, jargão dispensável, urgência artificial e instruções contraditórias. Validar copy em contexto renderizado, inclusive quebras, truncamento e estados negativos. Clara conduz conteúdo e UX Writing quando essa superfície exigir especialização.

## F. Sistemas empresariais e fluxos operacionais

Definir jornadas por tarefa e perfil: entrada, pré-condições, dados, ações, resultado e recuperação. Perfis e permissões visíveis devem orientar o uso e refletir decisões do componente confiável.

| Superfície | Critérios aplicáveis |
| --- | --- |
| Tabelas e registros | Identificar colunas, unidades, formatos e ações por registro; evitar truncamento de informação essencial sem acesso ao valor completo. Definir seleção em lote e seu alcance somente se previstas. |
| Busca, filtros e paginação | Mostrar critérios ativos, permitir sua limpeza e distinguir zero resultados de erro. Definir alcance da busca, ordenação e seleção entre páginas quando puder haver ambiguidade. |
| Cadastro e edição | Agrupar campos pela tarefa, distinguir criar de editar, indicar mudanças pendentes e tratar erros de campo e de operação. Proteger contra perda acidental quando o impacto justificar. |
| Ações destrutivas | Identificar alvo e efeito; aplicar confirmação, revisão ou reversão conforme risco. Não exigir confirmação para toda ação rotineira. |
| Histórico e rastreabilidade | Exibir eventos, autoria, horário e alterações somente quando requisitos e risco exigirem, com acesso e retenção definidos. |
| Indicadores e dashboards | Definir significado, unidade, período, fonte e atualização dos dados; diferenciar zero, ausência, dado atrasado e erro. Conectar indicadores às decisões que apoiam. |
| Aprovação | Quando prevista, mostrar estado, responsável ou papel, pendência e ações permitidas; impedir que a interface declare aprovação sem confirmação do domínio. |
| Concorrência | Quando edições simultâneas forem possíveis e relevantes, detectar conflito e oferecer atualização, comparação ou resolução segura; não sobrescrever silenciosamente alterações de terceiros. |
| Eficiência operacional | Preservar contexto útil entre consultas e ações; usar atalhos, edição em lote ou preenchimento assistido apenas quando frequência e risco justificarem. |

Não impor CRM, SLA, pipeline, auditoria ou aprovação a todo sistema. Esses recursos dependem de requisito explícito ou necessidade demonstrada. Validação operacional deve considerar volume representativo de registros e papéis pertinentes, com dados sintéticos ou autorizados.

## G. Estados e interações

Definir os estados aplicáveis de cada fluxo relevante, inclusive transições e recuperação. Uma página estática não precisa simular estados de transação que não possui.

| Estado | Comportamento esperado |
| --- | --- |
| Loading | Indicar a operação em andamento, manter contexto e reservar espaço quando necessário; progresso numérico só deve ser exibido se conhecido. |
| Empty state | Explicar ausência ou nenhum resultado e oferecer ação adequada, sem apresentar falha como conjunto vazio. |
| Success | Confirmar resultado efetivo e atualizar a tela com dados consistentes. |
| Error | Exibir mensagem segura e alternativa; evitar descartar dados pertinentes à recuperação. |
| Validation | Associar problema ao campo ou à operação, explicar correção e permitir localizar os erros. |
| Disabled | Indicar indisponibilidade quando sua causa não for evidente; oferecer orientação acessível sem depender de hover. |
| Unauthorized | Tratar falta de sessão ou permissão conforme contrato, com próximo passo seguro e sem divulgar dados protegidos. |
| Not found | Informar destino indisponível e caminho útil de retorno; respeitar eventual ocultação segura de existência. |
| Timeout | Informar demora e resultado possivelmente incerto; não incentivar reenvio cego de operação com efeito material. |
| Falha de conexão | Distinguir indisponibilidade de ausência de dados; mostrar última informação disponível apenas se seu estado estiver claro e seu uso for seguro. |
| Recuperação e nova tentativa | Repetir apenas quando seguro, limitar tentativas automáticas e reconciliar operações de resultado desconhecido antes de duplicá-las. |

Impedir duplicidade por interação repetida durante processamento; quando o efeito exigir garantia, coordenar idempotência com o componente confiável. Desabilitar um botão isoladamente não garante unicidade.

Preservar dados inseridos quando pertinente e seguro, definindo duração e local apropriados; não persistir automaticamente secrets ou dados sensíveis em armazenamento do cliente. Diferenciar rascunho, envio pendente e registro confirmado.

Motion deve comunicar relação, transição ou estado e respeitar movimento reduzido, preservando informação e funcionalidade.

## H. Responsividade e compatibilidade

Definir ambientes suportados conforme usuários e requisitos: navegadores, dispositivos, larguras, meios de entrada e, para interfaces locais, sistemas, janelas e escalas de exibição.

- Adaptar composição e densidade à largura disponível, preservando prioridade e acesso ao conteúdo essencial.
- Escolher pontos de adaptação pelas necessidades do conteúdo; não impor breakpoints fixos, mobile-first ou desktop-first.
- Conferir extremos e larguras intermediárias relevantes, textos longos, dados de teste representativos e componentes expandidos.
- Permitir toque, mouse e teclado conforme o ambiente; interações essenciais não podem depender exclusivamente de hover.
- Evitar overflow indesejado, corte de controles e texto ilegível. Rolagem deliberada deve ter limite, indicação e operação adequados.
- Em tabelas, selecionar rolagem localizada, priorização de colunas, detalhe ou outro tratamento que preserve relações e informação; não converter toda tabela em cards automaticamente.
- Em formulários, manter ordem de leitura, associação de instruções e acesso a erros, inclusive com teclado virtual quando pertinente.
- Em desktop/local, respeitar convenções, redimensionamento e escala previstos; registrar limitações de janela mínima justificadas.

Verificar a matriz de compatibilidade pertinente e registrar ambientes avaliados. Em ambiente não suportado, comunicar a limitação ou oferecer degradação adequada ao risco. Não alegar compatibilidade ampla a partir de um único navegador.

## I. Acessibilidade

Adotar [WCAG 2.2 nível AA](https://www.w3.org/TR/WCAG22/) como referência de qualidade para interfaces quando aplicável. Em interfaces locais, considerar equivalentes da plataforma. Não alegar conformidade formal sem auditoria adequada do escopo declarado.

Verificar:

- Operação por teclado, ordem coerente e ausência de aprisionamento.
- Foco visível e não oculto; gestão de foco em diálogos e mudanças de contexto.
- Semântica, nome, papel e estado acessíveis; preferir controles nativos apropriados.
- Rótulos, instruções e erros associados aos campos; mensagens de estado percebidas por leitores de tela.
- Contraste aplicável, informação independente de cor e alternativas textuais para conteúdo não textual.
- Alvos interativos adequados e alternativa a gestos complexos ou arrastar quando necessário.
- Zoom, espaçamento de texto e reflow sem perda de conteúdo ou operação, respeitando exceções aplicáveis.
- Preferências de movimento reduzido e controle de conteúdo em movimento.
- Idioma, mídia e autenticação acessível quando essas superfícies existirem.

Combinar validação automatizada disponível com inspeção manual proporcional: teclado, foco, zoom, erros e fluxos críticos; incluir leitor de tela conforme risco. Automação não comprova toda a acessibilidade.

No registro de aceitação, indicar critérios e jornadas examinados, ambientes e tecnologias assistivas usados, falhas, correções e limitações. Requisitos essenciais não verificados devem permanecer pendentes, conforme o Product System.

## J. Performance

Definir orçamento de performance quando criticidade, volume, conectividade ou experiência pública justificarem. Relacionar metas à jornada, dispositivo, rede e volume representativos; indicar métrica, condição de medição e critério de aceitação antes de concluir aprovação.

- Otimizar imagens por dimensão, formato, compressão e carregamento apropriados; evitar adiar recurso essencial da primeira visualização.
- Usar fontes necessárias, pesos e carregamento eficientes, preservando leitura e estabilidade.
- Evitar JavaScript, dependências, requisições e trabalho de renderização sem função demonstrada.
- Escolher renderização e carregamento adequados ao conteúdo, interação e descoberta; não impor SSR, SPA ou outra estratégia universal.
- Reservar espaço para conteúdo assíncrono quando pertinente e oferecer feedback de espera.
- Aplicar caching quando útil, definindo validade e invalidação; respeitar isolamento, sessão e sensibilidade dos dados.
- Em sistemas, medir resposta de consultas, formulários e listas sob volume relevante; paginação ou virtualização dependem de necessidade medida.
- Em interfaces locais, avaliar abertura, resposta, volume e consumo de recursos pertinentes.

Em experiências web públicas, considerar [Core Web Vitals](https://web.dev/articles/vitals), incluindo LCP, INP e CLS, e medições reais de uso quando disponíveis. Distinguir laboratório de campo; desempenho em teste controlado não prova resultado dos usuários.

Registrar ambiente, procedimento, valores observados e comparação com o orçamento ou baseline. Monitorar regressões com verificações ou sinais operacionais proporcionais e autorizados. Não declarar performance aprovada somente por inspeção de código ou por uma pontuação isolada. Não acrescentar complexidade sem benefício mensurável; se faltar medição essencial, registrar a pendência.

## K. SEO técnico

Aplicar somente a páginas públicas destinadas à indexação. Áreas privadas, dashboards e interfaces locais não exigem otimização de indexação. Conduzir SEO especializado com `seo-technical`.

Inventariar URLs públicas e intenção de indexação. Conforme a estrutura, verificar:

- URLs estáveis e canonical coerente com a página e eventuais duplicações.
- Títulos e metadados específicos, compatíveis com conteúdo visível.
- Robots e sitemap quando pertinentes, com configuração adequada ao ambiente.
- HTML semântico, headings significativos e links internos utilizáveis.
- Dados estruturados válidos, apoiados em fatos verificáveis e conteúdo público.
- Performance, renderização e acesso ao conteúdo pelos mecanismos de busca.
- Redirecionamentos de migração e resposta adequada para páginas removidas, preservando destinos relevantes.

Evitar redirecionar indiscriminadamente páginas inexistentes para a home. Conferir configurações de staging antes da publicação autorizada; restrição de rastreamento não protege dado privado.

Seguir a [documentação técnica de busca pertinente](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), sem impor artefatos a páginas que não precisam deles. Registrar URLs, HTML/respostas examinados e limitações. Acesso técnico e configuração correta não comprovam indexação efetiva, ranking ou tráfego.

## L. AI Search Visibility

Aplicar quando conteúdo público tiver objetivo pertinente de descoberta e compreensão por sistemas de busca com IA. A Skill responsável é `ai-search-visibility`; sua atuação não equivale a engenharia de sistemas de IA ou RAG.

- Definir identidade factual clara: entidade, atividade, serviços, público e contatos publicados.
- Manter nomes, relações, datas e fatos consistentes entre páginas.
- Publicar informações verificáveis, originais e relevantes às perguntas reais do público.
- Usar estrutura semântica e linguagem concreta que conectem conteúdos, serviços e evidências.
- Apresentar autoria, fontes, atualização e transparência quando pertinentes ao conteúdo.
- Preparar acesso técnico e relações entre páginas com SEO Technical, respeitando políticas e decisões de publicação.
- Incluir provas e referências somente quando confirmadas e autorizadas; minimizar dados pessoais publicados.

Não prometer aparição, posicionamento, recomendação ou citação por modelos de IA. Não tornar arquivo especial, tag ou método especulativo obrigatório.

Validar consistência factual e descoberta técnica. Se houver avaliação em ferramentas ou resultados públicos, registrar consulta, contexto, data e observação, sem extrapolar um resultado isolado. Diferenciar conteúdo tecnicamente acessível de conteúdo efetivamente citado.

## M. Segurança e privacidade da experiência

Aplicar o baseline do Product System à superfície da interface. Vera aprofunda riscos de arquitetura, dados e confiança quando pertinente. Esta seção trata consequências visíveis e integração de controles; não especifica o futuro Authentication & Security Standard.

- Exibir, coletar e exportar apenas dados necessários ao perfil e à tarefa; considerar telas compartilhadas, histórico, downloads e notificações.
- Evitar identificadores sensíveis em URLs, mensagens, telemetria e conteúdo acessível ao cliente quando não necessários ou autorizados.
- Formular entradas com limites e instruções claras; validar no cliente para orientar e no servidor ou componente confiável para garantir integridade e autorização.
- Tratar conteúdo externo, de usuários ou de modelos como não confiável. Usar codificação conforme contexto e sanitização apropriada quando HTML for necessário; evitar caminhos de renderização que permitam XSS.
- Retornar erros úteis sem secrets, payloads sensíveis, detalhes internos ou enumeração indevida de recursos.
- Comunicar finalidade, compartilhamento e consentimento quando aplicáveis aos requisitos de privacidade; não condicionar escolhas legítimas por interface enganosa.
- Na sessão, comunicar expiração quando necessário, oferecer retomada segura e evitar exposição residual após logout ou troca de usuário.
- Em interações protegidas, respeitar os mecanismos confiáveis de proteção, inclusive contra CSRF quando aplicável; confirmações visuais não substituem esses controles.
- Respeitar autorização por ação e recurso. Não enviar dados proibidos ao cliente para apenas ocultá-los, nem confiar em permissões editáveis no frontend.

Não embutir secrets em frontend ou artefato local distribuído. Preservação de rascunho, caching e observabilidade devem respeitar a sensibilidade do dado. Avaliar operações relevantes por acesso direto ao componente confiável quando necessário, além do fluxo visual. Encaminhar achados materiais ao Security Gate previsto no Product System.

## N. Integração com regras de negócio

Separar responsabilidades de apresentação e domínio de modo proporcional. Não exigir frontend/backend separados, classes, camadas ou arquitetura específica. Respeitar contratos e convenções existentes.

| Aspecto | Regra operacional |
| --- | --- |
| Contratos de API ou integração | Conhecer entradas, saídas, erros, permissões, limites e compatibilidade usados pela interface; não deduzir sucesso por ausência de exceção local. |
| Validação | Manter orientação de campo coerente com regras do domínio; componente confiável decide validade final e acesso. |
| Falhas | Distinguir rejeição de negócio, indisponibilidade, falha parcial e resultado desconhecido; orientar recuperação segura. |
| Estados consistentes | Sincronizar após operações confirmadas e invalidar dados obsoletos quando necessário; atualização otimista exige reversão ou reconciliação definida. |
| Idempotência | Quando repetição puder duplicar efeitos, garantir tratamento no componente responsável pela operação; coordenar interface, retries e resultado confirmado. |
| Integridade de fluxo | Preservar sequência, pré-condições e invariantes relevantes; impedir avanço visual que contradiga estado real ou permissão. |
| Observabilidade | Registrar sinais úteis para diagnóstico, como etapa e referência segura de operação, sem capturar dados sensíveis desnecessários. |
| Arquitetura existente | Usar os pontos de integração e padrões atuais; justificar alteração material antes de executar conforme governança. |

Em aplicação local sem servidor, a validação confiável pertence ao componente responsável pelo domínio e pelo acesso aos dados. Testar contratos e falhas representativas, não apenas respostas de sucesso simuladas.

## O. Quality Assurance

Selecionar verificações conforme mudança, exposição e criticidade. Relacionar cada cenário relevante a requisito e resultado observável. Quality Engineering conduz estratégia de testes; Visual QA examina a interface efetivamente renderizada.

| Superfície | Verificação e evidência esperadas |
| --- | --- |
| Direção visual e consistência | Comparar telas renderizadas com direção aprovada, componentes e páginas relacionadas; registrar desvios relevantes. |
| Responsividade e compatibilidade | Examinar larguras/janelas e ambientes previstos, incluindo extremos, conteúdo longo e overflow. |
| Acessibilidade | Executar verificações automatizadas disponíveis e inspeções manuais pertinentes da seção I. |
| Interações e estados | Exercitar navegação, teclado, feedback, loading, vazio, erro, recuperação e prevenção de duplicidade aplicáveis. |
| Formulários | Verificar dados válidos, inválidos, limites, erros remotos, envio repetido e preservação segura. |
| Segurança | Validar permissões, exposição de dados e conteúdo não confiável conforme risco; integrar resultados do Security Gate. |
| Performance | Medir jornadas e condições relevantes, comparando orçamento ou baseline; separar laboratório e campo. |
| SEO/GEO | Quando aplicáveis, conferir rotas, semântica, fatos, acesso técnico e configurações; não inferir descoberta efetiva sem evidência. |
| Integrações e fluxos críticos | Testar contratos, sucesso, rejeição, falhas e conflitos pertinentes com dados sintéticos ou autorizados. |
| Regressão | Reexecutar cenários afetados e comportamentos adjacentes após correção ou mudança relevante. |

QA visual de site exige navegador real disponível e autorizado, com interface renderizada nas larguras e estados pertinentes. DOM simulado não substitui navegador, inspeção estática não substitui execução funcional e inspeção de imagem isolada não valida o site. Em aplicativo local, identificar o runtime real examinado. Capturas podem registrar a renderização, mas não comprovam interação.

Distinguir **teste executado**, **inspeção realizada** e **teste necessário indisponível**, com causa e impacto. Usar os resultados `PASS`, `FAIL`, `BLOCKED` e `NOT RUN` conforme o Product System; indisponibilidade não é inaplicabilidade.

Registrar tela/fluxo, perfil, ambiente, condição, esperado, observado, evidência e achado com severidade quando pertinente. Corrigir e repetir verificações afetadas antes do parecer. Identificar revisor e independência real; quando o executor revisar, declarar autorrevisão. Nenhuma troca de Skill cria independência por si só.

## P. Definition of Ready e Definition of Done

### Aceite visual antes da entrega

Para interfaces, funcionamento aprovado não basta para o aceite visual. Implementar, renderizar em navegador ou runtime real, capturar estados pertinentes, examinar as capturas e a experiência, apontar problemas concretos, corrigir e reinspecionar as partes afetadas. Julgar identidade, composição, tipografia, imagens, interação, responsividade, diferenciação e linguagem pelo procedimento da Skill Visual QA. Gerar screenshots sem examiná-los não cumpre o critério.

Separar resultados técnicos objetivos de julgamento editorial fundamentado. Comparar outros projetos apenas quando suas fontes ou telas forem realmente acessíveis e houver pertinência; não afirmar exclusividade no mercado. Registrar direção, telas e estados examinados, achados, correções e limitações no registro existente. Sem navegador, usar `BROWSER_QA: BLOCKED`; com inspeção insuficiente, manter o parecer visual pendente. Autorrevisão não é revisão independente. O aceite estético do usuário continua necessário.

Estes critérios complementam a seção M do Product System e devem ser proporcionais à superfície alterada.

### Definition of Ready de interface e experiência

Antes da implementação dependente, deve haver:

- Tipo de experiência, público, tarefa e resultado esperado identificados.
- Páginas, fluxos, conteúdo, estados e perfis afetados delimitados.
- Direção visual e padrões existentes disponíveis, ou definição suficiente para a etapa.
- Copy e ativos necessários confirmados; fatos pendentes explicitados.
- Contratos, dados de teste, erros e permissões relevantes conhecidos.
- Ambientes, acessibilidade e condições de performance pertinentes definidos.
- Critérios de aceitação e meios de validação disponíveis ou limitações registradas.

Não exigir protótipo completo para ajuste simples. Definição de design pode ser a referência existente com o delta explicado. Lacuna material bloqueia apenas o trabalho que dela depende.

### Estados de realização e aceite

| Estado | Condição verificável |
| --- | --- |
| Design definido | Direção, hierarquia, conteúdo, estados e adaptações necessários à etapa estão definidos e coerentes com decisões aprovadas. |
| Interface implementada | Telas e componentes previstos existem, foram inspecionados e integram os contratos pertinentes; execução de testes ainda deve ser demonstrada. |
| Comportamento testado | Cenários essenciais de interação, regras e recuperação foram executados com resultados aceitos e cobertura explícita. |
| QA visual realizado | Interface final renderizada foi examinada nos contextos pertinentes; achados impeditivos tratados e limitações registradas. |
| Revisão de segurança pertinente | Riscos da superfície foram avaliados; quando exigido, Security Gate foi realizado com controles e evidências suficientes. Inaplicabilidade deve ser justificada. |
| Pronto para aprovação | Critérios essenciais atendidos, revisões exigidas concluídas, evidências e riscos reunidos para Gate B; validação essencial ausente impede este estado. |
| Publicado | Entrega autorizada foi executada e versão/destino registrados conforme Product System e Release/Deployment. |
| Verificado pós-entrega | Fluxos, renderização, configuração e sinais pertinentes foram conferidos no destino autorizado, com resultados e limitações registrados. |

A aprovação de layout não valida segurança, funcionamento, performance ou integridade do sistema. Estados podem ser parciais por superfície e precisam indicar seu alcance.

Uma tarefa pode terminar pronta para aprovação se publicação estiver fora do escopo. Não executar publicação ou acesso a produção para preencher o estado seguinte. Decisão humana e autorização de ações protegidas permanecem regidas pelo Product System.

## Q. Capability Routing

Selecionar o menor conjunto suficiente pelas superfícies realmente alteradas. Inspecionar Skills para compatibilidade de um Standard não significa ativá-las todas na execução de cada tarefa.

| Skill canônica | Selecionar quando | Responsabilidade nesta experiência |
| --- | --- | --- |
| `julian-premium-design` | Direção de arte, UX, hierarquia ou sistema visual precisam ser definidos/revistos. | Direção visual e arquitetura da experiência coerentes com o objetivo. |
| `clara-premium-copywriting` | Conteúdo de marca, oferta ou texto de interface está no escopo. | Copy, CTAs, instruções, estados e consistência factual. |
| `kael-interface-engineering` | Há implementação/correção de UI web ou local. | Componentes, layout, interação, estados e acessibilidade técnica. |
| `visual-interface-qa` | Há mudança visual relevante com interface renderizada para revisão. | Examinar experiência real e registrar achados; preferir revisor distinto. |
| `seo-technical` | Páginas públicas indexáveis ou sua descoberta técnica são afetadas. | Rotas, metadados, semântica, rastreamento e indexação. |
| `ai-search-visibility` | Conteúdo público tem objetivo de descoberta por busca com IA. | Identidade factual, consistência de entidades e compreensão do conteúdo. |
| `vera-architecture-security` | Permissões, dados sensíveis, integrações ou limites de confiança exigem análise especializada. | Riscos arquiteturais e segurança da superfície; Security Gate pertinente. |
| `quality-engineering-testing` | Comportamentos, contratos ou fluxos precisam de estratégia/execução de testes. | Evidências positivas, negativas, de integração e regressão proporcionais. |
| `release-deployment-reliability` | Preparação, publicação, distribuição ou verificação operacional integra o escopo. | Prontidão, entrega autorizada e recuperação; preparação não autoriza publicação. |
| `software-design-solid` | Lógica, módulos, serviços ou APIs são implementados/revistos. | Separação proporcional de responsabilidades e manutenção dos contratos. |
| `data-persistence-engineering` | Persistência, consultas, transações ou concorrência de dados são afetadas. | Integridade e desempenho dos dados que sustentam os fluxos. |
| `ai-engineering-production` | Modelos, agentes, RAG ou pipelines de IA integram a aplicação. | Qualidade e operação do componente de IA; não substitui AI Search Visibility público. |

Uma correção de rótulo pode precisar apenas de orientação editorial e verificação direta. Um cadastro com autorização e persistência exige capacidades adicionais conforme risco. Um dashboard privado não ativa SEO/GEO pelo fato de usar tecnologia web. Reavaliar roteamento se a superfície mudar, mantendo autorização e decisões existentes.

## R. Exceções, evidências e evolução

Aplicar proporcionalidade ao volume de documentação, profundidade de design e conjunto de testes. Não dispensar proteção de dados, autorização confiável, integridade ou validações essenciais para alegar rapidez.

Registrar exceção relevante no contexto autorizado: regra, motivo, alcance, risco, controle compensatório, responsável e condição de reavaliação. Ajuste rotineiro dentro do escopo não exige microaprovação; mudança material segue o Product System. Uma exceção de produto não altera silenciosamente este Standard.

Usar evidências reais e suficientes: telas renderizadas, resultados de tarefas, procedimentos, medições e respostas técnicas conforme a superfície. Não inventar métricas, testes, certificações, revisão independente ou conformidade. Separar observado, inferido e recomendado.

Na entrega, explicitar cobertura, limitações de ambiente ou ferramenta, validações pendentes e riscos residuais. Não substituir validação essencial indisponível por suposição. Preservar evidências sem dados sensíveis e dentro dos arquivos ou mecanismos autorizados.

Revisar este Standard diante de conflito, falha recorrente ou nova necessidade comprovada. A revisão deve identificar regra, evidência, impacto e compatibilidade com Product System e Skills, seguindo a governança de evolução do Product System. Não alterar outros documentos sem escopo próprio.

Futuras especializações, incluindo Authentication & Security, podem detalhar controles e procedimentos sem repetir este conteúdo nem enfraquecer o baseline. Até sua materialização, aplicar os documentos existentes pertinentes. A classificação Stable não substitui evidência de uso e validação operacional.

Revisão 1.1, Gate A de usabilidade de 13/10/2026: imagens conforme ferramentas disponíveis, assets locais, geração distinta de otimização e QA de site em navegador real. Preserva escopo e Gates; revisão documental não comprova execução de produto.

Revisão 1.2, autorizada no escopo de design e UI/UX: exploração de três direções, identidade contextual, tokens e aceite visual com crítica, correção e reinspeção. Nenhuma estética universal é criada; o julgamento editorial e o aceite humano continuam distintos de resultados técnicos.
