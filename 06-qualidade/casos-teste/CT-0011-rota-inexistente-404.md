---
id: CT-0011
titulo: 'Rota inexistente ⇒ 404 problem+json padrão do serviço'
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

# CT-0011 — Rota inexistente ⇒ 404 problem+json padrão do serviço

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | ADR-0001 v2 D8 itens 2 e 6 (PV, cobertura 404); ET RT-08, RT-09, CE-09 (fora do aceite dos CA) |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Enviar `GET /inexistente`.

## Resultado esperado (oráculo)
- HTTP 404; `application/problem+json` com exatamente `type: about:blank`, `title: Not Found`, `status: 404`; sem `traceId`.
- `Cache-Control: no-store` e `X-Content-Type-Options: nosniff`.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
