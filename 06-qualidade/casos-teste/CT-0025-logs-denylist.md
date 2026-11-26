---
id: CT-0025
titulo: 'Logs (D8 item 13c): nenhum item da denylist em 200, 503 e 500'
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

# CT-0025 — Logs (D8 item 13c): nenhum item da denylist em 200, 503 e 500

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-API — Automatizado pelo FS (xUnit + `WebApplicationFactory`, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | ADR-0001 v2 D8 item 13; parecer G3 v1.2 §9.2 (3); US-0001 CA-05; RN-0001 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado no PT/PQ).
- Projeto `apps/portal-api/tests/Portal.Api.Tests` com `WebApplicationFactory<Program>` (DEC-ARQ-0011).
- Teste identificado pelo ID deste CT (ex.: `[Trait("CT", "CT-nnnn")]` ou nome do método contendo o ID).

## Passos
1. Sumidouro injetado; executar 200, 503 injetado e 500 injetado.
2. Inspecionar mensagem, estado e exceção capturados.

## Resultado esperado (oráculo)
- Nenhum dado pessoal, credencial, token, hostname, IP, caminho, versão de runtime/dependência, hash de commit ou valor de variável de ambiente.
- Rastreio de pilha do código próprio, se houver, só em registro Error — nunca no corpo HTTP.

## Evidência exigida
- Saída de `dotnet test` (log/TRX) com o nome do teste e o resultado, na SHA do G4; caminho e SHA do código do teste revisado pela QA (força das asserções conferida).
