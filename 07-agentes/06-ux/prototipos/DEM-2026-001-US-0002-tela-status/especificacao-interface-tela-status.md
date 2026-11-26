---
id: UX-ESPEC-DEM-2026-001-TASK-0004
alias: UX-0001
titulo: "Especificação de interface — Tela de status da API (Portal Web)"
tipo: especificacao-interface
versao: 1.1
status: vigente
dono: UX
autores: [UX]
aprovado_por: PO
criado_em: 2026-11-26T12:25-03:00
atualizado_em: 2026-11-26T13:13-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0004, US-0002, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0002, DEC-PO-0005, DEC-PO-0006, DEC-AS-0001, DEC-AS-0002, ADR-0002, ADR-0003, UX-0001, TASK-0003, TASK-0005, TASK-0008]
substitui: null
substituido_por: null
---

# Especificação de interface — Tela de status da API (Portal Web)

> [TESTE] DEM-2026-001 · TASK-0004 (atividade A1 do PO) · US-0002 · Fluxo 01 · Fase de testes internos; nada vai à produção.
> **Status do artefato: vigente — aprovado com ressalvas (DEC-PO-0005, `validacao-po-prototipo-task-0004.md` v1.0, commit af208f2).** Este documento não altera estado, etapa nem gates (só o ORQ).
> **Alias:** UX-0001 (reservado em `00-memoria/registro-ids.yaml`, convenção v1.2; o `id` permanece `UX-ESPEC-DEM-2026-001-TASK-0004`). Campo de frontmatter: `alias` (a convenção pede o alias no frontmatter e não nomeia o campo; usei `alias: UX-0001`).
> Protótipo navegável correspondente: `prototipo-tela-status.html` v1.1 (`tipo: prototipo`, mesma pasta, mesma versão). Dados do protótipo são **fictícios**.
> Rótulos locais `P-UX-nn`, `L-UX-nn`, `D-UX-nn` e `RE-nn` **não são IDs da Stack** (convenção v1.2, regra 3). Decisão formal de UX usaria `DEC-UX-nnnn`.

## 1. Entendimento
- **Pedido (ORQ, MSG-SOL TASK-0004):** prototipar a tela de status do Portal Web com os estados **saudável, carregando e erro**, cobrindo os CA-01 a CA-06 da US-0002 e respeitando RN-0001 (sem informação sensível) e RN-0002 (indisponibilidade nunca aparece como saudável).
- **Alçada do UX (e limites):** layout, textos, indicadores, formato/fuso do timestamp e ação de atualizar são do UX (US-0002). Escopo/regras = PO; stack, formato dos dados e acesso = ARQ/AS; implementação = Full Stack (TASK-0008).
- **Validação (DEC-PO-0005):** o PO aprovou o protótipo/spec v1.0 com ressalvas; esta v1.1 incorpora essas decisões e o alias UX-0001. Não houve republicação de comportamento: RE-01 e RE-05 permanecem opcionais (RE-01 já demonstrada no painel do protótipo).
- **Fora de escopo (US-0002):** histórico, gráficos, alertas, notificações, múltiplos serviços, Mobile, atualização automática (polling — RE-04, demanda futura). Esta especificação **não** cobre o app Mobile.

## 2. Fontes consultadas (IDs e versões)
| Fonte | Versão / ref. | Uso |
|---|---|---|
| US-0002 | **v1.3 vigente** (CA conforme v1.1; revisão editorial v1.3, 26/11/2026 13:10) | Critérios CA-01..CA-06, inclusive caso (b) do CA-03 |
| REQ-0002, REQ-0003, REQ-0004 | v1.2 vigente | Requisitos da tela, erro e segurança |
| RN-0001, RN-0002 | v1.2 vigente | Sem dados sensíveis; indisponibilidade ≠ saudável |
| DEC-PO-0005 / `validacao-po-prototipo-task-0004.md` | v1.0, commit af208f2 | Aprovado com ressalvas; decisões RE-01..RE-05 e D-UX-05/08 |
| DEC-PO-0002 | confirmado pela CPO em 26/11/2026 12:36 (US-0002 v1.3) | Público da tela |
| DEC-PO-0006 | citada na US-0002 / DEC-PO-0005 | 503 de contrato (alternativa A) |
| DEC-AS-0001, DEC-AS-0002 | confirmadas na DEC-ARQ-0002; aceitas pelo PO como premissa | Tempo limite 5 s (sem retry); tolerância do timestamp ±5 s |
| ADR-0003 (health-check `GET /health`) | v1.0, **ainda proposto** (conferido 26/11/2026 13:13; commit 362ea35) | Formato de `status`/`version`/`timestamp`, sem login |
| ADR-0002 (SemVer / campo versão) | v1.0, **ainda proposto** (mesma conferência) | Formato da versão |
| ADR-0001 (stack base) | v1.0, **ainda proposto**; depende de AH-0001 | Portal em HTML/CSS/JS estático (premissa; sem framework) |
| `00-memoria/convencao-ids.md` | v1.2 vigente (merge 067d552 / a1619d6) | Prefixo UX-nnnn e alias UX-0001 |
| `00-memoria/registro-ids.yaml` | `sequencial_global.UX: 1` (reserva DOC) | Alias UX-0001 já reservado; UX não altera o registro |
| contexto.yaml DEM-2026-001 | v26 (commit 03f4f3a) | Ponteiro ainda aponta à v1.0 (ORQ atualiza) |
| EF-0001 v1.2 / ET-0001 v1.3 | em-revisao | Regras de consumo alinhadas a esta tela |

## 3. Premissas (de teste enquanto os ADR permanecerem propostos)
| ID | Premissa | Origem / situação |
|---|---|---|
| P-UX-01 | **Público da tela = operador/equipe técnica interna** (vocabulário técnico moderado e exibição do valor bruto). | **Confirmado pela CPO** em 26/11/2026 12:36 (DEC-PO-0002; US-0002 v1.3). Mudança de público (clientes/usuários finais) é nova decisão da CPO e exigiria revisão do vocabulário. |
| P-UX-02 | **Rótulos/valores de status provisórios:** a API devolve `status = "ok"` no 200 e `"unavailable"` no 503 (ADR-0003, *ainda proposto*). Na tela: `ok` → "API operacional / Saudável"; **qualquer outro valor, ausente ou desconhecido → estado Erro** (lista de permissão; nunca "saudável" por padrão — RN-0002). Os textos em português são rótulos de interface (ADR-0003: texto ao usuário em pt-BR). | ARQ — ADR-0003 **não aceito** nesta conferência; se mudar no G3, o UX revisa rótulos e regras (ressalva 1 da DEC-PO-0005). |
| P-UX-03 | **Sem identidade visual:** paleta neutra provisória, tipografia do sistema (sem fontes externas), cabeçalho "Portal Web" provisório. Tokens = embrião do design system, sem marca. | CPO / PMM (identidade). Aceitável no teste (ressalva 5 da DEC-PO-0005). |
| P-UX-04 | **Tela única, sem login** (ADR-0003, ainda proposto) e sem navegação existente: a tela é a única do Portal base; menu, rota e título de aba definitivos ficam para o ARQ/FS (sugestão não vinculante: rota `/status`). | ARQ; ressalva 1 da DEC-PO-0005. |
| P-UX-05 | **Tempo limite da consulta = 5 s**, do início à resposta completa, **sem nova tentativa automática**. Após o limite, a tela vai ao estado Erro. | **DEC-AS-0001**, confirmada na DEC-ARQ-0002 e aceita pelo PO como premissa até o contrato/ADR serem aceitos no G3. ADR-0003 permanece proposto. |
| P-UX-06 | `timestamp` = instante de geração da resposta pelo servidor, ISO 8601 UTC com `Z` e milissegundos (ADR-0003, proposto). A tela exibe o **valor bruto UTC** (oráculo do CA-01) e, **adicionalmente**, a conversão para America/Sao_Paulo (D-UX-05/08). Tolerância de verificação do QA: ±5 s (DEC-AS-0002). | ARQ / AS; D-UX-05 e D-UX-08 aceitos na DEC-PO-0005. |
| P-UX-07 | Sem atualização automática (polling) **nesta demanda**; só a ação manual "Atualizar status". | ADR-0003; **RE-04 aceita apenas como demanda futura** (DEC-PO-0005). |
| P-UX-08 | Idioma pt-BR; navegadores modernos de desktop e de dispositivos móveis (responsivo). Navegadores-alvo oficiais não definidos. | ARQ / QA |

## 4. Lacunas com dono
| ID | Situação | Dono | Efeito / residual |
|---|---|---|---|
| L-UX-01 | **Resolvida.** Prefixo `UX-nnnn` vigente (convenção v1.2, endosso do UX, merge 067d552 / a1619d6). Alias **UX-0001** reservado (`sequencial_global.UX: 1`); o `id` `UX-ESPEC-DEM-2026-001-TASK-0004` é mantido e o alias entra neste frontmatter (v1.1). | DOC / ORQ (convenção e reserva já feitas) | Ponteiro em `contexto.yaml` / INDEX ainda cita v1.0 — só o ORQ/DOC atualiza. |
| L-UX-02 | **Resolvida.** Público confirmado pela CPO (P-UX-01). | CPO | Se o público mudar para usuário final, revisar vocabulário e a exibição do valor bruto (nova decisão). |
| L-UX-03 | **Aberta.** ADR-0001/0002/0003 **permanecem propostos** (conferido em 26/11/2026 13:13). Stack depende de AH-0001 (R3/N3). | ARQ | Se formatos/`status`/5 s/sem login mudarem no G3, o UX revisa esta spec antes da TASK-0008 (ressalva 1 da DEC-PO-0005). |
| L-UX-04 | **Parcialmente resolvida.** Tempo limite 5 s e ausência de retry: DEC-AS-0001. Tolerância do timestamp ±5 s: DEC-AS-0002. Ambas confirmadas na DEC-ARQ-0002 e aceitas pelo PO como premissa. | AS / ARQ | Residual: vigência definitiva no aceite do contrato/ADR (G3). |
| L-UX-05 | **Aberta.** Regra de acesso à tela (aberta × restrita) e exposição interna × pública. Se a exposição virar pública, reavaliar a exibição da **versão** (RN-0001). | ARQ / CPO | Tela assume acesso aberto interno (P-UX-04, ADR-0003 proposto). |
| L-UX-06 | **Aberta.** Navegação/menu, título de aba, favicon e cabeçalho do Portal base inexistentes. | ARQ / FS / CPO | Cabeçalho "Portal Web" é provisório. RE-05 (título da aba) é opcional — ver seção 12. |
| L-UX-07 | **Aberta.** Navegadores-alvo e meta formal de conformidade (WCAG 2.1 AA assumida pelo PROMPT do UX) não constam em requisito. **Leitor de tela real, outros navegadores e zoom 400%** não foram verificados nesta entrega e **ficam com FS/QA** (ressalva 4 da DEC-PO-0005; itens "V" na seção 10). | PO / QA / FS | Acessibilidade tratada como boa prática até virar REQ; verificação na implementação. |
| L-UX-08 | **Resolvida quanto à validação.** PO aprovou com ressalvas (DEC-PO-0005). Sem teste com usuários (fase de testes internos). | PO | Artefato passa a vigente com as ressalvas das seções 3 e 4. |

## 5. Decisões de design (alçada do UX; rótulos locais)
| ID | Decisão | Justificativa / decisão do PO |
|---|---|---|
| D-UX-01 | **Uma única tela, um único cartão de status** com três estados mutuamente exclusivos (carregando, saudável, erro). | Escopo simples; evita estados mistos que gerariam falso "saudável". |
| D-UX-02 | **Atualizar sempre passa por "Carregando" e remove os valores anteriores do DOM** (não apenas os oculta). | CA-03/CA-04, RN-0002. **Promovido ao CA-04** na US-0002 v1.1 (vigente na v1.3). |
| D-UX-03 | **Estado erro não exibe versão nem timestamp**, mesmo se a API responder 503 com campos. | **Confirmado (RE-02, DEC-PO-0005).** US-0002 CA-03 caso (b). O contrato da API **não muda**: o 503 pode trazer os três campos; só a apresentação os omite. |
| D-UX-04 | **Cor nunca é o único indicador:** ícone distinto (círculo com ✓ / triângulo de alerta / indicador giratório), texto de título, selo textual ("Saudável"/"Erro") e estilo de borda (sólida / sólida com barra lateral / tracejada). | CA-02; WCAG 1.4.1. Aceito como oráculo de indicadores (US-0002 v1.1). |
| D-UX-05 | Exibir o **valor bruto** de `status` e `version` (como recebidos) e o timestamp UTC no formato da API. | **Aceito como oráculo do CA-01** (DEC-PO-0005): igualdade com a mesma consulta; a string formatada em pt-BR **não** substitui o valor bruto. |
| D-UX-06 | Mensagem de erro **única e genérica** para todas as causas (casos (a) e (b) do CA-03). Nunca repassar texto, código HTTP, URL, host ou stack. | RN-0001, CA-03, CA-06. Confirmado na DEC-PO-0005. |
| D-UX-07 | Ação "**Atualizar status**" como botão único, sempre visível e igual nos três estados; durante o carregamento fica `aria-disabled` (mantém o foco). Sem polling. | CA-05; P-UX-07; RE-04 só como demanda futura. |
| D-UX-08 | Timestamp **também** exibido em America/Sao_Paulo no formato `dd/MM/aaaa HH:mm:ss` + legenda "horário de Brasília (UTC−03:00)", além da linha "UTC: \<ISO bruto\>". | **Aceito como oráculo do CA-01** (DEC-PO-0005): a formatação local é **adicional**. |
| D-UX-09 | Paleta neutra provisória com tokens (seção 8). | P-UX-03; ressalva 5 da DEC-PO-0005. |

## 6. Fluxo e arquitetura da informação
Tela única "Status da API" (rota sugerida `/status`, P-UX-04). Hierarquia: cabeçalho do Portal → H1 "Status da API" → texto de apoio → **cartão de status** (título do estado + dados) → botão "Atualizar status".

```
Abrir a tela ──► [CARREGANDO] ──resposta válida (HTTP 200 e status "ok")──► [SAUDÁVEL]
                      │
                      ├─ (a) sem resposta | tempo esgotado (5 s) | HTTP inesperado (≠ 200 e ≠ 503 de contrato) | corpo fora do esquema ─► [ERRO]
                      └─ (b) HTTP 503 com status "unavailable" (se o contrato vigente prever) ─► [ERRO] (mesmo estado; sem versão/timestamp)

[SAUDÁVEL] ──Atualizar status──► [CARREGANDO] (valores antigos removidos do DOM) ──► [SAUDÁVEL] ou [ERRO]
[ERRO]     ──Atualizar status──► [CARREGANDO] ──► [SAUDÁVEL] (recuperação, CA-05) ou [ERRO]
```
Recarregar a página (F5) equivale a "abrir a tela" e também recupera (CA-05).

## 7. Especificação por estado

### 7.1 Estado CARREGANDO (CA-04)
| Item | Especificação |
|---|---|
| Quando | Ao abrir a tela e a cada ação "Atualizar status", enquanto `GET /health` está em andamento (até 5 s, P-UX-05). Toda consulta passa por este estado. |
| Título (H2) | "Verificando status da API…" com indicador giratório (ícone). |
| Texto de apoio | "Aguarde a resposta. Nenhum valor é exibido até a consulta terminar." |
| Dados | **Nenhum valor.** Três linhas de esqueleto (barras cinza, `aria-hidden`) sob os rótulos Status / Versão / Data e hora da resposta. Não usar "—", "0" nem "desconhecido" (poderiam ser lidos como valor). Valores da consulta anterior são **removidos do DOM**, não apenas ocultados (D-UX-02 / CA-04). |
| Erro/saudável | Nenhum indicador de erro nem de saudável. |
| Estilo | Fundo `--carga-bg`, texto `--carga-fg`, borda **tracejada** 2 px. |
| Botão | "Atualizar status" com `aria-disabled="true"` (visual desabilitado; não perde o foco; ativação ignorada). |
| Acessibilidade | Cartão com `aria-busy="true"`; região `aria-live="polite"` anuncia "Verificando status da API." Sem animação se `prefers-reduced-motion` (ícone estático). |
| Limite | Passados 5 s sem resposta completa → Erro caso (a) (P-UX-05 / DEC-AS-0001). Sem barra de progresso nem contagem. Sem nova tentativa automática. |

### 7.2 Estado SAUDÁVEL (CA-01, CA-02)
| Item | Especificação |
|---|---|
| Quando | Resposta HTTP 200, JSON válido com os campos esperados (`status`, `version`, `timestamp`; campos extras são ignorados e **nunca exibidos**) e `status === "ok"`. |
| Título (H2) | Ícone ✓ + "API operacional" + selo textual "Saudável". |
| Texto de apoio | "A API respondeu normalmente à última consulta." |
| Dados (lista de definição) | **Status (valor retornado)**: valor bruto (ex.: `ok`) · **Versão**: valor bruto recebido (ex.: `0.1.0`; sem prefixo "v") · **Data e hora da resposta**: valor bruto UTC (`2026-11-26T15:34:56.789Z`) **e**, adicionalmente, `26/11/2026 12:34:56` + "horário de Brasília (UTC−03:00)". Valores em fonte monoespaçada. **Oráculo do CA-01 (D-UX-05/08, DEC-PO-0005):** os valores brutos (status, versão, timestamp UTC) são iguais aos retornados por `GET /health` **na mesma consulta**; a formatação em America/Sao_Paulo não substitui o bruto. |
| Estilo | Fundo `--ok-bg`, texto `--ok-fg`, borda **sólida** 2 px `--ok-borda`. |
| Acessibilidade | `aria-busy="false"`; região polite anuncia "API operacional. Versão 0.1.0." Lista `<dl>` semântica. |
| Segurança | Valores inseridos **somente como texto** (nunca HTML). Só os três campos aparecem (RN-0001, CA-06). |

### 7.3 Estado ERRO / INDISPONÍVEL (CA-03, CA-05; RN-0002)
| Item | Especificação |
|---|---|
| Quando | **Caso (a):** a API não responde, o tempo de 5 s se esgota, há erro HTTP inesperado (≠ 200 e ≠ 503 de contrato) ou o corpo está fora do esquema. **Caso (b):** a API devolve resposta válida de indisponibilidade (HTTP 503 com `status` `"unavailable"`, se o contrato vigente prever — DEC-PO-0006 alternativa A). Qualquer `status` ≠ `"ok"` (inclusive ausente) também cai neste estado. |
| Título (H2) | Ícone ⚠ (triângulo) + "Status indisponível" + selo textual "Erro". |
| Mensagem | "Não foi possível obter o status da API. Até que uma nova consulta seja concluída com sucesso, não considere a API operacional." (genérica nos casos (a) e (b); sem código HTTP, URL, host ou stack). |
| Dica | "Use “Atualizar status” para tentar novamente." **Opcional (RE-01, DEC-PO-0005, sem novo CA):** se o dispositivo estiver sem conexão, pode-se complementar com "Verifique a conexão deste dispositivo com a rede…", **sem** detalhe técnico (CORS, código HTTP, host). Já demonstrada no painel do protótipo; não é obrigatória para o aceite. |
| Dados | **Nenhum** — inclusive no caso (b): **não exibe versão nem timestamp** recebidos no 503 (RE-02 / D-UX-03, US-0002 CA-03 caso (b)). Sem "último valor conhecido", sem tela em branco. |
| Estilo | Fundo `--erro-bg`, texto `--erro-fg`, borda sólida 2 px + **barra lateral de 8 px** (reforço não cromático). |
| Acessibilidade | Anúncio **assertivo** (`role="alert"`): "Status indisponível. Não foi possível obter o status da API." O foco **não** é movido (permanece no botão, se foi ele a causa). |
| Recuperação | "Atualizar status" → Carregando → (API ok) Saudável (CA-05). Se a nova consulta cair no CA-03, permanece o estado de erro. Recarregar a página tem o mesmo efeito. |

### 7.4 Botão "Atualizar status" (CA-05) — comum aos três estados
Rótulo "Atualizar status" (ícone decorativo `aria-hidden`); altura mínima 44 px; largura mínima 160 px (100 % no móvel); `<button type="button">`; foco visível anel 3 px `--cor-foco` com afastamento de 3 px; ativação por clique, Enter e Espaço; durante o carregamento `aria-disabled="true"` (não usar `disabled`, para não perder o foco). O rótulo **não muda** entre estados (nome acessível estável).

### 7.5 Comportamento comum (para o FS — TASK-0008)
1. `fetch` com tempo limite de 5 s (P-UX-05 / DEC-AS-0001), sem cache (`no-store`), sem polling, sem nova tentativa automática.
2. Validar: HTTP 200 **e** objeto com `status === "ok"`, `version` não vazia (SemVer, ADR-0002 proposto) e `timestamp` ISO 8601 UTC válido. Qualquer falha, inclusive 503 de contrato, → Erro (D-UX-06), **sem** renderizar versão/timestamp. Nunca assumir "saudável" por padrão.
3. Ao iniciar nova consulta: **remover** os valores anteriores do DOM (D-UX-02 / CA-04) antes de mostrar Carregando.
4. Inserir dados via `textContent`; mensagens de erro são **constantes do front**, nunca derivadas da resposta.
5. Não registrar no console/UI conteúdo da resposta de erro; sem dados pessoais ou segredos em qualquer estado (RN-0001, CA-06).
6. Estado inicial ao carregar a página = Carregando (nunca Saudável nem Erro "de partida").
7. **Opcional (RE-05, DEC-PO-0005, sem novo CA):** o título da aba pode refletir o estado (ex.: "Status da API" / "Status da API (erro)"), **sem vazar detalhe técnico** (RN-0001). Não implementado neste HTML; forma a cargo de UX/FS. **Não implementar** "Última tentativa em HH:MM:SS" no erro (RE-03 rejeitada nesta demanda).

## 8. Medidas e tokens (provisórios — P-UX-03)
| Token | Valor | Uso |
|---|---|---|
| Espaçamento | 4 / 8 / 16 / 24 / 32 px | `--esp-1..5` |
| Raio | 8 px (cartão e estados), 6 px (botão) | |
| Tipografia | Fonte do sistema (`system-ui`…); base 16 px / 1,5. H1 28/36 (24/32 abaixo de 600 px); título de estado 24/32 (20/28 móvel); valores 18 px monoespaçados; legendas 14 px | Sem fontes externas |
| Largura do conteúdo | máx. 720 px, centralizado; margens 24 px (16 px móvel) | |
| Cartão | borda 1 px `#6B7280`, padding 24 px (16 px móvel) | |
| Bloco de estado | borda 2 px, padding 16/24 px (16 px móvel) | |
| Lista de dados | 2 colunas (rótulo 160–224 px · valor) com espaço 16/24 px; 1 coluna no móvel | |
| Cores — base | página `#F5F6F8` · superfície `#FFFFFF` · texto `#1B1F24` · texto suave `#4B5563` · ação `#1F4E8C` · foco `#0B3D91` | |
| Cores — saudável | texto `#0F5B2A` · fundo `#E8F5EC` · borda `#1E7B3F` | |
| Cores — erro | texto `#8F1D1D` · fundo `#FDECEC` · borda `#B42318` | |
| Cores — carregando | texto `#1F2937` · fundo `#EEF1F5` · borda `#5B6575` | |
| Movimento | giro 1 s linear; desligado com `prefers-reduced-motion: reduce` | |

## 9. Responsividade (Portal Web)
| Faixa | Comportamento |
|---|---|
| ≥ 600 px (desktop/tablet) | Conteúdo centralizado (máx. 720 px); lista de dados em 2 colunas; selo alinhado à direita do título; botão com largura do conteúdo. |
| < 600 px (móvel; referência 360 px) | Margens 16 px; H1 24 px; lista de dados em **1 coluna** (rótulo acima do valor); selo quebra para linha própria; botão ocupa 100 % da largura; valores longos quebram (`overflow-wrap: anywhere`). |
| 320 px / zoom 200–400 % | Sem rolagem horizontal (reflow, WCAG 1.4.10); nenhuma informação oculta. **Zoom 400% a verificar na implementação (FS/QA)** — ressalva 4 da DEC-PO-0005. |
| Orientação | Retrato e paisagem. |
Verificado no protótipo v1.0/v1.1 em 1100 px e 390 px (capturas de tela em ambiente local; não versionadas). **Mobile app (Java) fora de escopo.**

## 10. Acessibilidade — WCAG 2.1 AA (checklist)
Legenda: **P** = atendido no protótipo (verificado); **V** = a verificar na implementação (TASK-0008) e pelo QA (TASK-0010). Leitor de tela real, outros navegadores e zoom 400% **ficam com FS/QA** (DEC-PO-0005, ressalva 4).

| Critério | Requisito aplicado | Situação |
|---|---|---|
| 1.1.1 Conteúdo não textual | Ícones decorativos `aria-hidden`; o significado está no texto | P |
| 1.3.1 Informação e relações | `<main>`, `h1`/`h2`, `<dl>` para rótulo/valor, `<section>` rotulada | P |
| 1.3.2 Sequência significativa | Ordem do DOM = ordem visual | P |
| 1.4.1 Uso de cor | Ícone + título + selo textual + estilo de borda por estado (D-UX-04) | P |
| 1.4.3 Contraste (texto) | Ver tabela abaixo (todos ≥ 7:1, supera 4,5:1) | P (valores calculados) / V na implementação |
| 1.4.4 Redimensionar texto / 1.4.10 Reflow | Unidades relativas (rem), layout fluido, 320 px sem rolagem horizontal | P / **V (zoom 400%, FS/QA)** |
| 1.4.11 Contraste não textual | Bordas de componente ≥ 3:1 (menor: 4,72:1); foco 10,04:1 | P |
| 1.4.12 Espaçamento de texto | Sem alturas fixas em blocos de texto | P / V |
| 2.1.1 Teclado / 2.1.2 Sem armadilha | Único controle interativo é o botão (Tab, Enter, Espaço) | P |
| 2.4.3 Ordem do foco | Botão é o único foco da tela (após cabeçalho/links do Portal base) | P |
| 2.4.6 / 2.4.7 Cabeçalhos e foco visível | H1 "Status da API"; anel de foco 3 px com afastamento | P |
| 2.2.2 Pausar, parar, ocultar | Único movimento = indicador giratório, curto (≤ 5 s) e desligado com `prefers-reduced-motion` | P |
| 3.1.1 Idioma | `lang="pt-BR"` | P |
| 3.2.2 Em entrada de dados | Ação só por clique no botão; nenhuma mudança de contexto inesperada | P |
| 3.3.x Erros de entrada | Não há campos de entrada | N/A |
| 4.1.2 Nome, função, valor | Botão nativo; nome estável "Atualizar status"; estado via `aria-disabled`/`aria-busy` | P |
| 4.1.3 Mensagens de status | Mudanças anunciadas sem mover o foco: `aria-live="polite"` (carregando/saudável) e `role="alert"` (erro) | P (testado por script no navegador; **leitor de tela real = V, FS/QA**) |
| Alvo de toque | ≥ 44 × 44 px (recomendação; mínimo AA 2.2 = 24 px) | P |
| Modo de alto contraste | Bordas e ícones em `currentColor`; `forced-colors` não depende de fundo | P / V |

**Contraste calculado (WCAG, relação de luminância):**
| Par | Relação |
|---|---|
| Texto `#1B1F24` / superfície `#FFFFFF` · página `#F5F6F8` | 16,56:1 · 15,31:1 |
| Texto suave `#4B5563` / `#FFFFFF` · `#F5F6F8` | 7,56:1 · 6,99:1 |
| Saudável: `#0F5B2A` / `#E8F5EC` (borda `#1E7B3F`/`#E8F5EC`) | 7,33:1 (4,72:1) |
| Erro: `#8F1D1D` / `#FDECEC` (borda `#B42318`/`#FDECEC`) | 7,79:1 (5,76:1) |
| Carregando: `#1F2937` / `#EEF1F5` (borda `#5B6575`/`#EEF1F5`) | 12,96:1 (5,20:1) |
| Botão: `#FFFFFF` / `#1F4E8C` | 8,31:1 |
| Foco `#0B3D91` / `#FFFFFF` | 10,04:1 |
| Esqueleto `#C9CFD8` / `#EEF1F5` | 1,38:1 — decorativo (`aria-hidden`), sem função informativa |

## 11. Matriz de rastreabilidade: estado ↔ CA da US-0002 (v1.3, CA da v1.1) ↔ RN/REQ
| CA (US-0002) | Estado(s) | Elemento / regra de interface (seção) | RN / REQ | Verificação sugerida (QA, TASK-0010) |
|---|---|---|---|---|
| **CA-01** Exibe os dados da API | Saudável | Valores **brutos** iguais aos de `GET /health` na mesma consulta (status, versão, timestamp UTC) + formatação Brasília adicional (7.2; **D-UX-05 e D-UX-08 = oráculo**, DEC-PO-0005) | REQ-0002 | Comparar brutos com a resposta da mesma consulta; a string pt-BR não precisa ser idêntica à da API |
| **CA-02** Saudável legível | Saudável | Ícone ✓ + "API operacional" + selo "Saudável" + borda sólida (7.2; D-UX-04, oráculo da US-0002) | REQ-0002 | Inspeção visual em escala de cinza/sem cor; leitor de tela (FS/QA) |
| **CA-03** Erro ou indisponível, casos (a) e (b) | Erro | Título "Status indisponível", mensagem genérica única, sem valores, sem tela em branco (7.3; D-UX-02/03/06). **Caso (b):** 503 com `unavailable` = mesmo erro, **sem versão/timestamp** (RE-02 confirmada; contrato não muda) | REQ-0003, **RN-0002**, RN-0001 | Caso (a): sem resposta, 5 s, HTTP inesperado, corpo inválido. Caso (b): 503 de contrato. DOM sem valores anteriores |
| **CA-04** Carregamento | Carregando | Título "Verificando status da API…", esqueleto sem valores, `aria-busy`; valores anteriores **removidos do DOM** (7.1; D-UX-02 promovido ao CA) | REQ-0002 | Toda consulta passa por Carregando; nenhum valor nem erro antes da resposta |
| **CA-05** Recuperação | Erro → Carregando → Saudável | Botão "Atualizar status" e recarga da página (7.4, seção 6). Se a nova consulta cair no CA-03, permanece o erro | REQ-0003, RN-0002 | Restaurar API; atualizar; ver Saudável com dados atuais |
| **CA-06** Sem dados sensíveis | Todos | Só status, versão e timestamp **no estado saudável**, mais mensagens genéricas; `textContent`; sem detalhes de erro (7.5; D-UX-06) | REQ-0004, **RN-0001** | Inspecionar DOM/rede/console nos três estados, inclusive no 503 |
| RN-0002 (transversal) | Todos | Lista de permissão `status === "ok"`; estado inicial = Carregando; valores limpos ao atualizar (7.5) | RN-0002 | Teste de caminhos que antes resultariam em "saudável" por engano |

## 12. Recomendações ao PO — decisão registrada (DEC-PO-0005)
| ID | Decisão do PO | Efeito nesta v1.1 |
|---|---|---|
| RE-01 | **Aceita como opcional**, sem novo CA e sem ampliar o escopo. A dica de "sem conexão do dispositivo" pode complementar a mensagem genérica, **sem detalhe técnico** (CORS, código HTTP, host). Não é obrigatória para o aceite. | Mantida no painel do protótipo e descrita em 7.3 como opcional. Forma da dica: UX. |
| RE-02 | **Confirmada.** 503 com `status: "unavailable"` = mesmo estado de erro genérico do CA-03 caso (b); **não exibe versão nem timestamp**. O contrato da API **não muda**. | D-UX-03 vigente; regra em 7.3 e 7.5. |
| RE-03 | **Rejeitada nesta demanda** ("Última tentativa em HH:MM:SS" no erro). Fora do CA-06; pode ser proposta futura. | **Não implementar.** |
| RE-04 | **Aceita apenas como demanda futura** (polling automático). Fora do escopo desta DEM. | P-UX-07 mantida; sem polling. |
| RE-05 | **Aceita como opcional**, sem novo CA. Se implementado, o título da aba **não pode vazar detalhe técnico** (RN-0001). Forma: UX/FS. | Especificado em 7.5 item 7; **não implementado** neste HTML. |

## 13. Impactos e riscos
| Componente | Impacto / risco |
|---|---|
| Portal Web | Define a primeira tela e os tokens iniciais do design system. Risco: retrabalho se os ADR (ainda propostos) mudarem no G3 — mitigação: L-UX-03 e revisão do UX antes da TASK-0008. |
| Backend/APIs | Nenhum campo adicional exigido além de `status`, `version`, `timestamp` (ADR-0003). O 503 **pode** trazer os três campos (contrato inalterado); a tela não os exibe. CORS para a origem do Portal é necessário (ARQ/AS). |
| Mobile, microsserviços, integrações, dados, infraestrutura | Sem impacto. |
| Acessibilidade | Risco médio de regressão se o FS não seguir 7.5 e a seção 10. Leitor de tela real e zoom 400% ficam com FS/QA. |
| Segurança/LGPD | Risco baixo: tela só exibe os três campos como texto no saudável; exposição pública reabriria a análise da versão (L-UX-05). |

## 14. Próximos passos
1. **ORQ:** atualizar o ponteiro em `contexto.yaml` (`prototipos`) para a spec/protótipo **v1.1** e o alias **UX-0001** (commit desta publicação). Só o ORQ grava estado/ponteiros. DOC: atualizar INDEX quando couber.
2. **FS (TASK-0008):** implementar conforme seções 7–10 desta v1.1, após G2/G3 e AH-0001, respeitando RE-02, CA-04 (remoção do DOM) e os oráculos D-UX-05/08. Alinhar viabilidade com o UX antes de fechar (HTML/CSS/JS estático, ADR-0001 ainda proposto). RE-01 e RE-05 são opcionais; RE-03 não entra.
3. **QA (TASK-0010):** oráculos = US-0002 v1.3 (CA da v1.1) + esta spec v1.1 + DEC-PO-0005. Verificar leitor de tela real, outros navegadores e zoom 400%.
4. **ARQ:** informar aceite ou mudança dos ADR-0001/0002/0003 (L-UX-03) para revisão desta spec antes da implementação, se couber.

## 15. Histórico de versões
| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 12:25 (America/Sao_Paulo) | UX | Primeira versão para validação do PO (TASK-0004). Commit 1290f25. |
| 1.1 | 26/11/2026 13:13 (America/Sao_Paulo) | UX | Alias `UX-0001` no frontmatter (id mantido); status vigente (aprovado com ressalvas, DEC-PO-0005); incorpora decisões RE-01..RE-05 e oráculos D-UX-05/08; L-UX-01 e L-UX-02 resolvidas; L-UX-04 parcial (DEC-AS-0001/0002); ADR-0002/0003 conferidos e ainda propostos; rastreio alinhado à US-0002 v1.3. Protótipo HTML alinhado à v1.1 (`tipo: prototipo`) sem mudança de comportamento. |
