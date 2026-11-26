---
id: US-0001
titulo: "Consultar o status da API pelo endpoint GET /health"
tipo: us
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:18-03:00
atualizado_em: 2026-11-26T12:18-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, REQ-0001, REQ-0004, RN-0001, US-0002]
substitui: null
substituido_por: null
---

# US-0001 — Consultar o status da API pelo endpoint GET /health

> [TESTE] DEM-2026-001 · TASK-0002 · Fluxo 01 · Prioridade Normal (CPO, G0) · Classe de risco R2 (padrão; ARQ confirma) · Tipo: Funcionalidade nova.

## História
**Como** consumidor técnico do health-check (operador/equipe técnica interna e, futuramente, ferramentas de monitoramento — premissa de teste, DEC-PO-0002),
**quero** consultar `GET /health` na API base do Portal Web,
**para** saber rapidamente se a API está respondendo e qual versão está em execução.

## Valor
Dá um sinal objetivo e barato de disponibilidade e versão da API, base para a tela de status (US-0002) e, no futuro, para verificações de implantação e monitoramento.

## Escopo
- Dentro: recurso `GET /health` na API base do Portal Web (a criar), retornando status, versão e timestamp (REQ-0001, REQ-0004).
- Fora: persistência de dados; verificações de dependências (banco, serviços externos); autenticação; métricas e alertas; Mobile; qualquer decisão de stack, formato ou contrato (ver Dependências).

## Critérios de aceite
> Nomes dos campos, valores de status e formatos de versão/timestamp são definidos pelo ARQ (TASK-0003) e pelo AS (EF/ET); o PO só exige que existam, sejam verificáveis e coerentes. Onde o critério cita "o formato definido", leia: o formato registrado na ET/ADR vigente.

- **CA-01 — Resposta com os três campos.** *Dado* que a API base está em execução, *quando* um cliente faz `GET /health`, *então* a resposta é HTTP 200 e o corpo contém os campos status, versão e timestamp, todos presentes e não vazios.
- **CA-02 — Status saudável.** *Dado* que a API está em execução normal, *quando* um cliente faz `GET /health`, *então* o campo status indica o estado operacional/saudável, usando um dos valores permitidos definidos na ET.
- **CA-03 — Timestamp.** *Dado* uma resposta de `GET /health`, *quando* o timestamp é verificado, *então* ele está no formato definido e corresponde ao instante em que a resposta foi gerada (dentro da tolerância definida na ET).
- **CA-04 — Versão rastreável.** *Dado* uma versão da API em execução, *quando* um cliente faz `GET /health`, *então* o campo versão está no formato definido e é igual à versão registrada daquela execução (build/commit), de modo que o QA consegue comparar os dois valores.
- **CA-05 — Sem dados sensíveis.** *Dado* qualquer resposta de `GET /health`, *quando* corpo e cabeçalhos são inspecionados, *então* não contêm dados pessoais, credenciais, segredos, tokens nem detalhes internos (nomes de máquina, caminhos, variáveis de ambiente, stack trace) — RN-0001, REQ-0004.
- **CA-06 — Somente leitura.** *Dado* que `GET /health` é chamado repetidas vezes, *quando* as chamadas terminam, *então* nenhum dado nem estado do sistema foi alterado (o recurso não tem efeitos colaterais).

## Dependências
- ARQ (TASK-0003): stack, estrutura do projeto, formato da versão e do timestamp, classe de risco, exposição do endpoint (interna/pública) e autenticação. Sem isso o AS não fecha a ET e o QA não fecha os casos de CA-02 a CA-04.
- G1 (escopo) antes do planejamento técnico.

## Rastreio (solicitação ↔ requisito ↔ atividade ↔ teste ↔ entrega)
Solicitação original (DEM-2026-001) → REQ-0001, REQ-0004, RN-0001 → US-0001 → atividades propostas A2, A3, A4, A5, A6, A7 (ver analise-po-task-0002.md) → CT (QA, por CA) → entrega (a preencher no G8).

## Definition of Ready (situação em 26/11/2026)
Objetivo e valor: OK · Critérios numerados e verificáveis: OK (testabilidade a confirmar pelo QA antes do G1) · Dependências identificadas: OK (ARQ aberto) · Protótipo: N/A (sem interface) · Contexto técnico: pendente (TASK-0003) · Responsáveis: propostos · Risco: R2 a confirmar pelo ARQ.
