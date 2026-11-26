# 06-qualidade

Planos e casos de teste (PT-nnnn, CT-nnnn), defeitos BUG-nnnn e pareceres em `pareceres/`.

## pareceres/
| Tipo | ID e nome do arquivo | Dono do conteúdo | Modelo |
|---|---|---|---|
| Parecer de qualidade | `PQ-nnnn-<slug>.md` | QA | `../modelos/parecer-pq.md` |
| Parecer de Code Review | `CR-nnnn-<slug>.md` — ponteiro na Evidência da TASK de Code Review (Tarefas.csv) | CR (2ª aprovação do ARQ quando crítica) | `../modelos/parecer-cr.md` |
| Análises e pareceres de planejamento (sem prefixo de ID próprio) | nome livre com o ID da TASK, frontmatter padrão | quem os emitiu (ex.: QA) | `../modelos/nota-analise.md` quando aplicável |

Regras: PQ-nnnn e CR-nnnn são prefixos distintos (ver `../00-memoria/convencao-ids.md` v1.3, vigente na main); reserve o número em `../00-memoria/registro-ids.yaml` antes de criar o arquivo; frontmatter padrão em todo documento (`../modelos/frontmatter.md`). Quem escreve em cada tipo de parecer segue a matriz 7.1 vigente de `../00-memoria/protocolo-memoria.md` v1.2 (AH-0004; a matriz 7.1 da v1.1, AH-0002, permanece válida no que não foi alterado): pareceres CR-nnnn com A = CR e E = ARQ; o restante de 06-qualidade (planos, casos, BUG, PQ) permanece A = QA.

Fluxo de alteração (protocolo-memoria v1.2, AH-0004): `git pull` antes de editar; worktree própria (o clone principal permanece na `main`); ramo `doc/<ID>-slug` ou `feat/<ID>-slug`; PR real no GitHub; revisão do CR quando aplicável; merge pelo dono da área. Quem produz não aprova — essa regra é registrada no PR; com uma única conta GitHub, ela é do protocolo, não da ferramenta. CODEOWNERS: `/06-qualidade/` A = QA; `/06-qualidade/pareceres/` A = CR (E = ARQ). Os repositórios são públicos: proibido segredo, credencial ou dado pessoal em commit, PR ou comentário.

Local do CR-nnnn: permanece o arquivo em `pareceres/CR-nnnn-<slug>.md`, com ponteiro na Evidência (convenção v1.3). O protocolo v1.2 não redefiniu esse local. A cláusula da convenção v1.3 (“quando o GitHub for conectado, o CR-nnnn volta a viver no PR”) **não é aplicada neste README**; a decisão é do ORQ e do CR.
