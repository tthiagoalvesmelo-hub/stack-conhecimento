---
id: CT-0004
titulo: 'R2: validação do timestamp com format: date-time e controle negativo do validador'
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

# CT-0004 — R2: validação do timestamp com format: date-time e controle negativo do validador

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | Ressalva R2 do G3; US-0001 CA-03; ET PS-09 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Validar o corpo real do 200 e do 503 (injetado) contra o esquema com `format: date-time` **ativo**.
2. Controle negativo: submeter ao mesmo validador `2026-02-31T10:00:00.000Z` (aceito pelo `pattern`, data inexistente).
3. Controle positivo: `2026-11-26T15:34:56.789Z`.

## Resultado esperado (oráculo)
- Corpos reais aprovados.
- O valor `2026-02-31T10:00:00.000Z` é **reprovado** pelo validador; se for aceito, o teste falha (validador sem `format` não vale como evidência).
- Valor positivo aprovado.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).

## Observações
- Biblioteca de validação de esquema (PS-09) a aprovar pelo ARQ; sem ela, validação explícita equivalente com o mesmo controle negativo.
