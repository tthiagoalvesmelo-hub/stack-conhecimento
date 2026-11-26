---
id: ADR-0003
titulo: "Padrão de health-check e diretrizes do contrato GET /health"
tipo: adr
versao: 1.0
status: proposto
dono: ARQ
autores: [ARQ]
aprovado_por: null
criado_em: 2026-11-26T12:20-03:00
atualizado_em: 2026-11-26T12:20-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0003, ADR-0001, ADR-0002, US-0001, US-0002, REQ-0001, REQ-0003, REQ-0004, RN-0001, RN-0002]
substitui: null
substituido_por: null
---

# ADR-0003 — Padrão de health-check e diretrizes do contrato `GET /health`

> [TESTE] **Status: PROPOSTO.** Estas são **diretrizes arquiteturais**, não o contrato. O detalhamento (EF/ET e OpenAPI) é do Analista de Sistemas (AS) e a **validação do contrato (G3) é do ARQ**. Não há decisão de stack aqui; os pontos que dependem da stack estão sinalizados.

## Contexto
- REQ-0001/US-0001: `GET /health` somente leitura, HTTP 200, com status, versão e timestamp. REQ-0004/RN-0001: nada sensível. RN-0002: indisponibilidade jamais aparece como saudável. US-0002: tela no Portal.
- Padrão da Stack: "nova rota já nasce com health check" e contratos versionados em `02-tecnica/contratos-api` aprovados antes da implementação (G3).
- Perguntas do PO ao ARQ respondidas aqui: exposição e autenticação (L4), acesso à tela (L5), desempenho e tempo limite (L6), persistência (L9), sensibilidade da versão (pendência de RN-0001).

## Decisão (proposta)
### Diretrizes de arquitetura
1. **Natureza:** `GET /health` é *liveness* do processo da `portal-api`. Não consulta dependências (não há nenhuma) nem persistência. *Readiness* (`/ready`) e verificação de dependências entram quando existir dependência, por ADR/nova versão menor do contrato.
2. **Exposição e autenticação:** contrato **interno** (consumidores: Portal e, futuramente, monitoramento). Sem autenticação em `/health` (sondas de monitoramento não carregam credenciais; a resposta é mínima). **Condição:** execução local/rede interna. Qualquer exposição fora da rede interna (Internet, clientes) torna o contrato **público** e muda para **R3 + N3** (contrato público e segurança: autenticação, limitação de taxa, reavaliação da versão exposta), com nova AH.
3. **Acesso à tela do Portal (L5):** sem login nesta demanda (o Portal base não tem autenticação). Exigir autenticação no Portal é demanda própria (autenticação/autorização = R3 sempre; N3).
4. **Persistência (L9):** nenhuma. Confirmado: sem banco, sem DBA nesta demanda.

### Diretrizes do contrato (para o AS detalhar em `02-tecnica/contratos-api/portal-api/`)
| Item | Diretriz |
|---|---|
| Rota/método | `GET /health`, sem parâmetros, sem corpo, sem efeitos colaterais (seguro e idempotente). Outros métodos: `405` com cabeçalho `Allow: GET` (e `HEAD` tolerado). Fora do prefixo de versão (endpoint operacional) |
| Resposta de sucesso | `200`, `Content-Type: application/json; charset=utf-8`, objeto com **exatamente** `status`, `version`, `timestamp` (`additionalProperties: false` no provedor; o Portal ignora campos desconhecidos — leitor tolerante). Nomes em minúsculas, ASCII, em inglês (padrão de identificadores de API) |
| `status` | enum. `200` ⇒ `"ok"`. `"unavailable"` reservado para o `503` (processo em encerramento ou, no futuro, dependência crítica fora). Valores adicionais = versão menor do contrato |
| `version` | SemVer do serviço, origem e regras no ADR-0002; nunca vazio |
| `timestamp` | ISO 8601 / RFC 3339 em **UTC com `Z` e milissegundos** (`AAAA-MM-DDThh:mm:ss.sssZ`), gerado no momento da resposta pelo relógio do servidor (relógio injetável nos testes). Tolerância de verificação do QA (CA-03): ± 5 s, a confirmar pelo AS na ET. O Portal converte para America/Sao_Paulo apenas para exibição |
| `503` | Mesmo formato do `200` com `status: "unavailable"`; sem causa, sem detalhe. Sem resposta, tempo esgotado, outro código ou corpo fora do esquema ⇒ o Portal mostra **erro/indisponível** (RN-0002), nunca "saudável" nem valor anterior |
| Erros (`405`, `5xx` inesperado) | Formato de erro padronizado da plataforma (sugestão: RFC 9457, `application/problem+json`, apenas `type`, `title`, `status`). **Nunca** stack trace, caminho, nome de máquina ou variável de ambiente (REQ-0004, CA-05) |
| Cabeçalhos | `Cache-Control: no-store`; `X-Content-Type-Options: nosniff`; sem cabeçalho que revele servidor, versão do runtime ou do framework; ID de correlação aceito/gerado e devolvido (`X-Request-Id`, formato restrito) |
| Dados proibidos | Dados pessoais, credenciais, tokens, hostnames, IPs, caminhos, versões de runtime/dependências, hash de commit, variáveis de ambiente, estado de dependências |
| CORS | Somente a origem do Portal configurada (`PORTAL_API_ALLOWED_ORIGIN`); sem curinga; métodos `GET`/`HEAD`; sem credenciais |
| Desempenho (L6) | Sem E/S externa; alvo **indicativo** de p95 ≤ 100 ms em execução local, a calibrar por OPS/QA (não é SLO). Tempo limite do cliente (Portal): orientação de 5 s, a fechar pelo AS na ET |
| Observabilidade | Log estruturado por requisição em nível `debug` para `/health` (evita ruído de sondas); erros em `error`; sem dados sensíveis |
| Versionamento do contrato | OpenAPI 3.1, SemVer próprio, inicial `1.0.0` (distinto da versão do serviço). Campo novo opcional = MINOR; remoção/renomeação/mudança de tipo = MAJOR (ADR; AH se público) |
| Testes de contrato | Provedor: resposta valida contra o esquema aprovado (`200` e `503`) e ausência de campos extras; Consumidor: Portal testado com mocks do contrato (PR-04), incluindo corpo inválido, tempo esgotado e `5xx` |

### Diretrizes para o Portal (consumidor)
- Consulta por `fetch` com tempo limite, sem cache; ao carregar e por atualização manual (polling automático fora de escopo; UX decide a ação).
- Conteúdo da resposta inserido no DOM **somente como texto** (nunca como HTML) e apenas os três campos; mensagens de erro genéricas.
- Servidor estático do Portal com `Content-Security-Policy` restritiva (`default-src 'self'`; `connect-src` limitado à origem da API) e `X-Content-Type-Options: nosniff` (a confirmar na stack, ADR-0001).

### Delegação e validação (G3)
- **AS (Juliana Castro):** elabora EF/ET e o OpenAPI 3.1 de `portal-api` em `02-tecnica/contratos-api/portal-api/` seguindo estas diretrizes; consulta o ARQ por MSG-COL para qualquer desvio.
- **ARQ (G3):** valida o contrato quando: (a) o OpenAPI é válido e traz exemplos de `200`/`503`/`405`; (b) campos, enums, formatos e `additionalProperties: false` coincidem com esta ADR e com o ADR-0002; (c) não há dado sensível nem detalhe interno em nenhuma resposta; (d) cabeçalhos e erros seguem a tabela; (e) os testes de contrato estão previstos; (f) o contrato é interno (qualquer exposição pública reabre R3/N3).
- **G3 não se inicia antes** da decisão sobre o ADR-0001 (a forma de implementação depende dela; o contrato em si é independente de stack).

## Alternativas avaliadas
| Alternativa | Veredito |
|---|---|
| `/health` único, liveness, sem autenticação, só interno (proposta) | Escolhida: atende a solicitação com a menor superfície |
| `/health` com autenticação | Rejeitada: sondas passam a depender de credencial e de decisão de segurança sem necessidade (nenhum dado sensível é exposto) |
| Resposta rica (dependências, uptime, host, commit) | Rejeitada: viola RN-0001/REQ-0004 e amplia a superfície de ataque |
| Separar `/health/live` e `/health/ready` já agora | Adiada: sem dependências não há o que distinguir (YAGNI) |
| Timestamp com deslocamento local (`-03:00`) | Rejeitada: servidor emite UTC; apresentação em America/Sao_Paulo é do Portal |
| Campos em português (`versao`) | Rejeitada: identificadores de API em inglês e ASCII; texto ao usuário em português no Portal |

## Justificativa
Mínimo que atende status, versão e timestamp, sem dado sensível e sem autenticação desnecessária, com condições explícitas que reabrem a análise de risco quando a exposição mudar. Seguindo as regras de microsserviços (health check desde o nascimento, contrato antes do código, erros padronizados).

## Consequências e impactos
- **Portal Web:** requisito de tratamento de erro, de renderização segura e de formatação de data.
- **Backend/APIs:** rota única, serviço de saúde com relógio injetável, esquema de resposta.
- **Microsserviços/Integrações/Dados/Mobile:** sem impacto.
- **Infraestrutura:** sondas futuras usam o mesmo endpoint sem credenciais; exposição só interna.
- **Segurança:** superfície mínima; ponto de reavaliação obrigatório na mudança de exposição.
- **Nível de autonomia:** contrato interno compatível = N2 (aprovação do ARQ no G3). Torna-se N3 se virar público.

## Status
Proposto → Aceito (somente o Arquiteto Líder aprova) → Substituído/Rejeitado. ADR aceito é imutável: para mudar, crie novo ADR com `substitui: ADR-0003`.
