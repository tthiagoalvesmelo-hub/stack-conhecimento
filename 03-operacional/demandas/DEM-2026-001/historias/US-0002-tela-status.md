---
id: US-0002
titulo: "Ver o status da API em uma tela simples do Portal Web"
tipo: us
versao: 1.1
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:19-03:00
atualizado_em: 2026-11-26T12:32-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, TASK-0004, TASK-0005, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, US-0001, ADR-0003, DEC-PO-0002, DEC-PO-0005, DEC-PO-0006]
substitui: null
substituido_por: null
---

# US-0002 — Ver o status da API em uma tela simples do Portal Web

> [TESTE] DEM-2026-001 · Fluxo 01 · Prioridade Normal (CPO, G0; DEC-PO-0004, pontuação 2,8) · Classe de risco **R3** (DEC-ARQ-0001) · Tipo: Funcionalidade nova.
> **Versão 1.1** (26/11/2026, America/Sao_Paulo): incorpora premissas do ADR-0003 proposto, a validação do protótipo (DEC-PO-0005, Aprovado com ressalvas) e os ajustes de testabilidade da QA (TASK-0005, DEC-PO-0006). Status **em-revisao**: prontos para o G1; a promoção a vigente fica para o G1.

## História
**Como** operador/equipe técnica interna (premissa de teste — público da tela não definido pela CPO, DEC-PO-0002),
**quero** abrir uma tela simples no Portal Web que mostre o status da API (status, versão e timestamp),
**para** verificar a saúde da API sem precisar chamar o endpoint manualmente e perceber de imediato quando ela está indisponível.

## Valor
Torna o sinal de US-0001 visível a pessoas e valida a integração Portal ↔ API desde o início do projeto.

## Escopo
- Dentro: tela de status no Portal Web (a criar) que consome `GET /health` (US-0001) e trata sucesso, carregamento e falha/indisponibilidade (REQ-0002, REQ-0003, REQ-0004, RN-0002).
- Fora: histórico de status, gráficos, alertas, notificações, múltiplos serviços, Mobile, atualização automática (polling — RE-04, demanda futura); qualquer solução visual, de navegação ou de acesso além do comportamento aqui definido (UX/UI e ARQ).

## Premissas (até confirmação do dono)
- Público = operador/equipe técnica interna (DEC-PO-0002; lacuna da CPO).
- Tela sem login nesta demanda (L5, ADR-0003 proposto).
- Tempo limite da consulta: orientação de 5 s, a fechar na ET (L6, AS/ARQ).
- Formatos de `status`/`version`/`timestamp` e valores `"ok"` / `"unavailable"`: premissa dos ADR-0002/0003 propostos (ver US-0001).
- Protótipo e spec UX v1.0 (TASK-0004, commit 1290f25) **aprovados com ressalvas** (DEC-PO-0005). D-UX-05 e D-UX-08 aceitos como oráculo do CA-01.

## Critérios de aceite
> A solução visual (layout, textos, indicadores, formato/fuso de exibição do timestamp, ação de atualizar) é do UX/UI; o PO exige o comportamento abaixo. Textos e tokens do protótipo/spec validados servem de oráculo de *copy* e de indicadores, salvo revisão do UX decorrente de mudança de ADR.

- **CA-01 — Exibe os dados da API.** *Dado* que Portal e API estão disponíveis e a API responde de forma saudável (US-0001 CA-01/CA-02), *quando* o usuário abre a tela de status, *então* a tela mostra status, versão e timestamp, com os **valores brutos iguais** aos retornados por `GET /health` **na mesma consulta** (status e versão como recebidos; timestamp UTC no formato da API). A formatação em America/Sao_Paulo é adicional, não substitui o valor bruto (D-UX-05 e D-UX-08, aceitos em DEC-PO-0005).

- **CA-02 — Estado saudável legível.** *Dado* que a API responde com status saudável, *quando* a tela é exibida, *então* ela comunica de forma explícita e distinguível que a API está operacional (não depender apenas de cor). Oráculo de indicadores do protótipo/spec validados: ícone, título ("API operacional"), selo textual ("Saudável") e estilo de borda, além da cor.

- **CA-03 — Estado de erro ou indisponível.** *Dado* que ocorre uma destas situações — (a) a API não responde, o tempo de espera definido na ET se esgota, há erro HTTP inesperado (≠ 200 e ≠ 503 de contrato) ou o corpo está fora do esquema do contrato; ou (b) a API devolve resposta válida de indisponibilidade (HTTP 503 com `status` `"unavailable"`, se o contrato vigente prever esse valor, DEC-PO-0006 alternativa A) —, *quando* o usuário abre ou atualiza a tela, *então* ela exibe um estado de erro/indisponível explícito, nunca “saudável”, não apresenta valores anteriores como se fossem atuais, não apresenta tela em branco nem mensagem técnica interna (RN-0002, RN-0001). No caso (a), informa que o status não pôde ser obtido. No caso (b), a tela **também** usa o mesmo estado de erro genérico e **não exibe versão nem timestamp** recebidos no 503 (DEC-PO-0005, RE-02 / D-UX-03 confirmados). Em ambos os casos, a mensagem permanece genérica (sem código HTTP, URL, host ou stack).

- **CA-04 — Estado de carregamento.** *Dado* que a consulta a `GET /health` está em andamento (primeira abertura ou atualização), *quando* a tela é exibida, *então* ela indica que o status está sendo carregado, passa por esse estado antes de exibir sucesso ou erro, e não mostra valores anteriores ou parciais como se fossem o status atual (os valores da consulta anterior são **removidos do DOM**, não apenas ocultados — D-UX-02, promovido ao CA).

- **CA-05 — Recuperação.** *Dado* que a tela está em estado de erro e a API voltou a responder de forma saudável, *quando* o usuário atualiza a tela (recarregando ou por ação definida pelo UX/UI, no protótipo: botão "Atualizar status"), *então* a tela passa a exibir o status atual (CA-01/CA-02). Se a nova consulta cair no CA-03, permanece o estado de erro.

- **CA-06 — Sem dados sensíveis.** *Dado* qualquer estado da tela (sucesso, carregando, erro), *quando* o conteúdo exibido é inspecionado, *então* ele só contém status, versão, timestamp (apenas no estado saudável) e mensagens genéricas, sem dados pessoais, credenciais, segredos nem detalhes internos (RN-0001, REQ-0004). Valores da API são inseridos somente como texto, nunca como HTML.

## Dependências
- US-0001 (endpoint) ou seu contrato aprovado (G3): o Portal pode ser implementado em paralelo com mocks do contrato (PR-04), nunca antes do G3.
- UX/UI: protótipo e spec v1.0 validados com ressalvas (DEC-PO-0005). Mudanças de ADR podem exigir revisão do UX.
- ARQ (TASK-0003): stack do Portal, forma de consumo da API, regra de acesso à tela (premissa: sem login).
- G1 (escopo) antes do planejamento técnico.

## Rastreio
Solicitação original (DEM-2026-001) → REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002 → US-0002 → TASK-0004 (protótipo), TASK-0006/0008/0009/0010/0011 → CT (QA, por CA) → entrega (G8).

## Definition of Ready (situação em 26/11/2026 12:32)
Objetivo e valor: OK · Critérios numerados e verificáveis: OK (ajustes da TASK-0005 incorporados; D-UX-05/08 aceitos) · Dependências identificadas: OK · Protótipo: Aprovado com ressalvas (DEC-PO-0005) · Contexto técnico: Parcial (TASK-0003; AH-0001) · Risco: R3 confirmado.
