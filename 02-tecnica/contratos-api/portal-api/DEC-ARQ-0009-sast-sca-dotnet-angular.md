---
id: DEC-ARQ-0009
titulo: "Recorte de SAST/SCA para .NET + Angular (TASK-0010)"
tipo: dec
versao: 1.1
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:03-03:00
atualizado_em: 2026-11-26T15:23-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, TASK-0008, TASK-0009, AH-0003, ADR-0001, DEC-ARQ-0007, DEC-ARQ-0008]
substitui: DEC-ARQ-0005
substituido_por: null
---

# DEC-ARQ-0009 — Recorte de SAST/SCA (substitui DEC-ARQ-0005)

> [TESTE] Não é N3 (sem custo, sem produção, sem framework novo além da diretriz AH-0003). Consultas sem instalar nada, em 26/11/2026.

## Decisão
A varredura exigida pela matriz R3 / G5 fica **explicitamente recortada** em:
1. **SCA da API:** NuGet Audit no restore (`NuGetAuditLevel=high`, `NuGetAuditMode=all`, NU1903/NU1904 como erro; NU1900 também reprova) + `dotnet list package --vulnerable --include-transitive --format json --output-version 1` (DEC-ARQ-0007 A1/A5). A reprovação do A5 é pelo **parse do JSON** (severidade High/Critical); o código de saída do `dotnet list`/`dotnet package list` **não** é o oráculo (documentação oficial não o define como falha; ver DEC-ARQ-0007 v1.1).
2. **SCA do Portal:** `npm audit --audit-level=high` (DEC-ARQ-0007 W5).
3. **Análise estática de segurança da API:** analyzers de segurança **do SDK** habilitados com `AnalysisModeSecurity=All` em `Directory.Build.props` (propriedade por categoria documentada em https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props), com avisos como erro. Sem pacote adicional.
4. **Análise estática do Portal:** `angular-eslint` *recommended* (DEC-ARQ-0008) — não é SAST de segurança; limite declarado.
5. **Testes dirigidos de segurança** do QA na TASK-0010 (RN-0001, REQ-0004, CA-05/CA-06, denylist de cabeçalhos/corpo, tentativa de forçar 503/500 por canais proibidos, corpo do 500 sem detalhe com `ASPNETCORE_ENVIRONMENT=Development`).

O PQ avalia a varredura **neste recorte**. Exceção a vulnerabilidade alta/crítica ou a este recorte exige AH de segurança.

## O que não adoto agora
- **Semgrep OSS, SonarQube, plugins de terceiros** e qualquer ferramenta de SAST externa: ferramenta nova, instalação/operação pelo OPS, desproporcional a um health-check local. Se o resíduo precisar ser reaberto, será **nova DEC**.
- `eslint-plugin-security` (avaliado na DEC-ARQ-0005): continua não adotado (sem `peerDependencies` declaradas; relevância baixa para um Portal Angular de uma tela).

## O que muda em relação à DEC-ARQ-0005
`npm audit` + ESLint recommended (API em Node) → NuGet Audit + analyzers de segurança do SDK (API) e `npm audit` + `angular-eslint` (Portal). Os testes dirigidos do QA permanecem.

## Revisão v1.1 (26/11/2026)
Esclarece o critério de falha do A5 (parse JSON; NuGet Audit no restore permanece a barreira principal). Sem mudança do recorte de SAST/SCA.
