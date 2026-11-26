---
id: DEC-ARQ-0015
titulo: "Referência ao contrato OpenAPI nos testes do repositório portal, sem cópia; fechamento da exposição de Program (DEC-ARQ-0011 §2); entrada da portal-api no catálogo"
tipo: dec
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T16:00-03:00
atualizado_em: 2026-11-26T16:00-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0008, TASK-0010, PT-0001, CT-0004, CT-0049, ADR-0001, ADR-0002, DEC-ARQ-0011, DEC-ARQ-0014, ET-0001, openapi.yaml]
substitui: null
substituido_por: null
---

# DEC-ARQ-0015 — Contrato nos testes sem cópia; fechamento da DEC-ARQ-0011 §2; catálogo

> [TESTE] Responde aos pedidos (c) e (d) do FS (MSG-RET da TASK-0008, esqueleto D6, HEAD `2240056`) e registra a confirmação da DEC-ARQ-0011 §2. Sem custo, sem N3, sem mudança de CA, de esquema ou de `info.version` (1.0.0). Pedido (a) (R2 = validador explícito) e pedido (b) (janela de drenagem) já estavam na DEC-ARQ-0014 e na DEC-ARQ-0012 (PR #4).

## 1. Como os testes do repositório `portal` referenciam o contrato (pedido c)

A fonte única do contrato é o `openapi.yaml` no repositório de memória `stack-conhecimento`, caminho `02-tecnica/contratos-api/portal-api/openapi.yaml`, `info.version` **1.0.0**.

**Decisão:**
1. Os testes do repositório `portal` **não copiam** o `openapi.yaml`, **não** usam *submodule* e **não** leem o contrato em rede (nem clone, nem API, nem *raw*).
2. O **validador explícito** da DEC-ARQ-0014 (projeto de testes da TASK-0008) **codifica as regras** (`const`, `required`, `additionalProperties: false`, `pattern` com `\z`, `format: date-time` por `DateTimeOffset.TryParseExact`, `$ref`/`allOf` dos esquemas 1.0.0).
3. **Rastreabilidade:** uma constante ou um comentário **único** no projeto de testes declara, juntos: o repositório (`https://github.com/tthiagoalvesmelo-hub/stack-conhecimento`), o caminho acima, `info.version` 1.0.0 e o **SHA de referência**. SHA inicial: **`e34e6b9`** (merge da prosa da R1 do G3 na main). Pode ser trocado por um SHA **posterior que não altere o contrato** (esquemas, operações, status, exemplos, `info.version`). Qualquer nova versão do contrato (ou mudança normativa no 1.0.0) **obriga** a atualizar a referência **e** os testes.
4. A **consistência** entre o validador e o `openapi.yaml` é verificada pela **QA** (CT-0049, e os negativos do CT-0004) e pelo **CR** no G4, por extração textual dos `pattern:` e `const:` (DEC-ARQ-0014 item 3). Sem essa evidência, o validador não conta.

## 2. Fechamento da lacuna da DEC-ARQ-0011 §2

O FS confirmou no esqueleto D6 (ramo `feat/TASK-0008-health-portal`, HEAD `2240056`): `WebApplicationFactory<Program>` funciona **sem** declarar `public partial class Program`. Isso **fecha** o “a confirmar na primeira implementação” da DEC-ARQ-0011 §2: a forma padrão da documentação de testes de integração do ASP.NET Core atende e **não amplia** a superfície em produção. A decisão da L-12 (itens 1–7) não muda. A DEC-ARQ-0011 é versionada a **v1.2** neste mesmo ramo (o PR #4 não a altera; não há conflito de arquivo).

## 3. Catálogo da `portal-api` (pedido d)

A área `01-institucional/microsservicos/` é do **ARQ** (CODEOWNERS; matriz mais próxima: arquitetura / padrões / tecnologias). A entrada `01-institucional/microsservicos/portal-api.md` é criada neste ramo. Sem *host*, IP, credencial, dado pessoal ou dado real (repositórios públicos). Status: em desenvolvimento (DEM-2026-001 / TASK-0008).

## Histórico
| Versão | Data/hora (America/Sao_Paulo) | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 16:00 | ARQ | Criação (pedidos c e d do FS; fechamento da DEC-ARQ-0011 §2) |
