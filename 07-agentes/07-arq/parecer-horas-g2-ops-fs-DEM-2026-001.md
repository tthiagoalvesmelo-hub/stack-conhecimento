---
id: PARECER-ARQ-DEM-2026-001-HORAS-OPS-FS
titulo: "Conversão das estimativas ARQ para horas, recorte OPS e parecer prévio L-12 / teste de tela"
tipo: parecer
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T13:10-03:00
atualizado_em: 2026-11-26T13:10-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, TASK-0007, TASK-0008, TASK-0009, TASK-0010, TASK-0012, DEC-ARQ-0003, DEC-ARQ-0005, DEC-ARQ-0006, ET-0001, AH-0001]
substitui: null
substituido_por: null
---

# Conversão de estimativas, recorte OPS e parecer prévio (FS/AS)

> America/Sao_Paulo, 26/11/2026. Complemento ao PARECER-ARQ-DEM-2026-001-G2 v1.0. **Não é o G3.** G2 já aprovado com observações. A confirmação formal da L-12 fica no G3 (TASK-0007), após a AH-0001.

## 1. Estimativas em horas (conversão da escala 1)

A escala 1 do PROMPT significa “horas” (não dias/semanas). Abaixo, faixas com base no escopo real já conhecido. Não invento duração pontual.

| Trabalho | Escala 1–5 | Faixa em horas | Valor de planejamento (ponto médio da faixa esperada) | Base e premissas |
|---|---|---|---|---|
| TASK-0003 residual | 1 | **1–3 h** se a AH-0001 aceitar a alternativa A; **4–8 h** se escolher B ou Node 26 | **2 h** (caminho A) | Caminho A: ler a decisão da AH, aceitar/rejeitar ADR-0001..0003 já redigidos (sem reescrever o conteúdo), preencher `01-institucional/tecnologias.md` e um MSG-RET curto. Caminho B/Node 26: revisão dos ADR e da DEC-ARQ-0004 (ainda horas, no máximo um dia). |
| TASK-0007 (G3) | 1 | **2–4 h** | **3 h** | Releitura do OpenAPI já na main (~353 linhas, já revisado no merge `cf660fb`), ET-0001 v1.3 (inclui L-12), checklist de G3 do PROMPT e parecer escrito. Premissa: AH-0001 **não** muda as diretrizes do contrato; se mudar, reestimar. |
| 2ª aprovação ARQ no G4 | 1 | **1–2 h** no 1º ciclo; **+1 h** se houver 2º ciclo | **1,5 h** (1º ciclo) | Mesmo PR estimado pelo CR em 300–600 linhas, cujo 1º ciclo o CR mediu em 3 h; a 2ª aprovação é aderência a ADR/contrato + parecer do CR, não substitui o CR. Só após CR favorável ou com observações não bloqueantes. Disponível no mesmo dia útil do parecer do CR. |

## 2. Procedimento da DEC-ARQ-0003 (OPS)

**Aceito** o recorte operacional do parecer TASK-0012 §6, com estes precisões já implícitas na DEC:

- Script raiz `/workspace/projetos/portal/scripts/verify-local.sh` após a AH e o esqueleto; `npm run verify` por app (FS no PR da 0008).
- Evidência em `evidencias/verify/...`, **gitignorada**, sanitizada (SHA, `node`/`npm`, log sem valores de ambiente). O veredito do G4 é a **reexecução do CR**, não só o log do autor.
- CR: checkout do mesmo commit, working tree limpa, Node 24, `./scripts/verify-local.sh` (o script começa com `npm ci`). Divergência ou falha impede o G4.
- Conferência ADR-0002 (manifesto == tag == `/health`) no verify quando a tag e o serviço estiverem no ar; se o serviço não estiver no ar no PR, a terceira ponta fica para o G6 — aceito.
- `portal-web` estático: não inventar etapa que a DEC não pede.

A OPS não reabre os critérios de qualidade (80% de linhas, audit high, lint).

## 3. SAST e p95 (antes da TASK-0010)

- **DEC-ARQ-0005:** recorte desta demanda = `npm audit` + ESLint *recommended* + testes dirigidos da QA. Não adoto `eslint-plugin-security` agora (peer ESLint 10 não declarado). Não adoto Semgrep OSS nesta demanda (ferramenta nova fora do npm).
- **DEC-ARQ-0006:** p95 por script Node embutido, sem dependência nova, parâmetros do OPS §7.2. Não adoto `autocannon`.

## 4. Parecer prévio ao FS/AS (não é G3)

**(a) L-12 (ET-0001 v1.3):** parecer **prévio favorável**. Concordo em estender o princípio da DEC-ARQ-0002 L-05 ao HTTP 500 (CA-09): injeção **somente** na fábrica de teste (ou equivalente de teste), mesmas proibições de controle remoto (endpoint, query, header, env, `FORCE_*`, `NODE_ENV` como interruptor), gancho inerte no bootstrap de execução, **fora do OpenAPI**. Distingo o gancho de teste do gancho de encerramento gracioso (PS-05, só 503). A forma concreta (`app.js` / `buildApp` / `inject` do Fastify) **não** é normativa até a AH-0001. **A confirmação formal é no G3**; não executo o G3 agora.

**(b) Teste de tela em navegador:** não decido o que a QA exige. Se a QA exigir teste em navegador real além dos unitários de módulo do FS, isso é **ferramenta/biblioteca nova** e exige decisão do ARQ (DEC ou ADR) **antes** de entrar no plano da TASK-0010/0008 — por exemplo Playwright (OSS, Apache-2.0) + binários de navegador (preparação OPS). Não é automaticamente N3: não há custo de licença nem nova tecnologia de serviço/banco/framework do produto; N3 de custo só se houver recurso pago. Alternativa **sem dependência nova**: testes de módulo da lógica de apresentação (funções puras, `fetch` mockado, estados da tela) com `node:test`, como o FS já prevê. Uma biblioteca de DOM simulado (`jsdom`, `happy-dom`, `linkedom`) **também** é dependência nova e também passaria pelo ARQ. Qualquer dependência nova de teste segue o ADR-0001 D4.
