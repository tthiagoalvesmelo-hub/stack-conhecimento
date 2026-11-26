---
id: RN-0002
titulo: "Indisponibilidade nunca é apresentada como saudável"
tipo: rn
versao: 1.2
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:15-03:00
atualizado_em: 2026-11-26T12:41-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0004, TASK-0005, REQ-0003, US-0002, ADR-0003, DEC-PO-0005]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (condição 1 do G1):** formatos, 503/405/500, tempo limite de 5 s e “sem login” dependem dos ADR-0002/0003 ainda propostos; se mudarem no G3, o PO reabre os CA afetados. Implementação depende da AH-0001.

# RN-0002 — Indisponibilidade nunca é apresentada como saudável

> [TESTE] Origem: DEM-2026-001 · TASK-0002 · **v1.1:** o HTTP 503 de contrato também nunca é apresentado como saudável.

**Regra:** a ausência de uma resposta **saudável e válida** do health-check (sem resposta, tempo esgotado, resposta de erro, conteúdo inválido, ou HTTP 503 com status de indisponibilidade previsto no contrato) deve ser tratada pelo Portal como **estado de erro/indisponível**. O Portal nunca apresenta um status anterior (último valor conhecido) como se fosse o status atual, nunca assume "saudável" por padrão e nunca trata o 503 como estado operacional.

**Justificativa:** o valor do health-check é a confiança no sinal; um falso "saudável" é pior que a ausência de informação.

**Aplicação:** REQ-0003; CA-03, CA-04 e CA-05 da US-0002. A forma visual do estado de erro é decisão do UX/UI (spec v1.0 aprovada com ressalvas; no 503, versão e timestamp não são exibidos — RE-02).
