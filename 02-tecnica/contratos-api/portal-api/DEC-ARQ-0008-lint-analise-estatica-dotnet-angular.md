---
id: DEC-ARQ-0008
titulo: "Lint e análise estática de C#/.NET e Angular (L-CR3)"
tipo: dec
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:03-03:00
atualizado_em: 2026-11-26T15:03-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0008, TASK-0009, AH-0003, ADR-0001, DEC-ARQ-0007, DEC-ARQ-0009, L-CR3]
substitui: DEC-ARQ-0004
substituido_por: null
---

# DEC-ARQ-0008 — Lint e análise estática (substitui DEC-ARQ-0004)

> [TESTE] Sem custo de licença (todas as ferramentas são gratuitas). Consultas ao NuGet, ao npm e à documentação oficial em 26/11/2026, **sem instalar nada**. Não é N3. Bloqueia a entrada no G4 via DEC-ARQ-0007.

## Decisão
**API (C#):** ferramentas **do próprio SDK**, sem pacote adicional:
- `Directory.Build.props`: `Nullable=enable`, `TreatWarningsAsErrors=true`, `EnableNETAnalyzers=true`, `EnforceCodeStyleInBuild=true`, `AnalysisLevel=10-recommended` (valor composto *versão-modo*; documentado em https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props), com `.editorconfig` versionado definindo a severidade das regras de estilo.
- `dotnet format --verify-no-changes` (aplica o `.editorconfig`; falha se houver diferença; https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format). Passo A2 do `verify-local`.
- Analyzers do pacote `xunit` (`xunit.analyzers`) já vêm como dependência do xUnit 2.9.3 (nuspec).

**Portal (Angular):** `ng lint` **exige adicionar um pacote** (`ng add`) que implemente o builder; adoto **`angular-eslint`** (22.8.0, MIT; builder `@angular-eslint/builder:lint`; peers: `eslint ^9 || ^10`, `typescript-eslint ^8`; fontes: https://angular.dev/cli/lint e registro npm, 26/11/2026). É devDependency (lockfile, `npm ci`), regras *recommended* do pacote, **zero avisos** (opção do builder a confirmar pelo FS). Passo W2 do `verify-local`. A compatibilidade exata de `angular-eslint` 22.8.0 com o ESLint e o TypeScript 6.0 fixados pelo `ng add` é conferida pelo FS na criação do workspace; falha de compatibilidade volta ao ARQ (não improvisar).

**Fora:** formatador do Portal (Prettier etc.) não é porta do G4; análise de segurança: DEC-ARQ-0009.

## Condições
- Não adoto analyzers de terceiros pagos nem SonarQube/Semgrep (instalação e operação desproporcionais; ferramenta nova exige avaliação do ARQ).
- Versões exatas ficam nos lockfiles, não abaixo das séries conferidas.

## O que muda em relação à DEC-ARQ-0004
ESLint/`@eslint/js`/`globals` (JS no Node) deixam de valer; passam a valer analyzers do SDK + `dotnet format` (API) e `angular-eslint` (Portal).
