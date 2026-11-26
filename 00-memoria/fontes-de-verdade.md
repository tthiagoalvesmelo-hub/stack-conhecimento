# Fontes de verdade (SSOT)

> Versão 1.0 · 26/11/2026 · gerado a partir dos Prompts 01–04 da Stack Multiagentes (Prompt 04, Anexo A, tem prioridade).

| Informação | Fonte de verdade | Ponteiros permitidos em |
|---|---|---|
| Estado/status de demandas e tarefas | Planilha “Stack Multiagentes — Operação” (aba Backlog; na fase atual, espelho CSV em planilha-operacao/); contexto.yaml na contingência | Pacote de contexto, Pages |
| Contexto consolidado da demanda | 03-operacional/<DEM>/contexto.yaml | Backlog (link), mensagens |
| Regras de negócio | 01-institucional/regras-negocio/RN-* | US, EF, contexto da demanda |
| Decisões arquiteturais | 02-tecnica/adr/ADR-* | Contexto, PRs, memória nativa |
| Contratos de API | 02-tecnica/contratos-api/<servico>/ | Código (gerado), EF/ET |
| Modelos de dados | 02-tecnica/modelos-dados/<servico>/ | ET, PRs |
| Código | Repositórios de código no GitHub | TASK, REL |
| Implantações | 05-releases/REL-* (+ tag Git) | INC, contexto da demanda, Pages |
| Incidentes e soluções | 04-incidentes/ | BUG, PRB, KB |
| Credenciais | Cofre / segredos mascarados | Somente o nome da variável |
| Roadmap | Planilha, aba Roadmap (dono: CPO) | Demandas (campo RM-) |
| Aprovações humanas (AH) | Planilha, aba Aprovações humanas + aprovacoes.md da demanda | Releases, mensagens |
| Estado operacional da Stack | 00-memoria/governanca/estado-operacional.md | Todos leem antes de operar em homologação/produção |

Regra: cada tipo de informação tem **um** lugar oficial; nas demais camadas ficam apenas ponteiros (ID + caminho + versão). Atualize sempre a fonte primeiro e depois avise os afetados.
