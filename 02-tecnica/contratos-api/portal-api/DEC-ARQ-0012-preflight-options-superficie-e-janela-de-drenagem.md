---
id: DEC-ARQ-0012
titulo: "OPTIONS fora do preflight (L-PT-03), preflight e a superfície do CT-0022 (L-PT-11) e janela de drenagem do encerramento gracioso (L-PT-04)"
tipo: dec
versao: 1.1
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:54-03:00
atualizado_em: 2026-11-26T16:02-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0007, TASK-0008, TASK-0010, TASK-0012, PT-0001, CT-0008, CT-0010, CT-0018, CT-0022, CT-0038, ADR-0001, ADR-0003, DEC-ARQ-0002, DEC-ARQ-0011, ET-0001, US-0001, L-PT-03, L-PT-04, L-PT-11, R4]
substitui: null
substituido_por: null
---

# DEC-ARQ-0012 — OPTIONS fora do preflight, superfície com preflight e janela de drenagem

> [TESTE] Decide as lacunas L-PT-03, L-PT-11 e L-PT-04 do PT-0001 v1.1 (§11), pedidas pela QA e formalizadas pelo ORQ. **Não é N3** (sem exposição nova, sem custo). **Não altera o conjunto de status, esquemas, operações nem o `info.version` (1.0.0) do OpenAPI.** A prosa do `/health` foi alinhada editorialmente na v1.1 (revisão da AS no PR #4). O §1 é um **esclarecimento de caso não previsto** (ver "Impacto em outros artefatos"). As medições vêm de um protótipo descartável do ARQ, **que não é o spike R4**: `07-agentes/07-arq/evidencias-lacunas-pt-0001/`.

## 1. OPTIONS e preflight (L-PT-03)
**Definição de preflight** (documentação oficial do CORS no ASP.NET Core e código do `CorsMiddleware`/`CorsService`, consultados em 26/11/2026): requisição `OPTIONS` **com** `Origin` **e** `Access-Control-Request-Method`. Sem esses dois cabeçalhos, não é preflight.

| Caso | Resposta decidida | Fundamento |
|---|---|---|
| **Preflight, origem permitida** (a configurada) | `204`, sem corpo; `Access-Control-Allow-Origin` = origem exata; `Access-Control-Allow-Methods` = {`GET`, `HEAD`}; sem `Allow-Credentials` e sem `Allow-Headers`; mais os cabeçalhos do ADR-0001 v2 D8 item 6 (`no-store`, `nosniff`) | DEC-ARQ-0002 L-02; ET RT-16; medido (evidência 01) |
| **Preflight, origem não permitida** | `204`, **sem** `Access-Control-Allow-Origin` e **sem** `Allow-Methods`; **nunca 403** | D8 item 8 (L-06); a documentação oficial diz que o preflight negado retorna 204 sem os cabeçalhos CORS; medido |
| **`OPTIONS` que não é preflight** (sem `Origin`, ou sem `Access-Control-Request-Method`, ou nenhum dos dois) | **`405`** com `Allow: GET, HEAD`, `Content-Type: application/problem+json`, corpo exato `{type: "about:blank", title: "Method Not Allowed", status: 405}` e os cabeçalhos do D8 item 6 — **igual a qualquer método não permitido** | D8 item 5: "`OPTIONS` ⇒ 204 **só** no preflight"; medido: o framework responde `405` + `Allow: GET, HEAD` (evidência 01) |

Observações medidas (protótipo, .NET 10.0.15, Kestrel): (i) `Access-Control-Allow-Methods` sai como `GET,HEAD` **sem espaço** (o `Allow` do 405 sai `GET, HEAD` com espaço); como o valor é lista separada por vírgulas (RFC 9110, espaço opcional), **o oráculo compara como conjunto**, não como texto literal; (ii) `OPTIONS` com `Origin` permitido e sem `Access-Control-Request-Method` recebe `405` **com** `Access-Control-Allow-Origin` (o CORS é aplicado à resposta de um pedido que não é preflight): o teste **não** deve exigir ausência de ACAO nesse caso; (iii) o preflight **termina no middleware de CORS**, antes do endpoint; por isso os cabeçalhos do D8 item 6 do preflight dependem de um middleware de cabeçalhos padrão **anterior** ao CORS na composição.

**Oráculo (CT-0010 e o caso novo de `OPTIONS` sem preflight, que a QA cria no PT — não crio CT):**
1. Preflight permitido: `204`, corpo vazio, ACAO = origem exata, ACAM como conjunto = {GET, HEAD}, sem `Allow-Credentials`/`Allow-Headers`, `Cache-Control: no-store`, `X-Content-Type-Options: nosniff`.
2. Preflight com origem diferente: `204`, sem ACAO e sem ACAM, status ≠ 403.
3. `OPTIONS /health` sem cabeçalhos; com só `Origin`; com só `Access-Control-Request-Method`: `405`, `Allow` = {GET, HEAD} (conjunto), `application/problem+json`, corpo exato, `no-store`, `nosniff`; nenhum `204`.

**Impacto em outros artefatos (esclarecimento; AS e PO com ciência):** a frase "`OPTIONS` não deve responder `405`" (DEC-ARQ-0002 L-02; ET-0001 RT-16 e CE-11) é lida como referente **ao preflight CORS** — esses trechos descrevem o preflight, e o D8 item 5 (aceito) já restringe o `204` ao preflight. Nenhum CA, esquema, status ou exemplo muda; o `405` com `Allow: GET, HEAD` já é contrato. A AS, na revisão do PR #4, confirmou que o §1 **não muda o comportamento prometido** e que não há conflito com CA. **Prosa do OpenAPI (v1.1):** alinhada neste ramo — o preflight (`Origin` + `Access-Control-Request-Method`) responde `204` (origem negada: `204` sem cabeçalhos CORS, nunca 403) e **não** responde `405`; o `OPTIONS` que não é preflight responde `405` com `Allow: GET, HEAD` e ProblemDetails. `info.version` permanece 1.0.0. **ET-0001:** a v1.5 editorial (RT-16, CE-11 e, no mesmo recorte, §4.1 e L-02) permanece com a AS, em PR próprio depois do merge, como ela propôs; o ARQ confirma esse recorte.

## 2. O preflight não é endpoint — superfície do CT-0022 (L-PT-11)
**Decisão:** o preflight é tratado **pelo middleware de CORS** e **não conta como endpoint**. A superfície registrada é **exatamente dois endpoints**: `GET /health` e `HEAD /health`.
- **Reprova o CT-0022:** qualquer mapeamento explícito de `OPTIONS` (`MapMethods("OPTIONS")`, `[HttpOptions]`, `MapFallback`/rota coringa que responda `OPTIONS`) e qualquer endpoint além dos dois.
- **Aceitas** as duas formas de habilitar o CORS embutido, com o mesmo comportamento medido e sem endpoint de `OPTIONS` em nenhuma: `UseCors(política)` global depois de `UseRouting`, ou `RequireCors(política)` no `/health` (evidência 02).
- O endpoint de rejeição `405` do roteamento é criado dinamicamente pelo *matcher* e **não** aparece no `EndpointDataSource`; não conta.
- **Oráculo (CT-0022):** enumerar os `RouteEndpoint` do `EndpointDataSource` da fábrica de produção e verificar que o conjunto de pares (padrão de rota, método HTTP) é igual a {(`/health`, `GET`), (`/health`, `HEAD`)} e que nenhum endpoint declara `OPTIONS`.

## 3. Janela de drenagem do encerramento gracioso (L-PT-04; liga ao R4 e ao CA-07)
**Fatos oficiais** (https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0, consultada em 26/11/2026; código de `Host.StopAsync`): no encerramento o host (1) dispara os manipuladores de `ApplicationStopping`, (2) **para o servidor**, que desabilita novas conexões e espera as requisições em curso "enquanto o tempo de encerramento permitir", (3) dispara `ApplicationStopped`. `HostOptions.ShutdownTimeout`: **padrão 30 s** (era 5 s até o .NET 5). Logo, o listener fica no ar enquanto o manipulador de `ApplicationStopping` estiver rodando.

**Medições do protótipo (indicativas; evidência 04):**
- Com um manipulador de `ApplicationStopping` que marca "encerrando" e **bloqueia 3 s**: 15 de 15 sondagens (a cada 200 ms) receberam `503` em 0,07–2,9 s; depois, listener fechado; processo saiu sozinho em ≈ 3,1 s, código de saída 0.
- **Sem** janela: a primeira sondagem já falha (conexão derrubada) e nenhum `503` aparece (saída em 0,22 s) — confirma que o `503` do CA-07 **só existe** com janela explícita (PS-05).
- A **janela deve ser implementada no `ApplicationStopping`.** Esperar dentro de `IHostedService.StopAsync` **não funciona**: o servidor já parou (0 respostas `503`; conexão recusada desde 0,02 s).
- Com **uma requisição de 30 s em curso** no SIGTERM: saída em ≈ `ShutdownTimeout` + 1 s (6,03 s com 5 s; 9,02 s com 8 s). Com o padrão de 30 s, o processo levaria ≈ 31 s e o `stop-local.sh` (SIGKILL após 10 s, parecer OPS v2.1) o mataria.
- O SIGTERM enviado ao PID do invólucro `dotnet run --no-build` alcançou o processo filho e o encerramento gracioso ocorreu (observado). O PID gravado em `run/` deve ser, de preferência, o do processo da API.

**Decisão:**
1. **Janela-alvo D = 3 s**, constante no código (sem chave de configuração nem variável de ambiente nova).
2. **`HostOptions.ShutdownTimeout` = 5 s**, definido **em código** na composição de produção (o padrão de 30 s excede a espera de 10 s do `stop-local.sh`).
3. **Relações obrigatórias:** `D < ShutdownTimeout`; `ShutdownTimeout + 2 s ≤` espera do `stop-local.sh` após SIGTERM (hoje 10 s; **se a OPS reduzir a espera, avisa o ARQ**). Folga atual: pior caso medido 6,03 s contra 10 s.
4. **Ajuste sem nova DEC:** FS/OPS podem ajustar D entre **2 s e 4 s** se registrarem a medição no spike R4 e mantiverem as relações do item 3. Fora disso, volta ao ARQ.
5. **Critério de aceite do spike R4 e do CT-0038 (substitui "duração não definida"):** com sondagem a cada ≤ 250 ms e SIGTERM pelo `stop-local.sh` real: (a) **≥ 1 `503`** válido (`status: "unavailable"`, esquema `HealthUnavailable`, sem `Retry-After`, sem detalhe) **antes** de a conexão ser recusada; (b) depois, conexão recusada; (c) o processo termina **sozinho em ≤ 8 s**, sem SIGKILL; (d) o `200` antes do sinal não muda. O número de `503` observado é registrado (esperado ≈ D ÷ intervalo), mas o mínimo do aceite é 1.
6. **O que o spike R4 precisa medir** (FS/OPS, sobre o código real): M1 tempo do SIGTERM ao 1º `503`; M2 quantidade de `503`; M3 instante do 1º "conexão recusada"; M4 tempo até a saída do processo e código de saída; M5 saída com uma requisição em curso (≤ `ShutdownTimeout` + 2 s); M6 que o sinal do `stop-local.sh` chega ao processo da API (PID de `run/`); M7 que o estado "encerrando" é a abstração injetada do DEC-ARQ-0011 (nunca controle remoto); M8 corpo e cabeçalhos do `503` conforme CT-0018. **O R4 continua aberto** até o FS/OPS registrarem isso no código real; o protótipo só mostra que a abordagem é viável no .NET 10.0.15/Linux.

**Responsabilidades:** FS implementa (TASK-0008) e mede com a OPS; OPS mantém a espera do `stop-local.sh` ≥ `ShutdownTimeout` + 2 s; QA ajusta o CT-0038 ao critério do item 5. Nenhum CA muda (CA-07 permanece).

## Verificação
CT-0010 (+ caso novo `OPTIONS` sem preflight), CT-0022, CT-0018 e CT-0038 (QA); suíte do FS (TASK-0008); CR confirma no G4 a ausência de endpoint `OPTIONS`; ARQ reconfirma na 2ª aprovação do G4.

## Histórico
| Versão | Data/hora (America/Sao_Paulo) | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 15:54 | ARQ | Criação (L-PT-03, L-PT-04, L-PT-11 do PT-0001 v1.1) |
| 1.1 | 26/11/2026 16:02 | ARQ | Prosa do OpenAPI alinhada ao §1 (revisão da AS no PR #4); status/esquemas/operações/`info.version` inalterados |
