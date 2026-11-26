---
id: RN-0002
titulo: "Indisponibilidade nunca é apresentada como saudável"
tipo: rn
versao: 1.3
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:15-03:00
atualizado_em: 2026-11-26T15:12-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0004, TASK-0005, REQ-0003, US-0002, ADR-0003, DEC-PO-0005, DEC-PO-0008, AH-0003, DEC-PO-0006]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (1) do G1 (atualizada em 26/11/2026 15:12 (America/Sao_Paulo), DEC-PO-0008):** os ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 foram **aceitos** (AH-0003 aprovada em 26/11/2026 14:54, America/Sao_Paulo, que substitui a AH-0001; G3 registrado em `a271ac1`). Os formatos, caminhos 503/405/500, tempo limite de 5 s e “sem login” seguem esses ADR aceitos. **Ressalva do G3:** R1..R5 (aprovacoes.md, 26/11/2026 15:08) — R1 (ET-0001 v1.4 da AS, condição para liberar a TASK-0008); R2 (teste de contrato com `format: date-time`); ressalva R3 do G3 (itens PV do ADR-0001 v2 D8 como testes obrigatórios antes do G4); R4 (SDK .NET 10 + Angular CLI e spike do encerramento gracioso em ASP.NET Core antes do CA-07); R5 (usar `\z` nas regex .NET). A implementação não depende mais da AH-0001.
>
> **v1.3** (26/11/2026 15:12 (America/Sao_Paulo)) — revisão editorial (DEC-PO-0008): ressalva (1) do G1 atualizada (ADR-0003 v1.1 aceito; ressalvas R1..R5 do G3). Nenhum CA foi reaberto nem alterado. Status **vigente** mantido.

# RN-0002 — Indisponibilidade nunca é apresentada como saudável

> [TESTE] Origem: DEM-2026-001 · TASK-0002 · **v1.1:** o HTTP 503 de contrato também nunca é apresentado como saudável.

**Regra:** a ausência de uma resposta **saudável e válida** do health-check (sem resposta, tempo esgotado, resposta de erro, conteúdo inválido, ou HTTP 503 com status de indisponibilidade previsto no contrato) deve ser tratada pelo Portal como **estado de erro/indisponível**. O Portal nunca apresenta um status anterior (último valor conhecido) como se fosse o status atual, nunca assume "saudável" por padrão e nunca trata o 503 como estado operacional.

**Justificativa:** o valor do health-check é a confiança no sinal; um falso "saudável" é pior que a ausência de informação.

**Aplicação:** REQ-0003; CA-03, CA-04 e CA-05 da US-0002. A forma visual do estado de erro é decisão do UX/UI (spec v1.0 aprovada com ressalvas; no 503, versão e timestamp não são exibidos — RE-02).
