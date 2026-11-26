---
id: REQ-0002
titulo: "Tela de status no Portal exibe status, versão e timestamp"
tipo: req
subtipo: funcional
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:16-03:00
atualizado_em: 2026-11-26T12:16-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, US-0002, REQ-0001]
substitui: null
substituido_por: null
---

# REQ-0002 — Tela de status no Portal Web

> [TESTE] DEM-2026-001 · TASK-0002 · origem: solicitação original ("uma tela simples no Portal que mostre esse status").

**Requisito:** o Portal Web deve ter uma tela simples que consulta `GET /health` (REQ-0001) e exibe ao usuário o status, a versão e o timestamp recebidos.

**Premissa de teste (lacuna CPO):** público da tela = operador/equipe técnica interna (DEC-PO-0002).

**Fora do requisito (decisão de outros donos):** layout, navegação, textos, cores e formato de exibição do timestamp/fuso (UX/UI); forma de acesso à tela (autenticação) e do consumo da API (ARQ/AS).

**Rastreio:** US-0002 (CA-01, CA-02, CA-04).
