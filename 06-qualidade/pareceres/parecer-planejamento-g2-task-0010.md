---
id: PARECER-G2-DEM-2026-001-TASK-0010
titulo: "Parecer de planejamento do G2 — TASK-0010 (plano de testes, execução e PQ)"
tipo: analise
versao: 1.0
status: vigente
dono: QA
autores: [QA]
aprovado_por: QA
criado_em: 2026-11-26T12:47-03:00
atualizado_em: 2026-11-26T12:47-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, TASK-0005, TASK-0009, TASK-0012, PLANO-DEM-2026-001-G2, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0005, DEC-PO-0006, DEC-ARQ-0001, DEC-ARQ-0002, DEC-AS-0001, DEC-AS-0002, EF-0001, ET-0001, AH-0001]
substitui: null
substituido_por: null
---

# Parecer de planejamento G2 — TASK-0010 (QA)

> [TESTE] DEM-2026-001 · parecer de **planejamento** para o G2 (etapa C). **Não** é PT, CT nem PQ: esses artefatos serão criados na execução da TASK-0010, após o G3 (oráculos de contrato) e o G4 (versão a testar). Este documento **não** altera estado, etapa, gates, `contexto.yaml`, `historico.md` nem `Tarefas.csv` (só o ORQ).

## 1. Resultado

A QA **confirma o recorte** do PLANO-DEM-2026-001-G2 para a TASK-0010, com **ajustes de complemento** (não de exclusão) descritos na seção 3. Estimativa QA, em **horas** (mesma unidade já gravada pelo ORQ na TASK-0009 a partir do parecer do CR): **20 h** como ponto para a planilha, faixa **16–23 h**, premissas na seção 2.

A TASK-0010 como um todo permanece aguardando o G4 para execução; este parecer encerra apenas o insumo de planejamento pedido no G2.

## 2. Estimativa (TASK-0010)

**Unidade:** horas. A coluna `Estimativa` de `Tarefas.csv` não declara unidade em `Listas.csv`, mas o CR já usou horas na TASK-0009 e o ORQ gravou nesse formato; a QA adota a mesma escala. A escala 1–5 de “Esforço estimado” de `criterios-classificacao.md` (1 = horas · 5 = semanas) é fator da pontuação da **demanda**, não unidade da TASK — não é usada aqui.

**Ponto sugerido para Tarefas.csv:** 20 h (estimativa QA).  
**Faixa:** 16–23 h, assim decomposta:

| Lote | Quando | Faixa | Conteúdo |
|---|---|---|---|
| PT + CT (planejamento detalhado) | Após o G3 (contrato aprovado); pode antecipar rascunho após o residual do OpenAPI | 8–11 h | Estratégia R3, rastreio dos **15** CA vigentes, casos de contrato/segurança/desempenho |
| Execução — 1º ciclo | Após o G4, na versão aprovada, no ambiente local do OPS | 6–8 h | API, tela, contrato, testes dirigidos de segurança, desempenho indicativo, evidências |
| Retrabalho — 2º ciclo (se houver) | Defeitos P2/P3 corrigidos e re-revisados | 2–3 h | Reexecução dos CT afetados e da regressão aplicável |
| PQ | Ao encerrar a execução | 1,5–2 h | PQ-nnnn, rastreio CA→CT, evidências, versão testada = G4 |

**Premissas da estimativa:**
- Ambiente local documentado pelo OPS (TASK-0012, preparação) antes da execução; API e Portal em processos separados.
- Contrato aprovado no G3 alinhado aos CA v1.2, sem reabertura ampla (condição 1 do G1).
- Stack confirmada (AH-0001) e versão candidata estável após G4 (CR + 2ª aprovação do ARQ).
- No máximo **um** ciclo de retrabalho de P2/P3; P0/P1 ou mudança de contrato no G3 reabre a faixa.
- Ganchos de teste do 503 (e equivalente para o 500) disponíveis só na fábrica de teste, conforme ET-0001 §7.2 (PS-05/PS-07). Sem isso, CA-07 (e possivelmente CA-09) não se executam no prazo.
- Ferramenta de p95 e forma da varredura de segurança definidas com OPS/ARQ antes da execução (senão esses lotes escorregam ou o PQ fica condicionado).
- Sem persistência, sem autenticação, dois componentes; suíte de regressão inicial = esta entrega.
- Esta estimativa **não** inclui a observação de 24 h nem o smoke/rollback (TASK-0012 / G6–G7).

## 3. Recorte: confirmação e ajustes

**Contagem vigente:** **15 CA** — US-0001 CA-01..CA-09 (9) e US-0002 CA-01..CA-06 (6), todos v1.2 vigentes (`babb9fe`). Não são mais 12.

### Confirmado (como no plano)

- Rastreio de **100% dos CA vigentes** (15) com CT e evidência no PQ.
- Testes de **contrato**: HTTP 200, 503, 405, 500, corpo inválido e timeout (5 s, sem retry — DEC-AS-0001); tolerância do timestamp ±5 s (DEC-AS-0002); `additionalProperties: false`.
- **Segurança dirigida:** RN-0001, REQ-0004, US-0001 CA-05, US-0002 CA-06, denylist (incluindo 405/503/500 e a tela nos três estados; no 503 a tela não exibe versão/timestamp — RE-02 / DEC-PO-0005).
- **Desempenho:** medição do alvo **indicativo** p95 ≤ 100 ms em execução local (não é SLO nem CA — ET-0001 RT-14); obrigatório nesta demanda por R3 / DEC-ARQ-0001, a calibrar com OPS.
- **Regressão** aplicável: suíte inicial = esta entrega (primeiro serviço).
- **Aceitação:** os 15 CA no PQ; versão testada = versão aprovada no G4.
- Tempo limite do cliente e oráculos de US-0002 (valores brutos da mesma consulta; carregando remove valores do DOM; recuperação pelo botão).

### Ajustes de complemento (não retiram nada do recorte)

| Item | vs. recorte do plano / matriz R3 | Posição da QA |
|---|---|---|
| `HEAD /health` | CA-08 / ET-0001 CE-10 (HEAD tolerado, mesmos código/cabeçalhos do GET, sem corpo) | Incluir no contrato, ligado ao CA-08. |
| CORS | ET-0001 CE-08 / DEC-ARQ-0002 L-06 | Incluir como integração Portal↔API (origem permitida e origem negada ⇒ erro caso (a) no navegador). Não é CA novo. |
| Acessibilidade da tela | Não estava explícita no recorte; CA-02 e a spec UX v1.0 (D-UX-04; validada com ressalvas) exigem informação **não só por cor** | Incluir como verificação do CA-02 (e checagens de apoio já rastreadas na spec: selo textual, `aria-live`/alerta). Sem CA novo de a11y. |
| Varredura de segurança | Matriz R3: **varredura + testes dirigidos**. O plano citou só os dirigidos. Não há pipeline/CI nem ferramenta nomeada (L7; parecer do CR já apontou substituto local de CI). | Os testes dirigidos **não substituem** a varredura. OPS/ARQ devem indicar ferramenta e método locais **antes da execução**. Sem varredura, o PQ não pode ser favorável pleno pelos critérios do G5 (exceção só com AH de segurança). |
| Linha de base de desempenho +10% | Critério do PQ: p95 e taxa de erro dentro da linha de base +10%. **Não existe linha de base** (projeto do zero). | Não aplicar o +10% literalmente na primeira entrega. A primeira medição local, com método documentado, vira **linha de base provisória**; o oráculo desta demanda é o alvo indicativo p95 ≤ 100 ms (e taxa de erro da amostra). Calibração com OPS (PS-08). |
| Unitários e integração | R3: ambos obrigatórios | QA **verifica** a suíte unitária do FS e executa integração Portal↔API / contrato; não substitui os unitários do desenvolvedor. |
| `404` de rota inexistente e `OPTIONS` de preflight | ET-0001 CE-09/CE-11; **não** são CA de `/health` | Fora do aceite da demanda. Podem aparecer como nota de contrato/serviço, sem bloquear o rastreio dos 15 CA. |
| Dados de teste | Não há persistência (L9) | Mocks e fábrica de teste (relógio e estado de saúde injetáveis); manifesto/tag para o CA-04; sem massa de banco. |
| Ambiente | Premissa: `/workspace/projetos/`, a confirmar pelo OPS | Execução do G5 só no ambiente registrado pelo OPS; valores de origem/porta por **nome** de variável (DEC-ARQ-0002 L-06). |

## 4. Riscos e pendências (com dono)

| ID | Tipo | Item | Dono | Efeito |
|---|---|---|---|---|
| P-QA-01 | Pendência | Ambiente local (L7) e valores de `PORTAL_WEB_PORT` / `PORTAL_API_ALLOWED_ORIGIN` | OPS (TASK-0012, preparação) | Bloqueia a **execução** da TASK-0010, não a decisão do G2. |
| P-QA-02 | Pendência | Ferramenta de medição do p95 (ET-0001 PS-08) | OPS / QA, premissa AH-0001 | Sem método, o teste de desempenho R3 não fecha. |
| P-QA-03 | Pendência | Ferramenta e método de **varredura** local (não há pipeline) | OPS / ARQ | Sem isso, o PQ fica condicionado ou desfavorável no critério de varredura. |
| P-QA-04 | Pendência | Gancho de 503 só na fábrica de teste (ET-0001 §7.2, PS-05/PS-07) e equivalente para injetar o 500 (CA-09) — este último ainda não está tão explícito quanto o do 503 | FS / AS (desenho); ARQ (AH-0001 / stack) | Sem gancho de teste, CA-07 e CA-09 não são executáveis de forma repetível (é proibido force remoto em não-teste). |
| P-QA-05 | Pendência | OpenAPI 1.0.0 ainda no ramo, ajustes do DEC-ARQ-0002 pendentes; G3 só após AH-0001 | AS (residual) / ARQ (G3) | PT/CT definitivos após o contrato aprovado; rascunho pode começar com ET-0001 v1.2. |
| P-QA-06 | Risco | ADR-0001/0002/0003 ainda **propostos**; condição 1 do G1: se o G3 mudar formatos, o PO reabre CA | ARQ / PO | Reabre PT/CT e a faixa de estimativa. |
| P-QA-07 | Risco | AH-0001 pendente (stack, origem da versão, ganchos, ferramenta de p95) | ORQ / Thiago | Não impede o G2; impede implementação, G4 e portanto a execução da TASK-0010. |
| P-QA-08 | Risco | Critério do PQ “linha de base +10%” inaplicável na primeira entrega | QA (trata no PT/PQ) + aceite do ARQ/PO se necessário | Mitigação: oráculo indicativo de 100 ms + linha de base provisória documentada. |
| P-QA-09 | Lacuna de ponteiro | `contexto.yaml` v12 ainda cita EF/ET v1.1; na main estão **EF-0001 e ET-0001 v1.2** em-revisao (commit `3a41a2c`) | ORQ | Não crítica; este parecer usa v1.2 commitada. |

Nenhum desses itens impede emitir este parecer nem, por si, a decisão do G2. Impedem ou condicionam a **entrada em execução** da TASK-0010.

## 5. Colaborações necessárias

- OPS: ambiente, variáveis (só nomes), método de p95, apoio à varredura local.
- ARQ: confirmação da varredura e da abordagem da linha de base provisória; G3; ciência de que o PQ R3 depende disso.
- FS: ganchos de teste (503 e 500) só na fábrica; suíte unitária verificável; IDs no PR.
- AS: residual do OpenAPI e alinhamento já iniciado na ET-0001 v1.2.
- PO: ciência dos complementos de recorte; validação futura do PQ (G6).

## 6. Fontes consultadas

- PLANO-DEM-2026-001-G2 v1.0 em-revisao (commit `4814277`); contexto.yaml **v12** (2026-11-26T12:55-03:00); historico.md até 26/11/2026 12:55; aprovacoes.md (G1 aprovado com observações).
- US-0001 e US-0002, REQ-0001..0004, RN-0001 e RN-0002 **v1.2 vigentes** (`babb9fe`); DEC-PO-0005 e DEC-PO-0006 (`af208f2`).
- EF-0001 e ET-0001 **v1.2 em-revisao** (`3a41a2c`); DEC-ARQ-0001 (R3); DEC-ARQ-0002 v1.0 vigente; DEC-AS-0001/0002/0003; ADR-0001/0002/0003 v1.0 propostos.
- Tarefas.csv (estimativa da TASK-0009 em horas); criterios-classificacao.md (escala 1–5 da demanda, não usada como unidade desta TASK); PROMPT do QA seção 6 (matriz R3 e critérios do PQ); estado-operacional.md (Normal).
- ANALISE-TESTABILIDADE-DEM-2026-001-TASK-0005 v1.0 (`80e9184`) — antecedente; os ajustes já foram incorporados na v1.2.
- Pacote de contexto TASK-0010: não encontrado em `pacotes-contexto/` (lacuna não crítica).
