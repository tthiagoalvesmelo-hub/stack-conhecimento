---
id: ADR-0002
titulo: "Versionamento semântico e origem do campo 'versão' do GET /health"
tipo: adr
versao: 1.1
status: aceito
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ (aceite técnico no G3; alçada N1/N2; sem AH adicional)
criado_em: 2026-11-26T12:20-03:00
atualizado_em: 2026-11-26T15:06-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, AH-0003, ADR-0001, ADR-0003, US-0001, REQ-0001, RN-0001]
substitui: null
substituido_por: null
---

# ADR-0002 — Versionamento semântico e origem do campo "versão"

> [TESTE] **Status: ACEITO (v1.1)** pelo ARQ no G3 (TASK-0007), em 26/11/2026. O formato (SemVer) independe da stack; a **origem** mudou com a stack: de `package.json` (v1.0, Node, AH-0001 substituída) para a propriedade MSBuild `<Version>` do `.csproj` do `portal-api` (ADR-0001 v2, aceito, AH-0003). **Revisão no mesmo ID** porque a v1.0 nunca foi aceita (imutabilidade só após "Aceito"). **O aceite foi dado no G3 (TASK-0007)**, junto com o contrato; nesta versão só a origem, a verificação e as consequências mudam, não o formato nem a regra de incremento.

## Contexto
- A solicitação exige que `GET /health` retorne a **versão** da API. O PO exige (US-0001, CA-04) que a versão esteja "no formato definido" e seja "igual à versão registrada daquela execução", de modo que o QA consiga comparar os dois valores; RN-0001 proíbe detalhes internos na resposta.
- Padrão da Stack: versão semântica por serviço; tag Git por release e REL-nnnn ligando versões (protocolo de memória, seção 3); contratos de API em SemVer à parte.
- Projeto do zero: não existe versão anterior, release nem REL.

## Decisão (proposta)
1. **Formato:** SemVer 2.0.0, `MAJOR.MINOR.PATCH`, com pré-release opcional (`-rc.N`) para candidatas a release. **Sem metadados de build** (`+...`) e sem hash de commit no valor. Expressão de validação sugerida para o contrato (o AS finaliza): `^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(-[0-9A-Za-z.-]+)?$`.
2. **O que é "a versão":** a versão do **serviço `portal-api` em execução**. Não é a versão do contrato (OpenAPI `info.version`, SemVer própria), nem a do `portal-web`, nem de runtime ou dependências (estes nunca são expostos).
3. **Origem única (SSOT):** a propriedade MSBuild **`<Version>` em `apps/portal-api/src/Portal.Api/Portal.Api.csproj`** (ADR-0001 v2, D6). O compilador a grava em `AssemblyInformationalVersion`; a API a lê **uma vez, na inicialização** (`AssemblyInformationalVersionAttribute` do assembly), valida o formato (expressão do item 1) e a mantém em memória. Nunca é escrita à mão no código nem vem de variável de ambiente. **Falha de leitura ou formato inválido → o serviço não inicia** (nunca "unknown" nem valor padrão). **Obrigatório:** `IncludeSourceRevisionInInformationalVersion=false` em `apps/portal-api/Directory.Build.props`, porque o SDK .NET (8+), com Source Link, anexa `+<hash do commit>` à versão informacional por padrão (fonte: https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props); isso violaria o item 1 (sem metadados de build) e o contrato. A validação do item 1 (que rejeita `+`) é a segunda barreira. O `Directory.Build.props` guarda só as propriedades **comuns**; o `<Version>` fica no `.csproj` do serviço para que os projetos de teste não herdem a versão do serviço.
4. **Regra de incremento:** versão inicial `0.1.0` (série 0.x enquanto for teste). PATCH: correção compatível; MINOR: funcionalidade compatível; MAJOR: quebra de compatibilidade (de contrato → ADR e, se público, AH). `1.0.0` só na primeira release para ambiente que o Thiago declarar como produção/estável, com AH. A versão muda **somente** em commit de release (`chore(release): portal-api vX.Y.Z [TASK-nnnn]`).
5. **Rastreabilidade:** a cada release, tag Git anotada `portal-api-v<versão>` no commit da release (formato **inalterado**), citada no REL-nnnn (DevOps). Verificação obrigatória (script em `scripts/`, executado no Code Review e no G6): `<Version>` do `.csproj` == versão da tag == valor retornado por `GET /health` na execução. O script lê o `<Version>` por análise do XML do `.csproj` (alternativa a verificar: `dotnet msbuild -getProperty:Version`).
6. **Como o QA verifica CA-04:** versão da resposta == `<Version>` do `.csproj` do commit testado == tag do commit (ou `-rc.N` no candidato testado no G5). Três fontes idênticas = rastreável. **A estrutura do oráculo (manifesto + tag + resposta) é a mesma da v1.0; muda apenas o arquivo do manifesto.**
7. **Portal:** exibe a versão **recebida da API** (US-0002). A versão do próprio `portal-web` é independente (`package.json` do workspace Angular) e não é exibida nesta demanda.
8. **Sensibilidade:** expor a versão do serviço em exposição **interna** não é sensível (decisão: RN-0001 permanece satisfeita). Se o endpoint passar a ser exposto fora da rede interna, a exposição da versão (fingerprinting) deve ser reavaliada junto com segurança e contrato público (N3/R3; ver ADR-0003).

## Alternativas avaliadas
| Alternativa | A favor | Contra | Veredito |
|---|---|---|---|
| **SemVer + `<Version>` no `.csproj` + tag Git** | Padrão da Stack; fonte única nativa do MSBuild; verificável por script | Exige disciplina de bump; exige desligar o `+commit` do SDK | **Proposta** |
| `<Version>` em `Directory.Build.props` (versão herdada por todos os projetos) | Um arquivo central | Projetos de teste herdariam a versão do serviço; mistura propriedades comuns com a identidade do serviço | Rejeitada para o `<Version>` (o arquivo guarda só propriedades comuns) |
| Manter `+<hash>` do SDK (padrão) | Rastreabilidade extra | Viola o formato (item 1) e o contrato | Rejeitada |
| Versão injetada por variável de ambiente no deploy | Independe do código | Divergência possível entre artefato e valor; sem pipeline no teste | Rejeitada |
| `git describe`/hash de commit como versão | Rastreabilidade máxima | Não é SemVer; expõe detalhe interno; exige repositório em execução | Rejeitada (hash fica fora da resposta) |
| CalVer (AAAA.MM.nn) | Simples de entender | Não comunica compatibilidade; contraria o padrão (versão semântica por serviço) | Rejeitada |
| Versão única do repositório (monorepo) | Um número só | Acopla Portal e API; contraria independência | Rejeitada |
| Constante no código (hard-coded) | Trivial | Esquecimento de bump; duas fontes | Rejeitada |

## Justificativa
Uma fonte única lida em tempo de inicialização elimina a divergência entre "versão em execução" e "versão registrada"; SemVer comunica compatibilidade a consumidores (Portal agora, Mobile depois); tags e REL dão a ponte com release e rollback.

## Consequências e impactos
- **Portal Web:** consome `version` como texto; trata ausência/formato inválido como resposta inválida (RN-0002).
- **Backend/APIs:** leitor da versão na inicialização (classe própria); teste unitário do bootstrap com versão inválida ou com `+` (serviço não inicia).
- **Contrato (AS):** `version` com a expressão acima; `additionalProperties: false` no objeto de resposta.
- **DevOps:** associa REL-nnnn à versão e à tag; plano de rollback = tag anterior.
- **Dados/Mobile/Infra:** sem impacto.
- **Nível de autonomia:** padrão de versionamento é da alçada do ARQ (N1); o aceite foi dado no G3 (TASK-0007), com o ADR-0001 v2 já aceito. Quebras futuras em contrato público = N3.

## Status
Proposto → **Aceito (v1.1, 26/11/2026)** → Substituído/Rejeitado. ADR aceito é imutável: para mudar, crie novo ADR com `substitui: ADR-0002`.
