---
id: PARECER-G2-DEM-2026-001-TASK-0008
titulo: "Parecer de planejamento do G2 — TASK-0008 (stack Node 24 + Fastify 5, AH-0001)"
tipo: parecer
versao: 1.0
status: substituido
dono: FS
autores: [FS]
aprovado_por: null
criado_em: 2026-11-26T12:49-03:00
atualizado_em: 2026-11-26T15:56-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0008, PLANO-DEM-2026-001-G2, US-0001, US-0002, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0002, DEC-ARQ-0011, AH-0001, AH-0003]
substitui: null
substituido_por: "PARECER-G2-DEM-2026-001-TASK-0008 v2.0 (parecer-planejamento-g2-task-0008-v2-dotnet.md)"
---

> Publicado em 26/11/2026 15:56 a partir do rascunho `rascunhos/fs/DEM-2026-001-TASK-0008-parecer-g2.md` (L-09 do plano G2 v1.2). Texto preservado como emitido; único ajuste: identificador interno de agente substituído pela sigla. **Substituído** pela v2.0 (stack .NET + Angular, AH-0003); mantido só como histórico.

# Rascunho — MSG-RET (parecer de planejamento G2)

DEM-2026-001 [TESTE] / TASK-0008 · FS (Lucas Fernandes) → ORQ (cópia: PO)

Status deste arquivo: rascunho em `/workspace/stack-memoria/rascunhos/fs/` (descartável). Não é commit, não é código, não foi enviado. Redigido em 26/11/2026 12:49 (America/Sao_Paulo).

---

MSG-RET — DEM-2026-001 [TESTE] / TASK-0008 · parecer de planejamento do G2 · FS → ORQ (cópia: PO)

ID da demanda / ID da atividade: DEM-2026-001 / TASK-0008
Remetente: Lucas Fernandes · FS (Agente 08) | Destinatário: Otávio Mendes · Orquestrador (cópia: PO)
Status: Concluída (apenas o parecer de planejamento; a implementação da TASK-0008 não foi iniciada e não começa antes da AH-0001 válida e do G3)
Resumo do resultado: Estimei a implementação da API `GET /health` e da tela de status, com testes unitários, em 22 h sob a premissa de que a AH-0001 aprove a alternativa A do ADR-0001 (Node.js 24 LTS + Fastify 5 + Portal estático) e de que o G3 aprove o contrato alinhado à ET-0001 v1.2 e à DEC-ARQ-0002, sem reabrir os CA. Confirmo os CA da US-0001 (01–09), da US-0002 (01–06) e o RE-02; não proponho alteração de critério ao PO — só premissas já registradas no G1. Há riscos R2/R3 (ADRs ainda propostos, AH-0001 pendente, CORS, origem da versão, timestamp, cache, exposição no health, impacto futuro no Mobile). Respondo à MSG-COL (P-QA): sim, proponho gancho de injeção na fábrica de teste para o 503 e o 500, nunca honrado fora de teste; a ET ainda não descreve o mecanismo do 500 (§7.4) e isso precisa constar no G3/ET.
Entregáveis: este parecer (rascunho em `/workspace/stack-memoria/rascunhos/fs/DEM-2026-001-TASK-0008-parecer-g2.md`). Nenhum código, repositório ou commit.
Critérios de conclusão atendidos:
- Estimativa da API e da tela, com testes unitários, premissas e quebra por item — OK
- Confirmação ou ajuste proposto de US-0001 CA-01..09, US-0002 CA-01..06 e RE-02 — OK
- Riscos com classe e mitigação — OK
- O que precisa constar no contrato do G3 para o FS começar — OK
- Resposta explícita à P-QA / MSG-COL (gancho de injeção 503 e 500) — OK
- Sem implementação, sem repositório, sem commit — OK
Decisões tomadas (na minha alçada): nenhuma. Este parecer não decide stack, contrato nem porta.
Decisões pendentes (de outros agentes):
- AH-0001 (stack base ADR-0001) — Thiago, via ORQ; status em aprovacoes.md: Solicitada, aguardando
- Aceitação dos ADR-0001/0002/0003 — ARQ, após a AH-0001
- Fechamento da TASK-0003 (parecer técnico consolidado, insumo do G2) — ARQ
- G3 / TASK-0007 (aprovação do contrato) — ARQ; o merge do OpenAPI proposto na main (cf660fb) não é o G3
- Estender a ET-0001 §7.4/§11 com a testabilidade do 500 (análoga à do §7.2) e confirmar no G3 que isso não entra na superfície do OpenAPI — AS / ARQ
- Valores de `PORTAL_WEB_PORT`, `PORTAL_API_PORT` / host e `PORTAL_API_ALLOWED_ORIGIN`, e comandos de execução — OPS/FS na TASK-0012 (o ARQ não inventa porta; eu também não)
- Decisão do G2 — PO
Riscos: ver seção 3. Não é “nenhum”.
Dúvidas:
- Ao ARQ/AS: confirmam a extensão da L-05 ao 500 (injeção só na fábrica; fora da superfície do OpenAPI), como na seção 5?
- Ao ARQ: a ferramenta de teste de tela no navegador, se o QA exigir além dos unitários de módulo do FS, precisa de ADR/dependência nova?
- Ao OPS (TASK-0012): quando fecharão porta, origem e comando de subida dos dois processos, para eu não inventar valor no código?
Impedimentos: para emitir este parecer, nenhum. Para iniciar a TASK-0008 em desenvolvimento: AH-0001 ainda não válida; G3 não realizado; ADRs 0001/0002/0003 ainda propostos. Reafirmo: a TASK-0008 não começa antes da AH-0001 válida do Thiago (stack base) e do G3.
Impactos nos componentes: Portal Web — sim (primeira tela, consumidor). Mobile — nenhum nesta demanda (contrato REST/JSON poderá ser consumido no futuro; mudança incompatível exigiria versão maior). Backend/APIs — sim (nasce `portal-api`). Microsserviços — primeiro serviço, domínio API base do Portal. Integrações — nenhuma externa. Dados — nenhum (sem persistência; DBA N/A). Infraestrutura — execução local em `/workspace/projetos/` (pasta ainda inexistente); sem CI, container ou nuvem.
Evidências: fontes versionadas listadas na seção 6 (commits no repositório `stack-conhecimento`); este rascunho no caminho acima. Sem PR nem testes executados (fora de escopo do parecer).
Fontes consultadas: seção 6. Lacunas de contexto: seção 7.
Artefatos criados/alterados: somente este rascunho (não é memória oficial; não houve commit).
Próximo responsável sugerido: ORQ consolida os pareceres do G2 e encaminha ao PO; em paralelo, AS/ARQ tratam a testabilidade do 500 na ET/G3; a implementação (FS) só depois da decisão do G2, da AH-0001 válida e do G3.

---

## Nota de análise (itens 1–9) — pré-requisito da DoR técnica (ainda não há “Em desenvolvimento”)

1. Requisitos. US-0001 e US-0002, REQ-0001..0004, RN-0001 e RN-0002, todos v1.2 vigentes (commit babb9fe), com a ressalva (1) do G1: formatos, 503/405/500, tempo limite de 5 s e “sem login” dependem dos ADR-0002/0003 ainda propostos; se mudarem no G3, o PO reabre os CA afetados. RE-02 aceito em DEC-PO-0005.
2. Arquitetura existente. Não há serviço, código nem catálogo preenchido. ADR-0001/0002/0003 v1.0 permanecem propostos (362ea35). DEC-ARQ-0001 confirma R3. DEC-ARQ-0002 v1.0 vigente (15b3809) fecha L-01 a L-07 como parecer prévio, e não é o G3. `01-institucional/tecnologias.md` segue como rascunho a confirmar.
3. Serviço responsável. Provedor: `portal-api` (a criar). Consumidor: `portal-web` (tela de status, a criar). Nenhuma regra de outro domínio entra na API. Catálogo em `02-tecnica/servicos/` vazio (só `.gitkeep`).
4. Dependências. G2 (PO); G3/TASK-0007 (ARQ); AH-0001 (Thiago); TASK-0004 concluída (protótipo validado com ressalvas). Sem banco, fila ou terceiro. TASK-0012 define valores de ambiente (pode preparar em paralelo após a AH-0001). OpenAPI 1.0.0 proposto já está na main (b3f13d6, merge cf660fb) com os ajustes da DEC-ARQ-0002; isso não aprova o contrato.
5. Contratos. ET-0001 v1.2 em revisão (3a41a2c) detalha o comportamento. OpenAPI 3.1 `info.version` 1.0.0, status proposto, ainda não validado no G3. Consumidores conhecidos: Portal (e, no futuro, monitoramento). Sem versão anterior a compatibilizar.
6. Banco. Nenhuma alteração. Sem modelo, sem migração, DBA não acionado (L9 / ADR-0003 diretriz 4).
7. Impactos no Portal Web e no Mobile. Portal: tela única conforme spec UX v1.0 e DEC-PO-0005 (valores brutos + UTC; formatação adicional em America/Sao_Paulo; RE-02; remoção de valores do DOM no carregamento; CSP e `connect-src` limitados à API — premissa ADR-0003/ADR-0001). Sem sessão e sem cache da consulta (`no-store`). Mobile: sem impacto nesta demanda (ADR-0001).
8. Critérios de aceite. Ver seção 2: todos confirmados, com premissas explícitas; nenhum ajuste de CA proposto ao PO.
9. Dúvidas e riscos. Ver seções 3 e 5, e o campo Dúvidas acima.

---

## 1. Estimativa (API + tela + testes unitários)

**Total: 22 h** (cerca de 3 dias de 8 h), condição de uma pessoa (FS), sem ciclo de retrabalho de CA.

Premissas explícitas (se alguma cair, a estimativa é reaberta):
- AH-0001 válida aprova a alternativa A do ADR-0001 v1.0 proposto: Node.js 24 LTS, JavaScript ESM, Fastify 5.x na `portal-api`, Portal estático sem framework e sem build, monorepo local `/workspace/projetos/portal/` com a estrutura D6, dois processos independentes, testes com `node:test` / `node:assert` e `inject` do Fastify.
- G3 aprova o contrato alinhado à ET-0001 v1.2 e à DEC-ARQ-0002, sem mudança dos CA vigentes.
- Sem persistência, sem Mobile, sem polling, sem autenticação, execução local, custo zero de licença.
- Testes do FS: unitários e de integração da API (incluindo contrato contra o esquema aprovado) e unitários dos módulos da tela (cliente HTTP, estados, formatação, RE-02), sem dependência nova. Teste em navegador, desempenho formal (p95 indicativo) e PQ são da TASK-0010 (QA), não desta estimativa.
- Valores de porta e origem saem da TASK-0012; não os invento.
- Se a AH-0001 escolher a alternativa B (zero dependências, `node:http`), acrescento **+6 h** (roteamento, validação, logs e adaptação de testes) e reavalio; troca para Node 26 é variação menor, a estimar se ocorrer.

Quebra:

| Item | Horas | Recorte |
|---|---:|---|
| Scaffold do monorepo | 3 | Estrutura D6, manifests e lockfile, `.nvmrc`/`.gitignore`, leitura e validação das variáveis (fail closed em origem e versão), `serve.js` esqueleto, README só com ponteiros e como instalar/executar/testar |
| Endpoint `GET /health` | 5 | Serviço de saúde, `version.js` (lê o manifesto uma vez; manifesto inválido ⇒ não inicia), relógio injetável, 200/503, 405 com `Allow: GET, HEAD`, 500 problem+json, 404 padrão do serviço, HEAD tolerado, OPTIONS de preflight, cabeçalhos (`Cache-Control: no-store`, `nosniff`, `X-Request-Id` UUID v4), CORS sem curinga, remoção de banner de servidor/framework, gancho de encerramento gracioso (premissa de stack) e ganchos de fábrica de teste (503 e 500) |
| Testes da API | 4 | Unitários e integração via `inject`: 200, 503 por injeção, 500 por injeção, 405, CA-06 (2+ chamadas, timestamp variável), timestamp exato com relógio injetável, `version` = manifesto, bootstrap recusa manifesto/origem inválidos, CORS (com e sem origem permitida, sem 403), esquema fechado, denylist de dado sensível (CA-05), ausência de controle remoto (query/cabeçalho/env não forçam 503/500) |
| Tela de status | 4 | Spec UX v1.0 / DEC-PO-0005: três estados, valores brutos da mesma consulta + UTC, formatação adicional America/Sao_Paulo, RE-02 (503 sem versão/timestamp na UI), carregando remove valores do DOM, timeout 5 s sem retry, botão “Atualizar status”, inserção só como texto, CSP do servidor estático |
| Testes da tela | 3 | Unitários dos módulos: sucesso, timeout, corpo inválido, HTTP inesperado, 503 sem renderizar versão/timestamp, recuperação, não assumir saudável, `textContent` |
| Instrumentação / logs | 1 | Logs estruturados (pino, premissa A): `/health` em `debug`, erros em `error`, `X-Request-Id` no log do servidor, sem dado sensível |
| Evidências / PR | 2 | Nota de análise anexada à TASK, `npm audit` sem alta/crítica, cobertura no código alterado (meta inicial 80%, a calibrar), ramo `feat/TASK-0008-…`, PR local com IDs e trailer `Agente: FS` |
| **Total** | **22** | |

Fora desta estimativa: retrabalho se o G3 reabrir CA; preparação formal de ambiente, smoke e rollback (TASK-0012); Code Review (TASK-0009); plano/execução/PQ (TASK-0010); documentação de versão (TASK-0011).

---

## 2. Critérios de aceite (confirmação ou ajuste proposto ao PO)

Ajustes, se houvesse, seriam propostas ao PO — não alterei US/REQ. Leitura: “o formato definido” = ET/ADR vigente no G3; até lá vale a premissa dos ADR propostos (já escrita nas US).

US-0001 CA-01 — Confirmo. HTTP 200, `Content-Type` JSON (`application/json; charset=utf-8` na ET), corpo com `status`, `version` e `timestamp` presentes, não nulos e não vazios.

US-0001 CA-02 — Confirmo, com premissa: o valor saudável é `"ok"` enquanto o ADR-0003/G3 não disser o contrário. Se o enum mudar no G3, o PO reabre o CA (condição 1 do G1).

US-0001 CA-03 — Confirmo. Formato RFC 3339 / ISO 8601 em UTC com `Z` e exatamente 3 milissegundos; gerado no instante da resposta; tolerância de verificação ±5 s (DEC-AS-0002, confirmada na DEC-ARQ-0002 L-07); igualdade exata com relógio injetável. Vale também no 503.

US-0001 CA-04 — Confirmo, com premissa: origem = campo `version` do manifesto do serviço (ADR-0002 / PS-02, depende da AH-0001); oráculo = resposta = manifesto do artefato = tag de release quando houver; sem hash de commit na resposta. Falha de leitura ou formato inválido ⇒ o serviço não inicia.

US-0001 CA-05 — Confirmo. Aplica-se a corpo e cabeçalhos de 200, 503, 405 e 500: sem dados pessoais, credenciais, segredos, tokens, hostname, caminho, IP, variável de ambiente, versão de runtime/dependência, hash de commit ou stack trace.

US-0001 CA-06 — Confirmo. Duas ou mais chamadas: sem persistência nem estado de negócio; logs de acesso/auditoria permitidos; `status` e `version` iguais; `timestamp` pode variar; recurso somente leitura.

US-0001 CA-07 — Confirmo, com premissa do ADR-0003 / DEC-PO-0006 (alternativa A): HTTP 503, mesmo esquema, `status: "unavailable"`, sem causa ou detalhe. Se o G3 não incluir esse caminho, o CA não se aplica até nova decisão. Testabilidade: ver seção 5 (já exigida na ET §7.2 e na L-05). O gancho de encerramento gracioso em execução é PS-05 / AH-0001, distinto do gancho de teste; parada abrupta é timeout no cliente (RN-0002).

US-0001 CA-08 — Confirmo. Métodos diferentes de `GET` (e do `HEAD` tolerado) ⇒ 405 com `Allow: GET, HEAD` (DEC-ARQ-0002 L-02; o texto do CA já admite HEAD “se aplicável”). OPTIONS de preflight não é 405 (L-02). Sem detalhe interno no corpo (CA-05).

US-0001 CA-09 — Confirmo. HTTP 500 em `application/problem+json` somente com `type`, `title` e `status` (premissa fechada na DEC-ARQ-0002 L-01: `about:blank`, `Internal Server Error`, 500). Não é estado saudável; a tela trata como US-0002 CA-03 caso (a). A ET §7.4 fecha o formato, mas ainda não o mecanismo de disparo repetível em teste — ver seção 5 (proposta, não alteração do CA).

US-0002 CA-01 — Confirmo. No caminho saudável, a tela mostra status, versão e timestamp com valores brutos iguais aos da mesma consulta (timestamp UTC no formato da API); a formatação em America/Sao_Paulo é adicional e não substitui o bruto (D-UX-05 e D-UX-08, aceitos em DEC-PO-0005).

US-0002 CA-02 — Confirmo. Estado operacional explícito e distinguível sem depender só de cor. Oráculo do protótipo/spec validados: ícone, título “API operacional”, selo “Saudável” e estilo de borda.

US-0002 CA-03 — Confirmo. Caso (a): sem resposta, timeout, HTTP inesperado (≠ 200 e ≠ 503 de contrato), corpo fora do esquema, ou bloqueio CORS ⇒ erro genérico, informa que o status não pôde ser obtido. Caso (b): 503 de contrato ⇒ o mesmo estado de erro genérico, **sem** exibir versão nem timestamp. Sem valores anteriores como atuais, sem tela em branco, sem código HTTP, URL, host ou stack.

RE-02 — Confirmo (já aceito pelo PO em DEC-PO-0005 / D-UX-03). É regra de apresentação, não muda o contrato da API (o 503 pode trazer os três campos).

US-0002 CA-04 — Confirmo. Toda consulta passa por “carregando”; valores da consulta anterior são removidos do DOM, não apenas ocultados (D-UX-02, promovido ao CA).

US-0002 CA-05 — Confirmo. Do estado de erro, a ação “Atualizar status” (protótipo) ou o recarregamento da página reexecuta a consulta: saudável ⇒ CA-01/CA-02; nova falha ⇒ permanece o erro.

US-0002 CA-06 — Confirmo. Em qualquer estado, só status, versão e timestamp (apenas no saudável) e mensagens genéricas; valores da API só como texto, nunca como HTML.

Observação (não é ajuste de CA): o corpo da US-0002 ainda cita “público da tela não definido pela CPO”, embora o plano G2 e o contexto registrem a confirmação da CPO (DEC-PO-0002). Cabe ao PO, se quiser, alinhar o texto narrativo.

---

## 3. Riscos

| ID | Risco | Classe | Prob. × impacto (qualitativo) | Mitigação |
|---|---|---|---|---|
| RK-FS-01 | ADRs 0001/0002/0003 ainda propostos; o G3 pode alterar formato, 503/405/500, timeout ou “sem login” e o PO reabre CA (condição 1 do G1) | R3 | Média × alto (retrabalho de API, tela e testes) | Não implementar antes do G3 e da AH-0001; estimar de novo se os CA mudarem |
| RK-FS-02 | Stack não aprovada (AH-0001). Sem ela não há runtime, estrutura nem origem da `version` | R3 | Alta × alto (bloqueio total da TASK-0008) | Estimativa condicionada à alternativa A; a TASK permanece bloqueada até AH válida |
| RK-FS-03 | Impacto no Mobile: nenhum agora, mas um contrato incompatível depois quebra um consumidor futuro | R1 | Baixa × médio | Contrato versionado (SemVer próprio, inicial 1.0.0); `additionalProperties: false` no provedor; Mobile fora de escopo; quebra = MAJOR (+ AH se público) |
| RK-FS-04 | CORS: origem/porta não definidas; origem errada ou curinga; serviço que não inicia (fail closed) ou tela em erro permanente | R2 | Média × alto | Regra já na DEC-ARQ-0002 L-06 e na ET §7.5; valores só na TASK-0012; testes de origem permitida e negada (sem 403, sem `*`); Portal não envia cabeçalhos não simples |
| RK-FS-05 | Origem da versão divergente (hard-code, env, hash) ou formato inválido | R2 | Média × médio | SSOT no manifesto, lido na inicialização (ADR-0002); serviço não inicia se inválido; oráculo CA-04 = resposta = manifesto = tag; a origem concreta depende da AH-0001 |
| RK-FS-06 | Fuso/formato do timestamp (UTC vs America/Sao_Paulo; precisão; relógio local do servidor) | R2 | Média × médio | Servidor emite só UTC com `Z` e 3 ms; tela exibe o bruto e, à parte, Brasília; relógio injetável; tolerância ±5 s |
| RK-FS-07 | Cache (navegador ou intermediário) reapresenta um “saudável” velho — viola RN-0002 | R2 | Média × alto | `Cache-Control: no-store` em todas as respostas de `/health` (L-04); `fetch` com `cache: 'no-store'`; atualização sempre passa por carregando e limpa o DOM |
| RK-FS-08 | Exposição de informação sensível no health (banner de framework, stack em 500, hash, hostname, campos extras) | R3 | Média × alto (REQ-0004 / RN-0001; demanda já é R3) | Esquema fechado; problem+json só `type`/`title`/`status`; remover cabeçalhos de servidor/runtime; denylist nos testes; logs sem segredo; exposição só interna — fora da rede interna reabre R3/N3 + AH (ADR-0003) |
| RK-FS-09 | CA-07/CA-09 não repetíveis se não houver gancho de fábrica (P-QA) ou se alguém expor controle remoto | R2 (repetibilidade) / R3 se houver controle remoto (N3 de segurança, L-05) | Média × alto | Seção 5: injeção só na fábrica, inerte fora de teste; pedir o mesmo na ET/G3; OpenAPI sem parâmetro de force |
| RK-FS-10 | Cadeia npm (Fastify e transitivas) — RK-3 do contexto | R2 | Baixa × médio | lockfile, `npm ci`, `npm audit` sem alta/crítica no CR (ADR-0001 D2) |
| RK-1 (contexto) | Stack sem confirmação atrasa FS | R3 | Já aberto, dono ORQ/ARQ | AH-0001; FS só após aceitação |

---

## 4. O que precisa constar no contrato do G3 para o FS começar

O OpenAPI 1.0.0 proposto já está na main (caminho `02-tecnica/contratos-api/portal-api/openapi.yaml`, commit b3f13d6, merge cf660fb) e já incorpora, no artefato, os apertos da DEC-ARQ-0002 (regex oficial SemVer sem `+build`, `Allow: GET, HEAD`, UUID de `X-Request-Id`, etc.). Isso **não** substitui o G3. Para eu começar, o contrato **aprovado** (OpenAPI + ET vigente no G3) precisa fechar, de forma inequívoca:

- Path e método: `GET /health`, sem parâmetros de consulta, sem corpo, fora do prefixo de versão, seguro e idempotente.
- Códigos: 200 (saudável), 503 (indisponibilidade de contrato), 405 (método não permitido), 500 (erro interno). 404 é padrão do serviço, não resposta de sucesso de `GET /health`. HEAD é tolerado (mesmo código e cabeçalhos do GET, sem corpo) e **não** integra a superfície prometida (sem operação `head`). OPTIONS é preflight CORS `204`, **não** é 405 e **não** é operação de negócio.
- Schema: objetos fechados (`additionalProperties: false`) com tipos, formatos e exemplos. 200/503: exatamente `status` (const `"ok"` / `"unavailable"`), `version` (SemVer 2.0.0 oficial sem metadados de build — regex da L-07), `timestamp` (RFC 3339 UTC `Z` com 3 ms — regex já na ET/OpenAPI). 405/500: `application/problem+json` somente `type` (`about:blank`), `title` (frase canônica em inglês) e `status` numérico (L-01).
- Exemplos de 200, 503, 405 e 500 no OpenAPI aprovado (critério da TASK-0007 no plano G2).
- Cabeçalhos em todas as respostas de `/health`: `Cache-Control: no-store`; `X-Content-Type-Options: nosniff`; `X-Request-Id` (UUID canônico 36 caracteres, hex minúsculo com hífens; ausente ou inválido ⇒ o servidor gera UUID v4 e **não** responde 400). 405 inclui `Allow: GET, HEAD`. Sem cabeçalho que revele servidor, runtime ou framework. CORS: `Access-Control-Allow-Origin` só se a origem for exatamente `PORTAL_API_ALLOWED_ORIGIN` (obrigatória, sem curinga; ausente/inválida/`*` ⇒ o serviço não inicia); métodos `GET`/`HEAD`; sem credenciais; sem `Allow-Headers`/`Expose-Headers` para `X-Request-Id` nesta demanda; origem não permitida = status normal **sem** ACAO e **sem** 403.
- Cache: `no-store` também como padrão do serviço (inclusive 404), conforme L-04.
- Versionamento: SemVer próprio do contrato, inicial `1.0.0`, distinto da versão do serviço; campo opcional novo = MINOR; remoção/renomeação/mudança de tipo = MAJOR.
- Erros: padrão L-01 acima; nunca `detail`, `instance`, stack, caminho ou causa no corpo desta versão; sem `Retry-After` no 503 (L-05).
- Autenticação: `security: []`; contrato interno, sem autenticação; condição de exposição local/rede interna. Exposição pública reabre R3/N3 + AH.
- SLA de latência: o alvo p95 ≤ 100 ms em execução local é **indicativo, não é SLO nem critério de aceite** (ADR-0003 / ET RT-14). O que precisa estar fechado para o cliente: tempo limite de 5 s sem nova tentativa automática (DEC-AS-0001, confirmada).
- Stack aprovada: AH-0001 válida e ADR-0001 aceito (ou condição explícita do ARQ no G3). Sem isso não há como fixar runtime, fábrica da aplicação nem origem da `version`.
- Estrutura de pastas em `/workspace/projetos/`: confirmar a D6 do ADR-0001 (`/workspace/projetos/portal/` com `apps/portal-api` e `apps/portal-web`, sem código compartilhado). A pasta `/workspace/projetos/` ainda não existe; eu só a crio após a AH e o G3.
- Comando de execução e porta: **não estão definidos em nenhum artefato vigente** (lacuna). O G3 ou o registro de ambiente da TASK-0012 precisa fechar: nomes já conhecidos (`PORTAL_API_HOST`, `PORTAL_API_PORT`, `PORTAL_API_ALLOWED_ORIGIN`, `LOG_LEVEL`, `PORTAL_WEB_PORT`, `PORTAL_API_BASE_URL`); valores concretos (loopback, origem `http://127.0.0.1:${PORTAL_WEB_PORT}`); comando para instalar e subir API e Portal em processos separados (premissa A: `npm ci` e o entrypoint de cada app). Eu não invento porta neste parecer.
- Ferramentas de teste: no G3/ADR aceito, confirmar `node:test` e `node:assert`, `inject` do Fastify (premissa A) e validação da resposta contra o esquema aprovado. Qualquer dependência nova de teste (incluindo ferramenta de navegador) passa pelo ARQ. Relógio, estado de saúde e falha interna injetáveis na fábrica — ver seção 5. Meta inicial de 80% de cobertura no código alterado, a calibrar.
- Testabilidade de 503 e 500: ver seção 5 (não pode aparecer como operação, query ou cabeçalho no OpenAPI).

Sem o G3 aprovado (e sem a AH-0001), a DoR técnica da TASK-0008 permanece incompleta e eu não começo a codificar.

---

## 5. Resposta à P-QA / MSG-COL — gancho de injeção do 503 e do 500 na fábrica de teste

Pergunta da QA (via ORQ, cópia ARQ e AS; pendência P-QA no contexto.yaml v14): haverá injeção do 500 na fábrica de teste (CA-09), no mesmo espírito do 503 da ET-0001 §7.2? Sem esse gancho, CA-07 e CA-09 não são repetíveis. A DEC-ARQ-0002 L-05 só permite injeção na fábrica, nunca endpoint, query, cabeçalho ou variável honrada fora de teste.

Textos conferidos (não parafraseio o sentido):

- US-0001 v1.2 CA-07: caminho de indisponibilidade (premissa ADR-0003; DEC-PO-0006 alternativa A); `GET /health` responde HTTP 503 com o mesmo esquema do 200, `status` de indisponibilidade (premissa `"unavailable"`), sem causa/detalhe; se o ADR/contrato vigente não incluir esse valor, o CA não se aplica até nova decisão.
- US-0001 v1.2 CA-09: falha interna que impede 200 ou o 503 de contrato ⇒ HTTP 500 no formato de erro padronizado da ET (premissa: `application/problem+json` apenas com `type`, `title` e `status`), sem causa, caminho, stack ou detalhe interno. A tela trata como US-0002 CA-03 caso (a).
- ET-0001 v1.2 §7.2 (testabilidade do 503): “o `503` é testável **somente** por injeção na fábrica da aplicação (estado de saúde injetável, no mesmo espírito do relógio injetável) ou equivalente de teste unitário/integração. **Proibido** endpoint, query string, cabeçalho ou variável honrada em execução não-teste que force o 503 remotamente (seria N3 de segurança). Em builds/ambientes que não forem de teste, o gancho não existe ou é inerte.” O gancho concreto de encerramento gracioso em execução é PS-05 / AH-0001, distinto deste.
- ET-0001 v1.2 §7.4 (500): fecha o corpo `{"type":"about:blank","title":"Internal Server Error","status":500}` e a ausência de detalhe; **não** descreve mecanismo de disparo em teste. A tabela §11 cita o 500 no teste de contrato (corpo sem detalhe), não o gancho.
- DEC-ARQ-0002 L-05: sem `Retry-After`; no encerramento gracioso, enquanto o listener estiver no ar, responder 503; “Teste do 503: permitido **somente** por injeção na fábrica da aplicação (estado de saúde injetável, no mesmo espírito do relógio injetável) ou equivalente de teste unitário/integração. **Proibido** endpoint, query string, cabeçalho ou variável honrada em execução não-teste que force o 503 remotamente (controle remoto inseguro; seria N3 de segurança). Em builds/ambientes que não forem de teste, o gancho não existe ou é inerte.” A L-05 não cita o 500.

**Resposta: sim.** Como FS, proponho — e usarei após AH-0001 e G3, se AS/ARQ confirmarem — um gancho de injeção **só na fábrica de teste** para o 503 (CA-07) e também para o 500 (CA-09), no mesmo espírito da L-05 e da ET §7.2. Não é decisão de contrato; é proposta de implementação e pedido de fechamento na ET/G3.

Proposta de gancho (premissa de stack A: fábrica `app.js` do ADR-0001 D6):
- A fábrica recebe **apenas argumentos de função**, dependências substituíveis: (1) `clock` — já previsto — para o timestamp determinístico; (2) provedor de estado de saúde — padrão `ok`; em teste, `unavailable` faz `GET /health` responder o 503 de contrato; (3) provedor de falha interna — quando ativo nos testes, o colaborador injetado falha e o tratador padronizado responde o 500 de CA-09, sem vazar detalhe no corpo (detalhe só em log interno, nível `error`, sem dado sensível).
- O bootstrap de execução (`server.js`) instancia a fábrica **sem** esses argumentos: relógio do sistema, saúde `ok`, nenhum provedor de falha. Os testes (`node:test` + `inject`, sem rede) é que chamam `buildApp({ clock, healthState, failure })`.
- Não descrevo código aqui (este parecer não implementa).

Como garantir que nada é honrado fora de teste:
- Nenhum endpoint, query string, cabeçalho ou variável de ambiente para forçar 503 ou 500 — inclusive nenhum `FORCE_*` e nenhum uso de `NODE_ENV`/`LOG_LEVEL` como controle remoto. A L-05 trata variável honrada em não-teste como proibida (N3 de segurança).
- “O gancho não existe ou é inerte” fora de teste significa: o argumento simplesmente não é passado no bootstrap de execução; não é um flag de ambiente que um operador possa ligar.
- Teste de segurança (CA-05 / REQ-0004 e a própria L-05): query, cabeçalho ou env tentando forçar 503/500 não alteram o caminho saudável.
- O gancho de encerramento gracioso (PS-05, após AH-0001) é comportamento de produção do 503 e não substitui o gancho de teste; também não pode virar controle remoto.

O que isso exige no contrato G3 / ET (pedido a AS e ARQ):
- ET-0001: estender §7.4 e a tabela §11 com a testabilidade do 500 em termos iguais aos do §7.2 (somente injeção na fábrica ou equivalente de teste; mesmas proibições da L-05). Distinguir no texto: (a) ganchos de teste de 503 e 500; (b) gancho de encerramento gracioso em execução (PS-05 / AH-0001).
- OpenAPI aprovado no G3: **não** documentar operação, parâmetro, cabeçalho ou schema de “force health/error”. A superfície 1.0.0 permanece `GET /health` e as respostas 200/503/405/500. A forma de obter 503/500 em teste é assunto da ET/testes, não do contrato.
- G3: o ARQ confirma esta leitura (L-05 estendida ao 500) ou registra equivalente aceito. Sem oráculo escrito, o QA não tem como repetir o CA-09 de forma controlada, e o FS ficaria só com esta premissa de parecer.

Efeito na estimativa: o trabalho já está embutido nos itens “Endpoint” e “Testes da API” da seção 1; não altera as 22 h se a proposta for aceita. Se o ARQ recusar qualquer gancho de 500, o CA-09 deixa de ser repetível de forma determinística — risco RK-FS-09 a reabrir com o PO/QA.

---

## 6. Fontes consultadas (ID + caminho + versão/commit)

Repositório: `/workspace/stack-memoria/stack-conhecimento/` (HEAD no momento da leitura final: b792363). Pacote `/workspace/stack-memoria/pacotes-contexto/DEM-2026-001/` inexistente.

| ID | Caminho | Versão / estado | Commit |
|---|---|---|---|
| PLANO-DEM-2026-001-G2 | `03-operacional/demandas/DEM-2026-001/plano-atividades-g2.md` | v1.0, em-revisao | 4814277 |
| contexto.yaml | `03-operacional/demandas/DEM-2026-001/contexto.yaml` | v14 | 4ed41be |
| historico.md | `03-operacional/demandas/DEM-2026-001/historico.md` | append-only (até parecer QA / v14 e merge do OpenAPI) | 4ed41be / cf660fb |
| aprovacoes.md | `03-operacional/demandas/DEM-2026-001/aprovacoes.md` | G1 aprovado com observações; AH-0001 solicitada, aguardando; G3 em branco | (arquivo na main) |
| US-0001 | `03-operacional/demandas/DEM-2026-001/historias/US-0001-endpoint-health.md` | v1.2, vigente | babb9fe |
| US-0002 | `03-operacional/demandas/DEM-2026-001/historias/US-0002-tela-status.md` | v1.2, vigente | babb9fe |
| REQ-0001..0004 | `03-operacional/demandas/DEM-2026-001/requisitos/` | v1.2, vigente | babb9fe |
| RN-0001, RN-0002 | `01-institucional/regras-negocio/` | v1.2, vigente | babb9fe |
| DEC-PO-0005 / validação do protótipo | `03-operacional/demandas/DEM-2026-001/validacao-po-prototipo-task-0004.md` | v1.0; RE-02 aceito | af208f2 |
| ADR-0001, ADR-0002, ADR-0003 | `02-tecnica/adr/` | v1.0, propostos | 362ea35 |
| DEC-ARQ-0002 | `02-tecnica/contratos-api/portal-api/DEC-ARQ-0002-detalhes-contrato-health.md` | v1.0, vigente (não é G3) | 15b3809 |
| EF-0001 | `02-tecnica/especificacoes/EF-0001-health-check-portal-api.md` | v1.2, em-revisao | 3a41a2c |
| ET-0001 | `02-tecnica/especificacoes/ET-0001-health-check-portal-api.md` | v1.2, em-revisao | 3a41a2c |
| OpenAPI portal-api | `02-tecnica/contratos-api/portal-api/openapi.yaml` | 3.1, `info.version` 1.0.0, proposto; na main após merge (não é G3) | b3f13d6 (merge cf660fb) |
| UX-ESPEC-DEM-2026-001-TASK-0004 + protótipo | `07-agentes/06-ux/prototipos/DEM-2026-001-US-0002-tela-status/` | v1.0, em-revisao; aprovado com ressalvas (DEC-PO-0005) | 1290f25 |
| PROMPT FS | `07-agentes/08-fs/PROMPT.md` | documento vigente do agente (MSG-RET, nota 1–9) | (arquivo na main) |

---

## 7. Lacunas de contexto (nada disto foi inventado)

- Pacote de contexto `/workspace/stack-memoria/pacotes-contexto/DEM-2026-001/` não existe.
- AH-0001 não está válida; ADR-0001/0002/0003 permanecem propostos; G3 não realizado.
- Portas, origem concreta e comando de execução não aparecem em artefato vigente (só nomes de variáveis e a premissa `http://127.0.0.1:${PORTAL_WEB_PORT}`).
- `/workspace/projetos/` não existe; catálogo de serviços vazio.
- ET-0001 §7.4 não especifica testabilidade do 500 (esta é a lacuna P-QA; a seção 5 propõe o fechamento, não o antecipa como decisão).
- Ferramenta de medição do p95 local (PS-08) e ferramenta de teste de tela no navegador não definidas (OPS/QA/ARQ).
- No contexto.yaml v14, o comentário de `tarefas.TASK-0006` ainda cita o OpenAPI só no ramo (`2b9fa2e`); o arquivo já está na main (b3f13d6 / cf660fb). Não alterei o contexto (alçada do ORQ).
- L-09 (modelos de EF/ET/contrato e `INDEX.md`) e o fechamento formal do CONF-0001 permanecem com a DOC, sem efeito direto neste parecer.
- Não consultei pareceres de planejamento de outros agentes além do que já está gravado no historico/contexto (CR no v12; QA no v14).

---

Restrição reafirmada: a TASK-0008 **não começa** antes da AH-0001 válida do Thiago (stack base) e do G3.
