---
id: PARECER-ARQ-DEM-2026-001-G3
titulo: "Parecer técnico do ARQ no G3 — contrato OpenAPI, ET-0001 e L-12 — DEM-2026-001 [TESTE]"
tipo: parecer
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:06-03:00
atualizado_em: 2026-11-26T15:06-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, TASK-0007, TASK-0008, AH-0003, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0001, DEC-ARQ-0002, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-ARQ-0011, ET-0001, EF-0001, US-0001, US-0002, L-12]
substitui: null
substituido_por: null
---

# Parecer técnico do ARQ — G3 · DEM-2026-001 [TESTE] · TASK-0007

> America/São Paulo. Fase de testes internos. Estado operacional: Normal. **Resultado: APROVADO COM RESSALVAS.** Quem registra o gate é o ORQ.

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
