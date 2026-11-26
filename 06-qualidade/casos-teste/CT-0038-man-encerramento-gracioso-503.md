---
id: CT-0038
titulo: 'Manual: encerramento gracioso real responde 503 na janela de drenagem'
tipo: ct
versao: 1.1
status: vigente
dono: QA
autores: [QA]
aprovado_por: QA
criado_em: 2026-11-26T15:35-03:00
atualizado_em: 2026-11-26T15:46-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, PT-0001]
substitui: null
substituido_por: null
---

# CT-0038 — Manual: encerramento gracioso real responde 503 na janela de drenagem

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-MAN — Manual da QA (navegador Chrome da box, base Chromium — esta é a referência quando o texto cita Chromium — e/ou processo real) |
| Rastreio | US-0001 CA-07; ADR-0001 v2 D8 item 10 (PV); ET PS-05, §7.2; ressalva R4 do G3 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão aprovada no G4; API em Release e Portal em `ng serve`, processos separados, via `scripts/start-local.sh` (origem configurada em `PORTAL_API_ALLOWED_ORIGIN`).
- Navegador da box: Google Chrome (base Chromium; esta é a referência quando o texto cita Chromium) com DevTools; nenhuma ferramenta nova.

## Passos
1. Pré-condição adicional: spike R4 concluído e registrado pelo FS/OPS (mecanismo da janela de drenagem).
2. Com a API em Release, iniciar consulta contínua a `GET /health` (intervalo curto).
3. Executar `scripts/stop-local.sh` (SIGTERM; SIGKILL após 10 s — parecer OPS v2.1).
4. Opcional: observar a tela aberta no navegador durante a parada.

## Resultado esperado (oráculo)
- Antes do fechamento do listener, ≥ 1 resposta **503** com `status: "unavailable"`, esquema válido, **sem** `Retry-After` e sem detalhe.
- Depois, conexão recusada (tratada pelo Portal como erro caso (a)).
- Na tela, se observada: estado Erro sem versão/timestamp.

## Evidência exigida
- Capturas de tela e registro da aba Network (ou HAR sanitizado), versão do navegador, hora America/Sao_Paulo, SHA; em `evidencias/` (gitignorado, sanitizado).

## Observações
- **Condicionado ao spike R4.** Se o spike mostrar inviabilidade, o CA-07 volta ao PO (DEC-PO-0008) e este CT fica sem efeito. Duração da janela não definida (lacuna L-PT-04).
- Quando o texto cita Chromium, a referência é o Chrome da box (base Chromium). Não altera o CA.
