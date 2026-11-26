---
id: CT-0042
titulo: 'p95 indicativo ≤ 100 ms (DEC-ARQ-0010)'
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

# CT-0042 — p95 indicativo ≤ 100 ms (DEC-ARQ-0010)

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-BB — Black-box da QA (processo real em Release, loopback) |
| Rastreio | DEC-ARQ-0010; ET RT-14; matriz R3 (desempenho); não é CA |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão aprovada no G4; API em **Release** subida por `scripts/start-local.sh` em loopback (`PORTAL_API_HOST`/`PORTAL_API_PORT`; valores no `.env` fora do git).
- Ferramenta de requisição já disponível na box (ex.: `curl`); nenhuma ferramenta nova.

## Passos
1. Confirmar `run/api.configuration=Release` gravado pelo `start-local.sh`.
2. Executar `scripts/measure-p95.mjs`: 50 requisições de aquecimento descartadas + 200 sequenciais, concorrência 1, `GET /health` em loopback.
3. Registrar `dotnet --version`, `node -v`, Release, SHA, `nproc`, `uptime`, memória disponível, hora America/Sao_Paulo e ausência de outro ensaio pesado.

## Resultado esperado (oráculo)
- Relatório com min, p50, p95, p99, max, erros e distribuição de status.
- Oráculo **indicativo**: p95 ≤ 100 ms; a 1ª medição vira linha de base provisória. Não é SLO e não bloqueia o aceite funcional.

## Evidência exigida
- Transcrição sanitizada das requisições e respostas (método, status, cabeçalhos, corpo), hora America/Sao_Paulo, SHA; em `evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado).
