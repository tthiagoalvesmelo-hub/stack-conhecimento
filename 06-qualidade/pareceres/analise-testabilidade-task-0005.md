---
id: ANALISE-TESTABILIDADE-DEM-2026-001-TASK-0005
titulo: "Análise de testabilidade dos CA, RN e REQ — DEM-2026-001 [TESTE] · TASK-0005"
tipo: analise
versao: 1.0
status: vigente
dono: QA
autores: [QA]
aprovado_por: QA
criado_em: 2026-11-26T12:26-03:00
atualizado_em: 2026-11-26T12:26-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0005, TASK-0002, TASK-0003, TASK-0010, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-ARQ-0001, ADR-0001, ADR-0002, ADR-0003, DEC-PO-0001, DEC-PO-0002, DEC-PO-0003, AH-0001]
substitui: null
substituido_por: null
---

# Análise de testabilidade — DEM-2026-001 [TESTE] · TASK-0005

> Parecer de **testabilidade** (condição para o G1). Não é plano de testes (PT), não é caso de teste (CT) e não é parecer de qualidade (PQ): esses artefatos pertencem à TASK-0010 / G5. Este documento **não** altera estado, etapa, gates nem aprovações (só o ORQ). A alteração de CA/REQ/RN é do PO; as redações abaixo são sugestões.

## 1. Escopo e premissas

- **Demanda:** DEM-2026-001 [TESTE] — endpoint `GET /health` (status, versão, timestamp) na API base do Portal Web + tela simples de status. Projeto do zero; ambiente de teste; nada vai à produção.
- **Atividade:** TASK-0005 (A4a) — revisar a testabilidade dos 12 CA (US-0001 e US-0002, 6 cada), RN-0001, RN-0002 e REQ-0001..REQ-0004.
- **Classe de risco aplicada:** **R3**, confirmada pelo ARQ em DEC-ARQ-0001 (26/11/2026 12:22, America/Sao_Paulo). A MSG-SOL desta TASK informava R2 a confirmar; a confirmação posterior reclassificou para cima (primeiro serviço + stack base). A matriz de proporcionalidade da seção 6 do PROMPT do QA é aplicada a R3 neste parecer.
- **Artefatos de formato:** ADR-0001, ADR-0002 e ADR-0003 existem na memória oficial, **v1.0, status proposto** (commit `362ea35`). Não estão aceitos. A stack (ADR-0001) aguarda AH-0001. **Nenhum formato foi inventado pelo QA:** valores, nomes de campo, tolerâncias e listas de dados proibidos abaixo são citados apenas como diretrizes propostas, a formalizar na ET/OpenAPI (TASK-0006) e a vigorar após aceitação dos ADR / G3.
- **Fora desta atividade:** elaboração de PT/CT, execução de testes e emissão de PQ (TASK-0010).

## 2. Critério do resultado (pré-G1)

Distinto dos critérios do PQ-nnnn (G5).

| Resultado | Critério |
|---|---|
| **Favorável ao G1** | 100% dos CA, RN e REQ classificados como Testável, com oráculo verificável no texto vigente ou por remissão explícita a ET/ADR, e sem conflito de comportamento entre os artefatos de escopo. |
| **Favorável com ressalvas ao G1** | Todos os itens são testáveis no mérito (comportamento observável), porém há ajustes de redação ou alinhamento com diretrizes técnicas propostas que o PO deve incorporar ou responder formalmente antes ou no G1. Lacunas de formalização (ADR proposto, ET/OpenAPI ausentes, protótipo UX ainda não apontado no contexto) ficam rastreadas. |
| **Desfavorável ao G1** | Um ou mais CA/RN/REQ sem oráculo possível, ou conflito de comportamento no escopo que impede planejar a verificação. |

**Resultado desta análise: favorável com ressalvas ao G1.**

## 3. Resumo da classificação

| Conjunto | Testável | Ajuste sugerido | Total |
|---|---:|---:|---:|
| CA da US-0001 | 4 | 2 | 6 |
| CA da US-0002 | 4 | 2 | 6 |
| RN | 2 | 0 | 2 |
| REQ | 3 | 1 | 4 |
| **Total** | **13** | **5** | **18** |

Itens com ajuste sugerido: US-0001 CA-04 e CA-06; US-0002 CA-03 e CA-04; REQ-0001.

## 4. Estratégia proporcional (R3) — visão de alto nível

Não substitui o plano de testes da TASK-0010. Matriz da seção 6 do PROMPT do QA, classe **R3**, reforçada por DEC-ARQ-0001 (“testes de todos os tipos aplicáveis + segurança e desempenho”):

| Tipo | Exigência R3 | Aplicação prevista nesta demanda |
|---|---|---|
| Unitários | Obrigatório | Regras de montagem da resposta, validação da versão no bootstrap (ADR-0002 proposto), relógio injetável (ADR-0003 proposto). Responsável: desenvolvedor; QA verifica. |
| Integração | Obrigatório | Portal ↔ API (`GET /health`); CORS e tempo limite do cliente, quando formalizados na ET. |
| Funcionais | Obrigatório | Tela de status (US-0002): saudável, carregando, erro e recuperação. |
| Regressão | Obrigatória e **completa** | Suíte do serviço e fluxos afetados; como é o primeiro serviço, a suíte inicial é a própria entrega. |
| Contrato | Obrigatório | Provedor (`200` e, se permanecer no contrato, `503`/`405`) e consumidor (Portal com mocks, inclusive corpo inválido, tempo esgotado e `5xx`) — diretrizes do ADR-0003 proposto. |
| Segurança | Varredura + **testes dirigidos** | RN-0001 / REQ-0004 / CA de dados sensíveis: inspeção de corpo, cabeçalhos e tela; denylist proposta no ADR-0003; varredura na pipeline quando existir. |
| Desempenho | Obrigatório se caminho crítico | DEC-ARQ-0001 determina desempenho nesta demanda. Alvo **indicativo** do ADR-0003 proposto: p95 ≤ 100 ms em execução local, a calibrar com OPS/QA; **não é SLO**. Incluir na TASK-0010, sem tratar como linha de base formal até o AS/OPS fecharem o número. |
| Aceitação | Obrigatório | Rastreio CA → CT na TASK-0010; pré-aceite do PO no G6. |

Ambiente previsto (premissa de teste, ainda a confirmar pelo OPS): execução local em `/workspace/projetos/`. Sem dev/hml, sem pipeline e sem produção.

## 5. Classificação detalhada — US-0001 (v1.0, em-revisao)

A US já declara que nomes de campos, valores de status e formatos de versão/timestamp vêm da ET/ADR vigente. Essa remissão é adequada e foi preservada.

### CA-01 — Resposta com os três campos — **Testável**

- **Justificativa:** HTTP 200, presença dos três campos e “não vazios” são objetivos e mensuráveis assim que o contrato formalizar nomes e esquema. O ADR-0003 proposto fecha o oráculo: `Content-Type: application/json; charset=utf-8`; objeto com exatamente `status`, `version` e `timestamp`; `additionalProperties: false`. Dados e ambiente: API em execução (premissa local).
- **Lacuna (não é ajuste de CA):** ET/OpenAPI ainda não existem; ADR-0003 não está aceito.
- **Técnicas previstas (alto nível):** teste de contrato/esquema; particionamento presença/ausência de campo; verificação de código HTTP.
- **Redação sugerida:** nenhuma obrigatória. Opcional, quando o PO promover a US: citar os nomes em inglês e “não nulos nem strings vazias”, alinhados à ET.

### CA-02 — Status saudável — **Testável**

- **Justificativa:** o oráculo é o valor permitido na ET. O ADR-0003 proposto define enum e `200` ⇒ `"ok"`; “execução normal” coincide com a diretriz de *liveness* do processo (sem checagem de dependências, já fora do escopo da US).
- **Lacuna:** formalizar o enum na ET; o caminho `503` / `"unavailable"` **não** está neste CA (ver REQ-0001 e US-0002 CA-03).
- **Técnicas previstas:** contrato (valor no enum); funcional de API no caminho saudável.

### CA-03 — Timestamp — **Testável**

- **Justificativa:** formato e tolerância já estão remetidos à ET; o critério de correspondência ao instante de geração é mensurável. O ADR-0003 proposto sugere ISO 8601 / RFC 3339 em UTC com `Z` e milissegundos e tolerância de ± 5 s (a confirmar pelo AS), com relógio injetável nos testes.
- **Lacuna:** AS deve fechar o valor da tolerância na ET; ADR ainda proposto.
- **Técnicas previstas:** contrato (formato); valor-limite da tolerância (± 5 s e imediatamente fora); comparação com relógio de referência/injetado.

### CA-04 — Versão rastreável — **Ajuste sugerido**

- **Justificativa:** a exigência de comparação é correta e testável, mas o texto vigente cita “versão registrada daquela execução **(build/commit)**”. O ADR-0002 proposto rejeita hash de commit na resposta e define oráculo tríplice: `version` da resposta == `version` do `package.json` do commit testado == tag Git (`portal-api-v<versão>` ou `-rc.N` no candidato). Sem ajuste, o executante pode procurar um commit hash que o próprio ADR proíbe (e que RN-0001/REQ-0004 tratam como detalhe interno).
- **Lacuna:** ADR-0002 depende da aceitação do ADR-0001 (AH-0001); a origem no `package.json` só vale se a stack for confirmada.
- **Técnicas previstas:** contrato (SemVer); comparação das três fontes; unitário de bootstrap com manifesto inválido (serviço não inicia — diretriz ADR-0002, a virar CA/ET se o PO/AS adotarem).
- **Redação sugerida (não altera o original):** *Dado* uma instância da API em execução a partir de um commit/artefato conhecido, *quando* um cliente faz `GET /health`, *então* o campo de versão está no formato definido na ET/ADR vigente e é idêntico à fonte de verdade daquela execução (conforme ADR-0002: valor do manifesto do serviço e, quando houver, a tag de release correspondente), de modo que o QA compare os valores sem ambiguidade e sem exigir hash de commit na resposta.

### CA-05 — Sem dados sensíveis — **Testável**

- **Justificativa:** o oráculo lista categorias concretas (dados pessoais, credenciais, segredos, tokens, detalhes internos) e o escopo de inspeção (corpo e cabeçalhos). O ADR-0003 proposto acrescenta denylist utilizável nos testes dirigidos de segurança (hostnames, IPs, caminhos, versões de runtime/dependências, hash de commit, variáveis de ambiente, estado de dependências; cabeçalhos sem fingerprint de servidor/framework). A pendência de sensibilidade da versão foi respondida pelo ARQ para exposição **interna** (não sensível); reavaliar se a exposição mudar.
- **Técnicas previstas:** inspeção de payload e cabeçalhos; checklist/denylist; testes dirigidos de segurança (R3); varredura quando houver pipeline.
- **Redação sugerida:** nenhuma. Recomenda-se que a ET incorpore a denylist e os cabeçalhos do ADR-0003 proposto.

### CA-06 — Somente leitura — **Ajuste sugerido**

- **Justificativa:** a ausência de efeitos colaterais é o comportamento certo, mas “nenhum dado nem estado do sistema foi alterado” é oráculo amplo demais. Logs de acesso (previstos em nível `debug` no ADR-0003 proposto) e o próprio avanço do timestamp são observáveis e não devem reprovar o CA. Não há persistência (L9 confirmada pelo ARQ). “Repetidas vezes” não define quantidade mínima. O ADR-0003 proposto também prevê `405` + `Allow: GET` para outros métodos — comportamento testável que hoje não tem CA.
- **Técnicas previstas:** repetição/idempotência dos campos `status` e `version`; verificação de ausência de persistência; (se o PO incorporar) contrato para métodos não permitidos.
- **Redação sugerida:** *Dado* que `GET /health` é chamado duas ou mais vezes sobre a mesma instância, *quando* as chamadas terminam, *então* não há criação, alteração nem exclusão de dados persistidos nem de estado de negócio. Logs de auditoria/acesso são permitidos. Os campos de status e versão permanecem iguais; o timestamp pode variar. O recurso permanece somente leitura.

## 6. Classificação detalhada — US-0002 (v1.0, em-revisao)

### CA-01 — Exibe os dados da API — **Testável**

- **Justificativa:** “valores iguais aos retornados por `GET /health` na mesma consulta” é objetivo, desde que a verificação intercepte **a mesma** requisição (uma segunda chamada pode mudar o timestamp). O risco de colisão com a formatação (servidor em UTC, tela em America/Sao_Paulo — ADR-0003 proposto) fica coberto pela especificação de interface UX v1.0 (commit `1290f25`, validação do PO pendente): D-UX-05 e D-UX-08 exibem o valor bruto de `status`, a versão recebida e a linha “UTC: <ISO bruto>” além da data formatada em horário de Brasília. Assim o oráculo de igualdade é observável sem exigir que a string formatada seja idêntica à da API.
- **Lacuna:** protótipo e spec v1.0 em revisão, ainda sem validação do PO. Se o PO rejeitar a exibição dos valores brutos, este CA volta a precisar de ajuste (equivalência semântica em vez de igualdade de string).
- **Técnicas previstas:** funcional de UI com interceptação da mesma consulta; comparação dos valores brutos exibidos com o corpo da resposta.
- **Redação sugerida:** nenhuma, condicionada à validação de D-UX-05/D-UX-08 pelo PO.

### CA-02 — Estado saudável legível — **Testável**

- **Justificativa:** “explícita e distinguível” e “não depender apenas de cor” são critérios objetivos. A spec UX v1.0 (D-UX-04) já propõe oráculo de *copy* e indicadores: ícone distinto, título “API operacional”, selo textual “Saudável” e borda — nenhum deles só por cor. Pendente apenas a validação do PO.
- **Técnicas previstas:** funcional de UI; verificação de acessibilidade (informação não só por cor; inspeção em escala de cinza).
- **Redação sugerida:** nenhuma obrigatória. Opcional, após validação: remeter o oráculo de textos ao protótipo/spec validados.

### CA-03 — Estado de erro com API indisponível — **Ajuste sugerido**

- **Justificativa:** as quatro famílias (sem resposta, tempo esgotado, erro HTTP, conteúdo inválido), a proibição de reapresentar valores anteriores como atuais, a vedação de tela em branco e de mensagem técnica interna são testáveis e alinhadas a RN-0002. Faltam dois fechamentos de oráculo no texto do CA: (1) **“conteúdo inválido”** ainda não aponta ao esquema do contrato (campos ausentes, tipos errados, corpo ilegível, `status` fora do enum); (2) o ADR-0003 proposto prevê **HTTP 503 com corpo válido** e `status: "unavailable"` — isso é resposta de contrato, e a frase vigente “o status não pôde ser obtido” não descreve bem esse caso. A spec UX v1.0 (D-UX-03, D-UX-06; RE-02) recomenda um único estado de erro genérico, **sem** exibir versão/timestamp mesmo no 503, e pede decisão explícita do PO. Tempo limite: orientação de 5 s no ADR-0003, a fechar na ET (não inventado aqui).
- **Técnicas previstas:** funcional negativa com mocks/falha injetada nas quatro famílias e no 503 válido, se permanecer no contrato; inspeção de ausência de valores obsoletos e de detalhes internos.
- **Redação sugerida:** *Dado* que ocorre uma destas situações — (a) a API não responde, o tempo de espera definido na ET se esgota, há erro HTTP inesperado ou o corpo está fora do esquema do contrato; ou (b) a API devolve resposta válida de indisponibilidade (HTTP 503 / `status` `"unavailable"`, se o contrato vigente prever esse valor) —, *quando* o usuário abre ou atualiza a tela, *então* ela exibe um estado de erro ou indisponível explícito, nunca “saudável”, não apresenta valores anteriores como se fossem atuais, não apresenta tela em branco nem mensagem técnica interna (RN-0002, RN-0001). No caso (a), informa que o status não pôde ser obtido. No caso (b), o PO decide, na validação do protótipo (RE-02 / D-UX-03), se a tela oculta versão e timestamp (recomendação do UX) ou se comunica a indisponibilidade exibindo os campos recebidos; a decisão fica escrita no CA para servir de oráculo.

### CA-04 — Estado de carregamento — **Ajuste sugerido**

- **Justificativa:** indicar carregamento e não mostrar valores nem erro antes da resposta é testável. O texto do CA não explicita o que acontece na **atualização/recarga**. A spec UX v1.0 (D-UX-02) já propõe a regra que fecha o oráculo: toda atualização passa por “Carregando” e **remove os valores anteriores do DOM** (não apenas os oculta), alinhada a RN-0002. Recomenda-se promover essa regra ao CA, para o aceite não ficar só na spec de interface (ainda pendente de validação do PO). O estado pode ser transitório demais para observação sem atraso controlado (técnica da TASK-0010; não exige número no CA).
- **Técnicas previstas:** funcional de UI com atraso controlado/mock lento; verificação na primeira carga e na atualização (DOM sem valores anteriores).
- **Redação sugerida:** *Dado* que a consulta a `GET /health` está em andamento (primeira abertura ou atualização), *quando* a tela é exibida, *então* ela indica que o status está sendo carregado, passa por esse estado antes de exibir sucesso ou erro, e não mostra valores anteriores ou parciais como se fossem o status atual (os valores da consulta anterior são removidos, não apenas ocultados).

### CA-05 — Recuperação — **Testável**

- **Justificativa:** precondição (tela em erro), ação do usuário (recarga ou ação definida pelo UX) e resultado (volta a CA-01/CA-02) são claros. Não exige polling automático (fora de escopo no ADR-0003 proposto). Se a API “voltar” com resposta inválida ou `503`, aplicam-se CA-03/RN-0002 — compatível.
- **Técnicas previstas:** funcional de transição de estado (erro → sucesso) com mock que passa a responder.
- **Redação sugerida:** nenhuma.

### CA-06 — Sem dados sensíveis — **Testável**

- **Justificativa:** cobre os três estados da tela e restringe o conteúdo a status, versão, timestamp e mensagens genéricas, com a mesma denylist de RN-0001/REQ-0004. O ADR-0003 proposto reforça o oráculo: inserir no DOM somente como texto (nunca HTML) e apenas os três campos.
- **Técnicas previstas:** inspeção da UI nos três estados; testes dirigidos de segurança (incluindo inserção como texto, não HTML).
- **Redação sugerida:** nenhuma.

## 7. Regras de negócio e requisitos

### RN-0001 (v1.0, em-revisao) — **Testável**

Aplicável via US-0001 CA-05 e US-0002 CA-06. A lista de proibições é concreta. Pendência de sensibilidade da versão: o ARQ respondeu, para exposição interna, que não é sensível (ADR-0002 proposto); a condição de reavaliação permanece se a exposição mudar. Sem ajuste de redação obrigatório; a ET deve incorporar a denylist do ADR-0003 proposto.

### RN-0002 (v1.0, em-revisao) — **Testável**

Aplicável via US-0002 CA-03 e CA-05 (e, na carga inicial, coerente com CA-04). “Nunca assume saudável por padrão” e “nunca apresenta status anterior como atual” são oráculos claros. O alinhamento fino entre “resposta de erro” e o `503` de contrato fica no ajuste sugerido da US-0002 CA-03; a regra em si não precisa mudar para o G1.

### REQ-0001 (v1.0, em-revisao) — **Ajuste sugerido**

O requisito vigente afirma que `GET /health` “responde com HTTP 200 e informa status, versão e timestamp”. Isso cobre o caminho feliz (US-0001 CA-01 a CA-04 e CA-06) e é testável. Porém o ADR-0003 proposto introduz HTTP `503` com o mesmo esquema e `status: "unavailable"` (processo em encerramento; reserva para dependência futura). Há **desalinhamento de comportamento** entre o requisito de escopo (só 200) e a diretriz técnica proposta. Sem decisão do PO, o G5 não terá CA para um caminho que o contrato poderá exigir.

- **Redação sugerida (alternativa A — recomendada se o PO aceitar a diretriz do ARQ):** além do `200` com status saudável, o recurso pode responder HTTP `503` com o mesmo esquema e status de indisponibilidade, sem detalhes de causa; este caminho terá CA próprio ou extensão da US-0001, e a tela o trata conforme US-0002 CA-03.
- **Alternativa B:** declarar explicitamente, no requisito, que `503`/`unavailable` fica fora do aceite desta demanda; o contrato não o incluirá até nova US.

### REQ-0002 (v1.0, em-revisao) — **Testável**

Comportamento observável (tela consulta `GET /health` e exibe os três dados). Público da tela permanece premissa DEC-PO-0002 (lacuna CPO). Layout e acesso são de outros donos. O ajuste de igualdade vs. formatação está no CA-01 da US-0002, não neste requisito.

### REQ-0003 (v1.0, em-revisao) — **Testável**

Cobre falha de obtenção e a recuperação ao atualizar. “Sem quebrar” é detalhado de forma testável no CA-03 (sem tela em branco). Tempo limite e política de nova tentativa continuam com AS/ARQ. Alinhar o detalhe do `503` no CA, não é obrigatório reescrever o requisito.

### REQ-0004 (v1.0, em-revisao) — **Testável**

NFR verificável por inspeção da resposta e da tela, em sucesso e em erro. Rastreio correto (US-0001 CA-05, US-0002 CA-06, RN-0001). Requisitos adicionais de exposição/autenticação/limitação de taxa permanecem com o ARQ (diretriz proposta: contrato interno, sem autenticação, condição de reabertura se a exposição mudar).

## 8. Lacunas e dependências rastreadas (sem inventar formatos)

| # | Lacuna | Dono | Efeito na testabilidade |
|---|---|---|---|
| G-QA-01 | Pacote `/workspace/stack-memoria/pacotes-contexto/DEM-2026-001/TASK-0005.md` inexistente no momento da análise. Contexto recomposto pelos artefatos da demanda + ADRs commitados. | ORQ | Não crítica (fontes oficiais lidas). |
| G-QA-02 | ADR-0001/0002/0003 v1.0 **propostos**, não aceitos; stack aguarda AH-0001. Origem da versão no `package.json` depende da stack. | ARQ / ORQ (AH) | Oráculos de formato existem como diretriz, não como padrão vigente. Revalidar esta análise se os ADR mudarem na aceitação. |
| G-QA-03 | ET, EF e OpenAPI ainda não existem (TASK-0006 em andamento; G3 só após AH-0001). Tolerância do timestamp (± 5 s) e tempo limite do cliente (orientação de 5 s) ainda “a confirmar/fechar pelo AS”. | AS | Casos da TASK-0010 só fecham após a ET. |
| G-QA-04 | Protótipo HTML e especificação de interface UX v1.0 (commit `1290f25`) apontados no contexto.yaml v5; **validação do PO pendente**, inclusive RE-01..RE-05 (503 sem versão/timestamp). | UX (entregue) / PO (validar) | Oráculos de *copy*, formatação e recarga existem como proposta; não estão vigentes até a validação. |
| G-QA-05 | Público da tela (L2) e visão de produto (L1) pendentes da CPO; premissa DEC-PO-0002 vigente para o teste. | CPO | Não impede testar o comportamento; pode afetar acesso/ambiente depois. |
| G-QA-06 | Ambientes dev/hml inexistentes; execução local a confirmar pelo OPS. | OPS | Ambiente dos testes da TASK-0010 ainda é premissa. |
| G-QA-07 | Desalinhamento REQ-0001 / US-0001 (só HTTP 200) × ADR-0003 proposto (também 503/`unavailable`). | PO (escopo) + ARQ (contrato) | Principal ressalva ao G1. |

Não há bloqueio que impeça concluir a TASK-0005: os ajustes são do PO e as formalizações técnicas seguem o fluxo já registrado.

## 9. Resultado e recomendação

**Resultado: favorável com ressalvas ao G1.**

Os 18 itens têm comportamento observável; nenhum CA é inverificável no mérito. As ressalvas são: (1) alinhar REQ-0001 e a US-0001 ao caminho `503` proposto ou declará-lo fora do aceite, e decidir no CA-03 da US-0002 (RE-02) se o 503 oculta versão/timestamp; (2) corrigir a redação de US-0001 CA-04 (“build/commit”) para o oráculo SemVer/manifesto/tag; (3) fechar oráculos de US-0001 CA-06 (estado observável) e US-0002 CA-04 (recarga remove valores anteriores — já proposto em D-UX-02). O CA-01 da US-0002 permanece testável se o PO validar a exibição dos valores brutos (D-UX-05/D-UX-08). As lacunas de ADR/ET/validação do protótipo/ambiente estão rastreadas e não foram preenchidas com formatos inventados.

Recomenda-se que o PO incorpore ou responda formalmente os seis ajustes (MSG-COL anexa) antes ou no G1, e que o ORQ atualize os ponteiros da demanda após este parecer. A TASK-0010 (PT, CT, execução e PQ) permanece no momento previsto, após implementação e G4, com estratégia R3.

## 10. Fontes consultadas

| Fonte | Versão / status | Caminho ou evidência |
|---|---|---|
| MSG-SOL TASK-0005 (ORQ) | — | Atividade e restrições (risco informado: R2 a confirmar) |
| contexto.yaml | v5 (atualizado_em 2026-11-26T12:30-03:00, ORQ) | `03-operacional/demandas/DEM-2026-001/contexto.yaml` |
| historico.md | entradas até 26/11/2026 12:30 | mesmo diretório (append-only) |
| analise-po-task-0002.md | v1.0, em-revisao | mesmo diretório |
| US-0001, US-0002 | v1.0, em-revisao | `historias/` |
| REQ-0001..REQ-0004 | v1.0, em-revisao | `requisitos/` |
| RN-0001, RN-0002 | v1.0, em-revisao | `01-institucional/regras-negocio/` |
| DEC-PO-0001, DEC-PO-0002, DEC-PO-0003 | registradas no histórico e na análise do PO | historico.md; analise-po-task-0002.md |
| DEC-ARQ-0001 (classe de risco R3) | registrada 26/11/2026 12:22 | historico.md; contexto.yaml v4 |
| ADR-0001, ADR-0002, ADR-0003 | v1.0, **proposto**, commit `362ea35` | `02-tecnica/adr/` |
| AH-0001 | Solicitada 26/11/2026 12:27 | contexto.yaml v4 |
| protocolo-memoria.md, convencao-ids.md, registro-ids.yaml | v1.0 / registro em 2026-11-26T12:17-03:00 | `00-memoria/` |
| PROMPT do QA, seções 6, 8 e 9 | — | `07-agentes/12-qa/PROMPT.md` |
| estado-operacional.md | v1.0, vigente, estado Normal | `00-memoria/governanca/` |
| modelos frontmatter, nota-analise, parecer-pq, msg-ret, msg-col | — | `modelos/` |
| Especificação de interface UX (UX-ESPEC-DEM-2026-001-TASK-0004) e protótipo HTML | v1.0, em-revisao, commit `1290f25`; validação do PO pendente | `07-agentes/06-ux/prototipos/DEM-2026-001-US-0002-tela-status/` |
| Pacote TASK-0005.md | **ausente** | `/workspace/stack-memoria/pacotes-contexto/DEM-2026-001/` |

A spec/protótipo UX foram usados apenas como proposta de oráculo de interface (ainda não validados pelo PO), sem alterar a classificação para além do que o texto dos CA já permite verificar.
