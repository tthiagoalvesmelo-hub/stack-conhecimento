---
id: CT-0022
titulo: 'L-12 nº 6: superfície registrada = só /health (GET/HEAD) e preflight'
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

# CT-0022 — L-12 nº 6: superfície registrada = só /health (GET/HEAD) e preflight

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | DEC-ARQ-0011 §6 (6), §3–4; ADR-0001 v2 D8 item 11 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Enumerar os endpoints registrados na composição de produção (mecanismo definido pelo FS, ex.: fonte de endpoints do ASP.NET Core).

## Resultado esperado (oráculo)
- Somente `/health` com `GET` e `HEAD`; o preflight tratado pelo middleware de CORS; nenhum endpoint de diagnóstico, de falha ou de controle.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).

## Observações
- Se o FS mapear `OPTIONS` como endpoint explícito, a aceitação depende do ARQ (lacuna L-PT-11).
