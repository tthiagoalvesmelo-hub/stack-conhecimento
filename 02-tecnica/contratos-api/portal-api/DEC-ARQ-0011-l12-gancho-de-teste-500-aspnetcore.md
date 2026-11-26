---
id: DEC-ARQ-0011
titulo: "Confirmação formal da L-12: gancho de teste do HTTP 500 (e do 503) por WebApplicationFactory, fora do OpenAPI"
tipo: dec
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:06-03:00
atualizado_em: 2026-11-26T15:06-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0007, TASK-0008, TASK-0010, ET-0001, US-0001, ADR-0001, ADR-0003, DEC-ARQ-0002, DEC-ARQ-0007, AH-0003, L-12, L-05]
substitui: null
substituido_por: null
---

# DEC-ARQ-0011 — L-12: gancho de teste do 500 (e do 503) em ASP.NET Core

> [TESTE] Confirmação formal pedida na ressalva (b) do G2, no G3 (TASK-0007). Não é N3 (nenhuma exposição nova; reduz risco). Não altera o OpenAPI.

## Decisão
1. **L-12 confirmada.** O princípio da DEC-ARQ-0002 L-05 (que citava só o 503) **estende-se ao HTTP 500** (US-0001 CA-09): o 500 só é provocável **por injeção de colaborador na composição de teste**; em execução fora de teste o gancho **não existe**.
2. **Mecanismo no ASP.NET Core (ADR-0001 v2):** a lógica de saúde depende de abstrações injetadas (estado de saúde e origem de falha interna; nomes e assinaturas: FS). A composição de produção (`Program.cs`) registra apenas as implementações reais (nunca falham; o estado de encerramento vem do ciclo de vida do host). Os testes de integração usam **`WebApplicationFactory<Program>`** (pacote `Microsoft.AspNetCore.Mvc.Testing`, série 10.0.x) com `WithWebHostBuilder(... ConfigureTestServices ...)` para **trocar** essas abstrações por dublês que simulam 503 ou falha interna. A forma de expor `Program` ao projeto de teste é a padrão da documentação de testes de integração do ASP.NET Core (a confirmar na primeira implementação); não pode ampliar a superfície em produção.
3. **Proibido** (qualquer um seria N3 de segurança): endpoint, parâmetro de query, cabeçalho, variável de ambiente, chave de configuração (`appsettings*`, `IConfiguration`), `FORCE_*`, ramo condicionado a `ASPNETCORE_ENVIRONMENT`/`IHostEnvironment.IsDevelopment()` ou a `#if DEBUG` que provoque ou altere o caminho de falha. O executável testado e o de execução são o **mesmo código de produção**.
4. **Fora do OpenAPI:** o gancho **não** é documentado no contrato; a superfície 1.0.0 permanece `GET /health` (+ `HEAD` tolerado e preflight) com respostas 200/503/405/500.
5. **Corpo do 500:** `application/problem+json` com apenas `type: about:blank`, `title: Internal Server Error`, `status: 500`; sem `traceId` nem detalhe, **em qualquer ambiente** (inclui `Development`; sem página de exceção de desenvolvedor).
6. **Testes obrigatórios** (QA escreve/planeja; CR verifica no G4):
   - 500 por falha injetada: status, `Content-Type`, corpo exato, `Cache-Control: no-store`, `X-Content-Type-Options: nosniff`, `X-Request-Id` canônico.
   - 503 por estado injetado: corpo no esquema, **sem** `Retry-After`.
   - Negativo de segurança: query, cabeçalho ou variável de ambiente tentando forçar 503/500 **não** alteram o 200 (CA-05/REQ-0004).
   - Fábrica **sem** override responde 200 (composição de produção sem gancho).
   - Corpo do 500 sem detalhe com `ASPNETCORE_ENVIRONMENT=Development`.
   - Teste de superfície: o conjunto de endpoints registrados é apenas `/health` (GET/HEAD) e o tratamento de preflight.
7. **Distinção mantida:** o gancho de **teste** não se confunde com o **encerramento gracioso em execução** (PS-05; ADR-0001 v2 D8 item 10), que é comportamento de produção do 503 e também não pode virar controle remoto.

## Verificação e responsabilidade
FS implementa; QA testa (TASK-0010); CR inclui no checklist do G4 "nenhum gancho de falha na composição de produção"; ARQ reconfirma na 2ª aprovação do G4.
