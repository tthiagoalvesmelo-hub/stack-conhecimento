---
id: GOV-ESTADO
titulo: "Estado operacional da Stack"
tipo: governanca
versao: 1.0
status: vigente
dono: ORQ
autores: [ORQ]
aprovado_por: Thiago Melo
criado_em: 2026-11-26T11:00-03:00
atualizado_em: 2026-11-26T11:00-03:00
revisar_ate: 2027-02-26
relacionados: []
substitui: null
substituido_por: null
---

# Estado operacional da Stack

**Estado atual: NORMAL** (definido em 26/11/2026 11:00, America/Sao_Paulo — fase de testes internos, não é produção)

Todos os agentes leem este arquivo antes de qualquer operação em homologação ou produção.

Registrado em 00-memoria/governanca/estado-operacional.md e lido por todos os agentes antes de qualquer operação em homologação ou produção.
| Estado | Efeito | Quem ativa |
|---|---|---|
| Normal | Operação conforme este documento. | Padrão. |
| Restrito | Somente correções de defeito, incidentes e itens que Thiago liberar; nenhuma publicação em produção não emergencial. | Thiago, ou o Orquestrador de forma preventiva após P0 aberto ou taxa de falha em mudanças acima do limite (Thiago informado na hora). |
| Congelado | Nenhuma alteração em homologação ou produção; agentes apenas analisam e preparam. Rollback por runbook continua permitido. | Somente Thiago (o Orquestrador recomenda). |

Quem muda o estado grava uma linha no histórico abaixo (append-only), com data/hora, quem decidiu e motivo. Congelar e voltar a Normal é decisão só do Thiago.

## Histórico
| Data/hora (America/Sao_Paulo) | De → Para | Decidido por | Motivo |
|---|---|---|---|
| 2026-11-26 11:00 | — → Normal | Thiago Melo (padrão inicial) | Criação da Stack |
