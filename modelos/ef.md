---
id: EF-nnnn
titulo: "<título da especificação funcional>"
tipo: ef
versao: 1.0
status: rascunho            # rascunho | em-revisao | aprovada | substituida (protocolo-memoria §3: Rascunho → Aprovada → Substituída)
dono: AS
autores: [AS]
aprovado_por: null
criado_em: AAAA-MM-DDTHH:MM-03:00
atualizado_em: AAAA-MM-DDTHH:MM-03:00
revisar_ate: AAAA-MM-DD
relacionados: [DEM-AAAA-nnn, TASK-nnnn, ET-nnnn, US-nnnn, REQ-nnnn, RN-nnnn, ADR-nnnn, DEC-<SIGLA>-nnnn]
substitui: null
substituido_por: null
---

# EF-nnnn — <título> — MODELO

> **Origem do modelo:** estrutura derivada de EF-0001 v1.2 (AS, TASK-0006, DEM-2026-001), criada pela DOC na L-09 (TASK-0011, incremento A). É uma base de navegação e padronização, **não** altera EF-0001. A AS (dona de EF/ET) pode propor ajustes ao modelo por MSG-COL à DOC. Reserve o EF-nnnn em `00-memoria/registro-ids.yaml` antes de criar o arquivo; nome do arquivo = `EF-nnnn-<slug>.md` em `02-tecnica/especificacoes/`. Uma EF tem uma ET par (mesmo escopo).

> [Linha de contexto] demanda · TASK · fluxo · classe de risco (fonte: decisão do ARQ) · autora. Em cada versão, registre o que a incorpora (fontes e versões) e as ressalvas vigentes.

## 1. Objetivo
## 2. Atores e consumidores
| Ator / consumidor | Papel | Fonte |
|---|---|---|
## 3. Casos de uso
### UC-01 — <nome> (US-nnnn)
- Ator · Pré-condição · Fluxo principal · Fluxos alternativos · Pós-condição.
## 4. Regras aplicadas
| Regra | Texto resumido | Onde se aplica |
|---|---|---|
## 5. Comportamento por cenário (resumo funcional; a matriz completa fica na ET)
| ID | Cenário | O que o consumidor vê | Regra |
|---|---|---|---|
## 6. Fora de escopo
## 7. Matriz de rastreabilidade
Legenda das seções (EF, ET, contrato OpenAPI) e versões das fontes (CA/REQ/RN).
### 7.1 Critérios de aceite por US
| CA (US-nnnn vX) | RN | REQ | EF | ET | OAS |
|---|---|---|---|---|---|
### 7.2 Regras e requisitos
| RN / REQ (versão vigente) | Cobertura |
|---|---|
## 8. Lacunas e pendências (dono)
Consolide as da ET; cada lacuna com ID, situação e dono. Nunca invente: lacuna vira pendência com dono.
## 9. Histórico de versões
| Versão | Data/hora | Autor | Mudança |
|---|---|---|---|

Ciclo e versionamento: protocolo-memoria §3 (versão v1, v2… no frontmatter; a demanda referencia a versão usada). Aprovação funcional: PO (G1/G6); especificação: AS (ponto 3 da matriz de aprovações).
