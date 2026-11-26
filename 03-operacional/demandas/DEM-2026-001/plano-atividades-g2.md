---
id: PLANO-DEM-2026-001-G2
titulo: "Plano de atividades para o G2 — DEM-2026-001 [TESTE]"
tipo: plano
versao: 1.1
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:50-03:00
atualizado_em: 2026-11-26T13:10-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, RM-0001, G1, G2, TASK-0003, TASK-0004, TASK-0005, TASK-0006, TASK-0007, TASK-0008, TASK-0009, TASK-0010, TASK-0011, TASK-0012, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0001, DEC-PO-0002, DEC-PO-0004, DEC-PO-0005, DEC-PO-0006, DEC-PO-0007, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0003, DEC-ARQ-0004, DEC-AS-0001, DEC-AS-0002, DEC-AS-0003, ADR-0001, ADR-0002, ADR-0003, AH-0001, EF-0001, ET-0001]
substitui: null
substituido_por: null
---

# Plano de atividades para o G2 — DEM-2026-001 [TESTE]

> Fase de testes internos; nada vai à produção. Fluxo 01, etapa C, estado "Em planejamento" (contexto.yaml v19, commit `ed35bdd`). G1 registrado em 26/11/2026 12:38 (America/Sao_Paulo) como **Aprovado com observações** (commit `b083eef`).
> Este documento **não** altera estado, etapa, gates, `contexto.yaml`, `aprovacoes.md` nem `Tarefas.csv` (só o ORQ). **Status: em-revisao** — o ciclo do protocolo (Rascunho → Em revisão → Vigente) só admite **vigente** depois que o G2 for decidido e o ORQ o registrar. Esta v1.1 é a referência para essa decisão; `aprovado_por` permanece vazio até lá.
> **Estimativas:** nenhuma foi inventada. Todas vêm dos pareceres de planejamento e já estão no Tarefas.csv (verificação do ORQ, 26/11 12:59). A estimativa é de quem executa; a decisão técnica é do ARQ.

## 1. Premissas e restrições (G1 e R3)

Condições do G1 (aprovacoes.md), que este plano respeita:

1. Formatos, caminhos 503/405/500, tempo limite de 5 s e tela sem login dependem dos ADR-0002/0003 **propostos**. Se mudarem no G3, o PO reabre os CA afetados.
2. Stack e implementação (TASK-0008 e a preparação da TASK-0012) **só após AH-0001** válida do Thiago. O G2 pode ser decidido antes da AH-0001; o G2 **não** substitui a AH.
3. A proposta técnica do ARQ (TASK-0003) segue **Parcial** até a AH-0001 (stack ainda proposta). O parecer consolidado de G2 (`d1b0235`) atende os critérios de fechamento definidos na v1.0 deste plano; os critérios originais (stack decidida) permanecem NOK.

Classe de risco **R3** (DEC-ARQ-0001) — requisitos mínimos a cumprir no plano, sem gravar gates:

- Testes de **segurança** (dirigidos + varredura) e de **desempenho**, além de unidade, integração, funcionais, regressão e contrato.
- **2ª aprovação do ARQ no G4** (além do parecer do CR; revisor ≠ autor).
- Janela de **observação de 24 h de calendário** (procedimento proposto pelo OPS no parecer da TASK-0012, seções 4.2–4.3).
- Plano de **rollback ensaiado no G6** (procedimento proposto pelo OPS, seção 4.1).
- AH de arquitetura já solicitada (AH-0001). Sem alteração de banco: DBA não é acionado (L9 fechada). Sem Mobile.

Escopo funcional vigente (commit `babb9fe`, com revisão editorial da US-0002 v1.3 neste pacote): US-0001 v1.2 e US-0002 v1.3, REQ-0001..0004 e RN-0001/0002 v1.2 — **vigentes**, com a ressalva (1) do G1. Público da tela confirmado pela CPO (DEC-PO-0002): operador/equipe técnica interna. Protótipo UX v1.0 aprovado com ressalvas (DEC-PO-0005).

Contrato OpenAPI 3.1 `portal-api` **1.0.0** está na **main**, status **proposto** (merge `--no-ff` `cf660fb`, autor AS, revisor ARQ). Isso **resolve o candidato a CONF** apontado pelo OPS (a v1.0 deste plano ainda descrevia o ramo como não mesclado). O merge **não é o G3**.

## 2. Fontes consultadas (IDs e versões)

- contexto.yaml v19 (26/11, commit `ed35bdd`); aprovacoes.md (G1); Tarefas.csv (espelho, estimativas gravadas pelo ORQ); historico.md (leitura).
- US-0001 v1.2 vigente (`babb9fe`); US-0002 v1.2 vigente no momento da consulta, corrigida editorialmente para v1.3 neste pacote (só o texto de público; CA inalterados).
- REQ-0001..0004, RN-0001/0002 v1.2 vigente; analise-po-task-0002.md v1.2 (lista de decisões do PO, acrescida da DEC-PO-0007 neste pacote).
- PARECER-ARQ-DEM-2026-001-G2 v1.0 vigente (`d1b0235`); DEC-ARQ-0001; DEC-ARQ-0002 v1.0 vigente; DEC-ARQ-0003 e DEC-ARQ-0004 (`b792363` / conteúdo em `d1b0235`).
- ADR-0001/0002/0003 v1.0 **propostos**.
- PARECER-G2-DEM-2026-001-TASK-0010 v1.0 vigente (`40c8ace`).
- Parecer FS: `rascunhos/fs/DEM-2026-001-TASK-0008-parecer-g2.md`. Parecer DOC: `rascunhos/doc/MSG-RET-ORQ-TASK-0011-parecer-g2.md`. Parecer OPS: `rascunhos/ops/DEM-2026-001-TASK-0012-parecer-g2.md`. Parecer CR: transcrito pelo ORQ na consolidação do G2 (estimativa e critério; 26/11 12:45).
- EF-0001 v1.2 em-revisao; ET-0001 **v1.3** em-revisao (`bb3e08a`: testabilidade do 500 por injeção na fábrica — proposta AS, confirmação do ARQ no G3). OpenAPI 1.0.0 proposto na main (`cf660fb`).
- DEC-AS-0001 (timeout 5 s, sem retry), DEC-AS-0002 (tolerância ±5 s), DEC-AS-0003.
- DEC-PO-0007 (26/11/2026 12:57, America/Sao_Paulo): libera o incremento A da TASK-0011. Registrada pelo ORQ no contexto v18 (`15259e7`) e no Tarefas.csv (início do incremento A 12:58).
- PROMPT do PO v1.0: Fluxo 01 etapa C; G2; DoR.

## 3. Situação das TASK já existentes

Não crio TASK novas (isso é do ORQ). Uso as TASK-0003 e 0007–0012 já registradas.

| TASK | Responsável | Estado (Tarefas.csv / contexto v19) | Papel neste plano |
|---|---|---|---|
| TASK-0001 | CPO | Concluída | G0 — encerrada |
| TASK-0002 | PO | Concluída | Análise inicial — encerrada |
| TASK-0003 | ARQ | **Parcial** | Parecer G2 consolidado (`d1b0235`); fecha após a AH-0001 (aceitação dos ADR) |
| TASK-0004 | UX | Concluída | Protótipo validado com ressalvas (DEC-PO-0005) |
| TASK-0005 | QA | Concluída | Testabilidade pré-G1, ajustes respondidos (DEC-PO-0006) |
| TASK-0006 | AS | Concluída | EF v1.2 / ET v1.3; residual do OpenAPI = **0 h** (já na main). Extensão do gancho do 500 (ET §7.4/§11) aberta com AS/ARQ até o G3 |
| TASK-0007 | ARQ | Aguardando dependências | Aprovação do contrato (G3); dependência **AH-0001** (já no Tarefas.csv) |
| TASK-0008 | FS | Aguardando dependências; **bloqueio AH-0001** | Implementação API + tela |
| TASK-0009 | CR | Aguardando dependências | Code Review (G4) + 2ª aprovação ARQ (R3) |
| TASK-0010 | QA | Aguardando dependências | Plano de testes, execução e PQ (G5) |
| TASK-0011 | DOC | **Em desenvolvimento (incremento A; DEC-PO-0007)**; incremento B aguarda TASK-0008 | Documentação em dois incrementos |
| TASK-0012 | OPS | Aguardando dependências; **bloqueio AH-0001** | Preparação após AH-0001, em paralelo à 0008; validação G6/G7 após o G5 |

## 4. Trabalho residual (não é TASK nova)

O residual da AS no OpenAPI (ajustes do DEC-ARQ-0002, rebase, retirada de `historico.md` do ramo) está **concluído** (`b3f13d6` + merge `cf660fb`). A TASK-0007 não espera mais esse residual. Se o ARQ pedir ajuste no G3, a AS estimou 0,5–1 h (Tarefas.csv, evidência da TASK-0006).

Permanece aberto com AS/ARQ, **sem bloquear o G2**: a confirmação no G3 da extensão da L-05 ao HTTP 500 (injeção só na fábrica de teste, fora da superfície do OpenAPI). A ET-0001 v1.3 já redige essa testabilidade como proposta da AS (`bb3e08a`).

Perguntas (a) e (b) do FS ao ARQ (parecer da TASK-0008) ficam até o G3. Porta, origem e comando de subida fecham na preparação da TASK-0012 (OPS propõe, FS confirma; valores só em `.env` fora do git). Nenhuma dessas lacunas impede a decisão do G2.

## 5. Decisões do PO nesta demanda

- **DEC-PO-0001** — Escopo e acionamentos (duas US; UX, AS, ARQ, FS, CR, QA, DOC e OPS enxuto; sem AN, DBA, MOB, PMM).
- **DEC-PO-0002** — Público da tela = operador/equipe técnica interna (confirmado pela CPO em 26/11/2026 12:36).
- **DEC-PO-0003** — Prioridade Normal apesar da fórmula (pontuação 2,4 provisória).
- **DEC-PO-0004** — Pontuação recalculada **2,8**; classe **Normal** mantida.
- **DEC-PO-0005** — Protótipo/spec UX v1.0: **Aprovado com ressalvas**.
- **DEC-PO-0006** — Ajustes QA/AS: alternativa A (503 no aceite); CA-08/CA-09; textos alinhados a R3.
- **DEC-PO-0007** — 26/11/2026 **12:57** (America/Sao_Paulo). O incremento **A** da TASK-0011 (**7 h**: L-CR2 1,5 h, fechamento formal do CONF-0001 0,5 h, L-09 3,5 h, L-UX-01 1,5 h) **pode começar já**, sem esperar a TASK-0008. Motivo: a L-CR2 é pré-requisito de entrada no G4 (RK-DOC-1); o incremento A não é N3 e não depende da AH-0001. O incremento **B** (**5,5 h**, documentação da versão) permanece após a TASK-0008, em paralelo à TASK-0010 (PR-06). O ORQ registrou a decisão no contexto v18 e atribuiu o incremento A à DOC (início 12:58).

## 6. Observações propostas para o G2

Estas observações consolidam as recomendações do ARQ e do OPS, a DEC-PO-0007 e os complementos do QA. Não são a decisão formal do gate (o PO a declara ao ORQ; o ORQ transcreve em aprovacoes.md):

- **(a)** A TASK-0008 e a **preparação** da TASK-0012 só começam após a AH-0001 válida. O OPS confirmou a preparação em paralelo à 0008. A validação formal (smoke, rollback ensaiado, observação) permanece após o G5. O G2 não substitui a AH.
- **(b)** O G3 (TASK-0007) só ocorre após a AH-0001. Se a AH ou o G3 alterar ADR ou contrato, o PO reabre os CA afetados (ressalva 1 do G1) e este plano é reavaliado antes da execução.
- **(c)** O PR da TASK-0008 e a entrada no G4 cumprem a **DEC-ARQ-0003** (o OPS confirmou o procedimento: orquestrador `/workspace/projetos/portal/scripts/verify-local.sh`, evidência sem segredos, reexecução pelo CR na box), a **DEC-ARQ-0004** (condicionada à aceitação do ADR-0001; revista se a stack mudar) e a **L-CR2** (incremento A da DOC, DEC-PO-0007). L-CR1/L-CR3 não bloqueiam a decisão do G2.
- **(d)** A **execução** da TASK-0010 depende de decisões do ARQ sobre varredura/SAST e método de p95 (proposta do OPS §7) e da calibração da meta inicial de **80% de cobertura** de linhas no código alterado (DEC-ARQ-0003, “a calibrar” com o QA no G5). Essas pendências não bloqueiam a decisão do G2; condicionam o PQ pleno.

## 7. Riscos relevantes para o G2

| ID | P×I / natureza | Tratamento |
|---|---|---|
| **RK-1** Stack sem confirmação | 3×2=**6 (alto)** (ARQ) | Mitigado pela observação (a): 0008 e preparação da 0012 não executam sem AH-0001 válida. Se a AH recusar ou mudar a stack, ADRs e este plano são reavaliados antes da execução. Suficiente para G2 com observações; não é aceitação do risco. |
| RK-2 Exposição pública | 1×3=3 | Condição no ADR-0003; reabre R3/N3. Não bloqueia o G2. |
| RK-3 npm/Fastify | 1×2=2 | Lockfile, `npm ci`, `npm audit` (DEC-ARQ-0003). |
| RK-CR1 evidência só do autor | apontado pelo CR | Mitigado: CR reexecuta `verify-local.sh` na box (DEC-ARQ-0003). |
| **RK-DOC-1** L-CR2 não implementada antes do G4 | prob. média / impacto alto (DOC) | Mitigado pela DEC-PO-0007: incremento A já liberado e em desenvolvimento, a concluir antes da entrada no G4. |

## 8. Plano por atividade (a executar)

Critérios abaixo são os de **conclusão da TASK**, verificáveis e ligados aos CA/REQ vigentes. Estimativas transcritas dos pareceres, com unidade e faixa.

**Lacuna de homogeneidade (não bloqueia o G2):** FS, CR, QA, DOC e OPS estimaram em **horas**. O ARQ usou a **escala 1–5** do PROMPT (1 = horas · 5 = semanas) para o residual da TASK-0003, a TASK-0007 e a 2ª aprovação no G4. As duas unidades não se somam. Pedido ao ORQ: solicitar ao ARQ a conversão dessas três estimativas para horas (faixa, se houver), sem o PO inventar a equivalência. Soma do que já está em horas, com o 2º ciclo de CR e sem a janela de 24 h nem o ARQ: **71,5 h** (verificação do ORQ).

### TASK-0003 — Análise técnica (fechamento) · ARQ (Ricardo)
- **Objetivo:** concluir a proposta técnica: aceitar ou rejeitar os ADR após a AH-0001 e preencher `tecnologias.md`. O parecer de G2 (`d1b0235`) já consolidou decisões, sequência, riscos e estimativas possíveis sem a AH.
- **Critérios de conclusão (originais, ainda NOK):** stack e estrutura decididas (ADR aceitos ou rejeitados com alternativa) e `tecnologias.md` preenchido. Até a AH-0001, a TASK permanece **Parcial**.
- **Dependências:** G1 (ok). Aceitação formal dos ADR depende da AH-0001.
- **Estimativa:** residual **1** (escala 1–5; ARQ). Após a AH, se a alternativa A for aceita: aceitar/rejeitar ADR-0001..0003 e preencher `tecnologias.md`. Se B ou Node 26: ainda escala 1, com revisão dos ADR (horas, no máximo um dia). Conversão para horas: lacuna, pedida ao ARQ via ORQ.
- **Bloqueio:** AH-0001 para fechar a TASK; não bloqueia o parecer nem um G2 com observações.

### TASK-0007 — Aprovação do contrato (G3) · ARQ (Ricardo)
- **Objetivo:** aprovar o contrato interno de `GET /health` (OpenAPI + ET) antes da implementação dependente (PR-04 / sequência obrigatória G3 → código).
- **Critérios de conclusão:** contrato alinhado a US-0001 CA-01..CA-09, REQ-0001, REQ-0004, RN-0001, ADR-0003 (quando aceito) e DEC-ARQ-0002; exemplos de 200, 503, 405 e 500; `additionalProperties: false`; sem dado sensível; CORS só da origem do Portal; parecer de G3 do ARQ registrado. Confirmação, no G3, da extensão da L-05 ao 500 (ET-0001 v1.3, proposta AS). Sem persistência: parecer do DBA = N/A, com justificativa. O merge `cf660fb` do contrato **proposto**, sozinho, não conclui esta TASK.
- **Dependências:** TASK-0006 (concluída) + **AH-0001**. Residual do OpenAPI concluído.
- **Estimativa:** **1** (escala 1–5; ARQ). Premissas: OpenAPI já na main (`cf660fb`); AH-0001 aprovada sem mudar as diretrizes; ET alinhada (hoje v1.3). Conversão para horas: lacuna, pedida ao ARQ via ORQ.
- **Bloqueio:** AH-0001.

### TASK-0008 — Implementação API `GET /health` + tela · FS (Lucas)
- **Objetivo:** implementar o provedor e o consumidor, com testes unitários, conforme US/REQ/RN vigentes, contrato aprovado (G3), protótipo/spec validados (DEC-PO-0005) e diretrizes do ARQ.
- **Critérios de conclusão:** PR com IDs (DEM/TASK/US) e trailer de agente; nota de análise (itens 1–9) anexada; US-0001 CA-01..CA-09 atendidos no código da API; US-0002 CA-01..CA-06 atendidos na tela (valores brutos + UTC no saudável; erro genérico; 503 **sem** exibir versão/timestamp — RE-02; carregando remove valores do DOM; recuperação pelo botão); testes unitários do serviço; ganchos de 503 e 500 **só na fábrica de teste**, nunca honrados fora de teste (DEC-ARQ-0002 L-05; ET-0001 §7.2/§7.4); cumprimento da DEC-ARQ-0003 e da DEC-ARQ-0004 no PR (observação (c)); nenhum segredo no repositório; implementação só na stack aprovada pela AH-0001. Fora: polling, Mobile, persistência.
- **Dependências (Tarefas.csv):** G2; G3; TASK-0004; **AH-0001**. O consumidor pode usar mocks do contrato **após** o G3 (PR-04).
- **Estimativa:** **22 h** (FS), premissa alternativa A do ADR-0001 e G3 sem reabrir CA. Se a AH adotar a alternativa **B**: **+6 h**.
- **DoR pendente de execução:** contrato G3 + stack aceita (AH-0001). Até lá a TASK não entra em desenvolvimento.
- **FS confirmou** os CA vigentes e o RE-02, sem propor alteração de critério ao PO.

### TASK-0009 — Code Review (G4) · CR (Eduardo) + 2ª aprovação ARQ
- **Objetivo:** revisar o código da TASK-0008 (revisor ≠ autor) e, por ser R3, obter a 2ª aprovação do ARQ.
- **Critérios de conclusão (conforme o CR):** o G4 só se encerra com parecer **CR Aprovado** ou **Aprovado com observações**, **mais** a **2ª aprovação explícita do ARQ**. **Reprovado** gera novo ciclo (correção do FS + nova revisão); não encerra a TASK. Limite de **2 ciclos** (1º ciclo 3 h + 2º ciclo 1 h se houver). Verificação de IDs no PR, ausência de segredos, aderência ao contrato aprovado, DEC-ARQ-0003 (script reexecutado pelo CR na box) e DEC-ARQ-0004. Observações não bloqueantes tratadas ou registradas como TD. Só então a versão segue ao QA (G5).
- **Dependências:** TASK-0008 (PR da versão candidata). **Entrada no G4:** DEC-ARQ-0003, DEC-ARQ-0004 e L-CR2 (incremento A da DOC) cumpridas.
- **Estimativa:** **3 h** no 1º ciclo + **1 h** se houver 2º ciclo (CR; premissa PR 300–600 linhas). 2ª aprovação do ARQ: **1** (escala 1–5; menor que o 1º ciclo do CR; disponível no mesmo dia útil do parecer do CR, só após CR favorável ou com observações não bloqueantes). Conversão da parcela do ARQ para horas: lacuna, pedida ao ARQ via ORQ.

### TASK-0010 — Plano de testes, testes e PQ (G5) · QA (Fernanda)
- **Objetivo:** planejar e executar os testes da demanda na versão aprovada no G4, com rastreio CA → CT, e emitir o PQ.
- **Critérios de conclusão:** PT/CT cobrindo **100% dos 15 CA vigentes** (US-0001 CA-01..CA-09 e US-0002 CA-01..CA-06); testes de contrato (200, 503, 405, 500, corpo inválido, timeout 5 s sem retry, tolerância do timestamp ±5 s, `additionalProperties: false`); **HEAD /health** no contrato, ligado ao CA-08; **CORS** (origem permitida e origem negada ⇒ erro caso (a) no navegador — não é CA novo); **acessibilidade** como verificação do CA-02 (informação não só por cor; checagens de apoio da spec UX: selo textual, `aria-live`/alerta — sem CA novo de a11y); testes dirigidos de **segurança** (RN-0001, REQ-0004, CA-05/CA-06, denylist, inclusive 405/503/500 e a tela nos três estados; no 503 a tela não exibe versão/timestamp); **varredura** de segurança local (os testes dirigidos não a substituem; ferramenta/método a decidir pelo ARQ com a proposta do OPS §7.1 — observação (d)); teste de **desempenho** com o alvo **indicativo** p95 ≤ 100 ms em execução local (não é SLO nem CA; ET-0001 RT-14); a primeira medição documentada vira **linha de base provisória** (não se aplica o +10% literal na primeira entrega); QA verifica a suíte unitária do FS e executa integração Portal↔API; regressão aplicável (suíte inicial = esta entrega); PQ-nnnn favorável (ou favorável com ressalvas aceitas pelo PO/ARQ), na versão do G4. `404` de rota inexistente e `OPTIONS` de preflight ficam como nota de contrato, fora do aceite dos 15 CA.
- **Dependências (Tarefas.csv):** TASK-0005 (concluída); TASK-0009 (G4). Execução condicionada a G3, G4 e às pendências P-QA-01..05 (ambiente, método p95, varredura R3, ganchos 503/500). P-QA-05 (OpenAPI ainda no ramo) foi **superada** pelo merge `cf660fb`; o G3 continua após a AH-0001. PT/CT definitivos após o contrato aprovado; rascunho pode começar com a ET vigente em revisão.
- **Estimativa:** **20 h** (faixa **16–23 h**; QA, `40c8ace`). Decomposição: PT+CT 8–11 h; execução 1º ciclo 6–8 h; retrabalho 2º ciclo 2–3 h (no máximo um ciclo de P2/P3); PQ 1,5–2 h. Não inclui a observação de 24 h nem o smoke/rollback (TASK-0012).
- **DoR pendente de execução:** ambiente do OPS; decisões do ARQ na observação (d).

### TASK-0011 — Documentação da versão · DOC (Beatriz)
- **Objetivo:** curadoria e padrões (incremento A) e documentação do endpoint e da tela (incremento B: G6 pronta, publicação no G8), em paralelo aos testes (PR-06) no que couber ao B.
- **Critérios de conclusão:**
  - **Incremento A (DEC-PO-0007, em andamento):** L-CR2 implementada (local `06-qualidade/pareceres/CR-nnnn-<slug>.md`, ponteiro na Evidência da TASK-0009, convenção/modelo/README e desdobramento da matriz 7.1 com CR = A nos pareceres CR); fechamento formal do CONF-0001 (lado PO já resolvido); L-09 (modelos de EF/ET/contrato e INDEX; o INDEX pode citar o OpenAPI 1.0.0 proposto na main, G3 pendente); L-UX-01 (prefixo na convenção; endosso do UX ao alias do artefato existente não bloqueia o G6). O incremento A deve terminar **antes da entrada no G4**.
  - **Incremento B:** documentação versionada do contrato `GET /health` e da tela de status, alinhada a US/REQ vigentes e ao contrato aprovado no G3; release notes da versão candidata; nenhum segredo; publicação final só após o G7 aplicável.
- **Dependências:** Incremento A — atribuição do ORQ (DEC-PO-0007); **sem** dependência da TASK-0008 nem da AH-0001. Incremento B — TASK-0008; paralelo à TASK-0010.
- **Estimativa:** **12,5 h** (faixa **11–14 h**; DOC): incremento A **7 h**; incremento B **5,5 h**.

### TASK-0012 — Execução local, smoke test e rollback · OPS (Diego)
- **Objetivo:** viabilizar a execução local de teste em `/workspace/projetos/`, validar ambiente e rollback no G6 e verificar a “implantação” local no G7 (não há produção neste teste).
- **Critérios de conclusão:** registro do ambiente local (como instalar, subir API e Portal em processos separados, variáveis só por **nome**, valores fora do git); origem do Portal e `PORTAL_API_ALLOWED_ORIGIN` definidos no ambiente (DEC-ARQ-0002 L-06; valores concretos na preparação, após a AH, via MSG-COL OPS→FS); orquestrador `scripts/verify-local.sh` conforme a DEC-ARQ-0003 (procedimento confirmado no parecer OPS §6); smoke test da versão candidata (pelo menos o caminho 200 e a tela saudável/erro); **plano de rollback ensaiado no G6** (passo a passo executado uma vez, com tempo cronometrado — parecer OPS §4.1); **observação de 24 h de calendário** após o “deploy” local no G7, com amostragem e relatório (parecer OPS §4.3; 1,5–2 h de trabalho ativo); Suporte informado se houver impacto operacional relevante (nesta fase, provavelmente N/A, com justificativa). Sem pipeline e sem custo.
- **Dependências (Tarefas.csv):** **AH-0001** (preparação, em paralelo à TASK-0008); **G5** (validação G6/G7). Sequência confirmada por OPS e ARQ.
- **Estimativa:** preparação **8 h** (faixa **6–10 h**) após a AH-0001, em paralelo à 0008; validação G6/G7 **5 h** ativas (faixa **4–7 h**) + **24 h de calendário** de observação R3 (não é esforço).
- **Propostas ao ARQ (observação (d), não bloqueiam o G2):** varredura/SAST (OPS §7.1) e medição do p95 (OPS §7.2, script Node embutido sem dependência nova).

### Atividades do PO (não são TASK novas)
- **G2 — decisão do planejamento:** Aprovado / Aprovado com observações / Reprovado, com referência a esta v1.1; o ORQ transcreve.
- **G6 — Pré-aceite funcional:** confirmar que os 15 CA vigentes foram evidenciados no PQ, com a ressalva (1) do G1 se o contrato no G3 tiver mudado.
- **G8 — Confirmação e encerramento:** critérios confirmados; documentação publicada; informar a CPO.

## 9. Sequência e paralelismo

```
[concluídas] TASK-0001..0002, 0004, 0005, 0006 (OpenAPI na main, proposto)
[parcial]    TASK-0003 ── parecer G2 ok; fecha após AH-0001

TASK-0011 incremento A (DEC-PO-0007) ── já em desenvolvimento; concluir antes do G4

G2 (PO, referência: esta v1.1) ─────────────────────────────┐
     (pode ser decidido antes da AH-0001)                   │
                                                            ▼
AH-0001 (Thiago, já solicitada) ──┬── TASK-0007 (G3)
                                  ├── TASK-0008 (FS)         [após G2, G3, AH-0001, TASK-0004]
                                  └── prep. TASK-0012 (OPS)  [paralela à 0008]
                                         │
                                         ▼
                                  TASK-0009 (CR+ARQ, G4)
                                    (exige DEC-ARQ-0003/0004 e L-CR2)
                                         │
                    ┌────────────────────┴────────────────────┐
                    ▼                                         ▼
              TASK-0010 (QA, G5)                    TASK-0011 incremento B (DOC)
                    ▼
              G6 (PO pré-aceite + OPS rollback ensaiado + DOC B pronta)
                    ▼
              TASK-0012 formal (smoke / G7 local) + observação 24 h de calendário
                    ▼
              G8 (PO) e informe à CPO
```

Regras: G1 → planejamento (esta etapa) → G3 (após AH-0001) → implementação dependente; implementação → G4 → G5; G5 + G6 → verificação local (G7) → G8. Paralelismo: incremento A da 0011 já corre; preparação do OPS ∥ TASK-0008 após AH-0001; incremento B da 0011 ∥ TASK-0010. Incidente P0 não se aplica (nada em produção).

## 10. Matriz resumida (DoR do G2)

| TASK | Responsável | Dependências | Bloqueios | Estimativa | Critérios (resumo) | DoR |
|---|---|---|---|---|---|---|
| 0003 | ARQ | G1 | AH-0001 para fechar (não para o parecer) | **1** (escala 1–5) | Parecer G2 ok; ADR aceitos após a AH | Parcial (stack) |
| 0007 | ARQ | 0006; **AH-0001** | AH-0001 | **1** (escala 1–5) | Contrato aprovado (G3) | Completa p/ planejar; execução após AH |
| 0008 | FS | G2; G3; 0004; **AH-0001** | **AH-0001**; G3 | **22 h** (alt. B +6 h) | PR + 15 CA + unitários + DEC-ARQ-0003/0004 + ganchos na fábrica | Completa p/ planejar; execução após AH+G3 |
| 0009 | CR (+ ARQ) | 0008 | Entrada: DEC-ARQ-0003/0004 e L-CR2 | **3 h + 1 h** (2º ciclo); 2ª apr. ARQ **1** (escala 1–5) | CR Aprovado ou Aprovado com observações + 2ª aprovação explícita do ARQ; Reprovado = novo ciclo; máx. 2 ciclos | Completa p/ planejar |
| 0010 | QA | 0005; 0009 | Execução: G3, G4, P-QA-01..04 e obs. (d) | **20 h** (16–23 h) | PT/CT 15 CA; HEAD; CORS; a11y no CA-02; segurança dirigida + varredura; p95 indicativo; PQ | Completa p/ planejar |
| 0011 | DOC | A: DEC-PO-0007; B: 0008 (∥ 0010) | A deve terminar antes do G4 | **12,5 h** (11–14 h): A 7 h; B 5,5 h | A: L-CR2, CONF-0001, L-09, L-UX-01; B: docs da versão | A em execução; B aguarda 0008 |
| 0012 | OPS | **AH-0001** (prep. ∥ 0008); G5 (G6/G7) | **AH-0001** | prep. **8 h** (6–10 h) + G6/G7 **5 h** (4–7 h) + **24 h** de calendário | Ambiente local; `verify-local.sh`; smoke; rollback ensaiado; observação 24 h | Completa p/ planejar; execução após AH / G5 |

## 11. Situação perante o G2

O G2 exige (PROMPT): atividades com ID, responsável, dependências, **estimativa** e critérios de conclusão; **decisões arquiteturais consolidadas**.

Agora há: IDs e responsáveis; dependências e bloqueios alinhados ao Tarefas.csv (AH-0001 na 0007; DOC A/B; preparação OPS ∥ 0008); critérios atualizados (CR, QA, RE-02, DEC-ARQ-0003/0004, L-CR2); requisitos R3; sequência confirmada por ARQ e OPS; parecer técnico consolidado do ARQ; estimativas de todos os executores.

Nada disso **impede** um G2 **Aprovado com observações** (a)–(d). O ARQ declarou que as decisões já registradas bastam para esse resultado, não para um G2 incondicional (ADR ainda propostos; TASK-0003 Parcial até a AH-0001). A AH-0001 **não** é pré-requisito da decisão.

Lacunas que permanecem, **sem bloquear** a decisão:

1. Homogeneidade das estimativas do ARQ (escala 1–5 vs. horas) — conversão pedida ao ARQ via ORQ.
2. AH-0001 ainda sem decisão do Thiago — condição das observações (a) e (b), não do gate em si.
3. Confirmação no G3 da extensão da L-05 ao 500 (ET-0001 v1.3, proposta AS) e perguntas do FS ao ARQ.
4. Porta, origem e comando de subida (OPS/FS, na preparação após a AH).
5. Decisões do ARQ sobre SAST/varredura, método de p95 e calibração dos 80% (observação (d); P-QA-02/03).
6. L-CR2 em implementação no incremento A (DEC-PO-0007); deve estar pronta antes do G4, não antes do G2.
7. L1 (visão de produto, CPO) permanece premissa de teste.

Quando o PO declarar o G2 e o ORQ o registrar, esta v1.1 pode ser promovida a **vigente** (mesmo conteúdo, só o status e `aprovado_por`). Até lá permanece em-revisao.

## 12. Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 12:50 (America/Sao_Paulo) | PO | Primeira versão para despacho dos pareceres de planejamento (etapa C, pré-G2). Commit `4814277`. |
| 1.1 | 26/11/2026 13:10 (America/Sao_Paulo) | PO | Incorpora os pareceres, as estimativas (com unidade e faixa), a DEC-PO-0007, o critério do CR, os complementos do QA, o OpenAPI na main (`cf660fb`), as observações (a)–(d), RK-1 e RK-DOC-1. Referência para a decisão do G2. |
