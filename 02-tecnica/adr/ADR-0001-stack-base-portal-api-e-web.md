---
id: ADR-0001
titulo: "Stack base, estrutura do projeto e convenções do Portal Web e da API base: C#/.NET e Angular (DEM-2026-001)"
tipo: adr
versao: 2.0
status: aceito
dono: ARQ
autores: [ARQ]
aprovado_por: "Thiago Melo — AH-0003 (diretriz N3, 26/11/2026 14:54, \"Aprovo AH-0003\"); aceite técnico: ARQ (26/11/2026)"
criado_em: 2026-11-26T12:20-03:00
atualizado_em: 2026-11-26T15:03-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, AH-0003, AH-0001, ADR-0002, ADR-0003, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-CPO-0001, RM-0002, US-0001, US-0002, REQ-0001, REQ-0004, RN-0001, INST-TECNOLOGIAS]
substitui: null
substituido_por: null
---

# ADR-0001 — Stack base, estrutura do projeto e convenções (Portal Web e API base): C#/.NET e Angular

> [TESTE] Fase de testes internos; nada vai à produção. **Status: ACEITO (v2.0)**, com base na **AH-0003** (Thiago Melo, 26/11/2026 14:54, texto literal "Aprovo AH-0003", sem condições; registrada pelo ORQ em c15d4f0). A partir deste aceite o ADR é imutável: mudança = novo ADR com `substitui: ADR-0001`.

## Histórico de versões e tratamento no protocolo
| Versão | Conteúdo | Status | Observação |
|---|---|---|---|
| 1.0 (commit 362ea35) | Node.js 24 + Fastify 5 + Portal estático JS | **Proposto, nunca aceito**; a AH-0001 (26/11 14:45) o aprovou como stack, mas a diretriz seguinte (AH-0003) a **substituiu** antes de qualquer código | Nada foi implementado em Node (sem repositório, sem esqueleto, sem runtime instalado pelo OPS). Texto preservado no histórico do git |
| **2.0 (este)** | C#/.NET LTS (ASP.NET Core) + Angular | **Aceito** | Base: AH-0003 |

**Por que revisão na própria numeração (v2.0) e não um ADR novo com `substitui`:** (i) a regra de imutabilidade (EL-02; modelo de ADR) vale **após "Aceito"**, e a v1.0 nunca foi aceita; (ii) a AH-0003 e o ORQ pedem "ADR-0001 refeito"; (iii) o ID ADR-0001 é referenciado por ET-0001, openapi.yaml (`x-stack`), contexto.yaml e AH; manter o ID evita ponteiros órfãos; (iv) o rastro da v1.0 e da AH-0001 fica neste quadro e no git (362ea35). Se o ORQ preferir o formato "substitui", a alternativa é criar um ADR novo (ID a reservar) marcando a v1.0 como Rejeitada; o conteúdo abaixo não muda.

## Contexto
- Demanda DEM-2026-001 [TESTE] (Fluxo 01, responsável PO; R3 por DEC-ARQ-0001): `GET /health` na API base do Portal Web e tela de status. Projeto do zero; TASK-0003 (ARQ) reaberta pela AH-0003.
- **Diretriz do Thiago (AH-0003):** APIs de backend do Portal Web em **C#/.NET (versão LTS vigente)**; front-end do Portal Web em **Angular (versão estável mais recente)**; capacitação do time (RM-0002, DEC-CPO-0001: custo zero, prioridade Alta).
- Restrições mantidas: custo zero de licença e de infraestrutura; execução local no computador compartilhado (sem GitHub, CI ou ambientes dev/hml); Portal e API independentes; segurança/LGPD desde a concepção; reversibilidade.
- **Ambiente verificado em 26/11/2026 (box):** Node.js v24.22.1, npm 11.21.1; **.NET SDK não instalado** (`dotnet: command not found`; instalação é do OPS, TASK-0012); Angular CLI não instalado. Nada foi instalado por este ADR.
- **Versões confirmadas em fonte oficial (consulta em 26/11/2026, 14:51–15:03, America/São Paulo):**

| Item | Resultado | Fonte |
|---|---|---|
| .NET LTS vigente | **.NET 10 (LTS)**, lançado em 11/11/2025; último patch **10.0.15** (10/11/2026); suporte até **14/11/2028** | https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core ("Last updated: November 10, 2026"); https://learn.microsoft.com/en-us/dotnet/core/releases-and-support |
| .NET mais novo | .NET 11 (**STS**), lançado em 10/11/2026; suporte também até 14/11/2028. .NET 8 e 9 sem suporte desde 10/11/2026 | mesma política |
| Angular estável mais recente | **22.3.0** (npm `latest`, 18/11/2026). Major 22 lançada em 03/06/2026, Active até 06/2027, LTS até 06/2028. v21: LTS até 06/2027; v20: LTS termina em 28/11/2026 | https://angular.dev/reference/releases; registro npm `@angular/core` |
| Node exigido pelo Angular 22.3 | `^22.22.3 \|\| ^24.15.0 \|\| >=26.0.0` (a box, 24.22.1, atende) | registro npm (`@angular/cli` 22.3.0) |
| TypeScript exigido | `>=6.0 <6.1` (peer do `@angular/compiler-cli` 22.3.0) | registro npm |
| Teste padrão do Angular | Vitest + jsdom | https://angular.dev/guide/testing |
| Lint no Angular | `ng lint` exige adicionar um pacote (`ng add`); builder `@angular-eslint/builder:lint`. `angular-eslint` 22.8.0, MIT, peers `eslint ^9 \|\| ^10`, `typescript-eslint ^8` | https://angular.dev/cli/lint; registro npm |
| `dotnet format` | Aplica `.editorconfig`; `--verify-no-changes` falha se houver diferença | https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format |
| Cobertura (.NET) | Coverlet (`coverlet.msbuild` 10.1.1, MIT; `Threshold`, `ThresholdType=line`, `ThresholdStat`) ou `Microsoft.Testing.Extensions.CodeCoverage` | https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-code-coverage; https://github.com/coverlet-coverage/coverlet (Documentation/MSBuildIntegration.md); NuGet |
| SCA (.NET) | NuGet Audit no `restore` e `dotnet list package --vulnerable --include-transitive` | https://learn.microsoft.com/en-us/nuget/concepts/auditing-packages |

## Decisão
**D1 — Runtime e linguagem da API:** C# em **.NET 10 LTS** (TFM `net10.0`, ASP.NET Core 10). `global.json` fixa a série do SDK 10.0.x; instalação e política de roll-forward: OPS. **.NET 11 (STS) não é adotado**: tem o mesmo fim de suporte (14/11/2028) que o 10 LTS, foi lançado há 16 dias e a diretriz pede LTS. Troca de major do .NET é atualização tecnológica futura (R3 pela regra de major de runtime), por novo ADR.

**D2 — API base (`portal-api`):** serviço HTTP/JSON em **ASP.NET Core Minimal APIs**. Escolha interna da alçada do ARQ (não desvia da diretriz, custo zero): menor superfície que controllers para um endpoint; o tutorial oficial a descreve como feita para APIs HTTP com dependências mínimas (https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api). **Zero pacote NuGet de terceiros em runtime**: CORS, ProblemDetails, DI, logging (`ILogger`) e `TimeProvider` vêm do framework. `Nullable` habilitado e avisos tratados como erro. Estrutura do código em D6.

**D3 — Portal Web (`portal-web`):** **Angular 22.x** (estável mais recente na data: 22.3.0) com TypeScript `>=6.0 <6.1`, criado pelo Angular CLI (`ng new`) com os padrões do CLI. Node 24 (`^24.15`) é só **ferramenta de build/teste** (não é runtime da API). Na fase de testes, o Portal roda no servidor de desenvolvimento (`ng serve`, interface de loopback), **processo separado da API** (consumidor e provedor independentes; o Portal não é servido pela API). `ng build` (produção) entra na verificação local para garantir que compila. **Fora**: SSR/prerender e biblioteca de componentes de UI (adoção só por novo ADR; evita dependências para uma tela). Hospedagem de produção e CSP do servidor estático: ADR próprio quando houver implantação.

**D4 — Testes e qualidade:**
- **API:** xUnit.net (`xunit` 2.9.3, Apache-2.0) + `Microsoft.NET.Test.Sdk` (18.12.0) + `Microsoft.AspNetCore.Mvc.Testing` (série 10.0.x, MIT) para `WebApplicationFactory<Program>`; `coverlet.msbuild` (10.1.1, MIT) com limiar de **80% de linhas**. xUnit v3 (4.0.3) não adotado agora (reavaliar). Versões exatas em `packages.lock.json`.
- **Web:** `ng test` (Vitest + jsdom, padrão do CLI); `ng lint` com `angular-eslint` (via `ng add`).
- Detalhes (comandos, limiares, SCA, SAST, p95): **DEC-ARQ-0007 a 0010**. Teste de contrato contra o esquema do OpenAPI: a escolha da biblioteca de validação de esquema (PS-09) passa pelo ARQ antes de qualquer dependência nova.

**D5 — Fora desta fase (decisão explícita de NÃO adotar):** banco, mensageria, containers, nuvem, CI/CD, autenticação, observabilidade além de logs estruturados, SSR e biblioteca de UI. Qualquer item exige ADR/demanda; qualquer custo exige AH própria.

**D6 — Repositório e estrutura (criados por FS/OPS após esta decisão; o ARQ não cria código nem esqueleto):**
```
/workspace/projetos/portal/                  # repositório Git local (monorepo de teste; sem remoto)
├── README.md  .gitignore  .editorconfig  global.json
├── apps/
│   ├── portal-api/
│   │   ├── Directory.Build.props            # Nullable, TreatWarningsAsErrors, analyzers, lockfile de pacotes,
│   │   │                                    # IncludeSourceRevisionInInformationalVersion=false (ADR-0002)
│   │   ├── PortalApi.sln (ou .slnx)
│   │   ├── src/Portal.Api/                  # Portal.Api.csproj com <Version> = fonte única (ADR-0002)
│   │   │   ├── Program.cs                   # composição (root): pipeline e DI; sem ganchos de falha
│   │   │   ├── Configuration/  Health/  Http/ (middlewares, problem details, cabeçalhos)
│   │   └── tests/Portal.Api.Tests/          # Unit, Integration (WebApplicationFactory), Contract
│   └── portal-web/                          # workspace Angular (package.json, package-lock.json, angular.json, src/app/...)
├── scripts/                                 # verify-local.sh, check-version.sh, measure-p95 (DEC-ARQ-0007/0010)
└── docs/README.md                           # SOMENTE ponteiros para o stack-conhecimento
```
Regras: um projeto por responsabilidade; **sem código compartilhado entre `portal-api` e `portal-web`**; cada app com manifesto, testes e versão próprios; contrato OpenAPI no stack-conhecimento (fonte única); mocks do Portal derivados dele (PR-04). Git: `main` sem commits diretos (convenção), ramos `feat|fix|chore/TASK-nnnn-descricao`, commits citando IDs com trailer `Agente: <sigla>`, tags `portal-api-v<versão>` (ADR-0002).

**D7 — Configuração (somente NOMES; valores fora do repositório, sem segredos):** `PORTAL_API_HOST` (padrão 127.0.0.1), `PORTAL_API_PORT`, `PORTAL_API_ALLOWED_ORIGIN` (obrigatória; fail closed), `LOG_LEVEL` (API); `PORTAL_WEB_PORT`, `PORTAL_API_BASE_URL` (Portal; a forma de injetar a URL no build/execução do Angular é do FS). **Nenhum comportamento do contrato pode depender de `ASPNETCORE_ENVIRONMENT`** (ver D8, itens 9 e 11).

**D8 — Diretrizes de conformidade do contrato em ASP.NET Core (obrigações de implementação; o contrato OpenAPI não muda).** Coluna **Fonte**: **V** = confirmado em documentação oficial lida; **PV** = *a verificar* no primeiro spike/teste (não afirmado como fato).

| # | Tema | Obrigação | Fonte |
|---|---|---|---|
| 1 | Versão | `<Version>` no `.csproj`; `IncludeSourceRevisionInInformationalVersion=false`, pois o SDK (.NET 8+, com Source Link) anexa `+<commit>` por padrão; leitura única de `AssemblyInformationalVersion`, validação pela expressão do ADR-0002, falha ⇒ não inicia | V (msbuild-props) |
| 2 | Erros | O ProblemDetails padrão usa `type` com URL (RFC 9110) e inclui `traceId`; o contrato exige `type: about:blank`, só `type/title/status` (DEC-ARQ-0002 L-01) ⇒ `CustomizeProblemDetails`/tratador próprio; cobrir também 404/405 gerados pelo roteamento | V (error-handling); cobertura de 404/405: PV |
| 3 | `timestamp` | `TimeProvider`, formato fixo `yyyy-MM-dd'T'HH:mm:ss.fff'Z'` (cultura invariante); não depender da serialização padrão de `DateTime`, que pode emitir até 7 casas | PV |
| 4 | Corpo/`Content-Type` | DTO com exatamente `status`, `version`, `timestamp`; `application/json; charset=utf-8` | PV |
| 5 | Métodos | Mapear `GET` e `HEAD` explicitamente; 405 com `Allow: GET, HEAD` e corpo problem+json; `OPTIONS` ⇒ 204 só no preflight (L-02) | PV |
| 6 | Cabeçalhos | `Cache-Control: no-store` e `X-Content-Type-Options: nosniff` em **toda** resposta (inclui 404/405/500/preflight; L-04); sem cabeçalho `Server` (opção do Kestrel a confirmar) | PV |
| 7 | `X-Request-Id` | Middleware: UUID canônico válido é devolvido; senão UUID v4 gerado; nunca 400 (L-03) | — |
| 8 | CORS | Middleware CORS embutido (sem pacote); `PORTAL_API_ALLOWED_ORIGIN` exata, sem `*`, ausente/inválida ⇒ não inicia; sem credenciais; métodos GET/HEAD; origem não permitida: sem cabeçalhos ACAO e **sem 403** (L-06) | PV (comportamento do preflight) |
| 9 | 500 | Tratador global ⇒ problem+json sem detalhe; **nunca** página de exceção de desenvolvedor, em **qualquer** ambiente (teste obrigatório com `ASPNETCORE_ENVIRONMENT=Development`) | PV |
| 10 | 503 no encerramento | O listener permanece no ar numa janela de drenagem após o sinal (ex.: `IHostApplicationLifetime.ApplicationStopping`), respondendo 503 sem `Retry-After` (L-05; PS-05). Exige protótipo | PV |
| 11 | Ganchos de teste (503/500; L-05 e L-12) | **Somente** por `WebApplicationFactory<Program>` com `ConfigureTestServices` trocando a abstração de estado/falha de saúde. A composição de produção não registra nenhum gancho. **Proibidos**: endpoint, query, cabeçalho, variável de ambiente, configuração, `FORCE_*` ou `if (env.IsDevelopment())` que force falha | padrão de testes do ASP.NET Core (confirmar na 1ª implementação) |
| 12 | Regex nos testes | `$` em regex do .NET aceita `\n` final (como em Python); usar `\z` (ou verificação equivalente) ao validar `version`/`timestamp`/UUID | PV |
| 13 | Logs | `ILogger` estruturado; `/health` em nível Debug; erros em Error; nada sensível | — |

**D9 — Fronteira da AH-0003 (o que é do ARQ e o que exige nova AH):**
- **Dentro da diretriz, alçada do ARQ (feito neste ADR):** Minimal APIs (vs controllers), xUnit, Coverlet, analyzers do SDK + `dotnet format`, `angular-eslint`, ferramentas padrão do Angular CLI (Vitest/jsdom), `ng serve` nos testes, estrutura do monorepo, versões dentro das séries listadas.
- **Fora da diretriz ⇒ lacuna e pedido de AH (não adotado):** outro framework de backend ou de front-end (p.ex. Blazor, Node/Fastify), qualquer item com custo (licença, curso, serviço, IDE paga), nuvem, banco, autenticação, biblioteca de UI paga. Bibliotecas gratuitas fora da lista exigem avaliação do ARQ caso a caso.

## Alternativas avaliadas
| # | Alternativa | A favor | Contra / trade-off | Veredito |
|---|---|---|---|---|
| A | **.NET 10 LTS + ASP.NET Core Minimal APIs + Angular 22** | É a diretriz AH-0003; LTS com suporte até 14/11/2028; framework compartilhado cobre CORS, ProblemDetails, DI, logs; zero NuGet de terceiros em runtime; Node já presente para o Angular | Duas toolchains (dotnet + Node/npm); SDK não instalado; curva de aprendizado (RM-0002); cadeia npm do Angular (a medir no `npm ls` do projeto gerado) | **Escolhida** |
| B | A com controllers MVC em vez de Minimal APIs | Convenções conhecidas | Mais código e superfície para um endpoint | Não escolhida |
| C | .NET 11 (STS) | Mais novo | Mesmo fim de suporte do 10; diretriz pede LTS; lançado há 16 dias | Não escolhida; reavaliar na troca de major |
| D | Angular 21 (LTS) | Janela de LTS ativa | Diretriz pede a estável mais recente (22.3.0) | Não escolhida |
| E | Manter Node 24 + Fastify 5 + Portal estático (v1.0) | Instalado; menor stack | Contraria a AH-0003 | **Rejeitada** pela AH-0003 (registrada) |
| F | Blazor (C# no front) | Uma linguagem | Contraria a diretriz (Angular) | Fora da diretriz; exigiria AH |
| G | Portal servido pelo mesmo processo da API | Menos um processo | Acopla consumidor e provedor | Rejeitada |

## Justificativa
- Atende literalmente a diretriz aprovada com a menor superfície adicional: Minimal APIs, framework compartilhado, sem biblioteca de terceiros em runtime.
- Mantém independência Portal/API e a decisão reversível (sem código e sem implantação).
- LTS do .NET e estável mais recente do Angular conferidos em fonte oficial, com data.

## Consequências e impactos
- **Portal Web:** primeira tela em Angular; consumo do contrato com tempo limite de 5 s e sem retry (DEC-AS-0001); valores da API exibidos apenas como texto (a interpolação padrão do Angular não insere HTML). Teste de componente com DOM simulado passa a ser padrão do CLI (QA reavalia o plano de DOM da TASK-0010).
- **Mobile (Java):** sem impacto; contrato REST/JSON neutro.
- **Backend/APIs:** nasce o `portal-api` (primeiro serviço .NET). Contrato OpenAPI 1.0.0 mantém-se (conclusão no MSG-RET TASK-0003).
- **Dados/Integrações:** nenhum.
- **Infraestrutura/DevOps:** SDK .NET 10 e Angular CLI a instalar pelo OPS (TASK-0012, refeita); Node 24 permanece como ferramenta; sem container, nuvem ou CI; custo zero.
- **Segurança/LGPD:** nenhum dado pessoal; dependências sob lockfile (`packages.lock.json` e `package-lock.json`), NuGet Audit e `npm audit` (DEC-ARQ-0009).
- **Pessoas:** capacitação RM-0002 (custo zero) — plano do ARQ, prioridade da CPO. A DEM-2026-001 é o primeiro exercício prático e não espera o fim da capacitação.
- **Débitos conhecidos:** ausência de CI; os itens **PV** do D8 só se fecham com código; hospedagem de produção do Portal sem ADR.
- **Plano de reversão:** até a primeira implantação, trocar de stack = descartar `/workspace/projetos/portal/`; depois, só por ADR substituto.

## Classe de risco e nível de autonomia
- Mantém **R3** (DEC-ARQ-0001): primeiro serviço e novo framework. **N3** coberto pela **AH-0003** (arquitetura de alto impacto; aprovada, sem condições, dentro da validade de 24 h). Sem custo e sem contrato público (ADR-0003: interno), logo sem AH adicional de custo ou de segurança.
- Escolhas dos D2/D4/D9 não desviam da diretriz e são da alçada do ARQ; por isso este ADR **não exige nova AH**.

## Lacunas abertas (não bloqueiam o aceite; donos indicados)
1. Itens **PV** do D8 — FS/QA (testes) e ARQ (spike) após a instalação do SDK pelo OPS.
2. Premissas PS-01..PS-09 da ET-0001 — AS (ET v1.4).
3. Forma de injetar `PORTAL_API_BASE_URL` no Angular — FS.
4. Biblioteca de validação de esquema para o teste de contrato (PS-09) — QA/FS, aprovação do ARQ.
5. Escopo da AH-0003 para backends que **não** sejam do Portal Web — fora deste ADR (CPO/ORQ se necessário).

## Status
**Aceito (v2.0)** pelo Arquiteto Líder em 26/11/2026, com base na AH-0003. Proposto → Aceito → Substituído/Rejeitado. ADR aceito é imutável: para mudar, crie novo ADR com `substitui: ADR-0001`.
