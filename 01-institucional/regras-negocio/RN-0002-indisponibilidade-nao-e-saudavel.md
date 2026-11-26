---
id: RN-0002
titulo: "Indisponibilidade nunca é apresentada como saudável"
tipo: rn
versao: 1.1
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:15-03:00
atualizado_em: 2026-11-26T12:32-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0004, TASK-0005, REQ-0003, US-0002, ADR-0003, DEC-PO-0005]
substitui: null
substituido_por: null
---

# RN-0002 — Indisponibilidade nunca é apresentada como saudável

> [TESTE] Origem: DEM-2026-001 · TASK-0002 · **v1.1:** o HTTP 503 de contrato também nunca é apresentado como saudável.

**Regra:** a ausência de uma resposta **saudável e válida** do health-check (sem resposta, tempo esgotado, resposta de erro, conteúdo inválido, ou HTTP 503 com status de indisponibilidade previsto no contrato) deve ser tratada pelo Portal como **estado de erro/indisponível**. O Portal nunca apresenta um status anterior (último valor conhecido) como se fosse o status atual, nunca assume "saudável" por padrão e nunca trata o 503 como estado operacional.

**Justificativa:** o valor do health-check é a confiança no sinal; um falso "saudável" é pior que a ausência de informação.

**Aplicação:** REQ-0003; CA-03, CA-04 e CA-05 da US-0002. A forma visual do estado de erro é decisão do UX/UI (spec v1.0 aprovada com ressalvas; no 503, versão e timestamp não são exibidos — RE-02).
