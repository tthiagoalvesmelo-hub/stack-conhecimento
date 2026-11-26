# Convenção de identificadores

> Versão 1.1 · 26/11/2026 · gerado a partir dos Prompts 01–04 da Stack Multiagentes (Prompt 04, Anexo A, tem prioridade).
> v1.1 (TASK-0011, incremento A, DOC): CR-nnnn na fase atual sem GitHub (L-CR2) e prefixo UX-nnnn proposto (L-UX-01). Ver “Histórico desta convenção” ao final.

| Prefixo | Artefato | Formato | Exemplo | Quem cria | Onde vive |
|---|---|---|---|---|---|
| DEM | Demanda (Fluxos 01 e 02) | DEM-AAAA-nnn | DEM-2026-041 | Orquestrador | Backlog + 03-operacional/demandas/ |
| INC | Incidente (Fluxo 03) | INC-AAAA-nnn | INC-2026-118 | Orquestrador / Suporte | 04-incidentes/incidentes/ |
| REQ | Requisito (funcional ou não funcional) | REQ-nnnn | REQ-0101 | PO / Analista de Sistemas | 03-operacional/<DEM>/requisitos/ |
| RN | Regra de negócio | RN-nnnn | RN-0210 | PO (com Analista de Negócio) | 01-institucional/regras-negocio/ |
| US | História de usuário | US-nnnn | US-0301 | PO | Backlog + 03-operacional/<DEM>/historias/ |
| TASK | Atividade/tarefa (técnica ou funcional) | TASK-nnnn | TASK-0412 | Responsável do fluxo / Orquestrador | Backlog + 03-operacional/<DEM>/tarefas/ |
| EF / ET | Especificação funcional / técnica | EF-nnnn / ET-nnnn | ET-0088 | Analista de Sistemas | 02-tecnica/especificacoes/ |
| ADR | Decisão arquitetural | ADR-nnnn | ADR-0031 | Arquiteto Líder | 02-tecnica/adr/ |
| DEC | Decisão não arquitetural (estratégica, de escopo, operacional) | DEC-<SIGLA>-nnnn | DEC-PO-0012 | Agente decisor | historico.md da demanda (+ 00-memoria se transversal) |
| BUG | Defeito (QA ou produção — Tipo C) | BUG-nnnn | BUG-0513 | QA / Suporte | 06-qualidade/defeitos/ |
| REL | Versão/release implantada | REL-nnnn (+ versão semântica) | REL-0057 (pedidos 3.9.0) | DevOps | 05-releases/ |
| CR | Parecer de Code Review | CR-nnnn | CR-0388 | Code Reviewer | PR no repositório de código (link em TASK). **Fase atual (sem GitHub):** `06-qualidade/pareceres/CR-nnnn-<slug>.md` (modelo `modelos/parecer-cr.md`), com ponteiro na coluna Evidência da linha da TASK de Code Review |
| PQ | Parecer de qualidade | PQ-nnnn | PQ-0077 | QA | 06-qualidade/pareceres/ (arquivo `PQ-nnnn-<slug>.md`) |
| PT / CT | Plano / caso de teste | PT-nnnn / CT-nnnn | CT-1204 | QA | 06-qualidade/ |
| RB | Runbook (procedimento operacional) | RB-nnnn | RB-0007 | DevOps / Suporte | 04-incidentes/runbooks/ |
| KB | Artigo da base de conhecimento | KB-nnnn | KB-0042 | Suporte | 04-incidentes/base-conhecimento/ |
| PRB | Problema recorrente | PRB-nnnn | PRB-0009 | Suporte | 04-incidentes/problemas/ |
| TD | Débito técnico | TD-nnnn | TD-0015 | Arquiteto Líder | 02-tecnica/debitos-tecnicos/ |
| CONF | Conflito/inconsistência sinalizada | CONF-nnnn | CONF-0003 | Quem detectou (dono resolve) | 00-memoria/conflitos/ |
| UX *(proposto — endosso do UX pendente)* | Entrega de UX: protótipo + especificação de interface | UX-nnnn | UX-0007 (exemplo) | UX | `07-agentes/06-ux/prototipos/<DEM>-<US>-<slug>/` |
Regras
- Identificadores são únicos, imutáveis e nunca reutilizados; um artefato cancelado mantém o ID com status “cancelado”.
- DEM e INC mantêm o padrão com ano do Prompt 02 (DEM-AAAA-nnn, INC-AAAA-nnn); os demais artefatos usam numeração sequencial global de 4 dígitos (formato do Prompt 03).
- A numeração é reservada no arquivo 00-memoria/registro-ids.yaml (ou gerada pela ferramenta de backlog para DEM/US/TASK, quando adotada) antes da criação do artefato.
- Nome de arquivo = ID + slug curto em minúsculas: ADR-0031-upload-url-preassinada.md.
- Referências cruzadas sempre por ID (e versão quando aplicável: “ET-0088 v2”, “openapi pedidos 1.4.0”).
- Commits, branches e PRs citam os IDs (TASK obrigatório; US/BUG quando houver) — é o elo requisito ↔ código ↔ teste ↔ implantação.

### Identificadores acrescentados pela governança (Prompt 04)
| Prefixo | Artefato | Formato | Exemplo | Quem cria | Onde vive |
|---|---|---|---|---|---|
| AH | Aprovação humana (N3) | AH-nnnn | AH-0007 | Orquestrador | Aba Aprovações humanas + aprovacoes.md da demanda |
| RM | Iniciativa de roadmap | RM-nnnn | RM-0003 | CPO | Aba Roadmap |
| CA | Critério de aceite (local à US) | CA-nn | CA-03 | PO | Dentro da US-nnnn |

### Ajustes de padronização
- Padrão de 4 dígitos para todos os prefixos, exceto DEM e INC (DEM-AAAA-nnn, INC-AAAA-nnn).
- A atividade é TASK-nnnn (campo `demanda: DEM-…`); o antigo DEM-AAAA-nnn-Tnn não é mais usado. Defeitos usam BUG-nnnn (não DEF-).
- Severidade: P0–P3. Prioridade: Imediata/Alta/Normal/Baixa. Risco: R1–R3.
- Reserve o número em `registro-ids.yaml` antes de criar o artefato; IDs nunca são reutilizados.

### Pareceres de revisão e de qualidade na fase atual (L-CR2)
- Sem GitHub, o parecer **CR-nnnn** não vive num PR: é um arquivo `06-qualidade/pareceres/CR-nnnn-<slug>.md`, com o frontmatter padrão (`tipo: cr`, `dono: CR`) e o corpo de `modelos/parecer-cr.md`. O ponteiro (ID + versão + caminho + commit) vai na coluna **Evidência** da linha da TASK de Code Review no Tarefas.csv. **PQ-nnnn** segue em `06-qualidade/pareceres/` (`tipo: pq`, `dono: QA`). Os dois prefixos não colidem; o prefixo do nome do arquivo distingue o tipo.
- Quando o GitHub for conectado, o CR-nnnn volta a viver no PR (link na TASK); os arquivos já criados mantêm o ID.
- Quem pode gravar em `06-qualidade/pareceres/` por tipo de parecer depende da matriz 7.1 do `protocolo-memoria.md`; o desdobramento proposto está num ramo separado, dependente de AH (ver histórico abaixo).

### Prefixo UX-nnnn (L-UX-01) — proposta, aguarda endosso do UX
- Identifica uma **entrega de UX** (protótipo navegável + especificação de interface da mesma US/versão). O ID é reservado em `registro-ids.yaml` (`sequencial_global.UX`) **antes** de a entrega ser criada ou regularizada; nunca é reutilizado. Contador atual: 0 (nenhum reservado).
- Tipos no frontmatter: o UX já usa `tipo: especificacao-interface` na especificação; o protótipo HTML é citado por ela, na mesma versão. Nome de pasta/arquivo: `<ID>-<slug>` quando o ID existir.
- Rótulos locais `P-UX-nn` (premissa), `L-UX-nn` (lacuna), `D-UX-nn` (decisão de design) e `RE-nn` (recomendação ao PO) **não são IDs da Stack**; valem só dentro do documento do UX. Decisões formais continuam em `DEC-UX-nnnn` (padrão DEC-<SIGLA>-nnnn).
- O artefato atual `UX-ESPEC-DEM-2026-001-TASK-0004` (v1.0, em revisão) **não foi alterado**. Um alias `UX-nnnn` só será reservado depois do endosso do UX (pedido de endosso por MSG-COL ao UX, cópia ORQ).

### Histórico desta convenção
| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 | Geração inicial (Prompts 01–04) | Criação |
| 1.1 | 26/11/2026 | DOC | CR-nnnn: local na fase atual (L-CR2); PQ-nnnn: padrão de nome; UX-nnnn proposto (L-UX-01). Sem mudança de regra de quem escreve (matriz 7.1 em ramo próprio, dependente de AH) |
