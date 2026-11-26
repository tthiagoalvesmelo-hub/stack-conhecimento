---
id: ARQ-ANALISE-DEM-2026-001-AH-0003
titulo: "Análise de impacto da troca de stack (AH-0003): ADR, contrato, ET, DEC, CA e horas"
tipo: parecer
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:03-03:00
atualizado_em: 2026-11-26T15:03-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, TASK-0007, AH-0003, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, ET-0001, US-0001, US-0002]
substitui: null
substituido_por: null
---

# Análise de impacto da troca de stack (AH-0003)

> [TESTE] Insumo do ARQ para o AS (ET-0001), o PO (CA, plano G2) e o ORQ. **O ARQ não edita artefatos do AS nem decide se o G2 se mantém (PO).** Base: ADR-0001 v2 (aceito), ADR-0002/0003 v1.1 (propostos), DEC-ARQ-0007..0010.

## 1. ADR-0002 e ADR-0003
| ADR | Muda? | O que muda | O que NÃO muda |
|---|---|---|---|
| **ADR-0002** (v1.0 → v1.1, proposto) | **Sim, só a origem** | Fonte única: `<Version>` no `.csproj` do `portal-api` (e não `package.json`); `IncludeSourceRevisionInInformationalVersion=false` obrigatório (o SDK .NET anexa `+commit` por padrão); leitura de `AssemblyInformationalVersion` na inicialização; script lê o XML do `.csproj` | SemVer 2.0.0, sem build metadata, regra de incremento, tag `portal-api-v<versão>`, rastreabilidade tripla (manifesto = tag = `/health`), ser a versão do `portal-api` |
| **ADR-0003** (v1.0 → v1.1, proposto) | **Não nas decisões de contrato** | Apenas alinhamento editorial: `Allow: GET, HEAD` (já decidido na DEC-ARQ-0002 L-02); CSP passa a ser requisito da hospedagem de produção do Portal Angular (ADR futuro; nos testes o Portal roda em `ng serve`); referências à stack | 200/503/405/500, `no-store`, `nosniff`, CORS, formatos de `status/version/timestamp`, problem+json, contrato interno sem autenticação |
Aceite de ambos: no G3 (TASK-0007).

## 2. OpenAPI 1.0.0 (cf660fb) — conclusão do ARQ: **MANTÉM-SE em 1.0.0, sem alteração semântica**
**Fundamentos:**
1. O contrato descreve comportamento HTTP (caminho, métodos, status, cabeçalhos, esquemas, exemplos, padrões de `version`/`timestamp`/UUID). Nada disso depende de runtime. As expressões regulares são ECMA-262 e a validação independente do ARQ (`validar-g3-openapi.py`, ~90 verificações, OpenAPI 3.1 válido, exemplos válidos, `additionalProperties: false`) e os testes de padrão em Node 24 independem da stack.
2. A dependência de stack está **isolada em prosa** marcada "premissa a confirmar (AH-0001)" (ET-0001 §PS; openapi.yaml linhas 9, 32, 90, 281) e já era declarada pelo AS como "nada altera o contrato".
3. O que o ASP.NET Core faz por padrão e **conflita** com o contrato é **risco de implementação**, não mudança de contrato: ProblemDetails com `type` URL e `traceId`; `+commit` na versão; `DateTime` com até 7 casas; cabeçalho `Server`; ausência de gancho de 503 no encerramento por padrão. Tudo isso é obrigação de conformidade no ADR-0001 v2 D8 e deve ser coberto por teste de contrato (G4/G5).
4. `info.version` não se altera (mudança editorial, contrato ainda não aprovado nem publicado).

**Ressalva editorial (AS, sem mudar `info.version`):** atualizar o texto do cabeçalho (linhas 7–9: fontes ADR v1.0 propostos, "aguarda AH-0001"), as linhas 32, 90 e 281 ("premissa a confirmar (AH-0001)" → remissão ao ADR-0001 v2 D8) e `x-stack`/`adr` (ADR-0001 v2 aceito; ADR-0002/0003 v1.1). **Cuidado do AS:** nos testes de padrão em .NET, `$` aceita `\n` final; a expressão do contrato está correta e rejeita a quebra de linha em ECMA-262 (verificado em Node 24).

## 3. ET-0001 v1.3 e EF-0001 — seções que o AS precisa revisar (o ARQ não edita)
O comportamento normativo (RT, CE, L-01..L-07, DEC-AS-0001..0003) **se mantém**. Revisar a premissa de stack:
| Onde (ET-0001 v1.3) | Revisão |
|---|---|
| Frontmatter `relacionados` e §Fora de escopo (linha ~30), §Dependências (linha ~37: ADR-0001 "1.0 · proposto · aguarda AH-0001") | ADR-0001 **2.0 aceito (AH-0003)**; ADR-0002/0003 v1.1 propostos |
| **Tabela PS-01..PS-09** (linhas ~51–63) e o título "Stack proposta no ADR-0001: Node.js 24 + Fastify 5, Portal estático" | Reescrever contra o ADR-0001 v2: PS-01 ASP.NET Core Minimal APIs/Kestrel, host/porta por `PORTAL_API_HOST/PORT`; **PS-02** `<Version>` do `.csproj` + `IncludeSourceRevisionInInformationalVersion=false`; PS-03 middleware CORS embutido; PS-04 remoção do `Server` (a verificar); PS-05 janela de drenagem no encerramento (a verificar); PS-06 ProblemDetails customizado; PS-07 `TimeProvider`, UUID v4, `WebApplicationFactory<Program>`; PS-08 DEC-ARQ-0010; PS-09 biblioteca de validação de esquema (aprovação do ARQ) |
| §7.2 e §7.4 (gancho de 503 e de 500; linhas ~159–162, ~183–186, ~246), CE-02 (~201), L-05/L-12 (~256, ~263) | "fábrica da aplicação/de teste" → `WebApplicationFactory<Program>` com `ConfigureTestServices`; manter as proibições. L-12 será **formalizada na DEC-ARQ-0011 (G3)** |
| §Infraestrutura (~224) | ADR-0001 v2 D5/D7; SDK .NET 10 e Angular CLI (TASK-0012) |
| L-10 (~262, "Dependência: AH-0001") | Fechada: AH-0001 substituída pela AH-0003 |
| Histórico de versões | Nova versão (1.4) pelo AS |
| EF-0001 (L-10, linha ~112) | Remover a dependência da AH-0001 |
O prazo desta revisão é do AS. **Recomendação do ARQ ao ORQ:** liberar a TASK-0008 somente após a ET-0001 v1.4 (ver parecer G3).

## 4. DEC-ARQ-0003/0004/0005/0006 → substituídas
| Antes | Depois | Mudança |
|---|---|---|
| 0003 verify-local (npm ci, ESLint, `node --test`, `npm audit`) | **0007** | dotnet restore `--locked-mode` + NuGet Audit; `dotnet format --verify-no-changes`; `dotnet build -warnaserror`; `dotnet test` + Coverlet ≥80% linhas; `dotnet list package --vulnerable`; Portal: `npm ci`, `ng lint`, `ng test --coverage` ≥80%, `ng build`, `npm audit` |
| 0004 lint (ESLint 10) | **0008** | analyzers do SDK + `dotnet format` (API); `angular-eslint` (Portal) |
| 0005 SAST (npm audit + ESLint) | **0009** | NuGet Audit + `AnalysisModeSecurity=All` (API); `npm audit` + `angular-eslint` (Portal); testes dirigidos do QA |
| 0006 p95 (Node `fetch`) | **0010** | mesmo método e parâmetros; API em Release; Node continua como ferramenta |
DEC-ARQ-0001 (R3) e DEC-ARQ-0002 (L-01..L-07, comportamento) **permanecem**.

## 5. Plano de QA (insumo ao QA; parecer de qualidade é do QA)
- O plano da TASK-0010 previa `node:test` com `fetch` mockado e CT manual no Chromium para os CA dependentes de DOM. No Angular, `ng test` traz Vitest + jsdom por padrão: a simulação de DOM deixa de ser dependência nova. **O QA reavalia** quais CA do US-0002 ficam automatizados e quais continuam em CT manual.
- API: xUnit + `WebApplicationFactory` (testes de integração sem rede), Coverlet 80% de linhas no limiar de entrada do G4 (ramos reportados), calibração no G5 mantida.
- Itens PV do ADR-0001 v2 D8 viram casos de teste obrigatórios (ProblemDetails em 404/405/500, timestamp com 3 casas, versão sem `+`, cabeçalhos em todas as respostas, 500 sem detalhe em `Development`).

## 6. CA: o que muda (insumo ao PO; a decisão sobre G2 e reabertura é do PO)
**Refutação parcial da leitura do PO sobre o CA-04 da US-0001:** o **texto do CA-04 não precisa mudar**. Ele já fala em "manifesto do serviço" e "tag de release", sem citar `package.json`, e a estrutura do oráculo (resposta == manifesto == tag) é a mesma no ADR-0002 v1.1. O que muda é o **arquivo do manifesto** (`<Version>` do `.csproj`) e a **premissa de formato** da US-0001 (linha ~40: "Origem (manifesto `package.json`) depende da aceitação do ADR-0001 / AH-0001"), além da nota do QA. **Se o PO considerar que o oráculo escrito com `package.json` nos documentos do QA exige reabertura, isso é decisão dele**; o ARQ apenas confirma que não há mudança de comportamento verificável.

| CA | Comportamento muda? | Texto a ajustar (se algum) | Condição |
|---|---|---|---|
| US-0001 CA-01, 02, 03, 05, 06, 08 | Não | Nenhum | CA-05/CA-03 passam a depender da conformidade D8 itens 2–3 (testes) |
| **US-0001 CA-04** | **Não** | Nenhum no CA; ajustar a premissa de formato (linha ~40) | Oráculo: `<Version>` do `.csproj` == tag == `/health` |
| US-0001 CA-07 (503 no encerramento) | Não | Nenhum | **Condicionado ao protótipo** do encerramento gracioso (D8 item 10). Se o protótipo mostrar que não é viável em ASP.NET Core, o CA-07/RN-0002 voltam ao PO por MSG-COL; **até agora, não há indício de inviabilidade** (a verificar) |
| US-0001 CA-09 (500) | Não | Nenhum | Gancho de teste via `WebApplicationFactory` (L-12, G3); 500 sem detalhe em qualquer ambiente |
| US-0002 CA-01, 03, 06 | Não | Nenhum | CA-06: interpolação do Angular trata valores como texto (a confirmar em teste) |
| US-0002 CA-02, 04, 05 | Não | Nenhum | Muda o **método de verificação** (QA), não o CA |
| Spec UX (UX-0001 v1.1, protótipo HTML) | Não | Mapeamento para componentes Angular (UX/FS) | — |
**Conclusão para o PO:** nenhum CA muda de comportamento. Texto: apenas a premissa de formato da US-0001 (stack). Reabertura formal é decisão do PO.

## 7. Horas (estimativas do ARQ, ex-ante; premissas abaixo)
| Item | Antes (Node, alt. A) | Agora (.NET + Angular) | Premissas |
|---|---|---|---|
| Residual da TASK-0003 | 1–3 h | **6–10 h** (ADR v2, tecnologias.md, ADR-0002/0003, 4 DEC, análise, MSG-RET); **resta ≈0,5–1 h** após esta entrega (ajustes de revisão) | Escopo entregue nesta MSG-RET; sem custo; sem spike com SDK |
| TASK-0007 (G3) | 2–4 h | **3–6 h** (inclui DEC-ARQ-0011 e mapeamento ASP.NET Core) | ET v1.4 do AS disponível; sem o AS, o G3 sai com ressalva |
| 2ª aprovação no G4 | 1–2 h | **1,5–3 h** (+1 h se houver 2º ciclo) | Stack nova exige leitura mais atenta; spike dos itens PV já feito pelo FS |
| Capacitação do ARQ (RM-0002) | — | 14–20 h | Fora da DEM-2026-001 |
**Outros papéis reestimam** (os 78 h do plano G2 eram em Node): FS (curva de aprendizado e 2 toolchains), OPS (instalar SDK .NET 10, Angular CLI, `verify-local`), QA (DOM padrão, Coverlet), CR (revisão de C#/TypeScript), AS (ET v1.4). O total do plano G2 está reaberto; o ARQ não consolida horas dos outros.
