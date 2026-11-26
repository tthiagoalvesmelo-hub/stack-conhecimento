---
id: EF-0001
titulo: "Especificação funcional do health-check GET /health da portal-api e consumo pela tela de status"
tipo: ef
versao: 1.3
status: em-revisao
dono: AS
autores: [AS]
aprovado_por: null
criado_em: 2026-11-26T12:27-03:00
atualizado_em: 2026-11-26T15:16-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0006, ET-0001, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, ADR-0003, DEC-PO-0005, DEC-PO-0006, DEC-ARQ-0002, DEC-ARQ-0011, DEC-AS-0001, CONF-0001, ADR-0001, AH-0003, L-10]
substitui: null
substituido_por: null
---

# EF-0001 — Health-check `GET /health` e consumo pela tela de status

> [TESTE] DEM-2026-001 · TASK-0006 · Fluxo 01 · classe de risco R3 (DEC-ARQ-0001) · autora: AS.
> **v1.3 (R1 do G3):** fecha a **L-10** (a dependência da AH-0001 acabou: AH-0001 substituída pela **AH-0003**; ADR-0001 v2.0 aceito — C#/.NET 10 + Angular 22; G3 concluído com ressalvas, parecer do ARQ, merge `a271ac1`). **Nenhuma mudança funcional**: CA, RN, REQ, fluxo e matriz §7 permanecem. Detalhamento técnico: ET-0001 v1.4. Contrato `openapi.yaml` 1.0.0 aprovado pelo ARQ no G3. A ressalva do G1 (se os ADR mudarem, o PO reabre os CA afetados) segue com o PO (plano G2 v1.2).
> **v1.2:** incorpora a resposta do PO (DEC-PO-0006, US/REQ/RN v1.1, promovidos a **v1.2 vigente** no G1 — commit babb9fe; G1 aprovado com observações, b083eef) e toma nota da DEC-ARQ-0002 (L-01 a L-07). (Na v1.2 os ADR-0001/0002/0003 estavam *propostos*; hoje: ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 *aceitos*.) A ressalva do G1 (formatos, 503/405/500, tempo limite de 5 s e “sem login” dependem dos ADR; se mudarem no G3, o PO reabre os CA) vale também para esta EF. Detalhamento técnico: ET-0001 (hoje v1.4). Contrato: `02-tecnica/contratos-api/portal-api/openapi.yaml` 1.0.0 (na main; aprovado pelo ARQ no G3).

## 1. Objetivo
Permitir saber, de forma rápida, objetiva e segura, se a `portal-api` (API base do Portal Web) está respondendo e qual versão do serviço está em execução, e tornar esse sinal visível numa tela simples do Portal — sem expor dado sensível e sem jamais apresentar indisponibilidade como saudável.

## 2. Atores e consumidores
| Ator / consumidor | Papel | Fonte |
|---|---|---|
| Portal Web — tela de status | Consome `GET /health`; exibe status, versão e timestamp, ou o estado de erro (US-0002) | US-0002 v1.2, REQ-0002 v1.2, REQ-0003 v1.2 |
| Operador / equipe técnica interna | Abre a tela e interpreta o estado (público confirmado pela CPO — DEC-PO-0002) | DEC-PO-0002 |
| Checagem operacional (ferramentas de monitoramento, futuro) | Consulta `GET /health` direto, sem credenciais, na rede interna | US-0001 v1.2, ADR-0003 |
| `portal-api` | Provedor do recurso | ET-0001 |

## 3. Casos de uso
### UC-01 — Consultar o status da API (US-0001)
- **Ator:** consumidor técnico (Portal ou checagem operacional).
- **Pré-condição:** acesso à rede interna onde a `portal-api` executa; origem do Portal permitida (no caso do Portal).
- **Fluxo principal:** (1) o consumidor envia `GET /health`; (2) a API responde `200` com `status` `"ok"`, `version` (versão do serviço em execução, idêntica ao manifesto e, quando houver, à tag — CA-04) e `timestamp` (instante da resposta, UTC com milissegundos); (3) o consumidor interpreta a resposta como saudável.
- **Fluxos alternativos:** `503` (processo em encerramento, CA-07) ⇒ indisponível; método diferente de `GET` (e de `HEAD`, se tolerado na ET) ⇒ `405` (CA-08); erro inesperado ⇒ `500` padronizado (CA-09); sem resposta/tempo esgotado/corpo inválido ⇒ o consumidor trata como indisponível (cenários na seção 5).
- **Pós-condição (CA-06):** após duas ou mais chamadas sobre a mesma instância, não há criação, alteração nem exclusão de dados persistidos nem de estado de negócio. Logs de auditoria/acesso são permitidos. Os campos de status e versão permanecem iguais; o timestamp pode variar. O recurso permanece somente leitura.

### UC-02 — Ver o status na tela do Portal (US-0002)
- **Ator:** operador / equipe técnica interna.
- **Fluxo principal:** abre a tela ⇒ estado Carregando (valores anteriores **removidos do DOM**, CA-04) ⇒ consulta `GET /health` (UC-01) ⇒ resposta válida e `status` `"ok"` ⇒ estado Saudável com os **valores brutos** de status, versão e timestamp UTC iguais aos da **mesma** consulta (CA-01); a formatação em America/Sao_Paulo é adicional e não substitui o valor bruto.
- **Fluxo de erro (CA-03):** (a) API não responde, tempo esgotado, erro HTTP inesperado (≠ 200 e ≠ 503 de contrato) ou corpo inválido; ou (b) `503` com `status` `"unavailable"` (DEC-PO-0006, alternativa A) ⇒ estado Erro/indisponível explícito, nunca “saudável”, sem valores anteriores, sem tela em branco e sem mensagem técnica. No caso (b), a tela usa o mesmo estado de erro genérico e **não exibe versão nem timestamp** recebidos no 503 (RE-02 / DEC-PO-0005). Ao atualizar com a API de volta e saudável ⇒ Saudável (CA-05).
- **Escopo visual:** do UX (especificação de interface UX-ESPEC-DEM-2026-001-TASK-0004, aprovada com ressalvas — DEC-PO-0005); esta EF não o altera.

## 4. Regras aplicadas
| Regra | Texto resumido | Onde se aplica |
|---|---|---|
| RN-0001 v1.2 | A resposta contém apenas status, versão e timestamp; proibido dado pessoal, credencial, segredo, token e detalhe interno de infraestrutura/implementação | Esquema fechado da resposta; erros sem detalhe; cabeçalhos sem revelar servidor/framework (ET-0001 RT-02, RT-08, RT-09, RT-12) |
| RN-0002 v1.2 | Ausência de resposta saudável e válida (sem resposta, tempo esgotado, erro, conteúdo inválido ou HTTP 503 de contrato) = indisponível; nunca exibir valor anterior como atual, nunca assumir "saudável" nem tratar o 503 como operacional; no 503 a tela não exibe versão/timestamp (RE-02) | Regras de consumo (ET-0001 seção 5); tempo limite de 5 s (DEC-AS-0001, confirmada na DEC-ARQ-0002 e aceita pelo PO como premissa); `503` com `status` `"unavailable"` |
| Diretrizes do ADR-0003 (v1.1 aceito) e DEC-ARQ-0002 | Contrato interno e sem autenticação; somente leitura; formato dos campos; CORS só do Portal | ET-0001 seção 4 |

## 5. Comportamento por cenário (resumo funcional; detalhe e matriz completa na ET-0001 seção 8)
| ID | Cenário | O que o consumidor vê | Regra |
|---|---|---|---|
| CE-01 | API em execução normal | `200` com status `"ok"`, versão e timestamp; tela Saudável com valores brutos + UTC da mesma consulta | US-0001 CA-01..04; US-0002 CA-01, CA-02 |
| CE-02 | Processo da API em encerramento | `503` com status `"unavailable"` (mesmo esquema, sem causa); tela Erro genérico **sem** exibir versão nem timestamp (RE-02) | US-0001 CA-07; US-0002 CA-03 caso (b); RN-0002; REQ-0001 item 2 |
| CE-03 | API fora do ar (sem resposta) | Tela Erro (caso (a): status não pôde ser obtido) | US-0002 CA-03 caso (a); RN-0002 |
| CE-04 | Sem resposta em 5 s | Consulta abortada; tela Erro (caso (a)); sem nova tentativa automática | US-0002 CA-03 caso (a); RN-0002; DEC-AS-0001 |
| CE-05 | Erro HTTP inesperado (`500` ou outro ≠ 200 e ≠ 503 de contrato) | Tela Erro (caso (a)); sem detalhe interno | US-0001 CA-09; US-0002 CA-03 caso (a); REQ-0001 item 4; REQ-0004; RN-0001; RN-0002 |
| CE-06 | Conteúdo inválido ou `200` com status diferente de `"ok"` | Tela Erro (caso (a)) | US-0002 CA-03 caso (a); RN-0002 |
| CE-07 | Método inválido (`POST`, `PUT`, `PATCH`, `DELETE`, outros, exceto `HEAD` tolerado) | `405` com `Allow: GET, HEAD` (DEC-ARQ-0002); sem detalhe interno. O Portal só usa `GET` | US-0001 CA-08; REQ-0001 item 3; RN-0001 |
| CE-08 | Origem diferente da do Portal (CORS negado) | Leitura bloqueada pelo navegador; tela Erro (caso (a)) | US-0002 CA-03 caso (a); ADR-0003; DEC-ARQ-0002 L-06 |
| CE-12 | Duas ou mais chamadas sobre a mesma instância | Status e versão iguais; timestamp pode variar; logs permitidos; nenhum dado persistido nem estado de negócio alterado | US-0001 CA-06; REQ-0001 |

## 6. Fora de escopo
Persistência; verificação de dependências (banco/serviços externos); autenticação (contrato interno, ADR-0003); métricas e alertas; Mobile; histórico e gráficos; polling automático; *readiness* (`/ready`, quando existir dependência — ADR-0003).

## 7. Matriz de rastreabilidade
Legenda das seções: **EF** = esta especificação; **ET** = ET-0001 v1.2; **OAS** = `openapi.yaml` 1.0.0. Fontes de CA/REQ/RN: **v1.2 vigente** (G1).

### 7.1 Critérios de aceite da US-0001
| CA (US-0001 v1.2) | RN | REQ | EF | ET | OAS |
|---|---|---|---|---|---|
| CA-01 Resposta com os três campos (HTTP 200) | — | REQ-0001 item 1 | §3 UC-01; §5 CE-01 | §4 RT-01, RT-02; §7.1; §14 | `paths./health.get`; `schemas.HealthOk` |
| CA-02 Status saudável (valor permitido) | — | REQ-0001 item 1 | §5 CE-01 | §4 RT-03 | `HealthOk.status` = `ok` |
| CA-03 Timestamp | — | REQ-0001 item 1 | §5 CE-01 | §4 RT-05; §7.1; §13 DEC-AS-0002 | `schemas.Timestamp` |
| CA-04 Versão rastreável (manifesto + tag, sem hash) | — | REQ-0001 item 1 | §3 UC-01; §5 CE-01 | §4 RT-04; §3 PS-02; §7.1; §13 DEC-AS-0003 / DEC-ARQ-0002 L-07 | `schemas.ServiceVersion` |
| CA-05 Sem dados sensíveis | RN-0001 | REQ-0004 | §4; §5 CE-05, CE-07 | §4 RT-08, RT-09, RT-12; §8 CE-13, CE-14 | `ProblemBase`; `components.headers`; esquemas com `additionalProperties: false` |
| CA-06 Somente leitura (2+ chamadas; logs permitidos; timestamp pode variar) | — | REQ-0001 item 1 | §3 UC-01 (pós-condição); §5 CE-12 | §4 RT-01; §8 CE-12 | `operationId getHealth` (seguro e idempotente) |
| CA-07 Indisponibilidade (HTTP 503, `"unavailable"`) | RN-0001, RN-0002 | REQ-0001 item 2 | §3 UC-01 (alternativo); §5 **CE-02** | §4 RT-06; §7.2; §8 CE-02 | `schemas.HealthUnavailable`; `responses.Unavailable` |
| CA-08 Método não permitido (HTTP 405, `Allow: GET, HEAD`) | RN-0001 | REQ-0001 item 3 | §5 **CE-07** | §4 RT-07, RT-16; §7.3; §8 CE-07 | `responses.MethodNotAllowed`; `headers.Allow` |
| CA-09 Erro interno inesperado (HTTP 500 padronizado) | RN-0001 | REQ-0001 item 4, REQ-0004 | §5 **CE-05** | §4 RT-08; §7.4; §8 CE-05 | `schemas.ProblemInternalError`; `responses.InternalError` |

### 7.2 Critérios da US-0002 que dependem do contrato (lado consumidor)
| CA (US-0002 v1.2) | RN | REQ | EF | ET | OAS |
|---|---|---|---|---|---|
| CA-01 Exibe os dados da API (valores brutos + timestamp UTC da mesma consulta) | — | REQ-0002 | §3 UC-02; §5 CE-01 | §5 itens 2 e 7 | `HealthOk` |
| CA-02 Estado saudável legível | — | REQ-0002 | §3 UC-02 | §5 item 2 | `HealthOk.status` |
| CA-03 Erro ou indisponível (caso (a) falha; caso (b) 503, RE-02: sem versão/timestamp na tela) | RN-0002, RN-0001 | REQ-0003, REQ-0001 item 2 | §5 CE-02 (b), CE-03..CE-08 (a) | §5; §7.2; §8; §13 DEC-AS-0001 | `responses.Unavailable`, `MethodNotAllowed`, `InternalError` |
| CA-04 Carregamento (passa por Carregando; valores anteriores removidos do DOM) | RN-0002 | REQ-0002 | §3 UC-02 | §5 itens 1 e 4 | — (UX) |
| CA-05 Recuperação | RN-0002 | REQ-0003 | §3 UC-02 | §5 itens 1 e 4 | — |
| CA-06 Sem dados sensíveis na tela (status/versão/timestamp só no estado saudável) | RN-0001 | REQ-0004 | §4 | §5 itens 5 e 6; RT-12 | — |

### 7.3 Regras e requisitos
| RN / REQ (v1.2 vigente) | Cobertura |
|---|---|
| RN-0001 | CA-05 e CA-07 (US-0001), CA-06 (US-0002): ET RT-02, RT-08, RT-09, RT-12; OAS esquemas fechados |
| RN-0002 | CA-03, CA-04 e CA-05 (US-0002): ET §5, §7.2, §8; DEC-AS-0001; RE-02 no CE-02 |
| REQ-0001 | Itens 1–4: ET RT-01..RT-08; OAS `paths./health.get` (200, 503, 405, 500) |
| REQ-0003 | ET §5, §8 CE-02..CE-08; DEC-AS-0001 (tempo limite e sem nova tentativa automática) |
| REQ-0004 | ET RT-08, RT-09, RT-12; US-0001 CA-05 e CA-09 |

## 8. Lacunas e pendências (dono)
Consolidadas na ET-0001 seção 12.
- **L-08 (PO, resolvida no conteúdo):** US-0001, US-0002 e REQ-0004 v1.1/v1.2 citam classe **R3** (DEC-ARQ-0001). O fechamento formal do CONF-0001 permanece com a **DOC** (o PO não fecha o registro; a AS não o altera).
- **L-11 (PO, resolvida — DEC-PO-0006):** o escopo passou a incluir HTTP 503 (US-0001 CA-07, REQ-0001 item 2; tela = US-0002 CA-03 caso (b), RE-02), 405 (CA-08, REQ-0001 item 3) e 500 (CA-09, REQ-0001 item 4 e REQ-0004; tela caso (a)). O CA-04 foi alinhado ao ADR-0002 (manifesto + tag, sem hash). Incorporado nesta v1.2.
- **L-01 a L-07 (ARQ, decididas — DEC-ARQ-0002):** o parecer prévio fecha formato de erro, HEAD/OPTIONS, `X-Request-Id`, cabeçalhos, 503/testabilidade, CORS e as DEC-AS-0001..0003 (com aperto do regex de `version`). Residual: valores de porta/origem no ambiente (OPS/FS, TASK-0012); implementação do gancho de encerramento gracioso (ADR-0001 v2 D8 item 10; spike antes do CA-07). Detalhe na ET §12.
- **L-09 (DOC):** modelos de EF/ET/contrato e `INDEX.md` ainda ausentes.
- **L-10 (ORQ/ARQ) — fechada na v1.3:** a AH-0001 foi substituída pela AH-0003 ("Aprovo AH-0003", 26/11/2026 14:54), o ADR-0001 v2.0 foi aceito e o G3 (TASK-0007) foi concluído com ressalvas (R1 = esta revisão e a ET-0001 v1.4). A ressalva do G1 (reabertura de CA pelo PO se os ADR mudarem) permanece com o PO.

## 9. Histórico de versões
| Versão | Data/hora | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 12:27 | AS | Criação (TASK-0006) (commit 950ebff) |
| 1.1 | 26/11/2026 12:33 | AS | Registra L-11 (cobertura funcional de `503`/`405`/`500`) (commit d836bc6) |
| 1.2 | 26/11/2026 12:43 | AS | Ajustes pedidos pelo PO (DEC-PO-0006): matriz §7.1 com CA-07/08/09 (CE-02, CE-05, CE-07); CA-04 manifesto+tag; CA-06 (2+ chamadas, logs, timestamp variável); US-0002 CA-01/03/04; §8 registra L-08/L-11 resolvidas no conteúdo. Fontes US/REQ/RN v1.2 vigente (G1). Toma nota da DEC-ARQ-0002. |
| 1.3 | 26/11/2026 15:16 | AS | R1 do G3: fecha a L-10 (AH-0001 → AH-0003; ADR-0001 v2.0 aceito; G3 concluído com ressalvas); atualiza a nota sobre a L-01..L-07 e o estado do contrato. Sem mudança funcional (CA/RN/REQ/matriz §7 inalterados). |
