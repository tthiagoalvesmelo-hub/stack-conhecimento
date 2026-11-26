---
id: AGT-ARQ-NOTAS
titulo: "Notas compartilháveis — Ricardo Almeida (Arquiteto Líder)"
tipo: agente
versao: 1.1
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: Thiago Melo
criado_em: 2026-11-26T11:00-03:00
atualizado_em: 2026-11-26T12:21-03:00
revisar_ate: 2027-02-26
relacionados: []
substitui: null
substituido_por: null
---

# Notas compartilháveis — Ricardo Almeida · Arquiteto Líder

Conhecimento da especialidade que outros agentes podem precisar. Informação da memória nativa que influencie outro agente deve ser publicada aqui (ou na área dona) no mesmo dia, com MSG-COL ao afetado.

## 26/11/2026 — DEM-2026-001 [TESTE] · TASK-0003 (ponteiros; a fonte é o ADR)
- Stack base **proposta, NÃO confirmada** (aguarda AH do Thiago via ORQ): ADR-0001 (status proposto). Até a confirmação, nenhum agente assume linguagem, framework ou estrutura; `01-institucional/tecnologias.md` continua "A CONFIRMAR".
- Versão do serviço (SemVer, origem única no manifesto, tag Git): ADR-0002 (proposto).
- Padrão de health-check e diretrizes do contrato `GET /health` (interno, sem autenticação, resposta mínima, timestamp UTC): ADR-0003 (proposto). O OpenAPI é do AS; a validação (G3) é do ARQ.
- Classe de risco da demanda confirmada como R3 (DEC-ARQ-0001, em ramo `doc/DEC-ARQ-0001-risco-r3` aguardando merge do ORQ).
- Regra prática: exposição do `/health` fora da rede interna reabre R3/N3 (contrato público e segurança).
