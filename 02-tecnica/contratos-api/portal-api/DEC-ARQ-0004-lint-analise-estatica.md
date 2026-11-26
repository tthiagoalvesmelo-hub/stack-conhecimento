---
id: DEC-ARQ-0004
titulo: "Lint e análise estática da stack proposta (L-CR3), condicionada ao ADR-0001"
tipo: dec
versao: 1.0
status: substituida
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T12:50-03:00
atualizado_em: 2026-11-26T15:03-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0008, TASK-0009, ADR-0001, DEC-ARQ-0003, L-CR3, AH-0001]
substitui: null
substituido_por: DEC-ARQ-0008
---

# DEC-ARQ-0004 — Lint e análise estática (L-CR3)

> **SUBSTITUÍDA pela DEC-ARQ-0008** em 26/11/2026 (AH-0003: stack C#/.NET + Angular; ADR-0001 v2). O texto abaixo é preservado como histórico da stack Node/Fastify (AH-0001 substituída) e **não vale mais**.

> [TESTE] **Condicionada à aceitação do ADR-0001** (AH-0001). Se a stack mudar (alternativa B, Node 26 ou outra), esta DEC é revista antes do PR da TASK-0008. Sem custo de licença. Consulta ao registro npm em 26/11/2026, **sem instalar nada**. Não é N3. **Não bloqueia a decisão do G2**; bloqueia a entrada no G4 e deve estar no PR da TASK-0008 (via DEC-ARQ-0003).

## Decisão (se a alternativa A do ADR-0001 for aceita)
Ferramentas de **desenvolvimento** (devDependencies, lockfile, `npm ci`), não de runtime:

| Ferramenta | Versão consultada (npm, 26/11/2026) | Licença | Uso |
|---|---|---|---|
| `eslint` | 10.15.0 (engines: Node ^20.19 / ^22.13 / ≥24) | MIT | Lint ESM, config flat (`eslint.config.js`) |
| `@eslint/js` | 10.0.1 | MIT | Regras recommended |
| `globals` | 17.14.0 | MIT | Globais `node` (`portal-api`) e `browser` (`portal-web`) |

- Sem TypeScript e sem transpilação (ADR-0001 D1). Não adoto `eslint-plugin-n` (peers opcionais de TypeScript, superfície desnecessária).
- Análise estática de segurança, nesta fase: o próprio ESLint (recommended) + `npm audit` (DEC-ARQ-0003). Não acrescento plugin de segurança pago nem cadeia extra.
- Formatador (Prettier etc.) não é porta do G4.
- Comandos: `npx eslint` nos dois apps, integrados ao `scripts/verify-local.sh`. Zero avisos bloqueantes (`--max-warnings 0`).
- Versões exatas ficam no lockfile na implementação (FS), não abaixo das séries conferidas.

## Se a AH-0001 não aceitar a alternativa A
Não aplicar estas ferramentas. O ARQ emite revisão desta DEC no mesmo ciclo em que atualizar o ADR-0001, antes do PR da TASK-0008.
