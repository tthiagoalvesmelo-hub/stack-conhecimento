---
id: CT-0044
titulo: 'Cobertura do Portal ≥ 80% de linhas (@vitest/coverage-v8)'
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

# CT-0044 — Cobertura do Portal ≥ 80% de linhas (@vitest/coverage-v8)

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-EVID — Verificação da QA sobre evidências do `verify-local` e da suíte |
| Rastreio | DEC-ARQ-0007 v1.1 W3; parecer G3 v1.2 §9.2 (1) |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- `scripts/verify-local.sh` executado na versão do G4: log integral anexado pelo FS ao PR, reexecução do CR (DEC-ARQ-0007 §3) e reexecução da QA na mesma SHA.
- Rede disponível (sem rede, NuGet Audit e `npm audit` não valem como evidência — DEC-ARQ-0007 §4).

## Passos
1. Conferir `@vitest/coverage-v8` em devDependencies e no `package-lock.json`, com versão alinhada à do `vitest`.
2. Conferir no `angular.json` (`architect.test.options`): `"coverage": true` e `"coverageThresholds": { "lines": 80 }`, sem outros limiares de falha.
3. Executar/ler `ng test --no-watch --coverage`; conferir exclusão dos `*.spec.ts`.

## Resultado esperado (oráculo)
- ≥ 80% de linhas do código da aplicação; ramos, funções e statements apenas reportados.
- Passo W3 aprovado.

## Evidência exigida
- Log/relatório do passo do `verify-local` arquivado em `evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado, sanitizado), citado no PQ.
