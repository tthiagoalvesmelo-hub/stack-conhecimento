---
id: CT-0001
titulo: 'GET /health responde 200 com exatamente os três campos'
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

# CT-0001 — GET /health responde 200 com exatamente os três campos

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0001 CA-01; ADR-0001 v2 D8 item 4 (PV); ET RT-02 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Criar a fábrica sem override.
2. Enviar `GET /health`.
3. Validar status, `Content-Type` e corpo contra o esquema `HealthOk` do `openapi.yaml` 1.0.0.

## Resultado esperado (oráculo)
- HTTP 200; `Content-Type: application/json; charset=utf-8`.
- Corpo com **exatamente** `status`, `version`, `timestamp` (nenhum campo extra — `additionalProperties: false`), todos presentes, não nulos e não vazios.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
