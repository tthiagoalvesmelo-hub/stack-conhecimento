---
id: DEC-ARQ-0003
titulo: "Substituto local do pré-requisito 'CI verde' (L-CR1) na fase de testes"
tipo: dec
versao: 1.0
status: substituida
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T12:50-03:00
atualizado_em: 2026-11-26T15:03-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0008, TASK-0009, TASK-0012, ADR-0001, DEC-ARQ-0004, L-CR1]
substitui: null
substituido_por: DEC-ARQ-0007
---

# DEC-ARQ-0003 — Substituto local do “CI verde” (L-CR1)

> **SUBSTITUÍDA pela DEC-ARQ-0007** em 26/11/2026 (AH-0003: stack C#/.NET + Angular; ADR-0001 v2). O texto abaixo é preservado como histórico da stack Node/Fastify (AH-0001 substituída) e **não vale mais**.

> [TESTE] Fase de testes internos; nada vai à produção. O ADR-0001 D5 (ainda PROPOSTO, AH-0001) exclui CI/CD nesta fase. O PROMPT exige “CI verde” (build, testes, análise estática, varredura) como pré-requisito do G4. Esta DEC define o **substituto local e reproduzível**. Não é N3 (sem pipeline, sem custo, sem produção). **Não bloqueia a decisão do G2**; bloqueia a **entrada no G4** e deve estar cumprida no PR da TASK-0008.

## Decisão
Adoto, com refinamentos, a proposta do CR (Eduardo Pires):

1. O FS inclui no repositório local (`/workspace/projetos/portal/`, após a AH-0001) um script único e versionado (ex.: `scripts/verify-local.sh`, também exposto como `npm run verify` em cada app aplicável) que, em sequência e com falha imediata, executa:
   - `npm ci` (lockfile obrigatório; instalação reproduzível);
   - lint e análise estática definidos na DEC-ARQ-0004;
   - testes (`npm test`, via `node --test` — ADR-0001 D4) **com cobertura** do runner embutido do Node 24: `node --test --experimental-test-coverage` e limiares `--test-coverage-lines=80` (e funções/ramos, se o FS puder aplicar o mesmo patamar sem ferramenta extra);
   - `npm audit --audit-level=high` (reprova em vulnerabilidade **alta ou crítica**).
2. **Cobertura:** a meta inicial é **80% no código alterado**, conforme o padrão de implementação do PROMPT do ARQ (“meta inicial de 80% de cobertura no código alterado (a calibrar)”). Não invento outro número. A calibração (escopo exato dos includes/excludes, se 80% vale também para branches/functions) é **premissa a confirmar com o QA** antes do G5; até lá, 80% de linhas no código-fonte dos apps (`src/` da API e JS do Portal, excluídos `test/` e `node_modules`) é o limiar de entrada no G4.
3. **Evidência:** o autor anexa à TASK-0008/PR o log completo da execução na box (sem segredos). O CR **reexecuta o mesmo script na box** antes de iniciar a revisão; divergência ou falha impede a entrada no G4 (mitiga o RK-CR1: evidência só do autor).
4. Não há pipeline remota nem serviço pago. Quando o GitHub/CI for conectado, esta DEC é revista (substituto provisório).

## Papel do OPS
Os critérios de qualidade (1–2) são da alçada do ARQ. A **forma operacional** (onde o script vive, como gravar a evidência sem segredo, como o CR reexecuta na box, variáveis só por nome) envolve o DevOps. Peço confirmação do OPS (Diego Carvalho) no MSG-RET do parecer G2; até lá, os critérios acima valem e o procedimento operacional permanece premissa a confirmar, sem abrir a entrada no G4.

## Alternativas
- Esperar CI real: rejeitada (não existe nesta fase; atrasaria o G4 indefinidamente).
- Aceitar só a declaração do autor: rejeitada (RK-CR1).
