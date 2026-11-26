---
id: CT-0027
titulo: 'Portal: saudável distinguível por ícone, título, selo e borda (parte automatizável)'
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

# CT-0027 — Portal: saudável distinguível por ícone, título, selo e borda (parte automatizável)

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-WEB — Automatizado pelo FS (`ng test`: Vitest + jsdom, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0002 CA-02; UX-0001 D-UX-04 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado).
- Workspace `apps/portal-web`; `ng test --no-watch --coverage` (Vitest + jsdom).
- Respostas HTTP simuladas derivadas dos exemplos do `openapi.yaml` 1.0.0 (PR-04); lógica de apresentação separada do DOM.
- Teste identificado pelo ID deste CT no nome do `describe`/`it`.

## Passos
1. Simular 200 saudável.
2. Inspecionar o DOM do cartão.

## Resultado esperado (oráculo)
- Título "API operacional", selo textual "Saudável", ícone presente (decorativo, `aria-hidden`), classe/estilo de borda do estado saudável.
- Região `aria-live="polite"` com o anúncio do estado; `aria-busy="false"`.

## Evidência exigida
- Saída de `ng test` com o nome do teste e o resultado, na SHA do G4; caminho e SHA do teste revisado pela QA.

## Observações
- Distinção sem cor (renderização visual) não se prova em jsdom: CT-0040.
