---
id: REQ-0003
titulo: "Tela exibe estado de erro quando a API está indisponível"
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
relacionados: [DEM-2026-001, TASK-0002, US-0002, RN-0002]
substitui: null
substituido_por: null
---

# REQ-0003 — Estado de erro da tela quando a API está indisponível

> [TESTE] DEM-2026-001 · TASK-0002 · requisito derivado pelo PO (tratamento de falha; RN-0002).

**Requisito:** quando o Portal não obtém uma resposta válida de `GET /health` (sem resposta, tempo esgotado, erro HTTP ou conteúdo inválido), a tela deve exibir um estado de erro explícito, sem apresentar valores antigos como atuais e sem quebrar. Ao usuário atualizar a tela após a API voltar, deve passar a exibir o status atual.

**Fora do requisito:** solução visual e textos (UX/UI); tempo limite de espera e política de nova tentativa (AS/ARQ — a definir na especificação).

**Rastreio:** US-0002 (CA-03, CA-05); RN-0002.
