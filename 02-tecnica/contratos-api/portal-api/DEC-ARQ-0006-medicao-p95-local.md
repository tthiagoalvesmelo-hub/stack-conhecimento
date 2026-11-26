---
id: DEC-ARQ-0006
titulo: "Medição do p95 indicativo local (TASK-0010), condicionada ao ADR-0001"
tipo: dec
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T13:10-03:00
atualizado_em: 2026-11-26T13:10-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, TASK-0012, ADR-0001, ADR-0003, AH-0001]
substitui: null
substituido_por: null
---

# DEC-ARQ-0006 — Medição do p95 indicativo ≤ 100 ms (local)

> [TESTE] **Condicionada à aceitação do ADR-0001**. Sem dependência nova e sem custo. O alvo **não é SLO** e **não bloqueia** aceite funcional (ADR-0003 / ET-0001 RT-14).

## Decisão
Adoto a proposta preferencial do OPS (parecer TASK-0012 §7.2): script versionado em Node embutido, p.ex. `/workspace/projetos/portal/scripts/measure-p95.mjs`, usando o `fetch` global do Node 24, **sem dependência nova**. A OPS cria o script na preparação (após a AH); a QA executa na TASK-0010; a OPS pode reexecutar no G7.

**Parâmetros (método):**

| Parâmetro | Valor |
|---|---|
| Alvo | `GET /health` em loopback, serviço já no ar (não é carga da tela) |
| Aquecimento | 50 requisições, descartadas do cálculo |
| Medição | 200 requisições sequenciais, concorrência 1 |
| Oráculo desta demanda | p95 ≤ 100 ms (indicativo; primeira medição = linha de base provisória) |
| Métricas | min, p50, p95, p99, max, erros, distribuição de status HTTP |
| Condições a registrar | `node -v`, `npm -v`, SHA, `nproc`, `uptime` (load), memória disponível, hora America/Sao_Paulo, declaração de que não há outro ensaio pesado simultâneo |
| Evidência | `evidencias/p95/<AAAA-MM-DDTHHMM-03>-<sha7>/`, gitignorada, sanitizada (sem valores de ambiente) |

Não adoto `autocannon` (nem outra ferramenta de carga) nesta fase: seria dependência nova (ADR-0001 D4). Resultado é indicativo do ambiente local da box; não justifica SLO nem substitui testes funcionais do G5.
