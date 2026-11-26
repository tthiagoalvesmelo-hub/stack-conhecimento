---
id: PARECER-G2-DEM-2026-001-TASK-0010
titulo: "Parecer de planejamento do G2 — TASK-0010 (plano de testes, execução e PQ) — v1.2: PT-0001/CT emitidos, Opção A confirmada"
tipo: analise
versao: 1.2
status: vigente
dono: QA
autores: [QA]
aprovado_por: QA
criado_em: 2026-11-26T12:47-03:00
atualizado_em: 2026-11-26T15:36-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, TASK-0005, TASK-0008, TASK-0009, TASK-0012, PLANO-DEM-2026-001-G2, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0005, DEC-PO-0006, DEC-PO-0008, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-ARQ-0011, DEC-AS-0001, DEC-AS-0002, EF-0001, ET-0001, ADR-0001, ADR-0002, ADR-0003, AH-0003, RM-0002, PLANO-RM-0002, DEC-PO-0009, PT-0001, CT-0001, CT-0049]
substitui: null
substituido_por: null
---

# Parecer de planejamento G2 — TASK-0010 (QA) — v1.2

> [TESTE] DEM-2026-001 · parecer de **planejamento** (reestimativa pedida pelo PO, via ORQ, para o plano G2 v1.2 após a AH-0003). **Não** é PT, CT nem PQ: o plano de testes é o **PT-0001** e os casos são **CT-0001..CT-0049** (emitidos na fase PT+CT, v1.2); o PQ será criado após o G4. Este documento **não** altera estado, etapa, gates, `contexto.yaml`, `historico.md` nem `Tarefas.csv` (só o ORQ), **não** altera critério de aceite (PO) e **não** reserva IDs (PT-0001 e CT-0001..CT-0049 foram reservados pela QA em commit próprio, EL-08). A v1.0 (`40c8ace`) e a v1.1 (`1bd34a6`) permanecem no histórico do git; esta v1.2 as substitui.

## Histórico de versões
| Versão | Data/hora (America/Sao_Paulo) | Mudança |
|---|---|---|
| 1.0 | 26/11/2026 12:47 (commit `40c8ace`) | Estimativa na stack Node (node:test com fetch mockado + CT manual em Chromium): 20 h (16–23 h). |
| **1.1** | 26/11/2026 15:25 | Reestimativa na stack do ADR-0001 v2.0 (AH-0003): recorte revisto (xUnit + `WebApplicationFactory` + Coverlet; `ng test` Vitest/jsdom; NuGet Audit/`npm audit`), ressalvas R2/R3/R5 do G3, 6 testes da DEC-ARQ-0011, premissas, riscos (inclui RM-0002) e lacunas. Correção de ponteiros (ADR/DEC/US/ET vigentes). |
| **1.2** | 26/11/2026 15:36 | Fase PT+CT liberada (G3 + R1; DEC-PO-0009): rótulos provisórios B1..B9 e PV-xx trocados pelos IDs **CT-0001..CT-0049** (PT-0001); **33 h (23,5–40 h) confirmadas**; **Opção A confirmada** (DEC-PO-0009; DEC-ARQ-0011 v1.1) e sensibilidade "cenário B, +8 a +12 h" **descartada**; L-05 e L-08 **fechadas** (DEC-ARQ-0007/0009 v1.1; parecer G3 v1.2 §9.2); L-02, L-04 e L-10 fechadas; L-01 atualizada. |

## 1. Resultado

- **v1.2 (fase PT+CT):** estimativa **confirmada em 33 h (23,5–40 h)**, sem mudança de fase nem de faixa. A especificação produziu o **PT-0001** e **49 CT** (32 automatizados pelo FS e verificados pela QA; 17 manuais/black-box/evidência da QA); os 15 CA têm CT (matriz no PT-0001 §7). Os 3 casos do item 13 do D8 (L-08 fechada) são código do FS (Opção A) e cabem na linha "11 casos PV + L-12" e na revisão de oráculo já estimadas. **Opção A confirmada**; cenário B (+8 a +12 h) **descartado** (seção 4.2).

- **Estimativa v1.1 (QA, em horas, uma pessoa):** ponto sugerido para `Tarefas.csv` **33 h**; faixa **23,5–40 h** (23,5 h = 1º ciclo sem retrabalho, piso; 40 h = com um 2º ciclo, teto). Antes (v1.0): 20 h publicadas (16–23 h). Decomposição e cálculo na seção 4; a comparação "anterior × nova" está na seção 4.1.
- **Por que sobe (+13 h no ponto):** (i) os itens **PV** do ADR-0001 v2 D8 (ressalva R3 do G3) viram casos de teste **obrigatórios antes do G4**, e nenhum deles foi exercido ainda em runtime; (ii) os **6 testes da L-12** (DEC-ARQ-0011 §6) e os controles de R2 e R5 entram no plano; (iii) duas toolchains (dotnet + Node/Angular) e a conferência de cobertura/SCA/lint nos dois apps; (iv) o teste da tela em Vitest/jsdom **reduz** o CT manual em Chromium (alívio de ~1–1,5 h), mas não elimina CA-02 visual nem CORS/ponta a ponta; (v) curva residual de C#/Angular, mostrada em linha própria para o PO poder discuti-la.
- **Nenhum CA muda** (DEC-PO-0008; ARQ, análise de impacto §6): continuam **15 CA** vigentes — US-0001 CA-01..CA-09 (9) e US-0002 CA-01..CA-06 (6) —, **risco R3**. Mudam apenas o **oráculo/método** de CA-04 (manifesto = `<Version>` do `.csproj`), dos ganchos de CA-07/CA-09 (`WebApplicationFactory`) e da verificação da US-0002 (Vitest + jsdom).
- **Meta de cobertura:** mantém-se **80% de linhas** (DEC-ARQ-0007 A4/W3). Ramos e métodos: só reportados.
- **Esta estimativa é ex-ante.** Nada foi medido: SDK .NET 10 e Angular CLI não estão instalados na box e `/workspace/projetos/` não existe (lacuna L-01). Calibração com a 1ª medição real no G5, como já combinado.

## 2. Recorte de teste revisto para a stack nova

Fontes: ADR-0001 v2.0 (D4, D8), DEC-ARQ-0007..0011, ET-0001 v1.4 (merge `9b3dc1b`; confirmação do ARQ da R1 pendente), parecer G3 do ARQ (R1..R5). Equivalência com o recorte v1.0:

| Camada | v1.0 (Node) | v1.1 (ADR-0001 v2 / DEC-ARQ-0007..0011) | Quem escreve o código do teste (Opção A — DEC-PO-0009; DEC-ARQ-0011 v1.1) |
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

### 2.1 Cobertura de R2, R3, R5 (G3) → CT (v1.2)

Na v1.1 estes itens tinham rótulos provisórios (B1..B9, PV-xx). Na v1.2 apontam para os IDs reservados pela QA (PT-0001; CT-0001..CT-0049). Detalhe, oráculos e evidência em cada CT; matriz completa no PT-0001 §7–§8.

| Ressalva | O que o plano faz | CT | CA / norma |
|---|---|---|---|
| **R2** — `format: date-time` | Validação do `timestamp` com `format` ativo; controle negativo `2026-02-31T10:00:00.000Z` tem de ser reprovado | CT-0004 (+ CT-0049, mutação de controle) | US-0001 CA-03; ET RT-05; PS-09 (L-03) |
| **R3** — itens PV do D8 + item 1 | Um CT por item, especificado antes do PR da TASK-0008 (tabela 2.2) | ver 2.2 | CA-03/04/05/07/08/09; RN-0001; REQ-0004 |
| **R5** — `\z` | Valores com `\n` final reprovados em `version`, `timestamp` e UUID | CT-0005 (+ CT-0049) | CA-03, CA-04; D8 item 12 |

### 2.2 Itens do ADR-0001 v2 D8 → CT (R3)

| Item D8 | Marca | CT |
|---|---|---|
| 1 — versão sem `+`, = `<Version>` do `.csproj` | V (incluído pela R3; L-07) | CT-0006, CT-0037 |
| 2 — problem+json em 404/405/500, sem `traceId` | PV | CT-0008, CT-0011, CT-0017 |
| 3 — `timestamp` 3 casas, cultura invariante | PV | CT-0003 |
| 4 — corpo exato e `Content-Type` | PV | CT-0001 |
| 5 — GET/HEAD; 405 com `Allow`; preflight 204 | PV | CT-0008, CT-0009, CT-0010 |
| 6 — `no-store`/`nosniff` em toda resposta; sem `Server` | PV | CT-0012, CT-0035 |
| 7 — `X-Request-Id` | sem marca | CT-0013 |
| 8 — CORS exato, sem 403, fail closed | PV | CT-0014, CT-0015, CT-0039 |
| 9 — 500 sem detalhe em Development | PV | CT-0021 |
| 10 — encerramento gracioso 503 | PV | CT-0038 (condicionado ao spike R4) + CT-0018 (gancho) |
| 11 — ganchos só por `WebApplicationFactory` | "confirmar na 1ª implementação" | CT-0019, CT-0020, CT-0022 |
| 12 — `\z` | PV | CT-0005 |
| 13 — logs (oráculos do parecer G3 v1.2 §9.2) | sem marca | (a) CT-0023 · (b) CT-0024 · (c) CT-0025 |

### 2.3 Os 6 testes da L-12 (DEC-ARQ-0011 v1.1 §6) → CT

| # | Teste | CT |
|---|---|---|
| 1 | 500 injetado: status, `Content-Type`, corpo exato, `no-store`, `nosniff`, `X-Request-Id` | CT-0017 |
| 2 | 503 injetado no esquema, sem `Retry-After` | CT-0018 |
| 3 | Negativo: query/cabeçalho/env não forçam 503/500 | CT-0019 (+ CT-0036 black-box) |
| 4 | Fábrica sem override → 200 | CT-0020 |
| 5 | 500 sem detalhe com `ASPNETCORE_ENVIRONMENT=Development` | CT-0021 |
| 6 | Superfície: só `/health` (GET/HEAD) e preflight | CT-0022 (L-PT-11 do PT) |

### 2.4 Rastreio dos 15 CA → CT

| CA | CT automatizados (FS) | CT da QA |
|---|---|---|
| US-0001 CA-01 | CT-0001 | CT-0033 |
| US-0001 CA-02 | CT-0002 | CT-0033 |
| US-0001 CA-03 | CT-0003, CT-0004, CT-0005, CT-0018 | CT-0034 |
| US-0001 CA-04 | CT-0005, CT-0006 | CT-0037 |
| US-0001 CA-05 | CT-0012, CT-0013, CT-0016, CT-0017, CT-0019, CT-0025 | CT-0035, CT-0036 |
| US-0001 CA-06 | CT-0007 | — |
| US-0001 CA-07 | CT-0018 | CT-0038 (condicionado ao spike R4) |
| US-0001 CA-08 | CT-0008, CT-0009 | CT-0033 |
| US-0001 CA-09 | CT-0017, CT-0021, CT-0024 | — (só por injeção) |
| US-0002 CA-01 | CT-0026 | CT-0041 |
| US-0002 CA-02 | CT-0027 | CT-0040 (manual, sem cor) |
| US-0002 CA-03 | CT-0028, CT-0029 | CT-0039, CT-0041 |
| US-0002 CA-04 | CT-0030 | CT-0041 |
| US-0002 CA-05 | CT-0031 | CT-0041 |
| US-0002 CA-06 | CT-0032 | CT-0041 |

Equivalência com os blocos da v1.1: **B1** → CT-0001..CT-0016 · **B2** → tabela 2.2 · **B3** → CT-0017..CT-0022 · **B4** → CT-0016, CT-0019, CT-0021, CT-0025, CT-0032, CT-0035, CT-0036 · **B5** → CT-0026..CT-0032 · **B6** → CT-0033, CT-0038..CT-0041 · **B7** → CT-0043..CT-0047 · **B8** → CT-0042 · **B9** → CT-0048. Novos na v1.2: CT-0023..CT-0025 (item 13), CT-0034 e CT-0037 (black-box de tolerância e versão) e CT-0049 (verificação da suíte do FS com mutações de controle). A cobertura vem do PT-0001.

## 3. Premissas da estimativa

1. **Stack e versões:** ADR-0001 v2.0 (.NET 10 LTS, ASP.NET Core Minimal APIs, Angular 22.x), ADR-0002/0003 v1.1, DEC-ARQ-0007..0011 vigentes; **15 CA** inalterados (DEC-PO-0008); R3.
2. **Autoria do código de teste automatizado — Opção A, confirmada (v1.2):** o FS escreve e mantém os testes xUnit/WAF e Vitest na TASK-0008 (DEC-PO-0009; concordância técnica na DEC-ARQ-0011 v1.1, que esclarece a frase "QA escreve/planeja" do item 6). A QA **especifica** PT/CT/oráculos antes do PR, **verifica** a suíte (CT-0049, com controles negativos de R2/R5), executa black-box e os CT manuais. O cenário B foi **descartado** (seção 4.2).
3. **Sequência:** PT/CT depois do G3 e da R1 (ET-0001 v1.4 já na main; confirmação do ARQ pendente) e **antes do PR da TASK-0008** (R3 do G3 exige os casos PV antes do G4). Execução depois do G4, na versão exata aprovada (a que o CR reexecutou), com SDK .NET 10 + Angular CLI instalados pelo OPS e rede disponível (sem rede, NuGet Audit e `npm audit` não valem como evidência — DEC-ARQ-0007 §4).
4. **Spike R4 (encerramento gracioso) bem-sucedido** antes do CA-07. Se inviável, o CA-07/RN-0002 voltam ao PO (DEC-PO-0008) e o CT-0038 não vale (CT-0018 continua, por gancho).
5. **Biblioteca de validação de esquema** (PS-09) aprovada pelo ARQ a tempo do CT-0004; sem ela o CT-0004 usa validações explícitas equivalentes (inclui `format: date-time`) com as mesmas horas.
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
| | **Novo:** 11 casos PV do D8 (R3; CT da tabela 2.2) com oráculos | 1,5–2,5 |
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
| ~~B — a QA escreve o código dos testes de B1–B3~~ | ~~+8 a +12 h~~ — **descartada na v1.2** | Opção A confirmada (DEC-PO-0009; DEC-ARQ-0011 v1.1): o código é do FS na TASK-0008 (40 h já incluem 11 h de testes, segundo o `historico.md` de 15:26). Sem contagem dupla. Só volta se o PO reabrir a opção B |
| Spike R4 mostra que o CA-07 é inviável | −1 a −1,5 h de CT de processo real; **CA-07 reabre no PO** | Não estimo o que o PO decidir |
| Núcleo RM-0002 do QA não ocorre antes | A linha "curva residual" **não cobre**; a QA reestima | Fora desta faixa |
| Biblioteca de esquema negada ou sem suporte a `format` | 0 h (validações explícitas equivalentes) a +1 h de avaliação | Depende do ARQ (PS-09) |
| Falha de PV no 1º ciclo (probabilidade média-alta) | 2º ciclo ocorre (já no teto de 40 h) | Dois ciclos é o limite |

## 5. Riscos e pendências (com dono)

| ID | Tipo | Item | Prob./Impacto | Dono | Mitigação / efeito |
|---|---|---|---|---|---|
| R-QA-01 | Risco | **Curva de capacitação (RM-0002)**: QA, FS, CR e OPS ainda sem experiência na stack; núcleo do QA 6–8 h fora desta faixa; PO ainda não validou prazo/backlog do PLANO-RM-0002 (CPO validou a estratégia) | Média-alta / médio | PO/CPO (prazo); ARQ (conteúdo); QA | Núcleo do QA antes da TASK-0010; evidência do QA = relatório de execução do laboratório com 3 casos PV (PLANO-RM-0002 §4). Sem SDK, a evidência fica "Parcial" (R-2 do plano) |
| R-QA-02 | Risco | Itens PV do D8 **nunca exercidos**; defaults do ASP.NET Core divergem do contrato (ProblemDetails, `+commit`, 7 casas, `Server`) | Média-alta / alto | FS; CR (checklist); QA | Casos PV especificados antes do PR; sondas black-box; 2º ciclo provável |
| R-QA-03 | Risco | **CA-07 depende do spike R4** (encerramento gracioso) | Média / alto no CA | FS/OPS (spike); ARQ; PO se inviável | Sem spike, CA-07 não fecha; CT-0038 (processo real) não vale |
| R-QA-04 | Risco | Sobreposição de autoria dos testes (L-04): custo contado duas vezes ou por ninguém | — | PO; ARQ; FS | **Fechado na v1.2:** Opção A (DEC-PO-0009; DEC-ARQ-0011 v1.1) |
| R-QA-05 | Risco | jsdom não calcula estilo/contraste: CA-02 ("não depender só de cor") não se prova em Vitest | Alta / baixo | QA | CT manual em Chromium mantido para CA-02 e CORS real |
| R-QA-06 | Risco | Auditoria sem rede ou NU1900: NuGet Audit e `npm audit` sem execução real não valem como evidência | Média / médio | OPS | Rede disponível; PQ não é favorável pleno sem SCA válida (exceção só com AH de segurança) |
| R-QA-07 | Risco | Duas toolchains instáveis na 1ª execução (Angular 22 + TS 6.0 + `angular-eslint`; `ng test` com cobertura) | Média / médio | FS/ARQ | Linha de curva residual; falha de compatibilidade volta ao ARQ (DEC-ARQ-0008) |
| R-QA-08 | Risco | Testar versão diferente da aprovada no G4 (PROMPT: reprovação automática) | Baixa / alto | QA/CR | SHA do G4 registrado no PT e no PQ |
| P-QA-01..05 | Pendência | v1.0: ambiente local, p95, varredura, ganchos, G3 — **resolvidas em decisão** (DEC-ARQ-0007..0011); falta **execução** (SDK/CLI instalados pelo OPS) | — | OPS | Ver L-01 |

## 6. Lacunas (registradas como lacunas; **não estimadas como se existissem**)

| ID | Lacuna | Dono | Efeito na estimativa |
|---|---|---|---|
| **L-01** | Toolchain **instalada** pelo OPS e conferida pelo ORQ (`dotnet` 10.0.404, Angular CLI 22.3.0, Node v24.22.1; `historico.md` 15:30). Restam: `/workspace/projetos/` ainda não existe (esqueleto D6 da TASK-0008) e o `dotnet` está em `~/.dotnet`, fora do PATH do shell da QA (L-PT-07 do PT-0001). Nada foi exercido em runtime | OPS (PATH); FS (esqueleto) | Estimativa segue ex-ante; calibrar no G5 |
| **L-02** | ~~Confirmação da R1~~ — **fechada (v1.2):** o ARQ confirmou a R1 (merges `e34e6b9` e `edc9467`, `historico.md` 15:34); ET-0001 v1.4 / EF-0001 v1.3 aprovadas (`b2d729d`) | — | PT/CT definitivos emitidos |
| **L-03** | **PS-09:** biblioteca de validação de esquema para o teste de contrato **não escolhida** (ADR-0001 v2 Lacuna 4; ET v1.4). Nenhuma foi nomeada ou estimada | QA/FS propõem; ARQ aprova | R2 depende de validador com `format: date-time`; CT-0004 condicionado (critério de entrada 6 do PT-0001) |
| **L-04** | ~~Quem escreve o código dos testes automatizados~~ — **fechada (v1.2):** Opção A (DEC-PO-0009, ID reservado em `7d85a6e`, conteúdo no plano G2 v1.2 em-revisão; DEC-ARQ-0011 v1.1) | — | Cenário B descartado |
| **L-05** | ~~Opção/pacote do `ng test --coverage` e oráculo do A5~~ — **fechada (v1.2):** W3 e A5 respondidos pelo ARQ na DEC-ARQ-0007 v1.1 e na DEC-ARQ-0009 v1.1 (cobertura do `ng test` com 80% de linhas; SCA pelo JSON do `dotnet list package --vulnerable` + NU1903/NU1904/NU1900 como erro, o código de saída não é o oráculo) | — | CT-0043, CT-0044, CT-0045 |
| **L-06** | **Spike R4** do encerramento gracioso (D8 item 10) não executado; viabilidade do CA-07 em aberto (DEC-PO-0008) | FS/OPS; ARQ | Linhas de CA-07 condicionadas |
| **L-07** | Divergência de rótulo no D8: item 1 (versão sem `+`) é **V** no ADR, mas está na lista de casos obrigatórios da R3/análise de impacto; item 11 sem marca literal PV | ARQ | Tratados como casos obrigatórios (custo marginal); sem CONF aberto |
| **L-08** | ~~D8 item 13 sem oráculo~~ — **fechada (v1.2):** 3 oráculos no parecer G3 v1.2 §9.2 → CT-0023 (a), CT-0024 (b), CT-0025 (c). Fica uma dúvida de escopo de categorias no 13(a), registrada como L-PT-13 no PT-0001 (dono: ARQ) | — | Dentro das 33 h (código do FS; verificação da QA na revisão de oráculo) |
| **L-09** | Minha análise de testabilidade v1.0 (TASK-0005, `80e9184`) cita `package.json` como fonte da versão; o oráculo vigente é `<Version>` do `.csproj` (ADR-0002 v1.1; DEC-PO-0008). **Não reabre CA** | QA | O PT/CT usa o oráculo novo; errata a registrar no PT (esta v1.1 é o aviso) |
| **L-10** | ~~Dependência da fase PT+CT~~ — **fechada (v1.2):** PT+CT depende de G3 + R1 (DEC-PO-0009; concordância técnica na DEC-ARQ-0011 v1.1); dependência ajustada pelo ORQ no `Tarefas.csv` (`historico.md` 15:26); fase liberada às 15:36 | — | — |
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

- **v1.2:** `main` `7d85a6e` (contexto v37; `historico.md` até 15:40); DEC-ARQ-0007/0009/0011 v1.1 e parecer G3 v1.2 §9 (`edc9467`); parecer OPS v2.1 (`ce58d16`); plano G2 v1.2 em-revisão e US-0001 v1.4 editorial (`7d85a6e`); PT-0001 e CT-0001..CT-0049 (ramo `doc/TASK-0010-pt-ct`).

- `main` `b57eaa1` (contexto v34); a MSG-SOL citava v33 `89fb397`. `contexto.yaml`, `historico.md` (até 26/11 15:20), `aprovacoes.md`, `Tarefas.csv`, `registro-ids.yaml`.
- **ADR-0001 v2.0** (aceito, AH-0003; D4, D8 itens 1–13, Lacunas); ADR-0002 v1.1; ADR-0003 v1.1; **DEC-ARQ-0007, 0008, 0009, 0010** (substituem 0003..0006) e **DEC-ARQ-0011**; DEC-ARQ-0001 (R3), DEC-ARQ-0002; parecer técnico do ARQ no G3 (R1..R5) e análise de impacto da troca de stack; PLANO-RM-0002 v1.0 (proposto; CPO validou 15:14, falta o PO).
- ET-0001 **v1.4** (merge `9b3dc1b`), EF-0001 v1.3, `openapi.yaml` 1.0.0 (prosa em `8494060`, não mesclada).
- US-0001 v1.3 e US-0002 v1.4 (CA-01..CA-09 e CA-01..CA-06 inalterados), REQ-0001..0004 e RN-0001/0002 v1.3, DEC-PO-0005/0006/0008, DEC-AS-0001/0002; plano G2 v1.1 (TASK-0010); `Tarefas.csv` (estimativas FS e CR de 26/11 15:1x como referência de outros papéis; parecer do FS ainda em `rascunhos/`, sem commit — usado só para detectar sobreposição, não como fonte).
- PARECER-G2 v1.0 (`40c8ace`); ANALISE-TESTABILIDADE (`80e9184`); PROMPT do QA §6 (matriz R3, critérios do PQ); estado-operacional.md (Normal).
- Verificação de ambiente: `which dotnet ng` vazio; `/workspace/projetos/` inexistente.
