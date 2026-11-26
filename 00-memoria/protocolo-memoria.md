# Protocolo de Memória da Stack e regras de leitura/escrita

> Versão 1.0 · 26/11/2026 · gerado a partir dos Prompts 01–04 da Stack Multiagentes (Prompt 04, Anexo A, tem prioridade).

## 1. Protocolo de Memória (copiado nos 16 PROMPT.md)

```
PROTOCOLO DE MEMÓRIA DA STACK — COPIAR PARA O CONTEXTO GLOBAL
FONTES DE VERDADE:
- Conhecimento permanente e técnico: repositório Git “stack-conhecimento”. FASE ATUAL: a fonte de verdade é o repositório Git LOCAL em /workspace/stack-memoria/stack-conhecimento (sem remoto até o GitHub ser conectado; depois, o GitHub passa a ser a cópia principal e a pasta local, o espelho de trabalho). Pastas: 00-memoria, 01-institucional, 02-tecnica, 03-operacional, 04-incidentes, 05-releases, 06-qualidade, 07-agentes, 08-arquivo, modelos.
- Estado operacional (demandas, US, TASK, status, bloqueios): planilha “Stack Multiagentes — Operação” (Google Sheets; na fase atual, espelho CSV em /workspace/stack-memoria/planilha-operacao/) para o status operacional, e 03-operacional/demandas/<ID>/contexto.yaml para o contexto consolidado. Só o Orquestrador grava estado, etapa, tarefas e aprovações (G0–G8).
- Sua memória nativa: apenas conhecimento da sua especialidade, preferências de trabalho e ponteiros (ID + caminho + versão). Nunca a única cópia de algo que outro agente precise.
ANTES DE QUALQUER ATIVIDADE (RECUPERAÇÃO DE CONTEXTO):
- 1) Identifique a demanda (DEM/INC) e a TASK; 2) consulte o institucional pertinente; 3) leia contexto.yaml e o histórico da demanda; 4) identifique ADRs e decisões relacionadas; 5) consulte a documentação técnica aplicável; 6) veja atividades anteriores; 7) verifique bloqueios e dependências; 8) só então execute.
- Sempre atualize antes de ler ou editar: com remoto, git pull; sem remoto (fase atual), confira git status e git log e releia o arquivo no momento da edição, porque outros agentes escrevem na mesma pasta.
- Se faltar informação, NÃO invente: registre em pendencias_contexto e peça ao dono da informação.
AO ESCREVER:
- Escreva apenas nas áreas da sua alçada (matriz de leitura/escrita). Áreas protegidas: por PR aprovado pelo dono (fase atual, sem GitHub: PR local = ramo doc/<ID>-slug + MSG-COL ao dono, que aprova com merge --no-ff); você não aprova sua própria alteração crítica.
- Use os modelos da pasta “modelos/”, o frontmatter padrão (id, versao, status, dono, autores, datas, revisar_ate, relacionados) e IDs do padrão da Stack (DEM, INC, REQ, RN, US, TASK, EF, ET, ADR, DEC, BUG, REL, CR, PQ, PT, CT, RB, KB, PRB, TD, CONF, AH, RM; CA-nn é local à US).
- Nunca altere decisão estratégica ou ADR aceito de outro dono: proponha nova decisão. Históricos são append-only.
- Commits e PRs citam os IDs e terminam com o trailer “Agente: <sua sigla>”.
- Informação da sua memória individual que influencie outro agente deve ser publicada na área compartilhada e comunicada a ele.
CONSISTÊNCIA:
- Viu algo desatualizado ou conflitante em conteúdo de outro dono? Não corrija: registre CONF-nnnn em 00-memoria/conflitos e avise o dono.
- Em conflito não resolvido, prevalece: ADR aceito > padrão vigente > especificação > contexto da demanda > memória individual.
SEGURANÇA:
- Nunca grave segredos, tokens, senhas, dados pessoais ou dados de produção em nenhuma memória, prompt, arquivo ou mensagem. Credenciais ficam no cofre ou como segredo mascarado; registre apenas o nome da variável.
NO RETORNO (MSG-RET):
- Liste as fontes consultadas (IDs e versões), os artefatos criados/alterados (caminho e versão) e as lacunas de contexto.
PASTAS COMPARTILHADAS (fase atual):
- /workspace/stack-memoria/stack-conhecimento/ — repositório Git local (memória oficial). Sua pasta de agente: 07-agentes/NN-sigla/ (nos documentos, 07-agentes/<sigla> equivale a ela).
- /workspace/stack-memoria/pacotes-contexto/<DEM>/<TASK>.md — pacotes de contexto gerados pelo Orquestrador (descartáveis).
- /workspace/stack-memoria/rascunhos/<sigla>/ — rascunhos antes do commit (descartáveis, nunca única cópia de algo importante).
- /workspace/stack-memoria/planilha-operacao/ — espelho CSV da planilha, uma aba por arquivo.
- Regra de leitura: como a pasta compartilhada não separa o acesso por agente, ler a memória operacional de demandas em que você não atua é uma regra de conduta que você respeita; por isso nada sensível é guardado ali.
PROTOCOLO COMPLETO, MATRIZ DE ESCRITA E MODELOS: /workspace/stack-memoria/stack-conhecimento/00-memoria/protocolo-memoria.md e /workspace/stack-memoria/stack-conhecimento/modelos/.
```

## 2. Regras de leitura e escrita

| ID | Regra |
|---|---|
| RL-01 | Leitura: todo agente pode ler institucional, técnica, incidentes e releases; a memória operacional é lida pelos agentes envolvidos na demanda (e por CPO, PO, Arquiteto, Suporte e Orquestrador para coordenação). Como o computador compartilhado não segrega acesso por agente (a confirmar), a restrição de leitura operacional é uma regra de conduta, não um bloqueio técnico — por isso nada sensível é armazenado na memória. |
| RL-02 | Antes de produzir qualquer análise, o agente executa a recuperação de contexto (seção 8) e cita as fontes consultadas (IDs e versões) no MSG-RET. |
| RL-03 | Nenhum agente inventa informação ausente: se não está na memória nem foi recebida, é registrada em pendencias_contexto e solicitada ao dono. |
| EL-01 | Escrita em área protegida (marcada A na matriz) só por PR aprovado pelo dono; o autor nunca aprova a própria alteração crítica (regra do Prompt 01). |
| EL-02 | Decisões estratégicas (CPO) e arquiteturais (ADR aceito) não são alteradas por ninguém além do dono; mudança = nova decisão que substitui a anterior (status “substituído por ADR-nnnn”). |
| EL-03 | historico.md e linha-do-tempo.md são append-only: corrige-se com nova entrada, nunca apagando. |
| EL-04 | Toda escrita registra autor (sigla), data/hora (America/Sao_Paulo), ID relacionado e motivo — no frontmatter e no commit (trailer “Agente: <sigla>”). |
| EL-05 | Informação da memória individual que influencie outro agente é promovida para a área compartilhada no mesmo dia em que for produzida, e o agente afetado é avisado (MSG-COL). |
| EL-06 | Proibido gravar segredos, tokens, senhas, dados pessoais não anonimizados ou dados de produção em qualquer camada de memória. |
| EL-07 | O Orquestrador é o único que altera estado, etapa e aprovações no contexto da demanda; os demais agentes escrevem seus resultados, e o Orquestrador consolida. |

## 7.1 Matriz de escrita e aprovação por área
A = dono (aprova o PR e responde pelo conteúdo) · E = escreve/propõe (via PR nas áreas protegidas) · vazio = somente leitura. Leitura liberada a todos, exceto a memória operacional (agentes da demanda e coordenação, ver RL-01). Siglas: ORQ = Orquestrador; demais conforme o Prompt 01.
| Área | ORQ | CPO | PO | PMM | AN | AS | UX | ARQ | FS | MOB | DBA | OPS | QA | CR | DOC | SUP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-institucional / produto e objetivos |  | A | E | E |  |  |  |  |  |  |  |  |  |  |  |  |
| 01-institucional / regras de negócio (RN) |  |  | A |  | E | E |  |  |  |  |  |  |  |  |  |  |
| 01-institucional / arquitetura, padrões, tecnologias |  |  |  |  |  | E |  | A | E | E | E | E |  | E |  |  |
| 01-institucional / bancos e ambientes |  |  |  |  |  |  |  | E |  |  | A | A |  |  |  |  |
| 01-institucional / segurança e LGPD |  |  |  |  |  |  |  | A |  |  | E | E |  | E |  |  |
| 02-tecnica / ADR |  |  |  |  |  | E |  | A | E | E | E | E |  |  |  |  |
| 02-tecnica / contratos de API |  |  |  |  |  | E |  | A | E | E |  |  |  |  |  |  |
| 02-tecnica / especificações EF/ET |  |  | E |  |  | A |  | E |  |  |  |  |  |  |  |  |
| 02-tecnica / modelos de dados |  |  |  |  |  |  |  |  | E | E | A |  |  |  |  |  |
| 02-tecnica / configurações e implantação |  |  |  |  |  |  |  | E |  |  |  | A |  |  |  |  |
| 02-tecnica / débitos técnicos |  |  |  |  |  |  |  | A | E | E | E | E | E | E |  |  |
| 03-operacional / contexto e histórico da demanda | A |  | E |  | E | E | E | E | E | E | E | E | E | E | E | E |
| 03-operacional / US, REQ, critérios de aceite |  |  | A |  | E | E |  |  |  |  |  |  | E |  |  |  |
| 04-incidentes / incidentes, KB, problemas |  |  |  |  |  |  |  | E | E | E | E | E |  |  | E | A |
| 04-incidentes / runbooks |  |  |  |  |  |  |  |  |  |  | E | A |  |  |  | E |
| 05-releases |  |  |  |  |  |  |  |  |  |  |  | A | E |  | E |  |
| 06-qualidade (planos, casos, BUG, PQ) |  |  |  |  |  |  |  |  | E | E |  |  | A |  |  | E |
| 07-agentes/<sigla> | E | E | E | E | E | E | E | E | E | E | E | E | E | E | E | E |
| 00-memoria, modelos, skills (curadoria) | E |  | E |  |  |  |  | E |  |  |  |  |  |  | A |  |

### Matriz de escrita e aprovação por área

A = dono (aprova o PR e responde pelo conteúdo) · E = escreve/propõe (via PR nas áreas protegidas) · vazio = somente leitura. Leitura liberada a todos, exceto a memória operacional (agentes da demanda e coordenação, ver RL-01). Siglas: ORQ = Orquestrador; demais conforme o Prompt 01.
| Área | ORQ | CPO | PO | PMM | AN | AS | UX | ARQ | FS | MOB | DBA | OPS | QA | CR | DOC | SUP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-institucional / produto e objetivos |  | A | E | E |  |  |  |  |  |  |  |  |  |  |  |  |
| 01-institucional / regras de negócio (RN) |  |  | A |  | E | E |  |  |  |  |  |  |  |  |  |  |
| 01-institucional / arquitetura, padrões, tecnologias |  |  |  |  |  | E |  | A | E | E | E | E |  | E |  |  |
| 01-institucional / bancos e ambientes |  |  |  |  |  |  |  | E |  |  | A | A |  |  |  |  |
| 01-institucional / segurança e LGPD |  |  |  |  |  |  |  | A |  |  | E | E |  | E |  |  |
| 02-tecnica / ADR |  |  |  |  |  | E |  | A | E | E | E | E |  |  |  |  |
| 02-tecnica / contratos de API |  |  |  |  |  | E |  | A | E | E |  |  |  |  |  |  |
| 02-tecnica / especificações EF/ET |  |  | E |  |  | A |  | E |  |  |  |  |  |  |  |  |
| 02-tecnica / modelos de dados |  |  |  |  |  |  |  |  | E | E | A |  |  |  |  |  |
| 02-tecnica / configurações e implantação |  |  |  |  |  |  |  | E |  |  |  | A |  |  |  |  |
| 02-tecnica / débitos técnicos |  |  |  |  |  |  |  | A | E | E | E | E | E | E |  |  |
| 03-operacional / contexto e histórico da demanda | A |  | E |  | E | E | E | E | E | E | E | E | E | E | E | E |
| 03-operacional / US, REQ, critérios de aceite |  |  | A |  | E | E |  |  |  |  |  |  | E |  |  |  |
| 04-incidentes / incidentes, KB, problemas |  |  |  |  |  |  |  | E | E | E | E | E |  |  | E | A |
| 04-incidentes / runbooks |  |  |  |  |  |  |  |  |  |  | E | A |  |  |  | E |
| 05-releases |  |  |  |  |  |  |  |  |  |  |  | A | E |  | E |  |
| 06-qualidade (planos, casos, BUG, PQ) |  |  |  |  |  |  |  |  | E | E |  |  | A |  |  | E |
| 07-agentes/<sigla> | E | E | E | E | E | E | E | E | E | E | E | E | E | E | E | E |
| 00-memoria, modelos, skills (curadoria) | E |  | E |  |  |  |  | E |  |  |  |  |  |  | A |  |

Nota: nesta fase, as pastas de agente são `07-agentes/NN-sigla/`.

## 3. Versionamento

| Artefato | Mecanismo | Ciclo de status |
|---|---|---|
| Documentos Markdown (institucional, técnica, KB, runbooks) | Git: cada alteração é um commit; versão do documento no frontmatter (versao: 1.3) incrementada a cada mudança de conteúdo | Rascunho → Em revisão → Vigente → Obsoleto/Substituído |
| ADR | Imutável após “Aceito”; alteração = novo ADR que substitui (campo substitui/substituido_por) | Proposto → Aceito → Substituído/Rejeitado |
| Contratos de API | Versionamento semântico (MAJOR.MINOR.PATCH); CHANGELOG por serviço; quebra de compatibilidade exige MAJOR e ADR | Rascunho → Aprovado → Publicado → Depreciado |
| Especificações EF/ET | Versão v1, v2… no frontmatter; a demanda referencia a versão usada | Rascunho → Aprovada → Substituída |
| Contexto da demanda | versao_contexto incrementada pelo Orquestrador; historico.md append-only | Segue os estados do ciclo de vida (Prompt 02) |
| Releases | Tag Git por release e REL-nnnn ligando versões dos serviços/app | Planejada → Implantada → Revertida |
| Ramificação | main protegida; ramos curtos doc/<ID>-slug; PR com revisão do dono; squash com mensagem contendo IDs | — |

FRONTMATTER PADRÃO DE TODO DOCUMENTO
---
id: ADR-0031
titulo: "Upload de anexos via URL pré-assinada"
tipo: adr                      # adr | rn | req | us | task | ef | et | kb | rb | rel | inc | bug | pq ...
versao: 1.0
status: aceito                 # rascunho | em-revisao | vigente/aceito | obsoleto | substituido
dono: ARQ                      # sigla do agente responsável pelo conteúdo
autores: [ARQ, AS]
aprovado_por: ARQ
criado_em: 2026-11-27T09:40-03:00
atualizado_em: 2026-11-27T11:15-03:00
revisar_ate: 2027-05-27        # data-limite de revisão (desatualização)
relacionados: [DEM-2026-041, ET-0088, REQ-0103]
substitui: null
substituido_por: null
---

## 4. Recuperação de contexto

Processo obrigatório antes de qualquer atividade (seção 8 do Prompt 03), implementado pela skill “recuperar-contexto”:
| Passo | Ação | Onde consultar |
|---|---|---|
| 1. Identificar a demanda | ID (DEM/INC) e TASK recebidos na MSG-SOL; se ausentes, pedir ao Orquestrador | MSG-SOL |
| 2. Consultar o contexto institucional | Trechos de 01-institucional relevantes à especialidade e aos componentes da demanda | INDEX.md, catálogos YAML |
| 3. Consultar o histórico da demanda | contexto.yaml (versão atual) + últimas entradas de historico.md | 03-operacional/<DEM>/ |
| 4. Identificar decisões relacionadas | ADR e DEC listados em decisoes + busca por componente em 02-tecnica/adr | 02-tecnica/adr/, historico.md |
| 5. Consultar documentação técnica aplicável | Contratos, EF/ET, modelos de dados, padrões, runbooks | 02-tecnica/, 04-incidentes/runbooks |
| 6. Identificar atividades anteriores | TASKs concluídas da demanda e, quando útil, demandas/incidentes anteriores do mesmo componente | Backlog, 03-operacional, 04-incidentes |
| 7. Verificar bloqueios e dependências | bloqueios, dependências e gates pendentes no contexto e no backlog | contexto.yaml, backlog |
| 8. Iniciar a execução | Somente após entender o necessário; registrar no MSG-RET as fontes consultadas e as lacunas | — |
Quando não houver informação suficiente, o agente registra a lacuna em pendencias_contexto, envia MSG-COL ao dono da informação e, se a lacuna impedir a atividade, abre MSG-BLQ do tipo “Informação ausente” (Prompt 02).

## 5. Atualização e consistência

| ID | Regra |
|---|---|
| PC-01 | Fonte única (SSOT): cada tipo de informação tem um único lugar oficial (tabela “fontes-de-verdade.md”); nas demais camadas só ficam ponteiros (ID + caminho + versão). |
| PC-02 | Atualização na origem: quem altera algo atualiza a fonte de verdade primeiro e, em seguida, avisa os afetados; nunca corrige apenas uma cópia. |
| PC-03 | Validade: todo documento vigente tem revisar_ate; uma rotina semanal lista os vencidos e abre aviso ao dono. Documento vencido continua válido, mas recebe a marca “revisão pendente”. |
| PC-04 | Desatualização detectada por um agente: ele não corrige conteúdo de outro dono; registra CONF-nnnn (tipo “desatualizado”) e avisa o dono. |
| PC-05 | Conflito entre fontes: registrar CONF-nnnn com as duas fontes, o impacto e o dono; enquanto não resolvido, prevalece o documento aprovado mais recente na hierarquia: ADR aceito > padrão vigente > especificação > contexto da demanda > memória individual. |
| PC-06 | Conflito de versão no Git (dois agentes editando o mesmo arquivo): sempre git pull antes de editar; conflito de merge é resolvido pelo dono do documento, nunca descartando a alteração do outro sem registro. |
| PC-07 | Alterações concorrentes no contexto da demanda: só o Orquestrador grava estado/aprovações; executores escrevem em seções próprias (resultados, evidências). |
| PC-08 | Encerramento: ao concluir uma demanda, o Orquestrador e o Analista de Documentação promovem para 01/02/04 o que virou conhecimento permanente e movem a pasta para 08-arquivo/ (mantendo o ID). |
| PC-09 | Revisão periódica: trimestral para 01-institucional; a cada release para contratos e configurações; a cada incidente S1/S2 para runbooks e KB. |

## 6. Segurança e integridade

A memória não é repositório de segredos em texto aberto. Credenciais, senhas e secrets ficam em mecanismos de gerenciamento de segredos, nunca em prompts ou na memória compartilhada.
| Tema | Regra | Responsável |
|---|---|---|
| Credenciais e senhas | Somente no cofre (vault) do Grok Bot ou como segredo mascarado exposto como variável de ambiente; na memória, apenas o NOME da variável (ex.: GIT_TOKEN_STACK). Nunca em prompts, memória nativa, arquivos ou mensagens. | DevOps |
| Tokens de acesso | Escopo mínimo (somente os repositórios necessários), validade definida e rotação periódica; revogação imediata se expostos (incidente S1 de segurança). | DevOps / Arquiteto |
| Dados pessoais (LGPD) | Proibido armazenar dados pessoais de clientes/usuários na memória; evidências e logs anonimizados ou mascarados antes de gravar; exemplos usam dados fictícios. | Todos; Arquiteto e DBA definem regras |
| Controle de acesso | GitHub: branch protegida, CODEOWNERS por pasta, PR obrigatório nas áreas protegidas. Computador compartilhado: sem segregação por agente verificada (a confirmar) → conteúdo sensível não é guardado ali. | DevOps / Documentação |
| Segregação de ambientes | Configurações documentadas por ambiente (dev, hml, prd) apenas com nomes de variáveis e parâmetros não sensíveis; dados de produção nunca copiados para a memória. | DevOps |
| Auditoria | Histórico do Git (autor, data/hora, trailer “Agente:”), revisões de PR, historico.md append-only e registros de mensagens. | Documentação / Orquestrador |
| Retenção | Demandas concluídas: movidas para 08-arquivo/ e mantidas; evidências com dados operacionais: sanitizadas; prazos formais de retenção definidos na Etapa 4 — Governança (a confirmar). | Documentação |
| Recuperação de dados | Repositório remoto no GitHub = cópia principal; o clone no computador compartilhado é descartável e recriável; Pages/Library são visões regeneráveis. | DevOps |
| Prevenção de alterações não autorizadas | PR com aprovação do dono, proteção da main, ADR imutável, histórico append-only e verificação semanal de diffs em áreas protegidas por rotina. | Arquiteto / Documentação |
