---
id: DEC-ARQ-0007
titulo: "Substituto local do pré-requisito 'CI verde' para .NET + Angular (verify-local)"
tipo: dec
versao: 1.1
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:03-03:00
atualizado_em: 2026-11-26T15:23-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0008, TASK-0009, TASK-0010, TASK-0012, AH-0003, ADR-0001, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, L-CR1]
substitui: DEC-ARQ-0003
substituido_por: null
---

# DEC-ARQ-0007 — `verify-local` para .NET + Angular (substitui DEC-ARQ-0003)

> [TESTE] Fase de testes internos; nada vai à produção. Mantém o propósito da DEC-ARQ-0003 (substituto local e reproduzível do "CI verde", L-CR1) e troca as ferramentas pela stack do **ADR-0001 v2** (AH-0003). Não é N3 (sem pipeline, sem custo, sem produção). Bloqueia a **entrada no G4**; deve estar cumprida no PR da TASK-0008.

## Decisão
1. O FS inclui em `/workspace/projetos/portal/` um script único e versionado, `scripts/verify-local.sh`, com falha imediata e saída integral registrada, que executa em sequência:

**API (`apps/portal-api`)**
| # | Passo | Critério |
|---|---|---|
| A1 | `dotnet restore --locked-mode` | `packages.lock.json` versionado (`RestorePackagesWithLockFile=true` em `Directory.Build.props`). O **NuGet Audit** roda no restore com `NuGetAuditLevel=high` e `NuGetAuditMode=all`; os avisos **NU1903** (alta) e **NU1904** (crítica) são tratados como erro, e **NU1900** (auditoria não executou) também reprova: auditoria silenciosamente ausente não vale como evidência (fonte: https://learn.microsoft.com/en-us/nuget/concepts/auditing-packages) |
| A2 | `dotnet format --verify-no-changes` | DEC-ARQ-0008 |
| A3 | `dotnet build -c Release --no-restore -warnaserror` | zero avisos (analyzers: DEC-ARQ-0008/0009) |
| A4 | `dotnet test -c Release --no-build` com cobertura Coverlet (`coverlet.msbuild`): `/p:CollectCoverage=true /p:Threshold=80 /p:ThresholdType=line /p:ThresholdStat=total /p:CoverletOutputFormat=cobertura` | **≥ 80% de linhas** do módulo `Portal.Api` (exclui o projeto de testes). Ramos e métodos: reportados, sem limiar (alinhado ao QA) |
| A5 | `dotnet list package --vulnerable --include-transitive --format json --output-version 1` (no SDK 10: também `dotnet package list` com os mesmos argumentos; https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-list) | Evidência independente do A1. **O código de saída do comando, por si só, não decide a reprovação:** a documentação oficial (Learn) **não declara** código de saída não-zero quando há vulnerabilidades; o repositório oficial `dotnet/sdk` (issue #16852) relata saída **0** mesmo com pacotes vulneráveis. Esta sessão **não executou** o comando (SDK não instalado). O script **analisa o JSON** (`projects[].frameworks[].topLevelPackages[]` e `transitivePackages[]`, campo `vulnerabilities[].severity`) e **reprova** se qualquer severidade for `High` ou `Critical` (comparação sem distinguir maiúsculas). Moderate/Low: apenas reportadas. Também reprova se o comando falhar de fato (JSON inválido, restore com erro, ou código de saída ≠ 0 por falha de execução — distinto de "listou vulnerabilidades e saiu 0"). A1 continua sendo a barreira no restore: NU1903/NU1904 (e NU1900) como erro (https://learn.microsoft.com/en-us/nuget/concepts/auditing-packages). Evidência: arquivo JSON sanitizado, sem valores de ambiente |

**Web (`apps/portal-web`)**
| # | Passo | Critério |
|---|---|---|
| W1 | `npm ci` | `package-lock.json` obrigatório |
| W2 | `ng lint` | DEC-ARQ-0008; zero avisos |
| W3 | `ng test --no-watch --coverage` | **≥ 80% de linhas** do código da aplicação (excluídos `*.spec.ts`). Pacote obrigatório, documentado pelo Angular: **`@vitest/coverage-v8`** (devDependency; MIT; gratuito; versão alinhada à do `vitest` do workspace — peer atual 5.1.2 no npm, 26/11/2026). Fonte: https://angular.dev/guide/testing/code-coverage ("To generate code coverage reports with Vitest, you must install the `@vitest/coverage-v8` package") e https://angular.dev/cli/test. Limiar no `angular.json` (`architect.test.options`): `"coverage": true` e `"coverageThresholds": { "lines": 80 }` — só linhas no patamar; ramos/funções/statements podem ser reportados (`coverageReporters`), sem limiar neste recorte (alinhado ao QA). É o provedor documentado do builder; não adoto `@vitest/coverage-istanbul` (exigiria `runnerConfig` fora do caminho suportado pelo Angular). O FS anexa a configuração e o relatório ao PR |
| W4 | `ng build` (configuração de produção) | compila sem erro |
| W5 | `npm audit --audit-level=high` | reprova em vulnerabilidade **alta ou crítica** |

**Release/G6 (quando houver tag):** `scripts/check-version.sh` — `<Version>` do `.csproj` == tag `portal-api-v<versão>` == `GET /health` (ADR-0002 item 5).

2. **Cobertura:** meta inicial **80% de linhas** no código-fonte dos dois apps (calibração com o QA antes do G5, como na DEC-ARQ-0003 item 2; escopo de ramos e funções fica reportado). Não invento outro número.
3. **Evidência:** o autor anexa à TASK-0008/PR o log completo (sem segredos). O **CR reexecuta o mesmo script na box** antes de revisar; divergência ou falha impede a entrada no G4 (mitiga RK-CR1).
4. **Pré-requisitos de ambiente (OPS, TASK-0012):** SDK .NET 10 (`global.json`), Node 24 `^24.15` e Angular CLI instalados; rede para o NuGet Audit e o `npm audit` (sem rede, A1/W5 não valem como evidência).
5. Sem pipeline remota e sem serviço pago. Com GitHub/CI, esta DEC é revista.

## Alternativas
- Cobertura nativa do Microsoft Testing Platform (`dotnet test --coverage`, exige configuração no `global.json` do SDK 10): válida (https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-code-coverage), mas o limiar de linhas do Coverlet é documentado e direto; reavaliar se o projeto migrar para o modo MTP.
- Esperar CI real: rejeitada. Aceitar só a declaração do autor: rejeitada (RK-CR1).

## O que muda em relação à DEC-ARQ-0003
Mesma estrutura e mesmos critérios (instalação reproduzível, lint, testes com 80% de linhas, varredura de vulnerabilidade alta/crítica, evidência + reexecução pelo CR). Muda o conjunto de ferramentas (Node `--test`/ESLint/npm audit únicos → dotnet + ng) e entra a reprovação por auditoria que não executou.

## Revisão v1.1 (26/11/2026)
Esclarecimentos pedidos pela QA, sem mudar a decisão de fundo (verify-local, 80% de linhas, SCA alta/crítica):
- A5: critério de falha por **parse do JSON** oficial (`--format json --output-version 1`); o código de saída **não** é o oráculo de vulnerabilidade.
- W3: pacote e opção de limiar fechados com fonte oficial (`@vitest/coverage-v8`, MIT; `coverageThresholds.lines = 80`).
