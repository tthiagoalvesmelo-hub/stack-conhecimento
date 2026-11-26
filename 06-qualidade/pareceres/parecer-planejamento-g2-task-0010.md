---
id: PARECER-G2-DEM-2026-001-TASK-0010
titulo: "Parecer de planejamento do G2 — TASK-0010 (plano de testes, execução e PQ) — v1.1: reestimativa na stack C#/.NET + Angular"
tipo: analise
versao: 1.1
status: vigente
dono: QA
autores: [QA]
aprovado_por: QA
criado_em: 2026-11-26T12:47-03:00
atualizado_em: 2026-11-26T15:25-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, TASK-0005, TASK-0008, TASK-0009, TASK-0012, PLANO-DEM-2026-001-G2, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0005, DEC-PO-0006, DEC-PO-0008, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-ARQ-0011, DEC-AS-0001, DEC-AS-0002, EF-0001, ET-0001, ADR-0001, ADR-0002, ADR-0003, AH-0003, RM-0002, PLANO-RM-0002]
substitui: null
substituido_por: null
---

# Parecer de planejamento G2 — TASK-0010 (QA) — v1.1

> [TESTE] DEM-2026-001 · parecer de **planejamento** (reestimativa pedida pelo PO, via ORQ, para o plano G2 v1.2 após a AH-0003). **Não** é PT, CT nem PQ: esses artefatos serão criados na execução da TASK-0010. Este documento **não** altera estado, etapa, gates, `contexto.yaml`, `historico.md` nem `Tarefas.csv` (só o ORQ), **não** altera critério de aceite (PO) e **não** reserva IDs PT/CT/PQ. A v1.0 (commit `40c8ace`) permanece no histórico do git; esta v1.1 a substitui para fins de estimativa.

## Histórico de versões
| Versão | Data/hora (America/Sao_Paulo) | Mudança |
|---|---|---|
| 1.0 | 26/11/2026 12:47 (commit `40c8ace`) | Estimativa na stack Node (node:test com fetch mockado + CT manual em Chromium): 20 h (16–23 h). |
| **1.1** | 26/11/2026 15:25 | Reestimativa na stack do ADR-0001 v2.0 (AH-0003): recorte revisto (xUnit + `WebApplicationFactory` + Coverlet; `ng test` Vitest/jsdom; NuGet Audit/`npm audit`), ressalvas R2/R3/R5 do G3, 6 testes da DEC-ARQ-0011, premissas, riscos (inclui RM-0002) e lacunas. Correção de ponteiros (ADR/DEC/US/ET vigentes). |

## 1. Resultado

- **Estimativa v1.1 (QA, em horas, uma pessoa):** ponto sugerido para `Tarefas.csv` **33 h**; faixa **23,5–40 h** (23,5 h = 1º ciclo sem retrabalho, piso; 40 h = com um 2º ciclo, teto). Antes (v1.0): 20 h publicadas (16–23 h). Decomposição e cálculo na seção 4; a comparação "anterior × nova" está na seção 4.1.
- **Por que sobe (+13 h no ponto):** (i) os itens **PV** do ADR-0001 v2 D8 (ressalva R3 do G3) viram casos de teste **obrigatórios antes do G4**, e nenhum deles foi exercido ainda em runtime; (ii) os **6 testes da L-12** (DEC-ARQ-0011 §6) e os controles de R2 e R5 entram no plano; (iii) duas toolchains (dotnet + Node/Angular) e a conferência de cobertura/SCA/lint nos dois apps; (iv) o teste da tela em Vitest/jsdom **reduz** o CT manual em Chromium (alívio de ~1–1,5 h), mas não elimina CA-02 visual nem CORS/ponta a ponta; (v) curva residual de C#/Angular, mostrada em linha própria para o PO poder discuti-la.
- **Nenhum CA muda** (DEC-PO-0008; ARQ, análise de impacto §6): continuam **15 CA** vigentes — US-0001 CA-01..CA-09 (9) e US-0002 CA-01..CA-06 (6) —, **risco R3**. Mudam apenas o **oráculo/método** de CA-04 (manifesto = `<Version>` do `.csproj`), dos ganchos de CA-07/CA-09 (`WebApplicationFactory`) e da verificação da US-0002 (Vitest + jsdom).
- **Meta de cobertura:** mantém-se **80% de linhas** (DEC-ARQ-0007 A4/W3). Ramos e métodos: só reportados.
- **Esta estimativa é ex-ante.** Nada foi medido: SDK .NET 10 e Angular CLI não estão instalados na box e `/workspace/projetos/` não existe (lacuna L-01). Calibração com a 1ª medição real no G5, como já combinado.

## 2. Recorte de teste revisto para a stack nova

Fontes: ADR-0001 v2.0 (D4, D8), DEC-ARQ-0007..0011, ET-0001 v1.4 (merge `9b3dc1b`; confirmação do ARQ da R1 pendente), parecer G3 do ARQ (R1..R5). Equivalência com o recorte v1.0:

| Camada | v1.0 (Node) | v1.1 (ADR-0001 v2 / DEC-ARQ-0007..0011) | Quem escreve o código do teste (premissa, ver L-04) |
|---|---|---|---|
| Unitário API | `node:test` | xUnit 2.9.x (`xunit`, `Microsoft.NET.Test.Sdk`), projeto `tests/Portal.Api.Tests` | FS (TASK-0008); QA **verifica** (PROMPT QA §6.1) |
| Integração / contrato API | testes HTTP em processo | `WebApplicationFactory<Program>` (`Microsoft.AspNetCore.Mvc.Testing` 10.0.x) sem rede; teste de contrato contra o esquema do OpenAPI com `format: date-time` (R2) e `\z` (R5) | FS implementa; **QA especifica os CT e oráculos** e verifica (premissa A) |
| Ganchos 503/500 | fábrica de teste | `ConfigureTestServices` trocando abstrações (DEC-ARQ-0011); produção sem gancho | FS implementa; QA testa/planeja os 6 testes (DEC-ARQ-0011 §6) |
| Unitário/módulo do Portal | `node:test` + fetch mockado | `ng test` (Vitest + jsdom, padrão do CLI); lógica de apresentação separada do DOM continua condição para o FS | FS; QA verifica e especifica oráculos |
| Verificação de tela no navegador | CT manual em Chromium (CA-02/04/05/06) | **Reduzido**: CA-01/03/04/05/06 passam a ter verificação automatizada em jsdom (incl. remoção de valores do DOM, CA-04). **Mantém-se CT manual em Chromium** para CA-02 (distinguível sem depender de cor: jsdom não calcula estilo/contraste), CORS real (CE-08) e ponta a ponta Portal↔API em loopback | QA |
| Cobertura | 80% de linhas no código alterado | Coverlet (`coverlet.msbuild`) `Threshold=80`, `ThresholdType=line`, total do módulo `Portal.Api`; `ng test --coverage` ≥ 80% de linhas do código da aplicação (W3: opção do limiar e pacote de cobertura **a confirmar**, L-05) | FS configura; QA confere o relatório (greenfield: "alterado" = total) |
| Lint/formato | ESLint | `dotnet format --verify-no-changes`, `-warnaserror`, analyzers do SDK; `ng lint` (`angular-eslint`) — DEC-ARQ-0008 | FS; QA lê o log do `verify-local` reexecutado pelo CR |
| SAST/SCA | `npm audit` + ESLint + dirigidos | NuGet Audit no restore (NU1903/NU1904/NU1900 como erro) + `dotnet list package --vulnerable --include-transitive`; `npm audit --audit-level=high`; `AnalysisModeSecurity=All`; **testes dirigidos do QA** (DEC-ARQ-0009). Limite declarado: `angular-eslint` **não** é SAST de segurança | OPS/FS rodam; QA avalia no PQ **neste recorte** |
| p95 indicativo | script Node `fetch` | `scripts/measure-p95.mjs` (Node 24 `fetch`) ou console .NET; API em **Release**, 50 req de aquecimento descartadas + 200 sequenciais; ≤ 100 ms indicativo, **não-SLO** (DEC-ARQ-0010) | OPS/QA |
| Regressão R3 | suíte = esta entrega | idem (primeiro serviço): reexecução completa do `verify-local` na versão do G4 | QA |

**Mantidos do v1.0 (sem alteração):** HEAD ligado ao CA-08; CORS como integração (não é CA); acessibilidade como verificação do CA-02; varredura **e** testes dirigidos (R3); `404`/`OPTIONS` fora do aceite (nota de contrato); linha de base +10% inaplicável na 1ª entrega (usa-se o alvo indicativo e a 1ª medição vira linha de base provisória); versão testada = versão aprovada no G4.

### 2.1 Cobertura de R2, R3, R5 (G3) e mapeamento para os CT

**Rótulos de bloco abaixo são provisórios de planejamento (B1…B9); não são IDs `CT-nnnn` (nenhum CT/PT/PQ foi reservado; `registro-ids.yaml`: PT 0, CT 0, PQ 0).** Os IDs serão reservados na execução da TASK-0010.

| Ressalva | O que o plano faz | Bloco | CA / norma | Condição de aceite do bloco |
|---|---|---|---|---|
| **R2** — `format: date-time` no teste de contrato | Teste de contrato valida o `timestamp` contra o esquema **com o `format: date-time` ativo**. Inclui **controle negativo do validador**: `2026-02-31T10:00:00.000Z` (aceito pelo `pattern`, rejeitado pelo `format`) tem de ser **reprovado**; se o validador o aceitar, o teste de contrato não vale como evidência | B1 | US-0001 CA-03; ET RT-05 | Biblioteca de validação **ainda não escolhida** (PS-09; L-03): sem ela, o bloco B1 fica condicionado |
| **R3** — itens PV do D8 viram casos obrigatórios antes do G4 | Um caso por item PV (tabela 2.2), com oráculo explícito; especificados no PT/CT **antes do PR da TASK-0008**, para entrarem no checklist do CR | B2 | CA-03/04/05/07/08/09; RN-0001; REQ-0004 | 100% dos casos PV especificados antes do G4 e executados no G5 |
| **R5** — `\z` nas regex .NET | Oráculo do QA e testes escritos em .NET usam `\z` (não `$`) para `version`, `timestamp` e UUID. Controle negativo: `1.0.0\n`, `…Z\n` e UUID + `\n` têm de ser **rejeitados** pelo validador usado no teste | B1/B2 (PV-12) | CA-03, CA-04; D8 item 12 | Casos negativos reprovam o valor com `\n` final |

### 2.2 Itens PV do ADR-0001 v2 D8 → casos de teste obrigatórios (R3)

Marcação lida no próprio D8 (coluna Fonte): **PV** nos itens 2 (cobertura 404/405), 3, 4, 5, 6, 8, 9, 10 e 12; o item 11 traz "confirmar na 1ª implementação" (tratado como PV). O item 1 está marcado **V**, mas a R3 do G3 e a análise de impacto o listam entre os casos obrigatórios ("versão sem `+`"); o plano o inclui (ver L-07). Itens 7 (X-Request-Id) e 13 (logs) não têm marca.

| Caso (rótulo) | Item D8 | Oráculo | Como se verifica | CA / RT |
|---|---|---|---|---|
| PV-01 | 1 | `version` sem `+<commit>`; resposta = `<Version>` do `.csproj`; (tag, quando existir, via `check-version.sh`) | xUnit/WAF + leitura do `.csproj` + sonda no processo Release | CA-04 |
| PV-02 | 2 | Erros em `application/problem+json`, `type: about:blank`, só `type/title/status`, **sem `traceId`**, em **404, 405 e 500** | xUnit/WAF + sonda black-box | CA-05/08/09 |
| PV-03 | 3 | `timestamp` `yyyy-MM-dd'T'HH:mm:ss.fff'Z'` (3 casas, cultura invariante) com `TimeProvider` fixo; sem 7 casas | xUnit/WAF (relógio injetado) | CA-03 |
| PV-04 | 4 | Corpo exatamente `status`, `version`, `timestamp`; `Content-Type: application/json; charset=utf-8` | xUnit/WAF + `additionalProperties: false` | CA-01/05 |
| PV-05 | 5 | `GET` e `HEAD` mapeados; 405 com `Allow: GET, HEAD` e corpo problem+json; `OPTIONS` ⇒ 204 só em preflight | xUnit/WAF + sonda | CA-08; CE-07/10/11 |
| PV-06 | 6 | `Cache-Control: no-store` e `X-Content-Type-Options: nosniff` em **toda** resposta (200/503/404/405/500/preflight); **sem** cabeçalho `Server` (opção do Kestrel a confirmar) | xUnit/WAF + sonda no Kestrel real (o `Server` só se vê no servidor real) | CA-05 |
| PV-08 | 8 | CORS: origem exata, sem `*`, sem credenciais; origem não permitida ⇒ sem ACAO e **sem 403**; variável ausente/inválida ⇒ **não inicia** | xUnit/WAF + CT manual no navegador (CE-08) | CE-08; L-06 |
| PV-09 | 9 | 500 sem detalhe e sem página de exceção de desenvolvedor, **inclusive** com `ASPNETCORE_ENVIRONMENT=Development` | xUnit/WAF (mesmo caso da L-12 nº 5) | CA-09 |
| PV-10 | 10 | No encerramento gracioso o listener permanece no ar numa janela de drenagem e responde **503 sem `Retry-After`** | **Depende do spike (R4)**; CT em processo real (sinal de parada) | CA-07 |
| PV-11 | 11 | Ganchos **só** por `WebApplicationFactory`; composição de produção sem gancho; proibidos endpoint/query/cabeçalho/env/config/`FORCE_*`/`IsDevelopment()` | = L-12 nº 3, 4 e 6 | CA-05/07/09 |
| PV-12 | 12 | `\z` (não `$`): valores com `\n` final rejeitados | = R5 | CA-03/04 |
| (fora dos PV) | 7 | `X-Request-Id`: UUID canônico válido devolvido; senão v4; nunca 400 | xUnit/WAF (ET L-03) — incluído no B1 | RT/L-03 |
| (sem oráculo) | 13 | Logs estruturados | **Não estimado**: sem oráculo documentado (L-08) | — |

### 2.3 Os 6 testes da L-12 (DEC-ARQ-0011 §6) → casos

| # | Teste exigido | Bloco | CA / norma | Observação de oráculo |
|---|---|---|---|---|
| L12-1 | 500 por falha **injetada**: status, `Content-Type`, corpo exato, `no-store`, `nosniff`, `X-Request-Id` canônico | B3 | CA-09, CA-05 | Corpo = `type: about:blank`, `title: Internal Server Error`, `status: 500` |
| L12-2 | 503 por estado **injetado**: corpo no esquema e **sem** `Retry-After` | B3 | CA-07, RN-0002 | Mesmo esquema do 200, `status: "unavailable"` |
| L12-3 | Negativo de segurança: query, cabeçalho ou variável de ambiente tentando forçar 503/500 **não** alteram o 200 | B3/B4 | CA-05, REQ-0004 | Executado também no processo Release (black-box) |
| L12-4 | Fábrica **sem** override responde 200 (composição de produção sem gancho) | B3 | PV-11 | — |
| L12-5 | Corpo do 500 sem detalhe com `ASPNETCORE_ENVIRONMENT=Development` | B3 | PV-09, CA-09 | = PV-09 |
| L12-6 | Teste de superfície: só `/health` (GET/HEAD) e tratamento de preflight | B3 | DEC-ARQ-0011 §3–4 | Mecanismo de enumeração dos endpoints: FS |

### 2.4 Rastreio dos 15 CA → blocos de CT (rótulos provisórios)

| CA | Bloco(s) | Observação |
|---|---|---|
| US-0001 CA-01 | B1 (+PV-04) | 200, 3 campos não nulos/vazios |
| US-0001 CA-02 | B1 | `status: "ok"` |
| US-0001 CA-03 | B1 (R2, R5, PV-03, PV-12) | tolerância ±5 s (DEC-AS-0002) com processo real; exata com relógio injetado |
| US-0001 CA-04 | B1/B2 (PV-01) | oráculo: `<Version>` do `.csproj` = resposta (= tag, quando houver). Substitui o oráculo `package.json` da análise de testabilidade v1.0 (L-09) |
| US-0001 CA-05 | B1, B2 (PV-02/04/06), B3 (L12-3), B4 | denylist em 200/405/503/500; também Server/`traceId` |
| US-0001 CA-06 | B1 | ≥ 2 chamadas: status/versão iguais, timestamp varia, sem persistência |
| US-0001 CA-07 | B3 (L12-2), B2 (PV-10), B6 (processo real) | **Condicionado ao spike R4** (L-06) |
| US-0001 CA-08 | B1/B2 (PV-05) | 405 + `Allow: GET, HEAD`; HEAD |
| US-0001 CA-09 | B3 (L12-1/5), B2 (PV-02/09) | 500 por injeção |
| US-0002 CA-01 | B5 (jsdom) + B6 | valores brutos = mesma consulta |
| US-0002 CA-02 | B5 (textos/ARIA) + **B6 manual Chromium** | não depender de cor: verificação visual manual |
| US-0002 CA-03 | B5 + B6 | casos (a) (timeout 5 s sem retry, ≠200/≠503, corpo inválido, CORS) e (b) (503: sem version/timestamp) |
| US-0002 CA-04 | B5 (remoção do DOM) | valores anteriores **removidos** do DOM, não ocultos |
| US-0002 CA-05 | B5 + B6 | recuperação via botão "Atualizar status" |
| US-0002 CA-06 | B5 + B4 | interpolação como texto (análise de impacto do ARQ §6: "a confirmar em teste"); sem HTML |

Blocos: **B1** contrato do provedor (WAF); **B2** itens PV (D8); **B3** L-12 (6 testes); **B4** segurança dirigida (RN-0001/REQ-0004/CA-05/CA-06; Server, `traceId`, denylist, tentativa de forçar 503/500); **B5** Portal em `ng test` (Vitest/jsdom); **B6** integração Portal↔API em loopback e CT manual em Chromium (CORS real, CA-02 visual, encerramento gracioso real); **B7** cobertura + lint + SCA/SAST (DEC-ARQ-0007/0008/0009: leitura/reexecução do `verify-local`); **B8** p95 indicativo (DEC-ARQ-0010); **B9** regressão R3 completa na versão do G4.

## 3. Premissas da estimativa

1. **Stack e versões:** ADR-0001 v2.0 (.NET 10 LTS, ASP.NET Core Minimal APIs, Angular 22.x), ADR-0002/0003 v1.1, DEC-ARQ-0007..0011 vigentes; **15 CA** inalterados (DEC-PO-0008); R3.
2. **Autoria do código de teste automatizado (premissa A):** o FS escreve e mantém os testes xUnit e Vitest na TASK-0008 (alinhado à PROMPT do QA — unitários/integração são do desenvolvedor — e ao parecer do FS, ainda sem commit); a QA **especifica** PT/CT/oráculos antes do PR, **verifica** a suíte (incl. controles negativos de R2/R5), executa black-box e os CT manuais. **Cenário B** (QA escreve o código dos testes de B1–B3): ver seção 4.2. Lacuna L-04.
3. **Sequência:** PT/CT depois do G3 e da R1 (ET-0001 v1.4 já na main; confirmação do ARQ pendente) e **antes do PR da TASK-0008** (R3 do G3 exige os casos PV antes do G4). Execução depois do G4, na versão exata aprovada (a que o CR reexecutou), com SDK .NET 10 + Angular CLI instalados pelo OPS e rede disponível (sem rede, NuGet Audit e `npm audit` não valem como evidência — DEC-ARQ-0007 §4).
4. **Spike R4 (encerramento gracioso) bem-sucedido** antes do CA-07. Se inviável, o CA-07/RN-0002 voltam ao PO (DEC-PO-0008) e as linhas de B6/PV-10 não valem.
5. **Biblioteca de validação de esquema** (PS-09) aprovada pelo ARQ a tempo do B1; sem ela o B1 usa validações explícitas equivalentes (inclui `format: date-time`) com as mesmas horas.
6. **Capacitação RM-0002:** o **núcleo do QA (6–8 h; total 10–14 h, estimativas do ARQ no PLANO-RM-0002 v1.0)** ocorre **antes** da TASK-0010 e **não está** neste total. A linha "curva residual" cobre só o atrito da 1ª execução no projeto real (toolchains, WAF, Vitest).
7. No máximo **um** 2º ciclo (limite de 2 ciclos por gate, PROMPT §1.1). P0/P1 ou mudança de contrato reabrem a faixa.
8. Sem persistência, sem autenticação, dois componentes, suíte de regressão inicial = esta entrega.
9. **Fora do total:** núcleo RM-0002 do QA; 24 h de observação e smoke/rollback (TASK-0012); 2ª aprovação do ARQ (TASK-0007/0003 residual); revisão do CR (TASK-0009).

## 4. Reestimativa por fase (horas)

Todas as linhas são **estimativas da QA** (ex-ante), com intervalo; soma explícita em cada fase.

| Fase | Componente | v1.1 (h) |
|---|---|---|
| **PT + CT** (após G3/R1; antes do PR da TASK-0008) | Estratégia R3, PT e rastreio dos 15 CA | 2–3 |
| | CT de API: contrato (200/503/405/500/HEAD), segurança, CORS, somente leitura, timestamp/versão | 2,5–3,5 |
| | CT do Portal: oráculos para `ng test` + CT manual reduzido (CA-02 a11y, CORS real) | 1,5–2 |
| | Plano de desempenho e de varredura (DEC-ARQ-0009/0010, limites declarados) | 1–1,5 |
| | **Novo:** 11 casos PV do D8 (R3: PV-01..PV-06, PV-08..PV-12) com oráculos | 1,5–2,5 |
| | **Novo:** 6 testes da L-12 + controles negativos de R2/R5 | 1–1,5 |
| | **Novo:** rastreio `verify-local` → critérios do PQ (Coverlet/ng ≥ 80%, lint, SCA/SAST) | 0,5–1 |
| | **Novo:** curva residual C#/Angular | 1–2 |
| | **Subtotal PT + CT** | **11–17** |
| **Execução — 1º ciclo** (após G4, versão aprovada) | Execução base: black-box HTTP, CT manual da tela reduzido, p95 (Release), evidências | 5–6,5 |
| | **Novo:** conferir o `verify-local` na versão do G4 (cobertura Coverlet e `ng test`, NuGet Audit, `npm audit`, analyzers) | 1–1,5 |
| | **Novo:** sondas black-box dos itens PV que só o runtime real mostra (`Server`, 404/405, preflight, 3 casas) | 1–2 |
| | **Novo:** L-12 em Release + controle negativo (remover o override ⇒ o teste tem de falhar) | 0,5–1 |
| | **Novo:** CA-07 em processo real (sinal de parada, janela de drenagem) — se o spike R4 passar | 1–1,5 |
| | **Novo:** revisão de oráculo dos testes do FS (R2/R5, força das asserções, 3–5 mutações manuais) | 1–1,5 |
| | **Novo:** curva residual | 1–2 |
| | **Subtotal 1º ciclo** | **10,5–16** |
| **Retrabalho — 2º ciclo** (se houver) | Reexecução dos CT afetados, `verify-local` e regressão R3 completa | 2,5–4 |
| **PQ** | PQ-nnnn, rastreio 15 CA→CT, evidências de 2 toolchains (cobertura, SCA, PV/L-12), versão = G4 | 2–3 |
| **Total sem 2º ciclo** | 11 + 10,5 + 2 = **23,5** (piso) · 17 + 16 + 3 = **36** | **23,5–36** |
| **Total com 2º ciclo** | 23,5 + 2,5 = **26** · 36 + 4 = **40** (teto) | **26–40** |

**Ponto sugerido para `Tarefas.csv`: 33 h** (≈ ponto médio do cenário com 2º ciclo, 26–40 → 33; a v1.0 também tomou o ponto no cenário com 2º ciclo). **Faixa total: 23,5–40 h.**

### 4.1 Anterior × nova

| Fase | v1.0 (publicado/componentes) | v1.1 | Δ no ponto médio |
|---|---|---|---|
| PT + CT | 8–11 h | 11–17 h | +4,5 h (9,5 → 14) |
| 1º ciclo | 6–8 h | 10,5–16 h | +6,25 h (7 → 13,25) |
| 2º ciclo (se houver) | 2–3 h | 2,5–4 h | +0,75 h (2,5 → 3,25) |
| PQ | 1,5–2 h | 2–3 h | +0,75 h (1,75 → 2,5) |
| **Total (publicado v1.0)** | **20 h (16–23 h)** | **33 h (23,5–40 h)** | **+13 h (+65%)** |

Retificação da própria v1.0: a soma dos seus componentes dá 15,5–21 h (sem 2º ciclo) ou 17,5–24 h (com 2º ciclo), não exatamente a faixa publicada 16–23 h. A comparação acima usa os valores **publicados** (20 h, 16–23 h) no total e os componentes por fase; a soma dos deltas por fase (+12,25 h nos pontos médios dos componentes) difere em ≤ 1 h do delta de totais publicados (+13 h), sem alterar a conclusão.

### 4.2 Sensibilidades (não somadas ao total)

| Cenário | Efeito sobre a TASK-0010 | Observação |
|---|---|---|
| **B — a QA escreve o código dos testes de B1–B3** (leitura literal de "QA escreve/planeja", DEC-ARQ-0011 §6) | **+8 a +12 h** (≈ 20–25 testes xUnit; estimativa QA) | A linha de testes da API do FS (rascunho dele, sem commit) **não pode ser contada duas vezes**: PO/FS ajustam a TASK-0008 |
| Spike R4 mostra que o CA-07 é inviável | −1 a −1,5 h de CT de processo real; **CA-07 reabre no PO** | Não estimo o que o PO decidir |
| Núcleo RM-0002 do QA não ocorre antes | A linha "curva residual" **não cobre**; a QA reestima | Fora desta faixa |
| Biblioteca de esquema negada ou sem suporte a `format` | 0 h (validações explícitas equivalentes) a +1 h de avaliação | Depende do ARQ (PS-09) |
| Falha de PV no 1º ciclo (probabilidade média-alta) | 2º ciclo ocorre (já no teto de 40 h) | Dois ciclos é o limite |

## 5. Riscos e pendências (com dono)

| ID | Tipo | Item | Prob./Impacto | Dono | Mitigação / efeito |
|---|---|---|---|---|---|
| R-QA-01 | Risco | **Curva de capacitação (RM-0002)**: QA, FS, CR e OPS ainda sem experiência na stack; núcleo do QA 6–8 h fora desta faixa; PO ainda não validou prazo/backlog do PLANO-RM-0002 (CPO validou a estratégia) | Média-alta / médio | PO/CPO (prazo); ARQ (conteúdo); QA | Núcleo do QA antes da TASK-0010; evidência do QA = relatório de execução do laboratório com 3 casos PV (PLANO-RM-0002 §4). Sem SDK, a evidência fica "Parcial" (R-2 do plano) |
| R-QA-02 | Risco | Itens PV do D8 **nunca exercidos**; defaults do ASP.NET Core divergem do contrato (ProblemDetails, `+commit`, 7 casas, `Server`) | Média-alta / alto | FS; CR (checklist); QA | Casos PV especificados antes do PR; sondas black-box; 2º ciclo provável |
| R-QA-03 | Risco | **CA-07 depende do spike R4** (encerramento gracioso) | Média / alto no CA | FS/OPS (spike); ARQ; PO se inviável | Sem spike, CA-07 não fecha; PV-10 e CT de processo real não valem |
| R-QA-04 | Risco | Sobreposição de autoria dos testes (L-04): custo contado duas vezes ou por ninguém | Média / médio | PO; ARQ (DEC-ARQ-0011); FS | Decisão explícita; cenário B na seção 4.2 |
| R-QA-05 | Risco | jsdom não calcula estilo/contraste: CA-02 ("não depender só de cor") não se prova em Vitest | Alta / baixo | QA | CT manual em Chromium mantido para CA-02 e CORS real |
| R-QA-06 | Risco | Auditoria sem rede ou NU1900: NuGet Audit e `npm audit` sem execução real não valem como evidência | Média / médio | OPS | Rede disponível; PQ não é favorável pleno sem SCA válida (exceção só com AH de segurança) |
| R-QA-07 | Risco | Duas toolchains instáveis na 1ª execução (Angular 22 + TS 6.0 + `angular-eslint`; `ng test` com cobertura) | Média / médio | FS/ARQ | Linha de curva residual; falha de compatibilidade volta ao ARQ (DEC-ARQ-0008) |
| R-QA-08 | Risco | Testar versão diferente da aprovada no G4 (PROMPT: reprovação automática) | Baixa / alto | QA/CR | SHA do G4 registrado no PT e no PQ |
| P-QA-01..05 | Pendência | v1.0: ambiente local, p95, varredura, ganchos, G3 — **resolvidas em decisão** (DEC-ARQ-0007..0011); falta **execução** (SDK/CLI instalados pelo OPS) | — | OPS | Ver L-01 |

## 6. Lacunas (registradas como lacunas; **não estimadas como se existissem**)

| ID | Lacuna | Dono | Efeito na estimativa |
|---|---|---|---|
| **L-01** | SDK .NET 10 e Angular CLI **não instalados** na box (`dotnet`/`ng` ausentes; `/workspace/projetos/` não existe; ADR-0001 v2 e historico). Nenhum item PV, a opção de limiar do `ng test` ou o comportamento do Coverlet foram exercidos | OPS (TASK-0012) | Toda a estimativa é ex-ante; calibrar no G5 |
| **L-02** | R1 do G3: ET-0001 v1.4/EF-0001 v1.3 estão na main (`9b3dc1b`), mas a **confirmação do ARQ da R1** e o merge da prosa do `openapi.yaml` (`8494060`, ramo próprio) estão pendentes; PT/CT definitivos só após isso | ARQ; AS | PT/CT como rascunho até a confirmação |
| **L-03** | **PS-09:** biblioteca de validação de esquema para o teste de contrato **não escolhida** (ADR-0001 v2 Lacuna 4; ET v1.4). Nenhuma foi nomeada ou estimada | QA/FS propõem; ARQ aprova | R2 depende de validador com `format: date-time`; B1 condicionado |
| **L-04** | **Quem escreve o código dos testes automatizados:** DEC-ARQ-0011 §6 diz "QA escreve/planeja; CR verifica"; PROMPT do QA §1 atribui unitários/integração ao desenvolvedor; o parecer do FS (sem commit) inclui os testes de API e da tela na TASK-0008 | PO/ARQ (decidem); FS; QA | Premissa A no total; cenário B +8–12 h na 4.2 |
| **L-05** | `ng test --coverage` com limiar de 80%: **opção exata e eventual pacote de cobertura a confirmar** (DEC-ARQ-0007 W3); A5 (`dotnet list package --vulnerable`): código de saída "a verificar". Escopo do 80%: DEC-ARQ-0007 usa o **total** do módulo/aplicação (na v1.0 eu escrevi "código alterado"); equivalente no greenfield | FS/QA (confirmar); ARQ (pacote novo) | Calibração no G5; pacote novo passa pelo ARQ |
| **L-06** | **Spike R4** do encerramento gracioso (D8 item 10) não executado; viabilidade do CA-07 em aberto (DEC-PO-0008) | FS/OPS; ARQ | Linhas de CA-07 condicionadas |
| **L-07** | Divergência de rótulo no D8: item 1 (versão sem `+`) é **V** no ADR, mas está na lista de casos obrigatórios da R3/análise de impacto; item 11 sem marca literal PV | ARQ | Tratados como casos obrigatórios (custo marginal); sem CONF aberto |
| **L-08** | D8 item 13 (logs estruturados) e itens sem marca: **sem oráculo de teste** na ET/CA | ARQ/AS | **Não estimado** |
| **L-09** | Minha análise de testabilidade v1.0 (TASK-0005, `80e9184`) cita `package.json` como fonte da versão; o oráculo vigente é `<Version>` do `.csproj` (ADR-0002 v1.1; DEC-PO-0008). **Não reabre CA** | QA | O PT/CT usa o oráculo novo; errata a registrar no PT (esta v1.1 é o aviso) |
| **L-10** | **Dependência no `Tarefas.csv`:** TASK-0010 lista TASK-0009 (G4) como dependência única da fase; a R3 do G3 exige os casos PV **antes do G4**, logo a fase PT+CT não pode esperar o G4 | ORQ | Proposta: dependência da fase PT+CT = G3 + R1 (não altera nada aqui) |
| **L-11** | **Contexto:** a MSG-SOL cita contexto v33 (`89fb397`); a `main` está em v34 (`b57eaa1`: DEC-PO-0008; US-0001 v1.3; US-0002 v1.4; REQ/RN v1.3; ET v1.4). Usei a main; contagem e texto dos 15 CA conferidos (sem reabertura) | ORQ | Sem impacto |
| **L-12** | Pacote de contexto da TASK-0010 em `pacotes-contexto/` **não existe** (não crítica, como na v1.0) | ORQ | Sem impacto |
| **L-13** | Perguntas (a)/(b) da diretriz AH-0003 com o Thiago (Angular 22.x estável; C# só nas APIs do Portal) — premissas registradas pela CPO | ORQ/Thiago | Se mudarem, reestimar |

## 7. Colaborações necessárias

- **OPS:** SDK .NET 10, Angular CLI, rede para NuGet Audit/`npm audit`, valores (nomes) de porta/origem; p95 em Release.
- **ARQ:** confirmar a R1; aprovar a biblioteca de esquema (PS-09) e qualquer pacote de cobertura do `ng test`; decidir L-04 se o PO pedir.
- **FS:** abstrações de saúde/falha injetáveis; expor `Program` ao projeto de teste sem ampliar a produção; lógica de apresentação separada do DOM; oráculos dos casos PV/L-12 recebidos da QA antes do PR; spike R4.
- **CR:** incluir no checklist do G4 os casos PV (R3) e "nenhum gancho na composição de produção" (DEC-ARQ-0011).
- **PO:** consolidar no plano G2 v1.2 (esta estimativa é insumo, não decisão); decidir L-04 com o ARQ; prazo do PLANO-RM-0002.

## 8. Fontes consultadas

- `main` `b57eaa1` (contexto v34); a MSG-SOL citava v33 `89fb397`. `contexto.yaml`, `historico.md` (até 26/11 15:20), `aprovacoes.md`, `Tarefas.csv`, `registro-ids.yaml`.
- **ADR-0001 v2.0** (aceito, AH-0003; D4, D8 itens 1–13, Lacunas); ADR-0002 v1.1; ADR-0003 v1.1; **DEC-ARQ-0007, 0008, 0009, 0010** (substituem 0003..0006) e **DEC-ARQ-0011**; DEC-ARQ-0001 (R3), DEC-ARQ-0002; parecer técnico do ARQ no G3 (R1..R5) e análise de impacto da troca de stack; PLANO-RM-0002 v1.0 (proposto; CPO validou 15:14, falta o PO).
- ET-0001 **v1.4** (merge `9b3dc1b`), EF-0001 v1.3, `openapi.yaml` 1.0.0 (prosa em `8494060`, não mesclada).
- US-0001 v1.3 e US-0002 v1.4 (CA-01..CA-09 e CA-01..CA-06 inalterados), REQ-0001..0004 e RN-0001/0002 v1.3, DEC-PO-0005/0006/0008, DEC-AS-0001/0002; plano G2 v1.1 (TASK-0010); `Tarefas.csv` (estimativas FS e CR de 26/11 15:1x como referência de outros papéis; parecer do FS ainda em `rascunhos/`, sem commit — usado só para detectar sobreposição, não como fonte).
- PARECER-G2 v1.0 (`40c8ace`); ANALISE-TESTABILIDADE (`80e9184`); PROMPT do QA §6 (matriz R3, critérios do PQ); estado-operacional.md (Normal).
- Verificação de ambiente: `which dotnet ng` vazio; `/workspace/projetos/` inexistente.
