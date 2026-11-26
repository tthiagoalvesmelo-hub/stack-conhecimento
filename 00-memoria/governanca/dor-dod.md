# Definition of Ready e Definition of Done

> Versão 1.0 · 26/11/2026 · gerado a partir dos Prompts 01–04 da Stack Multiagentes (Prompt 04, Anexo A, tem prioridade).

## DoR

Uma atividade está pronta para desenvolvimento quando todos os itens abaixo estão atendidos:
| Item | Critério objetivo | Quem verifica |
|---|---|---|
| Objetivo definido | Campo objetivo preenchido e vinculado a RM- ou DEM- | Responsável do fluxo |
| Descrição clara | Problema, escopo e fora de escopo; sem termos ambíguos (“melhorar”, “otimizar” sem medida) | Responsável do fluxo |
| Critérios de aceite | CA numerados e verificáveis, cada um testável | PO / Arquiteto; QA confirma testabilidade |
| Dependências identificadas | Lista com IDs; nenhuma impeditiva sem plano | Orquestrador |
| Contexto técnico suficiente | Nota de análise (itens 1–9 da seção 4.1); contratos e modelo de dados aprovados quando aplicável (G3) | Executor; Arquiteto valida em R2/R3 |
| Responsáveis definidos | Agente executor e validadores de cada gate | Orquestrador |
| Riscos conhecidos | Classe de risco R1–R3 confirmada; riscos altos com mitigação | Arquiteto Líder |
| Estimativa, quando aplicável | Estimativa por TASK registrada na aba Tarefas | Executor |
Complementos por tipo
| Tipo | Exigência adicional |
|---|---|
| Correção de defeito | BUG-nnnn com passos para reproduzir, severidade P0–P3, ambiente, versão e evidência |
| Melhoria arquitetural / atualização tecnológica | ADR proposto, alternativas e plano de compatibilidade |
| Segurança | Ameaça descrita, ativos afetados, critério de verificação e responsável pelo teste |
| Performance | Linha de base medida e meta numérica |
| Infraestrutura | Estimativa de custo e plano de reversão |
| Incidente | Não usa DoR (acionamento imediato); a correção definitiva (BUG) usa |

## DoD

| Item | Evidência exigida | Quem atesta |
|---|---|---|
| Implementação finalizada | PR mesclado na main com IDs citados | Code Reviewer / Orquestrador |
| Critérios de aceite atendidos | Rastreio CA → caso de teste aprovado; confirmação do PO (G8) | QA / PO |
| Code Review aprovado | CR-nnnn Aprovado ou Com observações (+ Arquiteto se crítica) | Code Reviewer |
| Testes aplicáveis aprovados | PQ-nnnn favorável conforme a matriz de proporcionalidade | QA |
| Alterações de banco validadas | Parecer do DBA e migração aplicada sem erro | DBA |
| Implantação concluída, quando aplicável | REL-nnnn com G7 (estabilidade confirmada) e AH quando exigida | DevOps |
| Documentação atualizada | Documentos e release notes publicados; contexto.yaml e INDEX atualizados | Documentação |
| Evidências registradas | Links na aba Backlog e em aprovacoes.md, verificados | Orquestrador |
| Sem bloqueios impeditivos | Nenhuma MSG-BLQ aberta; débitos aceitos registrados como TD-nnnn | Orquestrador |
O Orquestrador só move para “Concluída” quando todos os itens aplicáveis têm evidência vinculada e verificada. “Terminei” sem evidência é devolvido como MSG-RET incompleta. Item não aplicável fica marcado como “N/A” com justificativa.

## Checklists de qualidade

Usado pelo executor (autoverificação) e pelo Orquestrador (verificação de presença das evidências).

> ANTES DE IMPLEMENTAR (DOR)
> □  Objetivo, descrição e CA verificáveis
> □  Dependências e riscos registrados; classe R1–R3 confirmada
> □  Nota de análise (4.1) anexada
> □  Contrato e modelo de dados aprovados (G3), se aplicável
> □  Agentes e validadores definidos


> ANTES DE ABRIR O PR
> □  Branch por TASK; commits com IDs e trailer Agente
> □  Testes unitários (e integração, se aplicável) passando localmente/CI
> □  Sem segredos, dados pessoais ou código morto
> □  Logs, erros e validações conforme padrões
> □  Documentação técnica do PR (o quê, por quê, como testar, riscos)


> CODE REVIEW (G4)
> □  CI verde
> □  11 critérios avaliados; parecer CR-nnnn
> □  Revisor ≠ autor; 2ª aprovação do Arquiteto se crítica
> □  Ciclo ≤ 2 ou escalonamento


> TESTES (G5)
> □  Matriz de proporcionalidade aplicada
> □  100% dos CA com teste aprovado
> □  Sem P0/P1 aberto; P2 só com aceite
> □  Regressão e contrato aprovados; varredura sem alta/crítica
> □  PQ-nnnn com evidências e versão testada


> PRÉ-LIBERAÇÃO (G6)
> □  Banco validado pelo DBA
> □  Documentação pronta
> □  Pré-aceite do PO (funcional) ou do Arquiteto (técnico)
> □  Artefato imutável; homologação validada
> □  Plano de rollback (ensaiado em R3)
> □  AH-nnnn aprovada e válida (produção)


> PÓS-IMPLANTAÇÃO (G7)
> □  Janela de observação cumprida
> □  Critérios de sucesso atendidos (não só deploy sem erro)
> □  REL-nnnn registrada; Suporte informado


> ENCERRAMENTO (G8 / DOD)
> □  Todos os itens da DoD com evidência
> □  Documentação publicada; contexto.yaml e INDEX atualizados
> □  Indicadores e lições registrados na MSG-CONS final
> □  Responsável do fluxo informou o CPO
