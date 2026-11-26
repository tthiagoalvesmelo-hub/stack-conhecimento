---
id: REQ-0001
titulo: "Endpoint GET /health retorna status, versão e timestamp (200 e 503)"
tipo: req
subtipo: funcional
versao: 1.2
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:16-03:00
atualizado_em: 2026-11-26T12:41-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0005, US-0001, RN-0001, ADR-0003, DEC-PO-0006]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (condição 1 do G1):** formatos, 503/405/500, tempo limite de 5 s e “sem login” dependem dos ADR-0002/0003 ainda propostos; se mudarem no G3, o PO reabre os CA afetados. Implementação depende da AH-0001.

# REQ-0001 — Endpoint GET /health

> [TESTE] DEM-2026-001 · origem: solicitação original. **v1.1** (DEC-PO-0006): alternativa **A** — o caminho HTTP 503 entra no aceite desta demanda, como premissa do ADR-0003 proposto, até a aceitação do ADR pelo ARQ (G3). A implementação da stack continua a depender da AH-0001.

**Requisito:** a API base do Portal Web deve expor o recurso `GET /health`, somente leitura, que:
1. em execução normal, responde **HTTP 200** e informa o **status** da API, a **versão** em execução e o **timestamp** da resposta (US-0001 CA-01 a CA-04 e CA-06);
2. quando o contrato vigente prever o caminho de indisponibilidade (premissa ADR-0003: processo em encerramento ou equivalente definido na ET), responde **HTTP 503** com o **mesmo esquema** e status de indisponibilidade (premissa: `"unavailable"`), **sem** detalhes de causa (US-0001 CA-07). A tela trata esse caminho conforme US-0002 CA-03 (RE-02: não exibe versão/timestamp);
3. em método diferente de `GET` (e de `HEAD`, se a ET o tolerar), responde **HTTP 405** com cabeçalho `Allow` (US-0001 CA-08);
4. em falha interna inesperada, responde **HTTP 500** no formato de erro padronizado da ET, **sem** detalhe interno (US-0001 CA-09, REQ-0004). O formato é decisão técnica (AS/ARQ); o comportamento funcional (não vazar dado, não ser saudável, tela em erro) entra no aceite.

**Fora do requisito (decisão de outros donos):** linguagem/framework (ADR-0001 / AH-0001); nomes exatos dos campos e valores de status, formato da versão e do timestamp (ARQ/AS; premissa nos ADR-0002/0003 propostos); autenticação e exposição (ARQ: contrato interno, sem autenticação, rede local/interna).

**Rastreio:** US-0001 (CA-01 a CA-09); US-0002 (CA-03).
