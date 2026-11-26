SKILL — registrar-incidente
---
name: registrar-incidente
description: Use quando o Analista de Suporte abrir, atualizar ou encerrar um incidente (Fluxo 03).
---
# Registrar incidente
1. Antes de diagnosticar, busque em 04-incidentes (mensagem de erro, serviço, REL) e na base de conhecimento.
2. Crie 04-incidentes/incidentes/<INC-ID>/registro.md (modelo) com severidade P0–P3, tipo A/B/C, serviços, REL relacionada, sintomas — sem dados pessoais.
3. Registre a linha do tempo (append-only) a cada ação: quem, quando, o quê.
4. No encerramento: causa, solução, recuperação, lições aprendidas; crie/atualize KB-nnnn e PRB-nnnn se recorrente; vincule BUG e REL.
5. P0/P1: abra pos-incidente.md (RCA em até 5 dias úteis) com o Arquiteto.
