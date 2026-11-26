---
id: ADR-0001
titulo: "Stack base, estrutura do projeto e convenções do Portal Web e da API base (DEM-2026-001)"
tipo: adr
versao: 1.0
status: proposto
dono: ARQ
autores: [ARQ]
aprovado_por: null
criado_em: 2026-11-26T12:20-03:00
atualizado_em: 2026-11-26T12:20-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, ADR-0002, ADR-0003, DEC-ARQ-0001, US-0001, US-0002, REQ-0001, REQ-0004, RN-0001, INST-TECNOLOGIAS]
substitui: null
substituido_por: null
---

# ADR-0001 — Stack base, estrutura do projeto e convenções (Portal Web e API base)

> [TESTE] Fase de testes internos; nada vai à produção. **Status: PROPOSTO.** Este ADR NÃO é uma decisão em vigor: a stack tecnológica (exceto o Mobile em Java) é premissa a confirmar (Contexto Global; PROMPT do ARQ, seção 1.1). Enquanto não houver AH aprovada, nenhum agente assume esta stack e nenhum código é escrito.

## Contexto
- Demanda DEM-2026-001 [TESTE] (Fluxo 01, responsável PO; G0 aceito pela CPO em 26/11/2026): "endpoint de health-check (GET /health) na API base do Portal Web, retornando status, versão e timestamp, com uma tela simples no Portal que mostre esse status. Projeto do zero." Atividade TASK-0003 (ARQ).
- Não existe código, serviço, banco, contrato, ambiente, pipeline nem ADR anterior. `01-institucional/tecnologias.md` (INST-TECNOLOGIAS v1.0) está como rascunho, com tudo "A CONFIRMAR" exceto o Mobile em Java.
- Escopo funcional (PO): US-0001 (endpoint) e US-0002 (tela), REQ-0001 a REQ-0004, RN-0001 (só informação não sensível) e RN-0002 (indisponibilidade nunca aparece como saudável). Sem persistência (premissa L9 do PO; confirmada abaixo), sem autenticação no escopo, sem Mobile.
- Restrições: custo zero de licença e de infraestrutura; execução local no computador compartilhado (sem GitHub, sem CI, sem ambientes dev/hml); independência entre Portal (consumidor) e API (provedor); segurança e LGPD desde a concepção; stack mínima e reversível.
- Fatos do ambiente verificados em 26/11/2026 (box): Node.js v24.22.1 (LTS "Krypton"), npm 11.21.1, Python 3.13.5, Go 1.27.3, Git 2.47.3; **Java/JDK não instalado** (`java: command not found`); FastAPI/uvicorn não instalados (`pip list`). Consulta ao registro npm no mesmo dia: Fastify 5.12.8 (licença MIT) e @fastify/static 11.0.0 (MIT), dependências de runtime do Fastify listadas pelo registro (pino, avvio, find-my-way, ajv, entre outras). Calendário oficial do Node.js (nodejs/Release, schedule.json): v24 em Maintenance LTS desde 20/10/2026, fim de suporte em 30/04/2028; v26 "Lithium" em LTS desde 28/10/2026 (não instalado).

## Decisão (proposta)
**D1 — Runtime e linguagem (API e Portal):** Node.js 24 LTS (já instalado) e JavaScript moderno (ES2024, módulos ESM), sem etapa de build. TypeScript e transpilação ficam fora desta fase (evita toolchain extra); a adoção exige novo ADR.

**D2 — API base (`portal-api`):** serviço HTTP/JSON em Fastify 5.x (MIT). Única dependência de runtime direta prevista; versões exatas fixadas em `package-lock.json`; instalação por `npm ci`; `npm audit` sem vulnerabilidade alta/crítica como critério de Code Review. Logs estruturados com o logger embutido (pino) e validação por JSON Schema na borda.

**D3 — Portal Web (`portal-web`):** aplicação web estática em HTML5, CSS e JavaScript (módulos ES nativos), **sem framework e sem build**, que consome a API pelo contrato (fetch). Em desenvolvimento/teste, é servida por um servidor estático mínimo em Node (`node:http`, zero dependências), **processo separado da API** (consumidor e provedor independentes; o Portal não é servido pela API). Framework de UI (ex.: React, Vue) só por novo ADR, quando houver mais de uma tela com estado.

**D4 — Testes:** `node:test` e `node:assert` (embutidos) para unitários e integração; integração da API sem rede via `inject` do Fastify; teste de contrato validando a resposta contra o esquema do contrato aprovado (G3); teste de tela e ferramenta de navegador ficam a critério do QA (qualquer dependência nova de teste passa pelo ARQ). Meta inicial de 80% de cobertura no código alterado (padrão da Stack, a calibrar).

**D5 — Fora desta fase (decisão explícita de NÃO adotar):** banco de dados, mensageria, containers, nuvem, CI/CD, autenticação e observabilidade além de logs estruturados. Execução local e vínculo à interface de loopback por padrão. Ambiente de execução do teste e rollback simples: DevOps (A9 do PO). Qualquer item acima vira ADR/demanda própria.

**D6 — Repositório e estrutura (a criar pelos desenvolvedores/DevOps APÓS a aceitação; o ARQ não cria código nem o esqueleto):**

```
/workspace/projetos/portal/                  # repositório Git local (monorepo de teste; sem remoto)
├── README.md                                # visão geral, como instalar/executar/testar, ponteiros para ADR e contrato
├── .gitignore  .editorconfig  .nvmrc        # .nvmrc fixa a série principal do Node (24)
├── apps/
│   ├── portal-api/                          # serviço (provedor)
│   │   ├── package.json  package-lock.json  # "version" = fonte única da versão (ADR-0002)
│   │   ├── src/
│   │   │   ├── server.js                    # bootstrap: lê configuração e sobe o servidor
│   │   │   ├── app.js                       # fábrica da aplicação (testável sem rede)
│   │   │   ├── config/                      # leitura e validação das variáveis de ambiente
│   │   │   ├── health/                      # serviço de saúde: monta {status, version, timestamp}; relógio injetável
│   │   │   ├── routes/health.js             # rota GET /health (camada de apresentação, sem regra)
│   │   │   └── version.js                   # lê e valida a versão do package.json (ADR-0002)
│   │   └── test/{unit,integration,contract}/
│   └── portal-web/                          # consumidor
│       ├── package.json                     # sem dependências de runtime; "version" próprio
│       ├── public/                          # index.html, css/, js/ (módulos: cliente da API, apresentação)
│       ├── serve.js                         # servidor estático de desenvolvimento
│       └── test/
├── scripts/                                 # utilitários do repositório (ex.: conferir versão x tag)
└── docs/README.md                           # SOMENTE ponteiros para o stack-conhecimento (fonte única); não duplica ADR nem contrato
```
Regras da estrutura: um módulo por responsabilidade; **sem código compartilhado entre `portal-api` e `portal-web`** (nem biblioteca comum com regra); cada app com manifesto, testes e versão próprios (sem npm workspaces); o contrato OpenAPI vive em `stack-conhecimento/02-tecnica/contratos-api/portal-api/` (fonte única) e o Portal usa mocks derivados dele (PR-04). Git: ramo `main` sem commits diretos (convenção; proteção técnica inexistente nesta fase), ramos `feat|fix|chore/TASK-nnnn-descricao`, commits citando IDs e trailer `Agente: <sigla>`, tags `portal-api-v<versão>` (ADR-0002).

**D7 — Configuração (somente NOMES; valores fora do repositório, sem segredos):** `PORTAL_API_HOST`, `PORTAL_API_PORT`, `PORTAL_API_ALLOWED_ORIGIN` (origem do Portal para CORS), `LOG_LEVEL` (API); `PORTAL_WEB_PORT`, `PORTAL_API_BASE_URL` (Portal). Padrões seguros: interface de loopback; sem curinga de origem. Dono: FS define a finalidade de cada variável; OPS documenta valores por ambiente.

**D8 — Escolha de stack como decisão N3:** por ser stack de base (novo framework/serviço), esta decisão é **arquitetura de alto impacto — N3, exige AH** (ver "Classe de risco e nível de autonomia").

## Alternativas avaliadas
| # | Alternativa | A favor | Contra / trade-off | Veredito |
|---|---|---|---|---|
| A | **Node 24 + Fastify 5 (API) + Portal estático em JS ES modules** | Node instalado; custo zero (MIT/OpenJS); uma linguagem e uma toolchain para API e Portal; validação por JSON Schema, logs estruturados e ótima testabilidade na borda; Portal sem build reduz superfície de dependências | Fastify traz dependências transitivas (cadeia de suprimentos → lockfile + `npm audit`); Node 24 já em Maintenance LTS; sem tipagem estática | **Proposta** |
| B | Node 24 sem framework (`node:http`) + Portal estático | Zero dependências externas; menor superfície de ataque | Reimplementar roteamento, validação, logs e geração de contrato; não serve como base de vários serviços | Alternativa aceitável se o Thiago preferir zero dependências |
| C | Python 3.13 + FastAPI + páginas Jinja/HTMX | Python instalado; OpenAPI automático | FastAPI/uvicorn/pydantic não instalados; dois estilos (HTML no servidor) misturam Portal e API no mesmo processo | Não escolhida |
| D | Go 1.27 (`net/http` + `html/template`) | Instalado; binário único, zero dependências, bom desempenho | Portal ainda exigiria JS; sem geração de contrato pronta; segundo ecossistema para o Portal | Não escolhida; viável para serviços futuros |
| E | Java (Spring Boot) | Coerência com o Mobile em Java; ecossistema maduro | JDK não instalado; build (Maven/Gradle) e peso desproporcionais a um endpoint | Não escolhida agora; reavaliar quando houver backend compartilhando domínio com o Mobile |
| F | Portal como SPA (React/Vite ou similar) | Escala para muitas telas | Cadeia de build e dezenas de dependências para uma tela; exagero e mais risco de suprimentos | Não escolhida; ADR futuro |
| G | Portal servido pelo mesmo processo da API | Menos um processo | Acopla consumidor e provedor (deploy acoplado) | Rejeitada |
| H | Node 26 "Lithium" (LTS ativa até 2029) em vez do 24 | Suporte mais longo | Não instalado; instalação por DevOps | Variante de A: a troca do major é atualização tecnológica futura (R3 pela regra de major de runtime) |

## Justificativa
- Menor stack que cumpre os requisitos, sem custo e com o que já está instalado (A/H menos instalação).
- Mesma linguagem nos dois componentes reduz toolchain e custo de revisão, sem acoplar processos nem código (D3, D6).
- Fastify entrega, sem código próprio, validação de esquema, logs estruturados e testes sem rede, que são padrões da Stack (validação na borda, logs estruturados, testabilidade); a alternativa B é a opção conservadora para quem prioriza zero dependências.
- Decisão reversível e barata agora: não há código; reverter significa descartar o esqueleto (ver plano de reversão).

## Consequências e impactos
- **Portal Web:** primeira tela e primeiro cliente do contrato; sem framework; consumo por fetch com tratamento obrigatório de erro/indisponibilidade (RN-0002); conteúdo da API inserido no DOM só como texto (nunca como HTML).
- **Mobile (Java):** sem impacto. O contrato REST/JSON é neutro e poderá ser consumido pelo Mobile no futuro.
- **Backend/APIs e microsserviços:** nasce o serviço `portal-api` (primeiro serviço; domínio inicial: API base do Portal). Nenhuma regra de outro domínio entra nele; novos domínios serão serviços próprios. Contrato OpenAPI versionado antes da implementação (G3).
- **Integrações:** nenhuma externa. **Dados:** nenhum (sem banco, sem persistência; DBA não acionado — confirma a premissa L9 do PO).
- **Infraestrutura/DevOps:** execução local, sem container, sem CI, sem custo. Premissas de teste a registrar pelo OPS: ausência de pipeline, de proteção técnica de branch e de ambientes dev/hml (débitos aceitos só pela natureza de teste; viram TD se a stack for aceita).
- **Segurança/LGPD:** nenhuma coleta de dado pessoal; resposta mínima (ADR-0003); dependência externa controlada por lockfile e `npm audit`; sem segredos no repositório (apenas nomes de variáveis).
- **Observabilidade:** logs estruturados na API; health-check como primeira capacidade. Métricas e rastreamento: fora desta fase.
- **Custos:** zero (software livre; sem infraestrutura paga). Se o Thiago optar por qualquer recurso pago, nova AH de custo.
- **Débitos conhecidos:** ausência de CI e de tipagem; monorepo de teste (a decisão de repositório por serviço será reavaliada quando o GitHub for conectado, por ADR).
- **Plano de reversão:** até a primeira implantação, trocar de stack = descartar `/workspace/projetos/portal/` e reescrever o endpoint (horas); depois disso, só por ADR substituto.

## Classe de risco e nível de autonomia
- Este ADR sustenta DEC-ARQ-0001 (classe de risco **R3** da demanda: "novo framework/serviço" na tabela R1–R3).
- **Nível N3 (arquitetura de alto impacto: novo serviço e novo framework; matriz de operações com AH):** requer AH do Thiago antes do primeiro desenvolvimento. Pacote mínimo (esta seção): ADR proposto, alternativas, riscos e plano de reversão. Pedido formal (MSG-AH) só pelo ORQ.
- Não é N3 por custo (zero) nem por segurança/contrato público (ADR-0003: contrato interno).

## Pontos a confirmar (via ORQ/CPO, com o Thiago)
1. Aprova a alternativa A (Node 24 + Fastify 5 + Portal estático) como stack base de teste? Prefere B (zero dependências) ou Node 26?
2. Aprova monorepo local `/workspace/projetos/portal/` com dois apps independentes?
3. Confirma que nenhum recurso pago, nuvem, banco ou autenticação entra neste teste?
Após a resposta: o ARQ atualiza este ADR (status Aceito ou Rejeitado, `aprovado_por` e versão) e preenche `01-institucional/tecnologias.md`. Até lá, tudo que depende da stack segue como "premissa a confirmar".

## Status
Proposto → Aceito (somente o Arquiteto Líder aprova, após a AH do Thiago) → Substituído/Rejeitado. ADR aceito é imutável: para mudar, crie novo ADR com `substitui: ADR-0001`.
