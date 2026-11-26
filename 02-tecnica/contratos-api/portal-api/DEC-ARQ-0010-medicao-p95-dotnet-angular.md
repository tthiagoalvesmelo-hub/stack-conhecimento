---
id: DEC-ARQ-0010
titulo: "Medição do p95 indicativo local (TASK-0010) na stack .NET + Angular"
tipo: dec
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:03-03:00
atualizado_em: 2026-11-26T15:03-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, TASK-0012, AH-0003, ADR-0001, ADR-0003, DEC-ARQ-0007]
substitui: DEC-ARQ-0006
substituido_por: null
---

# DEC-ARQ-0010 — Medição do p95 indicativo ≤ 100 ms (substitui DEC-ARQ-0006)

> [TESTE] O alvo **não é SLO** e **não bloqueia** o aceite funcional (ADR-0003 / ET-0001 RT-14). Sem dependência nova e sem custo.

## Decisão
O **método da DEC-ARQ-0006 permanece idêntico**, porque mede só o endpoint HTTP em loopback, independente da stack. Muda apenas a condição de contexto e o executável:
- Script versionado `scripts/measure-p95.mjs` usando o `fetch` global do **Node 24**, que continua instalado como ferramenta do Angular (ADR-0001 v2 D3). Sem pacote novo, sem `autocannon`.
- Alternativa permitida à OPS, também sem dependência nova: um `HttpClient` em programa de console do .NET. A escolha é da OPS; o método e os parâmetros não mudam.
- **API em Release** (`dotnet run -c Release` ou publicação local), **não** em Debug, e **aquecida** (o JIT do .NET afeta as primeiras requisições): os 50 requests de aquecimento da DEC-ARQ-0006 são obrigatórios e descartados.

| Parâmetro | Valor |
|---|---|
| Alvo | `GET /health` em loopback, serviço no ar |
| Aquecimento | 50 requisições, descartadas |
| Medição | 200 requisições sequenciais, concorrência 1 |
| Oráculo | p95 ≤ 100 ms (indicativo; primeira medição = linha de base provisória) |
| Métricas | min, p50, p95, p99, max, erros, distribuição de status |
| Condições a registrar | `dotnet --version`, `node -v`, configuração (Release), SHA, `nproc`, `uptime`, memória disponível, hora America/São Paulo, declaração de ausência de outro ensaio pesado |
| Evidência | `evidencias/p95/<AAAA-MM-DDTHHMM-03>-<sha7>/`, gitignorada e sanitizada |

Resultado indicativo do ambiente local; não justifica SLO nem substitui testes funcionais do G5.

## O que muda em relação à DEC-ARQ-0006
Troca-se apenas a condição "Node `fetch`, `node -v`" por "API .NET em Release + condições registradas do SDK". Alvo, parâmetros e evidência são os mesmos.
