---
id: INDEX
titulo: "Índice do repositório stack-conhecimento"
tipo: indice
versao: 1.0
status: vigente
dono: DOC
autores: [DOC]
aprovado_por: DOC
criado_em: 2026-11-26T13:02-03:00
atualizado_em: 2026-11-26T13:02-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0011, L-09, EF-0001, ET-0001, CONF-0001]
substitui: null
substituido_por: null
---

# INDEX — stack-conhecimento

> Versão 1.0 · 2026-11-26 13:02 (America/Sao_Paulo) · DOC (L-09, TASK-0011 incremento A). Estado do Git no commit-base `13a10bd` mais o ramo `doc/TASK-0011-incremento-a`. Os campos Versão/Status/Último commit vêm do frontmatter e do `git log` dos arquivos. **Em caso de divergência, o arquivo e o histórico do Git prevalecem sobre este índice** (um índice é só ponteiro: ID + caminho + versão, ver `00-memoria/fontes-de-verdade.md`). Quem cria ou muda um documento atualiza este índice (DoD: “contexto.yaml e INDEX atualizados”).

## Como usar
1. Recuperação de contexto: `00-memoria/skills/recuperar-contexto/SKILL.md` (passo 5 aponta para este índice).
2. Atualização da memória: `00-memoria/skills/atualizar-memoria/SKILL.md` (passo 7).
3. IDs e reservas: `00-memoria/convencao-ids.md` e `00-memoria/registro-ids.yaml`. Modelos: pasta `modelos/`.

## 1. Catálogo das pastas
| Pasta | Conteúdo | Dono principal (matriz 7.1) |
|---|---|---|
| `00-memoria/` | Protocolo, IDs, SSOT, conflitos, governança, skills | DOC |
| `01-institucional/` | Produto, regras de negócio (RN), tecnologias, ambientes, segurança | CPO / PO / ARQ |
| `02-tecnica/` | ADR, contratos de API, especificações EF/ET, modelos de dados, débitos técnicos | ARQ / AS / DBA / OPS |
| `03-operacional/` | Demandas (contexto.yaml, historico.md, aprovacoes.md, requisitos, histórias), snapshots, quadro | ORQ |
| `04-incidentes/` | Incidentes, problemas, runbooks, base de conhecimento | SUP |
| `05-releases/` | REL-nnnn (com tag Git) | OPS |
| `06-qualidade/` | Planos e casos de teste, defeitos, pareceres (`PQ-nnnn`, `CR-nnnn`, análises) | QA (pareceres CR: ver matriz 7.1 e AH pendente) |
| `07-agentes/NN-sigla/` | PROMPT.md e notas compartilháveis de cada agente | cada agente / DOC |
| `08-arquivo/` | Demandas e documentos encerrados ou obsoletos | DOC / ORQ |
| `modelos/` | Modelos de documentos e mensagens | DOC |

Fora do Git, em `/workspace/stack-memoria/`: `planilha-operacao/` (espelho CSV das abas), `pacotes-contexto/`, `rascunhos/<sigla>/`, `criacao/`.

## 2. Memória e governança (`00-memoria/`)
| Arquivo | Último commit |
|---|---|
| `00-memoria/protocolo-memoria.md` | 55b315d |
| `00-memoria/convencao-ids.md` | 50329b6 |
| `00-memoria/fontes-de-verdade.md` | 55b315d |
| `00-memoria/glossario.md` | 55b315d |
| `00-memoria/registro-ids.yaml` | 50329b6 |

Conflitos (`00-memoria/conflitos/`):

| Caminho | ID | Versão | Status | Dono | Último commit |
|---|---|---|---|---|---|
| `00-memoria/conflitos/CONF-0001-classe-de-risco-r2-vs-r3.md` | CONF-0001 | 1.1 | resolvido | DOC | 771349e |

Governança (`00-memoria/governanca/`):

| Caminho | ID | Versão | Status | Dono | Último commit |
|---|---|---|---|---|---|
| `00-memoria/governanca/aprovadores.md` | GOV-APROVADORES | 1.0 | vigente | ORQ | 55b315d |
| `00-memoria/governanca/criterios-classificacao.md` | — | — | — | — | 55b315d |
| `00-memoria/governanca/dor-dod.md` | — | — | — | — | 55b315d |
| `00-memoria/governanca/estado-operacional.md` | GOV-ESTADO | 1.0 | vigente | ORQ | 55b315d |
| `00-memoria/governanca/matriz-aprovacoes.md` | — | — | — | — | 55b315d |
| `00-memoria/governanca/mudancas-padrao.md` | GOV-MUDANCAS-PADRAO | 1.0 | vigente | ORQ | 55b315d |
| `00-memoria/governanca/politica-autonomia.md` | — | — | — | — | 55b315d |

Skills de procedimento (`00-memoria/skills/`): `recuperar-contexto`, `atualizar-memoria`, `registrar-adr`, `registrar-incidente` (índice em `00-memoria/skills/README.md`).

## 3. Decisões, especificações e contrato — DEM-2026-001 [TESTE] (`GET /health`)
| Item | ID | Versão | Status | Dono | Caminho | Commit |
|---|---|---|---|---|---|---|
| Especificação funcional | EF-0001 | 1.2 | em-revisao | AS | `02-tecnica/especificacoes/EF-0001-health-check-portal-api.md` | 3a41a2c |
| Especificação técnica | ET-0001 | 1.3 | em-revisao | AS | `02-tecnica/especificacoes/ET-0001-health-check-portal-api.md` | bb3e08a |
| Contrato OpenAPI | portal-api | 1.0.0 | **proposto** (G3/TASK-0007 pendente; depende da AH-0001) | ARQ aprova; AS autora | `02-tecnica/contratos-api/portal-api/openapi.yaml` | b3f13d6 (conteúdo); merge `cf660fb` na main |
| Conflito (fechado) | CONF-0001 | 1.1 | resolvido | DOC | `00-memoria/conflitos/CONF-0001-classe-de-risco-r2-vs-r3.md` | 771349e |

ADR e decisões do ARQ (`02-tecnica/`):

| Caminho | ID | Versão | Status | Dono | Último commit |
|---|---|---|---|---|---|
| `02-tecnica/adr/ADR-0001-stack-base-portal-api-e-web.md` | ADR-0001 | 1.0 | proposto | ARQ | 362ea35 |
| `02-tecnica/adr/ADR-0002-versionamento-semver-campo-versao.md` | ADR-0002 | 1.0 | proposto | ARQ | 362ea35 |
| `02-tecnica/adr/ADR-0003-padrao-health-check-get-health.md` | ADR-0003 | 1.0 | proposto | ARQ | 362ea35 |
| `02-tecnica/contratos-api/portal-api/DEC-ARQ-0002-detalhes-contrato-health.md` | DEC-ARQ-0002 | 1.0 | vigente | ARQ | 15b3809 |
| `02-tecnica/contratos-api/portal-api/DEC-ARQ-0003-substituto-ci-local.md` | DEC-ARQ-0003 | 1.0 | vigente | ARQ | d1b0235 |
| `02-tecnica/contratos-api/portal-api/DEC-ARQ-0004-lint-analise-estatica.md` | DEC-ARQ-0004 | 1.0 | vigente | ARQ | d1b0235 |

Regras de negócio (`01-institucional/`):

| Caminho | ID | Versão | Status | Dono | Último commit |
|---|---|---|---|---|---|
| `01-institucional/regras-negocio/RN-0001-healthcheck-informacao-nao-sensivel.md` | RN-0001 | 1.2 | vigente | PO | babb9fe |
| `01-institucional/regras-negocio/RN-0002-indisponibilidade-nao-e-saudavel.md` | RN-0002 | 1.2 | vigente | PO | babb9fe |
| `01-institucional/tecnologias.md` | INST-TECNOLOGIAS | 1.0 | rascunho | ARQ | 55b315d |

## 4. Demanda DEM-2026-001 (`03-operacional/demandas/DEM-2026-001/`)
Contexto consolidado (fonte de verdade do contexto): `03-operacional/demandas/DEM-2026-001/contexto.yaml` (último commit 13a10bd; só o ORQ altera estado e etapa). Histórico append-only: `03-operacional/demandas/DEM-2026-001/historico.md`.

| Caminho | ID | Versão | Status | Dono | Último commit |
|---|---|---|---|---|---|
| `03-operacional/demandas/DEM-2026-001/analise-po-task-0002.md` | ANALISE-DEM-2026-001-TASK-0002 | 1.3 | em-revisao | PO | 053a2d4 |
| `03-operacional/demandas/DEM-2026-001/aprovacoes.md` | — | — | — | — | 2ad1838 |
| `03-operacional/demandas/DEM-2026-001/historias/US-0001-endpoint-health.md` | US-0001 | 1.2 | vigente | PO | babb9fe |
| `03-operacional/demandas/DEM-2026-001/historias/US-0002-tela-status.md` | US-0002 | 1.3 | vigente | PO | 053a2d4 |
| `03-operacional/demandas/DEM-2026-001/plano-atividades-g2.md` | PLANO-DEM-2026-001-G2 | 1.1 | vigente | PO | f61a1f9 |
| `03-operacional/demandas/DEM-2026-001/requisitos/REQ-0001-endpoint-get-health.md` | REQ-0001 | 1.2 | vigente | PO | babb9fe |
| `03-operacional/demandas/DEM-2026-001/requisitos/REQ-0002-tela-de-status-portal.md` | REQ-0002 | 1.2 | vigente | PO | babb9fe |
| `03-operacional/demandas/DEM-2026-001/requisitos/REQ-0003-estado-de-erro-tela.md` | REQ-0003 | 1.2 | vigente | PO | babb9fe |
| `03-operacional/demandas/DEM-2026-001/requisitos/REQ-0004-sem-dados-sensiveis.md` | REQ-0004 | 1.2 | vigente | PO | babb9fe |
| `03-operacional/demandas/DEM-2026-001/validacao-po-prototipo-task-0004.md` | DEC-PO-0005 | 1.0 | em-revisao | PO | af208f2 |

## 5. Qualidade (`06-qualidade/`)
| Caminho | ID | Versão | Status | Dono | Último commit |
|---|---|---|---|---|---|
| `06-qualidade/pareceres/analise-testabilidade-task-0005.md` | ANALISE-TESTABILIDADE-DEM-2026-001-TASK-0005 | 1.0 | vigente | QA | 80e9184 |
| `06-qualidade/pareceres/parecer-planejamento-g2-task-0010.md` | PARECER-G2-DEM-2026-001-TASK-0010 | 1.0 | vigente | QA | 40c8ace |

Observação: pareceres CR-nnnn e PQ-nnnn ainda não existem (contadores CR: 0, PQ: 0 em `registro-ids.yaml`). Local do CR-nnnn na fase atual: `06-qualidade/pareceres/CR-nnnn-<slug>.md` (convencao-ids v1.1).

## 6. Artefatos de UX e agentes (`07-agentes/`)
- Entrega de UX da DEM-2026-001: `07-agentes/06-ux/prototipos/DEM-2026-001-US-0002-tela-status/` — especificação `UX-ESPEC-DEM-2026-001-TASK-0004` v1.0 (em revisão) e `prototipo-tela-status.html`. Prefixo `UX-nnnn` proposto, alias pendente do endosso do UX (L-UX-01).
- Parecer técnico do ARQ: `07-agentes/07-arq/parecer-tecnico-DEM-2026-001-g2.md`.

| Agente (pasta) | ID das notas | Versão |
|---|---|---|
| `00-orq` | AGT-ORQ-NOTAS | 1.0 |
| `01-cpo` | AGT-CPO-NOTAS | 1.0 |
| `02-po` | AGT-PO-NOTAS | 1.0 |
| `03-pmm` | AGT-PMM-NOTAS | 1.0 |
| `04-an` | AGT-AN-NOTAS | 1.0 |
| `05-as` | AGT-AS-NOTAS | 1.0 |
| `06-ux` | AGT-UX-NOTAS | 1.1 |
| `07-arq` | AGT-ARQ-NOTAS | 1.3 |
| `08-fs` | AGT-FS-NOTAS | 1.0 |
| `09-mob` | AGT-MOB-NOTAS | 1.0 |
| `10-dba` | AGT-DBA-NOTAS | 1.0 |
| `11-ops` | AGT-OPS-NOTAS | 1.0 |
| `12-qa` | AGT-QA-NOTAS | 1.0 |
| `13-cr` | AGT-CR-NOTAS | 1.0 |
| `14-doc` | AGT-DOC-NOTAS | 1.0 |
| `15-sup` | AGT-SUP-NOTAS | 1.0 |

Cada pasta tem também o `PROMPT.md` completo do agente.

## 7. Modelos (`modelos/`)
| Arquivo |
|---|
| `modelos/adr.md` |
| `modelos/contrato-api.md` *(novo, L-09)* |
| `modelos/ef.md` *(novo, L-09)* |
| `modelos/et.md` *(novo, L-09)* |
| `modelos/aprovacoes.md` |
| `modelos/conf.md` |
| `modelos/contexto.yaml` |
| `modelos/frontmatter.md` |
| `modelos/historico.md` |
| `modelos/incidente.md` |
| `modelos/msg-ah.md` |
| `modelos/msg-blq.md` |
| `modelos/msg-col.md` |
| `modelos/msg-cons.md` |
| `modelos/msg-ret.md` |
| `modelos/msg-sol.md` |
| `modelos/nota-analise.md` |
| `modelos/pacote-contexto.md` |
| `modelos/parecer-cr.md` |
| `modelos/parecer-pq.md` |
| `modelos/rca.md` |
| `modelos/release.md` |

Modelos de EF, ET e contrato de API (`ef.md`, `et.md`, `contrato-api.md`) derivados de EF-0001 v1.2, ET-0001 v1.2 (a ET está hoje na v1.3; revisão do modelo se a v1.3 mudar a estrutura) e do contrato `portal-api` 1.0.0 (L-09). Se a AH-0001 ou o G3 mudarem ADR ou contrato, o DOC revisa estes modelos (DEC-PO-0007, ressalva).

## 8. Lacunas deste índice
- Linhas com “—” em ID/Versão/Status/Dono: arquivo sem frontmatter padrão (governança: `criterios-classificacao`, `dor-dod`, `matriz-aprovacoes`, `politica-autonomia`; `aprovacoes.md` da demanda). Padronizar é decisão do dono de cada arquivo; a DOC apenas registra.
- `DEC-ARQ-0003` e `DEC-ARQ-0004` estão em `02-tecnica/contratos-api/portal-api/` (local escolhido pelo ARQ); o índice reflete o que existe.
- Não há `01-institucional/produto` (visão e objetivos) nem `02-tecnica/modelos-dados` nesta fase (pastas vazias ou inexistentes).
- Itens de `04-incidentes/`, `05-releases/` e `08-arquivo/`: vazios (só README).
- Planilha (Backlog, Tarefas etc.): fonte de verdade do status; não indexada aqui (fora do Git).
