# aprovacoes.md — DEM-2026-001 [TESTE]

Demanda: DEM-2026-001 [TESTE] · Classe de risco: R3 (DEC-ARQ-0001) · Fluxo: 01 (confirmado CPO)

| Gate | Validador | Modo (automatizada / manual pelo agente / AH) | Resultado (Aprovado / Aprovado com observações / Reprovado) | Evidência (CR-/PQ-/pipeline/doc + versão) | Data/hora (America/Sao_Paulo) | Registrado por |
|---|---|---|---|---|---|---|
| G0 Entrada confirmada | CPO | manual pelo agente | Aprovado | MSG-RET CPO TASK-0001 (26/11 12:11) | 26/11/2026 12:11 | ORQ |
| G1 Escopo/proposta consolidados | Responsável do fluxo | | | | | ORQ |
| G2 Planejamento aprovado | PO / ARQ | | | | | ORQ |
| G3 Contratos e dados aprovados | ARQ · DBA | | | | | ORQ |
| G4 Code Review aprovado | CR (+ ARQ se crítica) | | | | | ORQ |
| G5 Qualidade aprovada | QA | | | | | ORQ |
| G6 Pré-liberação | DBA · DOC · PO/ARQ · OPS | | | | | ORQ |
| G7 Implantação verificada | OPS (+ SUP) | | | | | ORQ |
| G8 Encerramento | Responsável do fluxo | | | | | ORQ |

## Aprovações humanas (AH)
| AH | Operação | Categoria | Pedido em | Decisão (texto literal do Thiago) | Decidido por | Decidido em | Condições | Validade |
|---|---|---|---|---|---|---|---|---|
| AH-0001 | Adotar stack base ADR-0001 (Node.js 24 LTS + Fastify 5 portal-api + Portal estático JS) em monorepo git local /workspace/projetos/portal/ | arquitetura | 26/11/2026 12:27 | (aguardando) | | | | 24 h |

## Observações
- Aprovação de pedido de urgência para pular gate: não existe; registrar e escalar.
