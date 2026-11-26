---
id: PLANO-DEM-2026-001-G2
titulo: "Plano de atividades para o G2 — DEM-2026-001 [TESTE]"
tipo: plano
versao: 1.2
status: vigente
dono: PO
autores: [PO]
aprovado_por: "PO (G2 Aprovado com observações — mantido com ajuste, DEM-2026-001; registrado pelo ORQ em aprovacoes.md, 8017a7d)"
criado_em: 2026-11-26T12:50-03:00
atualizado_em: 2026-11-26T15:46-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, RM-0002, G1, G2, G3, TASK-0003, TASK-0004, TASK-0005, TASK-0006, TASK-0007, TASK-0008, TASK-0009, TASK-0010, TASK-0011, TASK-0012, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0001, DEC-PO-0002, DEC-PO-0004, DEC-PO-0005, DEC-PO-0006, DEC-PO-0007, DEC-PO-0008, DEC-PO-0009, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-ARQ-0011, DEC-AS-0001, DEC-AS-0002, DEC-CPO-0001, AH-0003, ADR-0001, ADR-0002, ADR-0003]
substitui: null
substituido_por: null
---

# Plano de atividades para o G2 — DEM-2026-001 [TESTE] — v1.2

> Fase de testes internos; nada vai à produção. Fluxo 01, responsável do fluxo: PO; classe de risco **R3** (DEC-ARQ-0001); prioridade Normal; pontuação 2,8. Estado da demanda: "Aprovada para execução" (contexto.yaml v37).
> **Status: vigente** desde 26/11/2026 15:46 (America/Sao_Paulo): o G2 foi decidido pelo PO como **Aprovado com observações — mantido com ajuste** (a)–(f) e registrado pelo ORQ em aprovacoes.md (commit `8017a7d`). O conteúdo é o da v1.2 em revisão (`7d85a6e`); mudaram só o status, `aprovado_por` e o alinhamento da numeração das observações da §7 com o MSG-RET registrado ((e)=DEC-PO-0009, (f)=RM-0002; o item de estimativas passou a (g)). A v1.1 permanece no histórico em `f61a1f9`.
> Este documento **não** altera estado, etapa, gates, tarefas, `contexto.yaml`, `historico.md`, `aprovacoes.md` nem `Tarefas.csv` (só o ORQ). **Nada aqui foi inventado:** cada número vem de um parecer ou de uma mensagem de retorno do executor/ARQ citada; onde faltou dado, há lacuna registrada na seção 11. Quem produz não aprova; "Concluída" só aparece onde há evidência verificável no repositório (senão "Parcial").
> Motivo da v1.2: a **AH-0003** (Thiago, 26/11/2026 14:54, substitui a AH-0001) trocou a stack para **C#/.NET 10 LTS (ASP.NET Core Minimal APIs) + Angular 22.3** (ADR-0001 v2.0, `d40518e`; ADR-0002/0003 v1.1; G3 aprovado com ressalvas R1..R5, `a271ac1`). Todas as estimativas de TASK-0008..0012 foram refeitas pelos donos, e o ARQ refez as próprias em horas.

## 1. Premissas, condições do G1 e requisitos R3

Condições do G1 (aprovacoes.md) e situação hoje:

1. Formatos, caminhos 503/405/500, tempo limite de 5 s e tela sem login dependiam dos ADR-0002/0003 propostos. **Atendida:** ADR-0002/0003 v1.1 **aceitos** no G3 (`a271ac1`). A DEC-PO-0008 decidiu **não reabrir os 15 CA**. O CA-04 é agnóstico de stack (manifesto = `<Version>` do `.csproj`, igual à tag `portal-api-v<ver>`). O **CA-07** segue válido, como **risco** ligado ao spike R4 do G3 (seção 8).
2. Stack e implementação só após AH válida do Thiago. **Atendida pela AH-0003** (aprovada em 26/11/2026 14:54, literal "Aprovo AH-0003"). A AH-0001 foi substituída. O G2 continua **não** substituindo AH.
3. TASK-0003 Parcial até a AH. **Encerrada:** TASK-0003 **Concluída** (ADR-0001 v2.0 aceito, `tecnologias.md` v1.1 vigente).

Classe **R3** — requisitos mínimos que o plano cumpre, sem gravar gates (DEC-ARQ-0001):

- Testes de **segurança** (dirigidos + varredura) e de **desempenho**, além de unidade, integração, funcionais, regressão e contrato.
- **2ª aprovação do ARQ no G4**, além do parecer do CR (revisor ≠ autor).
- **Observação de 24 h de calendário** (TASK-0012).
- **Rollback ensaiado no G6** (TASK-0012).
- **AH de arquitetura** (N3): AH-0003 aprovada. Sem alteração de banco (DBA não é acionado). Sem Mobile.

Stack e decisões técnicas vigentes (fonte: ARQ, `d40518e`, `a271ac1`): versão lida de `<Version>` no `.csproj` com `IncludeSourceRevisionInInformationalVersion=false`, SemVer sem *build metadata*, tag `portal-api-v<ver>`, resposta = manifesto = tag (ADR-0002 v1.1); contrato de `/health` inalterado — 200/503/405/500, `no-store`, `nosniff`, CORS, `Allow: GET, HEAD` (ADR-0003 v1.1); OpenAPI **1.0.0** inalterado; **DEC-ARQ-0007..0010** substituem 0003..0006 (`verify-local` A1–A5 e W1–W5; analyzers e `dotnet format`; Coverlet ≥ 80% de linhas; NuGet Audit; angular-eslint; `ng test` com Vitest/jsdom; p95 com a API em Release — 50 aquecimentos + 200 sequenciais, ≤ 100 ms indicativo); **DEC-ARQ-0011**: o gancho do 500 (L-12) só via `WebApplicationFactory`.

Escopo funcional vigente: **duas US, 15 CA** — US-0001 **v1.4** (correção editorial de referência: "ADR proposto" → "ADR v1.1, aceito" nos CA-04/07/08/09; **nenhum CA muda**) e US-0002 v1.4; REQ-0001..0004 e RN-0001/0002 v1.3 (`a20fe82`). Público da tela: operador/equipe técnica interna (DEC-PO-0002). Protótipo UX aprovado com ressalvas (DEC-PO-0005). Contrato OpenAPI 1.0.0 na main; a R1 do G3 só trocou prosa e `x-stack` (merge `e34e6b9`).

## 2. Fontes consultadas (IDs, versões e commits)

- **Estado/contexto:** `contexto.yaml` v37 (`6a1c810`); `aprovacoes.md` (G0–G3, AH-0001..0003); `historico.md` (leitura); `Tarefas.csv` (espelho; leitura). Estado operacional: **Normal**.
- **ARQ:** `07-agentes/07-arq/parecer-tecnico-DEM-2026-001-g2.md` (`d1b0235`); `parecer-tecnico-DEM-2026-001-g3.md` (`7bc37ba`; merge `a271ac1`; adendo/v1.2 no merge `edc9467`); `analise-impacto-troca-stack-DEM-2026-001.md` (`7fa2b43`); ADR-0001 v2.0 (`d40518e`), ADR-0002/0003 v1.1; DEC-ARQ-0007..0011; horas do ARQ em MSG-RET de 26/11 (TASK-0003 residual, TASK-0007, 2ª aprovação no G4; transcritas em `Tarefas.csv`). A conversão do ARQ para horas da v1.1 (`458acb8`: 1–3, 2–4 e 1–2 h, era Node) está **superada** pelos números AH-0003.
- **AS:** ET-0001 **v1.4** e EF-0001 v1.3 (`ac391ea`; merge `9b3dc1b`); OpenAPI 1.0.0 com prosa da R1 (`8494060`; merge `e34e6b9`). R1 **fechada** pelo ARQ (merges `e34e6b9` e `edc9467`).
- **FS (TASK-0008):** `rascunhos/fs/DEM-2026-001-TASK-0008-parecer-g2-v2-dotnet.md` — **rascunho sem commit**; números transcritos em `Tarefas.csv` e no `historico.md` (ORQ).
- **CR (TASK-0009):** reestimativa de 26/11 15:13 transcrita pelo ORQ em `Tarefas.csv` (sem rascunho em `rascunhos/cr/`).
- **QA (TASK-0010):** `06-qualidade/pareceres/parecer-planejamento-g2-task-0010.md` v1.1 (`1bd34a6`; merge `f5e54c2`).
- **DOC (TASK-0011):** `rascunhos/doc/MSG-RET-PO-TASK-0011-reestimativa-incremento-b.md` — rascunho sem commit; número transcrito no `historico.md` (ORQ).
- **OPS (TASK-0012):** `07-agentes/11-ops/parecer-planejamento-g2-task-0012.md` **v2.0 na main** (commit de conteúdo `d214f94`; merge `a525821`).
- **RM-0002 / CPO:** `07-agentes/07-arq/capacitacao/RM-0002-plano-capacitacao-dotnet-angular.md` (PLANO-RM-0002 v1.1; v1.0 em `97f90c4`); DEC-CPO-0001 (`1c1bdf6`); validação do PO em `07-agentes/02-po/validacao-po-plano-rm-0002.md` (`417d62f`).
- **PO:** DEC-PO-0001..0009 (`analise-po-task-0002.md` v1.5; DEC-PO-0008 `a20fe82`); PROMPT do PO; `00-memoria/protocolo-memoria.md` v1.0; `00-memoria/registro-ids.yaml`.
- **Cálculo dos totais:** `rascunhos/po/calc-totais-plano-g2-v1.2.py` (aritmética com `Decimal`; rascunho local, não versionado).

## 3. Situação das TASK (não crio TASK novas; isso é do ORQ)

| TASK | Responsável | Estado (contexto v37 / `Tarefas.csv`) | Papel neste plano |
|---|---|---|---|
| TASK-0001 | CPO | Concluída | G0 |
| TASK-0002 | PO | Concluída | Análise inicial |
| TASK-0003 | ARQ | **Concluída** (`d40518e`) | Residual da v1.1 fechado: 0,5–1 h |
| TASK-0004 | UX | Concluída | Protótipo (DEC-PO-0005) |
| TASK-0005 | QA | Concluída | Testabilidade pré-G1 |
| TASK-0006 | AS | Concluída | R1 do G3 entregue e **fechada pelo ARQ**; residual **0 h** (0,5–1 h só se o ARQ pedir ajuste) |
| TASK-0007 | ARQ | **Concluída** (G3 aprovado com ressalvas, `a271ac1`) | 3–6 h |
| TASK-0008 | FS | Aguardando dependências | Implementação API + tela; **ver dependências na seção 9** |
| TASK-0009 | CR (+ ARQ) | Aguardando dependências | G4 + 2ª aprovação do ARQ |
| TASK-0010 | QA | Aguardando dependências; **fase PT+CT liberada** pelo ORQ (DEC-PO-0009) | PT/CT; execução e PQ após o G4 |
| TASK-0011 | DOC | Em desenvolvimento: incremento A **Parcial**; B aguarda TASK-0008 | Documentação em dois incrementos |
| TASK-0012 | OPS | **Parcial**: toolchain instalada (evidência); preparação em curso | Preparação ∥ TASK-0008; G6/G7 após o G5 |

## 4. Trabalho residual (não é TASK nova)

- **TASK-0003 residual (ARQ):** **0,5–1 h**, **concluída**.
- **TASK-0006 (AS):** residual 0 h. O ARQ confirmou a R1 **sem ajustes à AS** (ET-0001 v1.4 aprovada tecnicamente para o G3). Falta só a AS atualizar o frontmatter da ET-0001 (status/aprovado_por ARQ), conforme o `historico.md`.
- **R1 em ordem:** ET-0001 v1.4 + EF-0001 L-10 + prosa do OpenAPI (`e34e6b9`).

## 5. Decisões do PO nesta demanda

- **DEC-PO-0001** — Escopo e acionamentos (duas US; UX, AS, ARQ, FS, CR, QA, DOC e OPS enxuto; sem AN, DBA, MOB, PMM).
- **DEC-PO-0002** — Público da tela = operador/equipe técnica interna (CPO, 26/11/2026 12:36).
- **DEC-PO-0003** — Prioridade Normal apesar da fórmula (pontuação 2,4 provisória).
- **DEC-PO-0004** — Pontuação recalculada **2,8**; classe **Normal** mantida.
- **DEC-PO-0005** — Protótipo/spec UX v1.0: **Aprovado com ressalvas**.
- **DEC-PO-0006** — Ajustes QA/AS: alternativa A (503 no aceite); CA-08/CA-09; textos alinhados a R3.
- **DEC-PO-0007** — Libera o incremento A da TASK-0011 (7 h) sem esperar a TASK-0008; incremento B (agora **7,5 h**, 6,5–9) após a TASK-0008, em paralelo à TASK-0010. Registrada pelo ORQ no contexto v18.
- **DEC-PO-0008** (26/11/2026 15:12, `a20fe82`) — Após a AH-0003 e o G3, **não reabrir os 15 CA**; CA-04 agnóstico; CA-07 é **risco** ligado ao spike R4. Se o spike mostrar que o encerramento gracioso é inviável, o ARQ devolve ao PO e o PO reabre o CA-07.
- **DEC-PO-0009** (26/11/2026 15:20; **ID reservado no commit desta v1.2**) — Planejamento sem reabrir CA e **sem horas extras do ARQ**: (1) **Opção A:** o **FS** escreve e mantém o código dos testes automatizados (xUnit/`WebApplicationFactory`, Vitest/jsdom) **dentro da TASK-0008** (as 40 h do FS já incluem 11 h de testes: 6 h da API + 5 h da tela); o **QA** especifica PT, CT e oráculos, **verifica** a suíte do FS (revisão de oráculo) e faz a verificação **black-box e manual** na TASK-0010. A opção B (QA escreve o código de teste) reabriria a conta das duas TASK, sem contagem dupla (sensibilidade do QA: +8–12 h, com redução na TASK-0008). (2) A fase **PT+CT** da TASK-0010 depende de **G3 + R1** (a R3 do G3 exige os casos PV antes do G4); **execução e PQ** só após o G4. Concordância técnica do ARQ: merge `edc9467`.

## 6. Ressalvas do G3 (R1..R5, `a271ac1`) — como entram no plano

| Ressalva | Conteúdo | Dono | Situação |
|---|---|---|---|
| R1 | ET-0001 v1.4 + EF-0001 L-10 + prosa do OpenAPI; condição para liberar a TASK-0008 | AS / ARQ | **Fechada** pelo ARQ (merges `9b3dc1b`, `e34e6b9`, `edc9467`) |
| R2 | Teste de contrato aplica `format: date-time`; biblioteca de schema aprovada pelo ARQ | FS (código) / QA (oráculo) | Aberta; antes dos testes de contrato (TASK-0008) |
| R3 | Itens PV do D8 do ADR-0001 v2 são testes **obrigatórios antes do G4** | FS (código) / QA (casos) / CR (verifica) | Aberta; entra na entrada do G4 |
| R4 | SDK + Angular CLI e **spike do encerramento gracioso** antes do CA-07 | OPS (ambiente) / FS (spike) | Ambiente **atendido** (dotnet 10.0.404, Angular CLI 22.3.0, Node 24.22.1; conferido pelo ORQ); **spike aberto** (linha de 3 h na TASK-0008) |
| R5 | `\z` nas regex dos testes .NET | FS / QA | Aberta |

## 7. Observações propostas para o G2 (revisão das observações (a)–(d) da v1.1)

Não são a decisão formal do gate: o PO a declara ao ORQ e o ORQ a transcreve em `aprovacoes.md`.

- **(a) [reformulada]** A condição "só após a AH-0001" **saiu**: a AH-0003 foi aprovada. A **TASK-0008 só é liberada** com (i) o plano G2 v1.2 registrado pelo ORQ, (ii) R1 fechada (já cumprida), (iii) SDK/CLI na box (já cumprido) e (iv) a premissa do núcleo da RM-0002 do FS (seção 10). A validação formal da TASK-0012 (smoke, rollback ensaiado, observação) permanece após o G5.
- **(b) [reformulada]** O G3 ocorreu. A DEC-PO-0008 não reabre CA; o **CA-07** fica condicionado ao spike R4 (reabrir só se o spike mostrar inviabilidade).
- **(c) [reformulada]** O PR da TASK-0008 e a entrada no G4 cumprem **DEC-ARQ-0007** (`verify-local` A1–A5/W1–W5, reexecutado pelo CR na box), **DEC-ARQ-0008** (analyzers, `dotnet format`, angular-eslint), as ressalvas **R3/R5** do G3, a **DEC-ARQ-0011** (L-12 só via fábrica) e a **L-CR2** (incremento A da DOC; hoje Parcial — RK-DOC-1).
- **(d) [reformulada]** A **execução** da TASK-0010 usa o p95 em Release (DEC-ARQ-0010) e SCA/SAST (DEC-ARQ-0009), já decididos. Resta calibrar com o QA a meta inicial de **80% de linhas** (Coverlet e `ng test`) no G5; não bloqueia o G2.
- **(e) [nova]** **DEC-PO-0009:** FS escreve o código de teste; PT+CT depende de G3 + R1; execução e PQ após o G4.
- **(f) [nova]** **RM-0002:** núcleo de capacitação **fora das somas**, em linha separada (seção 10); o PO avisa a CPO se o início da TASK-0008 passar de 2 dias úteis após o desbloqueio.
- **(g) [nova]** Estimativas **de todos os papéis** em horas e na stack AH-0003 (seção 10). Soma central maior que a da v1.1; o PO registra o aumento sem reabrir escopo.

## 8. Riscos relevantes

| ID | Natureza | Tratamento |
|---|---|---|
| **RK-1** Stack sem confirmação | Era 3×2 = 6 (ARQ) | **Mitigado:** AH-0003 aprovada e ADR-0001 v2.0 aceito. O `contexto.yaml` v37 ainda pode listá-lo como aberto — **ORQ atualiza** (lacuna L-12 da seção 11). |
| RK-2 Exposição pública | 1×3 = 3 | Condição no ADR-0003; reabre R3/N3. |
| RK-3 npm/Fastify | Obsoleto | A stack Node saiu com a AH-0003; substituído por NuGet Audit (DEC-ARQ-0009) e RK-FS-15. |
| **RK-CA07** Encerramento gracioso inviável no .NET | FS, spike R4 | Linha de 3 h (2–5 h) na TASK-0008. Se inviável: ARQ → PO; o PO reabre o CA-07. |
| RK-FS-15 Defaults do ASP.NET Core vazam `traceId`, `+commit`, 7 casas, cabeçalho `Server` | R3 | Obrigações D8 e testes PV (R3 do G3); `IncludeSourceRevisionInInformationalVersion=false`. |
| RK-FS-13 Curva de aprendizado | R2 | Núcleo da RM-0002 antes da TASK-0008 (premissa de 32 h); CR e 2ª aprovação do ARQ no G4. |
| RK-CR1 Evidência só do autor | CR | CR reexecuta `verify-local` na box (DEC-ARQ-0007). |
| RK-CR6 SDK ausente na box | CR | **Mitigado:** toolchain instalada e conferida pelo ORQ. |
| **RK-DOC-1** L-CR2 antes do G4 | média / alta | `modelos/parecer-cr.md` v1.1 mesclado (`a60b7b0`) e matriz 7.1 vigente (AH-0002 aprovada; merge `3755fc6`). O **incremento A segue Parcial** no `Tarefas.csv`; o fechamento depende de a DOC/ORQ registrar a evidência (L-08). |
| RK-RM Núcleo da RM-0002 atrasa a TASK | CPO/PO | Núcleo fora das somas; aviso à CPO (seção 10). |

## 9. Plano por atividade (a executar)

Critérios de **conclusão da TASK**, verificáveis e ligados aos CA/REQ vigentes. Estimativas em **horas** (todas), transcritas dos pareceres.

### TASK-0003 — Análise técnica (fechamento) · ARQ
- **Estado:** **Concluída** (ADR-0001 v2.0 aceito; `tecnologias.md` v1.1 vigente; DEC-ARQ-0007..0010; merge `d40518e`).
- **Estimativa:** **residual 0,5–1 h** (ARQ). Sem ponto único informado.

### TASK-0007 — Aprovação do contrato (G3) · ARQ
- **Estado:** **Concluída** — G3 **Aprovado com ressalvas R1..R5** (`7bc37ba`; merge `a271ac1`); OpenAPI 1.0.0 mantido; DEC-ARQ-0011; ADR-0002/0003 v1.1 aceitos.
- **Estimativa:** **3–6 h** (ARQ). Sem ponto único informado.

### TASK-0008 — Implementação API `GET /health` + tela · FS
- **Objetivo:** implementar o provedor (ASP.NET Core Minimal APIs, .NET 10) e o consumidor (Angular 22.3), com **testes automatizados escritos pelo FS** (DEC-PO-0009), conforme US/REQ/RN vigentes, contrato 1.0.0 e protótipo/spec UX.
- **Critérios de conclusão:** PR com IDs (DEM/TASK/US) e trailer de agente; nota de análise anexada; US-0001 CA-01..CA-09 atendidos na API; US-0002 CA-01..CA-06 na tela (valores brutos + UTC e Brasília no saudável; erro genérico; 503 **sem** versão/timestamp — RE-02; limpeza do DOM no carregando; timeout de 5 s sem retry; interpolação só como texto — CA-06); testes xUnit/WAF e Vitest/jsdom; ganchos de 503 e 500 **só na fábrica de teste** (DEC-ARQ-0002 L-05, DEC-ARQ-0011); `verify-local` verde (DEC-ARQ-0007..0009: lockfile, NuGet Audit, `dotnet format --verify-no-changes`, `-warnaserror`, Coverlet ≥ 80%, angular-eslint, `ng test`); **R2** (`format: date-time`), **R3** (itens PV como testes), **R5** (`\z`); spike do CA-07 (R4); versão = `<Version>` do `.csproj`; nenhum segredo. Fora: polling, Mobile, persistência.
- **Dependências:** G2 (esta v1.2 registrada pelo ORQ); G3 (OK, `a271ac1`); **R1 do G3 fechada** (ARQ; `e34e6b9`, `edc9467`); TASK-0004 (concluída); **SDK .NET 10 + Angular CLI** (instalados pelo OPS; conferidos pelo ORQ); **núcleo RM-0002 do FS** (premissa do valor de 32 h, seção 10). **A liberação da TASK-0008 depende do plano v1.2 registrado e da confirmação da R1 pelo ARQ; a R1 já foi confirmada, e resta o registro do plano v1.2 pelo ORQ.** AH-0001 deixa de ser dependência (AH-0003 aprovada).
- **Estimativa (FS):** ponto de planejamento **40 h**, faixa **32–50 h**; **32 h é o valor aplicável** se o núcleo da RM-0002 do FS (12–16 h, fora das somas) vier **antes** da TASK-0008 (preferência operacional do PO na validação da RM-0002, sujeita a o FS não ficar parado após o desbloqueio; a CPO validou o prazo com a condição de aviso, sem fixar este valor). Composição do FS: scaffold 6; endpoint 7; testes da API 6; encerramento gracioso/spike 3; tela 6; testes da tela 5; logs 1,5; `verify-local` 3; evidências/PR 2 (soma 39,5 ≈ 40; faixa 32–50 arredondada no teto).
- **Se o núcleo não vier antes:** a faixa do FS pode chegar a **50 h** (lacuna L-04).

### TASK-0009 — Code Review (G4) · CR + 2ª aprovação ARQ
- **Objetivo:** revisar o código da TASK-0008 (revisor ≠ autor) e, por ser R3, obter a **2ª aprovação explícita do ARQ**.
- **Critérios de conclusão:** parecer CR **Aprovado** ou **Aprovado com observações** + 2ª aprovação do ARQ; **Reprovado** gera novo ciclo (máx. 2). Verificação de IDs, segredos, aderência ao contrato; **DEC-ARQ-0007** (`verify-local` reexecutado pelo CR), **DEC-ARQ-0008**, **R3/R5** do G3, **DEC-ARQ-0011**; **L-CR2** (parecer em `06-qualidade/pareceres/CR-nnnn-<slug>.md`). Só então a versão segue ao QA.
- **Dependências:** TASK-0008 (PR); SDK .NET 10 + Angular CLI na box (atendido; RK-CR6); L-CR2 (incremento A da DOC).
- **Estimativa (CR):** **1º ciclo 5 h + 2º ciclo 2 h (se houver)**; prazo de 1 dia útil após entrada válida; premissa: PR de 600–1.000 linhas. **O CR conclui o núcleo da RM-0002 antes da TASK-0009: sem o +1 h.** (Se o núcleo não estiver feito: +1 h.)
- **2ª aprovação do ARQ no G4:** **1,5–3 h**, **+1 h** se houver 2º ciclo (ARQ).

### TASK-0010 — Plano de testes, testes e PQ (G5) · QA
- **Objetivo:** planejar e executar os testes na versão aprovada no G4, com rastreio dos 15 CA → CT, e emitir o PQ.
- **Critérios de conclusão:** PT/CT cobrindo **100% dos 15 CA**; contrato (200, 503, 405, 500, corpo inválido, timeout 5 s sem retry, tolerância ±5 s, `additionalProperties: false`); **HEAD**; **CORS**; **acessibilidade** no CA-02; **segurança** dirigida (casos PV, R3) + varredura SCA/SAST (DEC-ARQ-0009); **desempenho** p95 em Release (DEC-ARQ-0010; alvo indicativo ≤ 100 ms; 1ª medição = linha de base provisória); **revisão de oráculo** da suíte do FS (R2/R5, 3–5 mutações manuais); L-12 em Release + controle negativo; CA-07 em processo real **se** o spike R4 passar; PQ-nnnn na versão do G4. `404` e preflight ficam como nota de contrato.
- **Dependências:** **fase PT+CT: G3 + R1 (OK; DEC-PO-0009)**; execução e PQ: TASK-0009 (G4).
- **Estimativa (QA):** **33 h**, faixa **23,5–40 h** (piso = 1º ciclo sem retrabalho; teto = com 2º ciclo). Decomposição do QA: PT+CT 11–17; 1º ciclo 10,5–16; PQ 2–3; 2º ciclo 2,5–4 (sem 2º ciclo: 23,5–36; com: 26–40). **O núcleo da RM-0002 do QA (6–8 h) está fora da soma.**

### TASK-0011 — Documentação da versão · DOC
- **Incremento A — 7 h (DEC-PO-0007), estado Parcial** no `Tarefas.csv` e no contexto v37. Evidências no repositório: merge `b8e921b`; `modelos/parecer-cr.md` v1.1 (`a60b7b0`); protocolo v1.1 com matriz 7.1 e EL-08 vigente (`3755fc6`, AH-0002); INDEX v1.4 (`a52f96d`); UX-0001 reservado. **Não marco como Concluída**: o estado é do ORQ, e os campos de justificativa no `Tarefas.csv`/contexto ainda dizem que a matriz 7.1 aguarda a AH-0002 (desatualizado). Itens: L-CR2 1,5; CONF-0001 0,5; L-09 3,5; L-UX-01 1,5. Deve terminar **antes da entrada no G4**.
- **Incremento B — 7,5 h (6,5–9 h)**, após a TASK-0008 e em paralelo à TASK-0010: README e documentação da API e da tela (.NET 10 + Angular 22.3); release notes; nenhum segredo; publicação só após o G7. (v1.1: 5,5 h.) A DOC informa que, se o README (B1) for entregável do FS, o B cai para ≈ 6,5 h; **não adoto isso** sem decisão (lacuna L-08).
- **Total DOC: 14,5 h (13,5–16 h).**

### TASK-0012 — Execução local, smoke test e rollback · OPS
- **Fonte:** `07-agentes/11-ops/parecer-planejamento-g2-task-0012.md` **v2.0** (merge `a525821`; commit `d214f94`), reestimado para a stack AH-0003.
- **Preparação — 10 h (8–13 h):** toolchain, scripts de execução, artefato imutável, procedimento DEC-ARQ-0007, 1º bloco com o FS. **~5 h já feitas** (instalação .NET 10 + Angular CLI, evidência conferida pelo ORQ; RK-CR6 mitigado). **Saldo ≈ 5 h (4–7 h)**, após a existência do **esqueleto D6** (criado pelo FS na TASK-0008). A confirmação do FS (portas, origem CORS, comando do 1º bloco) **já foi feita** (`f1b6cda`), então essa lacuna está **fechada**; o esqueleto D6 **ainda não existe**.
- **Validação G6/G7 — 6 h ativas (5–8 h)**, após o G5, na versão aprovada no G4: smoke, rollback ensaiado (G6), pacote de pré-liberação e encerramento da observação. **Mais 24 h de calendário** de observação R3 (**não é esforço**; fora das somas).
- **Motivo do aumento** (v1.1: 8 h + 5 h): duas toolchains; `verify-local` com 10 passos (A1–A5 + W1–W5, DEC-ARQ-0007); p95 com a API em Release (DEC-ARQ-0010); versão lida do `.csproj`; instalação do SDK/CLI (feita).
- **Critérios de conclusão:** ambiente local registrado (variáveis só por **nome**, valores no `.env` fora do git); smoke da versão candidata; **rollback ensaiado no G6**; **observação de 24 h** com relatório; sem segredos; Suporte informado se houver impacto (nesta fase, provavelmente N/A).

### Atividades do AS (R1) e do PO (não são TASK novas)
- **AS — fechamento da R1:** **≈ 0,1 h** + **0,25 h** de contingência (R1 já entregue e fechada; resta atualizar o frontmatter da ET-0001).
- **G2:** decisão do PO sobre esta v1.2 (seção 12); o ORQ transcreve.
- **G6 — Pré-aceite:** 15 CA evidenciados no PQ. **G8 — Encerramento:** informar a CPO.

## 10. Estimativas e totais (horas; aritmética conferida por script)

Convenção: **ponto** = valor declarado pelo executor; **faixa** = mínimo–máximo declarado. O **ARQ declarou só faixas**; o PO **não calcula ponto** para o ARQ (nada inventado). **Cenário A:** sem 2º ciclo de revisão. **Cenário B:** com 2º ciclo (CR +2 h; ARQ +1 h; QA 26–40 com ponto 33, que já é o do cenário com 2º ciclo). Janela de **24 h** e **núcleo da RM-0002** ficam **fora**.

| Agente | Itens | Ponto | Faixa (A: sem 2º ciclo) | Faixa (B: com 2º ciclo) |
|---|---|---:|---:|---:|
| ARQ | TASK-0003 residual 0,5–1 (concluída) + TASK-0007 3–6 (concluída) + 2ª aprovação G4 1,5–3 (+1 no 2º ciclo) | — (só faixa) | 5–10 | 6–11 |
| FS | TASK-0008 | **32** aplicável (40 = ponto do FS) | 32–50 | 32–50 |
| CR | TASK-0009 (5 + 2) | 5 (A) / 7 (B) | 5–5 | 7–7 |
| QA | TASK-0010 | 33 (cenário B) | 23,5–36 | 26–40 |
| DOC | TASK-0011: A 7 + B 7,5 (6,5–9) | 14,5 | 13,5–16 | 13,5–16 |
| OPS | TASK-0012: preparação 10 (8–13) + G6/G7 6 (5–8) | 16 | 13–21 | 13–21 |
| AS | R1: 0,1 + 0,25 de contingência | 0,1 | 0,1–0,35 | 0,1–0,35 |
| **Total geral (faixa)** | | | **92,1–138,35** | **97,6–145,35** |

**Total central (soma dos pontos dos executores, cenário B, sem o ARQ):**

| Premissa do FS | Soma dos pontos (FS+CR 7+QA 33+DOC 14,5+OPS 16+AS 0,1) | + faixa do ARQ (6–11, cenário B) |
|---|---:|---:|
| FS = **32 h** (núcleo antes da TASK-0008; **valor aplicável**) | **102,6 h** | **108,6–113,6 h** |
| FS = 40 h (ponto do FS; sensibilidade) | 110,6 h | 116,6–121,6 h |

**Saldo a executar** (central, cenário B; exclui o AS entregue, 0,1 h, e a parte do OPS já feita, ~5 h; mantém o incremento A da DOC inteiro por estar Parcial; ARQ só o que resta — 2ª aprovação 2,5–4 h): FS 32 → **97,5 h** (**100,0–101,5 h** com o ARQ); FS 40 → 105,5 h (108,0–109,5 h).

**Comparação com a v1.1** (sem o ARQ; a v1.1 somava 71,5 h): FS 22 → 40 (**+18**; ou +10 com 32 h); CR 4 → 7 (+3); QA 20 → 33 (+13); DOC 12,5 → 14,5 (+2); OPS 13 → 16 (+3). Soma v1.2 = 110,5 h com FS 40 (**+39 h**) ou 102,5 h com FS 32 (**+31 h**), sem o AS. O ARQ somava 6,5 h na conversão `458acb8`, agora **superada** pelas faixas acima.

**Fora das somas (linhas separadas; RM-0002, CPO, DEC-CPO-0001):**

- **Núcleo de capacitação** (não é esforço da TASK): FS 12–16 h; CR 6–8 h; QA 6–8 h; OPS 6–8 h (**FS+CR+QA+OPS = 30–40 h**); AS 4–6 h (**não entra além da R1**). O plano da RM-0002 totaliza **46–62 h** de núcleo e **75–109 h** com o complementar (todos os papéis), **fora do prazo da DEM**. DBA e SUP: fora, com gatilho. MOB, PMM e AN: fora.
- **Janela de observação R3:** **24 h de calendário**.

**Regras da CPO para o núcleo (RM-0002):** o núcleo aparece **em linha separada, fora das somas das TASK**; a CPO aceitou o prazo **com a condição de o PO avisar se o núcleo atrasar uma TASK** (15:12; PLANO-RM-0002 v1.1). **Limiar adotado neste plano:** o PO **avisa a CPO se o início da TASK-0008 atrasar mais de 2 dias úteis** depois do desbloqueio (registro do plano; ver L-05). Não embuto o aprendizado nas horas da TASK.

## 11. Lacunas (nenhuma foi preenchida com número inventado)

| ID | Lacuna | Dono |
|---|---|---|
| L-01 | **Esqueleto D6 / monorepo** `/workspace/projetos/portal/` não existe; scripts do OPS ficam em rascunho | FS (TASK-0008) |
| L-02 | Injeção de `PORTAL_API_BASE_URL` no Angular (D7; item 3 das lacunas do ADR-0001 v2) | FS |
| L-03 | Pacote e limiar do `ng test --coverage` (80% de linhas) a calibrar no G5; respostas do ARQ ao QA no `historico.md`, sem documento versionado | FS / QA / ARQ |
| L-04 | O piso de **32 h** do FS vale só com o núcleo da RM-0002 **antes** da TASK-0008; o FS não confirmou o piso por escrito para essa condição | FS |
| L-05 | O limiar de "2 dias úteis" para avisar a CPO vem da instrução do plano; **não localizei** transcrição da CPO com esse número no repositório | ORQ / CPO |
| L-06 | **Spike do CA-07 (R4)** não executado; se inviável, o PO reabre o CA-07 | FS / ARQ |
| L-07 | CSP fora desta fase; limiar numérico de memória/CPU na observação de 24 h **não definido** | ARQ / OPS |
| L-08 | DOC B: README (B1) como entregável do FS reduziria o B para ≈ 6,5 h; **sem decisão**. DOC A consta **Parcial** (justificativa no `Tarefas.csv` desatualizada: matriz 7.1 já mesclada, `3755fc6`); item que falta para "Concluída" **não identificado** — DOC/ORQ confirmam | PO / DOC / ORQ |
| L-09 | Pareceres do **FS** e da **DOC** estão em `rascunhos/` **sem commit**; o parecer do CR só existe transcrito pelo ORQ | FS / DOC / CR |
| L-10 | Horas do ARQ **sem ponto único**: o total central não soma o ARQ; só faixa | ARQ |
| L-11 | `Tarefas.csv`: TASK-0003 e TASK-0007 ainda citam horas da era Node (`458acb8`); TASK-0008/0011/0012 e o contexto trazem estimativas antigas ou campos desatualizados | ORQ |
| L-12 | `contexto.yaml`: RK-1 pode ainda constar como aberto; ET-0001 v1.4 com frontmatter a atualizar pela AS (aprovação técnica do ARQ) | ORQ / AS |
| L-13 | A cobertura 80% e o p95 só têm linha de base após a 1ª medição (não há dado hoje) | QA / OPS |

## 12. Sequência, paralelismo e proposta para o G2

```
[concluídas] TASK-0001..0007 (G3 Aprovado com ressalvas R1..R5; R1 fechada)
[parcial]    TASK-0011 incremento A (concluir antes do G4); TASK-0012 preparação (~5 h feitas)

Plano G2 v1.2 (PO) ──registrado pelo ORQ──┐
Núcleo RM-0002 do FS (fora das somas) ────┤
                                          ▼
                                  TASK-0008 (FS; testes escritos pelo FS — DEC-PO-0009)
            ┌─────────────────────────────┼────────────────────────────────┐
            ▼                             ▼                                ▼
  TASK-0012 saldo da preparação   TASK-0010 PT+CT (G3 + R1; já liberada)   TASK-0009 (CR + ARQ, G4)
  (após esqueleto D6)                                                          │
                                                                               ▼
                                                              TASK-0010 execução e PQ (G5)  ∥  TASK-0011 incremento B
                                                                               ▼
                                              G6 (PO + OPS rollback ensaiado + DOC B pronta)
                                                                               ▼
                                   TASK-0012 G6/G7 (smoke) + 24 h de calendário → G8 (PO) e informe à CPO
```

**Proposta do PO ao ORQ para o G2:** **Aprovado com observações — mantido com ajuste** (esta v1.2 ajusta estimativas, dependências e decisões; **não reabre escopo nem CA**). A decisão só vale quando o PO a declarar ao ORQ e o ORQ registrar em `aprovacoes.md`. A promoção da v1.2 a vigente vem depois.

## 13. Matriz resumida (DoR do G2)

| TASK | Responsável | Dependências | Estimativa (h) | Critérios (resumo) | DoR |
|---|---|---|---|---|---|
| 0003 | ARQ | — | 0,5–1 (concluída) | ADR-0001 v2 aceito | Concluída |
| 0007 | ARQ | 0006; 0003 | 3–6 (concluída) | G3 com ressalvas R1..R5 | Concluída |
| 0008 | FS | G2 v1.2 registrado; G3 OK; R1 OK; SDK OK; TASK-0004; núcleo RM-0002 | 40 (32–50); 32 aplicável | PR + 15 CA + testes do FS + `verify-local` + R2/R3/R5 + spike R4 | Completa; aguarda registro da v1.2 |
| 0009 | CR (+ ARQ) | 0008 | 5 + 2 (2º ciclo); ARQ 1,5–3 (+1) | CR + 2ª aprovação; DEC-ARQ-0007/0008; R3/R5; L-CR2 | Completa |
| 0010 | QA | PT+CT: G3 + R1 (OK); execução/PQ: 0009 | 33 (23,5–40) | PT/CT dos 15 CA; segurança; p95 Release; revisão de oráculo; PQ | Completa; PT+CT liberada |
| 0011 | DOC | A: DEC-PO-0007; B: 0008 | A 7 (Parcial) + B 7,5 (6,5–9) = 14,5 (13,5–16) | L-CR2, CONF-0001, L-09, L-UX-01; docs da API/tela | Completa |
| 0012 | OPS | Prep.: esqueleto D6 (FS); G6/G7: G5 | 10 (8–13) + 6 (5–8) + 24 h calendário | Ambiente local; rollback ensaiado; observação | Parcial (toolchain feita; D6 inexistente) |

## 14. Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 12:50 (America/Sao_Paulo) | PO | Primeira versão (etapa C, pré-G2). Commit `4814277`. |
| 1.1 | 26/11/2026 13:10 (America/Sao_Paulo) | PO | Pareceres, estimativas, DEC-PO-0007, critério do CR, OpenAPI na main, observações (a)–(d). Conteúdo `053a2d4`; vigente em `f61a1f9` (G2 registrado em `2ad1838`). |
| 1.2 | 26/11/2026 15:29 (America/Sao_Paulo) | PO | **Em-revisão (proposta).** AH-0003 (.NET 10 + Angular 22.3, ADR-0001 v2.0); G3 com ressalvas R1..R5 (R1 fechada); reestimativas de FS, CR, QA, DOC B, OPS e ARQ em horas; DEC-PO-0008 e **DEC-PO-0009** (ID reservado); regras da RM-0002; totais por agente e geral; lacunas. A v1.1 (`f61a1f9`) segue vigente até o ORQ registrar a decisão. |
