# stack-conhecimento — memória oficial da Stack Multiagentes

> Versão 1.2 · 26/11/2026 · FASE DE TESTES INTERNOS (não é produção). AH-0004: PRs reais no GitHub. AH-0003: ponteiro da stack para tecnologias.md v1.1 e ADR-0001 v2.0.

Este repositório Git é a **fonte de verdade** da memória compartilhada dos 16 agentes da Stack Multiagentes de Desenvolvimento de Software (maximatech.com.br). Responsável e aprovador humano: **Thiago Melo**.

## Estado atual
- Cópia principal no GitHub (AH-0004): https://github.com/tthiagoalvesmelo-hub/stack-conhecimento. A pasta local `/workspace/stack-memoria/stack-conhecimento` é o espelho de trabalho, mantido sincronizado com `origin`. Repositório **público**: proibido segredo, credencial ou dado real em commit. PRs reais (ramo `doc/<ID>-slug` ou `feat/<ID>-slug`; PR aberto pelo autor; revisão do CR quando aplicável; merge pelo dono da área).
- Backlog e roadmap: planilha Google Sheets “Stack Multiagentes — Operação” (conector pendente). Enquanto isso, espelho CSV em `/workspace/stack-memoria/planilha-operacao/`.
- Stack tecnológica homologada (AH-0003): `01-institucional/tecnologias.md` v1.1 (vigente, commit `7abc2b1`) e `02-tecnica/adr/ADR-0001-stack-base-portal-api-e-web.md` (ADR-0001 v2.0, aceito, commit `7abc2b1`). O ADR é do ARQ; a DOC só aponta.

## Como navegar
Índice completo com ID, versão e status: [`INDEX.md`](INDEX.md) (mantido pela DOC).

| Pasta | Conteúdo | Dono principal |
|---|---|---|
| `00-memoria/` | Regras da própria memória: protocolo, IDs, SSOT, conflitos, governança, skills | Documentação (DOC) |
| `01-institucional/` | Produto, regras de negócio, arquitetura, padrões, tecnologias, ambientes, segurança | CPO / PO / ARQ |
| `02-tecnica/` | ADRs, contratos de API, modelos de dados, especificações, débitos técnicos | ARQ / AS / DBA / OPS |
| `03-operacional/` | Demandas (contexto.yaml, historico.md, aprovacoes.md), quadro e snapshots da planilha | Orquestrador |
| `04-incidentes/` | Incidentes, problemas, runbooks, base de conhecimento | Suporte |
| `05-releases/` | REL-nnnn por implantação (com tag Git) | DevOps |
| `06-qualidade/` | Planos e casos de teste, defeitos, pareceres de qualidade | QA |
| `07-agentes/NN-sigla/` | PROMPT.md completo de cada agente + notas compartilháveis | cada agente / DOC |
| `08-arquivo/` | Demandas e documentos encerrados ou obsoletos (IDs preservados) | DOC / Orquestrador |
| `modelos/` | Modelos: contexto.yaml, ADR, MSG-*, aprovacoes.md, DoR/DoD etc. | DOC |

Fora do Git, na pasta compartilhada `/workspace/stack-memoria/`: `pacotes-contexto/` (pacotes do Orquestrador), `rascunhos/<sigla>/`, `planilha-operacao/` e `criacao/` (descrições e lista de criação dos agentes).

## Regra central
Cada informação tem **uma única fonte de verdade** (`00-memoria/fontes-de-verdade.md`); nos demais lugares guarda-se apenas um **ponteiro** (ID + caminho + versão). Nunca grave segredos, dados pessoais ou dados de produção.
