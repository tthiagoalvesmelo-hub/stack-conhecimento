---
id: CT-0049
titulo: 'Verificação da suíte do FS: rastreio por CT e mutações de controle'
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

# CT-0049 — Verificação da suíte do FS: rastreio por CT e mutações de controle

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-EVID — Verificação da QA sobre evidências do `verify-local` e da suíte |
| Rastreio | DEC-ARQ-0011 v1.1 (opção A); DEC-PO-0009; ressalvas R2, R3, R5 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- `scripts/verify-local.sh` executado na versão do G4: log integral anexado pelo FS ao PR, reexecução do CR (DEC-ARQ-0007 §3) e reexecução da QA na mesma SHA.
- Rede disponível (sem rede, NuGet Audit e `npm audit` não valem como evidência — DEC-ARQ-0007 §4).

## Passos
1. Conferir que cada CT automatizado (CT-0001..CT-0032) tem teste identificável pelo ID.
2. Revisar a força das asserções frente ao resultado esperado de cada CT.
3. Mutações de controle, numa cópia descartável fora do repositório do FS: (a) remover o override de falha ⇒ CT-0017 deve falhar; (b) trocar `\z` por `$` ⇒ controle negativo do CT-0005 deve falhar; (c) desativar o `format` ⇒ controle negativo do CT-0004 deve falhar.

## Resultado esperado (oráculo)
- 100% dos CT automatizados rastreados por ID.
- As três mutações são detectadas pela suíte.

## Evidência exigida
- Log/relatório do passo do `verify-local` arquivado em `evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado, sanitizado), citado no PQ.

## Observações
- A QA não corrige o código testado; achados viram BUG-nnnn para o FS.
