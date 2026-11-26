SKILL — recuperar-contexto
---
name: recuperar-contexto
description: Use antes de iniciar qualquer atividade da Stack Multiagentes que tenha um ID de demanda (DEM/INC) ou TASK.
---
# Recuperar contexto antes de executar
1. Confirme o ID da demanda e da TASK na mensagem recebida. Sem ID, peça ao Orquestrador.
2. Em /workspace/stack-memoria/stack-conhecimento, atualize antes de ler (`git pull` para sincronizar o espelho local com origin; confira `git status` e `git log`). Trabalho em worktree própria; o clone principal permanece em main.
3. Leia 03-operacional/demandas/<ID>/contexto.yaml e as últimas 20 linhas de historico.md (ou o item no backlog).
4. Abra os ponteiros do pacote de contexto e os ADR/DEC listados em `decisoes`.
5. Leia só os trechos de 01-institucional e 02-tecnica ligados aos componentes da demanda (use INDEX.md e catálogos).
6. Para incidentes: procure em 04-incidentes por serviço, mensagem de erro e REL relacionada.
7. Verifique bloqueios, dependências e gates pendentes.
8. Escreva um resumo de 5 linhas do que entendeu + fontes (IDs e versões) + lacunas. Se houver lacuna crítica, pare e pergunte ao dono.
