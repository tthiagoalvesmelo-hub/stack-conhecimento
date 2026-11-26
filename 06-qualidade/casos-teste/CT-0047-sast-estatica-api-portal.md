---
id: CT-0047
titulo: 'SAST/análise estática no recorte da DEC-ARQ-0009'
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

# CT-0047 — SAST/análise estática no recorte da DEC-ARQ-0009

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-EVID — Verificação da QA sobre evidências do `verify-local` e da suíte |
| Rastreio | DEC-ARQ-0009 v1.1 itens 3 e 4; DEC-ARQ-0008; DEC-ARQ-0007 A2, A3, W2 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- `scripts/verify-local.sh` executado na versão do G4: log integral anexado pelo FS ao PR, reexecução do CR (DEC-ARQ-0007 §3) e reexecução da QA na mesma SHA.
- Rede disponível (sem rede, NuGet Audit e `npm audit` não valem como evidência — DEC-ARQ-0007 §4).

## Passos
1. Conferir em `Directory.Build.props`: `AnalysisModeSecurity=All`, `TreatWarningsAsErrors=true`, `EnableNETAnalyzers=true`, `AnalysisLevel=10-recommended`.
2. Ler os logs de `dotnet format --verify-no-changes`, `dotnet build -c Release --no-restore -warnaserror` e `ng lint`.

## Resultado esperado (oráculo)
- Build com zero avisos; formato sem diferença; `ng lint` com zero avisos.
- Limite declarado no PQ: `angular-eslint` **não** é SAST de segurança (DEC-ARQ-0009 item 4).

## Evidência exigida
- Log/relatório do passo do `verify-local` arquivado em `evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado, sanitizado), citado no PQ.
