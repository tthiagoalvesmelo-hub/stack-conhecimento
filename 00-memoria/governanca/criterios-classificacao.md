# Critérios de classificação, priorização e escalonamento

> Versão 1.0 · 26/11/2026 · gerado a partir dos Prompts 01–04 da Stack Multiagentes (Prompt 04, Anexo A, tem prioridade).

## Classes de risco R1–R3

| Classe | Critérios | Consequência mínima |
|---|---|---|
| R1 — Baixo | Sem mudança de contrato, de estrutura de banco, de segurança ou de custo; um serviço; reversível por rollback simples. Ex.: texto, ajuste visual, configuração não sensível, correção pontual. | Unitário + regressão automatizada do serviço; janela de observação de 30 min. |
| R2 — Médio | Mudança de comportamento em um ou poucos serviços; migração não destrutiva (expand); contrato interno compatível; nova dependência já aprovada. | Unitário, integração, funcional, regressão, contrato (se API); observação de 2 h. |
| R3 — Alto | Contrato público, migração destrutiva, autenticação/autorização, dados pessoais (LGPD), vários serviços, novo framework/serviço, impacto de custo, operação irreversível. | Todos os tipos aplicáveis + segurança e desempenho; 2ª aprovação do Arquiteto; AH; observação de 24 h. |
- A classe é proposta por quem detalha a demanda e confirmada pelo Arquiteto Líder no G2. Na dúvida, vale a classe mais alta.
- Qualquer agente pode pedir reclassificação para cima com justificativa; reclassificar para baixo exige o Arquiteto e fica registrado em historico.md.
- Se o escopo mudar durante a execução, a classe é reavaliada antes do G4.

## Classificação das demandas

| Tipo | Fluxo | Responsável do fluxo | Classe de risco típica | Gates |
|---|---|---|---|---|
| Funcionalidade nova | 01 | PO | R2 (R3 se contrato público, dados sensíveis ou novo serviço) | G0–G8 completos |
| Melhoria funcional | 01 | PO | R1–R2 | G0–G8; G3 se houver contrato/dados |
| Correção de defeito | 01 ou 03-C | PO (via Suporte quando vier de incidente) | Pela severidade: P0/P1 → R2+; P2/P3 → R1–R2 | G0, G2 simplificado, G4–G8 |
| Melhoria arquitetural | 02 | Arquiteto | R2–R3 | G0–G8; ADR obrigatório |
| Refatoração | 02 | Arquiteto | R1–R2 | G0–G8; sem mudança de comportamento (regressão obrigatória) |
| Atualização tecnológica | 02 | Arquiteto | R2 (R3 se major de framework, runtime ou banco) | G0–G8; teste de compatibilidade |
| Melhoria de infraestrutura | 02 | Arquiteto (DevOps executa) | R2 (R3 se custo, rede ou produção) | G0–G8; AH se custo ou produção |
| Segurança | 02 (ou 03 se ativa) | Arquiteto | R3 | G0–G8; teste de segurança e AH obrigatórios |
| Performance | 02 (ou 01 se percebida pelo usuário) | Arquiteto | R2 | G0–G8; teste de desempenho com linha de base |
| Incidente operacional | 03 | Suporte | Pela severidade P0–P3 | Fluxo 03; G8 de resolução + RCA (P0/P1) |

## Priorização

| Fator | O que mede | Quem pontua | Escala (1–5) |
|---|---|---|---|
| Impacto no negócio | Receita, compromisso, objetivo estratégico | PO (funcional) / CPO (estratégico) | 1 = marginal · 5 = objetivo estratégico ou compromisso firmado |
| Impacto nos usuários | Quantidade e criticidade dos usuários afetados | PO | 1 = poucos, sem bloqueio · 5 = muitos ou bloqueio de tarefa essencial |
| Severidade técnica | Gravidade do problema técnico ou do débito | Arquiteto Líder | 1 = cosmético · 5 = risco de indisponibilidade ou de dados |
| Risco operacional | Probabilidade × impacto de não fazer (ou de fazer) | Arquiteto Líder | 1 = desprezível · 5 = alto e iminente |
| Urgência | Custo de esperar (prazo legal, janela, degradação) | PO / CPO | 1 = sem prazo · 5 = perda se não for feito já |
| Dependências | Quantas demandas esta desbloqueia | Orquestrador (levanta) / Arquiteto | +1 a +2 no custo do atraso se desbloquear outras |
| Complexidade | Incerteza e número de componentes | Arquiteto Líder | 1 = trivial · 5 = muito incerta |
| Esforço estimado | Trabalho total dos agentes | Executores (consolidado pelo responsável do fluxo) | 1 = horas · 5 = semanas |

> MODELO DE PONTUAÇÃO
> FÓRMULA (INSPIRADA EM WSJF):
> Custo do atraso (CA) = Impacto no negócio + Impacto nos usuários + Severidade técnica + Risco operacional + Urgência + bônus de dependências (0 a 2)
> Tamanho (T) = (Complexidade + Esforço estimado) / 2
> Pontuação = CA / T  (arredondada a 1 casa)
> CLASSES:
> Imediata: incidente P0/P1 ou defeito P0/P1 em produção (fora da fórmula, sempre no topo).
> Alta: pontuação ≥ 6, ou prazo estratégico fixado pelo CPO.
> Normal: pontuação entre 3 e 6.
> Baixa: pontuação < 3.
> REGRAS:
> A pontuação orienta; quem decide é o PO (funcional) e o Arquiteto (técnico). Ajuste manual exige justificativa no histórico.
> Conflito entre demandas funcionais e técnicas, ou entre fluxos, vai ao CPO (decisão DEC-CPO-nnnn).
> Demanda com dependência não resolvida não entra em execução, qualquer que seja a pontuação.
> Débito técnico e segurança têm reserva mínima de capacidade, sugerida em 20% (a confirmar pelo Thiago), para não serem sempre preteridos.

## Gestão de riscos

| Etapa | Regra | Responsável |
|---|---|---|
| Identificação | Na proposta (G1) e no planejamento (G2): técnico, segurança, dados, operação, prazo, dependência externa | Responsável do fluxo; especialistas apontam riscos da sua área |
| Avaliação técnica | Probabilidade (1–3) × impacto (1–3); risco ≥ 6 é alto e exige mitigação planejada antes do G2 | Arquiteto Líder |
| Registro | Seção riscos do contexto.yaml (ID, descrição, P×I, dono, mitigação, status) | Orquestrador registra; dono atualiza |
| Tratamento | Mitigar, aceitar (com justificativa), transferir ou evitar; aceitar risco alto exige CPO e, se for N3, AH | Dono do risco |
| Acompanhamento | Revisado em cada MSG-CONS; risco materializado vira BLQ ou INC | Orquestrador |

## Severidade P0–P3, comunicação e ciclo do incidente

| Severidade | Definição | Responsáveis | Metas de referência | Comunicação |
|---|---|---|---|---|
| P0 — Crítico | Indisponibilidade generalizada; perda ou comprometimento de dados; falha grave de segurança; impacto generalizado na operação. | Suporte (coordena) + DevOps + Arquiteto imediatos; DBA se houver dados; desenvolvedores conforme o serviço | Reconhecer em até 15 min; mitigar em até 1 h (meta); atualização a cada 30 min | Thiago e CPO na abertura e a cada 30 min; PO informado |
| P1 — Alto | Funcionalidade essencial indisponível; impacto significativo em usuários; falha em serviço importante. | Suporte + DevOps; Arquiteto e desenvolvedor conforme o diagnóstico | Reconhecer em até 30 min; restaurar em até 8 h (meta); atualização a cada 2 h | CPO e Thiago na abertura; PO informado |
| P2 — Médio | Funcionalidade parcialmente comprometida; há alternativa operacional. | Suporte; correção pelo fluxo normal (PO prioriza) | Reconhecer em até 1 dia útil; correção conforme prioridade | PO; resumo semanal ao CPO |
| P3 — Baixo | Problema pontual; erro visual ou de baixo impacto; solicitação sem impacto operacional relevante. | Suporte; backlog | Reconhecer em até 2 dias úteis | PO no backlog |

| Etapa | Regra | Responsável |
|---|---|---|
| Entrada | Alerta ou relato vira ocorrência; entrada formal pelo CPO (Prompt 02). Indício de P0/P1: Orquestrador aciona o Suporte imediatamente e informa o CPO e o Thiago em paralelo. | Orquestrador · Suporte |
| Classificação | Suporte define a severidade P0–P3 e o tipo A/B/C em até 15 min (P0/P1); reclassificação registrada. | Suporte |
| Acionamento imediato | P0/P1: MSG-SOL direta aos especialistas, em paralelo, sem G1/G2 nem planejamento; o Orquestrador suspende evolutivas dos agentes necessários. | Orquestrador |
| Comunicação | Abertura, mudança de status, mitigação e encerramento, na cadência da tabela; aba Incidentes sempre atualizada. Comunicação externa a clientes: N3 na fase atual. | Suporte (conteúdo) · Orquestrador (distribuição) |
| Diagnóstico | Logs, métricas, REL recentes, 04-incidentes e KB; hipótese registrada com evidência. | Suporte + DevOps |
| Mitigação | Rollback, feature flag, contorno ou escala de recurso; prioridade é restaurar o serviço. Mudança de custo ou ação irreversível: AH expressa. | DevOps (executa) · Arquiteto (decide sem runbook) |
| Correção definitiva | BUG-nnnn no Fluxo 03-C com todos os gates (CR e QA expressos para P0/P1) e AH para publicar. | PO coordena; desenvolvedores |
| Validação | Suporte confirma o restabelecimento com evidência (métricas e teste do fluxo); QA valida a correção. | Suporte · QA |
| Encerramento | G8 do INC: causa, solução, REL e BUG vinculados, KB atualizada, PO e CPO informados. | Suporte |
| Causa raiz | RCA sem culpados obrigatória em P0/P1 em até 5 dias úteis (linha do tempo, causa raiz, fatores, ações com dono e prazo); P2 recorrente vira PRB-nnnn. | Suporte com Arquiteto; Documentação publica |

## Escalonamento

| Severidade | Reconhecimento | Escalonamento | Prompt 02 (provisório) | Decisão |
|---|---|---|---|---|
| P0 | Até 15 min | 30 min sem mitigação → Arquiteto + CPO; 1 h → Thiago decide estado Restrito/Congelado | S1: imediato / 30 min | Ajustado: reconhecimento explícito e Thiago no circuito |
| P1 | Até 30 min | 2 h sem solução → Arquiteto + CPO | S2: até 2 h / 4 h | Ajustado (mais curto): agentes operam continuamente; o gargalo é a aprovação humana, não a reação |
| P2 | Até 1 dia útil | 2 dias úteis → responsável do fluxo | S3: 1 dia útil / 2 dias úteis | Confirmado |
| P3 | Até 2 dias úteis | 5 dias úteis → responsável do fluxo | S4: 2 / 5 dias úteis | Confirmado |
Bloqueios de demandas (não incidentes)
| Classe de prioridade | Primeira ação | Escalonamento |
|---|---|---|
| Imediata | 2 h | 4 h → Arquiteto (técnico) ou CPO (prioridade) |
| Alta | 4 h | 1 dia útil → responsável do fluxo; 2 dias úteis → CPO |
| Normal | 1 dia útil | 2 dias úteis → responsável do fluxo; 5 dias úteis → CPO |
| Baixa | 2 dias úteis | 5 dias úteis → responsável do fluxo |
Bloqueio que depende de AH: sem resposta do Thiago em 4 h (Imediata/P0–P1: 30 min), o Orquestrador reenvia e aciona o designado, se houver. Sem resposta, a operação NÃO é executada: a demanda fica em “Aguardando dependências”. Dias úteis e horários no fuso America/Sao_Paulo; as metas são de referência na fase de testes e serão recalibradas após 30 dias de dados.

## Política de implantação

O DevOps é responsável pelo processo de implantação. Uma etapa só começa com a anterior concluída e evidenciada.
| Etapa | Responsável | Evidência | Gate | Automatizável |
|---|---|---|---|---|
| 1. Desenvolvimento concluído | Desenvolvedor | PR com testes e nota de análise | — | Parcial (CI) |
| 2. Code Review aprovado | Code Reviewer (+ Arquiteto se crítica) | CR-nnnn | G4 | Não (agente validador) |
| 3. Testes automatizados executados | Pipeline / DevOps | Execução verde vinculada ao commit | G4/G5 | Sim |
| 4. QA aprovado | QA | PQ-nnnn | G5 | R1 parcial; R2/R3 não |
| 5. Alterações de banco validadas | DBA | Parecer DBA + script testado em homologação | G6 | Não se houver migração |
| 6. Artefato de implantação preparado | DevOps | Imagem/pacote versionado e imutável, notas de versão | G6 | Sim |
| 7. Ambiente de homologação validado | DevOps + QA | Deploy em homologação, smoke test, pré-aceite do PO | G6 | Parcial |
| 8. Aprovação de publicação obtida | Thiago Melo (ou designado) | AH-nnnn aprovada e válida | G6 | Não na fase atual (ver 10.3) |
| 9. Deploy executado | DevOps (pipeline) | Log da pipeline, REL-nnnn | G7 | Sim (execução) |
| 10. Monitoramento pós-implantação | DevOps + Suporte | Painéis e alertas na janela de observação (R1 30 min, R2 2 h, R3 24 h) | G7 | Sim (coleta) + análise |
| 11. Confirmação da estabilidade | DevOps (Suporte confirma ausência de incidente) | Critérios de sucesso atendidos | G7 | Não |
| 12. Atualização da documentação | Documentação | Release notes e documentos publicados | G8 | Parcial |

> CRITÉRIOS DE SUCESSO DA IMPLANTAÇÃO
> UMA IMPLANTAÇÃO SÓ É BEM-SUCEDIDA QUANDO, NA JANELA DE OBSERVAÇÃO:
> Health checks de todos os serviços alterados e dependentes estão OK.
> Taxa de erro e latência p95 estão dentro da linha de base +10% (ou SLO do serviço).
> Smoke test dos fluxos de negócio afetados passou em produção.
> Nenhum alerta novo P0/P1 e nenhum incidente aberto relacionado à REL.
> Fila de mensagens com falha e consumo de recursos sem crescimento anormal.
> O deploy terminar sem erro não basta: G7 só é registrado com estes critérios.

Janelas de publicação
- Janela padrão de publicação em produção: a definir pelo Thiago (sugestão: dias úteis, 10h–16h, horário de Brasília, fora de véspera de feriado e de sexta à tarde).
- Fora da janela: só emergência (P0/P1) com AH.
- Durante a fase de testes internos, “produção” é o ambiente que o Thiago declarar como tal; as mesmas regras valem.

## Rollback e contingência

| Tema | Regra |
|---|---|
| Gatilhos objetivos | Critério de sucesso violado na janela de observação; alerta P0/P1 correlacionado à REL; smoke test reprovado; falha de migração. |
| Quem decide | Com runbook aprovado (RB-nnnn) para a situação: o DevOps executa sem esperar. Sem runbook: o Arquiteto Líder decide e o DevOps executa. Thiago é informado na hora. |
| Opções, em ordem de preferência | 1) Desligar feature flag; 2) rollback para a versão anterior (REL anterior); 3) roll-forward com hotfix (exige G4/G5 expressos e AH); 4) restauração de backup (N3: exige AH, salvo runbook de emergência pré-aprovado pelo Thiago). |
| Banco de dados | Com expand/contract a aplicação volta sem mexer no banco. Reversão de dados ou de schema: DBA prepara e executa; se for destrutiva, exige AH. |
| Plano obrigatório | Todo G6 inclui plano de rollback com passos, tempo estimado e responsável; em R3 ele é ensaiado em homologação. |
| Estados e registros | Demanda em “Em rollback”; REL marcada como Rollback; INC aberto se houve impacto em usuário; RCA quando P0/P1. |
| Contingência | Se o rollback falhar: P0 imediato, estado Restrito, Arquiteto + DBA + DevOps acionados, Thiago e CPO informados; restauração por backup com AH expressa. |
| Pós-rollback | Correção volta ao fluxo normal com todos os gates; a mesma versão não é reimplantada sem a causa corrigida. |

## Indicadores

| Indicador | Fórmula | Fonte | Frequência | Meta inicial | Contrapeso (ler junto) |
|---|---|---|---|---|---|
| Lead time | Recebida → Concluída (mediana, por fluxo e tipo) | Backlog (planilha) | Semanal | Linha de base em 30 dias | Taxa de defeitos |
| Cycle time | Em desenvolvimento → Concluída | Backlog / Tarefas | Semanal | Linha de base | Retrabalho |
| Demandas concluídas | Quantidade por período, tipo e classe | Backlog | Semanal | Tendência (sem meta de volume) | Taxa de falha em mudanças |
| Taxa de retrabalho | TASKs que voltaram de CR/QA ÷ TASKs | Tarefas (ciclos CR/QA) | Semanal | < 25% (inicial) | — |
| Taxa de defeitos | BUGs encontrados após G5 (em produção) ÷ demandas entregues | Backlog / Incidentes | Mensal | Linha de base, depois queda | Lead time |
| Aprovação no 1º Code Review | PRs aprovados na 1ª rodada ÷ PRs | Tarefas / CR- | Semanal | ≥ 60% (inicial) | Defeitos que escaparam do CR |
| Aprovação no 1º ciclo de QA | Entregas aprovadas no 1º PQ ÷ entregas | Tarefas / PQ- | Semanal | ≥ 70% (inicial) | Defeitos em produção |
| Frequência de implantação | REL por serviço por semana | Releases | Semanal | Tendência | Taxa de falha em mudanças |
| Taxa de falha em mudanças | REL com rollback, hotfix ou incidente ÷ REL | Releases / Incidentes | Mensal | < 15% | Frequência de implantação |
| Tempo médio de recuperação (MTTR) | Abertura do INC → serviço restabelecido (P0/P1) | Incidentes | Mensal | P0 ≤ 1 h; P1 ≤ 8 h | RCA concluída no prazo |
| Incidentes por microsserviço | INC por serviço e severidade | Incidentes | Mensal | Tendência; foco nos 3 maiores | — |
| Disponibilidade | Tempo disponível ÷ tempo total, por serviço | Monitoramento (a confirmar) | Mensal | SLO por serviço (a definir) | — |
| Débitos técnicos | TD registrados × resolvidos; idade média | 02-tecnica/debitos-tecnicos | Mensal | Resolvidos ≥ registrados no trimestre | — |
| Tempo de resposta de AH | Solicitada → decidida | Aprovações humanas | Mensal | Monitorar gargalo humano | — |
- Indicadores servem para melhoria contínua da Stack, nunca para ranquear agentes por velocidade.
- Toda métrica de fluxo (lead time, cycle time, volume, frequência) é lida junto com uma métrica de qualidade (contrapeso).
- Meta de velocidade nunca justifica pular gate, reduzir testes ou dividir artificialmente demandas; tentativa disso é registrada como CONF.
- Os 30 primeiros dias formam a linha de base; as metas iniciais são revistas com o Thiago após esse período.
- O Orquestrador calcula os indicadores semanalmente (rotina agendada) a partir das abas da planilha e publica na aba Indicadores; Arquiteto e PO analisam e propõem ações.
