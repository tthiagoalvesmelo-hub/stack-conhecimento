---
id: PT-0001
titulo: "Plano de testes — DEM-2026-001 [TESTE] · TASK-0010 · GET /health e tela de status (G5)"
tipo: pt
versao: 1.0
status: vigente
dono: QA
autores: [QA]
aprovado_por: QA
criado_em: 2026-11-26T15:35-03:00
atualizado_em: 2026-11-26T15:35-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, TASK-0008, TASK-0009, TASK-0012, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, ET-0001, EF-0001, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-ARQ-0011, DEC-PO-0005, DEC-PO-0006, DEC-PO-0008, DEC-PO-0009, DEC-AS-0001, DEC-AS-0002, UX-0001, PARECER-G2-DEM-2026-001-TASK-0010, CT-0001, CT-0049]
substitui: null
substituido_por: null
---

# PT-0001 — Plano de testes da DEM-2026-001 [TESTE] · TASK-0010 (G5)

> [TESTE] Fase de testes internos; nada vai à produção. Estado operacional: Normal. **Este plano especifica; nada foi executado.** A execução e o PQ-nnnn ocorrem **após o G4**, na versão exata aprovada (SHA registrada). Este documento não altera critérios de aceite (PO), estado, gates nem `contexto.yaml` (ORQ).

## 1. Objetivo e escopo
- **Objetivo:** verificar de forma independente os **15 CA vigentes** — US-0001 CA-01..CA-09 (v1.4) e US-0002 CA-01..CA-06 (v1.4), sem reabertura (DEC-PO-0008) — e as obrigações técnicas que condicionam o G4/G5: ressalvas **R2, R3 e R5** do G3, os **6 testes da L-12** (DEC-ARQ-0011), o **item 13** do ADR-0001 v2 D8 (logs), SAST/SCA (DEC-ARQ-0009 v1.1), cobertura (DEC-ARQ-0007 v1.1) e p95 indicativo (DEC-ARQ-0010).
- **Dentro:** `portal-api` (`GET /health`, HEAD, 405, 503, 500, preflight, 404 padrão do serviço) e a tela de status do `portal-web` (Angular), em execução local na box (loopback).
- **Fora do aceite dos CA (verificados como obrigação técnica, sem novo CA):** 404 de rota inexistente, `OPTIONS`/preflight, CORS, logs, cobertura, SCA/SAST, p95. **Fora deste plano:** observação de 24 h, smoke/rollback (TASK-0012), Mobile.
- **Classe de risco:** R3 (DEC-ARQ-0001) — matriz de proporcionalidade R3 (PROMPT do QA, seção 6.1 da governança, tabela 6.2): unitários, integração, funcionais, regressão completa, contrato, segurança (varredura + testes dirigidos), desempenho (caminho crítico) e aceitação obrigatórios.

## 2. Base (versões conferidas na `main` `7d85a6e`, contexto v37+)
US-0001 v1.4 (editorial de referência: "ADR proposto" → "ADR v1.1, aceito" nos CA-04/07/08/09; nenhum CA muda de comportamento, ID ou oráculo) e US-0002 v1.4 (CA inalterados); REQ-0001..0004 e RN-0001/0002 v1.3; ET-0001 v1.4 e EF-0001 v1.3 (aprovadas pelo ARQ, G3/R1); `openapi.yaml` portal-api 1.0.0 (prosa R1, e34e6b9); ADR-0001 v2.0 (D4, D7, D8), ADR-0002 v1.1, ADR-0003 v1.1; DEC-ARQ-0002; DEC-ARQ-0007 v1.1, 0008, 0009 v1.1, 0010, 0011 v1.1; parecer G3 do ARQ v1.2 (§9); UX-0001 v1.1 (DEC-PO-0005); DEC-AS-0001/0002; DEC-PO-0009 (ID reservado e conteúdo no plano G2 v1.2, `7d85a6e`, status em-revisão; concordância técnica na DEC-ARQ-0011 v1.1 — L-PT-08); parecer OPS da TASK-0012 v2.1 (portas, scripts, p95, evidências).

## 3. Estratégia e responsabilidades (Opção A — DEC-PO-0009; DEC-ARQ-0011 v1.1)
| Tipo do CT | Quem escreve/executa | O que a QA faz | Qtde |
|---|---|---|---|
| **AUT-API** | FS escreve e mantém (xUnit 2.9.x + `WebApplicationFactory<Program>`, `tests/Portal.Api.Tests`) na TASK-0008 | Especifica (este PT/CT, **antes do PR**), verifica a suíte (CT-0049) e a executa no `verify-local` (CT-0048) | 25 |
| **AUT-WEB** | FS escreve e mantém (`ng test`, Vitest + jsdom) na TASK-0008 | Idem | 7 |
| **QA-BB** | QA, black-box contra o processo real em Release (loopback) | Executa e registra evidência | 6 |
| **QA-MAN** | QA, manual no navegador da box (Chrome/Chromium) e/ou processo real | Executa e registra evidência | 4 |
| **QA-EVID** | QA, sobre as evidências do `verify-local` e da suíte | Reexecuta/lê e julga | 7 |
| **Total** | | | **49** (automatizados pelo FS: 32; QA manual/black-box/evidência: 17) |

Regras: (i) cada teste automatizado leva o ID do CT (ex.: `[Trait("CT","CT-0001")]`; nome do `describe`/`it` com o ID) — sem isso o rastreio CA → CT não fecha; (ii) a QA não corrige código testado: divergência vira **BUG-nnnn** (P0–P3) ao FS; (iii) ganchos de falha **só** por `WebApplicationFactory` (DEC-ARQ-0011); (iv) nenhuma ferramenta nova (sem Playwright/automação de navegador); (v) dados de teste fictícios; nenhum segredo; evidências sanitizadas em `/workspace/projetos/portal/evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado), citadas no PQ.

## 4. Ambiente
Execução local na box, em loopback, conforme o parecer OPS v2.1: API em **Release** e Portal em `ng serve`, processos separados, por `scripts/start-local.sh` / `scripts/stop-local.sh` (SIGTERM, SIGKILL após 10 s). Configuração **só por nome** (ADR-0001 v2 D7): `PORTAL_API_HOST`, `PORTAL_API_PORT`, `PORTAL_API_ALLOWED_ORIGIN`, `LOG_LEVEL`, `PORTAL_WEB_PORT`, `PORTAL_API_BASE_URL`; valores no `.env` fora do git. Toolchain: SDK .NET 10 (10.0.404), Angular CLI 22.3.0, Node 24 (evidência OPS). Rede necessária para NuGet Audit e `npm audit`.

## 5. Critérios de entrada no G5 (execução)
1. G4 encerrado: CR-nnnn **Aprovado** ou **Aprovado com observações** + 2ª aprovação explícita do ARQ (R3); SHA aprovada registrada.
2. `verify-local` verde na SHA do G4 (log do FS no PR e reexecução do CR — DEC-ARQ-0007 §3), incluindo A1–A5 e W1–W5.
3. CT-0001..CT-0032 implementados pelo FS, identificáveis pelo ID do CT (checklist do CR inclui os itens PV — R3 — e "nenhum gancho na composição de produção" — DEC-ARQ-0011).
4. Ambiente da TASK-0012 pronto (scripts depositados, valores no `.env`, toolchain com o `dotnet` acessível no PATH de quem executa — L-PT-07) e rede disponível.
5. Spike R4 registrado (condição do CT-0038 / CA-07). Sem ele, a execução começa, mas o CA-07 fica **pendente** no PQ.
6. Biblioteca de validação de esquema aprovada pelo ARQ (PS-09) ou validação explícita equivalente com o controle negativo do CT-0004.
7. Nenhuma MSG-BLQ aberta que impeça a execução; PT-0001 vigente.

## 6. Critérios de saída do G5 (PQ-nnnn — PROMPT do QA, tabela 6.3)
- **Favorável:** 100% dos 15 CA com CT executado e aprovado (matriz da seção 7); nenhum BUG P0/P1 aberto; P2 só com aceite registrado do PO (funcional) ou do ARQ (técnico) e BUG-nnnn planejado; suíte aplicável 100% aprovada (CT-0048; teste instável em quarentena com TD-nnnn não conta); contrato aprovado (CT-0001..CT-0011, CT-0033); varredura sem alta/crítica no recorte da DEC-ARQ-0009 (CT-0045..CT-0047; exceção só com AH de segurança); cobertura ≥ 80% de linhas nos dois apps (CT-0043, CT-0044); p95 medido e registrado (CT-0042; **indicativo**, a 1ª medição é a linha de base provisória — o "+10%" não se aplica à 1ª entrega); evidências anexadas; versão testada = versão do G4.
- **Favorável com ressalvas:** só P3 ou observações, com aceite registrado.
- **Desfavorável:** qualquer critério acima não atendido, ou versão testada diferente da aprovada no G4. A reprovação só é revista por escrito pelo ARQ (técnica) ou pelo PO (funcional).
- **Limite de retrabalho (PROMPT 7.5):** após 2 ciclos de reprovação no G5 para a mesma atividade, não há 3º ciclo automático: o ORQ escala ao ARQ e ao responsável do fluxo.

## 7. Matriz de rastreabilidade CA → CT (15 de 15)
| CA | Oráculo resumido | CT automatizados (FS) | CT da QA |
|---|---|---|---|
| US-0001 CA-01 | 200, JSON, exatamente `status`/`version`/`timestamp`, não nulos/vazios | [CT-0001](../casos-teste/CT-0001-get-health-200-tres-campos.md) | [CT-0033](../casos-teste/CT-0033-bb-contrato-kestrel-real.md) |
| US-0001 CA-02 | `status` = `"ok"` | [CT-0002](../casos-teste/CT-0002-status-ok.md) | [CT-0033](../casos-teste/CT-0033-bb-contrato-kestrel-real.md) |
| US-0001 CA-03 | `timestamp` UTC, `Z`, 3 casas; ±5 s (DEC-AS-0002); exato com relógio injetado; também no 503 | [CT-0003](../casos-teste/CT-0003-timestamp-formato-relogio-injetado.md), [CT-0004](../casos-teste/CT-0004-r2-format-date-time-controle-negativo.md), [CT-0005](../casos-teste/CT-0005-r5-ancora-z-controle-negativo.md), [CT-0018](../casos-teste/CT-0018-l12-2-503-injetado.md) | [CT-0034](../casos-teste/CT-0034-bb-timestamp-tolerancia.md) |
| US-0001 CA-04 | `version` = `<Version>` do `.csproj` (= tag, quando houver), SemVer sem `+`/hash | [CT-0005](../casos-teste/CT-0005-r5-ancora-z-controle-negativo.md), [CT-0006](../casos-teste/CT-0006-versao-igual-csproj-sem-build.md) | [CT-0037](../casos-teste/CT-0037-bb-versao-tripla.md) |
| US-0001 CA-05 | Sem dado sensível em corpo/cabeçalhos (200, 405, 503, 500); sem `Server`; logs sem denylist | [CT-0012](../casos-teste/CT-0012-cabecalhos-em-toda-resposta.md), [CT-0013](../casos-teste/CT-0013-x-request-id.md), [CT-0016](../casos-teste/CT-0016-denylist-corpo-cabecalhos.md), [CT-0017](../casos-teste/CT-0017-l12-1-500-injetado.md), [CT-0019](../casos-teste/CT-0019-l12-3-negativo-canais-proibidos.md), [CT-0025](../casos-teste/CT-0025-logs-denylist.md) | [CT-0035](../casos-teste/CT-0035-bb-server-e-cabecalhos.md), [CT-0036](../casos-teste/CT-0036-bb-negativo-forcar-falha.md) |
| US-0001 CA-06 | Chamadas repetidas: status/versão iguais, sem estado de negócio | [CT-0007](../casos-teste/CT-0007-somente-leitura-chamadas-repetidas.md) | — |
| US-0001 CA-07 | 503 com o mesmo esquema, `"unavailable"`, sem detalhe/`Retry-After` | [CT-0018](../casos-teste/CT-0018-l12-2-503-injetado.md) (gancho de teste) | [CT-0038](../casos-teste/CT-0038-man-encerramento-gracioso-503.md) (encerramento real; **condicionado ao spike R4**) |
| US-0001 CA-08 | 405 + `Allow: GET, HEAD` + problem+json; HEAD tolerado | [CT-0008](../casos-teste/CT-0008-metodos-nao-permitidos-405.md), [CT-0009](../casos-teste/CT-0009-head-tolerado.md) | [CT-0033](../casos-teste/CT-0033-bb-contrato-kestrel-real.md) |
| US-0001 CA-09 | 500 problem+json só `type/title/status`, qualquer ambiente | [CT-0017](../casos-teste/CT-0017-l12-1-500-injetado.md), [CT-0021](../casos-teste/CT-0021-l12-5-500-development.md), [CT-0024](../casos-teste/CT-0024-logs-500-error.md) | — (só por injeção: proibido forçar no processo real) |
| US-0002 CA-01 | Valores brutos = mesma consulta; formatação local adicional | [CT-0026](../casos-teste/CT-0026-portal-ca01-valores-brutos.md) | [CT-0041](../casos-teste/CT-0041-man-ponta-a-ponta-portal-api.md) |
| US-0002 CA-02 | Distinguível sem depender de cor (ícone, "API operacional", "Saudável", borda) | [CT-0027](../casos-teste/CT-0027-portal-ca02-indicadores-textuais.md) | [CT-0040](../casos-teste/CT-0040-man-ca02-sem-cor.md) |
| US-0002 CA-03 | Erro (a) e (b) genérico; (b) sem versão/timestamp; timeout 5 s sem retry | [CT-0028](../casos-teste/CT-0028-portal-ca03-erro-caso-a.md), [CT-0029](../casos-teste/CT-0029-portal-ca03-erro-caso-b-503.md) | [CT-0039](../casos-teste/CT-0039-man-cors-real-navegador.md), [CT-0041](../casos-teste/CT-0041-man-ponta-a-ponta-portal-api.md) |
| US-0002 CA-04 | Carregando; valores anteriores removidos do DOM | [CT-0030](../casos-teste/CT-0030-portal-ca04-carregando-remove-dom.md) | [CT-0041](../casos-teste/CT-0041-man-ponta-a-ponta-portal-api.md) |
| US-0002 CA-05 | Recuperação pelo "Atualizar status" | [CT-0031](../casos-teste/CT-0031-portal-ca05-recuperacao.md) | [CT-0041](../casos-teste/CT-0041-man-ponta-a-ponta-portal-api.md) |
| US-0002 CA-06 | Só texto; sem dado sensível em nenhum estado | [CT-0032](../casos-teste/CT-0032-portal-ca06-texto-sem-html.md) | [CT-0041](../casos-teste/CT-0041-man-ponta-a-ponta-portal-api.md) |

## 8. Cobertura das obrigações técnicas
| Obrigação | CT | Observação |
|---|---|---|
| **R2** — `format: date-time` no contrato, com controle negativo | [CT-0004](../casos-teste/CT-0004-r2-format-date-time-controle-negativo.md) (+ [CT-0049](../casos-teste/CT-0049-verificacao-suite-fs.md) mutação c) | `2026-02-31T10:00:00.000Z` tem de ser reprovado |
| **R3** — itens PV do D8 + item 1 | item 1: [CT-0006](../casos-teste/CT-0006-versao-igual-csproj-sem-build.md), [CT-0037](../casos-teste/CT-0037-bb-versao-tripla.md) · item 2 (404/405/500): [CT-0008](../casos-teste/CT-0008-metodos-nao-permitidos-405.md), [CT-0011](../casos-teste/CT-0011-rota-inexistente-404.md), [CT-0017](../casos-teste/CT-0017-l12-1-500-injetado.md) · item 3: [CT-0003](../casos-teste/CT-0003-timestamp-formato-relogio-injetado.md) · item 4: [CT-0001](../casos-teste/CT-0001-get-health-200-tres-campos.md) · item 5: [CT-0008](../casos-teste/CT-0008-metodos-nao-permitidos-405.md), [CT-0009](../casos-teste/CT-0009-head-tolerado.md), [CT-0010](../casos-teste/CT-0010-preflight-options-204.md) · item 6: [CT-0012](../casos-teste/CT-0012-cabecalhos-em-toda-resposta.md), [CT-0035](../casos-teste/CT-0035-bb-server-e-cabecalhos.md) · item 8: [CT-0014](../casos-teste/CT-0014-cors-origem-permitida-e-negada.md), [CT-0015](../casos-teste/CT-0015-cors-fail-closed.md), [CT-0039](../casos-teste/CT-0039-man-cors-real-navegador.md) · item 9: [CT-0021](../casos-teste/CT-0021-l12-5-500-development.md) · item 10: [CT-0038](../casos-teste/CT-0038-man-encerramento-gracioso-503.md) (+ gancho [CT-0018](../casos-teste/CT-0018-l12-2-503-injetado.md)) · item 11: [CT-0019](../casos-teste/CT-0019-l12-3-negativo-canais-proibidos.md), [CT-0020](../casos-teste/CT-0020-l12-4-fabrica-sem-override-200.md), [CT-0022](../casos-teste/CT-0022-l12-6-superficie-endpoints.md) · item 12: [CT-0005](../casos-teste/CT-0005-r5-ancora-z-controle-negativo.md) | Item 7 (`X-Request-Id`, sem marca): [CT-0013](../casos-teste/CT-0013-x-request-id.md) |
| **R5** — `\z`, com controle negativo | [CT-0005](../casos-teste/CT-0005-r5-ancora-z-controle-negativo.md) (+ [CT-0049](../casos-teste/CT-0049-verificacao-suite-fs.md) mutação b) | `\n` final reprovado em `version`, `timestamp` e UUID |
| **L-12** (DEC-ARQ-0011 §6) | nº 1 [CT-0017](../casos-teste/CT-0017-l12-1-500-injetado.md) · nº 2 [CT-0018](../casos-teste/CT-0018-l12-2-503-injetado.md) · nº 3 [CT-0019](../casos-teste/CT-0019-l12-3-negativo-canais-proibidos.md) (+ [CT-0036](../casos-teste/CT-0036-bb-negativo-forcar-falha.md)) · nº 4 [CT-0020](../casos-teste/CT-0020-l12-4-fabrica-sem-override-200.md) · nº 5 [CT-0021](../casos-teste/CT-0021-l12-5-500-development.md) · nº 6 [CT-0022](../casos-teste/CT-0022-l12-6-superficie-endpoints.md) | — |
| **D8 item 13** (logs; parecer G3 v1.2 §9.2) | (a) [CT-0023](../casos-teste/CT-0023-logs-200-debug.md) · (b) [CT-0024](../casos-teste/CT-0024-logs-500-error.md) · (c) [CT-0025](../casos-teste/CT-0025-logs-denylist.md) | Escopo de categorias: L-PT-13 |
| **SCA** (DEC-ARQ-0009 v1.1 itens 1–2) | [CT-0045](../casos-teste/CT-0045-sca-api-nuget.md), [CT-0046](../casos-teste/CT-0046-sca-portal-npm-audit.md) | Código de saída do `dotnet list package` não é oráculo; parse do JSON |
| **SAST/estática** (itens 3–4; DEC-ARQ-0008) | [CT-0047](../casos-teste/CT-0047-sast-estatica-api-portal.md) | `angular-eslint` não é SAST (limite declarado) |
| **Testes dirigidos de segurança** (item 5) | [CT-0016](../casos-teste/CT-0016-denylist-corpo-cabecalhos.md), [CT-0019](../casos-teste/CT-0019-l12-3-negativo-canais-proibidos.md), [CT-0021](../casos-teste/CT-0021-l12-5-500-development.md), [CT-0025](../casos-teste/CT-0025-logs-denylist.md), [CT-0032](../casos-teste/CT-0032-portal-ca06-texto-sem-html.md), [CT-0035](../casos-teste/CT-0035-bb-server-e-cabecalhos.md), [CT-0036](../casos-teste/CT-0036-bb-negativo-forcar-falha.md) | — |
| **Cobertura** (DEC-ARQ-0007 v1.1 A4/W3) | [CT-0043](../casos-teste/CT-0043-cobertura-api-coverlet.md), [CT-0044](../casos-teste/CT-0044-cobertura-portal-vitest.md) | 80% de linhas; ramos/funções/statements reportados |
| **p95 indicativo** (DEC-ARQ-0010) | [CT-0042](../casos-teste/CT-0042-p95-indicativo.md) | Não é SLO; não bloqueia aceite |
| **Regressão R3** | [CT-0048](../casos-teste/CT-0048-regressao-verify-local-completo.md) | Suíte = esta entrega |
| **CT manuais no navegador** | CA-02 sem cor [CT-0040](../casos-teste/CT-0040-man-ca02-sem-cor.md) · CORS real [CT-0039](../casos-teste/CT-0039-man-cors-real-navegador.md) · encerramento gracioso real [CT-0038](../casos-teste/CT-0038-man-encerramento-gracioso-503.md) · ponta a ponta [CT-0041](../casos-teste/CT-0041-man-ponta-a-ponta-portal-api.md) | CT-0038 depende do spike R4 |

## 9. Sequência e dependências
1. **Agora (fase PT+CT, liberada após G3 + R1 — DEC-PO-0009):** este PT e os CT vão ao FS **antes do PR** da TASK-0008 (a R3 exige os casos PV antes do G4) e ao CR para o checklist do G4.
2. **Após o G4:** execução (1º ciclo), registro de BUG, 2º ciclo se houver, PQ-nnnn (ID a reservar na execução).
3. Estimativa da TASK-0010: **33 h (23,5–40 h)** — parecer G2 v1.2.

## 10. Riscos
| Risco | Prob./Impacto | Mitigação |
|---|---|---|
| Itens PV nunca exercidos; defaults do ASP.NET Core divergem do contrato | Média-alta / alto | Casos PV antes do PR; sondas black-box; 2º ciclo previsto |
| CA-07 depende do spike R4 | Média / alto no CA | CT-0038 condicionado; inviabilidade volta ao PO |
| Curva de capacitação (RM-0002) de FS/QA/CR | Média-alta / médio | Núcleo antes da atividade; revisão do CR e do ARQ |
| SCA sem rede ou NU1900 | Média / médio | Rede na execução; sem SCA válida o PQ não é favorável pleno |
| jsdom não prova distinção sem cor | Alta / baixo | CT-0040 manual |
| Testar versão diferente da do G4 | Baixa / alto | SHA do G4 no PQ e em cada evidência |

## 11. Lacunas (não decididas pela QA; enviadas aos donos)
| ID | Lacuna | Dono |
|---|---|---|
| L-PT-01 | Reserva de PT-0001 e CT-0001..CT-0049 gravada pela QA em `registro-ids.yaml` (EL-08) **no ramo** `doc/TASK-0010-pt-ct`; só vale na `main` após o merge do ORQ (risco de colisão baixo: só a QA cria PT/CT) | ORQ (merge) |
| L-PT-02 | Não há modelo de PT/CT em `modelos/`: usados o frontmatter padrão e a estrutura deste documento | DOC (modelo, se quiser) |
| L-PT-03 | Comportamento de `OPTIONS /health` **sem** cabeçalhos de preflight não definido (D8 item 5: "204 só no preflight"; ET RT-16) | ARQ/AS |
| L-PT-04 | Duração da janela de drenagem no encerramento gracioso não definida (D8 item 10, PS-05); o `stop-local.sh` faz SIGKILL após 10 s; spike R4 pendente | ARQ/FS (OPS) |
| L-PT-05 | Forma de servir o Portal numa origem não permitida para o CORS real (CT-0039), sem ferramenta nova | OPS/FS |
| L-PT-06 | A box tem Google Chrome (`/usr/bin/google-chrome`, base Chromium), não Chromium puro; não há leitor de tela real nem outros navegadores. A UX-0001 (4.1.3 e orientação à QA, item 3) pede "leitor de tela real, outros navegadores e zoom 400%" — isso vai além dos CA; zoom 400% é feito no CT-0040 se o UX/PO confirmarem; leitor de tela e outros navegadores ficam fora até decisão do UX/PO | UX/PO |
| L-PT-07 | `dotnet` não está no PATH do shell da QA (instalação do OPS em `~/.dotnet`, verificada pelo ORQ: 10.0.404) | OPS |
| L-PT-08 | DEC-PO-0009 (Opção A; PT+CT depende de G3 + R1): ID reservado em `7d85a6e` e conteúdo no plano G2 v1.2, que está **em-revisão** (a v1.1 segue vigente até o ORQ registrar a decisão). Não há registro próprio da decisão; este PT a cita pelo plano e pelo `historico.md` (15:26) | PO (ORQ registra) |
| L-PT-09 | Timeout real de 5 s (CE-04) só é verificado em jsdom com relógio simulado (CT-0028); não há servidor lento sem ferramenta nova. Verificação real fica limitada à API parada (conexão recusada, CT-0041) | QA registra; ARQ ciente |
| L-PT-10 | Valores de porta/origem (127.0.0.1, 8080, 4200 — MSG FS→OPS; parecer OPS v2.1) ficam no `.env`; este PT usa só os nomes das variáveis | OPS/FS |
| L-PT-11 | CT-0022: se o FS mapear `OPTIONS` como endpoint explícito, a superfície muda; aceitar ou não é do ARQ | ARQ |
| L-PT-12 | US-0001 CA-04: "igual à tag, quando houver". Normalmente não há tag no G5 (a tag é do release); no G5 a QA compara com o `.csproj` e registra "sem tag" (CT-0037). Comparação com a tag só se existir na SHA do G4 | QA registra; PO ciente |
| L-PT-13 | Oráculo D8 13(a) "nenhum Information/Warning/Error dessa requisição": não diz se vale só para as categorias da aplicação ou também para as do framework (o ASP.NET Core registra, por padrão, início/fim de requisição em Information na categoria de hosting). A QA não decide o escopo | ARQ |



## 12. Índice dos CT
| CT | Título | Tipo | Rastreio |
|---|---|---|---|
| [CT-0001](../casos-teste/CT-0001-get-health-200-tres-campos.md) | GET /health responde 200 com exatamente os três campos | AUT-API | US-0001 CA-01; ADR-0001 v2 D8 item 4 (PV); ET RT-02 |
| [CT-0002](../casos-teste/CT-0002-status-ok.md) | Status saudável = "ok" | AUT-API | US-0001 CA-02; ET RT-03 |
| [CT-0003](../casos-teste/CT-0003-timestamp-formato-relogio-injetado.md) | Timestamp com 3 casas, UTC e Z, a partir do TimeProvider injetado | AUT-API | US-0001 CA-03; ADR-0001 v2 D8 item 3 (PV); ET RT-05, PS-07 |
| [CT-0004](../casos-teste/CT-0004-r2-format-date-time-controle-negativo.md) | R2: validação do timestamp com format: date-time e controle negativo do validador | AUT-API | Ressalva R2 do G3; US-0001 CA-03; ET PS-09 |
| [CT-0005](../casos-teste/CT-0005-r5-ancora-z-controle-negativo.md) | R5: âncora \z nas expressões .NET, com controle negativo de \n final | AUT-API | Ressalva R5 do G3; ADR-0001 v2 D8 item 12 (PV); US-0001 CA-03, CA-04 |
| [CT-0006](../casos-teste/CT-0006-versao-igual-csproj-sem-build.md) | Versão = <Version> do .csproj, SemVer sem +build | AUT-API | US-0001 CA-04; ADR-0001 v2 D8 item 1 (V; caso obrigatório pela R3); ADR-0002 v1.1; ET RT-04, PS-02 |
| [CT-0007](../casos-teste/CT-0007-somente-leitura-chamadas-repetidas.md) | Somente leitura: chamadas repetidas na mesma instância | AUT-API | US-0001 CA-06; ET CE-12 |
| [CT-0008](../casos-teste/CT-0008-metodos-nao-permitidos-405.md) | Métodos não permitidos ⇒ 405 com Allow: GET, HEAD e problem+json | AUT-API | US-0001 CA-08; ADR-0001 v2 D8 itens 2 e 5 (PV); ET RT-07, RT-08, CE-07 |
| [CT-0009](../casos-teste/CT-0009-head-tolerado.md) | HEAD /health: mesmo código e cabeçalhos do GET, sem corpo | AUT-API | US-0001 CA-08; ADR-0001 v2 D8 item 5 (PV); ET RT-16, CE-10 |
| [CT-0010](../casos-teste/CT-0010-preflight-options-204.md) | Preflight OPTIONS ⇒ 204 com métodos GET, HEAD | AUT-API | ADR-0001 v2 D8 itens 5 e 8 (PV); ET RT-16, CE-11 (fora do aceite dos CA) |
| [CT-0011](../casos-teste/CT-0011-rota-inexistente-404.md) | Rota inexistente ⇒ 404 problem+json padrão do serviço | AUT-API | ADR-0001 v2 D8 itens 2 e 6 (PV, cobertura 404); ET RT-08, RT-09, CE-09 (fora do aceite dos CA) |
| [CT-0012](../casos-teste/CT-0012-cabecalhos-em-toda-resposta.md) | no-store e nosniff em toda resposta | AUT-API | US-0001 CA-05; ADR-0001 v2 D8 item 6 (PV); ET RT-09 |
| [CT-0013](../casos-teste/CT-0013-x-request-id.md) | X-Request-Id: devolve UUID canônico válido; senão gera v4; nunca 400 | AUT-API | ADR-0001 v2 D8 item 7; ET RT-09, L-03; US-0001 CA-05 (sem eco de valor inválido) |
| [CT-0014](../casos-teste/CT-0014-cors-origem-permitida-e-negada.md) | CORS: origem permitida recebe ACAO exata; origem negada sem ACAO e sem 403 | AUT-API | ADR-0001 v2 D8 item 8 (PV); ET RT-10, CE-08, L-06 |
| [CT-0015](../casos-teste/CT-0015-cors-fail-closed.md) | CORS fail closed: origem ausente, inválida ou * impede a inicialização | AUT-API | ADR-0001 v2 D8 item 8 (PV); ET RT-10 |
| [CT-0016](../casos-teste/CT-0016-denylist-corpo-cabecalhos.md) | Denylist: nenhum dado sensível em corpo e cabeçalhos (200, 405, 503, 500) | AUT-API | US-0001 CA-05; RN-0001; REQ-0004; ET RT-12, CE-13, CE-14 |
| [CT-0017](../casos-teste/CT-0017-l12-1-500-injetado.md) | L-12 nº 1: 500 por falha injetada — status, Content-Type, corpo exato e cabeçalhos | AUT-API | DEC-ARQ-0011 §6 (1); US-0001 CA-09, CA-05; ADR-0001 v2 D8 item 2 |
| [CT-0018](../casos-teste/CT-0018-l12-2-503-injetado.md) | L-12 nº 2: 503 por estado injetado — esquema e sem Retry-After | AUT-API | DEC-ARQ-0011 §6 (2); US-0001 CA-07 (gancho de teste), CA-03; RN-0002; ET RT-06 |
| [CT-0019](../casos-teste/CT-0019-l12-3-negativo-canais-proibidos.md) | L-12 nº 3: query, cabeçalho ou variável de ambiente não forçam 503/500 | AUT-API | DEC-ARQ-0011 §6 (3) e §3; US-0001 CA-05; REQ-0004; ADR-0001 v2 D8 item 11 |
| [CT-0020](../casos-teste/CT-0020-l12-4-fabrica-sem-override-200.md) | L-12 nº 4: fábrica sem override responde 200 (composição de produção sem gancho) | AUT-API | DEC-ARQ-0011 §6 (4); ADR-0001 v2 D8 item 11 |
| [CT-0021](../casos-teste/CT-0021-l12-5-500-development.md) | L-12 nº 5: corpo do 500 sem detalhe com ASPNETCORE_ENVIRONMENT=Development | AUT-API | DEC-ARQ-0011 §6 (5) e §5; ADR-0001 v2 D8 item 9 (PV); US-0001 CA-09 |
| [CT-0022](../casos-teste/CT-0022-l12-6-superficie-endpoints.md) | L-12 nº 6: superfície registrada = só /health (GET/HEAD) e preflight | AUT-API | DEC-ARQ-0011 §6 (6), §3–4; ADR-0001 v2 D8 item 11 |
| [CT-0023](../casos-teste/CT-0023-logs-200-debug.md) | Logs (D8 item 13a): 200 gera Debug correlacionado ao X-Request-Id e nenhum Information/Warning/Error | AUT-API | ADR-0001 v2 D8 item 13; parecer G3 v1.2 §9.2 (3); ET RT-15 |
| [CT-0024](../casos-teste/CT-0024-logs-500-error.md) | Logs (D8 item 13b): 500 injetado gera Error e o corpo segue só type/title/status | AUT-API | ADR-0001 v2 D8 item 13; parecer G3 v1.2 §9.2 (3); DEC-ARQ-0011 |
| [CT-0025](../casos-teste/CT-0025-logs-denylist.md) | Logs (D8 item 13c): nenhum item da denylist em 200, 503 e 500 | AUT-API | ADR-0001 v2 D8 item 13; parecer G3 v1.2 §9.2 (3); US-0001 CA-05; RN-0001 |
| [CT-0026](../casos-teste/CT-0026-portal-ca01-valores-brutos.md) | Portal: estado saudável exibe os valores brutos da mesma consulta | AUT-WEB | US-0002 CA-01; UX-0001 D-UX-05, D-UX-08; ET §5 itens 3 e 7 |
| [CT-0027](../casos-teste/CT-0027-portal-ca02-indicadores-textuais.md) | Portal: saudável distinguível por ícone, título, selo e borda (parte automatizável) | AUT-WEB | US-0002 CA-02; UX-0001 D-UX-04 |
| [CT-0028](../casos-teste/CT-0028-portal-ca03-erro-caso-a.md) | Portal: erro caso (a) — rede, timeout de 5 s, HTTP inesperado, corpo inválido | AUT-WEB | US-0002 CA-03 (a); RN-0002; RN-0001; ET RT-13, §5 item 2, CE-03..06 |
| [CT-0029](../casos-teste/CT-0029-portal-ca03-erro-caso-b-503.md) | Portal: erro caso (b) — 503 válido não exibe versão nem timestamp | AUT-WEB | US-0002 CA-03 (b); UX-0001 D-UX-03 / RE-02 (DEC-PO-0005) |
| [CT-0030](../casos-teste/CT-0030-portal-ca04-carregando-remove-dom.md) | Portal: carregando remove valores anteriores do DOM | AUT-WEB | US-0002 CA-04; UX-0001 D-UX-02, D-UX-07 |
| [CT-0031](../casos-teste/CT-0031-portal-ca05-recuperacao.md) | Portal: recuperação do erro pelo botão Atualizar status | AUT-WEB | US-0002 CA-05; UX-0001 D-UX-07 |
| [CT-0032](../casos-teste/CT-0032-portal-ca06-texto-sem-html.md) | Portal: valores só como texto e sem dados sensíveis em nenhum estado | AUT-WEB | US-0002 CA-06; RN-0001; REQ-0004; ET §5 item 5 |
| [CT-0033](../casos-teste/CT-0033-bb-contrato-kestrel-real.md) | Black-box: contrato no Kestrel real (GET, HEAD, métodos, 404, preflight) | QA-BB | US-0001 CA-01, CA-02, CA-08; ADR-0001 v2 D8 itens 2, 4, 5 (PV) |
| [CT-0034](../casos-teste/CT-0034-bb-timestamp-tolerancia.md) | Black-box: timestamp dentro de ±5 s do instante de recebimento | QA-BB | US-0001 CA-03; DEC-AS-0002; ET RT-05 |
| [CT-0035](../casos-teste/CT-0035-bb-server-e-cabecalhos.md) | Black-box: sem cabeçalho Server e com no-store/nosniff em toda resposta | QA-BB | US-0001 CA-05; ADR-0001 v2 D8 item 6 (PV); ET PS-04, RT-09 |
| [CT-0036](../casos-teste/CT-0036-bb-negativo-forcar-falha.md) | Black-box: tentativas externas de forçar 503/500 não alteram o 200 | QA-BB | DEC-ARQ-0011 §3 e §6 (3); US-0001 CA-05; REQ-0004 |
| [CT-0037](../casos-teste/CT-0037-bb-versao-tripla.md) | Black-box: versão da resposta = <Version> do .csproj (= tag, quando houver) | QA-BB | US-0001 CA-04; ADR-0002 v1.1; ADR-0001 v2 D8 item 1 |
| [CT-0038](../casos-teste/CT-0038-man-encerramento-gracioso-503.md) | Manual: encerramento gracioso real responde 503 na janela de drenagem | QA-MAN | US-0001 CA-07; ADR-0001 v2 D8 item 10 (PV); ET PS-05, §7.2; ressalva R4 do G3 |
| [CT-0039](../casos-teste/CT-0039-man-cors-real-navegador.md) | Manual: CORS real no navegador — origem permitida e origem não permitida | QA-MAN | ADR-0001 v2 D8 item 8 (PV); ET CE-08, RT-10; US-0002 CA-03 (a) |
| [CT-0040](../casos-teste/CT-0040-man-ca02-sem-cor.md) | Manual: estados distinguíveis sem depender de cor | QA-MAN | US-0002 CA-02; UX-0001 D-UX-04; WCAG 1.4.1 |
| [CT-0041](../casos-teste/CT-0041-man-ponta-a-ponta-portal-api.md) | Manual: ponta a ponta Portal↔API (CA-01, CA-03, CA-04, CA-05, CA-06) | QA-MAN | US-0002 CA-01, CA-03, CA-04, CA-05, CA-06 |
| [CT-0042](../casos-teste/CT-0042-p95-indicativo.md) | p95 indicativo ≤ 100 ms (DEC-ARQ-0010) | QA-BB | DEC-ARQ-0010; ET RT-14; matriz R3 (desempenho); não é CA |
| [CT-0043](../casos-teste/CT-0043-cobertura-api-coverlet.md) | Cobertura da API ≥ 80% de linhas (Coverlet) | QA-EVID | DEC-ARQ-0007 v1.1 A4 |
| [CT-0044](../casos-teste/CT-0044-cobertura-portal-vitest.md) | Cobertura do Portal ≥ 80% de linhas (@vitest/coverage-v8) | QA-EVID | DEC-ARQ-0007 v1.1 W3; parecer G3 v1.2 §9.2 (1) |
| [CT-0045](../casos-teste/CT-0045-sca-api-nuget.md) | SCA da API: NuGet Audit no restore e JSON do dotnet list package | QA-EVID | DEC-ARQ-0009 v1.1 item 1; DEC-ARQ-0007 v1.1 A1 e A5 |
| [CT-0046](../casos-teste/CT-0046-sca-portal-npm-audit.md) | SCA do Portal: npm audit sem alta/crítica | QA-EVID | DEC-ARQ-0009 v1.1 item 2; DEC-ARQ-0007 W1, W5 |
| [CT-0047](../casos-teste/CT-0047-sast-estatica-api-portal.md) | SAST/análise estática no recorte da DEC-ARQ-0009 | QA-EVID | DEC-ARQ-0009 v1.1 itens 3 e 4; DEC-ARQ-0008; DEC-ARQ-0007 A2, A3, W2 |
| [CT-0048](../casos-teste/CT-0048-regressao-verify-local-completo.md) | Regressão R3: verify-local completo e suíte 100% na SHA do G4 | QA-EVID | Matriz R3 (regressão completa); critérios do PQ; DEC-ARQ-0007 |
| [CT-0049](../casos-teste/CT-0049-verificacao-suite-fs.md) | Verificação da suíte do FS: rastreio por CT e mutações de controle | QA-EVID | DEC-ARQ-0011 v1.1 (opção A); DEC-PO-0009; ressalvas R2, R3, R5 |

## Histórico
| Versão | Data/hora (America/Sao_Paulo) | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 15:35 | QA | Criação: 49 CT, matriz CA → CT, critérios de entrada/saída do G5 |
