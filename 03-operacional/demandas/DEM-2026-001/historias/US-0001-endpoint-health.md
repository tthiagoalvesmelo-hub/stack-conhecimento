---
id: US-0001
titulo: "Consultar o status da API pelo endpoint GET /health"
tipo: us
versao: 1.2
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:18-03:00
atualizado_em: 2026-11-26T12:41-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, TASK-0005, REQ-0001, REQ-0004, RN-0001, US-0002, ADR-0002, ADR-0003, DEC-ARQ-0001, DEC-PO-0004, DEC-PO-0006]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (condição 1 do G1):** formatos, 503/405/500, tempo limite de 5 s e “sem login” dependem dos ADR-0002/0003 ainda propostos; se mudarem no G3, o PO reabre os CA afetados. Implementação depende da AH-0001.
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
- Dentro: recurso `GET /health` na API base do Portal Web (a criar), retornando status, versão e timestamp no caminho saudável (HTTP 200) e, como premissa do ADR-0003 proposto (DEC-PO-0006, alternativa A), o caminho de indisponibilidade HTTP 503 com o mesmo esquema (REQ-0001, REQ-0004, RN-0001). Também o comportamento de método não permitido (HTTP 405) e o erro interno inesperado (HTTP 500 padronizado, sem detalhe interno).
- Fora: persistência de dados; verificações de dependências (banco, serviços externos); autenticação; métricas e alertas; Mobile; decisão de stack (ADR-0001 / AH-0001).

## Premissas de formato (ADR propostos — não são decisão do PO)
Enquanto os ADR-0002 e ADR-0003 estiverem com status **proposto**, os valores abaixo são **premissa de teste** (fonte: MSG-RET TASK-0003, commit 362ea35). Se o ARQ alterar o ADR na aceitação, os CA remeterão à ET/ADR vigente, sem o PO inventar formato.
- Nomes dos campos em inglês: `status`, `version`, `timestamp`.
- HTTP 200 ⇒ `status: "ok"`; HTTP 503 ⇒ `status: "unavailable"`, mesmo esquema, sem causa/detalhe (alternativa A, DEC-PO-0006).
- `version`: SemVer 2.0.0 (`MAJOR.MINOR.PATCH`, pré-release opcional `-rc.N`); **sem** metadados de build e **sem** hash de commit (ADR-0002). Origem (manifesto `package.json`) depende da aceitação do ADR-0001 / AH-0001.
- `timestamp`: ISO 8601 / RFC 3339 em UTC com `Z` e milissegundos; tolerância de verificação a fechar na ET (sugestão do ARQ: ± 5 s).
- Contrato interno, sem autenticação, exposição só em rede local/interna (L4). Versão não é considerada sensível nessa exposição (ADR-0002). Se a exposição mudar, reavaliar (R3/N3 + AH).
- Outros métodos: HTTP 405 com cabeçalho `Allow: GET` (e HEAD tolerado) — ADR-0003 proposto.

## Critérios de aceite
> Onde o critério cita "o formato definido", leia: o formato registrado na ET/ADR **vigente**. Até lá, vale a premissa da seção anterior.

- **CA-01 — Resposta com os três campos.** *Dado* que a API base está em execução e apta a atender, *quando* um cliente faz `GET /health`, *então* a resposta é HTTP 200, `Content-Type` JSON, e o corpo contém os campos `status`, `version` e `timestamp`, todos presentes, não nulos e não vazios.

- **CA-02 — Status saudável.** *Dado* que a API está em execução normal (liveness do processo), *quando* um cliente faz `GET /health`, *então* o campo `status` indica o estado operacional/saudável, usando um dos valores permitidos definidos na ET (premissa: `"ok"`).

- **CA-03 — Timestamp.** *Dado* uma resposta de `GET /health` (200 ou, se vigente no contrato, 503), *quando* o `timestamp` é verificado, *então* ele está no formato definido e corresponde ao instante em que a resposta foi gerada (dentro da tolerância definida na ET).

- **CA-04 — Versão rastreável.** *Dado* uma instância da API em execução a partir de um artefato conhecido, *quando* um cliente faz `GET /health`, *então* o campo `version` está no formato definido na ET/ADR vigente e é idêntico à fonte de verdade daquela execução (conforme o ADR-0002 proposto: valor do manifesto do serviço e, quando houver, a tag de release correspondente), de modo que o QA compare os valores sem ambiguidade e **sem exigir hash de commit na resposta**.

- **CA-05 — Sem dados sensíveis.** *Dado* qualquer resposta de `GET /health` (incluindo 405, 503 e 500), *quando* corpo e cabeçalhos são inspecionados, *então* não contêm dados pessoais, credenciais, segredos, tokens nem detalhes internos (nomes de máquina, caminhos, IPs, variáveis de ambiente, versões de runtime/dependências, hash de commit, stack trace) — RN-0001, REQ-0004.

- **CA-06 — Somente leitura.** *Dado* que `GET /health` é chamado duas ou mais vezes sobre a mesma instância, *quando* as chamadas terminam, *então* não há criação, alteração nem exclusão de dados persistidos nem de estado de negócio. Logs de auditoria/acesso são permitidos. Os campos de status e versão permanecem iguais; o timestamp pode variar. O recurso permanece somente leitura.

- **CA-07 — Indisponibilidade (HTTP 503).** *Dado* que o contrato vigente prevê o caminho de indisponibilidade (premissa do ADR-0003 proposto; DEC-PO-0006, alternativa A), *quando* a API está em encerramento ou de outro modo indisponível segundo a ET, *então* `GET /health` responde HTTP 503 com o mesmo esquema do 200 (`status`, `version`, `timestamp`), `status` igual ao valor de indisponibilidade definido na ET (premissa: `"unavailable"`), **sem** causa, detalhe interno ou mensagem técnica (RN-0001). Este caminho não é o estado saudável (RN-0002). Se o ADR/contrato vigente não incluir esse valor, este CA não se aplica até nova decisão.

- **CA-08 — Método não permitido.** *Dado* a premissa do ADR-0003 proposto, *quando* um cliente chama `/health` com um método diferente de `GET` (e de `HEAD`, se a ET o tolerar), *então* a resposta é HTTP 405 e inclui o cabeçalho `Allow` listando `GET` (e `HEAD`, se aplicável). Sem corpo com detalhes internos (CA-05).

- **CA-09 — Erro interno inesperado (HTTP 500).** *Dado* que ocorre uma falha interna que impede responder HTTP 200 ou o 503 de contrato, *quando* um cliente faz `GET /health`, *então* a API responde HTTP 500 no formato de erro padronizado definido na ET (premissa do ADR-0003 proposto: `application/problem+json` apenas com `type`, `title` e `status`), **sem** causa, caminho, stack trace ou outro detalhe interno (CA-05, RN-0001, REQ-0004). Este caminho não é estado saudável. A tela o trata como US-0002 CA-03, caso (a). O formato exato dos campos de erro é decisão técnica (AS/ARQ).

## Dependências
- ARQ (TASK-0003, Parcial): ADR-0001/0002/0003 propostos; classe de risco R3 (DEC-ARQ-0001); stack aguarda AH-0001. Sem a aceitação dos ADR e da ET, o QA formaliza os oráculos de CA-02 a CA-04 e CA-07/CA-08/CA-09 como premissa.
- AS (TASK-0006): EF/ET e OpenAPI; tolerância do timestamp e tempo limite do cliente.
- G1 (escopo) antes do planejamento técnico.

## Rastreio
Solicitação original (DEM-2026-001) → REQ-0001, REQ-0004, RN-0001 → US-0001 (CA-01 a CA-09) → TASK-0006/0007/0008/0009/0010/0011 → CT (QA, por CA) → entrega (G8).

## Definition of Ready (situação em 26/11/2026 12:32)
Objetivo e valor: OK · Critérios numerados e verificáveis: OK (ajustes da TASK-0005 incorporados na v1.1; testabilidade favorável com ressalvas) · Dependências identificadas: OK (ADR propostos; AH-0001 aberta) · Protótipo: N/A (sem interface nesta US) · Contexto técnico: Parcial (TASK-0003) · Risco: R3 confirmado.
