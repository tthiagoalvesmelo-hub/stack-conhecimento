---
id: REQ-0001
titulo: "Endpoint GET /health retorna status, versão e timestamp"
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
relacionados: [DEM-2026-001, TASK-0002, US-0001, RN-0001]
substitui: null
substituido_por: null
---

# REQ-0001 — Endpoint GET /health

> [TESTE] DEM-2026-001 · TASK-0002 · origem: solicitação original ("endpoint de health-check (GET /health) na API base do Portal Web, retornando status, versão e timestamp").

**Requisito:** a API base do Portal Web deve expor o recurso `GET /health`, somente leitura, que responde com HTTP 200 e informa o **status** da API, a **versão** em execução e o **timestamp** da resposta.

**Fora do requisito (decisão de outros donos):** linguagem/framework, nomes exatos dos campos e valores de status, formato da versão e do timestamp (ARQ, TASK-0003); contrato detalhado (AS/ARQ); autenticação e exposição interna ou pública do endpoint (ARQ).

**Rastreio:** US-0001 (CA-01 a CA-04, CA-06).
