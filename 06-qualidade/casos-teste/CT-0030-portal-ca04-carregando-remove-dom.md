---
id: CT-0030
titulo: 'Portal: carregando remove valores anteriores do DOM'
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

# CT-0030 — Portal: carregando remove valores anteriores do DOM

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-WEB — Automatizado pelo FS (`ng test`: Vitest + jsdom, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0002 CA-04; UX-0001 D-UX-02, D-UX-07 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado).
- Workspace `apps/portal-web`; `ng test --no-watch --coverage` (Vitest + jsdom).
- Respostas HTTP simuladas derivadas dos exemplos do `openapi.yaml` 1.0.0 (PR-04); lógica de apresentação separada do DOM.
- Teste identificado pelo ID deste CT no nome do `describe`/`it`.

## Passos
1. Estado inicial ao abrir (resposta pendente).
2. A partir do estado saudável, acionar "Atualizar status" com nova resposta pendente.
3. Acionar o botão de novo durante o carregamento.

## Resultado esperado (oráculo)
- Estado inicial = Carregando (nunca Saudável/Erro de partida).
- Durante o carregamento, a versão e o timestamp anteriores **não existem no DOM** (não apenas ocultos); sem valores parciais; `aria-busy="true"`.
- Botão com `aria-disabled="true"`; nova ativação ignorada (nenhuma requisição extra).

## Evidência exigida
- Saída de `ng test` com o nome do teste e o resultado, na SHA do G4; caminho e SHA do teste revisado pela QA.
