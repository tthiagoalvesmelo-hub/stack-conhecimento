---
id: NOTA-ANALISE-DEM-2026-001-TASK-0008
titulo: "Nota de análise (itens 1–9) — TASK-0008: GET /health da portal-api e tela de status (.NET 10 + Angular 22.3)"
tipo: nota-analise
versao: 1.0
status: em-revisao
dono: FS
autores: [FS]
aprovado_por: null
criado_em: 2026-11-26T15:55-03:00
atualizado_em: 2026-11-26T15:55-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0008, TASK-0009, TASK-0010, TASK-0012, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0002, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-ARQ-0011, DEC-PO-0008, DEC-PO-0009, ET-0001, EF-0001, PT-0001, RM-0002, AH-0003, AH-0004]
substitui: null
substituido_por: null
---

# Nota de análise — TASK-0008 · DEM-2026-001 [TESTE] · FS · 26/11/2026 15:55 (America/Sao_Paulo)

> Fase de testes internos; nada vai à produção. Pré-requisito da DoR técnica (PROMPT FS v1.1, §6.1). TASK-0008 liberada pelo ORQ às 15:41 (contexto.yaml v39). Esta nota cobre a **fase 1** (análise + esqueleto D6). A lógica das US-0001/US-0002 **ainda não** foi implementada.

## Fontes consultadas (ID · versão · commit)
ADR-0001 v2.0 aceito (`7abc2b1`, merge `d40518e`) · ADR-0002 v1.1 e ADR-0003 v1.1 aceitos (`7bc37ba`) · DEC-ARQ-0002 v1.0 (`15b3809`) · DEC-ARQ-0007 v1.1, 0009 v1.1, 0011 v1.1 (`ebb5f22`) · DEC-ARQ-0008 v1.0 e 0010 v1.0 (`7fa2b43`) · ET-0001 v1.4 e EF-0001 v1.3 aprovadas (`b2d729d`) · openapi.yaml 1.0.0 (`8494060`, merge `e34e6b9`) · US-0001 v1.4 (`7d85a6e`) · US-0002 v1.4, REQ-0001..0004 v1.3, RN-0001/0002 v1.3 (`a20fe82`) · UX-0001 v1.1 (`0e9a4af`) · plano G2 v1.2 vigente (`2d2ca94`) · DEC-PO-0008/0009 (no plano) · contexto.yaml v39 (`d82acba`) · historico.md até 15:50 · PT-0001 v1.1 e CT-0001..CT-0049 (`dcb0280`, merge `b49d803`) · protocolo-memoria v1.2 · PROMPT FS v1.1 · rascunhos do OPS (TASK-0012, `rascunhos/ops/DEM-2026-001-TASK-0012-preparacao-dotnet/`).

## 1. Requisito
US-0001 (CA-01..CA-09) e US-0002 (CA-01..CA-06) v1.4, REQ-0001..0004 e RN-0001/0002 v1.3. Os 15 CA não foram reabertos (DEC-PO-0008). Classe R3 (DEC-ARQ-0001). Escopo: `GET /health` (+ `HEAD` tolerado e preflight `OPTIONS`) com 200/503/405/500 e a tela de status com os estados carregando/saudável/erro.

## 2. Arquitetura
ADR-0001 v2.0: .NET 10 LTS, ASP.NET Core Minimal APIs, **zero NuGet de terceiros em runtime**; Angular 22.3 com os padrões do CLI; estrutura D6; nomes D7; obrigações D8 (1–13). ADR-0002 v1.1: `<Version>` do `Portal.Api.csproj` como fonte única, com `IncludeSourceRevisionInInformationalVersion=false`. ADR-0003 v1.1: padrão do health check. Qualidade e entrada no G4: DEC-ARQ-0007 (verify-local A1–A5/W1–W5), 0008 (lint), 0009 (SAST/SCA), 0010 (p95) e 0011 (ganchos 503/500 só pela `WebApplicationFactory<Program>`).
**Lacuna:** o catálogo `01-institucional/microsservicos/` está vazio, e a `portal-api` não está catalogada (dono: ARQ).

## 3. Serviço responsável
`portal-api` (provedor; nasce nesta TASK) e `portal-web` (consumidor), em processos separados e sem código compartilhado (D6). Nenhuma regra de negócio fica na tela: ela só apresenta o contrato (RN-0002: indisponível nunca aparece como saudável).

## 4. Dependências
- **Atendidas:** G2 v1.2 vigente; G3 com R1 fechada; SDK .NET 10.0.404, runtime 10.0.15, Angular CLI 22.3.0, Node 24.22.1 e npm 11.21.1 na box (OPS); PT/CT na main.
- **Pacotes (todos previstos no ADR/DEC; nenhuma tecnologia nova):** API de teste: `xunit` 2.9.3, `xunit.runner.visualstudio` 3.1.4 (padrão do template), `Microsoft.NET.Test.Sdk` 18.12.0, `Microsoft.AspNetCore.Mvc.Testing` 10.0.15, `coverlet.msbuild` 10.1.1 (no lugar do `coverlet.collector` do template). Portal: os do `ng new` (inclui `prettier`, padrão do CLI), `angular-eslint` 22.8.0 via `ng add` (DEC-ARQ-0008) e `@vitest/coverage-v8` 5.1.2 (DEC-ARQ-0007 W3).
- **Em aberto:** biblioteca de validação de esquema (PS-09/R2; ver §9-R2); spike do CA-07 (R4); scripts do OPS em `scripts/` (TASK-0012).

## 5. Contratos
openapi.yaml 1.0.0 (**inalterado**; fonte única no stack-conhecimento). Consumidor único: o Portal. O Mobile não consome. Os mocks do Portal derivam dos exemplos do contrato (PR-04). **Lacuna (ARQ):** como os testes do repositório `portal` referenciam o contrato sem copiá-lo. Proposta: fixtures derivadas dos exemplos, com cabeçalho citando o caminho e o commit do openapi.yaml; o ARQ confirma.

## 6. Banco
Nenhum (`bancos: []`; D5). Sem migração e sem acionar o DBA.

## 7. Impactos no Portal Web e no Mobile
Portal: tela nova (UX-0001 v1.1 / DEC-PO-0005), com tempo limite de 5 s e sem retry (DEC-AS-0001), valores brutos + UTC e Brasília como informação adicional, DOM só com texto, CORS com origem exata. Mobile: sem impacto. CSP: fora desta fase (L-07 do plano).

### 7.1 Decisão proposta — `PORTAL_API_BASE_URL` no Angular (lacuna 3 do ADR-0001 v2.0; L-02 do plano)
**Proposta:** usar a opção oficial `--define` do builder `@angular/build` (já presente; **sem dependência nova**), na subida (`ng serve --define`) e no build (`ng build --define`), com o valor vindo do `.env` local. No código: `declare const PORTAL_API_BASE_URL: string | undefined;`, lido **uma única vez** por um `InjectionToken` (`API_BASE_URL`) provido no `app.config.ts`. Validação: URL absoluta `http:`/`https:`, sem credenciais, sem query e sem fragmento. Se a variável estiver ausente ou for inválida, a tela vai para o estado de erro, sem valor embutido como padrão (fail closed, no mesmo espírito do L-06). Os testes (Vitest) sobrescrevem o token e não dependem do define. O W4 (`ng build`) compila sem o valor, porque o acesso é protegido por `typeof`.
**Ao OPS:** o `start-local.sh` passa o valor JSON-escapado (ex.: `--define "PORTAL_API_BASE_URL=\"$PORTAL_API_BASE_URL\""`).
**Alternativas rejeitadas:** `environment.ts` com `fileReplacements` (o valor iria para o repositório, contra o D7); `config.json` em tempo de execução (exige gerar arquivo e fazer uma requisição extra no bootstrap; mais superfície).
**Observação:** o valor fica visível no bundle. Não é segredo.
Decisão na alçada do FS (ADR-0001 v2.0 D7); peço apenas ciência do ARQ e do OPS.

## 8. Entendimento escrito dos CA
- **US-0001 CA-01** — 200, `application/json; charset=utf-8`, DTO com exatamente `status`/`version`/`timestamp`, não nulos (D8-4). **CA-02** — `status: "ok"`. **CA-03** — `timestamp` gerado por `TimeProvider` no formato `yyyy-MM-dd'T'HH:mm:ss.fff'Z'` com cultura invariante; tolerância de ±5 s; valor exato com relógio injetado; vale também para o 503 (D8-3). **CA-04** — `version` = `<Version>` do `.csproj` (0.1.0) lido uma vez na inicialização de `AssemblyInformationalVersion` e validado pela regex do ADR-0002 com `\z`; versão inválida ou com `+` ⇒ o serviço não inicia. **CA-05** — nenhum `traceId`, `Server`, `+commit`, caminho ou stack trace em nenhuma resposta (D8-2/6). **CA-06** — sem estado nem persistência. **CA-07** — 503 com o mesmo esquema e `status: "unavailable"`, sem `Retry-After`; gancho de teste pela fábrica; em execução, janela de drenagem (spike R4). **CA-08** — 405 com `Allow: GET, HEAD` e corpo problem+json; `HEAD` tolerado; `OPTIONS` ⇒ 204 só no preflight. **CA-09** — 500 com problem+json só `type: about:blank`, `title`, `status`, inclusive com `ASPNETCORE_ENVIRONMENT=Development`; falha injetada só pela fábrica (DEC-ARQ-0011).
- **US-0002 CA-01** — valores brutos iguais aos da mesma consulta, mais a formatação em America/Sao_Paulo como informação adicional; campo desconhecido é ignorado. **CA-02** — indicadores textuais além da cor. **CA-03** — (a) timeout de 5 s, erro HTTP, corpo fora do esquema; (b) 503 de contrato ⇒ erro sem exibir versão nem timestamp (RE-02). **CA-04** — estado inicial "carregando", valores anteriores **removidos do DOM**, `aria-busy`, botão inerte. **CA-05** — "Atualizar status" leva ao estado atual. **CA-06** — só interpolação de texto, nunca `innerHTML`.
Sem lacuna de CA ao PO. Lacunas técnicas do PT (ARQ): L-PT-03 (`OPTIONS` sem cabeçalhos de preflight), L-PT-04 (duração da drenagem), L-PT-11 (superfície com `OPTIONS` explícito), L-PT-13 (escopo dos logs do framework).

## 9. Dúvidas e riscos
### L-04 — piso de 32 h: **o FS NÃO confirma**
L-04 (plano G2 v1.2 §10/§11): as 32 h só valem se o **núcleo da RM-0002 do FS (12–16 h)** for concluído **antes** da TASK-0008. **Fato:** a TASK foi liberada às 15:41 e iniciada em seguida, sem evidência do núcleo do FS (PLANO-RM-0002 §81 pede o núcleo antes da TASK). A condição não se cumpriu, então **mantenho 40 h (faixa 32–50)**. As 32 h ficam só como piso da faixa. Não reduzo antes do spike do CA-07. Não houve atraso de início, então não cabe o aviso à CPO pela regra dos 2 dias úteis.

### Spike do CA-07 (R4) — plano com o ARQ (3 h; faixa 2–5 h)
1. **Hipótese:** no `StopAsync` do host, o `ApplicationStopping` dispara primeiro e marca o estado "encerrando" (o `/health` passa a responder 503). Um `IHostedService` registrado **depois** do servidor segura a parada por uma janela D, porque os hosted services param em ordem inversa e o Kestrel continua escutando. Depois disso, a parada segue. `HostOptions.ShutdownTimeout` deve ser maior que D.
2. **Experimento** em código descartável (ramo `spike/TASK-0008-ca07`, nunca mesclado): API em Release, `SIGTERM` pelo PID e `GET /health` a cada 50 ms. Mede a primeira resposta 503, o número de 503, a ausência de `Retry-After`, a recusa de conexão depois de D e o tempo total até a saída. D candidato < 10 s (o `stop-local.sh` faz SIGKILL em 10 s). **O valor de D é do ARQ (L-PT-04).**
3. **Saída:** relatório com evidência sanitizada. Se for viável, o ARQ valida o mecanismo e D, e o teste automatizado usa `IHostApplicationLifetime.StopApplication()` na fábrica. Se for inviável, o ARQ devolve ao PO, que reabre o CA-07 (DEC-PO-0008).

### R2 / R3 / R5
- **R2 (`format: date-time`):** proposta **sem dependência nova**: validação explícita do corpo com `System.Text.Json`, conjunto exato de campos, `DateTime.TryParseExact` (formato fixo, `InvariantCulture`, UTC) e regex com `\z`. Controle negativo `2026-02-31T10:00:00.000Z` reprovado (CT-0004), como permite o PT-0001. Uma biblioteca de JSON Schema seria tecnologia nova e precisa de avaliação do ARQ: **não adoto**. Peço ao ARQ que confirme a validação explícita.
- **R3 (itens PV do D8 como testes obrigatórios antes do G4):** D8-2 (404/405 problem+json) → CT-0008/0011; D8-3/4 → CT-0001/0003; D8-5 → CT-0008/0009/0010; D8-6 (cabeçalhos em toda resposta, sem `Server`: `KestrelServerOptions.AddServerHeader=false`) → CT-0012; D8-8 (CORS) → CT-0014/0015; D8-9 → CT-0021; D8-10 → spike + CT-0038 (QA); D8-11 → CT-0017..0020/0022; D8-12 → CT-0005. Cada teste leva `[Trait("CT","CT-nnnn")]`. **Confirmado no esqueleto:** a `WebApplicationFactory<Program>` compila e sobe com `Program.cs` de instruções de nível superior, sem declarar `public partial class Program` (o SDK 10 expõe `Program`), o que fecha o "a confirmar" da DEC-ARQ-0011 §2. O CA1707 proíbe `_` em nomes de método, então o ID do CT vai no `Trait`, não no nome.
- **R5 (`\z`):** em todas as regex de `version`/`timestamp`/UUID; controle negativo com `\n` final (CT-0005).

### Riscos
| ID | Risco | Classe | Tratamento |
|---|---|---|---|
| RK-CA07 | Encerramento gracioso inviável ou com D incompatível com os 10 s do stop | R2 | Spike acima; ARQ decide D |
| RK-FS-15 | Padrões do ASP.NET Core vazam `traceId`, `Server`, `+commit` e 7 casas decimais | R3 | D8 + testes R3; `IncludeSourceRevisionInInformationalVersion=false` já no esqueleto |
| RK-FS-13 | Curva de aprendizado sem o núcleo da RM-0002 | R2 | 40 h mantidas; CR + 2ª aprovação do ARQ |
| RK-FS-16 | Cadeia npm: `npm audit` mostra **7 moderadas** (minimatch via `typescript-eslint` 8.72.2 fixado pelo `ng add angular-eslint@22.8.0`; a correção 8.74.0 fica fora da faixa declarada); **0 altas/críticas**, então o W5 passa | R2 | Só reporto (DEC-ARQ-0009); ciência do ARQ |
| RK-FS-17 | npm 11 bloqueou o script de instalação de `msgpackr-extract` (opcional; `@angular/build` → `lmdb`); build e testes verdes sem ele | R1 | Não aprovo script; ciência do OPS/ARQ |

### Outras lacunas e decisões do esqueleto
- `global.json`: `10.0.100` com `rollForward: latestFeature` (série 10.0.x). A política final é do OPS.
- Removidos do template `launchSettings.json` e `appsettings.Development.json`: o bind fica no `Program.cs` (D7) e nada depende de `ASPNETCORE_ENVIRONMENT` (D8). Até a implementação de D7, o esqueleto escuta no padrão do Kestrel (`localhost:5000`).
- `LOG_LEVEL`: aceito `Trace|Debug|Information|Warning|Error|Critical|None`. Valor inválido ou ausente ⇒ `Information` + aviso no log. Mapeado no código para `Logging:LogLevel:Default`.
- Para o OPS: no SDK 10.0.404, `dotnet build --project …` falha (`MSB1001: Switch: --project`); use o caminho posicional. O `ng serve` dá precedência à variável `PORT` sobre `--port`: o `start-local.sh` deve desfazer `PORT`. O `.env.example` do repositório tem **só nomes** (os valores do rascunho do OPS vão para o `.env` local).
- `portal-web` com `package.json` em `0.0.0` (o ADR-0002 só cobre a API); `index.html` com `lang`/`title` do template: decisão do UX na US-0002.

## Próximos passos (fase 2, após o OK do ORQ)
Spike do CA-07 → implementação da US-0001 com CT-0001..0025 → US-0002 com CT-0026..0032 → `verify-local` verde → PR `feat/TASK-0008-health-portal` para o G4.
