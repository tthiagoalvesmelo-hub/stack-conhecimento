---
id: ANALISE-DEM-2026-001-TASK-0002
titulo: "Análise inicial do PO — escopo, atividades propostas e pontuação (DEM-2026-001 [TESTE])"
tipo: analise
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:22-03:00
atualizado_em: 2026-11-26T12:22-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0001, DEC-PO-0002, DEC-PO-0003]
substitui: null
substituido_por: null
---

# Análise inicial do PO — DEM-2026-001 [TESTE] · TASK-0002

> Fase de testes internos; nada vai à produção. Este documento **não** altera estado, etapa, gates nem tarefas (só o ORQ). Os códigos A1…A9 abaixo são rótulos locais da proposta, **não** IDs de TASK: o ORQ cria as TASK ao despachar.

## 1. Entendimento
- **O que foi pedido, por quem, para quê:** Thiago Melo (via Jarvis, ORQ) pediu, como teste ponta a ponta da esteira, um endpoint `GET /health` na API base do Portal Web (status, versão, timestamp) e uma tela simples no Portal que mostre esse status; projeto do zero. G0 aceito pela CPO (26/11/2026): Funcionalidade nova, Fluxo 01, responsável PO, prioridade Normal, não dividir a demanda, ARQ colaborador obrigatório.
- **Objetivo funcional:** dar um sinal verificável de disponibilidade e versão da API e torná-lo visível no Portal.
- **Separação requisito × decisão técnica:** o PO define comportamento e critérios (US/CA/REQ/RN). Stack, estrutura, formato da versão e do timestamp, nomes de campos, exposição/autenticação do endpoint e classe de risco são do ARQ (TASK-0003); contrato/EF/ET é do AS; interface é do UX/UI.

## 2. Premissas e lacunas
| # | Item | Tratamento | Dono da resposta |
|---|---|---|---|
| L1 | Visão e objetivos de produto ausentes em 01-institucional/produto | Premissa de teste: demanda de validação da esteira; sem compromisso de negócio | CPO |
| L2 | Público da tela de status não definido | Premissa de teste (DEC-PO-0002): operador/equipe técnica interna | CPO (confirmar) |
| L3 | Stack, estrutura, formato de versão e timestamp, nomes de campos e valores de status | Dependência do ARQ; CA escritos sem fixar formato | ARQ (TASK-0003) |
| L4 | Exposição do endpoint (interna × pública) e autenticação; se pública, contrato público = R3 + AH | Pergunta ao ARQ; PO não assume | ARQ |
| L5 | Regra de acesso à tela (aberta × restrita) | Pergunta ao ARQ/CPO; PO não assume | ARQ / CPO |
| L6 | Meta de desempenho (tempo de resposta) e tempo limite da tela | Sem requisito de desempenho no teste (premissa); tempo limite definido na ET | AS / ARQ |
| L7 | Ambientes dev/hml inexistentes | Premissa de teste: execução local, código em /workspace/projetos/ (git local) | OPS |
| L8 | Classe de risco | R2 padrão (CPO/ORQ); ARQ confirma; R3 se contrato público ou novo serviço | ARQ |
| L9 | Persistência | Premissa: nenhuma (health-check não grava dados) | ARQ (confirmar) |

## 3. Solução funcional consolidada
Duas histórias na **mesma demanda** (a CPO pediu para não dividir a demanda; DEC-PO-0001), entregáveis em incrementos:
1. **US-0001** — endpoint `GET /health` (REQ-0001, REQ-0004, RN-0001): 6 CA.
2. **US-0002** — tela de status no Portal (REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002): 6 CA, incluindo estado de erro com API indisponível.

Rastreio: solicitação → REQ/RN → US → atividade → CT → entrega (a completar nos gates seguintes).

| CA | Verificação prevista (QA confirma) |
|---|---|
| US-0001 CA-01 a CA-04, CA-06 | Teste de API automatizado sobre a resposta, a versão registrada e a ausência de efeitos colaterais |
| US-0001 CA-05, US-0002 CA-06 | Inspeção de corpo, cabeçalhos e tela com checagem de padrões sensíveis |
| US-0002 CA-01 a CA-05 | Teste funcional da tela com API real e com API simulada indisponível |

## 4. Quem aciona o quê (decisão do PO, DEC-PO-0001)
| Agente | Acionar? | Motivo |
|---|---|---|
| UX/UI — Bruno Tavares | **Sim** | Há tela nova; solução visual e estados (saudável, carregando, erro) são do UX/UI |
| Analista de Sistemas — Juliana Castro | **Sim** | Nova API: EF/ET do endpoint e da integração tela↔API (matriz de aprovação: nova API exige AS no G1/G2) |
| Arquiteto Líder — Ricardo Almeida | **Sim (obrigatório)** | TASK-0003 em andamento; contrato (G3), classe de risco, decisões de stack |
| Full Stack — Lucas Fernandes | **Sim** | Implementa API e tela |
| Code Reviewer — Eduardo Pires | **Sim** | G4 sempre que há código; revisor ≠ autor |
| QA — Fernanda Ribeiro | **Sim** | Demanda funcional exige G5; também revisa a testabilidade dos CA antes do G1 |
| Analista de Documentação — Beatriz Moraes | **Sim** | Contrato de API e mudança visível ao usuário (G6 pronta, G8 publicada) |
| DevOps — Diego Carvalho | **Sim, enxuto (condicional)** | G6/G7 exigem ambiente, rollback e smoke test; no teste: confirmar premissa de execução local (pendência de ambientes é dele) e plano de rollback simples; sem pipeline |
| Analista de Negócio — Marcos Vieira | **Não** | Objetivo e resultado esperado já claros e verificáveis; não há processo de negócio nem stakeholder a levantar. A lacuna de visão de produto é da CPO, não do AN. Reavaliar se a CPO trouxer novas regras |
| DBA — Patrícia Lima | **Não** | Sem persistência nem alteração de estrutura/consulta de dados (L9). Reacionar se o ARQ decidir o contrário |
| Java Mobile — André Nogueira | **Não** | Escopo é Portal Web e API; nada no Mobile |
| Product Marketing — Camila Rocha | **Não** | Sem comunicação ao mercado |
| Suporte — Gustavo Barros | **Informado** | Sem produção no teste; informado no G7 como parte do fluxo |

## 5. Atividades propostas e responsáveis (sem IDs TASK; plano formal no G2)
| Rótulo | Atividade | Responsável | Depende de | Entregável | Gate |
|---|---|---|---|---|---|
| A0 | Análise técnica: stack, estrutura, formato da versão, classe de risco (já existe) | ARQ | — | Parecer + ADR(s) | TASK-0003 |
| A1 | Protótipo simples da tela de status com estados saudável, carregando e erro | UX/UI | US-0002; CA validados | Protótipo/fluxo, validado pelo PO | G1/G2 |
| A2 | EF/ET do endpoint e da integração tela↔API (contrato proposto de `GET /health`) | AS | US-0001/0002; A0 (formatos) | EF/ET + contrato para aprovação do ARQ | G1/G2, G3 |
| A3 | Aprovação do contrato de API e consolidação das decisões arquiteturais | ARQ | A2 | Contrato aprovado | G3 |
| A4 | Revisão de testabilidade dos CA (antes do G1) e, depois, plano e casos de teste com rastreio CA→CT | QA | US-0001/0002 | Parecer de testabilidade; PT/CT | G1; G2/G5 |
| A5 | Implementar API `GET /health` e a tela, com testes unitários | Full Stack | G2, G3, A1 | PR com IDs | — |
| A6 | Code Review | CR | A5 | CR | G4 |
| A7 | Testes funcionais, de API e regressão; parecer de qualidade | QA | A5, A6 | PQ | G5 |
| A8 | Documentação do endpoint e da tela (preparada em paralelo aos testes; publicada após a implantação) | DOC | A2, A3 | Documentação versionada | G6, G8 |
| A9 | Ambiente de execução do teste, smoke test e rollback simples | OPS | A0 | Registro do ambiente e do rollback | G6, G7 |
| — | Pré-aceite funcional (G6) e confirmação final (G8); informar a CPO no encerramento | PO | A7, A8 | Aceite em aprovacoes.md | G6, G8 |

Paralelismo (PR-01/PR-04): A1 e A2 correm em paralelo (Etapa B); A4 (testabilidade) pode correr junto; A5 só começa após G2 e G3 (a tela pode usar mocks do contrato aprovado); A8 corre em paralelo a A7.
Sequência obrigatória: G1 → planejamento técnico → G3 → implementação → G4 → G5 → G6 → G7 → G8.

## 6. Pontuação de prioridade (WSJF simplificada, seção 3.1 do PROMPT)
| Fator | Valor | Quem pontua | Justificativa |
|---|---|---|---|
| Impacto no negócio | 2 | PO | Demanda de validação da esteira, sem compromisso de receita ou estratégia (L1) |
| Impacto nos usuários | 1 | PO | Poucos usuários internos, sem bloqueio de tarefa essencial |
| Severidade técnica | 1 (provisório) | **ARQ** | Sem problema técnico em produção; ARQ confirma |
| Risco operacional | 1 (provisório) | **ARQ** | Baixo risco de fazer e de não fazer; ARQ confirma |
| Urgência | 1 | PO | Sem prazo |
| Bônus de dependências | 0 | ORQ levanta | Nenhuma demanda dependente registrada no backlog |
| Complexidade | 3 (provisório) | **ARQ** | Dois componentes, projeto do zero e stack indefinida |
| Esforço estimado | 2 | executores/PO | De algumas horas a poucos dias |

- Custo do atraso = 2 + 1 + 1 + 1 + 1 + 0 = **6**
- Tamanho = (3 + 2) / 2 = **2,5**
- **Pontuação = 6 / 2,5 = 2,4** (provisória até o ARQ confirmar severidade técnica, risco operacional e complexidade).
- **Classe pela fórmula:** Baixa (< 3). **Classe adotada: Normal**, já confirmada pela CPO no G0 (TASK-0001). Ajuste manual justificado em DEC-PO-0003: prioridade estratégica pertence ao CPO; a demanda é o teste ponta a ponta aprovado por Thiago e a fórmula (voltada a backlog competitivo) não reflete esse propósito. Se o ARQ pontuar acima do provisório, reavaliar. Dependência não resolvida (TASK-0003) impede execução, qualquer que seja a pontuação.

## 7. Impactos e riscos
| Componente | Impacto |
|---|---|
| Portal Web | Nova tela de status (a criar) |
| Backend/APIs | Novo recurso `GET /health` na API base (a criar); possível novo contrato |
| Microsserviços | Nenhum identificado (API base do zero; ARQ define se é serviço) |
| Mobile | Nenhum |
| Integrações | Nenhuma externa; integração Portal → API |
| Dados | Nenhum (sem persistência, L9) |
| Infraestrutura | Execução local no teste; ambientes a definir (L7) |

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Endpoint exposto publicamente vira contrato público (R3 + AH) | Baixa | Médio | ARQ define exposição em TASK-0003; PO não assume (L4) |
| Falso "saudável" na tela | Baixa | Médio | RN-0002 e US-0002 CA-03/CA-05 |
| Vazamento de informação interna (versão, erros) | Baixa | Médio | RN-0001, REQ-0004, CA-05/CA-06; ARQ avalia sensibilidade da versão |
| Formatos indefinidos atrasam AS e QA | Média | Baixo | Dependência explícita de TASK-0003; CA não fixam formato |

## 8. Decisões (alçada do PO)
- **DEC-PO-0001** — Escopo e acionamentos: duas US na mesma demanda; acionar UX/UI, AS, ARQ, Full Stack, CR, QA, DOC e OPS (enxuto); não acionar AN, DBA, Mobile e PMM.
- **DEC-PO-0002** — Premissa de teste: público da tela de status = operador/equipe técnica interna, enquanto a CPO não definir.
- **DEC-PO-0003** — Prioridade: manter Normal (CPO, G0) apesar da pontuação provisória 2,4 (Baixa pela fórmula).

## 9. Decisões e respostas pendentes de outros agentes
Stack, estrutura, formatos, exposição/autenticação e classe de risco (ARQ); EF/ET e contrato (AS); protótipo (UX/UI); confirmação de testabilidade (QA); ambiente de execução (OPS); confirmação do público da tela e da visão de produto (CPO); atualização de pendencias_contexto e dos ponteiros historias, requisitos, regras_negocio e decisoes em contexto.yaml (ORQ, único com alçada).

## 10. Próximos passos
1. ORQ confirma o escopo e, se aprovar, registra G1 e despacha A1, A2 e A4 (Etapa B), com TASK-0003 do ARQ como dependência de formato.
2. ARQ entrega TASK-0003 e fornece severidade técnica, risco operacional e complexidade para fechar a pontuação.
3. PO revisa os CA com o QA e promove US/REQ/RN de em-revisao para vigente antes do G1.
