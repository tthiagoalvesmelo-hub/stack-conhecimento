---
id: REQ-0004
titulo: "Sem dados pessoais, segredos ou detalhes internos na resposta e na tela"
tipo: req
subtipo: nao-funcional
versao: 1.1
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:16-03:00
atualizado_em: 2026-11-26T12:32-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, US-0001, US-0002, RN-0001, ADR-0002, ADR-0003]
substitui: null
substituido_por: null
---

# REQ-0004 — Segurança e LGPD (requisito não funcional)

> [TESTE] DEM-2026-001 · requisito derivado pelo PO (segurança desde a concepção; RN-0001). **v1.1:** pendência de sensibilidade da versão respondida pelo ARQ para exposição interna.

**Requisito:** a resposta de `GET /health` (200, 503, 405 e 500) e a tela de status não podem conter nem exibir dados pessoais, credenciais, segredos, tokens ou detalhes internos de infraestrutura/implementação (inclusive em respostas e mensagens de erro: hostnames, IPs, caminhos, versões de runtime/dependências, hash de commit, variáveis de ambiente, stack trace).

**Premissa (ADR-0002 proposto):** expor a versão do serviço em exposição **interna** não é considerado sensível; se o endpoint passar a ser exposto fora da rede interna, a exposição da versão deve ser reavaliada (R3/N3 + AH).

**Pendência residual (dono ARQ):** requisitos adicionais se a exposição mudar (autenticação, limitação de taxa, contrato público).

**Rastreio:** US-0001 (CA-05); US-0002 (CA-06); RN-0001.
