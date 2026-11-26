---
id: CT-0033
titulo: 'Black-box: contrato no Kestrel real (GET, HEAD, métodos, 404, preflight)'
tipo: ct
versao: 1.0
status: vigente
dono: QA
autores: [QA]
aprovado_por: QA
criado_em: 2026-11-26T15:35-03:00
atualizado_em: 2026-11-26T15:35-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, PT-0001]
substitui: null
substituido_por: null
---

# CT-0033 — Black-box: contrato no Kestrel real (GET, HEAD, métodos, 404, preflight)

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-BB — Black-box da QA (processo real em Release, loopback) |
| Rastreio | US-0001 CA-01, CA-02, CA-08; ADR-0001 v2 D8 itens 2, 4, 5 (PV) |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão aprovada no G4; API em **Release** subida por `scripts/start-local.sh` em loopback (`PORTAL_API_HOST`/`PORTAL_API_PORT`; valores no `.env` fora do git).
- Ferramenta de requisição já disponível na box (ex.: `curl`); nenhuma ferramenta nova.

## Passos
1. `GET /health`; `HEAD /health`; `POST /health`; `GET /inexistente`; `OPTIONS /health` com cabeçalhos de preflight da origem configurada.

## Resultado esperado (oráculo)
- Mesmos oráculos de CT-0001, CT-0002, CT-0008, CT-0009, CT-0010 e CT-0011, agora no processo Release real.

## Evidência exigida
- Transcrição sanitizada das requisições e respostas (método, status, cabeçalhos, corpo), hora America/Sao_Paulo, SHA; em `evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado).
