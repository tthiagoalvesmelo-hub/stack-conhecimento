---
id: CT-0003
titulo: 'Timestamp com 3 casas, UTC e Z, a partir do TimeProvider injetado'
tipo: ct
versao: 1.0
status: vigente
dono: QA
autores: [QA]
aprovado_por: QA
criado_em: 2026-11-26T15:35-03:00
atualizado_em: 2026-11-26T15:35-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, PT-0001]
substitui: null
substituido_por: null
---

# CT-0003 — Timestamp com 3 casas, UTC e Z, a partir do TimeProvider injetado

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0001 CA-03; ADR-0001 v2 D8 item 3 (PV); ET RT-05, PS-07 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Substituir o `TimeProvider` por um relógio fixo (ex.: 2026-11-26T15:34:56.7891234Z).
2. Executar com cultura corrente não invariante (ex.: pt-BR).
3. `GET /health`.

## Resultado esperado (oráculo)
- `timestamp` == `2026-11-26T15:34:56.789Z` (exatamente 3 casas, `Z`, cultura invariante; nunca 7 casas).
- Igualdade exata ao instante simulado.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
