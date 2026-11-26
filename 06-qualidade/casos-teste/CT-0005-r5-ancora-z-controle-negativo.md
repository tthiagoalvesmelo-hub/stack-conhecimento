---
id: CT-0005
titulo: 'R5: âncora \z nas expressões .NET, com controle negativo de \n final'
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

# CT-0005 — R5: âncora \z nas expressões .NET, com controle negativo de \n final

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | Ressalva R5 do G3; ADR-0001 v2 D8 item 12 (PV); US-0001 CA-03, CA-04 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Conferir que as expressões de `version`, `timestamp` e UUID usadas nos testes .NET terminam em `\z` (não `$`).
2. Controle negativo: `0.1.0\n`, `2026-11-26T15:34:56.789Z\n` e um UUID canônico seguido de `\n`.
3. Controle positivo: os mesmos valores sem `\n`.

## Resultado esperado (oráculo)
- Os três valores com `\n` final são **reprovados**.
- Os valores sem `\n` são aprovados.
- Nenhuma expressão de teste .NET termina em `$`.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
