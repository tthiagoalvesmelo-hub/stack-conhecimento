SKILL — atualizar-memoria
---
name: atualizar-memoria
description: Use ao criar ou alterar qualquer artefato no repositório de conhecimento da Stack.
---
# Atualizar a memória com rastreabilidade
1. Confirme que a área está na sua alçada (00-memoria/protocolo-memoria.md). Se não estiver, registre CONF ou peça ao dono.
2. atualize o repositório (`git pull` para sincronizar o espelho local com origin; confira `git status` e `git log`); reserve o ID em 00-memoria/registro-ids.yaml se for artefato novo. Trabalho em worktree própria; o clone principal permanece em main.
3. Copie o modelo de modelos/, preencha o frontmatter (id, versao, status, dono, autores, datas, revisar_ate, relacionados).
4. Nunca grave segredos, dados pessoais ou dados de produção.
5. Área protegida: crie o ramo `doc/<ID>-slug` ou `feat/<ID>-slug` e abra PR real no GitHub (aberto pelo autor; revisão do CR quando aplicável; merge pelo dono da área; protocolo-memoria v1.2, AH-0004). Com uma única conta GitHub, a regra “quem produz não aprova” é garantida pelo protocolo, não pela ferramenta. Área não protegida: commit direto. Reserva de ID (EL-08): sem PR, só o contador do próprio prefixo e novo CONF.
6. Mensagem de commit: "<tipo>(<area>): <resumo> [IDs]" + linha final "Agente: <sigla>".
7. Atualize os ponteiros (contexto.yaml da demanda, INDEX.md) e avise os agentes afetados (MSG-COL).
