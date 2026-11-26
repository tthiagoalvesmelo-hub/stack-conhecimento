# MSG-RET — retorno  — MODELO

```
MODELO — MSG-RET
ID da demanda / ID da atividade: [IDs]
Remetente: [agente que executou] | Destinatário: [quem solicitou] (cópia: Orquestrador)
Status: Concluída | Parcial | Bloqueada | Fora de escopo (indicar o agente correto)
Resumo do resultado: [2 a 5 linhas]
Entregáveis: [artefatos, IDs, versões, localização]
Critérios de conclusão atendidos: [critério 1 – OK/NOK; critério 2 – OK/NOK]
Decisões tomadas (na minha alçada): [ID da decisão, descrição, justificativa]
Decisões pendentes (de outros agentes): [decisão – dono]
Riscos: [risco, probabilidade, impacto, mitigação]
Dúvidas: [pergunta – a quem]
Impedimentos: [nenhum | descrição + quem pode resolver]
Impactos nos componentes: Portal Web | Mobile | Backend/APIs | Microsserviços | Integrações | Dados | Infraestrutura
Evidências: [testes, logs, prints, pareceres, links; sem evidência verificável o status é Parcial]
Fontes consultadas: [IDs e versões; lacunas de contexto encontradas]
Artefatos criados/alterados: [caminho e versão]
Próximo responsável sugerido: [agente e atividade]
```

Regras dos contratos (valem para todos os agentes):
- Todo envio entre agentes usa MSG-SOL (ou MSG-COL para colaboração pontual) e todo retorno usa MSG-RET; o Orquestrador recebe cópia de tudo. MSG-BLQ registra impedimentos; MSG-CONS consolida etapas (Orquestrador); MSG-AH é o pedido de aprovação humana (somente o Orquestrador envia ao Thiago).
- Campo obrigatório em branco torna a mensagem inválida: o Orquestrador devolve ao remetente. Artefatos sempre por ID e versão, nunca “o documento mais recente”.
- O retorno sempre informa riscos, dúvidas e impedimentos, mesmo que seja “nenhum”. Status “Concluída” exige evidências verificáveis; sem evidência, o status é “Parcial”.
- Atividade fora da sua especialidade: retorne “Fora de escopo” indicando o agente correto; não execute.
- Decisões só são registradas por quem tem a alçada; o Orquestrador apenas transcreve.
