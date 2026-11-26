---
id: AGT-DOC-NOTAS
titulo: "Notas compartilháveis — Beatriz Moraes (Analista de Documentação)"
tipo: agente
versao: 1.2
status: vigente
dono: DOC
autores: [DOC]
aprovado_por: Thiago Melo
criado_em: 2026-11-26T11:00-03:00
atualizado_em: 2026-11-26T15:40-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0011, AH-0002, AH-0004, L-CR2]
substitui: null
substituido_por: null
---

# Notas compartilháveis — Beatriz Moraes · Analista de Documentação

Conhecimento da especialidade que outros agentes podem precisar. Informação da memória nativa que influencie outro agente deve ser publicada aqui (ou na área dona) no mesmo dia, com MSG-COL ao afetado.

## Protocolo de memória v1.2 — vigente (AH-0004)

- `00-memoria/protocolo-memoria.md` **v1.2** está vigente desde 26/11/2026 15:29 (America/Sao_Paulo), conforme AH-0004 (texto literal transcrito pelo ORQ: “Aprovo AH-0004”; sem condições; commit `27eb1e1`).
- A matriz 7.1 da v1.1 (AH-0002, merge `3755fc6`) permanece válida no que não foi alterado: pareceres **CR-nnnn** em `06-qualidade/pareceres/` com **A = CR** e **E = ARQ**. O restante de `06-qualidade` (planos, casos, BUG, PQ) permanece **A = QA**.
- Áreas protegidas: PR real no GitHub (ramo `doc/<ID>-slug` ou `feat/<ID>-slug`; PR aberto pelo autor; revisão do CR quando aplicável; merge pelo dono da área). Quem produz não aprova. Trabalho em worktree própria; o clone principal permanece em `main`; `git pull` antes de editar.
- Repositórios **públicos**: proibido segredo, credencial ou dado real em commit. Cópia principal: https://github.com/tthiagoalvesmelo-hub/stack-conhecimento.
- Regra **EL-08**: cada agente pode gravar, sem PR, só o contador do próprio prefixo em `00-memoria/registro-ids.yaml` e um novo CONF em `00-memoria/conflitos/`. A = DOC nesses arquivos.

## Onde vive o CR-nnnn (L-CR2)

- Arquivo: `06-qualidade/pareceres/CR-nnnn-<slug>.md` (modelo `modelos/parecer-cr.md` v1.2; frontmatter `tipo: cr`, `dono: CR`).
- Ponteiro: coluna **Evidência** da linha da TASK de Code Review no `Tarefas.csv` (ID + versão + caminho + commit).
- O protocolo v1.2 e a matriz de aprovações v1.1 não redefiniram esse local. A cláusula anterior da convenção (“quando o GitHub for conectado, o CR-nnnn volta a viver no PR”) não foi aplicada. Mudar o local é lacuna para o ORQ e o CR.
- Convenção: `00-memoria/convencao-ids.md` v1.4.

## Leia-me.csv v1.1 (aba Leia-me, alçada DOC)

- Fora do Git: `/workspace/stack-memoria/planilha-operacao/Leia-me.csv`.
- A coluna **Evidência** do Tarefas.csv passa a ser atualizada pelo **executor da TASK** na própria linha (FS, MOB, CR, QA, DOC, …). Não altera Ciclos de CR (dono CR) nem Ciclos de QA (dono QA).
- Inclusão em 26/11/2026 14:48 (America/Sao_Paulo), autor DOC, base AH-0002. Evidência (sha256 e diff): `/workspace/stack-memoria/rascunhos/doc/aplicados/leia-me-evidencia-AH-0002-aplicado.md`.
