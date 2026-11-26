---
id: CT-0010
titulo: 'Preflight OPTIONS ⇒ 204 com métodos GET, HEAD'
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

# CT-0010 — Preflight OPTIONS ⇒ 204 com métodos GET, HEAD

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | ADR-0001 v2 D8 itens 5 e 8 (PV); ET RT-16, CE-11 (fora do aceite dos CA) |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Enviar `OPTIONS /health` com `Origin` = origem configurada e `Access-Control-Request-Method: GET`.

## Resultado esperado (oráculo)
- HTTP 204 sem corpo; `Access-Control-Allow-Methods` contém só `GET, HEAD`; `Access-Control-Allow-Origin` = origem exata; sem `Access-Control-Allow-Credentials` e sem `Access-Control-Allow-Headers`.
- Também `Cache-Control: no-store` e `X-Content-Type-Options: nosniff` (D8 item 6).

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).

## Observações
- O comportamento de `OPTIONS` **sem** cabeçalhos de preflight não está definido (lacuna L-PT-03, ARQ/AS); não é oráculo deste CT.
