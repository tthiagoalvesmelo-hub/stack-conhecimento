---
id: REQ-0002
titulo: "Tela de status no Portal exibe status, versão e timestamp"
tipo: req
subtipo: funcional
versao: 1.2
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:16-03:00
atualizado_em: 2026-11-26T12:41-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0004, US-0002, REQ-0001, DEC-PO-0002, DEC-PO-0005]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (condição 1 do G1):** formatos, 503/405/500, tempo limite de 5 s e “sem login” dependem dos ADR-0002/0003 ainda propostos; se mudarem no G3, o PO reabre os CA afetados. Implementação depende da AH-0001.

# REQ-0002 — Tela de status no Portal Web

> [TESTE] DEM-2026-001 · origem: solicitação original ("uma tela simples no Portal que mostre esse status"). **v1.1:** premissas de acesso e oráculo de exibição atualizados (DEC-PO-0005).

**Requisito:** o Portal Web deve ter uma tela simples que consulta `GET /health` (REQ-0001) e, no caminho saudável, exibe ao usuário o status, a versão e o timestamp recebidos, com os valores brutos iguais aos da mesma consulta e formatação adicional em America/Sao_Paulo (US-0002 CA-01; D-UX-05/D-UX-08 aceitos).

**Premissa de teste (lacuna CPO):** público da tela = operador/equipe técnica interna (DEC-PO-0002).
**Premissa de acesso (ADR-0003 proposto, L5):** tela sem login nesta demanda.

**Fora do requisito (decisão de outros donos):** layout, navegação, textos, cores (UX/UI; protótipo v1.0 aprovado com ressalvas); forma de consumo da API (ARQ/AS).

**Rastreio:** US-0002 (CA-01, CA-02, CA-04); validação DEC-PO-0005.
