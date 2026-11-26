---
id: DEC-ARQ-0005
titulo: "Recorte de SAST/varredura desta demanda (TASK-0010), condicionado ao ADR-0001"
tipo: dec
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T13:10-03:00
atualizado_em: 2026-11-26T13:10-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0010, TASK-0008, TASK-0009, ADR-0001, DEC-ARQ-0003, DEC-ARQ-0004, AH-0001]
substitui: null
substituido_por: null
---

# DEC-ARQ-0005 — Recorte de SAST/varredura (TASK-0010)

> [TESTE] **Condicionada à aceitação do ADR-0001** (como a DEC-ARQ-0004). Se a stack mudar, esta DEC é revista antes da execução da TASK-0010. Não é N3 (sem custo, sem produção, sem nova tecnologia de serviço/banco/framework). Consulta ao registro npm em 26/11/2026, **sem instalar nada**.

## Decisão
Nesta demanda de teste, a varredura exigida pela matriz R3 / G5 fica **explicitamente recortada** em:

1. **SCA:** `npm audit --audit-level=high` no script `verify-local` (DEC-ARQ-0003) — já decidido.
2. **Análise estática:** ESLint *recommended* (DEC-ARQ-0004: `eslint` + `@eslint/js` + `globals`).
3. **Testes dirigidos de segurança** da QA na TASK-0010 (RN-0001, REQ-0004, CA-05/CA-06, denylist, tentativa de forçar 503/500).

O PQ deve avaliar a varredura **neste recorte**, não condicionar o favorável pleno a uma ferramenta de SAST que a arquitetura não adotou. Exceção a vulnerabilidade alta/crítica ou a este recorte exige AH de segurança.

## O que não adoto agora
- **`eslint-plugin-security` 4.2.1** (Apache-2.0; engines Node compatíveis com o 24; **`peerDependencies` ausentes** — não declara ESLint 10 nem config flat). Sem instalação, a compatibilidade com ESLint 10 **não está evidenciada**. Não acrescento plugin com peer não declarado.
- **Semgrep OSS:** ferramenta **nova**, fora do npm, **não instalada** na box. Enquadra-se em “ferramenta nova só com avaliação do Arquiteto”. Não é N3 de arquitetura (não é novo serviço, banco, mensageria ou framework do produto) nem N3 de custo (OSS, sem licença). Ainda assim é desproporcional a esta demanda (health-check local, toolchain npm já definida) e exigiria instalação e operação pelo OPS. Não adoto nesta demanda.

Se, depois da AH-0001 ou de uma evidência de compatibilidade com ESLint 10 (sem improviso), o residual de SAST precisar ser reaberto, isso será **nova DEC**, não alteração in-place desta.
