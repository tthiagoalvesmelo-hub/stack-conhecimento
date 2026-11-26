---
id: DEC-CPO-0001
titulo: "Priorização da capacitação do time em C#/.NET e Angular (RM-0002) e manutenção da prioridade da DEM-2026-001"
tipo: dec
versao: 1.0
status: vigente
dono: CPO
autores: [CPO]
aprovado_por: CPO
criado_em: 2026-11-26T15:00-03:00
atualizado_em: 2026-11-26T15:00-03:00
revisar_ate: 2027-02-26
relacionados: [AH-0003, RM-0001, RM-0002, DEM-2026-001, ADR-0001]
substitui: null
substituido_por: null
---

# DEC-CPO-0001 — Priorização da capacitação em C#/.NET e Angular

> Fase de testes internos (não é produção).

## Contexto
- Diretriz do Thiago Melo (repassada pelo Jarvis ao ORQ em 26/11/2026 14:49): APIs de backend do Portal Web em C#/.NET, front-end do Portal Web na versão mais recente do Angular, e capacitação de todo o time envolvido.
- A AH-0003 foi aprovada por Thiago Melo em 26/11/2026 14:54 com a frase literal "Aprovo AH-0003". A aprovação foi conferida em planilha-operacao/Aprovacoes-humanas.csv e no commit c15d4f0. A AH-0003 substitui a AH-0001 para a DEM-2026-001.
- O pedido do ORQ veio por MSG-SOL de 26/11/2026 14:51 (contexto v30, 257b1d6).

## Alternativas consideradas
1. Tratar a capacitação como demanda (DEM) na esteira. **Descartada**: não há entrega de software nem tipo correspondente entre os 10 tipos de demanda.
2. Iniciativa de Roadmap com prioridade Normal. **Descartada**: bloquearia na prática todas as demandas futuras de API e front do Portal Web.
3. Iniciativa de Roadmap com prioridade Alta. **Escolhida.**

## Decisão
1. A capacitação entra como iniciativa própria no Roadmap: **RM-0002 "Capacitação do time em C#/.NET e Angular"**, prioridade **Alta**. O ARQ é dono do conteúdo e do plano, e a CPO é dona da prioridade.
2. **Custo zero autorizado.** Qualquer custo com cursos, licenças ou ferramentas exige uma AH própria.
3. A **DEM-2026-001 mantém a prioridade Normal**. A troca de stack não altera o valor estratégico nem a urgência, e a demanda continua sem prazo definido. O impacto em prazo será estimado pelo PO com o ARQ.
4. A DEM-2026-001 é o primeiro exercício prático da RM-0002 e não espera o fim da capacitação para retomar. Ela continua vinculada à RM-0001.

## Justificativa
A capacitação é pré-requisito de toda demanda futura do Portal Web na nova stack. Usar a demanda de teste como prática acelera o aprendizado sem criar um bloqueio artificial.

## Impactados
ARQ (plano de capacitação, ADR-0001 v2, tecnologias.md), PO (estimativa de prazo), FS, MOB, QA, CR e OPS (capacitação), ORQ (registro).

## Lacunas
- O escopo, a carga horária e o prazo da capacitação ainda não foram definidos. Dono: ARQ, no plano.
- L1: a visão e os objetivos de produto continuam ausentes. Dono: CPO, depende da base de conhecimento do Thiago.
