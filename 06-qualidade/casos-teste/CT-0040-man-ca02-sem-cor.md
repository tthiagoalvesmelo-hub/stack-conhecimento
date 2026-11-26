---
id: CT-0040
titulo: 'Manual: estados distinguíveis sem depender de cor'
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

# CT-0040 — Manual: estados distinguíveis sem depender de cor

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-MAN — Manual da QA (navegador Chrome da box, base Chromium — esta é a referência quando o texto cita Chromium — e/ou processo real) |
| Rastreio | US-0002 CA-02; UX-0001 D-UX-04; WCAG 1.4.1 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão aprovada no G4; API em Release e Portal em `ng serve`, processos separados, via `scripts/start-local.sh` (origem configurada em `PORTAL_API_ALLOWED_ORIGIN`).
- Navegador da box: Google Chrome (base Chromium; esta é a referência quando o texto cita Chromium) com DevTools; nenhuma ferramenta nova.

## Passos
1. Exibir os estados Saudável, Carregando e Erro (este com a API parada).
2. Em cada um, ativar no DevTools a emulação sem cor (escala de cinza/acromatopsia) e capturar a tela.
3. Conferir a árvore de acessibilidade no DevTools.

## Resultado esperado (oráculo)
- Sem cor, o estado saudável é identificável por ícone ✓, título "API operacional", selo "Saudável" e borda sólida; os três estados são distinguíveis entre si.
- Árvore de acessibilidade com o título e o selo como texto.

## Evidência exigida
- Capturas de tela e registro da aba Network (ou HAR sanitizado), versão do navegador, hora America/Sao_Paulo, SHA; em `evidencias/` (gitignorado, sanitizado).

## Observações
- Leitor de tela real, outros navegadores e zoom 400% (UX-0001) estão **fora do escopo desta demanda**, por decisão do PO (L-PT-06 fechada; o critério são os 15 CA, DEC-PO-0008). Não é falha. Os CT manuais usam o Chrome da box (base Chromium).
