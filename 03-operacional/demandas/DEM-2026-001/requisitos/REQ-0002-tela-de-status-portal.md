---
id: REQ-0002
titulo: "Tela de status no Portal exibe status, versão e timestamp"
tipo: req
subtipo: funcional
versao: 1.3
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:16-03:00
atualizado_em: 2026-11-26T15:12-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0004, US-0002, REQ-0001, DEC-PO-0002, DEC-PO-0005, DEC-PO-0008, AH-0003, ADR-0001, ADR-0003]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (1) do G1 (atualizada em 26/11/2026 15:12 (America/Sao_Paulo), DEC-PO-0008):** os ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 foram **aceitos** (AH-0003 aprovada em 26/11/2026 14:54, America/Sao_Paulo, que substitui a AH-0001; G3 registrado em `a271ac1`). Os formatos, caminhos 503/405/500, tempo limite de 5 s e “sem login” seguem esses ADR aceitos. **Ressalva do G3:** R1..R5 (aprovacoes.md, 26/11/2026 15:08) — R1 (ET-0001 v1.4 da AS, condição para liberar a TASK-0008); R2 (teste de contrato com `format: date-time`); ressalva R3 do G3 (itens PV do ADR-0001 v2 D8 como testes obrigatórios antes do G4); R4 (SDK .NET 10 + Angular CLI e spike do encerramento gracioso em ASP.NET Core antes do CA-07); R5 (usar `\z` nas regex .NET). A implementação não depende mais da AH-0001.
>
> **v1.3** (26/11/2026 15:12 (America/Sao_Paulo)) — revisão editorial (DEC-PO-0008): premissas de stack e acesso atualizadas (ADR-0001 v2.0 / ADR-0003 v1.1; público confirmado pela CPO). Nenhum CA foi reaberto nem alterado. Status **vigente** mantido.

# REQ-0002 — Tela de status no Portal Web

> [TESTE] DEM-2026-001 · origem: solicitação original ("uma tela simples no Portal que mostre esse status"). **v1.1:** premissas de acesso e oráculo de exibição atualizados (DEC-PO-0005).

**Requisito:** o Portal Web deve ter uma tela simples que consulta `GET /health` (REQ-0001) e, no caminho saudável, exibe ao usuário o status, a versão e o timestamp recebidos, com os valores brutos iguais aos da mesma consulta e formatação adicional em America/Sao_Paulo (US-0002 CA-01; D-UX-05/D-UX-08 aceitos).

**Premissa de teste:** público da tela = operador/equipe técnica interna (DEC-PO-0002, confirmado pela CPO em 26/11/2026 12:36).
**Premissa de acesso (ADR-0003 v1.1 aceito, L5):** tela sem login nesta demanda.
**Stack (fora da alçada do PO):** Portal em Angular 22.3 (ADR-0001 v2.0 / AH-0003).

**Fora do requisito (decisão de outros donos):** layout, navegação, textos, cores (UX/UI; protótipo v1.0 aprovado com ressalvas); forma de consumo da API (ARQ/AS).

**Rastreio:** US-0002 (CA-01, CA-02, CA-04); validação DEC-PO-0005.
