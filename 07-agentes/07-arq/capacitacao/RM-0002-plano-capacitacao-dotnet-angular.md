---
id: PLANO-RM-0002
titulo: "Plano de capacitação do time em C#/.NET e Angular (RM-0002)"
tipo: plano
versao: 1.1
status: proposto
dono: ARQ
autores: [ARQ]
aprovado_por: null
criado_em: 2026-11-26T15:06-03:00
atualizado_em: 2026-11-26T15:19-03:00
revisar_ate: 2027-02-26
relacionados: [RM-0002, RM-0001, DEC-CPO-0001, AH-0003, ADR-0001, DEM-2026-001, INST-TECNOLOGIAS]
substitui: null
substituido_por: null
---

# PLANO-RM-0002 — Capacitação em C#/.NET e Angular

> [TESTE] Fase de testes internos. **Conteúdo: ARQ (dono, DEC-CPO-0001). Prioridade: CPO (Alta).** **Escopo de negócio, prazo e a inclusão de papéis são propostas do ARQ, marcadas "PARA VALIDAÇÃO" da CPO e do PO; o ARQ não os decide.** **Custo zero** (DEC-CPO-0001): só fontes gratuitas e oficiais; qualquer curso, certificação, licença ou ferramenta paga exige AH própria. Este plano não prevê nenhuma.

## Validação da CPO (26/11/2026 15:12) e premissas da diretriz
A CPO validou este plano estrategicamente, dentro da DEC-CPO-0001 (sem DEC nova):
- **Fora:** MOB, PMM e AN.
- **DBA e SUP:** fora agora; **entram por gatilho.** Antes da primeira atividade de cada um numa demanda .NET/Angular, o **ARQ define um núcleo curto** para o papel (conteúdo, fontes oficiais gratuitas, uma evidência, carga horária).
- **Prazo e forma** (leitura + exercício + evidência; Parcial sem evidência) aceitos, com a condição de o PO avisar a CPO se o núcleo atrasar uma TASK. Prioridade da DEM-2026-001 permanece Normal.
- **Pendente:** o PO validar o impacto em backlog e prazo da demanda.

**Premissas (a) e (b) da diretriz AH-0003, vigentes até o Thiago responder** (texto levado pela CPO): (a) Angular **22.x estável** mais recente (hoje 22.3.0), acompanhando o suporte; (b) C#/.NET **só nas APIs do Portal Web**. Se (b) ampliar, a CPO abre DEC-CPO-0002. A DEM-2026-001 não espera essa resposta.

## 1. Objetivo
Capacitar os agentes envolvidos para trabalhar na stack da AH-0003 (ADR-0001 v2): **C# em .NET 10 LTS com ASP.NET Core Minimal APIs** e **Angular 22.x**, com os padrões de qualidade da Stack (DEC-ARQ-0007..0011). Resultado esperado: cada agente comprova, por **uma evidência verificável**, que consegue executar o seu papel nessa stack. **A DEM-2026-001 é o primeiro exercício prático e não espera o fim da capacitação** (DEC-CPO-0001).

## 2. Escopo (PARA VALIDAÇÃO — CPO/PO)
- **Papéis:** ARQ, FS, AS, CR, QA, OPS, UX, DOC (os oito pedidos). **Mobile (MOB):** a DEC-CPO-0001 o lista entre os impactados, mas a AH-0003 trata de API/front-end do Portal Web e o Mobile segue em Java. **Proposta: fora deste plano** (sem impacto no Mobile); a CPO decide se entra.
- **Conteúdo:** apenas o necessário para a demanda e para o padrão da Stack (não é formação completa em C# nem em Angular). Fora: bancos (EF Core), autenticação, SSR, bibliotecas de UI, nuvem, containers (D5 do ADR-0001 v2).
- **Fontes:** Microsoft Learn e documentação oficial do .NET/ASP.NET Core; angular.dev. Nada pago.

## 3. Fontes oficiais e gratuitas (URLs abertas em 26/11/2026; HTTP 200 e título conferidos)
| # | Fonte | Uso |
|---|---|---|
| M1 | Write your first code using C# (Get started with C#, Part 1) — https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-1/ | C# básico |
| M2 | A tour of C# — https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/ | referência rápida da linguagem |
| M3 | Tutorial: Create a Minimal API with ASP.NET Core — https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api (pré-requisito: SDK .NET 10) | API base |
| M4 | APIs overview (Minimal APIs) — https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/overview | modelo de API |
| M5 | ASP.NET Core middleware — https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/ | pipeline, cabeçalhos, X-Request-Id |
| M6 | Dependency injection in ASP.NET Core — https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection | ganchos de teste (L-12) |
| M7 | Enable Cross-Origin Requests (CORS) in ASP.NET Core — https://learn.microsoft.com/en-us/aspnet/core/security/cors | CORS (L-06) |
| M8 | Handle errors in ASP.NET Core (ProblemDetails) — https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling | problem+json (L-01) |
| M9 | Kestrel web server — https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel; .NET Generic Host — https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host | execução, encerramento gracioso |
| M10 | Integration tests in ASP.NET Core (`WebApplicationFactory`) — https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests | testes de API |
| M11 | Unit testing C# with xUnit — https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-csharp-with-xunit; Code coverage — https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-code-coverage | xUnit e cobertura |
| M12 | NuGet auditing — https://learn.microsoft.com/en-us/nuget/concepts/auditing-packages; `dotnet format` — https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format; MSBuild properties — https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props | SCA, formato, analyzers, versão |
| M13 | Install .NET on Linux — https://learn.microsoft.com/en-us/dotnet/core/install/linux; global.json — https://learn.microsoft.com/en-us/dotnet/core/tools/global-json; support policy — https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core | instalação e versões |
| A1 | Learn Angular (tutorial interativo) — https://angular.dev/tutorials/learn-angular | fundamentos |
| A2 | Essentials — https://angular.dev/essentials; What is Angular? — https://angular.dev/overview | conceitos |
| A3 | Angular CLI — https://angular.dev/tools/cli; `ng lint` — https://angular.dev/cli/lint | ferramentas |
| A4 | HTTP Client — https://angular.dev/guide/http | consumo da API |
| A5 | Testing — https://angular.dev/guide/testing (padrão Vitest + jsdom) | testes do Portal |
| A6 | Accessibility — https://angular.dev/best-practices/a11y | UX/QA |
| A7 | Releases — https://angular.dev/reference/releases; Version compatibility — https://angular.dev/reference/versions | política de versões |
**Durações:** só os módulos do Microsoft Learn que declaram tempo têm duração de fonte: "Write your first C# code" 27 min, "Create a web API with ASP.NET Core controllers" 41 min, "Build a web API with minimal API, ASP.NET Core, and .NET" 20 min, "Introduction to .NET" 28 min, "Create a new .NET project and work with dependencies" 18 min, "Create a web UI with ASP.NET Core" 45 min (coleção https://learn.microsoft.com/en-us/collections/moqrtqmjz7d8, 28 módulos, 16 h 4 min). O tutorial Learn Angular e as demais páginas **não declaram duração**. **Todas as horas por papel abaixo são ESTIMATIVAS DO ARQ** (leitura + exercício), não valores das fontes.

## 4. Conteúdo, carga horária, evidência por papel
**Núcleo** = obrigatório antes da primeira atividade técnica do papel na DEM-2026-001. **Complementar** = depois, em paralelo. Horas = estimativa do ARQ, em intervalo.

| Papel | Objetivos | Conteúdo (fontes) | Núcleo | Total | **UMA evidência de conclusão** |
|---|---|---|---|---|---|
| **ARQ** | Governar a stack: pipeline, DI, hospedagem, ProblemDetails, versões e suporte; fechar os itens PV do ADR-0001 v2 D8 | M3–M9, M12, M13, A3, A7 | 8–10 h | 14–20 h | **Relatório de spike** `capacitacao/evidencias/spike-aspnetcore-health.md`, com saídas de comando fechando os itens PV do D8 (depende do SDK instalado pelo OPS) |
| **FS** | Implementar `GET /health` em Minimal API e a tela em Angular, com testes e `verify-local` verde | M1–M3, M5–M7, M10–M12, A1, A2, A4, A5 | 12–16 h | 18–26 h | **Log do `verify-local` verde** do repositório-laboratório `/workspace/projetos/lab-dotnet-angular/` (API de saúde com teste + componente Angular com teste), com o hash do commit |
| **AS** | Mapear padrões do ASP.NET Core ao contrato; reescrever as premissas PS-01..PS-09 da ET | M4, M5, M7, M8, M12 (versão), A4 | 4–6 h | 6–10 h | **ET-0001 v1.4** com a tabela PS reescrita (entregável real; conferida pelo ARQ) |
| **CR** | Revisar C# e TypeScript/Angular com critério: nulabilidade, DI, ganchos de teste, analyzers, cabeçalhos | M1, M2, M5, M6, M10, M11, M12, A3, A5 | 6–8 h | 10–14 h | **Parecer de revisão do PR do laboratório do FS**, com checklist C#/Angular aplicado (checklist anexado) |
| **QA** | Planejar e executar testes de API (xUnit, `WebApplicationFactory`) e do Portal (`ng test`), cobertura 80% de linhas | M10, M11, M8, A5, A6 | 6–8 h | 10–14 h | **Relatório de execução dos testes do laboratório**, com cobertura e **3 casos dos itens PV** (ProblemDetails de 404/405/500, `timestamp` com 3 casas, versão sem `+`) |
| **OPS** | Instalar SDK .NET 10 e Angular CLI na box; `verify-local`; execução em loopback; p95 | M13, M9, M11, M12, A3 | 6–8 h | 10–14 h | **Log sanitizado** de `dotnet --info`, `ng version` e do `verify-local.sh` executado na box (sem segredos) |
| **UX** | Traduzir a spec UX-0001 em componentes Angular acessíveis | A1, A2, A6 | 2–3 h | 4–6 h | **UX-0001 v1.2** com a seção "mapeamento para componentes Angular e acessibilidade", revisada pelo FS |
| **DOC** | Documentar a stack: glossário, README do monorepo, ponteiros | M13 (versões), A7, `tecnologias.md` | 2–3 h | 3–5 h | **Glossário .NET/Angular e README-modelo do monorepo** versionados no stack-conhecimento |
| **Total** | | | **46–62 h** | **75–109 h** | 8 evidências |
Premissa das horas: agentes sem experiência prévia na stack; leitura + exercício; sem tempo de espera de terceiros; não inclui a execução da demanda. Os agentes não "reprovam" a si mesmos: veja §6.

## 5. Prazo (PARA VALIDAÇÃO — CPO/PO)
- **Núcleo:** concluído **antes** da primeira atividade técnica do papel: OPS e ARQ antes do spike/TASK-0012; AS antes da ET-0001 v1.4; FS antes da TASK-0008; CR antes da revisão do G4; QA antes da TASK-0010; UX antes de adaptar a UX-0001; DOC antes do incremento B da TASK-0011.
- **Complementar:** até **10 dias úteis** após o início do plano (proposta; o prazo de negócio é da CPO/PO).
- **Encerramento da RM-0002:** as 8 evidências aceitas (ver §6). Não bloqueia a DEM-2026-001, que segue em paralelo (DEC-CPO-0001).

## 6. Evidências, aceite e vínculo com a DEM-2026-001
- "Quem produz não aprova": o **ARQ aceita** as evidências dos outros sete papéis; a evidência do **ARQ é conferida pelo CR** e o **ORQ registra** o encerramento. Sem evidência verificável, o papel permanece "Parcial".
- **Laboratório** (`lab-dotnet-angular`): repositório local descartável, **fora** do Portal e sem código de produção; criado pelo OPS/FS depois da instalação do SDK; sem segredos.
- **Vínculo:** a TASK-0012 (OPS) instala SDK/CLI; a ET-0001 v1.4 (AS) e a UX-0001 v1.2 (UX) são entregáveis reais da demanda que valem como evidência; a TASK-0008 (FS) é o primeiro exercício prático em produção de teste.

## 7. Riscos e lacunas
| ID | Risco / lacuna | Tratamento |
|---|---|---|
| R-1 | Horas são estimativas do ARQ, sem base histórica | Recalibrar após as primeiras evidências |
| R-2 | Dependência do SDK instalado (OPS) para as evidências de ARQ, FS, QA, OPS | OPS primeiro; sem SDK, essas evidências ficam "Parcial" |
| R-3 | Sem experiência, risco de qualidade na TASK-0008 | CR e a segunda aprovação do ARQ no G4 (R3) |
| L-1 | Escopo de MOB, PMM, AN, DBA e SUP | **Fechada pela CPO (15:12):** MOB/PMM/AN fora; DBA/SUP por gatilho (núcleo curto do ARQ) |
| L-2 | Prazo de negócio | **Prazo e forma validados pela CPO (15:12)**; falta o PO validar o impacto em backlog e prazo da DEM |
| L-3 | Qualquer custo (curso, certificação, licença) | Exige AH própria; **não previsto** |
