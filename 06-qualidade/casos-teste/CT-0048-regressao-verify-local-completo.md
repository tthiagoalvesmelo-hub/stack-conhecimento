---
id: CT-0048
titulo: 'Regressão R3: verify-local completo e suíte 100% na SHA do G4'
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

# CT-0048 — Regressão R3: verify-local completo e suíte 100% na SHA do G4

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-EVID — Verificação da QA sobre evidências do `verify-local` e da suíte |
| Rastreio | Matriz R3 (regressão completa); critérios do PQ; DEC-ARQ-0007 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- `scripts/verify-local.sh` executado na versão do G4: log integral anexado pelo FS ao PR, reexecução do CR (DEC-ARQ-0007 §3) e reexecução da QA na mesma SHA.
- Rede disponível (sem rede, NuGet Audit e `npm audit` não valem como evidência — DEC-ARQ-0007 §4).

## Passos
1. Reexecutar `scripts/verify-local.sh` na SHA aprovada no G4.
2. Conferir A1–A5 e W1–W5 aprovados e a lista de testes executados.

## Resultado esperado (oráculo)
- Todos os passos aprovados; SHA == G4.
- Todos os CT automatizados (CT-0001..CT-0032) presentes e aprovados; teste em quarentena não conta como aprovado (TD-nnnn).

## Evidência exigida
- Log/relatório do passo do `verify-local` arquivado em `evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado, sanitizado), citado no PQ.
