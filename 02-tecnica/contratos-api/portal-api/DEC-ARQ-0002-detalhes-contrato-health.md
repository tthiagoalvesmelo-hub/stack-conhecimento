---
id: DEC-ARQ-0002
titulo: "Detalhes do contrato interno GET /health (L-01 a L-07) — parecer prévio, não é G3"
tipo: dec
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T12:36-03:00
atualizado_em: 2026-11-26T12:36-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0006, TASK-0007, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0001, DEC-AS-0001, DEC-AS-0002, DEC-AS-0003, ET-0001, EF-0001, AH-0001, CONF-0001]
substitui: null
substituido_por: null
---

# DEC-ARQ-0002 — Detalhes do contrato interno `GET /health` (L-01 a L-07)

> [TESTE] Fase de testes internos; nada vai à produção. **Este documento NÃO é o G3** (TASK-0007, só após AH-0001). É o parecer prévio do ARQ às lacunas L-01 a L-07 da ET-0001 v1.1 §12 e à MSG-COL da AS (TASK-0006). Nenhuma decisão abaixo torna o contrato público, exige autenticação ou gera custo. O ADR-0003 permanece PROPOSTO e **não foi editado in-place** (já citado na AH-0001, na EF/ET e no OpenAPI); este DEC complementa os pontos que o ADR deixou em aberto. Quando o ADR-0003 for aceito, estas decisões entram como adendo (ou numa revisão explícita do ADR).

## Decisões

### L-01 — Erro padronizado (RFC 9457)
**Confirmo** a proposta da AS e a adoto como padrão inicial da plataforma (não é mais só "sugestão" do ADR-0003):
- `Content-Type: application/problem+json`
- corpo com **somente** `type`, `title`, `status` (`additionalProperties: false`)
- `type`: `"about:blank"` (padrão da RFC 9457 quando não há URI de tipo adicional)
- `title`: frase canônica do status HTTP em inglês (`Method Not Allowed`, `Internal Server Error`, `Not Found`)
- `status`: o código HTTP numérico, igual ao da linha de status
Sem `detail`, `instance` ou extensão nesta versão. Tipos URI próprios (ex.: `https://…/problems/…`) exigem DEC/ADR futuro. Não é N3 (contrato interno, sem mudança de autenticação).

### L-02 — HEAD, `Allow` do 405 e OPTIONS/preflight
- **HEAD:** tolerado com a semântica da ET-0001 §4.1: mesmo código HTTP e os mesmos cabeçalhos do `GET`, **sem corpo**. Não integra a superfície prometida do contrato 1.0.0 (sem operação `head` no OpenAPI; consumidores não dependem dele).
- **`Allow` do 405:** `GET, HEAD` (HEAD é método suportado; RFC 9110). O literal `Allow: GET` do ADR-0003 fica refinado por este DEC.
- **OPTIONS:** não é operação de negócio e **não** deve responder `405`. O provedor implementa preflight CORS: `204`, sem corpo, `Access-Control-Allow-Origin` só se a origem for a configurada, `Access-Control-Allow-Methods: GET, HEAD`, sem `Access-Control-Allow-Credentials`, sem `Access-Control-Allow-Headers` nesta demanda (ver L-03). O GET do Portal continua "simples" (sem preflight). OPTIONS existe para um preflight futuro não quebrar.

### L-03 — `X-Request-Id`
- **Formato restrito:** UUID canônico, 36 caracteres, hexadecimal minúsculo com hífens: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`. O servidor **gera UUID v4** quando o cabeçalho está ausente ou é inválido; **não** responde `400` em `/health`.
- **Portal:** confirmo a premissa da AS — o Portal **não envia nem lê** `X-Request-Id` nesta demanda. Sem `Access-Control-Allow-Headers` e sem `Access-Control-Expose-Headers` para esse cabeçalho (mantém o GET simples). O ID segue nos logs do servidor.

### L-04 — `Cache-Control: no-store` e `X-Content-Type-Options: nosniff`
**Sim:** valem para **todas** as respostas de `/health` (200, 503, 405, 500) e, como padrão do serviço `portal-api`, também para as demais respostas, inclusive `404` de rota inexistente. O `404` usa o mesmo problema RFC 9457 (`type: "about:blank"`, `title: Not Found`, `status: 404`). Não é caminho de sucesso de `/health`; o OpenAPI pode registrá-lo como comportamento padrão da API, não como resposta de `GET /health`.

### L-05 — 503, `Retry-After` e testabilidade
- **Sem `Retry-After`** nesta versão (o cliente não faz nova tentativa automática — DEC-AS-0001; não há SLO nem tempo de volta conhecido). Reavaliar quando houver readiness ou várias instâncias.
- **Encerramento gracioso:** enquanto o listener estiver no ar, o processo **deve** responder `503` com `status: "unavailable"` (mesmo formato do 200). Se a parada for abrupta, o cliente esgota o tempo e trata como indisponível (RN-0002). O gancho concreto depende da stack (AH-0001 / ADR-0001).
- **Teste do 503:** permitido **somente** por injeção na fábrica da aplicação (estado de saúde injetável, no mesmo espírito do relógio injetável) ou equivalente de teste unitário/integração. **Proibido** endpoint, query string, cabeçalho ou variável honrada em execução não-teste que force o 503 remotamente (controle remoto inseguro; seria N3 de segurança). Em builds/ambientes que não forem de teste, o gancho não existe ou é inerte.

### L-06 — CORS e origem do Portal
- **Não invento porta nem origem concreta.** A origem é a variável `PORTAL_API_ALLOWED_ORIGIN` (ADR-0001 D7): valor exato, **sem curinga**, obrigatória; se ausente, inválida ou igual a `*`, o serviço **não inicia** (falha fechada).
- **Premissa de teste:** o valor deve ser exatamente a origem do Portal em loopback, `http://127.0.0.1:${PORTAL_WEB_PORT}`. `PORTAL_WEB_PORT` e o valor correspondente de `PORTAL_API_ALLOWED_ORIGIN` são definidos por OPS/FS no ambiente (TASK-0012), não neste DEC.
- **Origem não permitida:** a resposta segue o status normal do recurso (200/503/405/500) **sem** `Access-Control-Allow-Origin` (e nunca `*`); **sem 403** no servidor. O navegador bloqueia a leitura. Confirmado.

### L-07 — DEC-AS-0001, 0002 e 0003
- **DEC-AS-0001** (timeout do cliente = 5 s, sem nova tentativa automática): **confirmado**.
- **DEC-AS-0002** (tolerância do `timestamp` = ±5 s; igualdade exata com relógio injetável): **confirmado**.
- **DEC-AS-0003:** o regex de `timestamp` está **confirmado** — é um perfil válido de RFC 3339/ISO 8601 (UTC, `Z`, exatamente 3 casas de milissegundo), alinhado ao ADR-0003. O regex de `version` (`(-[0-9A-Za-z.-]+)?` no pré-release) é o que o ADR-0002 sugeriu, porém é **mais permissivo** que o SemVer 2.0.0 oficial (aceita zeros à esquerda em identificadores numéricos, segmentos vazios e pontos consecutivos). **Ajuste:** usar a gramática oficial SemVer 2.0.0 **sem** metadados de build (`+…`), que o ADR-0002 proíbe:

```
^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(-((0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)(\.(0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*))?$
```

Exemplos `0.1.0` e `0.2.0-rc.1` continuam válidos. Não é mudança de semântica; é aperto de validação antes do G3.

## O que este DEC não faz
- Não aprova o contrato (G3 / TASK-0007). Não mescla o ramo `doc/ET-0001-contrato-portal-api-health`.
- Não altera exposição, autenticação nem custo. CONF-0001 (US/REQ ainda citam R2; a classe confirmada é R3) é do PO; apenas tomo nota.
