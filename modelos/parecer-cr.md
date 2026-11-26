---
id: CR-nnnn
titulo: "Parecer de Code Review — <TASK/PR>"
tipo: cr
versao: 1.0
status: rascunho            # rascunho | em-revisao | vigente | substituido
dono: CR
autores: [CR]               # inclua ARQ quando houver 2ª aprovação (alteração crítica)
aprovado_por: null          # CR; e ARQ na 2ª aprovação, quando exigida
criado_em: AAAA-MM-DDTHH:MM-03:00
atualizado_em: AAAA-MM-DDTHH:MM-03:00
revisar_ate: AAAA-MM-DD
relacionados: [DEM-AAAA-nnn, TASK-nnnn, US-nnnn]
substitui: null
substituido_por: null
---

> **Local de registro na fase atual (sem GitHub):** `06-qualidade/pareceres/CR-nnnn-<slug>.md`. Reserve o CR-nnnn em `00-memoria/registro-ids.yaml` antes de criar o arquivo. Ponteiro (ID + versão + caminho + commit) na coluna **Evidência** da linha da TASK de Code Review no Tarefas.csv. Com o GitHub conectado, o parecer volta a ser registrado no PR (link na TASK). Esta nota e o frontmatter não alteram as regras de mérito abaixo.

# Parecer de Code Review CR-nnnn — MODELO

PR/TASK/DEM: · Autor: · Revisor: (≠ autor) · CI verde: sim/não · Rodada: 1 | 2 (máx. 2; na 3ª escala ao Arquiteto)

Resultado: Aprovado | Aprovado com observações não bloqueantes | Reprovado (lista numerada: arquivo, linha, critério, sugestão)

2ª aprovação do Arquiteto (alteração crítica): sim/não/NA

RESULTADO E REGRAS DO CODE REVIEW
RESULTADOS POSSÍVEIS (PARECER CR-nnnn NO PR):
Aprovado: sem pendências.
Aprovado com observações não bloqueantes: observações viram ajuste opcional no mesmo PR ou TD-nnnn; não impedem o G4.
Reprovado, exigindo correções: lista numerada de problemas (arquivo, linha, critério violado, sugestão) devolvida ao desenvolvedor responsável pelo Orquestrador.
REGRAS:
Pré-requisito: CI verde (build, testes, análise estática, varredura). PR sem CI verde não entra em revisão.
O revisor nunca é o autor. Alteração crítica (R3, segurança, contrato, migração, autenticação, mais de um serviço) exige 2ª aprovação do Arquiteto Líder e nunca é aprovada só pelo autor.
Máximo de 2 ciclos de reprovação por PR; no 3º, o Orquestrador escala ao Arquiteto e ao responsável do fluxo (Prompt 02).
Prazo de referência para o parecer: Imediata/P0–P1 em até 1 h; Alta em 4 h; demais em 1 dia útil.
O merge na main só ocorre com G4 registrado e branch protegida (revisão obrigatória e checks verdes).
O revisor avalia o delta na 2ª rodada, mas pode reabrir qualquer ponto se a correção afetar outra parte.
