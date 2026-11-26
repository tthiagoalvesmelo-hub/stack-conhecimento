---
id: REQ-0004
titulo: "Sem dados pessoais, segredos ou detalhes internos na resposta e na tela"
tipo: req
subtipo: nao-funcional
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:16-03:00
atualizado_em: 2026-11-26T12:16-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, US-0001, US-0002, RN-0001]
substitui: null
substituido_por: null
---

# REQ-0004 — Segurança e LGPD (requisito não funcional)

> [TESTE] DEM-2026-001 · TASK-0002 · requisito derivado pelo PO (segurança desde a concepção; RN-0001).

**Requisito:** a resposta de `GET /health` e a tela de status não podem conter nem exibir dados pessoais, credenciais, segredos, tokens ou detalhes internos de infraestrutura/implementação (inclusive em respostas e mensagens de erro).

**Pendência (dono ARQ):** requisitos de segurança adicionais do endpoint (exposição, autenticação, limitação de taxa) e confirmação da classe de risco (R2 padrão; R3 se for contrato público).

**Rastreio:** US-0001 (CA-05); US-0002 (CA-06); RN-0001.
