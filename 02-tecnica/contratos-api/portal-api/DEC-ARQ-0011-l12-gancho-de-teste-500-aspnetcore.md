---
id: DEC-ARQ-0011
titulo: "Confirmação formal da L-12: gancho de teste do HTTP 500 (e do 503) por WebApplicationFactory, fora do OpenAPI"
tipo: dec
versao: 1.2
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:06-03:00
atualizado_em: 2026-11-26T16:00-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0007, TASK-0008, TASK-0010, ET-0001, US-0001, ADR-0001, ADR-0003, DEC-ARQ-0002, DEC-ARQ-0007, DEC-PO-0009, AH-0003, L-12, L-05, DEC-ARQ-0015]
substitui: null
substituido_por: null
---

# DEC-ARQ-0011 — L-12: gancho de teste do 500 (e do 503) em ASP.NET Core

> [TESTE] Confirmação formal pedida na ressalva (b) do G2, no G3 (TASK-0007). Não é N3 (nenhuma exposição nova; reduz risco). Não altera o OpenAPI.

## Decisão
1. **L-12 confirmada.** O princípio da DEC-ARQ-0002 L-05 (que citava só o 503) **estende-se ao HTTP 500** (US-0001 CA-09): o 500 só é provocável **por injeção de colaborador na composição de teste**; em execução fora de teste o gancho **não existe**.
2. **Mecanismo no ASP.NET Core (ADR-0001 v2):** a lógica de saúde depende de abstrações injetadas (estado de saúde e origem de falha interna; nomes e assinaturas: FS). A composição de produção (`Program.cs`) registra apenas as implementações reais (nunca falham; o estado de encerramento vem do ciclo de vida do host). Os testes de integração usam **`WebApplicationFactory<Program>`** (pacote `Microsoft.AspNetCore.Mvc.Testing`, série 10.0.x) com `WithWebHostBuilder(... ConfigureTestServices ...)` para **trocar** essas abstrações por dublês que simulam 503 ou falha interna. A forma de expor `Program` ao projeto de teste é a padrão da documentação de testes de integração do ASP.NET Core (**confirmado** na primeira implementação — esclarecimento v1.2 e DEC-ARQ-0015: `WebApplicationFactory<Program>` funciona sem `public partial class Program`); não pode ampliar a superfície em produção.
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

## Esclarecimento v1.1 (26/11/2026) — autoria dos testes e dependência da fase PT+CT
**Não altera** a decisão da L-12 (itens 1–7: mecanismo, proibições, fora do OpenAPI, os 6 casos obrigatórios). Apenas esclarece a frase "QA escreve/planeja" do item 6 e o parágrafo "Verificação e responsabilidade", a pedido do PO (MSG-COL 15:20) e em linha com a DEC-PO-0009:

**Opção A (adotada):**
- O **FS escreve e mantém** o código dos testes automatizados na **TASK-0008**: xUnit / `WebApplicationFactory` (os 6 casos do item 6, os itens PV do ADR-0001 v2 D8, R2 e R5) e `ng test` / Vitest do Portal.
- A **QA especifica** PT/CT e oráculos **antes do PR**, **verifica** a suíte e **executa** os testes black-box e manuais na **TASK-0010**. Não escreve o código da suíte automatizada nesta demanda.
- A opção B (QA escreve o código) **não** é adotada.

**Dependência da fase PT+CT da TASK-0010:** o ARQ **concorda tecnicamente** que essa fase passa a depender de **"G3 + R1"** (e não do G4). Motivo: a R3 do G3 exige que os casos PV existam como teste obrigatório **antes da entrada no G4**; a especificação (QA) e o código (FS) precisam estar prontos após a R1. A **execução** da suíte e o PQ **continuam após o G4**. A decisão de planejamento é do PO (DEC-PO-0009); este parágrafo é concordância técnica do ARQ.

## Esclarecimento v1.2 (26/11/2026) — exposição de `Program` (fecha a lacuna do item 2)
**Não altera** a decisão da L-12 (itens 1–7) nem o esclarecimento v1.1 (Opção A). Apenas fecha o “a confirmar na primeira implementação” do item 2, com evidência do FS no esqueleto D6 da TASK-0008 (ramo `feat/TASK-0008-health-portal`, HEAD `2240056`, repositório `portal`): `WebApplicationFactory<Program>` funciona **sem** declarar `public partial class Program`. Nada além disso é exigido para expor `Program` ao projeto de teste. O item 3 permanece (proibido qualquer artifício que amplie a superfície em produção). Detalhe e rastreio: DEC-ARQ-0015 §2.
