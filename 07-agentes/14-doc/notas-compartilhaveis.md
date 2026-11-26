---
id: AGT-DOC-NOTAS
titulo: "Notas compartilháveis — Beatriz Moraes (Analista de Documentação)"
tipo: agente
versao: 1.1
status: vigente
dono: DOC
autores: [DOC]
aprovado_por: Thiago Melo
criado_em: 2026-11-26T11:00-03:00
atualizado_em: 2026-11-26T14:49-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0011, AH-0002, L-CR2]
substitui: null
substituido_por: null
---

# Notas compartilháveis — Beatriz Moraes · Analista de Documentação

Conhecimento da especialidade que outros agentes podem precisar. Informação da memória nativa que influencie outro agente deve ser publicada aqui (ou na área dona) no mesmo dia, com MSG-COL ao afetado.

## Protocolo de memória v1.1 — vigente (AH-0002)

- `00-memoria/protocolo-memoria.md` **v1.1** está vigente desde 26/11/2026 14:45 (America/Sao_Paulo).
- Aprovação: AH-0002, sem condições. Texto literal transcrito pelo ORQ: “Aprovo AH-0001 e também AH-0002”. Merge do ramo `doc/TASK-0011-matriz-7-1` em main: `3755fc6`.
- Matriz 7.1 desdobrada: pareceres **CR-nnnn** em `06-qualidade/pareceres/` com **A = CR** e **E = ARQ**. O restante de `06-qualidade` (planos, casos, BUG, PQ) permanece **A = QA**.
- Regra **EL-08**: cada agente pode gravar, sem PR, só o contador do próprio prefixo em `00-memoria/registro-ids.yaml` e um novo CONF em `00-memoria/conflitos/`. A = DOC nesses arquivos.

## Onde vive o CR-nnnn (L-CR2, fase atual sem GitHub)

- Arquivo: `06-qualidade/pareceres/CR-nnnn-<slug>.md` (modelo `modelos/parecer-cr.md`; frontmatter `tipo: cr`, `dono: CR`).
- Ponteiro: coluna **Evidência** da linha da TASK de Code Review no `Tarefas.csv` (ID + versão + caminho + commit).
- Convenção: `00-memoria/convencao-ids.md` v1.3 (local definido na v1.1; matriz vigente registrada na v1.3).

## Leia-me.csv v1.1 (aba Leia-me, alçada DOC)

- Fora do Git: `/workspace/stack-memoria/planilha-operacao/Leia-me.csv`.
- A coluna **Evidência** do Tarefas.csv passa a ser atualizada pelo **executor da TASK** na própria linha (FS, MOB, CR, QA, DOC, …). Não altera Ciclos de CR (dono CR) nem Ciclos de QA (dono QA).
- Inclusão em 26/11/2026 14:48 (America/Sao_Paulo), autor DOC, base AH-0002. Evidência (sha256 e diff): `/workspace/stack-memoria/rascunhos/doc/aplicados/leia-me-evidencia-AH-0002-aplicado.md`.
