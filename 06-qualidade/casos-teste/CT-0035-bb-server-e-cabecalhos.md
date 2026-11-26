---
id: CT-0035
titulo: 'Black-box: sem cabeçalho Server e com no-store/nosniff em toda resposta'
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

# CT-0035 — Black-box: sem cabeçalho Server e com no-store/nosniff em toda resposta

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-BB — Black-box da QA (processo real em Release, loopback) |
| Rastreio | US-0001 CA-05; ADR-0001 v2 D8 item 6 (PV); ET PS-04, RT-09 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão aprovada no G4; API em **Release** subida por `scripts/start-local.sh` em loopback (`PORTAL_API_HOST`/`PORTAL_API_PORT`; valores no `.env` fora do git).
- Ferramenta de requisição já disponível na box (ex.: `curl`); nenhuma ferramenta nova.

## Passos
1. Coletar cabeçalhos completos de 200, HEAD, 404, 405 e preflight no processo real.

## Resultado esperado (oráculo)
- Nenhum cabeçalho `Server` nem outro que revele servidor/runtime/framework.
- `Cache-Control: no-store` e `X-Content-Type-Options: nosniff` em todas.

## Evidência exigida
- Transcrição sanitizada das requisições e respostas (método, status, cabeçalhos, corpo), hora America/Sao_Paulo, SHA; em `evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado).
