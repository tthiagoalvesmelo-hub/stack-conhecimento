# MSG-SOL — solicitação  — MODELO

```
MODELO — MSG-SOL
ID da demanda: DEM-AAAA-nnn | INC-AAAA-nnn
ID da atividade: TASK-nnnn
Fluxo de origem: Fluxo 01 (negócio) | Fluxo 02 (técnico) | Fluxo 03 (produção)
Remetente: [agente que solicita]
Destinatário / responsável pela atividade: [agente]
Responsável pelo fluxo: PO | Arquiteto Líder | Analista de Suporte
Prioridade: Imediata | Alta | Normal | Baixa · Severidade: P0–P3 (quando aplicável) · Classe de risco: R1 | R2 | R3
Contexto: [por que esta atividade existe; resumo da demanda e das decisões já tomadas]
Objetivo: [resultado que a atividade deve produzir]
Atividade solicitada: [o que exatamente deve ser feito, dentro da especialidade do destinatário]
Prazo (quando definido): [data/hora ou “não definido”]
Dependências: [atividades/gates que precisam estar concluídos; o que esta atividade libera]
Informações disponíveis e PACOTE DE CONTEXTO: [ponteiros: ID + caminho + versão de US, RN, EF/ET, protótipos, ADR, contratos, scripts, logs; decisões que afetam o destinatário; bloqueios conhecidos; o que NÃO foi incluído]
Entregável esperado: [artefato, formato e destino]
Critérios de conclusão: [lista verificável]
Restrições e limites: [o que não está no escopo; decisões que pertencem a outros agentes]
Formato de retorno: MSG-RET
```
