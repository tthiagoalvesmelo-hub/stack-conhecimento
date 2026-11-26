---
id: CT-0013
titulo: 'X-Request-Id: devolve UUID canônico válido; senão gera v4; nunca 400'
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

# CT-0013 — X-Request-Id: devolve UUID canônico válido; senão gera v4; nunca 400

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | ADR-0001 v2 D8 item 7; ET RT-09, L-03; US-0001 CA-05 (sem eco de valor inválido) |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Requisição com `X-Request-Id` canônico válido.
2. Sem o cabeçalho.
3. Com valores inválidos: maiúsculas, `abc`, 37 caracteres, UUID com chaves.

## Resultado esperado (oráculo)
- Válido: devolvido idêntico.
- Ausente/inválido: resposta traz UUID v4 canônico novo (hex minúsculo, 36 caracteres, validado com `\z`); o valor inválido não é ecoado.
- Nunca 400; status do caminho normal (200).

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
