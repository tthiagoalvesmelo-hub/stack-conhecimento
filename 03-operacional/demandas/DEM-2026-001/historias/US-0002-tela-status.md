---
id: US-0002
titulo: "Ver o status da API em uma tela simples do Portal Web"
tipo: us
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:19-03:00
atualizado_em: 2026-11-26T12:19-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, US-0001]
substitui: null
substituido_por: null
---

# US-0002 — Ver o status da API em uma tela simples do Portal Web

> [TESTE] DEM-2026-001 · TASK-0002 · Fluxo 01 · Prioridade Normal (CPO, G0) · Classe de risco R2 (padrão; ARQ confirma) · Tipo: Funcionalidade nova.

## História
**Como** operador/equipe técnica interna (premissa de teste — público da tela não definido pela CPO, DEC-PO-0002),
**quero** abrir uma tela simples no Portal Web que mostre o status da API (status, versão e timestamp),
**para** verificar a saúde da API sem precisar chamar o endpoint manualmente e perceber de imediato quando ela está indisponível.

## Valor
Torna o sinal de US-0001 visível a pessoas e valida a integração Portal ↔ API desde o início do projeto.

## Escopo
- Dentro: tela de status no Portal Web (a criar) que consome `GET /health` (US-0001) e trata sucesso, carregamento e falha (REQ-0002, REQ-0003, REQ-0004, RN-0002).
- Fora: histórico de status, gráficos, alertas, notificações, múltiplos serviços, Mobile; qualquer solução visual, de navegação ou de acesso (UX/UI e ARQ).

## Critérios de aceite
> A solução visual (layout, textos, indicadores, formato/fuso de exibição do timestamp, ação de atualizar) é do UX/UI; o PO só exige o comportamento abaixo.

- **CA-01 — Exibe os dados da API.** *Dado* que Portal e API estão disponíveis, *quando* o usuário abre a tela de status, *então* a tela mostra status, versão e timestamp, com valores iguais aos retornados por `GET /health` na mesma consulta.
- **CA-02 — Estado saudável legível.** *Dado* que a API responde com status saudável, *quando* a tela é exibida, *então* ela comunica de forma explícita e distinguível que a API está operacional (não depender apenas de cor).
- **CA-03 — Estado de erro com API indisponível.** *Dado* que a API não responde, expira o tempo de espera, responde erro HTTP ou devolve conteúdo inválido, *quando* o usuário abre ou atualiza a tela, *então* ela exibe um estado de erro explícito informando que o status não pôde ser obtido, não exibe valores anteriores como se fossem atuais e não apresenta tela em branco nem mensagem técnica interna (RN-0002).
- **CA-04 — Estado de carregamento.** *Dado* que a consulta a `GET /health` está em andamento, *quando* a tela é exibida, *então* ela indica que o status está sendo carregado, sem mostrar valores nem erro antes da resposta.
- **CA-05 — Recuperação.** *Dado* que a tela está em estado de erro e a API voltou a responder, *quando* o usuário atualiza a tela (recarregando ou por ação definida pelo UX/UI), *então* a tela passa a exibir o status atual (CA-01/CA-02).
- **CA-06 — Sem dados sensíveis.** *Dado* qualquer estado da tela (sucesso, carregando, erro), *quando* o conteúdo exibido é inspecionado, *então* ele só contém status, versão, timestamp e mensagens genéricas, sem dados pessoais, credenciais, segredos nem detalhes internos (RN-0001, REQ-0004).

## Dependências
- US-0001 (endpoint) ou seu contrato aprovado (G3): o Portal pode ser implementado em paralelo com mocks do contrato (PR-04), nunca antes do G3.
- UX/UI: protótipo validado pelo PO (estados saudável, carregando, erro).
- ARQ (TASK-0003): stack do Portal, forma de consumo da API, regra de acesso à tela.
- G1 (escopo) antes do planejamento técnico.

## Rastreio (solicitação ↔ requisito ↔ atividade ↔ teste ↔ entrega)
Solicitação original (DEM-2026-001) → REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002 → US-0002 → atividades propostas A1, A2, A3, A4, A5, A6, A7 (ver analise-po-task-0002.md) → CT (QA, por CA) → entrega (a preencher no G8).

## Definition of Ready (situação em 26/11/2026)
Objetivo e valor: OK · Critérios numerados e verificáveis: OK (testabilidade a confirmar pelo QA antes do G1) · Dependências identificadas: OK · Protótipo: pendente (A1, UX/UI) · Contexto técnico: pendente (TASK-0003) · Responsáveis: propostos · Risco: R2 a confirmar pelo ARQ.
