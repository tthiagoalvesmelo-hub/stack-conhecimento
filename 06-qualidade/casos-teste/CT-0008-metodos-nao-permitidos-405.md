---
id: CT-0008
titulo: 'Métodos não permitidos ⇒ 405 com Allow: GET, HEAD e problem+json'
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

# CT-0008 — Métodos não permitidos ⇒ 405 com Allow: GET, HEAD e problem+json

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0001 CA-08; ADR-0001 v2 D8 itens 2 e 5 (PV); ET RT-07, RT-08, CE-07 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Enviar `POST`, `PUT`, `PATCH` e `DELETE` para `/health`.

## Resultado esperado (oráculo)
- HTTP 405 em todos; cabeçalho `Allow: GET, HEAD`.
- `Content-Type: application/problem+json`; corpo exatamente `{type: "about:blank", title: "Method Not Allowed", status: 405}`; **sem** `traceId` nem detalhe.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
