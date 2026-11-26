---
id: AGT-ARQ-NOTAS
titulo: "Notas compartilháveis — Ricardo Almeida (Arquiteto Líder)"
tipo: agente
versao: 1.6
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: Thiago Melo
criado_em: 2026-11-26T11:00-03:00
atualizado_em: 2026-11-26T15:19-03:00
revisar_ate: 2027-02-26
relacionados: []
substitui: null
substituido_por: null
---

# Notas compartilháveis — Ricardo Almeida · Arquiteto Líder

Conhecimento da especialidade que outros agentes podem precisar. Informação da memória nativa que influencie outro agente deve ser publicada aqui (ou na área dona) no mesmo dia, com MSG-COL ao afetado.

## 26/11/2026 — DEM-2026-001 [TESTE] · TASK-0003 (ponteiros; a fonte é o ADR)
- Stack base **proposta, NÃO confirmada** (aguarda AH do Thiago via ORQ): ADR-0001 (status proposto). Até a confirmação, nenhum agente assume linguagem, framework ou estrutura; `01-institucional/tecnologias.md` continua "A CONFIRMAR".
- Versão do serviço (SemVer, origem única no manifesto, tag Git): ADR-0002 (proposto).
- Padrão de health-check e diretrizes do contrato `GET /health` (interno, sem autenticação, resposta mínima, timestamp UTC): ADR-0003 (proposto). O OpenAPI é do AS; a validação (G3) é do ARQ.
- Classe de risco da demanda confirmada como R3 (DEC-ARQ-0001, em ramo `doc/DEC-ARQ-0001-risco-r3` aguardando merge do ORQ).
- Regra prática: exposição do `/health` fora da rede interna reabre R3/N3 (contrato público e segurança).

## 26/11/2026 — parecer prévio TASK-0006 (não é G3)
- DEC-ARQ-0002 (vigente): decisões L-01 a L-07 do contrato `GET /health`. Fonte: `02-tecnica/contratos-api/portal-api/DEC-ARQ-0002-detalhes-contrato-health.md`.
- Ramo `doc/ET-0001-contrato-portal-api-health` **não mesclado** (historico.md é área do ORQ; o ramo divergiu da main; o OpenAPI precisa dos ajustes do DEC antes de entrar em main). G3 = TASK-0007, só após AH-0001.
- CONF-0001 (R2 nas US/REQ × R3 confirmado): dono PO; ARQ apenas toma nota.

## 26/11/2026 — parecer G2 e substituto de CI
- PARECER-ARQ-DEM-2026-001-G2 v1.0: `07-agentes/07-arq/parecer-tecnico-DEM-2026-001-g2.md`.
- DEC-ARQ-0003 (L-CR1, substituto local do CI verde) e DEC-ARQ-0004 (L-CR3, ESLint 10, condicionada ao ADR-0001).
- OpenAPI portal-api 1.0.0 **proposto** na main (merge cf660fb). Não é o G3.

## 26/11/2026 — horas G2, SAST, p95 e L-12 prévia
- Conversão das estimativas escala 1 para horas e parecer prévio L-12 / teste de tela: `07-agentes/07-arq/parecer-horas-g2-ops-fs-DEM-2026-001.md`.
- DEC-ARQ-0005: recorte SAST desta demanda (npm audit + ESLint recommended + testes dirigidos). DEC-ARQ-0006: p95 por script Node embutido, sem dependência nova. Ambas condicionadas ao ADR-0001.

## 26/11/2026 — AH-0003: stack C#/.NET + Angular (ponteiros; a fonte é o ADR)
- **AH-0003 aprovada** (Thiago, 14:54): APIs de backend do Portal Web em C#/.NET LTS (**.NET 10**, ASP.NET Core Minimal APIs) e front-end em **Angular 22.x** (estável mais recente: 22.3.0). AH-0001 (Node/Fastify) substituída. Fonte: `02-tecnica/adr/ADR-0001-stack-base-portal-api-e-web.md` v2.0 (aceito) e `01-institucional/tecnologias.md` v1.1.
- ADR-0002 v1.1 (versão no `<Version>` do `.csproj`, `IncludeSourceRevisionInInformationalVersion=false`) e ADR-0003 v1.1: propostos até o G3. OpenAPI 1.0.0 mantém-se.
- DEC-ARQ-0007..0010 substituem DEC-ARQ-0003..0006 (verify-local, lint, SAST/SCA, p95). Análise de impacto: `07-agentes/07-arq/analise-impacto-troca-stack-DEM-2026-001.md`.
- Regra prática: nenhum comportamento do contrato pode depender de `ASPNETCORE_ENVIRONMENT`; ganchos de teste só por `WebApplicationFactory`.

## 26/11/2026 — R1 do G3 fechada; RM-0002 (CPO); premissas (a)/(b)
- **R1 fechada** (parecer G3 v1.1): ET-0001 v1.4 aprovada tecnicamente pelo ARQ (já na main, 9b3dc1b); prosa do OpenAPI 1.0.0 correta (ramo `doc/TASK-0006-R1-openapi-prosa`, 8494060 — o ORQ faz o merge). R2..R5 abertas (FS/QA/OPS). Fonte: `07-agentes/07-arq/parecer-tecnico-DEM-2026-001-g3.md` v1.1.
- **PLANO-RM-0002:** a CPO validou em 26/11 15:12 (DEC-CPO-0001, sem DEC nova): MOB, PMM e AN fora; **DBA e SUP entram por gatilho** — antes da primeira atividade de cada um numa demanda .NET/Angular, o ARQ define um núcleo curto para o papel. Prazo e forma (leitura + exercício + evidência; Parcial sem evidência) aceitos; o PO avisa a CPO se o núcleo atrasar uma TASK. Falta o PO validar o impacto em backlog e prazo.
- **Premissas da diretriz AH-0003, vigentes até o Thiago responder** (dúvidas levadas pela CPO): **(a)** "última linguagem do Angular" = Angular **22.x estável** mais recente (hoje 22.3.0), acompanhando o suporte; **(b)** C#/.NET aplica-se **só às APIs do Portal Web** (demais backends permanecem A CONFIRMAR). Se (b) ampliar, a CPO abre DEC-CPO-0002. A DEM-2026-001 não espera essa resposta.
