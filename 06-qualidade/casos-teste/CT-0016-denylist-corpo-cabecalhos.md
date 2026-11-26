---
id: CT-0016
titulo: 'Denylist: nenhum dado sensível em corpo e cabeçalhos (200, 405, 503, 500)'
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

# CT-0016 — Denylist: nenhum dado sensível em corpo e cabeçalhos (200, 405, 503, 500)

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0001 CA-05; RN-0001; REQ-0004; ET RT-12, CE-13, CE-14 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Coletar corpo e cabeçalhos de 200, 405, 503 (injetado) e 500 (injetado).
2. Procurar a denylist: dados pessoais, credenciais, tokens, hostname da máquina, IPs, caminhos, versões de runtime/dependências, hash de commit, valores de variáveis de ambiente, stack trace.

## Resultado esperado (oráculo)
- Nenhuma ocorrência; corpo limitado ao esquema (200/503) ou a `type/title/status` (405/500).

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
