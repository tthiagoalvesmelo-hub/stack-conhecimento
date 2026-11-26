# Contrato de API — MODELO (OpenAPI 3.1)

> **Origem do modelo:** estrutura derivada de `02-tecnica/contratos-api/portal-api/openapi.yaml` 1.0.0 (proposto, AS; dono ARQ) e das regras de contratos do `00-memoria/protocolo-memoria.md` §3, criada pela DOC na L-09 (TASK-0011, incremento A). Não altera o contrato vigente. Local: `02-tecnica/contratos-api/<servico>/openapi.yaml` (matriz 7.1: dono/aprovador ARQ; AS, FS e MOB propõem por ramo `doc/<ID>-slug`).

## Metadados (comentário no topo do YAML; equivalem ao frontmatter padrão)
```
# Contrato OpenAPI 3.1 — <servico> — <recurso>
#   versão do contrato: X.Y.Z (SemVer próprio; distinto da versão do serviço quando assim decidido em ADR)
#   status: <rascunho | proposto | aprovado | publicado | depreciado>
#   dono: ARQ (aprova) · autor: <sigla> · criado em AAAA-MM-DDTHH:MM-03:00 · atualizado em AAAA-MM-DDTHH:MM-03:00 · revisar até AAAA-MM-DD
#   demanda: DEM-AAAA-nnn · atividade: TASK-nnnn · especificação: EF-nnnn vX / ET-nnnn vX
#   fontes: <ADR, DEC, US/REQ/RN com versões>
#   Itens que dependem de decisão pendente: marcar literalmente "premissa a confirmar (<ID>)".
```

## Esqueleto (chaves de primeiro nível usadas no contrato vigente)
```yaml
openapi: 3.1.0
info:
  title: <servico>
  version: X.Y.Z                # versão do CONTRATO
  summary: <uma linha>
  description: |
    <contrato interno ou público; regras transversais; tempo limite do cliente; o que não é resposta do recurso>
  x-stack:
    demanda: DEM-AAAA-nnn
    atividade: TASK-nnnn
    especificacao: [EF-nnnn, ET-nnnn]
    adr: [ADR-nnnn]
    decisoes: [DEC-<SIGLA>-nnnn]
    status-documento: <proposto | aprovado | ...>
    dono: ARQ
    autor: <sigla>
    classe-de-risco: R1 | R2 | R3
    exposicao: <interna | publica>   # pública = contrato público = N3 + AH
  x-rastreabilidade: {}          # CA/REQ/RN ↔ operação/esquema
tags: []
security: []                      # contrato interno sem autenticação: lista vazia e justificado em ADR/DEC
paths: {}
components:
  parameters: {}
  headers: {}
  schemas: {}
  responses: {}
```

## Regras (do protocolo §3 e da governança)
- Versionamento semântico MAJOR.MINOR.PATCH; CHANGELOG por serviço; quebra de compatibilidade exige MAJOR e ADR.
- Ciclo: Rascunho → Aprovado → Publicado → Depreciado (protocolo §3). O contrato `portal-api` 1.0.0 usa o rótulo “proposto”; o alinhamento do vocabulário com o ARQ é lacuna aberta (não decidida pela DOC).
- Aprovação (G3): Arquiteto Líder. Contrato **público** de API: N3, exige AH-nnnn.
- Valide a sintaxe com ferramenta de OpenAPI antes de propor (a AS usou `openapi-spec-validator` na TASK-0006, conforme historico.md).
- Nunca inclua segredos, hostnames internos, dados pessoais ou de produção.
