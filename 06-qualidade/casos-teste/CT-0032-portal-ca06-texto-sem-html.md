---
id: CT-0032
titulo: 'Portal: valores só como texto e sem dados sensíveis em nenhum estado'
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

# CT-0032 — Portal: valores só como texto e sem dados sensíveis em nenhum estado

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-WEB — Automatizado pelo FS (`ng test`: Vitest + jsdom, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0002 CA-06; RN-0001; REQ-0004; ET §5 item 5 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado).
- Workspace `apps/portal-web`; `ng test --no-watch --coverage` (Vitest + jsdom).
- Respostas HTTP simuladas derivadas dos exemplos do `openapi.yaml` 1.0.0 (PR-04); lógica de apresentação separada do DOM.
- Teste identificado pelo ID deste CT no nome do `describe`/`it`.

## Passos
1. Na lógica de apresentação, renderizar valor contendo marcação (ex.: `<img src=x onerror=alert(1)>`).
2. Simular 500 com corpo contendo texto técnico fictício (caminho, stack).
3. Inspecionar os três estados.

## Resultado esperado (oráculo)
- A marcação aparece como texto literal; nenhum elemento é criado.
- Mensagem de erro é constante do front, nunca derivada do corpo de erro.
- Status, versão e timestamp só no estado saudável; nenhum dado sensível.

## Evidência exigida
- Saída de `ng test` com o nome do teste e o resultado, na SHA do G4; caminho e SHA do teste revisado pela QA.
