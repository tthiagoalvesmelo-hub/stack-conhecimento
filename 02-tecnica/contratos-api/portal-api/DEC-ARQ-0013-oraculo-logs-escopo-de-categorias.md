---
id: DEC-ARQ-0013
titulo: "Oráculo de logs do ADR-0001 v2 D8 item 13: escopo de categorias e nível do framework (L-PT-13)"
tipo: dec
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:54-03:00
atualizado_em: 2026-11-26T15:54-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0007, TASK-0008, TASK-0010, PT-0001, CT-0023, CT-0024, CT-0025, ADR-0001, DEC-ARQ-0011, RN-0001, US-0001, L-PT-13]
substitui: null
substituido_por: null
---

# DEC-ARQ-0013 — Escopo de categorias do oráculo de logs (D8 item 13)

> [TESTE] Decide a L-PT-13 do PT-0001 v1.1. **Refina o oráculo** do parecer G3 v1.2 §9.2 (3) **sem alterar o ADR-0001 v2** (aceito, imutável; o item 13 segue: "`ILogger` estruturado; `/health` em nível Debug; erros em Error; nada sensível"). Sem custo, sem N3. Medições: `07-agentes/07-arq/evidencias-lacunas-pt-0001/` (03).

## Problema medido
Com a configuração padrão (nível `Information`) e **sem** regra para o framework, um único `GET /health` gera **cinco registros Information do framework**: `Microsoft.AspNetCore.Hosting.Diagnostics` ("Request starting…" e "Request finished…"), `Microsoft.AspNetCore.Routing.EndpointMiddleware` ("Executing endpoint…" e "Executed endpoint…") e `Microsoft.AspNetCore.Http.Result.JsonResult`. Isso viola "`/health` em Debug" e o oráculo "nada ≥ Information". Na documentação oficial (https://learn.microsoft.com/en-us/aspnet/core/fundamentals/logging/?view=aspnetcore-10.0, consultada em 26/11/2026) a recomendação é `Default = Information` e `Microsoft.AspNetCore = Warning`; o gabarito `dotnet new web` traz essa regra no `appsettings.json`.

Também medido: a regra no `appsettings.json` **só vale se o arquivo estiver na raiz de conteúdo**, que por padrão é o diretório de trabalho do processo; iniciado de outro diretório, a regra não foi lida e os registros do framework voltaram. Uma regra **em código** não tem essa fragilidade.

## Decisão
1. **Decisão de escopo:** o oráculo vale para **as duas coisas**, não só para a aplicação. As categorias do framework **não** são excluídas do oráculo: elas são **silenciadas por configuração** (item 2) e o teste verifica o efeito.
2. **Regra obrigatória, em código, na composição de produção (`Program.cs`):** `builder.Logging.AddFilter("Microsoft.AspNetCore", LogLevel.Warning)`. O prefixo cobre `Hosting.Diagnostics`, `Routing.*`, `Http.Result.*` e `Server.*`. Pode haver cópia no `appsettings.json`, mas **não** é ela que garante o requisito. O `LOG_LEVEL` (ADR-0001 v2 D7; hoje `Information` por padrão) continua definindo o nível base da aplicação e **não** reabilita o framework.
3. **Ciclo de vida do host** (`Microsoft.Hosting.Lifetime`: "Now listening on", "Application started", "Hosting environment", "Content root path", "Application is shutting down") **fica no nível padrão** e **fora do oráculo**: acontece na partida e na parada, **não por requisição**, e a OPS precisa dele. Observação de risco: essas linhas trazem URL de escuta e **caminho da raiz de conteúdo**; no log local de teste isso é aceito e a evidência é sanitizada (parecer OPS v2.1); rever no ADR de produção. Não é falha do item 13.
4. **Janela da requisição:** o sumidouro de logs registra o índice (ou o instante) antes e depois da requisição; só os registros dessa janela entram nos oráculos (a)–(b); os da partida e da parada do host ficam de fora.

## Oráculo resultante (CT-0023, CT-0024, CT-0025 — a QA ajusta o texto; não crio nem altero CT)
Mecanismo (do FS, a confirmar na 1ª implementação): sumidouro de `ILogger` escrito à mão, injetado na `WebApplicationFactory`; o teste **eleva** só a categoria da aplicação a `Debug` (prefixo do namespace raiz, ex.: `Portal.Api`, constante documentada pelo FS); **não** usa regra que reabilite categorias do framework (nada de `SetMinimumLevel(Debug)` global que sobreponha a regra do item 2).

- **CT-0023 (13a), `GET /health` com 200 e `X-Request-Id` conhecido:**
  1. Categorias da aplicação: ≥ 1 registro **Debug** com o `X-Request-Id` no estado estruturado ou no escopo (nome do campo: FS documenta); **0** registros ≥ Information.
  2. Categorias do framework: **0** registros ≥ Information de `Microsoft.AspNetCore.*` na janela. Verificação complementar equivalente: `loggerFactory.CreateLogger("Microsoft.AspNetCore.Hosting.Diagnostics").IsEnabled(LogLevel.Information)` é `false`.
  3. Nenhum registro Information, Warning ou Error na janela, de qualquer categoria, **exceto** o que o item 3 deixa fora.
- **CT-0024 (13b), 500 injetado (L-12):** ≥ 1 registro **Error** de **categoria da aplicação**; o corpo HTTP continua só `type`/`title`/`status`. Registros Error do framework são permitidos.
- **CT-0025 (13c), caminhos 200, 503 injetado e 500 injetado:** em **todos os registros capturados na janela** (mensagem formatada, estado estruturado, valores de escopo, tipo e mensagem da exceção), nenhum dado pessoal, credencial, token, nome de máquina, IP, caminho **de arquivo do sistema**, versão de runtime/dependência, hash de commit ou valor de variável de ambiente. Esclarecimentos: (i) o caminho da requisição (`/health`) **é permitido** no log da aplicação; (ii) o rastreio de pilha (`Exception.StackTrace`) só é permitido em registro **Error** e fica isento da regra de "caminho de arquivo" (o rastreio pode trazer o caminho do build); nunca no corpo HTTP.

## Verificação e responsabilidade
FS implementa a regra e os testes (TASK-0008, opção A); QA especifica e verifica (TASK-0010); CR confere no G4 a regra do item 2 na composição de produção; ARQ reconfirma na 2ª aprovação do G4. Nenhum CA muda.

## Histórico
| Versão | Data/hora (America/Sao_Paulo) | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 15:54 | ARQ | Criação (L-PT-13) |
