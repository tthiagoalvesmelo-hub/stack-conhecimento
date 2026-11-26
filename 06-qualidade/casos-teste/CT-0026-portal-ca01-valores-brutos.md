---
id: CT-0026
titulo: 'Portal: estado saudável exibe os valores brutos da mesma consulta'
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

# CT-0026 — Portal: estado saudável exibe os valores brutos da mesma consulta

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-WEB — Automatizado pelo FS (`ng test`: Vitest + jsdom, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0002 CA-01; UX-0001 D-UX-05, D-UX-08; ET §5 itens 3 e 7 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado).
- Workspace `apps/portal-web`; `ng test --no-watch --coverage` (Vitest + jsdom).
- Respostas HTTP simuladas derivadas dos exemplos do `openapi.yaml` 1.0.0 (PR-04); lógica de apresentação separada do DOM.
- Teste identificado pelo ID deste CT no nome do `describe`/`it`.

## Passos
1. Simular 200 com o exemplo do contrato (`status: ok`, `version: 0.1.0`, `timestamp` UTC) **mais** um campo desconhecido.
2. Abrir o componente.

## Resultado esperado (oráculo)
- Status, versão e timestamp UTC exibidos com valor **bruto** igual ao da resposta simulada.
- Formatação em America/Sao_Paulo (`dd/MM/aaaa HH:mm:ss` + legenda) apenas **adicional**.
- Campo desconhecido ignorado (leitor tolerante).

## Evidência exigida
- Saída de `ng test` com o nome do teste e o resultado, na SHA do G4; caminho e SHA do teste revisado pela QA.
