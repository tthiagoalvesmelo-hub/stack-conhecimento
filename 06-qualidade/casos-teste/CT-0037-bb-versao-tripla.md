---
id: CT-0037
titulo: 'Black-box: versão da resposta = <Version> do .csproj (= tag, quando houver)'
tipo: ct
versao: 1.0
status: vigente
dono: QA
autores: [QA]
aprovado_por: QA
criado_em: 2026-11-26T15:35-03:00
atualizado_em: 2026-11-26T15:35-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, PT-0001]
substitui: null
substituido_por: null
---

# CT-0037 — Black-box: versão da resposta = <Version> do .csproj (= tag, quando houver)

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-BB — Black-box da QA (processo real em Release, loopback) |
| Rastreio | US-0001 CA-04; ADR-0002 v1.1; ADR-0001 v2 D8 item 1 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão aprovada no G4; API em **Release** subida por `scripts/start-local.sh` em loopback (`PORTAL_API_HOST`/`PORTAL_API_PORT`; valores no `.env` fora do git).
- Ferramenta de requisição já disponível na box (ex.: `curl`); nenhuma ferramenta nova.

## Passos
1. `GET /health` no processo da SHA do G4.
2. Ler `<Version>` do `.csproj` nessa SHA.
3. Se existir tag `portal-api-v<versão>`, executar `scripts/check-version.sh`.

## Resultado esperado (oráculo)
- Resposta == `<Version>` (== tag, quando houver); sem `+` nem hash.

## Evidência exigida
- Transcrição sanitizada das requisições e respostas (método, status, cabeçalhos, corpo), hora America/Sao_Paulo, SHA; em `evidencias/<tipo>/<AAAA-MM-DDTHHMM-03>-<sha7>/` (gitignorado).

## Observações
- No G5 normalmente não há tag (tag é do release/G6); a comparação com a tag fica "quando houver" (CA-04).
