---
id: CT-0045
titulo: 'SCA da API: NuGet Audit no restore e JSON do dotnet list package'
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

# CT-0045 — SCA da API: NuGet Audit no restore e JSON do dotnet list package

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-EVID — Verificação da QA sobre evidências do `verify-local` e da suíte |
| Rastreio | DEC-ARQ-0009 v1.1 item 1; DEC-ARQ-0007 v1.1 A1 e A5 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- `scripts/verify-local.sh` executado na versão do G4: log integral anexado pelo FS ao PR, reexecução do CR (DEC-ARQ-0007 §3) e reexecução da QA na mesma SHA.
- Rede disponível (sem rede, NuGet Audit e `npm audit` não valem como evidência — DEC-ARQ-0007 §4).

## Passos
1. Conferir em `Directory.Build.props`: `NuGetAuditLevel=high`, `NuGetAuditMode=all`, NU1903, NU1904 e NU1900 como erro.
2. Ler o log do A1 (`dotnet restore --locked-mode`).
3. Ler o JSON de `dotnet list package --vulnerable --include-transitive --format json --output-version 1` (A5): `projects[].frameworks[].topLevelPackages[]` e `transitivePackages[]`, `vulnerabilities[].severity`.

## Resultado esperado (oráculo)
- A1 sem NU1903/NU1904/NU1900 (auditoria executada).
- Nenhuma severidade `High` ou `Critical` (sem distinguir maiúsculas); Moderate/Low só reportadas.
- Comando sem falha real de execução (JSON válido, restore sem erro). O **código de saída não é usado como oráculo**.

## Evidência exigida
- Log/relatório do passo do `verify-local` arquivado em `evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado, sanitizado), citado no PQ.

## Observações
- Exceção a vulnerabilidade alta/crítica só com AH de segurança.
