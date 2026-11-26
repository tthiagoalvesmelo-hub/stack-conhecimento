---
id: INST-TECNOLOGIAS
titulo: "Stack tecnológica homologada"
tipo: institucional
versao: 1.1
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: "Thiago Melo — AH-0003"
criado_em: 2026-11-26T11:00-03:00
atualizado_em: 2026-11-26T15:03-03:00
revisar_ate: 2027-02-26
relacionados: [AH-0003, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-CPO-0001, RM-0002, DEM-2026-001]
substitui: null
substituido_por: null
---

# Stack tecnológica homologada

**Status: VIGENTE (v1.1) para as camadas marcadas "Vigente".** Base: **AH-0003** (Thiago Melo, 26/11/2026 14:54, "Aprovo AH-0003", sem condições). Camadas "A CONFIRMAR" **não** têm tecnologia assumida: nenhum agente a presume. Em fase de testes internos (não é produção).

## Diretriz (AH-0003)
- **Toda demanda de backend que envolva API do Portal Web:** C#/.NET (versão LTS vigente), ASP.NET Core.
- **Toda demanda que envolva o front-end do Portal Web:** Angular (versão estável mais recente).
- Todo o time envolvido se capacita nestas tecnologias (RM-0002, DEC-CPO-0001: custo zero).
- A AH-0001 (Node.js 24 + Fastify 5 + Portal estático) está **substituída** (nada foi implementado em Node).

## Stack por camada
| Camada | Tecnologia | Versão (consulta em 26/11/2026) | ADR | Status |
|---|---|---|---|---|
| Aplicativo Mobile | Java (plataforma-alvo e versão mínima a confirmar) | — | — | Parcial |
| Backend / APIs do **Portal Web** | C# em **.NET 10 (LTS)**, ASP.NET Core Minimal APIs | .NET 10; patch 10.0.15 em 10/11/2026; suporte até 14/11/2028 | ADR-0001 v2 | **Vigente** |
| Backend / APIs e microsserviços **fora** do Portal Web | A CONFIRMAR (a AH-0003 cobre só demandas que envolvam a API do Portal Web) | — | — | Pendente |
| **Portal Web** (front-end) | **Angular** + TypeScript | Angular **22.3.0** (estável mais recente; major 22: Active até 06/2027, LTS até 06/2028); TypeScript `>=6.0 <6.1` | ADR-0001 v2 | **Vigente** |
| Ferramenta de build do Portal | Node.js (só tooling; não é runtime da API) + npm | `^24.15` (Angular 22.3 exige `^22.22.3 \|\| ^24.15.0 \|\| >=26.0.0`); box: 24.22.1 | ADR-0001 v2 | **Vigente** |
| Testes da API | xUnit.net 2.9.3, Microsoft.NET.Test.Sdk 18.12.0, Microsoft.AspNetCore.Mvc.Testing 10.0.x, coverlet.msbuild 10.1.1 (80% de linhas) | séries conferidas em NuGet (26/11/2026); exatas em `packages.lock.json` | ADR-0001 v2; DEC-ARQ-0007 | **Vigente** |
| Testes do Portal | `ng test` (Vitest + jsdom, padrão do Angular CLI) | conforme Angular CLI 22.x | ADR-0001 v2; DEC-ARQ-0007 | **Vigente** |
| Lint / análise estática | Analyzers do SDK .NET + `dotnet format --verify-no-changes`; `angular-eslint` (via `ng add`; 22.8.0, MIT) | — | DEC-ARQ-0008 | **Vigente** |
| SCA / varredura | NuGet Audit (`dotnet list package --vulnerable --include-transitive`); `npm audit` | — | DEC-ARQ-0009 | **Vigente** |
| Bancos de dados | A CONFIRMAR (nenhum na DEM-2026-001) | — | ADR-0001 v2 D5 | Pendente |
| Mensageria / eventos | A CONFIRMAR | — | — | Pendente |
| Nuvem / hospedagem / containers | A CONFIRMAR (fora da fase de testes) | — | ADR-0001 v2 D5 | Pendente |
| CI/CD | A CONFIRMAR (substituto local: `verify-local`, DEC-ARQ-0007) | — | DEC-ARQ-0007 | Pendente |
| Observabilidade | Logs estruturados (`ILogger`); resto a CONFIRMAR | — | ADR-0001 v2 | Parcial |
| Autenticação / autorização | A CONFIRMAR (fora da DEM-2026-001) | — | — | Pendente |

## Fontes oficiais (verificadas em 26/11/2026, 14:51–15:03, America/São Paulo)
- .NET: https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core (política, "Last updated: November 10, 2026"); https://learn.microsoft.com/en-us/dotnet/core/releases-and-support. .NET 11 é STS (suporte até 14/11/2028); .NET 8 e 9 sem suporte desde 10/11/2026.
- Angular: https://angular.dev/reference/releases; registro npm `@angular/core` (22.3.0, 18/11/2026) e `@angular/cli` (engines de Node); testes: https://angular.dev/guide/testing; lint: https://angular.dev/cli/lint.
- Ferramentas: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format; https://learn.microsoft.com/en-us/nuget/concepts/auditing-packages; https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-code-coverage.

## Regras de manutenção
- Atualizar este documento a cada troca de major do .NET ou do Angular, ou quando uma versão sair de suporte (próximos marcos: Angular 20 LTS termina em 28/11/2026, sem uso na Stack; .NET 10 em 14/11/2028).
- Mudança de linguagem/framework fora da AH-0003, ou qualquer custo, exige nova AH.
- Mudança de tecnologia só por ADR (ADR aceito é imutável: novo ADR substitui).
