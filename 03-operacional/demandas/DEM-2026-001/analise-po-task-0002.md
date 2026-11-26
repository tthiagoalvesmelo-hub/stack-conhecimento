---
id: ANALISE-DEM-2026-001-TASK-0002
titulo: "Análise inicial do PO — escopo, atividades propostas e pontuação (DEM-2026-001 [TESTE])"
tipo: analise
versao: 1.1
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:22-03:00
atualizado_em: 2026-11-26T12:32-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, TASK-0004, TASK-0005, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0001, DEC-PO-0002, DEC-PO-0003, DEC-PO-0004, DEC-PO-0005, DEC-PO-0006, DEC-ARQ-0001, ADR-0001, ADR-0002, ADR-0003]
substitui: null
substituido_por: null
---

# Análise inicial do PO — DEM-2026-001 [TESTE] · TASK-0002

> Fase de testes internos; nada vai à produção. Este documento **não** altera estado, etapa, gates nem tarefas (só o ORQ). **v1.1** (26/11/2026 12:32, America/Sao_Paulo): incorpora TASK-0003 (ADR propostos, R3, fatores técnicos), validação do protótipo (DEC-PO-0005), ajustes de testabilidade (DEC-PO-0006) e pontuação recalculada 2,8 (DEC-PO-0004). Os códigos A1…A9 foram mapeados pelo ORQ às TASK-0004…0012.

## 1. Entendimento
- **O que foi pedido, por quem, para quê:** Thiago Melo (via Jarvis, ORQ) pediu, como teste ponta a ponta da esteira, um endpoint `GET /health` na API base do Portal Web (status, versão, timestamp) e uma tela simples no Portal que mostre esse status; projeto do zero. G0 aceito pela CPO (26/11/2026): Funcionalidade nova, Fluxo 01, responsável PO, prioridade Normal, não dividir a demanda, ARQ colaborador obrigatório.
- **Objetivo funcional:** dar um sinal verificável de disponibilidade e versão da API e torná-lo visível no Portal.
- **Separação requisito × decisão técnica:** o PO define comportamento e critérios (US/CA/REQ/RN). Stack, estrutura, formato da versão e do timestamp, nomes de campos, exposição/autenticação do endpoint e classe de risco são do ARQ (TASK-0003, ADR propostos); contrato/EF/ET é do AS; interface é do UX/UI.

## 2. Premissas e lacunas
| # | Item | Tratamento (v1.1) | Dono |
|---|---|---|---|
| L1 | Visão e objetivos de produto ausentes em 01-institucional/produto | **Aberta.** Premissa de teste: demanda de validação da esteira; sem compromisso de negócio | CPO |
| L2 | Público da tela de status | **Aberta.** Premissa de teste (DEC-PO-0002): operador/equipe técnica interna | CPO |
| L3 | Stack, estrutura, formato de versão e timestamp, nomes de campos e valores de status | **Respondida como premissa** (ADR-0001/0002/0003 v1.0 **propostos**, commit 362ea35). Formatos incorporados nas US/REQ v1.1 sem o PO decidir arquitetura. Stack = N3, aguarda **AH-0001** | ARQ / Thiago (via ORQ) |
| L4 | Exposição do endpoint e autenticação | **Respondida como premissa** (ADR-0003): contrato interno, `/health` sem autenticação, só rede local/interna. Exposição pública reabre R3/N3 + AH | ARQ |
| L5 | Regra de acesso à tela | **Respondida como premissa** (ADR-0003): tela sem login nesta demanda; autenticação do Portal é demanda própria | ARQ / CPO (público) |
| L6 | Desempenho e tempo limite da tela | **Respondida em parte:** alvo indicativo p95 ≤ 100 ms local (não é SLO). Tempo limite do cliente: orientação do ARQ de 5 s, **fechada pela AS em 5 s** (DEC-AS-0001, ET-0001 v1.1), premissa até o ADR/contrato ser aceito | AS (fechou) / ARQ |
| L7 | Ambientes dev/hml inexistentes | **Aberta.** Premissa de teste: execução local, código em /workspace/projetos/ | OPS |
| L8 | Classe de risco | **Fechada.** R3 confirmada (DEC-ARQ-0001): primeiro serviço + stack base. Não é por contrato público | ARQ |
| L9 | Persistência | **Fechada.** Confirmado pelo ARQ: nenhuma. DBA não acionado | ARQ (confirmou) |

## 3. Solução funcional consolidada
Duas histórias na **mesma demanda** (DEC-PO-0001):
1. **US-0001 v1.1** — endpoint `GET /health`: CA-01 a CA-09 (inclui 503, alternativa A; 405; e 500 padronizado sem detalhe interno).
2. **US-0002 v1.1** — tela de status: CA-01 a CA-06, com RE-02 escrito no CA-03 (503 oculta versão/timestamp) e CA-04 promovendo a remoção dos valores anteriores do DOM.

Protótipo/spec UX v1.0: **Aprovado com ressalvas** (DEC-PO-0005). D-UX-05/D-UX-08 aceitos (oráculo do CA-01).

## 4. Quem aciona o quê (DEC-PO-0001) — sem mudança de elenco
UX/UI, AS, ARQ, Full Stack, CR, QA, DOC e OPS (enxuto): **sim**. AN, DBA (L9 confirmada), Mobile e PMM: **não**. Suporte: informado no G7.

## 5. Atividades e TASK (criadas pelo ORQ)
| Rótulo | TASK | Responsável | Estado conhecido (contexto v6, só leitura) | Gate |
|---|---|---|---|---|
| A0 | TASK-0003 | ARQ | Parcial (ADR propostos; AH-0001) | — |
| A1 | TASK-0004 | UX/UI | Concluída; validação do PO = DEC-PO-0005 | G1/G2 |
| A2 | TASK-0006 | AS | Em andamento (EF/ET sob premissa) | G1/G2, G3 |
| A3 | TASK-0007 | ARQ | Aguardando dependências | G3 |
| A4a | TASK-0005 | QA | Concluída (favorável com ressalvas; ajustes incorporados na v1.1) | pré-G1 |
| A4b/A7 | TASK-0010 | QA | Aguardando dependências | G5 |
| A5 | TASK-0008 | Full Stack | Aguardando G2, G3, protótipo validado e AH-0001 | — |
| A6 | TASK-0009 | CR | Aguardando dependências | G4 (+ 2ª aprovação ARQ, R3) |
| A8 | TASK-0011 | DOC | Aguardando dependências | G6, G8 |
| A9 | TASK-0012 | OPS | Aguardando dependências | G6, G7 (rollback **ensaiado**, R3) |

## 6. Pontuação de prioridade (recalculada — DEC-PO-0004)
Fatores confirmados pelo ARQ (TASK-0003): severidade técnica **1**, risco operacional **2**, complexidade **3**. Demais fatores do PO inalterados.

| Fator | Valor | Quem pontua | Justificativa |
|---|---|---|---|
| Impacto no negócio | 2 | PO | Validação da esteira, sem compromisso de receita (L1) |
| Impacto nos usuários | 1 | PO | Poucos usuários internos, sem bloqueio |
| Severidade técnica | 1 | ARQ | Confirmada |
| Risco operacional | 2 | ARQ | Confirmada (era 1 provisório) |
| Urgência | 1 | PO | Sem prazo |
| Bônus de dependências | 0 | ORQ levanta | Nenhuma demanda dependente |
| Complexidade | 3 | ARQ | Confirmada |
| Esforço estimado | 2 | executores/PO | De algumas horas a poucos dias |

- Custo do atraso = 2+1+1+2+1+0 = **7**
- Tamanho = (3+2)/2 = **2,5**
- **Pontuação = 7 / 2,5 = 2,8**
- **Classe pela fórmula:** Baixa (< 3). **Classe adotada: Normal**, confirmada pela CPO no G0. Ajuste manual mantido (DEC-PO-0003 e DEC-PO-0004): a prioridade estratégica é da CPO e o propósito é o teste ponta a ponta aprovado por Thiago.

## 7. Observação: impactos do R3 no plano (não grava estado nem gates)
DEC-ARQ-0001 (R3) implica, quando aplicável: 2ª aprovação do ARQ no G4; testes de segurança e desempenho além dos demais tipos; janela de observação de 24 h; plano de rollback **ensaiado** no G6; AH (AH-0001 já solicitada para a stack base, N3). O PO registra aqui apenas como observação de planejamento. Quem grava gates é o ORQ.

## 8. Impactos e riscos
| Componente | Impacto |
|---|---|
| Portal Web | Nova tela de status (protótipo v1.0 aprovado com ressalvas) |
| Backend/APIs | `GET /health` (200, 503 e 405) na API base a criar; contrato interno |
| Microsserviços | Nasce `portal-api` se o ADR-0001 for aceito (AH-0001) |
| Mobile | Nenhum |
| Integrações | Portal → API; nenhuma externa |
| Dados | Nenhum (L9 confirmada) |
| Infraestrutura | Execução local no teste; ambientes a definir (L7) |

Riscos anteriores permanecem. Acrescenta-se: ADRs ainda propostos — se formatos mudarem após a AH, US/spec/ET devem ser revisados (prob. média, impacto baixo).

## 9. Decisões (alçada do PO)
- **DEC-PO-0001** — Escopo e acionamentos (inalterada).
- **DEC-PO-0002** — Público da tela = operador/equipe técnica interna (premissa; CPO confirma).
- **DEC-PO-0003** — Prioridade Normal apesar da fórmula (v1.0, pontuação 2,4 provisória).
- **DEC-PO-0004** — Pontuação recalculada **2,8** com os fatores do ARQ; classe **Normal** mantida.
- **DEC-PO-0005** — Protótipo/spec UX v1.0: **Aprovado com ressalvas**; RE-01..RE-05 e D-UX-05/08 decididos.
- **DEC-PO-0006** — Ajustes de testabilidade da TASK-0005 e respostas à AS (TASK-0006, L-11): REQ-0001 alternativa **A** (503 no aceite, premissa até o ADR-0003 ser aceito); 405 e 500 também entram no aceite (CA-08 e CA-09). Conteúdo de US/REQ atualizado para R3 (CONF-0001, lado PO).

## 10. Próximos passos
1. ORQ atualiza contexto.yaml (ponteiros v1.1, pontuação 2,8, validação do protótipo, DEC-PO-0004..0006, pendências L1/L2/L6/L7/AH-0001) e avalia o G1 (TASK-0003 Parcial + TASK-0005 Concluída + validação do PO + ajustes respondidos). A stack continua bloqueada pela AH-0001.
2. UX aplica, se quiser, as recomendações aceitas como opcionais (RE-01, RE-05); não é obrigatório para o aceite.
3. AS alinha a ET/OpenAPI à alternativa A, ao CA-07/CA-08 e à decisão RE-02 (contrato 503 tem os campos; a tela não os exibe).
4. QA usa os CA v1.1 como oráculo na TASK-0010.
