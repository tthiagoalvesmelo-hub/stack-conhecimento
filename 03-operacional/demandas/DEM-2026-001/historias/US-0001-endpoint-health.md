---
id: US-0001
titulo: "Consultar o status da API pelo endpoint GET /health"
tipo: us
versao: 1.4
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:18-03:00
atualizado_em: 2026-11-26T15:27-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, TASK-0005, REQ-0001, REQ-0004, RN-0001, US-0002, ADR-0002, ADR-0003, DEC-ARQ-0001, DEC-PO-0004, DEC-PO-0006, DEC-PO-0008, AH-0003, ADR-0001]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (1) do G1 (atualizada em 26/11/2026 15:12 (America/Sao_Paulo), DEC-PO-0008):** os ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 foram **aceitos** (AH-0003 aprovada em 26/11/2026 14:54, America/Sao_Paulo, que substitui a AH-0001; G3 registrado em `a271ac1`). Os formatos, caminhos 503/405/500, tempo limite de 5 s e “sem login” seguem esses ADR aceitos. **Ressalva do G3:** R1..R5 (aprovacoes.md, 26/11/2026 15:08) — R1 (ET-0001 v1.4 da AS, condição para liberar a TASK-0008); R2 (teste de contrato com `format: date-time`); ressalva R3 do G3 (itens PV do ADR-0001 v2 D8 como testes obrigatórios antes do G4); R4 (SDK .NET 10 + Angular CLI e spike do encerramento gracioso em ASP.NET Core antes do CA-07); R5 (usar `\z` nas regex .NET). A implementação não depende mais da AH-0001.
>
> **v1.3** (26/11/2026 15:12 (America/Sao_Paulo)) — revisão editorial (DEC-PO-0008): premissas de stack e origem da versão atualizadas para C#/.NET 10 LTS + Angular 22.3 (ADR-0001 v2.0 / AH-0003) e manifesto no `<Version>` do `.csproj` do `portal-api` (ADR-0002 v1.1). Nenhum CA foi reaberto nem alterado. Status **vigente** mantido.
> **v1.4** (26/11/2026 15:27 (America/Sao_Paulo)) — correção editorial só de referência (plano G2 v1.2): nos CA-04, CA-07, CA-08 e CA-09 a expressão "ADR proposto" passa a "ADR v1.1, aceito" (ADR-0002/0003 v1.1 aceitos no G3, `a271ac1`). **Nenhum CA muda de comportamento, de ID ou de oráculo** (DEC-PO-0008 mantida; os 15 CA seguem os mesmos).
# US-0001 — Consultar o status da API pelo endpoint GET /health

> [TESTE] DEM-2026-001 · Fluxo 01 · Prioridade Normal (CPO, G0; DEC-PO-0004, pontuação 2,8) · Classe de risco **R3** (DEC-ARQ-0001) · Tipo: Funcionalidade nova.
> **Versão 1.1** (26/11/2026, America/Sao_Paulo): incorpora respostas do ARQ (TASK-0003, ADR-0002/0003 **propostos** — premissa até a aceitação pelo ARQ; a implementação da stack depende da AH-0001) e os ajustes de testabilidade da QA (TASK-0005, DEC-PO-0006). Status **em-revisao**: prontos para o G1; a promoção a vigente fica para o G1 (ADRs ainda propostos).

## História
**Como** consumidor técnico do health-check (operador/equipe técnica interna e, futuramente, ferramentas de monitoramento — premissa de teste, DEC-PO-0002),
**quero** consultar `GET /health` na API base do Portal Web,
**para** saber rapidamente se a API está respondendo e qual versão está em execução.

## Valor
Dá um sinal objetivo e barato de disponibilidade e versão da API, base para a tela de status (US-0002) e, no futuro, para verificações de implantação e monitoramento.

## Escopo
- Dentro: recurso `GET /health` na API base do Portal Web (a criar), retornando status, versão e timestamp no caminho saudável (HTTP 200) e, conforme o ADR-0003 v1.1 aceito (DEC-PO-0006, alternativa A), o caminho de indisponibilidade HTTP 503 com o mesmo esquema (REQ-0001, REQ-0004, RN-0001). Também o comportamento de método não permitido (HTTP 405) e o erro interno inesperado (HTTP 500 padronizado, sem detalhe interno).
- Fora: persistência de dados; verificações de dependências (banco, serviços externos); autenticação; métricas e alertas; Mobile; decisão de stack (já tomada: ADR-0001 v2.0 / AH-0003 — C#/.NET 10 LTS + Angular 22.3).

## Premissas de formato (ADR aceitos — não são decisão do PO)
Com a AH-0003 aprovada e os ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 **aceitos** (G3, `a271ac1`), os valores abaixo deixam de ser premissa de ADR proposto. A DEC-PO-0008 **não reabre** os CA: o comportamento permanece o dos 15 CA vigentes. A ressalva vigente é a do G3 (R1..R5); a R1 (ET-0001 v1.4) ainda pode alinhar a prosa de premissas da ET, sem mudança semântica do contrato.
- Nomes dos campos em inglês: `status`, `version`, `timestamp`.
- HTTP 200 ⇒ `status: "ok"`; HTTP 503 ⇒ `status: "unavailable"`, mesmo esquema, sem causa/detalhe (alternativa A, DEC-PO-0006; ADR-0003 v1.1 aceito).
- `version`: SemVer 2.0.0 (`MAJOR.MINOR.PATCH`, pré-release opcional `-rc.N`); **sem** metadados de build e **sem** hash de commit (ADR-0002 v1.1 aceito). Origem (manifesto do serviço): elemento `<Version>` do `.csproj` do `portal-api` (`IncludeSourceRevisionInInformationalVersion=false`). Oráculo: valor da resposta = manifesto = tag `portal-api-v<versão>` (quando houver).
- `timestamp`: ISO 8601 / RFC 3339 em UTC com `Z` e milissegundos; tolerância de verificação ±5 s (DEC-AS-0002, confirmada no G3).
- Contrato interno, sem autenticação, exposição só em rede local/interna (L4). Versão não é considerada sensível nessa exposição (ADR-0002 v1.1). Se a exposição mudar, reavaliar (R3/N3 + AH).
- Outros métodos: HTTP 405 com cabeçalho `Allow: GET, HEAD` (ADR-0003 v1.1 / DEC-ARQ-0002 L-02).
- Stack (fora da alçada do PO; ADR-0001 v2.0 aceito, AH-0003): C#/.NET 10 LTS nas APIs e Angular 22.3 no Portal. A AH-0001 (Node 24 + Fastify 5 + Portal estático) foi substituída e não está mais pendente.
- CA-07 (503 no encerramento): o critério permanece válido (DEC-PO-0008). A viabilidade do encerramento gracioso em ASP.NET Core depende do spike previsto na ressalva R4 do G3. Se o spike mostrar inviabilidade, o ARQ volta ao PO e o CA-07 é reaberto.

## Critérios de aceite
> Onde o critério cita "o formato definido", leia: o formato registrado na ET/ADR **vigente**. Até lá, vale a premissa da seção anterior.

- **CA-01 — Resposta com os três campos.** *Dado* que a API base está em execução e apta a atender, *quando* um cliente faz `GET /health`, *então* a resposta é HTTP 200, `Content-Type` JSON, e o corpo contém os campos `status`, `version` e `timestamp`, todos presentes, não nulos e não vazios.

- **CA-02 — Status saudável.** *Dado* que a API está em execução normal (liveness do processo), *quando* um cliente faz `GET /health`, *então* o campo `status` indica o estado operacional/saudável, usando um dos valores permitidos definidos na ET (premissa: `"ok"`).

- **CA-03 — Timestamp.** *Dado* uma resposta de `GET /health` (200 ou, se vigente no contrato, 503), *quando* o `timestamp` é verificado, *então* ele está no formato definido e corresponde ao instante em que a resposta foi gerada (dentro da tolerância definida na ET).

- **CA-04 — Versão rastreável.** *Dado* uma instância da API em execução a partir de um artefato conhecido, *quando* um cliente faz `GET /health`, *então* o campo `version` está no formato definido na ET/ADR vigente e é idêntico à fonte de verdade daquela execução (conforme o ADR-0002 v1.1, aceito: valor do manifesto do serviço e, quando houver, a tag de release correspondente), de modo que o QA compare os valores sem ambiguidade e **sem exigir hash de commit na resposta**.

- **CA-05 — Sem dados sensíveis.** *Dado* qualquer resposta de `GET /health` (incluindo 405, 503 e 500), *quando* corpo e cabeçalhos são inspecionados, *então* não contêm dados pessoais, credenciais, segredos, tokens nem detalhes internos (nomes de máquina, caminhos, IPs, variáveis de ambiente, versões de runtime/dependências, hash de commit, stack trace) — RN-0001, REQ-0004.

- **CA-06 — Somente leitura.** *Dado* que `GET /health` é chamado duas ou mais vezes sobre a mesma instância, *quando* as chamadas terminam, *então* não há criação, alteração nem exclusão de dados persistidos nem de estado de negócio. Logs de auditoria/acesso são permitidos. Os campos de status e versão permanecem iguais; o timestamp pode variar. O recurso permanece somente leitura.

- **CA-07 — Indisponibilidade (HTTP 503).** *Dado* que o contrato vigente prevê o caminho de indisponibilidade (ADR-0003 v1.1, aceito; DEC-PO-0006, alternativa A), *quando* a API está em encerramento ou de outro modo indisponível segundo a ET, *então* `GET /health` responde HTTP 503 com o mesmo esquema do 200 (`status`, `version`, `timestamp`), `status` igual ao valor de indisponibilidade definido na ET (premissa: `"unavailable"`), **sem** causa, detalhe interno ou mensagem técnica (RN-0001). Este caminho não é o estado saudável (RN-0002). Se o ADR/contrato vigente não incluir esse valor, este CA não se aplica até nova decisão.

- **CA-08 — Método não permitido.** *Dado* o ADR-0003 v1.1 (aceito), *quando* um cliente chama `/health` com um método diferente de `GET` (e de `HEAD`, se a ET o tolerar), *então* a resposta é HTTP 405 e inclui o cabeçalho `Allow` listando `GET` (e `HEAD`, se aplicável). Sem corpo com detalhes internos (CA-05).

- **CA-09 — Erro interno inesperado (HTTP 500).** *Dado* que ocorre uma falha interna que impede responder HTTP 200 ou o 503 de contrato, *quando* um cliente faz `GET /health`, *então* a API responde HTTP 500 no formato de erro padronizado definido na ET (ADR-0003 v1.1, aceito: `application/problem+json` apenas com `type`, `title` e `status`), **sem** causa, caminho, stack trace ou outro detalhe interno (CA-05, RN-0001, REQ-0004). Este caminho não é estado saudável. A tela o trata como US-0002 CA-03, caso (a). O formato exato dos campos de erro é decisão técnica (AS/ARQ).

## Dependências
- ARQ (TASK-0003): ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 aceitos (AH-0003; G3 com ressalvas R1..R5, `a271ac1`). Classe de risco R3 (DEC-ARQ-0001). A TASK-0008 espera a R1 (ET-0001 v1.4). O CA-07 depende do spike da R4 (risco, sem reabertura — DEC-PO-0008).
- AS (TASK-0006 / ressalva R1 do G3): EF/ET e OpenAPI; ET-0001 v1.4 pendente (alinha premissas PS à nova stack, sem mudança semântica do contrato).
- G3 aprovado com ressalvas R1..R5 (`a271ac1`).

## Rastreio
Solicitação original (DEM-2026-001) → REQ-0001, REQ-0004, RN-0001 → US-0001 (CA-01 a CA-09) → TASK-0006/0007/0008/0009/0010/0011 → CT (QA, por CA) → entrega (G8).

## Definition of Ready (situação em 26/11/2026 15:12)
Objetivo e valor: OK · Critérios numerados e verificáveis: OK (nenhum CA reaberto, DEC-PO-0008) · Dependências identificadas: OK (ADR-0001 v2.0 / ADR-0002 v1.1 / ADR-0003 v1.1 aceitos; AH-0003 aprovada) · Protótipo: N/A (sem interface nesta US) · Contexto técnico: G3 com ressalvas R1..R5 (ET-0001 v1.4 pendente, R1) · Risco: R3 confirmado; CA-07 condicionado ao spike da R4.
