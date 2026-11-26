---
id: PARECER-G2-DEM-2026-001-TASK-0012
titulo: "Parecer de planejamento do G2 — TASK-0012 (execução local, smoke, rollback e observação) — stack .NET + Angular"
tipo: parecer
versao: 2.1
status: em-revisao
dono: OPS
autores: [OPS]
aprovado_por: null
criado_em: 2026-11-26T12:56-03:00
atualizado_em: 2026-11-26T15:25-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0012, TASK-0008, TASK-0009, TASK-0010, PLANO-DEM-2026-001-G2, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-ARQ-0011, DEC-AS-0001, AH-0003, AH-0001, AH-0002, ET-0001, RM-0002]
substitui: "rascunho v1.1 (stack Node/Fastify; AH-0001; DEC-ARQ-0003..0006)"
substituido_por: null
---

# Parecer de planejamento G2 — TASK-0012 (OPS) — v2.1

> [TESTE] DEM-2026-001 · parecer de **planejamento** para o G2 (etapa C), **v2.1** (1º bloco fechado com o FS). Refeito na v2.0 após a **AH-0003** (Thiago, 26/11/2026 14:54, texto literal: “Aprovo AH-0003”) e o **ADR-0001 v2.0 aceito** na main (merge `d40518e`): C#/.NET 10 LTS + ASP.NET Core na `portal-api` e Angular 22.3 no front; Node 24 permanece só como ferramenta. Substitui o rascunho v1.1 (stack Node/Fastify da AH-0001, hoje substituída). Nada vai para produção. **Não** altera estado, etapa, gates, `contexto.yaml`, `historico.md`, `aprovacoes.md` nem `Tarefas.csv` (só o ORQ). Registrado em ramo próprio de `07-agentes/11-ops/` para o ORQ mesclar (`merge --no-ff`); a OPS não faz o merge.
>
> Horário: America/Sao_Paulo. Estado operacional: **Normal** (fase de testes internos). Fluxo 01, responsável do fluxo: PO. Classe de risco: **R3** (DEC-ARQ-0001, inalterada). Preparação da TASK-0012 **liberada** pelo ORQ (MSG-SOL, contexto v33/v34). Esqueleto da aplicação **não** é criado por este parecer nem por esta preparação (código do FS, ADR-0001 v2 D6).

## 0. Recuperação de contexto (5 linhas)

A demanda cria, do zero, o GET `/health` da API base do Portal e uma tela de status, só em execução local. O G2 v1.1 foi aprovado com observações; o G3 foi **aprovado com ressalvas** R1–R5 (26/11 15:08). A AH-0003 substituiu a AH-0001 e trocou a stack; o ARQ publicou e o ORQ mesclou o ADR-0001 v2.0 e as DEC-ARQ-0007..0010 (que **substituem** as 0003..0006). A preparação, suspensa às 14:52, foi **liberada**. Este parecer reestima a TASK-0012, descreve o impacto no `verify-local`, no p95 e na origem CORS, e registra a instalação do SDK .NET 10 e do Angular CLI 22.x na box (R4 do G3; também pré-requisito da RM-0002). Não há ambientes dev/hml, nem pipeline, nem versão anterior para rollback.

## 1. Resultado

A OPS **reestima** a TASK-0012 para a stack aceita e **não propõe alternativa** às DEC-ARQ-0007..0010. Estimativas em **horas** (mesma unidade de CR, QA e FS). A instalação da toolchain **já foi feita** nesta entrega; o ponto da preparação abaixo **inclui** esse esforço. O plano G2 vigente continua o v1.1 (`f61a1f9`); o PO monta o v1.2 com esta cifra (DEC-PO-0008 já decidiu não reabrir CA).

| Lote | Ponto para Tarefas.csv | Faixa | Quando |
|---|---|---|---|
| Preparação (toolchain, scripts de execução, artefato imutável, procedimento DEC-ARQ-0007, 1º bloco com o FS) | **10 h** | 8–13 h | Liberada; em paralelo à TASK-0008 |
| — já executado nesta entrega (instalação + evidência + rascunhos + este parecer + proposta ao FS) | **5 h** | — | 26/11/2026 |
| — saldo da preparação | **5 h** | 4–7 h | Após confirmação do FS e existência do esqueleto D6 |
| Validação G6/G7 (smoke, rollback ensaiado, pacote de pré-liberação e encerramento da observação) | **6 h** de trabalho ativo | 5–8 h | Após o G5, na versão aprovada no G4 |
| Janela de observação R3 | **24 h de calendário** (não é esforço) | — | Após o “deploy” local da versão candidata, no G7 |

**Delta em relação à v1.1 (Node):** preparação 8 h (6–10) → **10 h (8–13)**; G6/G7 5 h (4–7) → **6 h (5–8)**; a janela de 24 h **não muda**. Motivo: duas toolchains, `verify-local` com dez passos (A1–A5 + W1–W5), API em Release no p95, conferência de versão pelo `.csproj`, e a instalação do SDK/CLI (já realizada).

## 2. Estimativas e premissas

**Unidade:** horas. A escala 1–5 de `criterios-classificacao.md` é fator da demanda, não unidade desta TASK.

### 2.1 Preparação — 10 h (faixa 8–13 h)

| Item | Faixa | Conteúdo |
|---|---|---|
| Toolchain e registro do ambiente local | 2,5–3,5 h | Instalar SDK .NET 10 e Angular CLI 22.x por fontes oficiais, sem custo; desligar telemetria/analytics; evidência sanitizada; PATH persistente; documentar como subir API (Release) e Portal (`ng serve`) em processos separados, variáveis só por nome |
| Scripts de execução (raiz `scripts/`) | 3–4 h | `start-local.sh`, `stop-local.sh`, `check-version.sh`, `observe-local.sh`; fronteira com o FS (PR-01): OPS é dono de `scripts/` |
| Procedimento operacional do verify local (DEC-ARQ-0007) | 2,5–3,5 h | Script raiz com A1–A5 e W1–W5, evidência gitignorada, modo de reexecução pelo CR |
| Artefato imutável, p95 (DEC-ARQ-0010) e evidências | 1–2 h | Tag `portal-api-v<versão>` + `packages.lock.json` + `package-lock.json` (sem container, D5); `measure-p95.mjs` com API em Release; modelo de evidência sanitizada |

### 2.2 Validação G6/G7 — 6 h ativas (faixa 5–8 h) + 24 h de calendário

| Item | Faixa | Conteúdo |
|---|---|---|
| Pacote de pré-liberação (G6) | 1,5–2 h | Plano de rollback escrito, checagens de ambiente (SDK 10 + Node 24 + CLI), `check-version.sh` (`<Version>` do `.csproj` == tag == `GET /health`) |
| Ensaio de rollback | 1–1,5 h | Uma execução completa, com tempo cronometrado (parar os dois processos) |
| Smoke da versão candidata | 1–1,5 h | Caminho 200 da API e tela saudável/erro no Portal Angular (critério do plano) |
| Observação de 24 h (instrumentar, acompanhar, encerrar) | 1,5–2,5 h ativas | Amostragem local + relatório; a janela em si é calendário, não esforço |

Esta estimativa **não** inclui: implementação (TASK-0008), CR/G4, PT/CT/PQ (TASK-0010), documentação (TASK-0011), capacitação RM-0002 (fora desta DEM), nem qualquer operação em produção.

### 2.3 Premissas (se alguma cair, a faixa reabre)

- **ADR-0001 v2.0 aceito** na main (merge `d40518e`): .NET 10 LTS (`net10.0`), Angular 22.3, Node 24 só como ferramenta, monorepo `/workspace/projetos/portal/`, estrutura D6, configuração D7. Não há premissa de merge pendente.
- **AH-0003 aprovada** (26/11 14:54, “Aprovo AH-0003”), sem condições; AH-0001 substituída. Preparação **liberada** pelo ORQ.
- Toolchain **já instalada** na box desta entrega (versões em §9 e na evidência): SDK 10.0.404, ASP.NET Core 10.0.15, Angular CLI 22.3.0, Node 24.22.1, npm 11.21.1. Telemetria do dotnet e analytics do `ng` desligadas. Custo zero.
- Nada vai a produção; não há dev/hml; execução só na box, em loopback; sem pipeline, container, nuvem ou custo (D5).
- O **FS cria o esqueleto D6** e implementa os apps (TASK-0008). A OPS **não** cria código da aplicação. Os rascunhos desta preparação ficam em `rascunhos/ops/DEM-2026-001-TASK-0012-preparacao-dotnet/` até haver monorepo; os rascunhos Node anteriores permanecem só como histórico.
- A TASK-0008 ainda aguarda, no contexto v34, a confirmação do ARQ sobre o fechamento da R1 (ET-0001 v1.4 já na main, `9b3dc1b`; prosa do OpenAPI em ramo, merge pendente de confirmação) e o plano G2 v1.2. Isso **não** impede a conclusão dos rascunhos da OPS; impede o depósito e o ensaio N1 no monorepo até o esqueleto existir.
- Primeira entrega: **não há REL nem tag anterior**. O rollback da primeira versão é parar os processos (serviço ausente). Não há banco (DBA N/A).
- Observabilidade além de logs estruturados está fora desta fase (D5): a janela de 24 h usa ferramentas já presentes (`curl`, `dotnet`, `node`, utilitários do SO). Não invento painel, alerta ou APM.
- G6 formal também depende de documentação pronta (TASK-0011) e pré-aceite do PO; a OPS valida ambiente e rollback. Autorização de publicação em produção **não se aplica**.
- Calibração da cobertura 80% (Coverlet e `ng test --coverage`) é premissa do QA, como na DEC-ARQ-0007 item 2.
- A pergunta da CPO ao Thiago sobre o alcance da diretriz AH-0003 (contexto v33/v34) **não bloqueia** esta DEM; premissas registradas: Angular 22.x estável e C#/.NET só nas APIs do Portal Web. Se (b) ampliar, a faixa é reaberta só se a preparação desta demanda for afetada (hoje não é).

## 3. Sequência — confirmação

**Confirmo**, com o ajuste da AH-0003:

1. A **preparação** da TASK-0012 está **liberada** e corre em **paralelo à TASK-0008** (quando o FS puder iniciar).
2. A **validação formal** (smoke, rollback ensaiado no G6, observação de 24 h no G7) ocorre **depois do G5**, na mesma versão aprovada no G4 (PR-03).

**Ressalvas:**

- Subir os processos localmente para ajuste de script, na preparação, é N1 (teste em dev). Não é G7.
- Fronteira de artefatos (PR-01): FS é dono de `apps/portal-api/` e `apps/portal-web/` (incluindo `.csproj`, `Directory.Build.props`, lockfiles, `angular.json`, lint/test/build de cada app); OPS é dono de `/workspace/projetos/portal/scripts/` e da documentação operacional de ambiente/evidências (arquivos de evidência **fora** do git ou em diretório ignorado).
- Se uma nova AH ou o G3 residual mudar stack ou contrato, preparação, variáveis e este parecer são reavaliados antes de concluir a execução.

## 4. Procedimento proposto: observação de 24 h e rollback ensaiado (R3, ambiente local)

Ferramentas: o que as DEC/ADRs já pressupõem e o que está na box (`git`, SDK .NET 10.0.404, `node` v24.22.1, `npm` 11.21.1, Angular CLI 22.3.0, `curl`, `ps`/`uptime`). Sem pipeline. Runbook formal (RB-nnnn) será redigido na **execução** remanescente da TASK-0012 (OPS é dono de runbooks); até lá, o ensaio segue este procedimento. Rascunho: `scripts/observe-local.sh`.

### 4.1 Rollback ensaiado (G6, antes do “deploy” formal da candidata)

**Contexto da primeira entrega:** não existe tag `portal-api-v*` anterior nem REL anterior. Feature flag não está definida. Não há banco. Ordem de preferência: (1) flag — N/A; (2) voltar à versão anterior — na primeira REL, “versão anterior” = **processos parados**; (3) roll-forward — fora do ensaio; (4) backup — N/A.

**Passos (ensaio, uma vez, cronometrado):**

1. Garantir working tree limpa no commit da versão candidata (o mesmo que passará pelo G4/G5). Conferir `dotnet --version` (série 10), `node -v` (série 24) e o `global.json`.
2. Restaurar de forma reproduzível: `dotnet restore --locked-mode` na API e `npm ci` no Portal.
3. Subir API (**Release**) e Portal (`ng serve`, loopback) em processos separados, com variáveis **já definidas fora do git** (seção 5), via `scripts/start-local.sh`. Registrar PID, configuração Release e hora de início (America/Sao_Paulo).
4. Smoke mínimo: `GET /health` → 200 com `status`/`version`/`timestamp`; conferir triângulo ADR-0002 (`<Version>` do `.csproj` == tag candidata, se já houver, == campo `version` da resposta) com `scripts/check-version.sh`; abrir a tela no estado saudável e no estado de erro (critério do plano).
5. Executar o rollback: `scripts/stop-local.sh` (SIGTERM no grupo de processos; sem kill -9 como procedimento oficial). Não subir a “versão anterior” — ela não existe.
6. Critério de sucesso: `GET /health` **não** estabelece conexão; a tela não exibe dados de saúde de um processo ainda no ar; nenhum processo órfão permanece escutando as portas configuradas.
7. Critério de falha: processo ainda escuta após o stop; health responde 200 depois do rollback; ou o stop exige passo não documentado. Nesse caso o G6 de ambiente/rollback fica **NÃO validado** até novo ensaio.
8. Restaurar a candidata (subir de novo pelo passo 3) só para encerrar o ensaio, ou deixar parado até o G7 — registrar qual dos dois foi feito.
9. Registrar o **tempo** observado (passos 5–6). Expectativa: minutos (sem migração). Se exceder o que o runbook declarar, o plano é ajustado antes do G7.

**Quem decide / quem é informado:** com runbook aprovado, a OPS executa o rollback sem esperar. Sem runbook (caso desta primeira execução, até o RB ser gravado), o Arquiteto Líder decide e a OPS executa. Thiago é informado **na hora**, somente via ORQ (Jarvis). Cópia: PO e SUP. Neste teste, impacto em usuário é N/A (nada em produção).

### 4.2 “Deploy” local e smoke (G7, após G5+G6)

1. Artefato = commit aprovado no G4/G5 + tag Git anotada `portal-api-v<versão>` (ADR-0002 v1.1) + `packages.lock.json` / `package-lock.json` instalados de forma reproduzível. Não se usa `latest`. Working tree limpa. API em **Release**.
2. Subir os dois processos como no ensaio (`scripts/start-local.sh`).
3. Repetir o smoke do item 4.1.4. Falha de smoke é gatilho de rollback (seção 4.1).
4. Iniciar a janela de observação de 24 h (hora de início e fim em America/Sao_Paulo).

### 4.3 Janela de observação de 24 h (R3)

**Método:** `scripts/observe-local.sh` emite `GET /health` em loopback a cada **15 min**, durante 24 h, e registra uma linha por amostra (hora, HTTP status, latência, campo `status` do corpo, PID vivo). A cada 4 h (e no início, meio e fim), um ponto de checagem humana registra carga da máquina (`uptime`) e uso de memória/CPU dos dois PIDs (`ps`). Sem painel e sem alerta automático — lacuna consciente desta fase (dono da observabilidade futura: ARQ; não é bloqueio do G2).

**Sucesso da janela (G7 só com estes critérios, no recorte local):**

- Health checks das amostras no horário previsto: HTTP 200 e `status` saudável, salvo janela declarada de ensaio/rollback.
- Nenhuma amostra fora de janela declarada com não-200 ou falha de conexão.
- Latência das amostras e, se o p95 (seção 7) já tiver sido executado pelo QA, o oráculo **p95 ≤ 100 ms** (ET-0001 RT-14 / DEC-ARQ-0010), **indicativo**, não SLO e não CA. A primeira medição documentada vira linha de base **provisória**.
- Smoke inicial da versão candidata passou (seção 4.2).
- Nenhum incidente aberto relacionado a esta REL/teste; não há alertas P0/P1 (não há stack de alerta — N/A, justificado).
- Sem crescimento anômalo de memória/CPU dos processos ao longo da janela (julgamento qualitativo nos pontos de checagem; **não há limiar numérico definido** — lacuna, dono ARQ/OPS na execução se for preciso calibrar; não invento número).

**Falha / gatilho de rollback:** qualquer critério acima violado; smoke reprovado; processo morto inesperadamente. A OPS executa o rollback do 4.1 e informa ORQ, PO, ARQ, SUP e, via ORQ, o Thiago.

**Encerramento:** relatório da janela com início/fim, amostras, checagens, veredito OK/NOK e ponteiro para o commit/tag. Só então a OPS considera o G7 apto a ser registrado pelo ORQ. O deploy “terminar sem erro” não basta.

### 4.4 Evidências a registrar (sem segredos nem dado pessoal)

`/workspace/projetos/portal/evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado).

Conteúdo mínimo:

- Cabeçalho: DEM/TASK/REL (se houver), tipo, data/hora America/Sao_Paulo, agente, `git rev-parse HEAD`, tag se houver, `git status --porcelain` (deve estar vazio), `dotnet --version`, `node -v`, configuração (Release).
- Comando executado (sem expandir valores de variáveis de ambiente).
- Código de saída de cada etapa e log completo **sanitizado** (remover valores de variáveis, tokens, caminhos de home, endereços que não sejam loopback se aparecerem).
- Resultado (OK/NOK) e, no rollback, tempo cronometrado.
- Não gravar `.env`, dumps de ambiente, segredos, dados pessoais nem corpos que os contenham (o corpo de `/health` é só status/versão/timestamp — permitido).

Evidência já produzida desta entrega (toolchain): `rascunhos/ops/evidencias/TASK-0012-toolchain-box-2026-11-26T1516-03/`.

## 5. Variáveis necessárias (somente nomes; sem valores nem segredos) e impacto CORS

Nenhuma variável nova é proposta além das já nomeadas no **ADR-0001 v2 D7** e na DEC-ARQ-0002 L-06. Os **nomes oficiais permanecem** `PORTAL_*` e `LOG_LEVEL`. Os valores locais de desenvolvimento do 1º bloco foram **confirmados pelo FS** em 26/11/2026 15:23 (America/Sao_Paulo) e constam da seção 5.1; vivem no `.env` local, **fora do git**. Não são segredos (loopback e portas de teste).

| Nome | Origem | Finalidade (resumo) | Situação |
|---|---|---|---|
| `PORTAL_API_HOST` | ADR-0001 v2 D7 | Interface de escuta da API | Confirmado pelo FS (§5.1): `127.0.0.1` |
| `PORTAL_API_PORT` | ADR-0001 v2 D7 | Porta de escuta da API | Confirmado pelo FS (§5.1): `8080` |
| `PORTAL_API_ALLOWED_ORIGIN` | ADR-0001 v2 D7, D8 item 8; DEC-ARQ-0002 L-06; ADR-0003 v1.1 | Origem exata do Portal para CORS; obrigatória; fail closed se ausente, inválida ou `*` | Confirmado pelo FS (§5.1): `http://127.0.0.1:4200` (exata, sem curinga) |
| `LOG_LEVEL` | ADR-0001 v2 D7 | Nível de log da API (`ILogger`) | Confirmado pelo FS (§5.1): `Information`. Aceitos: Trace, Debug, Information, Warning, Error, Critical, None. Fallback se inválido/ausente: nota de análise da TASK-0008 (FS) |
| `PORTAL_WEB_PORT` | ADR-0001 v2 D7 | Porta do `ng serve` (fase de testes; D3) | Confirmado pelo FS (§5.1): `4200` |
| `PORTAL_API_BASE_URL` | ADR-0001 v2 D7 | URL da API usada pelo Portal | Confirmado pelo FS (§5.1): `http://127.0.0.1:8080`; **injeção no Angular é do FS** (lacuna D7 / ADR item 3) |

A versão do serviço **não** vem de variável de ambiente (ADR-0002 v1.1): lê-se `<Version>` do `.csproj` de `Portal.Api` (`IncludeSourceRevisionInInformationalVersion=false`).

**Impacto CORS vs convenção `__` do ASP.NET Core (pedido do PO):** o contrato externo de configuração **não muda de nome**. `PORTAL_API_ALLOWED_ORIGIN` continua sendo a variável oficial (D7, fail closed, origem exata, sem `*`, sem credenciais, métodos GET/HEAD; origem não permitida: sem ACAO e **sem 403**, L-06). A convenção de variáveis hierárquicas do ASP.NET Core (ex.: `Section__Key`) **não substitui** esse nome. **Confirmado pelo FS (26/11 15:23):** o mapeamento dos nomes D7 para a configuração do ASP.NET Core é feito no código (sem segundo nome oficial no `.env`). `ASPNETCORE_URLS` e `ASPNETCORE_ENVIRONMENT` **não** são variáveis oficiais desta demanda; nenhum comportamento do contrato pode depender de `ASPNETCORE_ENVIRONMENT` (D8 itens 9 e 11). O `start-local.sh` não exporta `ASPNETCORE_URLS` nem passa `--urls` (bind no `Program.cs`). Atenção: `http://localhost:4200` e `http://127.0.0.1:4200` são origens diferentes; testes e evidências abrem o Portal em `http://127.0.0.1:4200`.

**Angular (`ng serve`) e proxy:** na fase de testes o Portal roda em processo separado (`ng serve`, loopback — D3), com o **binário local** após `npm ci` (`npx --no-install ng serve`). O script de subida **não gera** arquivo de configuração do front (injeção de `PORTAL_API_BASE_URL`: FS). Um `proxy.conf.json` **pode** ser usado pelo FS; **confirmado:** o proxy é opcional e **não dispensa** `PORTAL_API_ALLOWED_ORIGIN` nem o teste de CORS na origem do Portal.

**CSP:** no ADR-0003 v1.1 a CSP passa a ser requisito da **hospedagem de produção** do Portal Angular (ADR futuro). Nesta fase o Portal roda em `ng serve`; a OPS **não** implementa CSP agora e não estima hospedagem de produção (D5). Compatibilidade da CSP com o `ng build` fica para esse ADR futuro (já marcada “a verificar” no ADR-0003).

### 5.1 1º bloco fechado

**Fechado** em 26/11/2026 15:23 America/Sao_Paulo, pela MSG-RET do FS (Lucas Fernandes) à MSG-COL da OPS, com cópia ao ORQ. Nada foi implementado no monorepo (a TASK-0008 segue aguardando liberação do ORQ; `/workspace/projetos/` não existe). Os valores confirmados ficam no `.env` local, fora do git; o `.env.example` dos rascunhos traz os mesmos valores só como exemplo de desenvolvimento (não são segredos).

Valores confirmados:

| Variável | Valor confirmado |
|---|---|
| `PORTAL_API_HOST` | `127.0.0.1` |
| `PORTAL_API_PORT` | `8080` |
| `PORTAL_WEB_PORT` | `4200` |
| `PORTAL_API_ALLOWED_ORIGIN` | `http://127.0.0.1:4200` (exata, sem curinga, fail closed) |
| `PORTAL_API_BASE_URL` | `http://127.0.0.1:8080` |
| `LOG_LEVEL` | `Information`. Aceitos: Trace, Debug, Information, Warning, Error, Critical, None. Fallback se inválido ou ausente: fica na nota de análise da TASK-0008 (proposta do FS: cair em Information e registrar um aviso) |

Comandos oficiais confirmados: `scripts/start-local.sh` e `scripts/stop-local.sh`.

Observações do FS, todas incorporadas nos rascunhos em `rascunhos/ops/DEM-2026-001-TASK-0012-preparacao-dotnet/`:

1. Bind da API no `Program.cs` a partir de `PORTAL_API_HOST`/`PORTAL_API_PORT`. O `start-local.sh` **não** exporta `ASPNETCORE_URLS` nem passa `--urls` (e desfaz essas variáveis se herdadas). Mantém `--no-launch-profile` (proposta operacional 1, confirmada). Porta ausente ou inválida: a API não sobe (fail closed, no código).
2. O `start-local.sh` imprime a URL do Portal (`http://127.0.0.1:${PORTAL_WEB_PORT}`) e avisa que `localhost` é outra origem para o CORS. Testes e evidências abrem `http://127.0.0.1:4200`.
3. O Angular usa o binário local (`npx --no-install ng serve`, após `npm ci` em `apps/portal-web`). O script **não gera** arquivo de configuração do front (lacuna 3 do ADR-0001 v2 permanece com o FS).
4. O `stop-local.sh` encerra a API e o `ng serve` **pelos PIDs gravados em `run/`** (gitignorado), com SIGTERM e espera curta, **sem pkill genérico**. Espera após SIGTERM: **10 s (proposta OPS)**; só se o processo não sair, registra aviso e envia SIGKILL **ao PID específico**. Serve também para exercitar o CA-07 (encerramento gracioso).

Propostas operacionais 1 a 4 da MSG-COL (**confirmadas** pelo FS): `--no-launch-profile`; nomes D7 sem segundo nome oficial no `.env`; proxy do `ng serve` opcional, sem dispensar o CORS; `ASPNETCORE_ENVIRONMENT` fora das variáveis oficiais.

O depósito dos scripts em `/workspace/projetos/portal/scripts/` fica para quando o FS avisar que o esqueleto D6 existe.

## 6. Impacto no procedimento de verificação local (DEC-ARQ-0003 → DEC-ARQ-0007..0010)

As DEC-ARQ-0003, 0004, 0005 e 0006 estão **substituídas** (vigentes: 0007, 0008, 0009 e 0010). A OPS **não propõe alternativa** e **não inventa flags**. O script raiz permanece `scripts/verify-local.sh` em `/workspace/projetos/portal/`, com falha imediata, evidência gitignorada e sanitizada, e **reexecução pelo CR** na box como veredito de entrada no G4.

**API (`apps/portal-api`) — passos A1–A5 da DEC-ARQ-0007:**

| # | Comando (como decidido pelo ARQ) | Critério |
|---|---|---|
| A1 | `dotnet restore --locked-mode` | `packages.lock.json` versionado; NuGet Audit no restore (`NuGetAuditLevel=high`, `NuGetAuditMode=all`, propriedades no `Directory.Build.props` do FS). NU1903/NU1904 como erro; NU1900 (auditoria não executou) também reprova |
| A2 | `dotnet format --verify-no-changes` | DEC-ARQ-0008 |
| A3 | `dotnet build -c Release --no-restore -warnaserror` | zero avisos |
| A4 | `dotnet test -c Release --no-build` + Coverlet: `/p:CollectCoverage=true /p:Threshold=80 /p:ThresholdType=line /p:ThresholdStat=total /p:CoverletOutputFormat=cobertura` | ≥ 80% de linhas do módulo `Portal.Api` (exclui o projeto de testes); ramos/métodos reportados, sem limiar |
| A5 | `dotnet list package --vulnerable --include-transitive` | Evidência independente do A1; o script reprova se a saída listar severidade **High** ou **Critical**. O código de saída do comando, **por si só, não decide** (a verificar, como a própria DEC registra) |

**Web (`apps/portal-web`) — passos W1–W5:**

| # | Comando | Critério |
|---|---|---|
| W1 | `npm ci` | `package-lock.json` obrigatório |
| W2 | `ng lint` | DEC-ARQ-0008 (`angular-eslint`); zero avisos. Opção exata do builder: FS confirma (já na DEC) |
| W3 | `ng test --no-watch --coverage` | ≥ 80% de linhas da aplicação (excluídos `*.spec.ts`). Limiar e eventual pacote de cobertura: **FS/QA confirmam** (DEC-ARQ-0007); a OPS não inventa flag adicional |
| W4 | `ng build` (configuração de produção) | compila sem erro; comando como escrito na DEC |
| W5 | `npm audit --audit-level=high` | reprova em vulnerabilidade alta ou crítica |

**Release/G6 (quando houver tag):** `scripts/check-version.sh` — `<Version>` do `.csproj` == tag `portal-api-v<versão>` == `GET /health`.

**Pré-requisitos de ambiente (item 4 da DEC-ARQ-0007):** cumpridos nesta entrega quanto ao SDK .NET 10, Node 24 `^24.15` e Angular CLI. Rede é necessária para A1/W5; sem rede, esses passos não valem como evidência.

**O que não foi inventado (proposta só onde a DEC deixou em aberto):**

- Alvo do `dotnet` (`.sln`, `.slnx` ou `.csproj`): o rascunho **detecta** o que o FS criar, alinhado ao D6 (“PortalApi.sln (ou .slnx)”).
- `--no-launch-profile` no `dotnet run` do `start-local.sh`: **confirmado pelo FS** (26/11 15:23), para `launchSettings.json` não sobrescrever host/porta. Sem `ASPNETCORE_URLS` e sem `--urls`.
- Uso do `ng` local (`npx --no-install ng serve` após `npm ci` em `apps/portal-web`), em vez do CLI global: **confirmado pelo FS**. O CLI global permanece como pré-requisito da box (R4 / RM-0002). O script não gera configuração do front.
- Espera do `stop-local.sh` após SIGTERM: **10 s (proposta OPS)**; SIGKILL só no PID específico se a espera esgotar. Sem pkill genérico. Confirmado o encerramento pelo PID em `run/`.

SAST/SCA (DEC-ARQ-0009): recorte = NuGet Audit + `AnalysisModeSecurity=All` (API) e `npm audit` + `angular-eslint` recommended (Portal), mais testes dirigidos do QA. Sem Semgrep, SonarQube ou ferramenta nova. A OPS não instala SAST externo.

## 7. Impacto no método do p95 (DEC-ARQ-0006 → DEC-ARQ-0010)

O **método permanece idêntico** (DEC-ARQ-0010): `GET /health` em loopback; 50 requisições de aquecimento **descartadas** (obrigatórias: o JIT do .NET afeta as primeiras); 200 requisições sequenciais, concorrência 1; oráculo indicativo p95 ≤ 100 ms; métricas min, p50, p95, p99, max, erros, distribuição de status; evidência em `evidencias/p95/<AAAA-MM-DDTHHMM-03>-<sha7>/`, gitignorada e sanitizada. Não é SLO e não bloqueia o aceite funcional.

**O que muda:** a API deve estar em **Release** (`dotnet run -c Release` ou publicação local), **não** em Debug; as condições registradas passam a incluir `dotnet --version`, configuração Release, SHA, `nproc`, `uptime`, memória disponível, hora America/Sao_Paulo e declaração de ausência de outro ensaio pesado (além de `node -v`).

**Escolha da OPS (alçada prevista na DEC-ARQ-0010):** script versionado `scripts/measure-p95.mjs` com o `fetch` global do Node 24 (já ferramenta do Angular). A alternativa com `HttpClient` em programa de console .NET **não** é adotada agora (evita um segundo executável no monorepo antes do esqueleto). Sem `autocannon` e sem pacote novo.

O `start-local.sh` grava `run/api.configuration=Release` para o script de p95 recusar medição se a API não estiver em Release.

## 8. Lacunas de contexto e candidatos a conflito (v2.1)

| Lacuna | Dono | Situação na v2.1 |
|---|---|---|
| Esqueleto D6 / monorepo `/workspace/projetos/portal/` ainda inexistente | FS | Scripts depositados só após o esqueleto; preparação permanece Parcial nesse ponto |
| Confirmação FS das portas, origem e comando (1º bloco) | FS | **Fechada** em 26/11 15:23 (§5.1) |
| Injeção de `PORTAL_API_BASE_URL` no Angular | FS | Lacuna já aberta no ADR-0001 v2 (item 3 das lacunas) |
| Opção exata do `ng lint` / pacote e limiar do `ng test --coverage` | FS/QA | Já declarada na DEC-ARQ-0007/0008; a OPS não inventa |
| Código de saída de `dotnet list package --vulnerable` como veredito | ARQ (já “a verificar”) | O rascunho julga pela **saída** (High/Critical), não pelo exit code |
| Itens PV do D8 (preflight CORS, cabeçalho `Server`, drenagem 503, etc.) | FS/QA/ARQ | R3 do G3: testes obrigatórios antes do G4; o spike do encerramento (R4, parte FS) não é desta preparação |
| Confirmação do ARQ sobre o fechamento da R1 (prosa do OpenAPI ainda em ramo) | ARQ | ET-0001 v1.4 já na main (`9b3dc1b`); não bloqueia os rascunhos da OPS |
| Calibração 80% no G5; limiar de CPU/memória da janela de 24 h | QA / ARQ-OPS | Inalteradas; não invento número |
| CSP da hospedagem de produção do Portal | ARQ (ADR futuro) | Fora desta fase (`ng serve`) |
| Plano G2 v1.2 ainda não publicado (v1.1 vigente, `f61a1f9`) | PO | Este parecer é o insumo pedido (DEC-PO-0008: faltavam OPS, QA e DOC) |
| Comentários pontuais desatualizados no `contexto.yaml` v34 | ORQ | Ver candidatos abaixo; a OPS não corrige área do ORQ |

**Candidatos a CONF (não registrados neste momento — o conteúdo normativo já está correto nas decisões; são comentários/campos operacionais atrasados):**

1. `contexto.yaml` v34, TASK-0012: estimativa ainda cita “prep. 8 h (6–10) + G6/G7 5 h (4–7)” e parecer “v1.0 (sem commit)” — fica defasado ao incorporar esta v2.0 (dono ORQ, após este MSG-RET).
2. `contexto.yaml` v34, TASK-0011: o comentário ainda diz “matriz 7.1 aguarda AH-0002”, embora a AH-0002 tenha sido aprovada em 26/11 14:45 (3755fc6). Dono: ORQ (e DOC no texto da TASK).
3. `contexto.yaml` v34, TASK-0006: o comentário ainda menciona “G3 pendente após AH-0001”, embora o G3 já tenha sido aprovado com ressalvas. Dono: ORQ.
4. Pendência “OPS: instalar SDK…” no mesmo contexto: esta entrega a cumpre; o ORQ pode baixá-la após conferir a evidência.

Não registro CONF formal agora: não há choque entre ADR/DEC vigentes, apenas campos operacionais que o ORQ consolidará. Se o ORQ preferir CONF-nnnn, a OPS formaliza na sequência.

## 9. Fontes consultadas

Cabeça da main no momento desta emissão: `f75d8d4` (`f75d8d473505814519b815410728294231d2168a`). Estado operacional: Normal (GOV-ESTADO v1.0). Protocolo de memória v1.1 vigente (AH-0002).

| Artefato | Caminho | Versão / status | Commit |
|---|---|---|---|
| ADR-0001 v2.0 | `02-tecnica/adr/ADR-0001-stack-base-portal-api-e-web.md` | 2.0 **aceito** | 7abc2b1 (merge d40518e) |
| ADR-0002 / ADR-0003 | `02-tecnica/adr/` | v1.1 **aceitos** no G3 | 7abc2b1 / 7bc37ba (merge a271ac1) |
| DEC-ARQ-0007..0010 | `02-tecnica/contratos-api/portal-api/` | v1.0 vigentes; substituem 0003..0006 | 7fa2b43 (merge d40518e) |
| DEC-ARQ-0011 | mesmo diretório | L-12 / `WebApplicationFactory` | 7bc37ba (merge a271ac1) |
| Análise de impacto AH-0003 | `07-agentes/07-arq/analise-impacto-troca-stack-DEM-2026-001.md` | v1.0 vigente | 7fa2b43 |
| tecnologias.md | `01-institucional/tecnologias.md` | v1.1 vigente | 7abc2b1 (merge d40518e) |
| ET-0001 v1.4 / EF-0001 v1.3 | `02-tecnica/especificacoes/` | v1.4 / v1.3 em revisão (R1 entregue) | ac391ea (merge 9b3dc1b) |
| OpenAPI 1.0.0 | `02-tecnica/contratos-api/portal-api/openapi.yaml` | 1.0.0; prosa em ramo (merge de confirmação do ARQ pendente) | cf660fb (contrato); prosa 8494060 em ramo |
| PLANO-DEM-2026-001-G2 | `03-operacional/demandas/DEM-2026-001/plano-atividades-g2.md` | v1.1 vigente (v1.2 em montagem pelo PO) | 053a2d4 / f61a1f9 |
| contexto / historico / aprovacoes | pasta da demanda | contexto **v34**; AH-0003 literal em aprovacoes.md | b57eaa1 (v34); cabeça da main: f75d8d4 |
| DEC-PO-0008 | (registrada no contexto v34) | nenhum CA reaberto | a20fe82 |
| Parecer G3 do ARQ | `07-agentes/07-arq/parecer-tecnico-DEM-2026-001-g3.md` | v1.0; G3 aprovado com ressalvas | 7bc37ba |
| Este parecer v1.1 (histórico) | `rascunhos/ops/_versoes-anteriores/DEM-2026-001-TASK-0012-parecer-g2.v1.1.md` | 1.1 (Node) | sem commit |
| Toolchain na box | `rascunhos/ops/evidencias/TASK-0012-toolchain-box-2026-11-26T1516-03/` | SDK 10.0.404; Angular CLI 22.3.0; Node 24.22.1; npm 11.21.1 | evidência fora do git |

## 10. O que este parecer não faz

Não cria `/workspace/projetos/` nem o esqueleto D6 (FS). Não envia mensagens (os textos do 1º bloco já circularam; esta revisão só ajusta rascunhos e o parecer). Não altera estado/gates/`contexto.yaml`/`historico.md`/`aprovacoes.md`/`Tarefas.csv` (só o ORQ). Não decide arquitetura (ADR/DEC do ARQ já vigentes). Não implementa CSP de produção. Não executa G6/G7 (aguardam o G5). Na v2.0 o parecer é registrado em ramo próprio da pasta do agente (`07-agentes/11-ops/`), **sem merge**.

## 11. Histórico de versões

| Versão | Data/hora (America/Sao_Paulo) | Autor | Mudança |
|---|---|---|---|
| 1.0 | 2026-11-26 12:56 | OPS | Parecer de planejamento do G2 (rascunho, stack Node da AH-0001) |
| 1.1 | 2026-11-26 14:55 | OPS | AH-0001 aprovada; DEC-ARQ-0005/0006; prazo/método do 1º bloco com o FS |
| 2.0 | 2026-11-26 15:21 | OPS | Refeito para AH-0003 / ADR-0001 v2.0 aceito (.NET 10 + Angular 22); DEC-ARQ-0007..0010; reestimativa 10 h + 6 h + 24 h; instalação da toolchain registrada; premissa de merge pendente retirada |
| 2.1 | 2026-11-26 15:25 | OPS | 1º bloco fechado com o FS (26/11 15:23): valores, comandos e observações 1–4 incorporados aos rascunhos e a este parecer (§5.1) |
