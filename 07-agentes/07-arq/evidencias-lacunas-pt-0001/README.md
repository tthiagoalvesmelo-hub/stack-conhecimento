# Evidências — lacunas L-PT-03, L-PT-04, L-PT-11, L-PT-13 e PS-09 (DEC-ARQ-0012, 0013, 0014; DEC-ARQ-0007 v1.2)

> [TESTE] DEM-2026-001 · TASK-0010. **Protótipo descartável do ARQ, fora do monorepo do Portal. NÃO é o spike R4** (que continua sendo do FS/OPS sobre o código real) **nem substitui os testes do FS/QA.** Serve só para fundamentar decisões de arquitetura com medição, e não com suposição.

Ambiente: ver `00-ambiente.txt` (SDK 10.0.404; runtime 10.0.15; Linux). Nenhum segredo, valor de ambiente real ou caminho local neste diretório (a linha "Content root path" foi omitida na saída de logs).

| Arquivo | O que mostra | Decisão que sustenta |
|---|---|---|
| 01-options-preflight.txt | OPTIONS com e sem `Origin`/`Access-Control-Request-Method`, origem permitida e negada; UseCors global e RequireCors | DEC-ARQ-0012 §1 (L-PT-03) |
| 02-endpoints-registrados.txt | Endpoints do `EndpointDataSource`: o preflight não é endpoint | DEC-ARQ-0012 §2 (L-PT-11) |
| 03-logs-categorias.txt | Registros por requisição com e sem a regra `Microsoft.AspNetCore=Warning`, e dependência da raiz de conteúdo | DEC-ARQ-0013 (L-PT-13) |
| 04-janela-drenagem.txt | Janela de drenagem, tempo de saída, requisição em voo, mecanismo alternativo (IHostedService) | DEC-ARQ-0012 §3 (L-PT-04) |
| 05-nuget-audit-exit-codes.txt | Códigos de saída do restore e do `dotnet list package --vulnerable` com pacote vulnerável de controle | DEC-ARQ-0007 v1.2 (A5) |
| 06-njsonschema-contra-contrato.txt | NJsonSchema contra os esquemas reais do OpenAPI | DEC-ARQ-0014 (PS-09) |
| 07-regex-datetime-sem-pacote.txt | `$` × `\z` e `TryParseExact` para o `timestamp` | DEC-ARQ-0014 (PS-09), R2/R5 |
| prototipo/ | Fonte do protótipo (Program.cs) e scripts de medição (drain.py, inflight.py) | reprodução |

Limites: sem `WebApplicationFactory` (o protótipo usa Kestrel real e `curl`); sem o código real do FS; a medição de logs usa o provedor Console (o comportamento de filtro por categoria é o do framework, comum aos provedores). O FS confirma cada ponto na 1ª implementação e o spike R4 repete a janela de drenagem com o `stop-local.sh` real.
