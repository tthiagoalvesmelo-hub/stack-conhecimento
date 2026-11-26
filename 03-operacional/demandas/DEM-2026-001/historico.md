# historico.md — DEM-2026-001 [TESTE] (append-only)
<!-- Corrija com nova entrada; nunca apague. -->

| Data/hora | Quem (sigla) | O quê | IDs / evidência |
|---|---|---|---|
| 26/11/2026 12:10 | ORQ | Solicitação recebida do Jarvis (em nome do Thiago) para teste ponta a ponta | mensagem do Jarvis 12:10 |
| 26/11/2026 12:12 | ORQ | DEM-2026-001 registrada no estado Recebida (TESTE); proposto Fluxo 02, responsável ARQ, tipo Funcionalidade nova, prioridade Normal, risco R1 | contexto.yaml v1 |
| 26/11/2026 12:13 | ORQ | MSG-SOL TASK-0001 à CPO para triagem e confirmação de entrada (G0) | TASK-0001 |
| 26/11/2026 12:11 | CPO | MSG-RET TASK-0001: G0 aceita; tipo Funcionalidade nova confirmado; fluxo AJUSTADO para 01 (responsável PO); prioridade Normal; ARQ colaborador obrigatório; risco R2 padrão a confirmar pelo ARQ; propõe RM-0001 | MSG-RET CPO 12:11 |
| 26/11/2026 12:15 | ORQ | G0 registrado em aprovacoes.md; estado Recebida → Em análise (motivo: G0 aceito pela CPO); RM-0001 reservado; contexto.yaml v2 | contexto.yaml v2 |
| 26/11/2026 12:16 | ORQ | MSG-SOL TASK-0002 ao PO (análise inicial, definição de atividades) e TASK-0003 ao ARQ (análise técnica: stack, estrutura, versão, risco), em paralelo | TASK-0002, TASK-0003 |
| 26/11/2026 12:23 | PO | TASK-0002: análise inicial. Reservados e criados US-0001, US-0002, REQ-0001 a REQ-0004, RN-0001, RN-0002 (status em-revisao, v1.0); proposta de atividades e responsáveis e pontuação provisória 2,4 em analise-po-task-0002.md v1.0 | US-0001, US-0002, REQ-0001..0004, RN-0001..0002; commit desta entrada |
| 26/11/2026 12:23 | PO | DEC-PO-0001: duas US na mesma demanda; acionar UX/UI, AS, ARQ, FS, CR, QA, DOC e OPS (enxuto); não acionar AN, DBA, MOB e PMM (justificativas em analise-po-task-0002.md §4) | DEC-PO-0001 |
| 26/11/2026 12:23 | PO | DEC-PO-0002: premissa de teste — público da tela de status = operador/equipe técnica interna, até a CPO definir (lacuna L2) | DEC-PO-0002 |
| 26/11/2026 12:23 | PO | DEC-PO-0003: prioridade mantida em Normal (CPO, G0) apesar da pontuação provisória 2,4 (Baixa pela fórmula); ajuste manual justificado; reavaliar após os fatores do ARQ | DEC-PO-0003; analise-po-task-0002.md §6 |
