---
id: VALIDACAO-PO-PLANO-RM-0002
titulo: "Validação do PO — escopo, sobreposição e prazo do PLANO-RM-0002 v1.0 na DEM-2026-001"
tipo: analise
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T15:17-03:00
atualizado_em: 2026-11-26T15:17-03:00
revisar_ate: 2027-02-26
relacionados: [RM-0002, RM-0001, DEM-2026-001, PLANO-RM-0002, PLANO-DEM-2026-001-G2, DEC-CPO-0001, AH-0003, ADR-0001, TASK-0008, TASK-0009, TASK-0010, TASK-0012, TASK-0003, TASK-0007, TASK-0011, DEC-ARQ-0007, DEC-ARQ-0008, DEC-ARQ-0009, DEC-ARQ-0010, DEC-ARQ-0011]
substitui: null
substituido_por: null
---

# Validação do PO — PLANO-RM-0002 v1.0 e prazo da DEM-2026-001

> [TESTE] Fase de testes internos; nada vai à produção. 26/11/2026 15:17, America/Sao_Paulo.
> Alçada: análise de backlog, sobreposição de esforço e caminho crítico da DEM (PO). **Não decide prioridade estratégica** (CPO; DEC-CPO-0001 vigente). Este documento **não** altera `historico.md`, `contexto.yaml`, `aprovacoes.md`, planilha nem artefatos de outros donos.
> Recomendação de esforço e prazo; a soma do plano G2 v1.2 permanece aberta até as reestimativas do OPS, do QA e da DOC.

## 1. Fontes (nenhum número inventado)

| Fonte | ID / caminho | Commit ou registro |
|---|---|---|
| Plano de capacitação v1.0 proposto | `07-agentes/07-arq/capacitacao/RM-0002-plano-capacitacao-dotnet-angular.md` (PLANO-RM-0002) | conteúdo `3dc12a6`; merge `97f90c4` |
| Prioridade e relação RM × DEM | DEC-CPO-0001 v1.0 vigente | `1c1bdf6` |
| Validação estratégica da CPO (escopo de papéis, prazo e forma) | transcrição do ORQ em `historico.md` e pendência em `contexto.yaml` | `b606d11` (15:12 / 15:14) |
| Contexto da demanda | `03-operacional/demandas/DEM-2026-001/contexto.yaml` v33 e v34 | v33: `89fb397`; v34: `b57eaa1` |
| Plano G2 v1.1 vigente (horas em Node; total 78 h após conversão do ARQ) | `03-operacional/demandas/DEM-2026-001/plano-atividades-g2.md` | vigente `f61a1f9`; conteúdo `053a2d4`; conversão ARQ `458acb8` |
| Stack vigente | ADR-0001 v2.0; DEC-ARQ-0007..0010 | `d40518e` |
| G3 com ressalvas R1..R5 | parecer / merge | `a271ac1` |
| Reestimativa FS (TASK-0008) | `/workspace/stack-memoria/rascunhos/fs/DEM-2026-001-TASK-0008-parecer-g2-v2-dotnet.md` | 26/11/2026 15:14; também em contexto v34 |
| Reestimativa CR (TASK-0009) | MSG-RET do CR ao PO, 26/11/2026 15:13; contexto v34 | `b57eaa1` |
| Horas do ARQ (pós-AH-0003) | MSG-RET ARQ e contexto v33/v34 | residual TASK-0003 0,5–1 h; TASK-0007 3–6 h (feita); 2ª aprovação no G4 1,5–3 h (+1 h no 2º ciclo) |
| R1 do G3 (AS) | ET-0001 v1.4 + EF-0001 v1.3 | `ac391ea`; merge `9b3dc1b`; contexto v34 registra ≈0,1 h real + 0,25 h de contingência |

Estado operacional: **Normal** (`00-memoria/governanca/estado-operacional.md`).

## 2. O que já está decidido (CPO) e o que este parecer cobre

A CPO, na DEC-CPO-0001 (`1c1bdf6`): RM-0002 com prioridade **Alta**; DEM-2026-001 permanece **Normal**, é o primeiro exercício prático da RM e **não espera o fim da capacitação**; a demanda **continua sem prazo definido**; custo zero.

Na validação estratégica das 15:12 (registro `b606d11`, sem DEC nova): (1) MOB fora; (2) PMM e AN fora; DBA e SUP fora agora, com gatilho (núcleo curto a definir pelo ARQ antes da 1ª atividade de cada um numa demanda .NET/Angular); (3) prazo de acordo, **com a condição de o PO avisar a CPO se o núcleo atrasar uma TASK**; prioridade da DEM continua Normal; (4) forma leitura + exercício + evidência; sem evidência, o papel permanece Parcial. Ficou pendente, no contexto v34, a validação do PO sobre **impacto em backlog e prazo da DEM**. É esta validação.

Este parecer **não** reabre prioridade, não inclui MOB/PMM/AN e não faz a DEM esperar o encerramento das 8 evidências da RM-0002 (§6 do plano).

## 3. (a) Escopo do núcleo frente a TASK-0008 / 0009 / 0010 / 0012

O plano (§4) define **núcleo** = obrigatório antes da primeira atividade técnica do papel na DEM, e declara que as horas **não incluem a execução da demanda**. **Complementar** = depois, em paralelo (proposta de até 10 dias úteis, §5). Totais do plano: núcleo **46–62 h**; completo **75–109 h**.

Cobertura do núcleo, só com as fontes listadas no próprio plano, para o que as quatro TASKs exigem na stack da AH-0003 / ADR-0001 v2.0 / DEC-ARQ-0007..0011:

| Papel / TASK | Núcleo (plano) | O que o núcleo cobre | Lacuna no recorte das fontes do núcleo | Complementar (pode ficar fora da DEM) |
|---|---|---|---|---|
| **FS / TASK-0008** | 12–16 h (total 18–26 h). Fontes: M1–M3, M5–M7, M10–M12, A1, A2, A4, A5 | C# inicial, Minimal API, middleware, DI, CORS, testes de integração, xUnit/Coverlet, formato/analyzers/NuGet Audit, fundamentos Angular, HTTP Client, testes do Portal | **M8** (ProblemDetails) e **M9** (Kestrel / Generic Host, encerramento gracioso) **não** estão nas fontes do núcleo do FS, embora a TASK-0008 inclua conformidade D8 e o protótipo do CA-07 (3 h no parecer v2). A3 (`ng lint` / CLI) também não está no núcleo do FS | 6–10 h (18–26 − 12–16). Fora do prazo da DEM |
| **CR / TASK-0009** | 6–8 h (total 10–14 h). Fontes: M1, M2, M5, M6, M10, M11, M12, A3, A5 | Linguagem, middleware, DI, testes, cobertura, analyzers/SCA, CLI, testes Angular — alinhado ao 1º ciclo (reexecução do `verify-local`, checklist C#/TypeScript) | M8 e M9 não figuram nas fontes do núcleo do CR, e o checklist do CR (15:13) inclui itens PV de ProblemDetails e encerramento gracioso | 4–6 h. Fora do prazo da DEM. A revisão do PR do laboratório (§6) é evidência da RM, distinta do G4 da TASK-0009 |
| **QA / TASK-0010** | 6–8 h (total 10–14 h). Fontes: M10, M11, M8, A5, A6 | `WebApplicationFactory`, xUnit, cobertura 80% de linhas, ProblemDetails, `ng test`, acessibilidade | M9 (encerramento / CA-07) e M12 (audit/format) não estão no núcleo do QA; o p95 (DEC-ARQ-0010) é método já decidido, não um módulo do plano. Reestimativa da TASK-0010 **ainda não chegou** (contexto v34) | 4–6 h. Fora do prazo da DEM. O relatório do laboratório é evidência da RM, distinta da execução da TASK-0010 |
| **OPS / TASK-0012** | 6–8 h (total 10–14 h). Fontes: M13, M9, M11, M12, A3 | Instalação do SDK/CLI, host/encerramento, cobertura, formato/audit, Angular CLI; objetivo do plano cita também `verify-local`, loopback e p95 | Nenhuma lacuna evidente no recorte das fontes para a preparação e o `verify-local`. Reestimativa da TASK-0012 **ainda não chegou** | 4–6 h. Fora do prazo da DEM |

**O que do completo pode ficar fora da DEM** (além do complementar dos quatro papéis acima):

- Complementar de ARQ (14–20 − 8–10 h), AS (6–10 − 4–6 h), UX (4–6 − 2–3 h) e DOC (3–5 − 2–3 h).
- Núcleo do **DOC** (2–3 h): o plano o pede antes do incremento B da TASK-0011, não como pré-requisito de 0008/0009/0010/0012. O incremento A (DEC-PO-0007) já corre e não depende da stack.
- Núcleo do **UX** (2–3 h, evidência UX-0001 v1.2): não é das quatro TASKs; pode afetar a TASK-0008 só se a v1.2 for insumo da tela. O parecer FS v2 registrou que a UX-0001 v1.2 não tinha sido vista. Fora do recorte estrito de 0008/0009/0010/0012, com ressalva.
- MOB, PMM e AN: já fora (CPO, 15:12). DBA/SUP: fora agora, por gatilho.

**Núcleos de outros papéis que tocam o caminho da DEM, mas não são as quatro TASKs:** AS 4–6 h antes da ET-0001 v1.4 (já entregue, merge `9b3dc1b`, confirmação do ARQ pendente); ARQ 8–10 h antes do spike / TASK-0012 (evidência `capacitacao/evidencias/spike-aspnetcore-health.md`, depende do SDK).

## 4. (b) Sobreposição com horas já estimadas na DEM (evitar contagem dupla)

Regra do próprio plano (§4 e §6): as horas da RM **não incluem a execução da demanda**; ao mesmo tempo, três evidências **são** entregáveis reais da DEM (instalação na TASK-0012; ET-0001 v1.4 da AS; UX-0001 v1.2) e a TASK-0008 é o primeiro exercício prático.

Reestimativas já recebidas (não somar o que falta):

| Item | Valor citado | Relação com o núcleo da RM-0002 | Risco de contagem dupla |
|---|---|---|---|
| TASK-0008 (FS, 15:14) | **40 h** de planejamento, faixa **32–50 h**. O parecer Node era 22 h | O núcleo do FS (**12–16 h**) fica **fora** da TASK. A faixa alarga por isso: o **mínimo** vale se a capacitação vier **antes**; o **máximo**, se a curva ocorrer **durante** a execução | **Não somar** 12–16 h de núcleo **com** o teto de 50 h. Os dois extremos já descrevem o mesmo esforço de aprendizado em momentos diferentes. Correto: (núcleo 12–16 + execução no mínimo/planejamento 32–40) **ou** (sem núcleo prévio + execução até 50), nunca os dois |
| TASK-0009 (CR, 15:13) | **5 h** no 1º ciclo + **2 h** no 2º. Se a capacitação do CR **não** tiver sido concluída, **+1 h**. Toolchain .NET 10 + Angular CLI 22 na box **antes** do PR (não está nas 5 h) | Núcleo do CR = 6–8 h, evidência = parecer do PR do laboratório, distinto do G4 | **Não somar** 6–8 h de núcleo **e** o +1 h. O +1 h é o substituto quando o núcleo não ocorreu. A toolchain é do OPS/FS, não do CR |
| TASK-0010 (QA) | Ainda **20 h (16–23 h)** do G2 v1.1 em Node (`40c8ace`) | Núcleo QA 6–8 h + relatório do laboratório | Reestimativa pendente. Quando chegar, aplicar a mesma regra: núcleo fora da TASK, sem somar núcleo e “curva na execução” |
| TASK-0012 (OPS) | Ainda prep. **8 h (6–10)** + G6/G7 **5 h (4–7)** + 24 h de calendário (parecer G2 em Node) | Núcleo OPS 6–8 h; evidência = log de `dotnet --info`, `ng version` e `verify-local`. A instalação do SDK/CLI é a mesma da preparação da TASK-0012 e pré-requisito do G4 (CR, 15:13) e das evidências da RM (R-2 do plano) | Reestimativa pendente. **Não contar duas vezes a instalação do SDK**: ou na preparação da 0012, ou no núcleo, com a interseção descontada. O G6/G7 formal não é capacitação |
| AS / ET-0001 v1.4 (R1) | Contexto v34: ≈**0,1 h** real + **0,25 h** de contingência; evidência da RM = a própria ET-0001 v1.4 | Núcleo AS 4–6 h no plano | A evidência já é o entregável da R1. **Não acrescer** 4–6 h de núcleo no prazo da DEM além do esforço já registrado da R1 |
| ARQ | Residual TASK-0003 **0,5–1 h**; G3 **3–6 h** (feita); 2ª aprovação G4 **1,5–3 h** (+1 h no 2º ciclo) | Núcleo ARQ 8–10 h; evidência = relatório de spike dos itens PV do D8 | Risco de **sobreposição de spike**: o parecer FS v2 reserva **3 h** (2–5) ao protótipo do CA-07 (G3 R4, D8 item 10). Se o spike do ARQ e o protótipo do FS forem o mesmo trabalho, contar uma vez. Não invento a partilha — o ARQ e o ORQ confirmam |
| Plano G2 v1.1 (Node) | **71,5 h** (TASKs em horas, com 2º ciclo de CR, sem janela de 24 h nem ARQ) e **78 h** após a conversão `458acb8` (sem a janela de 24 h) | — | Esses totais **não** devem ser somados ao núcleo 46–62 h nem ao completo 75–109 h. Também **não** são mais a base da TASK-0008 (22 h) nem da TASK-0009 (3+1 h), já reestimadas |

Não fecho um novo total da DEM: faltam as reestimativas de **OPS, QA e DOC** (contexto v34).

## 5. (c) Recomendação: o núcleo no caminho crítico e no prazo da DEM

**Recomendação:** o **completo (75–109 h) não entra** no prazo nem no caminho crítico da DEM. Do núcleo (46–62 h), **só a fatia que é pré-requisito e ainda não está contada num entregável da DEM** entra no **caminho crítico do papel** (DoR da primeira atividade). Essas horas **não se somam** ao total das TASKs da DEM. A DEM **não espera** o encerramento da RM-0002 (DEC-CPO-0001). Se essa fatia atrasar o início de uma TASK já desbloqueada por R1 e SDK, o PO **avisa a CPO** (condição das 15:12).

Critérios:

1. **DEC-CPO-0001:** prioridade da DEM permanece Normal; sem prazo definido; a demanda não espera o fim da capacitação; a RM é o recipiente do esforço de formação (Alta).
2. **Validação CPO 15:12:** prazo de acordo; o PO avisa se o núcleo atrasar uma TASK.
3. **Declaração do FS (15:14):** núcleo 12–16 h fora da TASK-0008; mínimo da faixa se o núcleo vier antes; máximo se a curva for durante a execução.
4. **Declaração do CR (15:13):** +1 h somente se o núcleo do CR não estiver concluído; toolchain na box antes do PR.
5. **Sem contagem dupla** (seção 4): não somar núcleo e teto da faixa; não somar núcleo do CR e +1 h; não contar duas vezes SDK, ET-0001 v1.4 ou o spike do CA-07.
6. **Paralelismo:** núcleos de CR e QA podem correr **em paralelo** à TASK-0008 (o G4 e a TASK-0010 vêm depois). O núcleo do FS e a instalação do SDK estão no caminho de partida da 0008. A R1 (ET-0001 v1.4) já foi entregue; falta a confirmação do ARQ (contexto v34).

Aplicação prática (para o plano G2 v1.2, quando as horas restantes chegarem):

- **Fora do prazo da DEM:** todo o complementar; núcleos de DOC (salvo o incremento B, que já é da TASK-0011) e, salvo ressalva da UX-0001 v1.2, o que não for pré-requisito de uma TASK da DEM.
- **No caminho, mas já contados na DEM (não somar de novo):** instalação do SDK (preparação da TASK-0012 / premissa do G4); ET-0001 v1.4 (R1); UX-0001 v1.2, se for tratada como revisão de artefato da demanda.
- **No caminho como habilitação da RM, em linha separada (não entram na soma das TASKs):** núcleo do FS 12–16 h (laboratório `lab-dotnet-angular`) **antes** da TASK-0008, para viabilizar a faixa mínima (32 h; planejamento 40 h); núcleo do CR 6–8 h **durante** a 0008, para evitar o +1 h no G4; núcleo do QA 6–8 h **durante** 0008/0009, antes da 0010; núcleo do ARQ (spike), descontada a sobreposição com o protótipo CA-07 da 0008, se confirmada.
- **Preferência operacional do PO (sujeita à pergunta 1 à CPO):** concluir o núcleo do FS antes de iniciar a TASK-0008, desde que isso não deixe a 0008 parada depois da confirmação da R1 e da instalação do SDK. Se a espera for a atrasar a TASK, avisar a CPO e não embutir o aprendizado no teto de 50 h ao mesmo tempo em que se conta o núcleo.

## 6. (d) Lacunas, riscos e perguntas

### Lacunas

- Reestimativas da TASK-0012 (OPS), da TASK-0010 (QA) e da TASK-0011 (DOC) ainda não chegaram; sem elas não há total novo da DEM.
- Fontes M8/M9 ausentes no núcleo do FS e do CR (e M9/M12 no do QA), diante de ProblemDetails, encerramento gracioso e itens PV do D8.
- UX-0001 v1.2 não confirmada como disponível (parecer FS v2).
- Spike do CA-07: dono e partilha de horas entre ARQ (evidência da RM) e FS (3 h na TASK-0008) não definidos.
- SDK .NET 10 e Angular CLI 22 ainda pendentes na box (OPS; G3 R4; premissa do CR para entrar no G4).
- Prosa do OpenAPI da R1 ainda em ramo, merge à espera do ARQ (contexto v34).
- Horas do plano da RM são estimativas ex-ante do ARQ, sem base histórica (R-1 do próprio plano).

### Riscos (sem números novos)

- Contagem dupla do núcleo com o teto das faixas da DEM, inflando o prazo.
- Iniciar a TASK-0008 sem o núcleo do FS e usar o teto de 50 h **e** ainda lançar 12–16 h na RM.
- Qualidade no G4 se o núcleo do CR não ocorrer (mitigação já cotada: +1 h; permanece o risco R-3 do plano, coberto pelo CR e pela 2ª aprovação do ARQ).
- CA-07 inviável no spike (já previsto pelo ARQ e pelo FS: volta ao PO por MSG-COL; a linha de 3 h é reaberta).
- Toolchain ausente bloqueia evidências da RM (R-2 do plano) e a entrada no G4 (RK-CR6 do CR).

### Perguntas para a CPO

1. Se o núcleo do FS (12–16 h, fora da TASK-0008) for atrasar o início da 0008 **depois** que a confirmação da R1 e o SDK estiverem prontos, a preferência é: **(i)** concluir o núcleo antes e usar a faixa mínima da TASK (32 h; planejamento 40 h), com o aviso já previsto às 15:12; ou **(ii)** iniciar a 0008 imediatamente e aceitar a faixa máxima (50 h) e, se o núcleo do CR também estiver incompleto, o +1 h do 1º ciclo?
2. Confirma o critério de contagem: o esforço de núcleo que **não** é entregável da DEM permanece na **RM-0002** (Alta) e **não entra na soma das TASKs** da DEM (Normal, ainda sem prazo definido na DEC-CPO-0001)? O PO sinaliza apenas o atraso de TASK, sem embutir as 46–62 h no total da demanda.

### Perguntas para o ORQ (para registro; este parecer não envia mensagem)

- No Tarefas.csv e no plano G2 v1.2, registrar a TASK-0008 como 40 h (32–50) **sem** incluir 12–16 h, e anotar a premissa da faixa (mínimo com núcleo prévio; máximo sem).
- Registrar a TASK-0009 como 5 h + 2 h, com +1 h **somente** se o núcleo do CR estiver incompleto; não somar 6–8 h e +1 h.
- Não fechar a soma do G2 v1.2 até OPS, QA e DOC reestimarem; não reutilizar os totais 71,5 h / 78 h do v1.1 em Node como base da 0008/0009.
- Descontar a interseção: instalação do SDK (TASK-0012 / núcleo OPS) e ET-0001 v1.4 (R1 / núcleo AS). Pedir ao ARQ se o spike da evidência da RM é o mesmo protótipo CA-07 das 3 h da TASK-0008.
- Manter a condição da CPO: o PO avisa se o núcleo atrasar uma TASK já desbloqueada.

## 7. O que este parecer não decide

- Prioridade da RM-0002 ou da DEM-2026-001 (CPO).
- Se o G2 se mantém com ajuste ou é refeito (fica para o plano G2 v1.2, com as horas que faltam).
- Aceite formal do PLANO-RM-0002 (dono do conteúdo: ARQ; prioridade já validada pela CPO).
- Alteração de CA, US, REQ, RN, ADR ou DEC-ARQ.

## 8. Histórico de versões

| Versão | Data/hora (America/Sao_Paulo) | Autor | Mudança |
|---|---|---|---|
| 1.0 | 2026-11-26 15:17 | PO | Primeira validação de backlog e prazo, após a validação estratégica da CPO e as reestimativas FS/CR. |
