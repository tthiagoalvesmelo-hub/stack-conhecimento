---
id: CONF-0001
titulo: "US-0001, US-0002 e REQ-0004 citam classe de risco R2; DEC-ARQ-0001 e contexto.yaml confirmam R3"
tipo: conf
versao: 1.0
status: aberto
dono: DOC
autores: [AS]
aprovado_por: null
criado_em: 2026-11-26T12:28-03:00
atualizado_em: 2026-11-26T12:28-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0006, US-0001, US-0002, REQ-0004, DEC-ARQ-0001, ET-0001, EF-0001]
substitui: null
substituido_por: null
---

# CONF-0001
- Tipo: desatualizado
- Fontes em conflito (ID + caminho + versão):
  - US-0001 v1.0 (`03-operacional/demandas/DEM-2026-001/historias/US-0001-endpoint-health.md`): cabeçalho e DoR dizem "Classe de risco R2 (padrão; ARQ confirma)".
  - US-0002 v1.0 (`.../historias/US-0002-tela-status.md`): idem.
  - REQ-0004 v1.0 (`.../requisitos/REQ-0004-sem-dados-sensiveis.md`): "confirmação da classe de risco (R2 padrão; R3 se for contrato público)".
  - DEC-ARQ-0001 (historico.md da DEM-2026-001, 26/11/2026 12:22) e `contexto.yaml` v4/v5 (`classe_risco: R3`): classe **R3** confirmada pelo ARQ (primeiro serviço + stack base), já com contrato interno.
- Impacto: leitores da US/REQ podem aplicar R2 (menos testes e aprovações) em vez de R3; a ET-0001/EF-0001 adotam R3 (ADR e decisão prevalecem sobre o texto da US).
- Dono que deve resolver: PO (conteúdo de US/REQ); DOC apenas registra.
- Detectado por / em: AS (Juliana Castro), TASK-0006, 26/11/2026 12:28.
- Resolução: pendente (PO atualiza US-0001, US-0002 e REQ-0004 para refletir R3 ou remove a menção à classe).
