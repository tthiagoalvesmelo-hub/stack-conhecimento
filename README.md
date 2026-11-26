# stack-conhecimento — memória oficial da Stack Multiagentes

> Versão 1.0 · 26/11/2026 · FASE DE TESTES INTERNOS (não é produção).

Este repositório Git é a **fonte de verdade** da memória compartilhada dos 16 agentes da Stack Multiagentes de Desenvolvimento de Software (maximatech.com.br). Responsável e aprovador humano: **Thiago Melo**.

## Estado atual
- Repositório Git **local**, sem remoto: o GitHub ainda não foi conectado (credenciais pendentes). Quando for, ele terá um repositório/diretório inicialmente vazio e este histórico será enviado por AH de governança.
- Backlog e roadmap: planilha Google Sheets “Stack Multiagentes — Operação” (conector pendente). Enquanto isso, espelho CSV em `/workspace/stack-memoria/planilha-operacao/`.
- Stack tecnológica (exceto Mobile em Java) e demais premissas: **a confirmar** — ver `01-institucional/README.md`.

## Como navegar
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
