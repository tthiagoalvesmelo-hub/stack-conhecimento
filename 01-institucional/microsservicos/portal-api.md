---
id: INST-MSVC-PORTAL-API
titulo: "Catálogo — portal-api"
tipo: microsservico
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T16:00-03:00
atualizado_em: 2026-11-26T16:00-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0008, ADR-0001, ADR-0002, ADR-0003, DEC-ARQ-0015, ET-0001, US-0001, openapi.yaml]
substitui: null
substituido_por: null
---

# portal-api

> [TESTE] Primeira entrada do catálogo `01-institucional/microsservicos/` (DEC-ARQ-0015). Fase de testes internos; não é produção. **Proibido** neste arquivo: *host*, IP, porta real, credencial, variável de ambiente com valor, dado pessoal ou dado real.

| Campo | Valor |
|---|---|
| **Nome** | `portal-api` |
| **Finalidade** | API de backend do Portal Web. Nesta demanda (DEM-2026-001), expõe somente o health-check `GET /health` (e `HEAD /health`), para a tela de status do Portal. |
| **Dono técnico** | ARQ (catálogo e contrato). Implementação: FS (TASK-0008). Operação local: OPS (scripts `start-local`/`stop-local`, quando houver). |
| **Stack** | C# / **.NET 10 LTS**, ASP.NET Core Minimal APIs, Kestrel — ADR-0001 v2.0 (aceito; AH-0003). |
| **Repositório de código** | https://github.com/tthiagoalvesmelo-hub/portal (público). Ramo em curso: `feat/TASK-0008-health-portal`. O contrato **não** vive neste repositório. |
| **Contrato** | OpenAPI 3.1, `info.version` **1.0.0**, `status-documento: aprovado`. Fonte única: `02-tecnica/contratos-api/portal-api/openapi.yaml` no repositório `stack-conhecimento`. SHA de referência inicial: `e34e6b9` (DEC-ARQ-0015). |
| **Versionamento do serviço** | SemVer 2.0.0 (`MAJOR.MINOR.PATCH`, sem metadados `+…`). Origem única: `<Version>` no `.csproj` do serviço, com `IncludeSourceRevisionInInformationalVersion=false`. Tag Git `portal-api-v<versão>`. Série atual de teste: `0.1.0`. ADR-0002 v1.1 (aceito). A versão do contrato (`info.version`) é independente da versão do serviço. |
| **Endpoints** | `GET /health` e `HEAD /health`. Respostas de contrato: 200, 503, 405, 500. O preflight CORS é tratado por middleware e **não** é endpoint (DEC-ARQ-0012, PR #4). |
| **Dependências** | Nenhuma (sem banco, sem mensageria, sem serviço externo). O `portal-web` é consumidor, não dependência. |
| **Classificação** | Interno; **sem autenticação**. Exposição fora da rede interna reabre R3/N3 (ADR-0003 v1.1; RN-0001). |
| **Status** | Em desenvolvimento (DEM-2026-001 / TASK-0008). Esqueleto D6 no ramo citado (HEAD `2240056`); implementação das US em curso. Sem release e sem ambiente de produção. |

## Histórico
| Versão | Data/hora (America/Sao_Paulo) | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 16:00 | ARQ | Criação (DEC-ARQ-0015; pedido d do FS) |
