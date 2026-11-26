---
id: PARECER-ARQ-DEM-2026-001-G3
titulo: "Parecer técnico do ARQ no G3 — contrato OpenAPI, ET-0001 e L-12 — DEM-2026-001 [TESTE]"
tipo: parecer
versao: 1.1
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:06-03:00
atualizado_em: 2026-11-26T15:19-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, TASK-0006, TASK-0007, TASK-0008, AH-0003, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-ARQ-0011, ET-0001, EF-0001, US-0001, US-0002, L-12]
substitui: null
substituido_por: null
---

# Parecer técnico do ARQ — G3 · DEM-2026-001 [TESTE] · TASK-0007

> America/São Paulo. Fase de testes internos. Estado operacional: Normal. **Resultado (v1.0): APROVADO COM RESSALVAS R1..R5.** **Adendo v1.1 (26/11/2026 15:19):** **R1 fechada.** Quem registra o gate e o status formal da ET é o ORQ.

> **ET-0001 v1.4:** aprovada tecnicamente pelo ARQ para fins do G3. O artefato do AS permanece `em-revisao` neste repositório (o ARQ não o edita); o registro formal fica com o ORQ.
> **OpenAPI 1.0.0:** a prosa da R1 (ramo `doc/TASK-0006-R1-openapi-prosa`, 8494060) está correta; o **ORQ faz o merge `--no-ff`**. O ARQ não mescla.
> **R2..R5 permanecem abertas** (FS, QA, OPS). A liberação da TASK-0008 é do ORQ, após esta confirmação e o plano G2 v1.2 do PO.

## 1. Pré-condição verificada
- **AH-0003 registrada pelo ORQ como aprovada, com a frase literal:** `aprovacoes.md` e `Aprovacoes-humanas.csv` (linha AH-0003: "Aprovada — texto literal: \"Aprovo AH-0003\" (chat do ORQ, 26/11/2026 14:54)", Thiago Melo, sem condições, 24 h), `historico.md` (26/11 14:54) e `contexto.yaml` v32 (c15d4f0). AH-0001 consta "substituída pela AH-0003". O sinal informal anterior ("aprovado AH-0003", conversa do Jarvis) **não** foi usado.
- **ADR-0001 v2.0 aceito** na TASK-0003 (ramo `doc/TASK-0003-stack-dotnet-angular`), que é pré-requisito do G3 e a base deste ramo (empilhado).

## 2. Escopo e fontes
OpenAPI `portal-api` 1.0.0 (idêntico ao do merge cf660fb; último commit de conteúdo b3f13d6); ET-0001 v1.3 (bb3e08a, em revisão, AS); EF-0001 v1.2; ADR-0001 v2.0, ADR-0002 v1.1, ADR-0003 v1.1; DEC-ARQ-0001, 0002, 0007..0010; US-0001/US-0002 v1.2. **Não** edito artefatos do AS.

## 3. Método e evidências
| Evidência | Resultado | Onde |
|---|---|---|
| Validação independente do OpenAPI (`validar-g3-openapi.py`: YAML estrito, OpenAPI 3.1.0 válido pelo `openapi-spec-validator`, exemplos válidos contra os esquemas, `additionalProperties:false`, somente `GET /health`, `security: []`, sem `Retry-After`, `Allow: GET, HEAD`, problem+json de 3 campos, cabeçalhos coerentes) | **90 verificações OK, 0 falhas, 1 informativa** | `07-agentes/07-arq/evidencias-g3/saida-validar-g3-openapi.txt` |
| Padrões de `version`, `timestamp` e UUID em Node 24 (`toISOString()` e `crypto.randomUUID()` sempre satisfazem os padrões; `\n` final rejeitado) | OK | `evidencias-g3/regex-g3.mjs` e `saida-regex-g3.txt` |
| Coerência cruzada ET × OpenAPI × DEC-ARQ-0002 × ADR-0003 v1.1 (`Allow: GET, HEAD`; 503 sem `Retry-After`; preflight 204; `no-store`/`nosniff` em todas as respostas; CORS sem 403; `about:blank`) | Consistente | ET RT-05/07/16, CE-07/11, L-02/L-04/L-05; openapi linhas 37, 67–72, 89, 198 |
| Contrato **interno**, sem autenticação, resposta mínima, sem dado sensível (ADR-0003 critérios a–f) | Atende | OpenAPI + ADR-0003 |
Limite declarado: **nenhum comportamento em runtime foi executado** (SDK .NET não instalado; nada instalado por mim). Os itens **PV** do ADR-0001 v2 D8 são obrigações de teste, não fatos verificados.

## 4. Decisões do G3
| Artefato | Decisão |
|---|---|
| **OpenAPI portal-api 1.0.0** | **Aprovado pelo ARQ (contrato interno, N2) com a ressalva R1.** Mantém-se 1.0.0, sem mudança semântica (análise em `analise-impacto-troca-stack-DEM-2026-001.md` §2). O campo `status-documento` passa de `proposto` a `aprovado` no commit do AS que fechar a R1 (artefato do AS) |
| **ET-0001 v1.3** | **Aprovada com ressalvas**: o comportamento normativo (RT, CE, L-01..L-07, DEC-AS-0001..0003) está coerente e é independente de stack; as **premissas PS-01..PS-09 e as remissões a AH-0001/Node/Fastify/`package.json`/"fábrica" estão desatualizadas** (R1) |
| **L-12** | **Confirmada formalmente** na **DEC-ARQ-0011** (gancho de teste por `WebApplicationFactory<Program>`; fora do OpenAPI; extensão ao 500) |
| **ADR-0002 v1.1 e ADR-0003 v1.1** | **Aceitos** (alçada N1/N2; sem AH adicional) |
| ADR-0001 v2.0 | Já aceito na TASK-0003 (AH-0003) |
| DEC-ARQ-0007..0010 | Vigentes (substituem 0003..0006), emitidas na TASK-0003 |

## 5. Ressalvas e achados
| ID | Ressalva | Dono | Condição |
|---|---|---|---|
| **R1** | Publicar **ET-0001 v1.4** (e EF-0001, linha de L-10) reescrevendo as premissas PS-01..PS-09 conforme o ADR-0001 v2 D8, trocando "fábrica"/`NODE_ENV` por `WebApplicationFactory`/`ASPNETCORE_ENVIRONMENT`, fechando L-10 e L-12 (DEC-ARQ-0011); e ajustar a **prosa** do `openapi.yaml` (cabeçalho linhas 7–9, linhas 32, 90, 281 e `x-stack`) sem alterar `info.version` e **sem tocar** em caminhos, esquemas, exemplos ou cabeçalhos. Lista detalhada: análise de impacto §3 | AS | **Recomendação do ARQ ao ORQ: liberar a TASK-0008 somente após a R1**, para o FS não implementar contra premissas de Node. Não bloqueia o registro do G3 |
| **R2** | Achado informativo: o padrão de `timestamp` do contrato aceita datas inexistentes (`2026-02-31T…Z`), que o `format: date-time` rejeita. Não é defeito (o provedor emite sempre pelo `TimeProvider`; o Portal é leitor tolerante). O **teste de contrato deve aplicar o `format: date-time`**; a biblioteca de validação de esquema (PS-09) deve suportá-lo | QA/FS; aprovação do ARQ à biblioteca | Antes do teste de contrato (G4/G5) |
| **R3** | Itens **PV** do ADR-0001 v2 D8 (ProblemDetails em 404/405/500; `timestamp` com 3 casas; versão sem `+`; cabeçalhos em toda resposta; `Server`; preflight; encerramento gracioso/503; 500 sem detalhe em `Development`) viram **casos de teste obrigatórios** e entram no checklist do CR | FS, QA, CR | Entrada no G4 |
| **R4** | Instalar SDK .NET 10 e Angular CLI e rodar o `verify-local` vazio; **spike** do encerramento gracioso (D8 item 10) antes de o FS fechar o CA-07. Se inviável, volta ao ARQ/PO por MSG-COL | OPS, FS | Antes da TASK-0008 |
| **R5** | Nos testes em .NET usar `\z` (ou equivalente) para as expressões de `version`/`timestamp`/UUID: `$` aceita `\n` final no .NET | FS/QA | Teste de contrato |

## 6. Por que "Aprovado com ressalvas" e não "Pendente da revisão do AS"
(i) O contrato OpenAPI, objeto principal do G3, é válido e independente de stack, com evidência repetível. (ii) A parte desatualizada da ET está **isolada** em premissas já rotuladas por ela mesma como "nada altera o contrato", sem efeito no comportamento normativo. (iii) Reter o G3 não reduz risco: a R1 é editorial e rápida, e o ARQ a controla recomendando ao ORQ a liberação da TASK-0008 só depois dela. Se o ORQ preferir tratar a R1 como bloqueio do gate, o resultado equivalente é "Pendente" até a ET-0001 v1.4; a decisão técnica do ARQ não muda.

## 7. Encaminhamentos
- **AS:** MSG-COL com a R1 (texto no MSG-RET do G3).
- **PO:** nenhum CA muda de comportamento; apenas a premissa de formato da US-0001 (linha ~40) cita `package.json` (análise de impacto §6).
- **ORQ:** registrar o G3 como "Aprovado com ressalvas"; liberar TASK-0008 após a R1 (recomendação); segunda aprovação do ARQ no G4 (R3: DEC-ARQ-0001).
- **QA:** reavaliar o plano de testes (DEC-ARQ-0011 §6; Angular com DOM simulado por padrão).

## 8. Adendo v1.1 — fechamento da R1 (26/11/2026 15:19, America/São Paulo)

A AS entregou a R1 em dois ramos a partir de b606d11. O ORQ já mesclou a ET-0001 v1.4 e a EF-0001 v1.3 na main (9b3dc1b, conteúdo ac391ea). O ramo do `openapi.yaml` (8494060) permanece aberto, área do ARQ. Revisão independente nesta data, contra a lista da análise de impacto §3 e deste parecer §5.

### 8.1 OpenAPI (ramo `doc/TASK-0006-R1-openapi-prosa`, 8494060)
- `validar-g3-openapi.py`: **90 verificações OK, 0 falhas, 1 informativa** (a mesma da v1.0: o padrão de `timestamp` aceita datas inexistentes; o `format: date-time` as rejeita — R2). Evidência: `evidencias-g3/saida-validar-g3-openapi-r1-8494060.txt`.
- Comparação estrutural main (b57eaa1) × ramo: após remover `description`/`summary`/`title` e `x-stack`, as árvores são **idênticas**. As 5 diferenças reais são: `info.description`, `paths./health.get.description`, `components.responses.Unavailable.description`, `info.x-stack.status-documento` (`proposto` → `aprovado`) e `info.x-stack.decisoes` (inclusão de DEC-ARQ-0011 e AH-0003). `info.version` permanece **1.0.0**. Caminhos, esquemas, exemplos e cabeçalhos HTTP não mudam. Evidência: `evidencias-g3/comparacao-estrutural-openapi-main-x-8494060.txt`.
- O ramo altera **somente** `openapi.yaml`. Não toca `historico.md` nem `contexto.yaml`. `merge-tree` com a main atual (b57eaa1) é **limpo**. Evidência: `evidencias-g3/merge-tree-openapi-8494060.txt`.
- A prosa atende à lista da R1 (cabeçalho linhas 7–9, stack, CORS, 503/`WebApplicationFactory`, `x-stack`).

### 8.2 ET-0001 v1.4 e EF-0001 v1.3 (já na main, 9b3dc1b)
- PS-01..PS-09 reescritas contra o ADR-0001 v2 D8 e as DEC-ARQ-0007..0011, com coluna Fonte V/PV. A ET declara que **PV não é afirmado como fato**.
- Comportamento normativo **inalterado**: RT-01..RT-16 (em RT-10 mudou só a célula de fonte); CE-02/CE-05 mudam só o mecanismo de teste (`WebApplicationFactory` / DEC-ARQ-0011), não o oráculo; L-01..L-03, L-06 e L-07 inalteradas; L-04/L-05 atualizam residual/mecanismo, não a regra; DEC-AS-0001..0003 inalteradas.
- **L-10 fechada** (AH-0001 substituída pela AH-0003; ADR-0001 v2 aceito). **L-12 fechada**, confirmada na DEC-ARQ-0011.
- Remissões vigentes a Node/Fastify/`package.json`/`NODE_ENV`/"fábrica"/AH-0001: nenhuma (só histórico ou citação da substituição).
- EF-0001 v1.3: L-10 fechada; sem mudança funcional (CA/RN/REQ/matriz).
- Evidência: `evidencias-g3/revisao-et-0001-v1.4-main.txt`.

### 8.3 Decisão
**R1 fechada**, sem ajustes pendentes da AS. **ET-0001 v1.4 aprovada tecnicamente pelo ARQ para fins do G3.** O ARQ não edita o artefato do AS (o frontmatter permanece `em-revisao` / `aprovado_por: null` até o ORQ registrar). **O ORQ faz o merge `--no-ff`** de `doc/TASK-0006-R1-openapi-prosa` e deste ramo `doc/G3-R1-fechamento`. A liberação da TASK-0008 é do ORQ, depois desta confirmação e do plano G2 v1.2 do PO.

**R2..R5 seguem abertas:** R2 (QA/FS, `format: date-time`); R3 (FS/QA/CR, itens PV do D8); R4 (OPS/FS, SDK .NET 10, Angular CLI e spike do encerramento gracioso); R5 (FS/QA, `\z` nos testes em .NET).
