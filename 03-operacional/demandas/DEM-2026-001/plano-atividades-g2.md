---
id: PLANO-DEM-2026-001-G2
titulo: "Plano de atividades para o G2 — DEM-2026-001 [TESTE]"
tipo: plano
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:50-03:00
atualizado_em: 2026-11-26T12:50-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, RM-0001, G1, G2, TASK-0003, TASK-0004, TASK-0005, TASK-0006, TASK-0007, TASK-0008, TASK-0009, TASK-0010, TASK-0011, TASK-0012, US-0001, US-0002, REQ-0001, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0001, DEC-PO-0004, DEC-PO-0005, DEC-PO-0006, DEC-ARQ-0001, DEC-ARQ-0002, DEC-AS-0001, DEC-AS-0002, DEC-AS-0003, ADR-0001, ADR-0002, ADR-0003, AH-0001, EF-0001, ET-0001]
substitui: null
substituido_por: null
---

# Plano de atividades para o G2 — DEM-2026-001 [TESTE]

> Fase de testes internos; nada vai à produção. Fluxo 01, etapa C, estado "Em planejamento" (contexto.yaml v10). G1 registrado em 26/11/2026 12:38 (America/Sao_Paulo) como **Aprovado com observações** (commit `b083eef`).
> Este documento **não** altera estado, etapa, gates, `contexto.yaml`, `aprovacoes.md` nem `Tarefas.csv` (só o ORQ). **Status: em-revisao.** Não é a decisão do G2: faltam estimativas dos executores e o parecer técnico consolidado do ARQ (TASK-0003 Parcial).
> **Estimativas:** nenhuma foi inventada. Constam como "a estimar pelo responsável". A estimativa é de quem executa; a decisão técnica é do ARQ.

## 1. Premissas e restrições (G1 e R3)

Condições do G1 (aprovacoes.md), que este plano respeita:

1. Formatos, caminhos 503/405/500, tempo limite de 5 s e tela sem login dependem dos ADR-0002/0003 **propostos**. Se mudarem no G3, o PO reabre os CA afetados.
2. Stack e implementação (TASK-0008 e TASK-0012) **só após AH-0001** válida do Thiago. O G2 pode ser decidido antes da AH-0001; o G2 **não** substitui a AH.
3. A proposta técnica do ARQ (TASK-0003) segue **Parcial**.

Classe de risco **R3** (DEC-ARQ-0001) — requisitos mínimos a cumprir no plano, sem gravar gates:

- Testes de **segurança** e de **desempenho**, além dos demais tipos aplicáveis (unidade, integração, funcionais, regressão, contrato).
- **2ª aprovação do ARQ no G4** (além do parecer do CR; revisor ≠ autor).
- Janela de **observação de 24 h** (como aplicar no teste local fica a cargo do OPS no parecer de planejamento).
- Plano de **rollback ensaiado no G6**.
- AH de arquitetura já solicitada (AH-0001). Sem alteração de banco: DBA não é acionado (L9 fechada). Sem Mobile.

Escopo funcional vigente (commit `babb9fe`): US-0001 e US-0002, REQ-0001..0004, RN-0001 e RN-0002 — **v1.2, vigente**, com a ressalva (1) do G1. Público da tela confirmado pela CPO (DEC-PO-0002): operador/equipe técnica interna. Protótipo UX v1.0 aprovado com ressalvas (DEC-PO-0005).

## 2. Fontes consultadas (IDs e versões)

- contexto.yaml v10 (26/11 12:48); aprovacoes.md (G1); Tarefas.csv (espelho); historico.md (append-only, até o G1).
- US-0001/US-0002, REQ-0001..0004, RN-0001/0002 v1.2 vigente (`babb9fe`); analise-po-task-0002.md v1.2; validacao-po-prototipo-task-0004.md / DEC-PO-0005.
- ADR-0001/0002/0003 v1.0 **propostos**; DEC-ARQ-0001 (R3); DEC-ARQ-0002 v1.0 vigente (parecer prévio L-01..L-07; **não é o G3**).
- EF-0001 e ET-0001 v1.1 em-revisao; OpenAPI 1.0.0 proposto no ramo `doc/ET-0001-contrato-portal-api-health` (commit `2b9fa2e`, **não mesclado**; ajustes do DEC-ARQ-0002 pendentes da AS).
- DEC-AS-0001 (timeout 5 s, sem retry), DEC-AS-0002 (tolerância ±5 s), DEC-AS-0003 (regex; version a apertar conforme DEC-ARQ-0002 L-07).
- PROMPT do PO v1.0: Fluxo 01 etapa C; G2 = atividades com ID, responsável, dependências, estimativa e critérios de conclusão, e decisões arquiteturais consolidadas; DoR (objetivo, descrição, CA, dependências, contexto técnico, responsáveis, riscos, estimativa do executor).

## 3. Situação das TASK já existentes

Não crio TASK novas (isso é do ORQ). Uso as TASK-0003 e 0007–0012 já registradas.

| TASK | Responsável | Estado (Tarefas.csv / contexto v10) | Papel neste plano |
|---|---|---|---|
| TASK-0001 | CPO | Concluída | G0 — encerrada |
| TASK-0002 | PO | Concluída | Análise inicial — encerrada |
| TASK-0003 | ARQ | **Parcial** | Análise técnica / consolidação da proposta (insumo obrigatório do G2) |
| TASK-0004 | UX | Concluída | Protótipo validado com ressalvas (DEC-PO-0005) |
| TASK-0005 | QA | Concluída | Testabilidade pré-G1, ajustes respondidos (DEC-PO-0006) |
| TASK-0006 | AS | Concluída | EF/ET v1.1; resta trabalho residual no OpenAPI (DEC-ARQ-0002), pré-requisito da TASK-0007 |
| TASK-0007 | ARQ | Aguardando dependências | Aprovação do contrato (G3) |
| TASK-0008 | FS | Aguardando dependências; **bloqueio AH-0001** | Implementação API + tela |
| TASK-0009 | CR | Aguardando dependências | Code Review (G4) + 2ª aprovação ARQ (R3) |
| TASK-0010 | QA | Aguardando dependências | Plano de testes, execução e PQ (G5) |
| TASK-0011 | DOC | Aguardando dependências | Documentação (paralela à TASK-0010) |
| TASK-0012 | OPS | Aguardando dependências; **bloqueio AH-0001** | Execução local, smoke e rollback (G6/G7) |

## 4. Trabalho residual (não é TASK nova)

Antes do G3 (TASK-0007), a AS aplica no OpenAPI os ajustes 1–6 do DEC-ARQ-0002 (L-01..L-07), faz rebase na `main` atual e retira `historico.md` do ramo `doc/ET-0001-contrato-portal-api-health`. O ARQ só então avalia o merge `--no-ff` do contrato **proposto** (isso **não** é o G3). O G3 permanece após a AH-0001, com ADR aceitos ou condição explícita do ARQ.

A EF-0001/ET-0001 v1.1 ainda estão em-revisao e ancoradas, em parte, à US/REQ v1.0; a AS deve alinhar o rastreio aos CA v1.2 (CA-07/08/09, RE-02, oráculos do CA-04/CA-06) na revisão que anteceder o G3. Esforço desse residual: a estimar pela AS, se o ORQ despachar (não é parecer de nova implementação).

## 5. Plano por atividade (a executar)

Critérios abaixo são os de **conclusão da TASK**, verificáveis e ligados aos CA/REQ vigentes. Estimativa: **a estimar pelo responsável**.

### TASK-0003 — Análise técnica (fechamento) · ARQ (Ricardo)
- **Objetivo:** concluir a proposta técnica iniciada na TASK-0003 (Parcial): consolidar decisões arquiteturais, sequência de implementação e confirmação da classe R3 no G2.
- **Critérios de conclusão:** parecer técnico escrito (MSG-RET) que (a) confirma ou atualiza ADR-0001/0002/0003 e o enquadramento R3 (DEC-ARQ-0001); (b) declara a sequência e o paralelismo técnicos (incluindo G3 → implementação e o papel da 2ª aprovação no G4); (c) lista riscos e mitigações (RK-1..RK-3 e cadeia npm, se a AH-0001 aceitar a stack); (d) explicita o que permanece pendente da AH-0001. Não é o G3.
- **Dependências:** G1 (ok); AH-0001 não é pré-requisito deste parecer, mas a aceitação formal dos ADR de stack depende dela.
- **Estimativa:** a estimar pelo ARQ.
- **Bloqueio:** nenhum para emitir o parecer; a stack permanece N3 até a AH-0001.

### TASK-0007 — Aprovação do contrato (G3) · ARQ (Ricardo)
- **Objetivo:** aprovar o contrato interno de `GET /health` (OpenAPI + ET) antes da implementação dependente (PR-04 / sequência obrigatória G3 → código).
- **Critérios de conclusão:** contrato alinhado a US-0001 CA-01..CA-09, REQ-0001, REQ-0004, RN-0001, ADR-0003 (quando aceito) e DEC-ARQ-0002; exemplos de 200, 503, 405 e 500; `additionalProperties: false`; sem dado sensível; CORS só da origem do Portal; parecer de G3 do ARQ registrado. Sem persistência: parecer do DBA = N/A, com justificativa. O merge do ramo do contrato proposto, sozinho, não conclui esta TASK.
- **Dependências:** TASK-0006 (concluída) + residual da AS (OpenAPI ajustado e ramo limpo) + **AH-0001** (G3 só após AH-0001, já registrado pelo ORQ/ARQ).
- **Estimativa:** a estimar pelo ARQ.
- **Bloqueio:** AH-0001; OpenAPI ainda desatualizado em relação ao DEC-ARQ-0002; ramo do contrato não mesclável no estado atual.

### TASK-0008 — Implementação API `GET /health` + tela · FS (Lucas)
- **Objetivo:** implementar o provedor e o consumidor, com testes unitários, conforme US/REQ/RN v1.2, contrato aprovado (G3), protótipo/spec validados (DEC-PO-0005) e diretrizes do ARQ.
- **Critérios de conclusão:** PR com IDs (DEM/TASK/US) e trailer de agente; nota de análise (itens 1–9) anexada; US-0001 CA-01..CA-09 atendidos no código da API (200 com `status`/`version`/`timestamp`, 503 de contrato, 405 com `Allow`, 500 padronizado, somente leitura, sem dado sensível); US-0002 CA-01..CA-06 atendidos na tela (valores brutos + UTC no saudável; erro genérico; 503 **sem** exibir versão/timestamp — RE-02; carregando remove valores do DOM; recuperação pelo botão); testes unitários do serviço; nenhum segredo no repositório; implementação só na stack aprovada pela AH-0001. Fora: polling, Mobile, persistência.
- **Dependências (Tarefas.csv):** G2; G3; TASK-0004. **Bloqueio adicional:** AH-0001. O consumidor pode usar mocks do contrato **após** o G3 (PR-04), em paralelo com refinamentos do provedor, nunca antes do G3.
- **Estimativa:** a estimar pelo FS.
- **DoR pendente:** estimativa; contexto técnico completo (contrato G3 + stack aceita). Até lá a TASK não entra em desenvolvimento.

### TASK-0009 — Code Review (G4) · CR (Eduardo) + 2ª aprovação ARQ
- **Objetivo:** revisar o código da TASK-0008 (revisor ≠ autor) e, por ser R3, obter a 2ª aprovação do ARQ.
- **Critérios de conclusão:** parecer CR-nnnn (Aprovado ou Com observações); 2ª aprovação explícita do ARQ no mesmo G4; verificação de IDs no PR, ausência de segredos, aderência ao contrato aprovado e aos padrões vigentes; observações tratadas ou registradas como TD. Só então a versão segue ao QA (G5).
- **Dependências:** TASK-0008 (PR da versão candidata).
- **Estimativa:** a estimar pelo CR (e o ARQ indica disponibilidade para a 2ª aprovação).
- **DoR pendente:** estimativa.

### TASK-0010 — Plano de testes, testes e PQ (G5) · QA (Fernanda)
- **Objetivo:** planejar e executar os testes da demanda na versão aprovada no G4, com rastreio CA → CT, e emitir o PQ.
- **Critérios de conclusão:** PT/CT cobrindo 100% dos CA vigentes (US-0001 CA-01..CA-09 e US-0002 CA-01..CA-06); testes de contrato (200, 503, 405, 500, corpo inválido, timeout); testes dirigidos de **segurança** (RN-0001, REQ-0004, CA-05/CA-06, denylist); teste de **desempenho** com o alvo indicativo p95 ≤ 100 ms em execução local (não é SLO; calibrar com OPS); regressão aplicável (suíte inicial = esta entrega); PQ-nnnn favorável (ou favorável com ressalvas aceitas pelo PO/ARQ), na versão do G4. Tempo limite do cliente = 5 s sem retry (DEC-AS-0001); tolerância do timestamp ±5 s (DEC-AS-0002).
- **Dependências (Tarefas.csv):** TASK-0005 (concluída); TASK-0009 (G4).
- **Estimativa:** a estimar pelo QA.
- **DoR pendente:** estimativa; ambiente de execução a confirmar pelo OPS.

### TASK-0011 — Documentação da versão · DOC (Beatriz)
- **Objetivo:** preparar a documentação do endpoint e da tela (G6 pronta) e publicá-la após a verificação da implantação (G8), em paralelo aos testes (PR-06).
- **Critérios de conclusão:** documentação versionada do contrato `GET /health` e da tela de status, alinhada a US/REQ v1.2 e ao contrato aprovado no G3; release notes da versão candidata; nenhum segredo; publicação final só após o G7 aplicável. Residual já na alçada da DOC, se couber nesta TASK ou em nota: fechamento formal do CONF-0001 (lado PO já resolvido); L-UX-01 (prefixo de ID de protótipo); L-09 (modelos de EF/ET/contrato e INDEX), se o DOC julgar no mesmo pacote — caso contrário, permanece pendência à parte, sem bloquear o G6 desta demanda.
- **Dependências (Tarefas.csv):** TASK-0008; paralela à TASK-0010.
- **Estimativa:** a estimar pelo DOC.
- **DoR pendente:** estimativa; recorte exato do residual CONF/L-UX-01/L-09.

### TASK-0012 — Execução local, smoke test e rollback · OPS (Diego)
- **Objetivo:** viabilitar a execução local de teste em `/workspace/projetos/`, validar ambiente e rollback no G6 e verificar a “implantação” local no G7 (não há produção neste teste).
- **Critérios de conclusão:** registro do ambiente local (como instalar, subir API e Portal em processos separados, variáveis só por **nome**, valores fora do git); origem do Portal e `PORTAL_API_ALLOWED_ORIGIN` definidos no ambiente (DEC-ARQ-0002 L-06; o ARQ não inventou porta); smoke test da versão candidata (pelo menos o caminho 200 e a tela saudável/erro); **plano de rollback ensaiado no G6** (passo a passo executado uma vez, com tempo estimado); proposta de **observação de 24 h** compatível com o teste local (o OPS define como evidenciar; o PO não inventa o procedimento); Suporte informado se houver impacto operacional relevante (nesta fase, provavelmente N/A, com justificativa). Sem pipeline e sem custo. Débitos de ausência de CI/ambientes dev-hml só com TD se o ARQ aceitar.
- **Dependências (Tarefas.csv):** G5; **bloqueio AH-0001**. Proposta de sequência (a confirmar por OPS/ARQ): a *preparação* do ambiente local pode começar após a AH-0001, em paralelo à TASK-0008; a validação formal (smoke, rollback ensaiado, observação) permanece após o G5, no G6/G7. Não alterei o Tarefas.csv.
- **Estimativa:** a estimar pelo OPS (preparação e janela de G6/G7, em separado se útil).
- **DoR pendente:** estimativa; procedimento de observação de 24 h; valores de ambiente (não gravar segredos).

### Atividades do PO (não são TASK novas)
- **G6 — Pré-aceite funcional:** confirmar que os CA vigentes foram evidenciados no PQ, com a ressalva (1) do G1 se o contrato no G3 tiver mudado.
- **G8 — Confirmação e encerramento:** critérios confirmados; documentação publicada; informar a CPO.

## 6. Sequência e paralelismo

```
[concluídas] TASK-0001..0002, 0004, 0005, 0006
[parcial]    TASK-0003 ── parecer consolidado (insumo do G2)

G2 (PO) ──────────────────────────────────────────────┐
     (pode ser decidido antes da AH-0001)             │
                                                      ▼
AH-0001 (Thiago, já solicitada) ──┬── residual AS (OpenAPI + DEC-ARQ-0002)
                                  └── TASK-0007 (G3)        [após AH + residual]
                                         │
                                         ▼
                                  TASK-0008 (FS)            [após G2, G3, AH-0001, TASK-0004]
                                         │
                    ┌────────────────────┼────────────────────┐
                    ▼                    ▼                    ▼
              TASK-0009 (CR+ARQ, G4)  (prep. OPS, se AH ok)  TASK-0011 inicia insumos
                    ▼
              TASK-0010 (QA, G5)  ∥  TASK-0011 (DOC, PR-06)
                    ▼
              G6 (PO pré-aceite + OPS rollback ensaiado + DOC pronta)
                    ▼
              TASK-0012 formal (smoke / G7 local) + observação 24 h
                    ▼
              G8 (PO) e informe à CPO
```

Regras: G1 → planejamento (esta etapa) → G3 → implementação dependente; implementação → G4 → G5; G5 + G6 → verificação local (G7) → G8. Paralelismo: TASK-0011 ∥ TASK-0010; preparação do OPS ∥ TASK-0008 após AH-0001, se o OPS confirmar. Incidente P0 não se aplica (nada em produção).

## 7. Matriz resumida (DoR do G2)

| TASK | Responsável | Dependências | Bloqueios | Estimativa | Critérios (resumo) | DoR |
|---|---|---|---|---|---|---|
| 0003 | ARQ | G1 | — (AH-0001 para aceitar stack) | a estimar pelo ARQ | Parecer técnico consolidado + sequência + R3 | Incompleta (Parcial) |
| 0007 | ARQ | 0006 + residual AS + AH-0001 | AH-0001; OpenAPI desatualizado | a estimar pelo ARQ | Contrato aprovado (G3) | Incompleta |
| 0008 | FS | G2; G3; 0004 | **AH-0001** | a estimar pelo FS | PR + CA US-0001/0002 + unitários | Incompleta (est., G3, AH) |
| 0009 | CR (+ ARQ) | 0008 | — | a estimar pelo CR | CR-nnnn + 2ª aprovação ARQ (R3) | Incompleta (est.) |
| 0010 | QA | 0005; 0009 | — | a estimar pelo QA | PT/CT 100% CA; segurança; desempenho; PQ | Incompleta (est., ambiente) |
| 0011 | DOC | 0008 (∥ 0010) | — | a estimar pelo DOC | Docs da versão (G6 pronta; G8 publicada) | Incompleta (est.) |
| 0012 | OPS | G5 (prep. proposta após AH) | **AH-0001** | a estimar pelo OPS | Ambiente local; smoke; rollback ensaiado G6; observação 24 h | Incompleta (est., AH) |

## 8. O que falta para decidir o G2

O G2 exige (PROMPT): atividades com ID, responsável, dependências, **estimativa** e critérios de conclusão; **decisões arquiteturais consolidadas**.

Já há: IDs e responsáveis (ORQ); dependências e bloqueios (este plano, alinhados ao Tarefas.csv); critérios de conclusão ligados aos CA/REQ v1.2; requisitos R3 listados; sequência proposta.

Ainda falta:

1. **Estimativas** de TASK-0003 (fechamento), 0007, 0008, 0009, 0010, 0011 e 0012, dadas pelos responsáveis — o ORQ as grava em Tarefas.csv. Sem estimativa do executor, o item da DoR “Estimativa, quando aplicável” não fecha.
2. **Parecer técnico consolidado do ARQ** (fechamento da TASK-0003 / insumo explícito de G2): sequência confirmada, riscos, o que a AH-0001 ainda trava, e se as decisões já registradas (DEC-ARQ-0001, DEC-ARQ-0002, ADR propostos) bastam para aprovar o planejamento com condição, ou se o G2 deve esperar algo mais.
3. **Pareceres de planejamento** (esforço, riscos da especialidade, necessidades de colaboração, confirmação dos critérios e da sequência) de **FS, OPS, QA, CR e DOC**. O residual da AS (OpenAPI) pode ser estimado no mesmo despacho, se o ORQ incluir a AS.
4. A AH-0001 **não** é pré-requisito da decisão do G2, mas deve constar como condição: TASK-0008 e TASK-0012 não entram em execução sem ela (já é a condição 2 do G1).

Quando esses pareceres voltarem, o PO decide o G2 (Aprovado, Aprovado com observações ou Reprovado) e pede ao ORQ que registre. Até lá, este plano permanece em-revisao.

## 9. Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 12:50 (America/Sao_Paulo) | PO | Primeira versão para despacho dos pareceres de planejamento (etapa C, pré-G2) |
