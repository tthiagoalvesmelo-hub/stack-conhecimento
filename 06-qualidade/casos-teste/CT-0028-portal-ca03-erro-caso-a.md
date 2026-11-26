---
id: CT-0028
titulo: 'Portal: erro caso (a) — rede, timeout de 5 s, HTTP inesperado, corpo inválido'
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

# CT-0028 — Portal: erro caso (a) — rede, timeout de 5 s, HTTP inesperado, corpo inválido

> [TESTE] DEM-2026-001 · TASK-0010 · PT-0001 v1.0 · risco R3. **Especificação; nada executado.** Execução só após o G4, na versão aprovada.

| Campo | Valor |
|---|---|
| Tipo | AUT-WEB — Automatizado pelo FS (`ng test`: Vitest + jsdom, TASK-0008), verificado pela QA (TASK-0010) |
| Rastreio | US-0002 CA-03 (a); RN-0002; RN-0001; ET RT-13, §5 item 2, CE-03..06 |
| Estado de execução | Não executado (aguarda G4) |

## Pré-condições
- Versão candidata aprovada no G4 (SHA registrado).
- Workspace `apps/portal-web`; `ng test --no-watch --coverage` (Vitest + jsdom).
- Respostas HTTP simuladas derivadas dos exemplos do `openapi.yaml` 1.0.0 (PR-04); lógica de apresentação separada do DOM.
- Teste identificado pelo ID deste CT no nome do `describe`/`it`.

## Passos
1. Parametrizar: falha de rede; sem resposta em 5 s (relógio simulado); 405; 500; 404; 200 com `status` ≠ `"ok"`; 200 com JSON malformado; campo ausente; `version` fora do SemVer; `timestamp` inválido.

## Resultado esperado (oráculo)
- Estado Erro: título "Status indisponível", selo "Erro", mensagem genérica constante; `role="alert"`.
- Sem código HTTP, URL, host ou stack; sem valores; nunca "Saudável".
- Timeout: a consulta é abortada aos 5 s e há **exatamente uma** requisição (sem nova tentativa automática).

## Evidência exigida
- Saída de `ng test` com o nome do teste e o resultado, na SHA do G4; caminho e SHA do teste revisado pela QA.
