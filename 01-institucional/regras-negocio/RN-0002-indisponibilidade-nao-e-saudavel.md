---
id: RN-0002
titulo: "Indisponibilidade nunca é apresentada como saudável"
tipo: rn
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:15-03:00
atualizado_em: 2026-11-26T12:15-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, REQ-0003, US-0002]
substitui: null
substituido_por: null
---

# RN-0002 — Indisponibilidade nunca é apresentada como saudável

> [TESTE] Origem: DEM-2026-001 · TASK-0002 · Regra proposta pelo PO; status em-revisao até o G1.

**Regra:** a ausência de uma resposta válida do health-check (sem resposta, tempo esgotado, resposta de erro ou conteúdo inválido) deve ser tratada pelo Portal como **estado de erro/indisponível**. O Portal nunca apresenta um status anterior (último valor conhecido) como se fosse o status atual, e nunca assume "saudável" por padrão.

**Justificativa:** o valor do health-check é a confiança no sinal; um falso "saudável" é pior que a ausência de informação.

**Aplicação:** REQ-0003; CA-03 e CA-05 da US-0002. A forma visual do estado de erro é decisão do UX/UI.
