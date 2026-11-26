---
id: UX-ESPEC-DEM-2026-001-TASK-0004
titulo: "Especificação de interface — Tela de status da API (Portal Web)"
tipo: especificacao-interface
versao: 1.0
status: em-revisao
dono: UX
autores: [UX]
aprovado_por: null
criado_em: 2026-11-26T12:25-03:00
atualizado_em: 2026-11-26T12:25-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0004, US-0002, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0002, ADR-0003, TASK-0003, TASK-0005, TASK-0008]
substitui: null
substituido_por: null
---

# Especificação de interface — Tela de status da API (Portal Web)

> [TESTE] DEM-2026-001 · TASK-0004 (atividade A1 do PO) · US-0002 · Fluxo 01 · Fase de testes internos; nada vai à produção.
> **Status do artefato: em revisão — validação do PO pendente.** Este documento não altera estado, etapa nem gates (só o ORQ).
> Protótipo navegável correspondente: `prototipo-tela-status.html` v1.0 (mesma pasta). Dados do protótipo são **fictícios**.
> Rótulos locais `P-UX-nn` (premissa), `L-UX-nn` (lacuna), `D-UX-nn` (decisão de design), `RE-nn` (recomendação ao PO) **não são IDs da Stack**; não há prefixo de ID para protótipo/especificação de UX em `00-memoria/convencao-ids.md` (ver L-UX-01).

## 1. Entendimento
- **Pedido (ORQ, MSG-SOL TASK-0004):** prototipar a tela de status do Portal Web com os estados **saudável, carregando e erro**, cobrindo os CA-01 a CA-06 da US-0002 e respeitando RN-0001 (sem informação sensível) e RN-0002 (indisponibilidade nunca aparece como saudável).
- **Alçada do UX (e limites):** layout, textos, indicadores, formato/fuso do timestamp e ação de atualizar são do UX (US-0002, nota dos CA). Escopo/regras = PO; stack, formato dos dados e acesso = ARQ/AS; implementação = Full Stack (TASK-0008).
- **Fora de escopo (US-0002):** histórico, gráficos, alertas, notificações, múltiplos serviços, Mobile. Esta especificação **não** cobre o app Mobile.

## 2. Fontes consultadas (IDs e versões)
| Fonte | Versão / ref. | Uso |
|---|---|---|
| US-0002 | v1.0 (em-revisao) | Critérios CA-01..CA-06 |
| REQ-0002, REQ-0003, REQ-0004 | v1.0 (em-revisao) | Requisitos da tela, erro e segurança |
| RN-0001, RN-0002 | v1.0 (em-revisao) | Sem dados sensíveis; indisponibilidade ≠ saudável |
| analise-po-task-0002.md (DEC-PO-0001, DEC-PO-0002) | v1.0, commit 9bde637 | Público (premissa) e atividade A1 |
| ADR-0003 (health-check `GET /health`) | v1.0, **proposto** (commit 362ea35) | Formato de `status`/`version`/`timestamp`, tempo limite, sem login |
| ADR-0002 (SemVer / campo versão) | v1.0, **proposto** | Formato da versão |
| ADR-0001 (stack base) | v1.0, **proposto**; depende de AH-0001 | Portal em HTML/CSS/JS estático (premissa; sem framework) |
| contexto.yaml DEM-2026-001 | v4 (commit 454f49e) | Estado das TASK; risco R3 (DEC-ARQ-0001) |
| protocolo-memoria.md / PROMPT UX / modelos (msg-ret, frontmatter) | v1.0 | Regras de escrita e formato |
| Identidade visual / design system | **inexistente** | Ver P-UX-03 |

## 3. Premissas (todas de teste, até confirmação do dono)
| ID | Premissa | Origem / dono da confirmação |
|---|---|---|
| P-UX-01 | **Público da tela = operador/equipe técnica interna** (usa-se vocabulário técnico moderado e exibe-se o valor bruto retornado pela API). | DEC-PO-0002 — CPO confirma |
| P-UX-02 | **Rótulos/valores de status provisórios:** a API devolve `status = "ok"` no 200 e `"unavailable"` no 503 (ADR-0003, *proposto*). Na tela: `ok` → "API operacional / Saudável"; **qualquer outro valor, ausente ou desconhecido → estado Erro** (lista de permissão; nunca "saudável" por padrão — RN-0002). Os textos em português são **rótulos de teste** (ADR-0003 manda que o texto ao usuário seja pt-BR). | ARQ (TASK-0003; ADR-0003 ainda não aceito) / PO |
| P-UX-03 | **Sem identidade visual:** paleta neutra provisória, tipografia do sistema (sem fontes externas), cabeçalho "Portal Web" provisório. Os tokens deste documento são o **embrião** do design system, sem marca. | CPO / PMM (identidade) |
| P-UX-04 | **Tela única, sem login** (ADR-0003, proposto) e sem navegação existente: a tela é a única do Portal base; menu, rota e título de aba definitivos ficam para o ARQ/FS (sugestão não vinculante: rota `/status`). | ARQ |
| P-UX-05 | **Tempo limite da consulta = 5 s** (orientação do ADR-0003; a ET/AS fecha). Após o limite, a tela vai ao estado Erro. | AS / ARQ |
| P-UX-06 | `timestamp` = instante de geração da resposta pelo servidor, ISO 8601 UTC com `Z` e milissegundos (ADR-0003). A tela converte **somente para exibição** a America/Sao_Paulo. | ARQ / AS |
| P-UX-07 | Sem atualização automática (polling) nesta demanda; só a ação manual "Atualizar status" (ADR-0003: polling fora do escopo; "UX decide a ação"). | ARQ / PO |
| P-UX-08 | Idioma pt-BR; navegadores modernos de desktop e de dispositivos móveis (responsivo). Navegadores-alvo oficiais não definidos. | ARQ / QA |

## 4. Lacunas com dono
| ID | Lacuna | Dono | Efeito se não resolvida |
|---|---|---|---|
| L-UX-01 | Não existe prefixo/ID para protótipo ou especificação de UX em `convencao-ids.md`; o UX **não** tem permissão de escrita em `00-memoria/` (matriz: apenas ORQ, PO, ARQ têm E; DOC é A). Nenhum ID foi reservado em `registro-ids.yaml`; os artefatos são identificados por `UX-ESPEC-…`/nome de arquivo + TASK-0004 + versão. | DOC / ORQ | Rastreio só por TASK/US/commit; pedir decisão sobre prefixo (ex.: `PROTO-nnnn`) ou confirmar o uso do ID do documento. |
| L-UX-02 | Público confirmado (P-UX-01). | CPO | Se for usuário final não técnico, revisar vocabulário e a exibição do valor bruto. |
| L-UX-03 | ADR-0001/0002/0003 estão **propostos** (stack depende de AH-0001, R3/N3): valores de `status` e formatos podem mudar. | ARQ | Revisar P-UX-02/05/06 se mudarem. |
| L-UX-04 | Tempo limite e política de nova tentativa definitivos. | AS (ET) / ARQ | Mantém 5 s como premissa. |
| L-UX-05 | Regra de acesso à tela (aberta × restrita) e exposição interna × pública. Se a exposição virar pública, reavaliar a exibição da **versão** (RN-0001, pendência do ARQ). | ARQ / CPO | Tela hoje assume acesso aberto interno. |
| L-UX-06 | Navegação/menu, título de aba, favicon e cabeçalho do Portal base inexistentes. | ARQ / FS / CPO | Cabeçalho "Portal Web" é provisório. |
| L-UX-07 | Navegadores e dispositivos-alvo e meta de conformidade (WCAG 2.1 AA assumida pelo PROMPT do UX) não constam em requisito. | PO / QA | Acessibilidade tratada como boa prática até virar REQ. |
| L-UX-08 | Validação do protótipo pelo PO **pendente**; sem teste com usuários (fase de testes internos). | PO | Artefato permanece em revisão. |

## 5. Decisões de design (alçada do UX; rótulos locais)
| ID | Decisão | Justificativa |
|---|---|---|
| D-UX-01 | **Uma única tela, um único cartão de status** com três estados mutuamente exclusivos (carregando, saudável, erro). | Escopo simples; evita estados mistos que gerariam falso "saudável". |
| D-UX-02 | **Atualizar sempre passa por "Carregando" e remove os valores anteriores do DOM** (não apenas os oculta). | CA-03/CA-04, RN-0002: nunca exibir valor antigo como atual. |
| D-UX-03 | **Estado erro não exibe versão nem timestamp**, mesmo se a API responder 503 com campos. | CA-03/CA-06 (só mensagens genéricas); evita exibir dado de resposta não saudável como atual. |
| D-UX-04 | **Cor nunca é o único indicador:** cada estado tem ícone distinto (círculo com ✓ / triângulo de alerta / indicador giratório), texto de título, selo textual ("Saudável"/"Erro") e estilo de borda diferente (sólida / sólida com barra lateral / tracejada). | CA-02; WCAG 1.4.1. |
| D-UX-05 | Exibir o **valor bruto** de `status` ("ok") ao lado do rótulo amigável, e o timestamp também em UTC ISO. | P-UX-01; CA-01 ("valores iguais aos da API") fica verificável a olho nu e por QA. |
| D-UX-06 | Mensagem de erro **única e genérica** para todas as causas (sem resposta, tempo esgotado, erro HTTP, conteúdo inválido, 503). Nunca repassar texto, código HTTP, URL, host ou stack da API/navegador. | RN-0001, CA-03, CA-06. |
| D-UX-07 | Ação "**Atualizar status**" como botão único, sempre visível e igual nos três estados; durante o carregamento fica `aria-disabled` (mantém o foco). Sem polling. | CA-05; ADR-0003 (UX decide); P-UX-07. |
| D-UX-08 | Timestamp exibido em **America/Sao_Paulo** no formato `dd/MM/aaaa HH:mm:ss` + legenda "horário de Brasília (UTC−03:00)", e a linha "UTC: <ISO bruto>". | Pedido da US-0002 (UX define formato/fuso); P-UX-06. |
| D-UX-09 | Paleta neutra provisória com tokens (seção 8). | P-UX-03. |

## 6. Fluxo e arquitetura da informação
Tela única "Status da API" (rota sugerida `/status`, P-UX-04). Hierarquia: cabeçalho do Portal → H1 "Status da API" → texto de apoio → **cartão de status** (título do estado + dados) → botão "Atualizar status".

```
Abrir a tela ──► [CARREGANDO] ──resposta válida (status "ok")────────► [SAUDÁVEL]
                      │
                      └─ sem resposta | tempo esgotado (5 s) | HTTP ≠ 200 | JSON/campos inválidos | status ≠ "ok" ─► [ERRO]

[SAUDÁVEL] ──Atualizar status──► [CARREGANDO] (valores antigos removidos) ──► [SAUDÁVEL] ou [ERRO]
[ERRO]     ──Atualizar status──► [CARREGANDO] ──► [SAUDÁVEL] (recuperação, CA-05) ou [ERRO]
```
Recarregar a página (F5) equivale a "abrir a tela" e também recupera (CA-05).

## 7. Especificação por estado

### 7.1 Estado CARREGANDO (CA-04)
| Item | Especificação |
|---|---|
| Quando | Ao abrir a tela e a cada ação "Atualizar status", enquanto `GET /health` está em andamento (até 5 s). |
| Título (H2) | "Verificando status da API…" com indicador giratório (ícone). |
| Texto de apoio | "Aguarde a resposta. Nenhum valor é exibido até a consulta terminar." |
| Dados | **Nenhum valor.** Três linhas de esqueleto (barras cinza, `aria-hidden`) sob os rótulos Status / Versão / Data e hora da resposta. Não usar "—", "0" nem "desconhecido" (poderiam ser lidos como valor). |
| Erro/saudável | Nenhum indicador de erro nem de saudável. |
| Estilo | Fundo `--carga-bg`, texto `--carga-fg`, borda **tracejada** 2 px. |
| Botão | "Atualizar status" com `aria-disabled="true"` (visual desabilitado; não perde o foco; ativação ignorada). |
| Acessibilidade | Cartão com `aria-busy="true"`; região `aria-live="polite"` anuncia "Verificando status da API." Sem animação se `prefers-reduced-motion` (ícone estático). |
| Limite | Passados 5 s sem resposta → Erro (P-UX-05). Sem barra de progresso nem contagem. |

### 7.2 Estado SAUDÁVEL (CA-01, CA-02)
| Item | Especificação |
|---|---|
| Quando | Resposta HTTP 200, JSON válido com exatamente os campos esperados (`status`, `version`, `timestamp`; campos extras são ignorados e **nunca exibidos**) e `status === "ok"`. |
| Título (H2) | Ícone ✓ + "API operacional" + selo textual "Saudável". |
| Texto de apoio | "A API respondeu normalmente à última consulta." |
| Dados (lista de definição) | **Status (valor retornado)**: `ok` · **Versão**: valor recebido (ex.: `0.1.0`; exibido sem prefixo "v") · **Data e hora da resposta**: `26/11/2026 12:34:56` + "horário de Brasília (UTC−03:00)" + "UTC: `2026-11-26T15:34:56.789Z`". Valores em fonte monoespaçada, idênticos ao retorno da mesma consulta (CA-01). |
| Estilo | Fundo `--ok-bg`, texto `--ok-fg`, borda **sólida** 2 px `--ok-borda`. |
| Acessibilidade | `aria-busy="false"`; região polite anuncia "API operacional. Versão 0.1.0." Lista `<dl>` semântica. |
| Segurança | Valores inseridos **somente como texto** (nunca HTML). Só os três campos aparecem (RN-0001). |

### 7.3 Estado ERRO / INDISPONÍVEL (CA-03, CA-05; RN-0002)
| Item | Especificação |
|---|---|
| Quando | Qualquer resposta que não seja saudável válida: sem resposta (rede/CORS), tempo esgotado, HTTP ≠ 200 (inclui 503), corpo ausente/ não JSON/ fora do esquema, `status` ≠ `"ok"`, `version` ou `timestamp` ausentes/mal formados. |
| Título (H2) | Ícone ⚠ (triângulo) + "Status indisponível" + selo textual "Erro". |
| Mensagem | "Não foi possível obter o status da API. Até que uma nova consulta seja concluída com sucesso, não considere a API operacional." |
| Dica | "Use “Atualizar status” para tentar novamente." |
| Dados | **Nenhum** (sem versão, sem timestamp, sem "último valor conhecido"). Nenhum código HTTP, URL, host, exceção ou stack. Sem tela em branco. |
| Estilo | Fundo `--erro-bg`, texto `--erro-fg`, borda sólida 2 px + **barra lateral de 8 px** (reforço não cromático). |
| Acessibilidade | Anúncio **assertivo** (`role="alert"`): "Status indisponível. Não foi possível obter o status da API." O foco **não** é movido (permanece no botão, se foi ele a causa). |
| Recuperação | "Atualizar status" → Carregando → (API ok) Saudável (CA-05). Recarregar a página tem o mesmo efeito. |

### 7.4 Botão "Atualizar status" (CA-05) — comum aos três estados
Rótulo "Atualizar status" (ícone decorativo `aria-hidden`); altura mínima 44 px; largura mínima 160 px (100 % no móvel); `<button type="button">`; foco visível anel 3 px `--cor-foco` com afastamento de 3 px; ativação por clique, Enter e Espaço; durante o carregamento `aria-disabled="true"` (não usar `disabled`, para não perder o foco). O rótulo **não muda** entre estados (nome acessível estável).

### 7.5 Comportamento comum (para o FS — TASK-0008)
1. `fetch` com tempo limite de 5 s (premissa), sem cache (`no-store`), sem polling.
2. Validar: HTTP 200 **e** objeto com `status === "ok"`, `version` não vazia (SemVer, ADR-0002) e `timestamp` ISO 8601 UTC válido. Falhou → Erro (D-UX-06). Nunca assumir "saudável" por padrão.
3. Ao iniciar nova consulta: limpar e ocultar valores anteriores (D-UX-02) antes de mostrar Carregando.
4. Inserir dados via `textContent`; mensagens de erro são **constantes do front**, nunca derivadas da resposta.
5. Não registrar no console/UI conteúdo da resposta de erro; sem dados pessoais ou segredos em qualquer estado (RN-0001).
6. Estado inicial ao carregar a página = Carregando (nunca Saudável nem Erro "de partida").

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
| 320 px / zoom 200–400 % | Sem rolagem horizontal (reflow, WCAG 1.4.10); nenhuma informação oculta. |
| Orientação | Retrato e paisagem. |
Verificado no protótipo em 1100 px e 390 px (capturas de tela em ambiente local; não versionadas). **Mobile app (Java) fora de escopo.**

## 10. Acessibilidade — WCAG 2.1 AA (checklist)
Legenda: **P** = atendido no protótipo (verificado); **V** = a verificar na implementação (TASK-0008) e pelo QA.

| Critério | Requisito aplicado | Situação |
|---|---|---|
| 1.1.1 Conteúdo não textual | Ícones decorativos `aria-hidden`; o significado está no texto | P |
| 1.3.1 Informação e relações | `<main>`, `h1`/`h2`, `<dl>` para rótulo/valor, `<section>` rotulada | P |
| 1.3.2 Sequência significativa | Ordem do DOM = ordem visual | P |
| 1.4.1 Uso de cor | Ícone + título + selo textual + estilo de borda por estado (D-UX-04) | P |
| 1.4.3 Contraste (texto) | Ver tabela abaixo (todos ≥ 7:1, supera 4,5:1) | P (valores calculados) / V na implementação |
| 1.4.4 Redimensionar texto / 1.4.10 Reflow | Unidades relativas (rem), layout fluido, 320 px sem rolagem horizontal | P / V |
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
| 4.1.3 Mensagens de status | Mudanças anunciadas sem mover o foco: `aria-live="polite"` (carregando/saudável) e `role="alert"` (erro) | P (testado por script no navegador; leitor de tela real = V) |
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

## 11. Matriz de rastreabilidade: estado ↔ CA da US-0002 ↔ RN/REQ
| CA (US-0002) | Estado(s) | Elemento / regra de interface (seção) | RN / REQ | Verificação sugerida (QA, TASK-0005/0010) |
|---|---|---|---|---|
| **CA-01** Exibe os dados da API | Saudável | Lista de dados: status bruto, versão, timestamp (7.2; D-UX-05, D-UX-08) | REQ-0002 | Comparar valores exibidos com a resposta de `GET /health` da mesma consulta; conferir conversão UTC → Brasília |
| **CA-02** Saudável legível | Saudável | Ícone ✓ + "API operacional" + selo "Saudável" + borda sólida (7.2; D-UX-04) | REQ-0002 | Inspeção visual em escala de cinza/sem cor; leitor de tela |
| **CA-03** Erro com API indisponível | Erro | Título "Status indisponível", mensagem genérica, sem valores antigos, sem tela em branco (7.3; D-UX-02/03/06) | REQ-0003, **RN-0002**, RN-0001 | API simulada: sem resposta, 5 s, 500, 503, corpo inválido, `status` ≠ `ok` → mesmo estado Erro; DOM sem valores anteriores |
| **CA-04** Carregamento | Carregando | Título "Verificando status da API…", esqueleto sem valores, `aria-busy` (7.1) | REQ-0002 | API simulada lenta: nenhum valor nem erro antes da resposta |
| **CA-05** Recuperação | Erro → Carregando → Saudável | Botão "Atualizar status" e recarga da página (7.4, seção 6) | REQ-0003, RN-0002 | Derrubar e restaurar API; atualizar; ver Saudável com dados atuais |
| **CA-06** Sem dados sensíveis | Todos | Somente status, versão, timestamp e mensagens fixas; `textContent`; sem detalhes de erro (7.5; D-UX-06) | REQ-0004, **RN-0001** | Inspecionar DOM/rede/console nos três estados: sem dados pessoais, credenciais, hosts, caminhos, stack |
| RN-0002 (transversal) | Todos | Lista de permissão `status === "ok"`; estado inicial = Carregando; valores limpos ao atualizar (7.5) | RN-0002 | Teste de caminhos que antes resultariam em "saudável" por engano |

## 12. Recomendações ao PO (não ampliam o escopo; decisão do PO)
| ID | Recomendação | Benefício / custo |
|---|---|---|
| RE-01 | **Estado/variante "sem conexão do dispositivo"** (`navigator.onLine === false`): mesma tela de erro com a dica "Verifique a conexão deste dispositivo com a rede…". Já demonstrada no protótipo (seletor de causa). | Orienta o operador a distinguir problema local de API fora; custo baixo (1 frase condicional). |
| RE-02 | **Resposta inválida** já é tratada como Erro (CA-03). Recomenda-se o PO confirmar que **503 com `status: "unavailable"`** também seja Erro **sem** mostrar versão/timestamp (D-UX-03). | Evita exibir dados de resposta não saudável. |
| RE-03 | Exibir "Última tentativa em HH:MM:SS" (horário local da consulta) no estado Erro. Não implementado: acrescenta dado fora de CA-06. | Ajuda a saber se a tela está desatualizada; exigiria ajuste do CA-06. |
| RE-04 | Atualização automática (polling, ex.: a cada 30 s) como demanda futura. | Hoje é só manual (P-UX-07). |
| RE-05 | Título da aba refletindo o estado (ex.: "(Erro) Status da API"). Não implementado. | Útil a operadores com a aba aberta; depende de ARQ/FS. |

## 13. Impactos e riscos
| Componente | Impacto / risco |
|---|---|
| Portal Web | Define a primeira tela e os tokens iniciais do design system. Risco: baixo retrabalho se ADRs mudarem (apenas rótulos/limite de tempo). |
| Backend/APIs | Nenhum campo adicional exigido além de `status`, `version`, `timestamp` (ADR-0003). CORS para a origem do Portal é necessário (ARQ/AS). |
| Mobile, microsserviços, integrações, dados, infraestrutura | Sem impacto. |
| Acessibilidade | Risco médio de regressão se o FS não seguir 7.5 e a seção 10 (verificar com QA). |
| Segurança/LGPD | Risco baixo: tela só exibe os três campos como texto; exposição pública reabriria a análise da versão (L-UX-05). |

## 14. Próximos passos
1. **PO:** validar protótipo e spec (aprovação pendente); decidir RE-01..RE-05; confirmar P-UX-01 com a CPO.
2. **ORQ:** registrar o ponteiro em `contexto.yaml` (`prototipos`) — apenas o ORQ grava estado/ponteiros.
3. **FS (TASK-0008):** implementar conforme seções 7–10, após G1/G2/G3 e **somente com a versão aprovada pelo PO**; alinhar viabilidade com o UX antes de fechar (HTML/CSS/JS estático, ADR-0001 proposto).
4. **QA (TASK-0005/0010):** usar a matriz (seção 11) e o checklist (seção 10) para critérios visuais e de usabilidade.
5. **ARQ/AS:** informar mudanças de `status`/formatos/tempo limite (L-UX-03/04) para revisão desta spec.

## 15. Histórico de versões
| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 12:25 (America/Sao_Paulo) | UX | Primeira versão para validação do PO (TASK-0004) |
