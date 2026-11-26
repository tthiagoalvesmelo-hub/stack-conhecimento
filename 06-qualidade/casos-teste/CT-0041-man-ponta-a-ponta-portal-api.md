---
id: CT-0041
titulo: 'Manual: ponta a ponta Portal↔API (CA-01, CA-03, CA-04, CA-05, CA-06)'
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

# CT-0041 — Manual: ponta a ponta Portal↔API (CA-01, CA-03, CA-04, CA-05, CA-06)

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | QA-MAN — Manual da QA (navegador Chrome da box, base Chromium — esta é a referência quando o texto cita Chromium — e/ou processo real) |
| Rastreio | US-0002 CA-01, CA-03, CA-04, CA-05, CA-06 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão aprovada no G4; API em Release e Portal em `ng serve`, processos separados, via `scripts/start-local.sh` (origem configurada em `PORTAL_API_ALLOWED_ORIGIN`).
- Navegador da box: Google Chrome (base Chromium; esta é a referência quando o texto cita Chromium) com DevTools; nenhuma ferramenta nova.

## Passos
1. Abrir a tela; comparar os valores exibidos com o corpo da mesma requisição na aba Network.
2. Com limitação de rede no DevTools, acionar "Atualizar status" e observar Carregando sem valores antigos (inspecionar o DOM).
3. Parar a API (`stop-local.sh`) e atualizar: Erro.
4. Subir a API e atualizar: Saudável (recuperação).
5. Inspecionar o DOM nos três estados.

## Resultado esperado (oráculo)
- Valores brutos iguais à mesma resposta; formatação local adicional.
- Carregando sem valores anteriores no DOM.
- Erro genérico sem detalhe técnico; recuperação para Saudável.
- Nenhum dado além de status/versão/timestamp no saudável e mensagens genéricas.

## Evidência exigida
- Capturas de tela e registro da aba Network (ou HAR sanitizado), versão do navegador, hora America/Sao_Paulo, SHA; em `evidencias/` (gitignorado, sanitizado).

## Observações
- Quando o texto cita Chromium, a referência é o Chrome da box (base Chromium). Não altera o CA.
