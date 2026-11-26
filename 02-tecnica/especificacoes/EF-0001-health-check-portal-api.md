---
id: EF-0001
titulo: "Especificação funcional do health-check GET /health da portal-api e consumo pela tela de status"
tipo: ef
versao: 1.1
status: em-revisao
dono: AS
autores: [AS]
aprovado_por: null
criado_em: 2026-11-26T12:27-03:00
atualizado_em: 2026-11-26T12:33-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0006, ET-0001, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, ADR-0003, CONF-0001]
substitui: null
substituido_por: null
---

# EF-0001 — Health-check `GET /health` e consumo pela tela de status

> [TESTE] DEM-2026-001 · TASK-0006 · Fluxo 01 · classe de risco R3 (DEC-ARQ-0001) · autora: AS.
> Rascunho **em revisão**: depende de US/REQ/RN v1.0 (`em-revisao`, G1 pendente) e de ADR-0001/0002/0003 (propostos). A consolidação funcional é do PO; o detalhamento técnico está na ET-0001 v1.1 e o contrato em `02-tecnica/contratos-api/portal-api/openapi.yaml` 1.0.0 (ramo `doc/ET-0001-contrato-portal-api-health`, aguarda ARQ).

## 1. Objetivo
Permitir saber, de forma rápida, objetiva e segura, se a `portal-api` (API base do Portal Web) está respondendo e qual versão do serviço está em execução, e tornar esse sinal visível numa tela simples do Portal — sem expor dado sensível e sem jamais apresentar indisponibilidade como saudável.

## 2. Atores e consumidores
| Ator / consumidor | Papel | Fonte |
|---|---|---|
| Portal Web — tela de status | Consome `GET /health`; exibe status, versão e timestamp, ou o estado de erro (US-0002) | US-0002, REQ-0002, REQ-0003 |
| Operador / equipe técnica interna | Abre a tela e interpreta o estado (premissa de teste DEC-PO-0002; público a confirmar pela CPO) | DEC-PO-0002 |
| Checagem operacional (ferramentas de monitoramento, futuro) | Consulta `GET /health` direto, sem credenciais, na rede interna | US-0001, ADR-0003 |
| `portal-api` | Provedor do recurso | ET-0001 |

## 3. Casos de uso
### UC-01 — Consultar o status da API (US-0001)
- **Ator:** consumidor técnico (Portal ou checagem operacional).
- **Pré-condição:** acesso à rede interna onde a `portal-api` executa; origem do Portal permitida (no caso do Portal).
- **Fluxo principal:** (1) o consumidor envia `GET /health`; (2) a API responde `200` com `status` `"ok"`, `version` (versão do serviço em execução) e `timestamp` (instante da resposta, UTC com milissegundos); (3) o consumidor interpreta a resposta como saudável.
- **Fluxos alternativos:** `503` (processo em encerramento) ⇒ indisponível; método diferente de `GET` ⇒ `405`; erro inesperado ⇒ `500` padronizado; sem resposta/tempo esgotado/corpo inválido ⇒ o consumidor trata como indisponível (cenários na seção 5).
- **Pós-condição:** nenhum dado ou estado do sistema foi alterado (CA-06).

### UC-02 — Ver o status na tela do Portal (US-0002)
- **Ator:** operador / equipe técnica interna.
- **Fluxo principal:** abre a tela ⇒ estado Carregando ⇒ consulta `GET /health` (UC-01) ⇒ resposta válida e `status` `"ok"` ⇒ estado Saudável com status, versão e timestamp iguais aos da resposta.
- **Fluxo de erro:** qualquer falha (seção 5) ⇒ estado Erro explícito, sem valores anteriores e sem mensagem técnica; ao atualizar com a API de volta ⇒ Saudável.
- **Escopo visual:** do UX (especificação de interface UX-ESPEC-DEM-2026-001-TASK-0004); esta EF não o altera.

## 4. Regras aplicadas
| Regra | Texto resumido | Onde se aplica |
|---|---|---|
| RN-0001 v1.0 | A resposta contém apenas status, versão e timestamp; proibido dado pessoal, credencial, segredo, token e detalhe interno de infraestrutura/implementação | Esquema fechado da resposta; erros sem detalhe; cabeçalhos sem revelar servidor/framework (ET-0001 RT-02, RT-08, RT-09, RT-12) |
| RN-0002 v1.0 | Ausência de resposta válida (sem resposta, tempo esgotado, erro, conteúdo inválido) = indisponível; nunca exibir valor anterior como atual nem assumir "saudável" | Regras de consumo (ET-0001 seção 5); tempo limite de 5 s (DEC-AS-0001); `503` com `status` `"unavailable"` |
| Diretrizes do ADR-0003 (proposto) | Contrato interno e sem autenticação; somente leitura; formato dos campos; CORS só do Portal | ET-0001 seção 4 |

## 5. Comportamento por cenário (resumo funcional; detalhe e matriz completa na ET-0001 seção 8)
| ID | Cenário | O que o consumidor vê | Regra |
|---|---|---|---|
| CE-01 | API em execução normal | `200` com status `"ok"`, versão e timestamp; tela Saudável | CA-01..04 |
| CE-02 | Processo da API em encerramento | `503` com status `"unavailable"`; tela Erro | RN-0002 |
| CE-03 | API fora do ar (sem resposta) | Tela Erro | RN-0002 |
| CE-04 | Sem resposta em 5 s | Consulta abortada; tela Erro; sem nova tentativa automática | RN-0002 |
| CE-05 | Erro HTTP (`405`, `5xx`, outro ≠ 200) | Tela Erro; sem detalhe interno | RN-0001, RN-0002 |
| CE-06 | Conteúdo inválido ou `200` com status diferente de `"ok"` | Tela Erro | RN-0002 |
| CE-08 | Origem diferente da do Portal (CORS negado) | Leitura bloqueada pelo navegador; tela Erro | ADR-0003 |
| CE-12 | Consultas repetidas | Mesma estrutura de resposta; só o timestamp muda; nada é alterado | CA-06 |

## 6. Fora de escopo
Persistência; verificação de dependências (banco/serviços externos); autenticação (contrato interno, ADR-0003); métricas e alertas; Mobile; histórico e gráficos; polling automático; *readiness* (`/ready`, quando existir dependência — ADR-0003).

## 7. Matriz de rastreabilidade
Legenda das seções: **EF** = esta especificação; **ET** = ET-0001 v1.1; **OAS** = `openapi.yaml` 1.0.0.

### 7.1 Critérios de aceite da US-0001
| CA (US-0001) | RN | REQ | EF | ET | OAS |
|---|---|---|---|---|---|
| CA-01 Resposta com os três campos (HTTP 200) | — | REQ-0001 | §3 UC-01; §5 CE-01 | §4 RT-01, RT-02; §7.1; §14 | `paths./health.get`; `schemas.HealthOk` |
| CA-02 Status saudável (valor permitido) | — | REQ-0001 | §5 CE-01 | §4 RT-03 | `HealthOk.status` = `ok` |
| CA-03 Timestamp | — | REQ-0001 | §5 CE-01 | §4 RT-05; §7.1; §13 DEC-AS-0002 | `schemas.Timestamp` |
| CA-04 Versão rastreável | — | REQ-0001 | §5 CE-01 | §4 RT-04; §3 PS-02; §7.1; §13 DEC-AS-0003 | `schemas.ServiceVersion` |
| CA-05 Sem dados sensíveis | RN-0001 | REQ-0004 | §4; §5 CE-05 | §4 RT-08, RT-09, RT-12; §8 CE-13, CE-14 | `ProblemBase`; `components.headers`; esquemas com `additionalProperties: false` |
| CA-06 Somente leitura | — | REQ-0001 | §3 UC-01 (pós-condição); §5 CE-12 | §4 RT-01; §8 CE-12 | `operationId getHealth` (seguro e idempotente) |

### 7.2 Critérios da US-0002 que dependem do contrato (lado consumidor)
| CA (US-0002) | RN | REQ | EF | ET | OAS |
|---|---|---|---|---|---|
| CA-01 Exibe os dados da API | — | REQ-0002 | §3 UC-02 | §5 itens 2 e 7 | `HealthOk` |
| CA-02 Estado saudável legível | — | REQ-0002 | §3 UC-02 | §5 item 2 | `HealthOk.status` |
| CA-03 Erro com API indisponível | RN-0002, RN-0001 | REQ-0003 | §5 CE-02..CE-08 | §5; §7.2; §8; §13 DEC-AS-0001 | `responses.Unavailable`, `MethodNotAllowed`, `InternalError` |
| CA-04 Carregamento | — | REQ-0002 | §3 UC-02 | §5 item 1 | — (UX) |
| CA-05 Recuperação | RN-0002 | REQ-0003 | §3 UC-02 | §5 itens 1 e 4 | — |
| CA-06 Sem dados sensíveis na tela | RN-0001 | REQ-0004 | §4 | §5 itens 5 e 6; RT-12 | — |

### 7.3 Regras e requisitos
| RN / REQ | Cobertura |
|---|---|
| RN-0001 | CA-05 (US-0001), CA-06 (US-0002): ET RT-02, RT-08, RT-09, RT-12; OAS esquemas fechados |
| RN-0002 | CA-03, CA-05 (US-0002): ET §5, §7.2, §8; DEC-AS-0001 |
| REQ-0001 | ET RT-01..RT-06; OAS `paths./health.get` |
| REQ-0003 | ET §5, §8 CE-02..CE-08; DEC-AS-0001 (tempo limite e sem nova tentativa automática) |
| REQ-0004 | ET RT-08, RT-09, RT-12 |

## 8. Lacunas e pendências (dono)
Consolidadas na ET-0001 seção 12 (L-01..L-11). Destaques funcionais: REQ-0001/US-0001 só preveem `200` — `503`, `405` e `500` do ADR-0003 não têm CA/REQ de escopo e US-0001 CA-04 cita "build/commit" (PO decide — L-11, apontado pelo QA em TASK-0005); público da tela e exposição interna × pública (CPO/ARQ — contexto.yaml); US/RN ainda `em-revisao` e citando R2 enquanto o contexto confirma R3 (PO — CONF-0001); AH-0001 pendente (ORQ/ARQ).

## 9. Histórico de versões
| Versão | Data/hora | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 12:27 | AS | Criação (TASK-0006) (commit 950ebff) |
| 1.1 | 26/11/2026 12:33 | AS | Registra L-11 (cobertura funcional de `503`/`405`/`500`) |
