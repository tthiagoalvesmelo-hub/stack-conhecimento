---
id: CONF-0001
titulo: "US-0001, US-0002 e REQ-0004 citam classe de risco R2; DEC-ARQ-0001 e contexto.yaml confirmam R3"
tipo: conf
versao: 1.1
status: resolvido
dono: DOC
autores: [AS, DOC]
aprovado_por: null
criado_em: 2026-11-26T12:28-03:00
atualizado_em: 2026-11-26T13:01-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0006, TASK-0011, US-0001, US-0002, REQ-0004, DEC-ARQ-0001, ET-0001, EF-0001]
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
- Resolução: **resolvido** em 2026-11-26 13:01 (DOC, TASK-0011 incremento A; MSG-SOL do ORQ e DEC-PO-0007). Texto e conferência (America/Sao_Paulo):
  - US-0001 v1.2 e US-0002 v1.3 (editorial, vigentes): cabeçalho e DoR citam **R3** (DEC-ARQ-0001). Correção feita pelo PO na v1.1 (commit `af208f2`); promoção a vigente v1.2 no commit `babb9fe`.
  - REQ-0004 v1.2 (vigente): a menção “R2 padrão; R3 se for contrato público” foi removida na v1.1 (commit `af208f2`); resta apenas a premissa de reavaliar (R3/N3 + AH) se a exposição deixar de ser interna, coerente com ADR-0002/ADR-0003 (propostos) e com a DEC-ARQ-0001.
  - Fonte de verdade da classe: DEC-ARQ-0001 (historico.md da DEM-2026-001, 26/11/2026 12:22) e `contexto.yaml` (`classe_risco: R3`). EF-0001 v1.2 (commit `3a41a2c`) e ET-0001 v1.3 (commit `bb3e08a`; a v1.2 em `3a41a2c`) já adotam R3.
  - Verificação por busca textual da menção à classe R2 em `historias/` e `requisitos/` da DEM-2026-001, em `01-institucional/regras-negocio/` e nas EF/ET no commit-base `13a10bd`: nenhuma ocorrência; as demais ocorrências no repositório são históricas (historico.md, DEC-ARQ-0002), de modelos (valor padrão) ou descrevem este conflito.
  - O PO reportou a correção em 26/11/2026 12:33 (historico.md); o fechamento formal é do DOC (dono do registro). Nenhum conteúdo de PO, ARQ ou AS foi alterado pelo DOC.
  - Pendente fora deste CONF: o ORQ baixa a pendência “CONF-0001” em `pendencias_contexto` do contexto.yaml (só o ORQ escreve estado).
