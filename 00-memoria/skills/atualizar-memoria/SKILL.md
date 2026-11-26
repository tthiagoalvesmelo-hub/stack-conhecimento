SKILL — atualizar-memoria
---
name: atualizar-memoria
description: Use ao criar ou alterar qualquer artefato no repositório de conhecimento da Stack.
---
# Atualizar a memória com rastreabilidade
1. Confirme que a área está na sua alçada (00-memoria/protocolo-memoria.md). Se não estiver, registre CONF ou peça ao dono.
2. atualize o repositório (sem remoto: `git status`/`git log`); reserve o ID em 00-memoria/registro-ids.yaml se for artefato novo.
3. Copie o modelo de modelos/, preencha o frontmatter (id, versao, status, dono, autores, datas, revisar_ate, relacionados).
4. Nunca grave segredos, dados pessoais ou dados de produção.
5. Área protegida: crie o ramo doc/<ID>-slug e abra PR para o dono aprovar (fase atual: PR local = ramo + MSG-COL ao dono, que faz o merge --no-ff). Área não protegida: commit direto.
6. Mensagem de commit: "<tipo>(<area>): <resumo> [IDs]" + linha final "Agente: <sigla>".
7. Atualize os ponteiros (contexto.yaml da demanda, INDEX.md) e avise os agentes afetados (MSG-COL).
