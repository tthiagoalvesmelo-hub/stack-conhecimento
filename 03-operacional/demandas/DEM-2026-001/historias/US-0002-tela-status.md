---
id: US-0002
titulo: "Ver o status da API em uma tela simples do Portal Web"
tipo: us
versao: 1.4
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:19-03:00
atualizado_em: 2026-11-26T15:12-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, TASK-0004, TASK-0005, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, US-0001, ADR-0003, DEC-PO-0002, DEC-PO-0005, DEC-PO-0006, DEC-PO-0008, AH-0003, ADR-0001, ADR-0002]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (1) do G1 (atualizada em 26/11/2026 15:12 (America/Sao_Paulo), DEC-PO-0008):** os ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 foram **aceitos** (AH-0003 aprovada em 26/11/2026 14:54, America/Sao_Paulo, que substitui a AH-0001; G3 registrado em `a271ac1`). Os formatos, caminhos 503/405/500, tempo limite de 5 s e “sem login” seguem esses ADR aceitos. **Ressalva do G3:** R1..R5 (aprovacoes.md, 26/11/2026 15:08) — R1 (ET-0001 v1.4 da AS, condição para liberar a TASK-0008); R2 (teste de contrato com `format: date-time`); ressalva R3 do G3 (itens PV do ADR-0001 v2 D8 como testes obrigatórios antes do G4); R4 (SDK .NET 10 + Angular CLI e spike do encerramento gracioso em ASP.NET Core antes do CA-07); R5 (usar `\z` nas regex .NET). A implementação não depende mais da AH-0001.
>
> **v1.3** (26/11/2026 13:10, America/Sao_Paulo) — revisão editorial: o texto da história e a premissa de público registram a confirmação da CPO (DEC-PO-0002). Os critérios de aceite e o status **vigente** não mudam; a ressalva (1) do G1 permanece.
>
> **v1.4** (26/11/2026 15:12 (America/Sao_Paulo)) — revisão editorial (DEC-PO-0008): premissas de stack atualizadas para C#/.NET 10 LTS + Angular 22.3 (ADR-0001 v2.0 / AH-0003); ADR-0002/0003 v1.1 aceitos; ressalva (1) do G1 atualizada e ressalvas R1..R5 do G3 registradas. Nenhum CA foi reaberto nem alterado. Status **vigente** mantido.

# US-0002 — Ver o status da API em uma tela simples do Portal Web

> [TESTE] DEM-2026-001 · Fluxo 01 · Prioridade Normal (CPO, G0; DEC-PO-0004, pontuação 2,8) · Classe de risco **R3** (DEC-ARQ-0001) · Tipo: Funcionalidade nova.
> **Versão 1.1** (26/11/2026, America/Sao_Paulo): incorpora premissas do ADR-0003 proposto, a validação do protótipo (DEC-PO-0005, Aprovado com ressalvas) e os ajustes de testabilidade da QA (TASK-0005, DEC-PO-0006). Status **em-revisao**: prontos para o G1; a promoção a vigente fica para o G1.

## História
**Como** operador/equipe técnica interna (DEC-PO-0002, confirmado pela CPO em 26/11/2026 12:36),
**quero** abrir uma tela simples no Portal Web que mostre o status da API (status, versão e timestamp),
**para** verificar a saúde da API sem precisar chamar o endpoint manualmente e perceber de imediato quando ela está indisponível.

## Valor
Torna o sinal de US-0001 visível a pessoas e valida a integração Portal ↔ API desde o início do projeto.

## Escopo
- Dentro: tela de status no Portal Web (a criar) que consome `GET /health` (US-0001) e trata sucesso, carregamento e falha/indisponibilidade (REQ-0002, REQ-0003, REQ-0004, RN-0002).
- Fora: histórico de status, gráficos, alertas, notificações, múltiplos serviços, Mobile, atualização automática (polling — RE-04, demanda futura); qualquer solução visual, de navegação ou de acesso além do comportamento aqui definido (UX/UI e ARQ).

## Premissas
- Público = operador/equipe técnica interna (DEC-PO-0002, confirmado pela CPO em 26/11/2026 12:36; exposição a clientes ou usuários finais é nova decisão da CPO).
- Tela sem login nesta demanda (L5, ADR-0003 v1.1 aceito).
- Tempo limite da consulta: 5 s, sem nova tentativa automática (DEC-AS-0001, confirmado no G3).
- Formatos de `status`/`version`/`timestamp` e valores `"ok"` / `"unavailable"`: ADR-0002 v1.1 e ADR-0003 v1.1 aceitos (ver US-0001). A tela (Portal Angular 22.3, ADR-0001 v2.0 / AH-0003) consome o mesmo contrato.
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
- ARQ (TASK-0003): stack do Portal = Angular 22.3 (ADR-0001 v2.0 / AH-0003); forma de consumo da API e acesso à tela sem login (ADR-0003 v1.1 aceito). G3 com ressalvas R1..R5; a TASK-0008 espera a R1.
- G1 (escopo) antes do planejamento técnico.

## Rastreio
Solicitação original (DEM-2026-001) → REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002 → US-0002 → TASK-0004 (protótipo), TASK-0006/0008/0009/0010/0011 → CT (QA, por CA) → entrega (G8).

## Definition of Ready (situação em 26/11/2026 15:12)
Objetivo e valor: OK · Critérios numerados e verificáveis: OK (nenhum CA reaberto, DEC-PO-0008) · Dependências identificadas: OK (ADR aceitos; AH-0003 aprovada) · Protótipo: Aprovado com ressalvas (DEC-PO-0005) · Contexto técnico: G3 com ressalvas R1..R5 (ET-0001 v1.4 pendente, R1) · Risco: R3 confirmado.
