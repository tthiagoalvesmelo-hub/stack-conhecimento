# aprovacoes.md — DEM-2026-001 [TESTE]

Demanda: DEM-2026-001 [TESTE] · Classe de risco: R3 (DEC-ARQ-0001) · Fluxo: 01 (confirmado CPO)

| Gate | Validador | Modo (automatizada / manual pelo agente / AH) | Resultado (Aprovado / Aprovado com observações / Reprovado) | Evidência (CR-/PQ-/pipeline/doc + versão) | Data/hora (America/Sao_Paulo) | Registrado por |
|---|---|---|---|---|---|---|
| G0 Entrada confirmada | CPO | manual pelo agente | Aprovado | MSG-RET CPO TASK-0001 (26/11 12:11) | 26/11/2026 12:11 | ORQ |
| G1 Escopo/proposta consolidados | PO (responsável do Fluxo 01) | manual pelo agente | Aprovado com observações — condições: (1) formatos, 503/405/500, 5 s e "sem login" dependem dos ADR-0002/0003 propostos; se mudarem no G3, PO reabre os CA afetados; (2) stack e implementação (TASK-0008/TASK-0012) só após AH-0001 válida do Thiago; G1 não substitui AH; (3) proposta técnica do ARQ (TASK-0003) segue Parcial | US-0001 (CA-01..09), US-0002 (CA-01..06), REQ-0001..0004, RN-0001/0002 v1.1; parecer QA TASK-0005 respondido; commits af208f2, 4df588e; MSG-RET PO 26/11 12:38 | 26/11/2026 12:38 | ORQ |
| G2 Planejamento aprovado | PO (responsável do Fluxo 01) | manual pelo agente | Aprovado com observações — (a) TASK-0008 e preparação da TASK-0012 só começam com AH-0001 válida ("Aprovo AH-0001" do Thiago, via ORQ); preparação do OPS em paralelo à 0008; (b) G3 (TASK-0007) só após a AH-0001, que entra nas dependências da 0007; se a AH ou o G3 mudarem ADR ou contrato, o PO reabre os CA afetados e o plano é reavaliado (ressalva 1 do G1); L-12 da ET-0001 v1.3 (gancho do 500) confirmada pelo ARQ no G3; CA não mudaram; (c) PR da 0008 e entrada no G4 cumprem DEC-ARQ-0003 (scripts/verify-local.sh, reexecutado pelo CR), DEC-ARQ-0004 e L-CR2 (incremento A da DOC, DEC-PO-0007, pronto antes do G4); critério da TASK-0009: CR Aprovado ou Aprovado com observações + 2ª aprovação explícita do ARQ; Reprovado gera novo ciclo; limite de 2 ciclos; (d) execução da TASK-0010 depende das decisões do ARQ sobre SAST/varredura e método do p95 e da calibração dos 80% de cobertura com o QA (P-QA-01..05); (e) estimativas do ARQ na escala 1–5: ORQ pede ao ARQ conversão para horas, incorporada ao plano sem nova decisão; total em horas registrado 71,5 h, sem a janela de 24 h de observação R3 e sem o ARQ | PLANO-DEM-2026-001-G2 v1.1 (plano-atividades-g2.md, commit 053a2d4, em-revisao → vigente pelo PO após registro); pareceres G2 ARQ (d1b0235), QA (40c8ace), CR, FS, DOC e OPS (rascunhos); MSG-RET PO 26/11 13:05 | 26/11/2026 13:05 | ORQ |
| G3 Contratos e dados aprovados | ARQ · DBA | | | | | ORQ |
| G4 Code Review aprovado | CR (+ ARQ se crítica) | | | | | ORQ |
| G5 Qualidade aprovada | QA | | | | | ORQ |
| G6 Pré-liberação | DBA · DOC · PO/ARQ · OPS | | | | | ORQ |
| G7 Implantação verificada | OPS (+ SUP) | | | | | ORQ |
| G8 Encerramento | Responsável do fluxo | | | | | ORQ |

## Aprovações humanas (AH)
| AH | Operação | Categoria | Pedido em | Decisão (texto literal do Thiago) | Decidido por | Decidido em | Condições | Validade |
|---|---|---|---|---|---|---|---|---|
| AH-0001 | Adotar stack base ADR-0001 (Node.js 24 LTS + Fastify 5 portal-api + Portal estático JS) em monorepo git local /workspace/projetos/portal/ | arquitetura | 26/11/2026 12:27 | Aprovada — texto literal: "Aprovo AH-0001 e também AH-0002" (chat do ORQ, 26/11/2026 14:45) | Thiago Melo | 26/11/2026 14:45 | nenhuma | 24 h |
| AH-0002 | Mesclar o ramo doc/TASK-0011-matriz-7-1 (40c7d84: protocolo-memoria.md v1.1 — matriz 7.1 pareceres CR-nnnn A=CR/E=ARQ, linha registro-ids/conflitos, EL-08) e aplicar o patch do Leia-me.csv (Evidência pelo executor da TASK) | governança | 26/11/2026 13:08 | Aprovada — texto literal: "Aprovo AH-0001 e também AH-0002" (chat do ORQ, 26/11/2026 14:45) | Thiago Melo | 26/11/2026 14:45 | nenhuma | 24 h |

## Observações
- Aprovação de pedido de urgência para pular gate: não existe; registrar e escalar.
| AH-0003 | Adotar como diretriz institucional (01-institucional/tecnologias.md, dono ARQ): APIs de backend do Portal Web em C#/.NET (versão LTS vigente, a confirmar pelo ARQ em fonte oficial) e front-end do Portal Web em Angular (versão estável mais recente, a confirmar pelo ARQ); a AH-0001 (Node.js 24 + Fastify 5) fica substituída para a DEM-2026-001, com ADR-0001 refeito pelo ARQ sem nova AH se seguir a diretriz; plano de capacitação dos agentes envolvidos | arquitetura (alto impacto, institucional) | 26/11/2026 14:52 | (aguardando) | | | | 24 h |
