---
id: CT-0039
titulo: 'Manual: CORS real no navegador — origem permitida e origem não permitida'
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

# CT-0039 — Manual: CORS real no navegador — origem permitida e origem não permitida

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-MAN — Manual da QA (navegador Chrome/Chromium da box e/ou processo real) |
| Rastreio | ADR-0001 v2 D8 item 8 (PV); ET CE-08, RT-10; US-0002 CA-03 (a) |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão aprovada no G4; API em Release e Portal em `ng serve`, processos separados, via `scripts/start-local.sh` (origem configurada em `PORTAL_API_ALLOWED_ORIGIN`).
- Navegador da box (Chrome/Chromium) com DevTools; nenhuma ferramenta nova.

## Passos
1. Abrir a tela na origem configurada: estado Saudável.
2. Abrir o Portal numa origem **não** permitida (forma combinada com OPS/FS, sem ferramenta nova) e carregar a tela.
3. Na aba Network, conferir a resposta da API para essa origem.

## Resultado esperado (oráculo)
- Origem permitida: Saudável.
- Origem não permitida: o navegador bloqueia a leitura; a tela mostra Erro caso (a) com mensagem genérica.
- A API responde 200 **sem** `Access-Control-Allow-Origin` e **sem** 403.

## Evidência exigida
- Capturas de tela e registro da aba Network (ou HAR sanitizado), versão do navegador, hora America/Sao_Paulo, SHA; em `evidencias/` (gitignorado, sanitizado).

## Observações
- Forma de servir a origem não permitida a combinar (lacuna L-PT-05).
