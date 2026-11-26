---
id: PARECER-ARQ-DEM-2026-001-G2
titulo: "Parecer técnico consolidado do ARQ para o G2 — DEM-2026-001 [TESTE]"
tipo: parecer
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T12:50-03:00
atualizado_em: 2026-11-26T12:50-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, TASK-0007, TASK-0008, TASK-0009, PLANO-DEM-2026-001-G2, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0003, DEC-ARQ-0004, AH-0001]
substitui: null
substituido_por: null
---

# Parecer técnico consolidado — G2 · DEM-2026-001 [TESTE] · TASK-0003

> America/Sao_Paulo. **Isto não é o G3** (TASK-0007). Estado operacional: Normal. Fluxo 01, etapa C. Este parecer cumpre os critérios de fechamento da TASK-0003 definidos no PLANO-DEM-2026-001-G2 v1.0; os critérios originais da TASK-0003 (stack/estrutura *decididas*) permanecem **Parciais** até a AH-0001. Recomendo manter a TASK-0003 como **Parcial**.

## 1. Decisões arquiteturais (status)

| Artefato | Status | Comentário |
|---|---|---|
| ADR-0001 (stack, estrutura) | Proposto | Node 24 + Fastify 5 + Portal estático; N3 (AH-0001). Sem código nem esqueleto até a aceitação. |
| ADR-0002 (SemVer, origem da versão) | Proposto | Aceito por mim após o ADR-0001 (origem = `package.json`). |
| ADR-0003 (padrão GET /health) | Proposto | Diretrizes; complemento DEC-ARQ-0002. |
| DEC-ARQ-0001 | Vigente | Classe **R3** (novo serviço + stack base). Consequências: testes aplicáveis + segurança e desempenho; 2ª aprovação do ARQ no G4; AH; observação 24 h; rollback ensaiado no G6. |
| DEC-ARQ-0002 | Vigente | L-01..L-07 do contrato (parecer prévio; não foi G3). |
| DEC-ARQ-0003 | Vigente | L-CR1: substituto local do “CI verde”. |
| DEC-ARQ-0004 | Vigente, condicionada ao ADR-0001 | L-CR3: ESLint 10 + `@eslint/js` + `globals` (MIT, npm 26/11, nada instalado). |

Contrato OpenAPI 3.1 `portal-api` 1.0.0 está na **main**, status **proposto**, merge `--no-ff` `cf660fb` (ramo `doc/ET-0001-contrato-portal-api-health`, autor AS, revisor ARQ). EF/ET-0001 v1.2 na main (`3a41a2c`). **Isso não é o G3.**

## 2. Sequência e bloqueios

**Confirmo** a sequência do plano, com estes ajustes/precisões (não alterei Tarefas.csv):

1. Residual da AS no OpenAPI: **concluído** (b3f13d6 + merge `cf660fb`). A TASK-0007 não espera mais esse residual.
2. TASK-0007 (G3) permanece **após a AH-0001**. Pedido ao ORQ: gravar a dependência AH-0001 na TASK-0007 (hoje o Tarefas.csv lista só TASK-0006).
3. TASK-0008 só após G2 + G3 + AH-0001 + TASK-0004; mocks do consumidor só após o G3 (PR-04). O PR deve cumprir DEC-ARQ-0003 e 0004.
4. Preparação do OPS após a AH-0001, em paralelo à TASK-0008; validação formal (smoke, rollback ensaiado, observação 24 h) após o G5, no G6/G7 — confirmo a proposta do plano.
5. TASK-0009 (G4): CR + **2ª aprovação do ARQ** (R3). Entrada no G4: DEC-ARQ-0003, DEC-ARQ-0004 e L-CR2 (não é minha alçada).
6. TASK-0010 ∥ TASK-0011 (PR-06); G6 → G7 local → G8.

Nenhuma atividade com dependência não resolvida entra em execução (0008/0012/0007 formal).

## 3. Riscos (P×I, 1–3; ≥ 6 exige mitigação antes do G2)

| ID | P×I | Tratamento antes do G2 |
|---|---|---|
| RK-1 Stack sem confirmação | 3×2=**6 (alto)** | **Mitigar** (não aceitar): 0008 e 0012 não executam sem AH-0001 válida; se a AH recusar ou mudar a stack, ADRs e o plano são reavaliados antes da execução. Mitigação já no plano — suficiente para o G2 condicional. |
| RK-2 Exposição pública | 1×3=3 | Condição no ADR-0003; reabre R3/N3. |
| RK-3 npm/Fastify | 1×2=2 | Lockfile, `npm ci`, `npm audit` (DEC-ARQ-0003). |
| RK-CR1 evidência só do autor | (apontado pelo CR) | Mitigado: CR reexecuta o script na box (DEC-ARQ-0003). |

## 4. Estimativas (escala do PROMPT: 1 = horas · 5 = semanas)

Não invento duração exata; a escala e a ordem de grandeza têm base na natureza da tarefa (revisão documental / parecer), no tamanho esperado do PR (CR: 300–600 linhas) e no fato de o residual da AS no OpenAPI já ter sido entregue.

| Trabalho | Escala | Ordem de grandeza e premissas |
|---|---|---|
| TASK-0003 residual (após este parecer) | **1** | Horas. Após a AH-0001, se a alternativa A for aceita: aceitar/rejeitar ADR-0001..0003 e preencher `tecnologias.md`. Se B ou Node 26: ainda escala 1, com revisão dos ADR (horas, no máximo um dia). |
| TASK-0007 (G3) | **1** | Horas. Premissas: OpenAPI já na main (proposto, `cf660fb`); AH-0001 aprovada sem mudar as diretrizes do contrato; ET v1.2 alinhada. É revisão de um contrato de um recurso + parecer de G3, não implementação. |
| 2ª aprovação do ARQ no G4 (R3), na TASK-0009 | **1** | Horas; menor que o 1º ciclo do CR (3 h). Premissas: PR 300–600 linhas (CR); 1º ciclo após CR favorável ou com observações não bloqueantes; se o CR reprovar, a 2ª aprovação só no ciclo seguinte. Estou disponível no mesmo dia útil do parecer do CR (prioridade Normal). |

O ORQ grava as estimativas no Tarefas.csv. Eu não gravei.

## 5. O que a AH-0001 ainda trava

Trava: aceitação dos ADR-0001 (e, em cadeia, 0002/0003); `tecnologias.md`; esqueleto em `/workspace/projetos/`; TASK-0008; preparação da TASK-0012; G3 formal (TASK-0007); aplicação concreta da DEC-ARQ-0004 (condicionada à stack).

Não trava: este parecer; a decisão de um **G2 com observações**; o contrato proposto já na main; documentação residual (CONF-0001 formal, L-09, L-CR2); redação de PT/CT pelo QA (a execução do G5 espera o G4).

## 6. G2 com condição / observações

O PROMPT admite o resultado **“Aprovado com observações”** (já usado no G1). Quem **decide** o G2 no Fluxo 01 é o **PO**; o ORQ **grava** o gate. O ARQ não grava G2.

As decisões já registradas **bastam para um G2 com observações**, não para um G2 incondicional: “decisões arquiteturais consolidadas” ainda estão *propostas* (N3 pendente).

Observações que recomendo (o PO decide):

1. TASK-0008 e TASK-0012 não entram em execução sem AH-0001 válida (já é a condição 2 do G1). O G2 não substitui a AH.
2. TASK-0007 (G3) só após a AH-0001. Se a AH ou o G3 alterar ADR/contrato, o PO reabre os CA afetados (condição 1 do G1) e o plano é reavaliado antes da execução.
3. L-CR1 e L-CR3 **não bloqueiam a decisão do G2**. Já estão decididas (DEC-ARQ-0003 e 0004). Devem constar como observação: o PR da TASK-0008 e a entrada no G4 exigem o cumprimento dessas DEC (e da L-CR2, dono DOC/ORQ). A DEC-ARQ-0004 é revista se a stack mudar.
4. RK-1 permanece mitigado pela observação (1).

## 7. Pedido ao OPS (confirmação, não bloqueia o G2)

Confirmar o procedimento operacional da DEC-ARQ-0003: localização do script, retenção da evidência sem segredos e modo de reexecução pelo CR na box.
