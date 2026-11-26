---
id: REQ-0001
titulo: "Endpoint GET /health retorna status, versão e timestamp (200 e 503)"
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
relacionados: [DEM-2026-001, TASK-0002, TASK-0005, US-0001, RN-0001, ADR-0003, DEC-PO-0006, DEC-PO-0008, AH-0003, ADR-0001, ADR-0002]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (1) do G1 (atualizada em 26/11/2026 15:12 (America/Sao_Paulo), DEC-PO-0008):** os ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 foram **aceitos** (AH-0003 aprovada em 26/11/2026 14:54, America/Sao_Paulo, que substitui a AH-0001; G3 registrado em `a271ac1`). Os formatos, caminhos 503/405/500, tempo limite de 5 s e “sem login” seguem esses ADR aceitos. **Ressalva do G3:** R1..R5 (aprovacoes.md, 26/11/2026 15:08) — R1 (ET-0001 v1.4 da AS, condição para liberar a TASK-0008); R2 (teste de contrato com `format: date-time`); ressalva R3 do G3 (itens PV do ADR-0001 v2 D8 como testes obrigatórios antes do G4); R4 (SDK .NET 10 + Angular CLI e spike do encerramento gracioso em ASP.NET Core antes do CA-07); R5 (usar `\z` nas regex .NET). A implementação não depende mais da AH-0001.
>
> **v1.3** (26/11/2026 15:12 (America/Sao_Paulo)) — revisão editorial (DEC-PO-0008): premissas de stack e ADR atualizadas; nenhum critério de aceite das US foi reaberto nem alterado. Status **vigente** mantido.

# REQ-0001 — Endpoint GET /health

> [TESTE] DEM-2026-001 · origem: solicitação original. **v1.1** (DEC-PO-0006): alternativa **A** — o caminho HTTP 503 entra no aceite desta demanda, como premissa do ADR-0003 proposto, até a aceitação do ADR pelo ARQ (G3). A implementação da stack continua a depender da AH-0001.

**Requisito:** a API base do Portal Web deve expor o recurso `GET /health`, somente leitura, que:
1. em execução normal, responde **HTTP 200** e informa o **status** da API, a **versão** em execução e o **timestamp** da resposta (US-0001 CA-01 a CA-04 e CA-06);
2. quando o contrato vigente prever o caminho de indisponibilidade (ADR-0003 v1.1 aceito: processo em encerramento ou equivalente definido na ET), responde **HTTP 503** com o **mesmo esquema** e status de indisponibilidade (premissa: `"unavailable"`), **sem** detalhes de causa (US-0001 CA-07). A tela trata esse caminho conforme US-0002 CA-03 (RE-02: não exibe versão/timestamp);
3. em método diferente de `GET` (e de `HEAD`, se a ET o tolerar), responde **HTTP 405** com cabeçalho `Allow` (US-0001 CA-08);
4. em falha interna inesperada, responde **HTTP 500** no formato de erro padronizado da ET, **sem** detalhe interno (US-0001 CA-09, REQ-0004). O formato é decisão técnica (AS/ARQ); o comportamento funcional (não vazar dado, não ser saudável, tela em erro) entra no aceite.

**Fora do requisito (decisão de outros donos):** linguagem/framework (já tomada: ADR-0001 v2.0 / AH-0003 — C#/.NET 10 LTS + Angular 22.3); nomes exatos dos campos e valores de status, formato da versão e do timestamp (ARQ/AS; ADR-0002 v1.1 e ADR-0003 v1.1 aceitos; origem da versão = `<Version>` do `.csproj` do `portal-api`); autenticação e exposição (ARQ: contrato interno, sem autenticação, rede local/interna).

**Rastreio:** US-0001 (CA-01 a CA-09); US-0002 (CA-03).
