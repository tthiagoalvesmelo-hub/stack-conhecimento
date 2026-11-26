---
id: CT-0014
titulo: 'CORS: origem permitida recebe ACAO exata; origem negada sem ACAO e sem 403'
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

# CT-0014 — CORS: origem permitida recebe ACAO exata; origem negada sem ACAO e sem 403

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | ADR-0001 v2 D8 item 8 (PV); ET RT-10, CE-08, L-06 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. `GET /health` com `Origin` = origem configurada.
2. `GET /health` com `Origin` diferente (ex.: outra porta).

## Resultado esperado (oráculo)
- Permitida: `Access-Control-Allow-Origin` = origem exata (nunca `*`); sem `Access-Control-Allow-Credentials`.
- Negada: HTTP 200 normal, **sem** `Access-Control-Allow-Origin`, **sem** 403.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
