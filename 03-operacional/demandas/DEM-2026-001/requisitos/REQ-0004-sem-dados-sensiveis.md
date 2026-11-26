---
id: REQ-0004
titulo: "Sem dados pessoais, segredos ou detalhes internos na resposta e na tela"
tipo: req
subtipo: nao-funcional
versao: 1.3
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:16-03:00
atualizado_em: 2026-11-26T15:12-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, US-0001, US-0002, RN-0001, ADR-0002, ADR-0003, DEC-PO-0008, AH-0003]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (1) do G1 (atualizada em 26/11/2026 15:12 (America/Sao_Paulo), DEC-PO-0008):** os ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 foram **aceitos** (AH-0003 aprovada em 26/11/2026 14:54, America/Sao_Paulo, que substitui a AH-0001; G3 registrado em `a271ac1`). Os formatos, caminhos 503/405/500, tempo limite de 5 s e “sem login” seguem esses ADR aceitos. **Ressalva do G3:** R1..R5 (aprovacoes.md, 26/11/2026 15:08) — R1 (ET-0001 v1.4 da AS, condição para liberar a TASK-0008); R2 (teste de contrato com `format: date-time`); ressalva R3 do G3 (itens PV do ADR-0001 v2 D8 como testes obrigatórios antes do G4); R4 (SDK .NET 10 + Angular CLI e spike do encerramento gracioso em ASP.NET Core antes do CA-07); R5 (usar `\z` nas regex .NET). A implementação não depende mais da AH-0001.
>
> **v1.3** (26/11/2026 15:12 (America/Sao_Paulo)) — revisão editorial (DEC-PO-0008): premissa do ADR-0002 atualizada para v1.1 aceito. Nenhum CA foi reaberto nem alterado. Status **vigente** mantido.

# REQ-0004 — Segurança e LGPD (requisito não funcional)

> [TESTE] DEM-2026-001 · requisito derivado pelo PO (segurança desde a concepção; RN-0001). **v1.1:** pendência de sensibilidade da versão respondida pelo ARQ para exposição interna.

**Requisito:** a resposta de `GET /health` (200, 503, 405 e 500) e a tela de status não podem conter nem exibir dados pessoais, credenciais, segredos, tokens ou detalhes internos de infraestrutura/implementação (inclusive em respostas e mensagens de erro: hostnames, IPs, caminhos, versões de runtime/dependências, hash de commit, variáveis de ambiente, stack trace).

**Premissa (ADR-0002 v1.1 aceito):** expor a versão do serviço em exposição **interna** não é considerado sensível; se o endpoint passar a ser exposto fora da rede interna, a exposição da versão deve ser reavaliada (R3/N3 + AH).

**Pendência residual (dono ARQ):** requisitos adicionais se a exposição mudar (autenticação, limitação de taxa, contrato público).

**Rastreio:** US-0001 (CA-05); US-0002 (CA-06); RN-0001.
