---
id: ADR-0002
titulo: "Versionamento semântico e origem do campo 'versão' do GET /health"
tipo: adr
versao: 1.0
status: proposto
dono: ARQ
autores: [ARQ]
aprovado_por: null
criado_em: 2026-11-26T12:20-03:00
atualizado_em: 2026-11-26T12:20-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, ADR-0001, ADR-0003, US-0001, REQ-0001, RN-0001]
substitui: null
substituido_por: null
---

# ADR-0002 — Versionamento semântico e origem do campo "versão"

> [TESTE] **Status: PROPOSTO.** O formato (SemVer) independe da stack; a **origem** (campo `version` do `package.json`) depende do ADR-0001. Por isso este ADR só será aceito depois da decisão sobre o ADR-0001. Se o ARQ aceitar este ADR antes, não há ganho: nenhuma versão é produzida sem código.

## Contexto
- A solicitação exige que `GET /health` retorne a **versão** da API. O PO exige (US-0001, CA-04) que a versão esteja "no formato definido" e seja "igual à versão registrada daquela execução", de modo que o QA consiga comparar os dois valores; RN-0001 proíbe detalhes internos na resposta.
- Padrão da Stack: versão semântica por serviço; tag Git por release e REL-nnnn ligando versões (protocolo de memória, seção 3); contratos de API em SemVer à parte.
- Projeto do zero: não existe versão anterior, release nem REL.

## Decisão (proposta)
1. **Formato:** SemVer 2.0.0, `MAJOR.MINOR.PATCH`, com pré-release opcional (`-rc.N`) para candidatas a release. **Sem metadados de build** (`+...`) e sem hash de commit no valor. Expressão de validação sugerida para o contrato (o AS finaliza): `^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(-[0-9A-Za-z.-]+)?$`.
2. **O que é "a versão":** a versão do **serviço `portal-api` em execução**. Não é a versão do contrato (OpenAPI `info.version`, SemVer própria), nem a do `portal-web`, nem de runtime ou dependências (estes nunca são expostos).
3. **Origem única (SSOT):** o campo `version` do `package.json` de `apps/portal-api` (ADR-0001, D6). A API o lê **uma vez, na inicialização**, valida o formato e o mantém em memória. Nunca é escrito à mão no código nem vem de variável de ambiente (evita divergência entre o binário e o valor informado). **Falha de leitura ou formato inválido → o serviço não inicia** (nunca responder "unknown" nem valor padrão).
4. **Regra de incremento:** versão inicial `0.1.0` (série 0.x enquanto for teste). PATCH: correção compatível; MINOR: funcionalidade compatível; MAJOR: quebra de compatibilidade (de contrato → ADR e, se público, AH). `1.0.0` só na primeira release para ambiente que o Thiago declarar como produção/estável, com AH. A versão muda **somente** em commit de release (`chore(release): portal-api vX.Y.Z [TASK-nnnn]`).
5. **Rastreabilidade:** a cada release, tag Git anotada `portal-api-v<versão>` no commit da release, citada no REL-nnnn (DevOps). Verificação obrigatória (script em `scripts/`, executado no Code Review e no G6): `version` do manifesto == versão da tag == valor retornado por `GET /health` na execução.
6. **Como o QA verifica CA-04:** versão da resposta == `version` do `package.json` do commit testado == tag do commit (ou `-rc.N` no candidato testado no G5). Três fontes idênticas = rastreável.
7. **Portal:** exibe a versão **recebida da API** (US-0002). A versão do próprio `portal-web` é independente (`package.json` do app) e não é exibida nesta demanda.
8. **Sensibilidade:** expor a versão do serviço em exposição **interna** não é sensível (decisão: RN-0001 permanece satisfeita). Se o endpoint passar a ser exposto fora da rede interna, a exposição da versão (fingerprinting) deve ser reavaliada junto com segurança e contrato público (N3/R3; ver ADR-0003).

## Alternativas avaliadas
| Alternativa | A favor | Contra | Veredito |
|---|---|---|---|
| **SemVer + `package.json` + tag Git** | Padrão da Stack; fonte única; verificável por script | Exige disciplina de bump no commit de release | **Proposta** |
| Versão injetada por variável de ambiente no deploy | Independe do código | Divergência possível entre artefato e valor; sem pipeline no teste | Rejeitada |
| `git describe`/hash de commit como versão | Rastreabilidade máxima | Não é SemVer; expõe detalhe interno; exige repositório em execução | Rejeitada (hash fica fora da resposta) |
| CalVer (AAAA.MM.nn) | Simples de entender | Não comunica compatibilidade; contraria o padrão (versão semântica por serviço) | Rejeitada |
| Versão única do repositório (monorepo) | Um número só | Acopla Portal e API; contraria independência | Rejeitada |
| Constante no código (hard-coded) | Trivial | Esquecimento de bump; duas fontes | Rejeitada |

## Justificativa
Uma fonte única lida em tempo de inicialização elimina a divergência entre "versão em execução" e "versão registrada"; SemVer comunica compatibilidade a consumidores (Portal agora, Mobile depois); tags e REL dão a ponte com release e rollback.

## Consequências e impactos
- **Portal Web:** consome `version` como texto; trata ausência/formato inválido como resposta inválida (RN-0002).
- **Backend/APIs:** novo módulo `version.js`; teste unitário do bootstrap com manifesto inválido (serviço não inicia).
- **Contrato (AS):** `version` com a expressão acima; `additionalProperties: false` no objeto de resposta.
- **DevOps:** associa REL-nnnn à versão e à tag; plano de rollback = tag anterior.
- **Dados/Mobile/Infra:** sem impacto.
- **Nível de autonomia:** padrão de versionamento é da alçada do ARQ (N1); aceito por mim após o ADR-0001. Quebras futuras em contrato público = N3.

## Status
Proposto → Aceito (somente o Arquiteto Líder aprova) → Substituído/Rejeitado. ADR aceito é imutável: para mudar, crie novo ADR com `substitui: ADR-0002`.
