---
id: PARECER-G2-DEM-2026-001-TASK-0008
titulo: "Parecer de planejamento do G2 — TASK-0008 (stack .NET 10 LTS + Angular 22.3, AH-0003)"
tipo: parecer
versao: 2.0
status: vigente
dono: FS
autores: [FS]
aprovado_por: null
criado_em: 2026-11-26T15:12-03:00
atualizado_em: 2026-11-26T15:56-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0008, PLANO-DEM-2026-001-G2, US-0001, US-0002, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0002, DEC-ARQ-0011, AH-0001, AH-0003]
substitui: "PARECER-G2-DEM-2026-001-TASK-0008 v1.0 (Node, AH-0001)"
substituido_por: null
---

> Publicado em 26/11/2026 15:56 a partir do rascunho `rascunhos/fs/DEM-2026-001-TASK-0008-parecer-g2-v2-dotnet.md` (L-09 do plano G2 v1.2). Texto preservado como emitido, sem ajustes. Vigente: 40 h (32–50). Posição sobre a L-04 (piso de 32 h) na nota de análise da TASK-0008.

# Rascunho — MSG-RET v2 (parecer de planejamento G2, stack AH-0003)

DEM-2026-001 [TESTE] / TASK-0008 · FS (Lucas Fernandes) → PO (cópia: ORQ)

Status deste arquivo: rascunho em `/workspace/stack-memoria/rascunhos/fs/` (descartável). Não é commit, não é código, não foi enviado. Redigido em 26/11/2026 15:12 (America/Sao_Paulo). Substitui, para fins de estimativa, o parecer Node de 22 h (`DEM-2026-001-TASK-0008-parecer-g2.md`).

---

MSG-RET — DEM-2026-001 [TESTE] / TASK-0008 · reestimativa na stack AH-0003 · FS → PO (cópia: ORQ)

ID da demanda / ID da atividade: DEM-2026-001 / TASK-0008
Remetente: Lucas Fernandes · FS (Agente 08) | Destinatário: Rafael Monteiro · PO (cópia: Orquestrador)
Status: Concluída (somente o parecer v2; implementação não iniciada)
Resumo do resultado: Reestimo a TASK-0008 na stack da AH-0003 (C#/.NET 10 LTS + Angular 22.3) em **32–50 h**, valor de planejamento **40 h** (ante 22 h no parecer Node, +18 h). Nenhum CA muda de comportamento; mudam oráculo ou método de verificação no CA-04 (manifesto `<Version>` do `.csproj`), nos ganchos de teste CA-07/CA-09 (`WebApplicationFactory`) e nos testes da US-0002 (Vitest+jsdom). O CA-07 permanece condicionado ao protótipo de encerramento gracioso (G3 R4 / D8 item 10). Não escrevo código: a TASK-0008 aguarda a R1 do G3 (ET-0001 v1.4, ainda inédita), o plano G2 v1.2 e o SDK/.NET CLI (hoje `dotnet` e `ng` ausentes na box).
Entregáveis: este rascunho em `/workspace/stack-memoria/rascunhos/fs/DEM-2026-001-TASK-0008-parecer-g2-v2-dotnet.md`.
Critérios de conclusão atendidos: estimativa com faixa, quebra e premissas — OK; tabela de CA/RE (oráculo/viabilidade) — OK; lacunas novas, riscos e o que permanece do G3 — OK; sem código/repo/commit — OK.
Decisões tomadas (na minha alçada): nenhuma.
Decisões pendentes: ET-0001 v1.4 (AS, R1); plano G2 v1.2 (PO); instalação SDK .NET 10 e Angular CLI (OPS, R4); biblioteca de validação de esquema (ARQ, R2); valores de porta/origem (TASK-0012); spike do CA-07 (FS após o SDK).
Riscos: seção 4. Dúvidas: ao OPS, quando o SDK/CLI estarão na box? Ao AS, prazo da ET v1.4? Ao ARQ/PO, se o protótipo do CA-07 for inviável?
Impedimentos: para emitir este parecer, nenhum. Para iniciar o desenvolvimento: ET-0001 v1.4 (R1), SDK .NET 10 e Angular CLI, reavaliação do plano G2. Reafirmo: sem código antes disso.
Impactos: Portal Web e portal-api (nascem na nova stack). Mobile: nenhum nesta demanda. Dados: nenhum. Infra: execução local; pasta `/workspace/projetos/` inexistente; duas toolchains.
Evidências: fontes na seção 6; conferência na box em 26/11/2026 15:10 (America/Sao_Paulo): `node` v24.22.1 e `npm` 11.21.1 presentes; `dotnet` e `ng` ausentes (`command not found`). Nada foi instalado.
Fontes consultadas: seção 6. Lacunas: seção 3.
Artefatos criados/alterados: somente este rascunho.
Próximo responsável sugerido: PO (reavaliação do plano G2, ressalva b); AS (ET-0001 v1.4); OPS (SDK/CLI); FS só depois desses insumos.

---

## Premissas da estimativa

- AH-0003 aprovada pelo Thiago em 26/11/2026 14:54 (literal «Aprovo AH-0003»), substitui a AH-0001. ADR-0001 v2.0 aceito.
- O aviso do PO pedia registrar o merge do ramo `doc/TASK-0003-stack-dotnet-angular` como pendente. **Fato na leitura (15:12):** o ramo já está na `main` (merge `d40518e`; conteúdo 7abc2b1 + 7fa2b43). Estimo com o ADR-0001 v2.0 aceito já na main, sem premissa de merge pendente.
- ADR-0002 v1.1 e ADR-0003 v1.1 **aceitos** no G3 (7bc37ba / merge a271ac1). Origem da versão: `<Version>` do `.csproj`.
- OpenAPI portal-api 1.0.0 **não muda** semanticamente (G3: aprovado com ressalva R1 só de prosa).
- G3 registrado como Aprovado com ressalvas (R1–R5). Recomendação do ARQ e contexto.yaml v33: **não liberar a TASK-0008 antes da R1** (ET-0001 v1.4). A v1.4 **não está publicada** (vigente: ET-0001 v1.3, bb3e08a, ainda com premissas Node/AH-0001).
- L-12 formalizada na DEC-ARQ-0011 (parecer prévio favorável do ARQ, confirmado no G3): 503 e 500 só por `WebApplicationFactory<Program>` + `ConfigureTestServices`; fora do OpenAPI; proibido endpoint/query/cabeçalho/env/`FORCE_*`/`IsDevelopment()`.
- Qualidade: DEC-ARQ-0007..0010; lógica de apresentação da tela **separada do DOM**; cobertura **≥ 80% de linhas** no código alterado/aplicação (ramos e métodos só reportados, sem limiar).
- Curva de aprendizado (RM-0002): o time ainda se capacita. O PLANO-RM-0002 v1.0 (proposto, merge 97f90c4) estima núcleo do FS em **12–16 h** (total 18–26 h), **fora desta TASK** («não inclui a execução da demanda»). A DEM é o primeiro exercício prático e **não espera** o fim da capacitação (DEC-CPO-0001). Isso alarga a faixa abaixo: com o núcleo antes, a execução tende ao mínimo; se a curva ocorrer na própria TASK, tende ao máximo. Não invento horas de curso nem embuto o núcleo no valor de planejamento.
- SDK .NET 10 e Angular CLI: instalação do OPS (TASK-0012 / G3 R4). Conferido na box: não instalados. Node 24.22.1 atende o requisito do Angular 22.3 (`^24.15`).
- Portas e origem concreta: TASK-0012; não invento valores. Nomes já no ADR-0001 v2 D7.
- Sem persistência, Mobile, polling, autenticação. Biblioteca de validação de esquema (G3 R2 / PS-09) só após aprovação do ARQ.
- Se o protótipo do encerramento gracioso (D8 item 10) mostrar inviabilidade, o CA-07 volta ao ARQ/PO (MSG-COL) e esta estimativa é reaberta nesse item.

## 1. Estimativa (faixa e valor de planejamento)

**32–50 h**, planejamento **40 h** (uma pessoa, FS, sem ciclo de retrabalho de CA e sem as 12–16 h de núcleo da RM-0002).

| Item | Faixa (h) | Planejamento (h) | Recorte |
|---|---:|---:|---|
| Scaffold .NET + Angular | 5–8 | 6 | Monorepo D6, `global.json`, `Directory.Build.props` (incl. `IncludeSourceRevisionInInformationalVersion=false`), `.csproj`/`packages.lock.json`, `ng new` (Angular 22.3, TS 6.0), validação fail-closed das variáveis, `README`/`.editorconfig` |
| Endpoint `GET /health` | 6–9 | 7 | Minimal APIs; conformidade D8 (ProblemDetails só `type`/`title`/`status`, timestamp com 3 casas, `Allow: GET, HEAD`, preflight, CORS, `no-store`/`nosniff`, remoção de `Server`, versão do assembly, 500 sem detalhe em qualquer ambiente) |
| Testes da API (xUnit + `WebApplicationFactory`, ganchos 503/500) | 5–8 | 6 | 200; 503 e 500 por injeção (DEC-ARQ-0011); negativo de segurança; fábrica sem override = 200; contrato com `format: date-time` e `\z` (R2/R5); CA-04 (`<Version>` = resposta); CA-06 |
| Encerramento gracioso / protótipo CA-07 | 2–5 | 3 | Spike G3 R4 (D8 item 10, PV): janela de drenagem com 503, sem `Retry-After`; distinto do gancho de teste. Se inviável, MSG-COL; esta linha é reaberta |
| Tela Angular | 5–8 | 6 | Spec UX / DEC-PO-0005: três estados, valores brutos + UTC e Brasília, RE-02, limpeza do DOM no carregando, timeout 5 s sem retry, interpolação só como texto (CA-06) |
| Testes da tela (Vitest + jsdom) | 4–6 | 5 | Lógica de apresentação isolada do DOM; sucesso, timeout, corpo inválido, 503 sem version/timestamp, recuperação; cobertura de linhas |
| Logs / instrumentação | 1–2 | 1,5 | `ILogger` estruturado; `/health` em Debug; erros em Error; `X-Request-Id`; sem dado sensível |
| Lint, cobertura, NuGet Audit (`verify-local`) | 2–4 | 3 | DEC-ARQ-0007..0009: `dotnet restore --locked-mode` + audit, `dotnet format --verify-no-changes`, `build -warnaserror`, Coverlet ≥80% linhas, `list package --vulnerable`, `ng lint`, `ng test --coverage`, `ng build`, `npm audit` |
| Evidências / PR | 2–3 | 2 | Nota de análise, relatórios de cobertura, `verify-local` verde, ramo `feat/TASK-0008-…`, trailer `Agente: FS` |
| **Total** | **32–50** | **40** | Soma das faixas 32–53 arredondada no teto a 50 h (incerteza do spike CA-07 e da curva) |

**Comparação com as 22 h do parecer Node (alternativa A):** +18 h no valor de planejamento (~+82%). Principais acréscimos: duas toolchains e scaffold Angular (de 3 para 6 h); conformidade D8 com defaults do ASP.NET Core que conflitam com o contrato (endpoint 5→7); testes via WAF e itens PV (4→6); **item novo** do protótipo CA-07 (3 h); tela e testes Angular/Vitest (4+3 → 6+5); `verify-local`/lint/audit/cobertura formalizados (3 h, antes diluídos no PR). A capacitação (12–16 h) **não** entra neste 40 h.

Fora: retrabalho se o CA-07 for inviável; TASK-0009/0010/0011/0012; núcleo RM-0002; medição formal do p95 (DEC-ARQ-0010, QA/OPS).

## 2. CA e RE — oráculo e viabilidade na stack .NET/Angular

Alinhado à análise do ARQ (§6): **nenhum CA muda de comportamento**. Ajustes de texto, se o PO quiser, são narrativa (premissa da US-0001 que ainda cita `package.json`), não reabertura de comportamento — decisão do PO (ressalva b do G2).

| ID | Comportamento | Oráculo / viabilidade com .NET + Angular | Situação |
|---|---|---|---|
| US-0001 CA-01, CA-02, CA-03, CA-05, CA-06, CA-08 | Igual | Oráculo HTTP/JSON igual (contrato 1.0.0). CA-03 e CA-05 passam a depender da conformidade D8 (timestamp com 3 casas, sem `+`/traceId/`Server`, regex com `\z` nos testes .NET) | Sem mudança de CA |
| US-0001 CA-04 | Igual | **Muda o arquivo do manifesto**, não a estrutura do oráculo: resposta == `<Version>` do `Portal.Api.csproj` == tag `portal-api-v…` (ADR-0002 v1.1). A premissa da US-0001 (linha ~40, `package.json` / AH-0001) está desatualizada | Oráculo operacional atualizado; texto do CA não precisa mudar (ARQ); PO decide se ajusta a premissa |
| US-0001 CA-07 | Igual (503 de contrato) | **Viabilidade de produção condicionado** ao protótipo de encerramento gracioso em ASP.NET Core (D8 item 10, G3 R4). Gancho de **teste** do 503: `WebApplicationFactory` (não confunde com o encerramento). Até agora o ARQ não vê indício de inviabilidade (a verificar). Sem o spike, não fecho o CA | Viabilidade em aberto até o protótipo |
| US-0001 CA-09 | Igual (500 padronizado) | **Muda o mecanismo de teste:** injeção só na composição de teste via `WebApplicationFactory` (DEC-ARQ-0011 / L-12). Corpo sem detalhe inclusive em `Development` | Oráculo de teste atualizado; CA intacto |
| US-0002 CA-01, CA-03, RE-02 | Iguais | Mesmos valores brutos, erro genérico, 503 **sem** exibir versão/timestamp | Sem mudança |
| US-0002 CA-02, CA-04, CA-05 | Iguais | **Muda o método de verificação** (Vitest + jsdom no `ng test`, não mais só módulos com `node:test`). Lógica de apresentação separada do DOM (condição QA) | Método, não o CA |
| US-0002 CA-06 | Igual | Interpolação do Angular deve tratar valores como texto (a confirmar em teste) | Confirmar no teste; CA intacto |

## 3. Novas lacunas (nada disto foi inventado)

- ET-0001 v1.4 **inexistente** (G3 R1). ET vigente = v1.3 (bb3e08a), premissas ainda Node/AH-0001/`package.json`/«fábrica». EF-0001 segue v1.2 (L-10). Prosa do OpenAPI ainda cita AH-0001 (R1; `info.version` 1.0.0 não deve mudar).
- SDK .NET 10 e Angular CLI **não instalados** na box (verificado 15:10; ADR-0001 v2 e G3 R4 já apontavam o mesmo). Sem eles não há scaffold, spike do CA-07 nem `verify-local`.
- `/workspace/projetos/` não existe. Portas, origem e comandos concretos de subida: não definidos (TASK-0012; `PORTAL_API_HOST` tem padrão 127.0.0.1 no D7, demais valores não).
- Biblioteca de validação de esquema do teste de contrato (PS-09 / G3 R2) não escolhida — depende do ARQ.
- Protótipo de encerramento gracioso (D8 item 10, PV) não executado; exposição de `Program` ao projeto de teste «a confirmar na primeira implementação» (DEC-ARQ-0011). Itens PV do D8 (404/405, `Server`, preflight, 3 casas do timestamp) são obrigação, não fato verificado (G3: nenhum runtime .NET foi exercido).
- Pacote eventual de cobertura do `ng test` (DEC-ARQ-0007 W3) a confirmar; dependência nova passa pelo ARQ.
- UX-0001 v1.2 (mapeamento a componentes Angular) consta como evidência proposta da RM-0002, não encontrada como artefato vigente nesta leitura.
- PLANO-RM-0002 v1.0 está **proposto** (escopo/prazo para validação CPO/PO). Núcleo do FS ainda não evidenciado.
- Plano G2 v1.2 ainda não publicado (v1.1 vigente, f61a1f9); contexto v33: TASK-0008 aguarda R1, G2 v1.2 e SDK.
- Pacote `/workspace/stack-memoria/pacotes-contexto/DEM-2026-001/` continua inexistente.

## 4. Riscos atualizados

| ID | Risco | Classe | Mitigação |
|---|---|---|---|
| RK-FS-11 | SDK/CLI ausentes bloqueiam a TASK | R3 | OPS (R4 / TASK-0012); eu não instalo nada nesta atividade |
| RK-FS-12 | Implementar contra ET v1.3 (premissas Node) | R2 | Esperar ET-0001 v1.4 (R1), como recomenda o ARQ |
| RK-FS-13 | Curva de aprendizado (primeira entrega na stack; RM-0002 proposta) | R2 | Faixa larga; núcleo RM-0002 em paralelo, não no 40 h; CR + 2ª aprovação ARQ no G4 (DEC-ARQ-0001) |
| RK-FS-14 | Protótipo do CA-07 inviável ou demorado | R2 | Spike antes de fechar o CA; MSG-COL ao ARQ/PO; reabrir esta linha |
| RK-FS-15 | Defaults do ASP.NET Core vazam `traceId`, `+commit`, timestamp com 7 casas ou cabeçalho `Server` (RN-0001/CA-05) | R3 | Obrigações D8 + testes PV (G3 R3); `IncludeSourceRevisionInInformationalVersion=false` |
| RK-FS-16 | Cadeia npm do Angular (além do NuGet) | R2 | lockfile, `npm ci`, `npm audit` e NuGet Audit no `verify-local` (DEC-ARQ-0007/0009) |
| RK-FS-04..08 | CORS, timestamp/fuso, cache `no-store`, dado sensível, origem da versão — permanecem, agora com a origem no `.csproj` | R2/R3 | Iguais ao parecer anterior, com os testes D8 |
| RK-FS-03 | Mobile futuro | R1 | Contrato 1.0.0 inalterado semanticamente |

## 5. O que precisa constar no G3 (e o que já consta)

O G3 **já foi registrado** (Aprovado com ressalvas, 7bc37ba / merge a271ac1). Não peço um novo G3. Para eu começar, falta fechar as ressalvas que o próprio G3 apontou como pré-TASK-0008:

Já aprovado / aceito: OpenAPI 1.0.0 (comportamento: path `GET /health`, 200/503/405/500, esquemas, exemplos, `no-store`, CORS, `security: []`, timeout de cliente 5 s; p95 indicativo não é SLO); L-12 / DEC-ARQ-0011; ADR-0001 v2.0, ADR-0002/0003 v1.1; DEC-ARQ-0002 e 0007..0010; estrutura D6.

Ainda necessário (não inventar, só ecoar R1–R5 e o contexto v33):
- **R1 (bloqueia o início, recomendação ARQ):** ET-0001 v1.4 + prosa do OpenAPI (sem mudar `info.version` nem esquemas) e EF-0001 (L-10).
- **R4 (antes da TASK / antes de fechar CA-07):** SDK .NET 10 + Angular CLI; `verify-local` vazio; spike do encerramento gracioso.
- **R2 / R5 (antes dos testes de contrato):** biblioteca de schema aprovada pelo ARQ; usar `\z` nas regex em .NET; aplicar `format: date-time`.
- **R3:** itens PV do D8 como casos de teste obrigatórios no PR e no checklist do CR.
- Portas e comandos de execução: ainda a cargo da TASK-0012 (não estão no contrato). Premissa de subida, depois do SDK: `dotnet run` / `ng serve` em processos separados, loopback — valores concretos não definidos.

## 6. Fontes consultadas (ID + caminho + commit)

Repositório `/workspace/stack-memoria/stack-conhecimento/` (HEAD na leitura: 89fb397). Ramo `doc/TASK-0003-stack-dotnet-angular` lido também via log/diff; conteúdo já na main.

| ID | Caminho | Versão / estado | Commit |
|---|---|---|---|
| ADR-0001 | `02-tecnica/adr/ADR-0001-stack-base-portal-api-e-web.md` | v2.0, aceito (AH-0003) | 7abc2b1 (merge d40518e) |
| ADR-0002 | `02-tecnica/adr/ADR-0002-versionamento-semver-campo-versao.md` | v1.1, aceito (G3) | 7bc37ba |
| ADR-0003 | `02-tecnica/adr/ADR-0003-padrao-health-check-get-health.md` | v1.1, aceito (G3) | 7bc37ba |
| ARQ-ANALISE-DEM-2026-001-AH-0003 | `07-agentes/07-arq/analise-impacto-troca-stack-DEM-2026-001.md` | v1.0, vigente | 7fa2b43 |
| DEC-ARQ-0007..0010 | `02-tecnica/contratos-api/portal-api/` | v1.0, vigentes (substituem 0003..0006) | 7fa2b43 |
| DEC-ARQ-0011 | `02-tecnica/contratos-api/portal-api/DEC-ARQ-0011-l12-gancho-de-teste-500-aspnetcore.md` | v1.0, vigente | 7bc37ba |
| PARECER-ARQ-DEM-2026-001-G3 | `07-agentes/07-arq/parecer-tecnico-DEM-2026-001-g3.md` | v1.0, vigente | 7bc37ba (merge a271ac1) |
| ET-0001 | `02-tecnica/especificacoes/ET-0001-health-check-portal-api.md` | v1.3, em-revisao (**v1.4 ausente**) | bb3e08a |
| EF-0001 | `02-tecnica/especificacoes/EF-0001-health-check-portal-api.md` | v1.2, em-revisao | 3a41a2c |
| OpenAPI portal-api | `02-tecnica/contratos-api/portal-api/openapi.yaml` | 1.0.0, aprovado com R1 (prosa) | b3f13d6 |
| PLANO-DEM-2026-001-G2 | `03-operacional/demandas/DEM-2026-001/plano-atividades-g2.md` | v1.1, vigente | f61a1f9 |
| contexto.yaml | `03-operacional/demandas/DEM-2026-001/contexto.yaml` | v33 | 89fb397 |
| aprovacoes.md | `03-operacional/demandas/DEM-2026-001/aprovacoes.md` | AH-0003 aprovada 14:54; G3 com ressalvas | (main) |
| US-0001 / US-0002 / REQ / RN | histórias, requisitos, regras-negocio | v1.2 vigentes | babb9fe |
| PLANO-RM-0002 | `07-agentes/07-arq/capacitacao/RM-0002-plano-capacitacao-dotnet-angular.md` | v1.0, proposto | 3dc12a6 (merge 97f90c4) |
| INST-TECNOLOGIAS | `01-institucional/tecnologias.md` | v1.1, vigente | 7abc2b1 |
| Parecer FS anterior (Node, 22 h) | `/workspace/stack-memoria/rascunhos/fs/DEM-2026-001-TASK-0008-parecer-g2.md` | rascunho, não oficial | — |

A TASK-0008 **não começa** antes da ET-0001 v1.4 (R1), da instalação do SDK/.NET CLI e da reavaliação do plano G2 pelo PO.
