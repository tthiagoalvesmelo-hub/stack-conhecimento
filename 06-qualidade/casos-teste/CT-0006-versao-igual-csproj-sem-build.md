---
id: CT-0006
titulo: 'Versão = <Version> do .csproj, SemVer sem +build'
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

# CT-0006 — Versão = <Version> do .csproj, SemVer sem +build

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0001 CA-04; ADR-0001 v2 D8 item 1 (V; caso obrigatório pela R3); ADR-0002 v1.1; ET RT-04, PS-02 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Ler `<Version>` do `src/Portal.Api/Portal.Api.csproj` (XML) na SHA testada.
2. `GET /health`.
3. Comparar e validar pela expressão do RT-04 (com `\z`).

## Resultado esperado (oráculo)
- `version` == `<Version>` do `.csproj`.
- Sem `+` nem hash de commit; casa a expressão SemVer do RT-04.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
