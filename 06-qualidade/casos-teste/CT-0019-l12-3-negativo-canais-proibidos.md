---
id: CT-0019
titulo: 'L-12 nº 3: query, cabeçalho ou variável de ambiente não forçam 503/500'
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

# CT-0019 — L-12 nº 3: query, cabeçalho ou variável de ambiente não forçam 503/500

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | DEC-ARQ-0011 §6 (3) e §3; US-0001 CA-05; REQ-0004; ADR-0001 v2 D8 item 11 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Fábrica sem override.
2. `GET /health?force=503`, `?status=500`, `?fail=true`.
3. Cabeçalhos `X-Force-Status: 503`, `X-Health-Fail: 1`.
4. Variáveis de ambiente fictícias definidas antes da criação da fábrica: `FORCE_HEALTH_STATUS=503`, `HEALTH_FAIL=1`.

## Resultado esperado (oráculo)
- Todas as respostas permanecem 200 com o corpo saudável.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).

## Observações
- Os nomes são representativos (escolha de desenho da QA); o oráculo é "nenhum canal externo altera o caminho". Complemento black-box: CT-0036.
