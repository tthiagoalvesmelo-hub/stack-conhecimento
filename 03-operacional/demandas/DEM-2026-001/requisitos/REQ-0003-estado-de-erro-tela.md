---
id: REQ-0003
titulo: "Tela exibe estado de erro quando a API está indisponível ou a consulta falha"
tipo: req
subtipo: funcional
versao: 1.1
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:16-03:00
atualizado_em: 2026-11-26T12:32-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0004, TASK-0005, US-0002, RN-0002, DEC-PO-0005, DEC-PO-0006]
substitui: null
substituido_por: null
---

# REQ-0003 — Estado de erro da tela quando a API está indisponível

> [TESTE] DEM-2026-001 · requisito derivado pelo PO (tratamento de falha; RN-0002). **v1.1:** inclui o 503 de contrato (alternativa A) e a decisão RE-02.

**Requisito:** quando o Portal não obtém uma resposta saudável e válida de `GET /health` — sem resposta, tempo esgotado, erro HTTP inesperado, conteúdo fora do esquema, **ou** HTTP 503 com status de indisponibilidade previsto no contrato —, a tela deve exibir um estado de erro/indisponível explícito, sem apresentar valores antigos como atuais, sem tela em branco e sem mensagem técnica. No 503 de contrato, **não exibe versão nem timestamp** (DEC-PO-0005, RE-02). Ao usuário atualizar a tela após a API voltar ao caminho saudável, deve passar a exibir o status atual.

**Fora do requisito:** solução visual e textos (UX/UI; spec v1.0 aprovada com ressalvas); tempo limite de espera e política de nova tentativa (AS/ARQ — orientação de 5 s, a fechar na ET). Polling automático está fora desta demanda (RE-04).

**Rastreio:** US-0002 (CA-03, CA-04, CA-05); RN-0002.
