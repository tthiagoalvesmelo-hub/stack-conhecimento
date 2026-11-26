# 06-qualidade

Planos e casos de teste (PT-nnnn, CT-nnnn), defeitos BUG-nnnn e pareceres em `pareceres/`.

## pareceres/
| Tipo | ID e nome do arquivo | Dono do conteúdo | Modelo |
|---|---|---|---|
| Parecer de qualidade | `PQ-nnnn-<slug>.md` | QA | `../modelos/parecer-pq.md` |
| Parecer de Code Review (fase atual, sem GitHub) | `CR-nnnn-<slug>.md` — ponteiro na Evidência da TASK de Code Review (Tarefas.csv) | CR (2ª aprovação do ARQ quando crítica) | `../modelos/parecer-cr.md` |
| Análises e pareceres de planejamento (sem prefixo de ID próprio) | nome livre com o ID da TASK, frontmatter padrão | quem os emitiu (ex.: QA) | `../modelos/nota-analise.md` quando aplicável |

Regras: PQ-nnnn e CR-nnnn são prefixos distintos (ver `../00-memoria/convencao-ids.md` v1.3); reserve o número em `../00-memoria/registro-ids.yaml` antes de criar o arquivo; frontmatter padrão em todo documento (`../modelos/frontmatter.md`). Quem escreve em cada tipo de parecer segue a matriz 7.1 vigente de `../00-memoria/protocolo-memoria.md` v1.1 (AH-0002): pareceres CR-nnnn com A = CR e E = ARQ; o restante de 06-qualidade (planos, casos, BUG, PQ) permanece A = QA.
