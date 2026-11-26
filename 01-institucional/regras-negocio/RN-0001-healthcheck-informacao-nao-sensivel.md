---
id: RN-0001
titulo: "Health-check expõe somente informação não sensível"
tipo: rn
versao: 1.2
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:15-03:00
atualizado_em: 2026-11-26T12:41-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, REQ-0001, REQ-0004, US-0001, US-0002, ADR-0002]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (condição 1 do G1):** formatos, 503/405/500, tempo limite de 5 s e “sem login” dependem dos ADR-0002/0003 ainda propostos; se mudarem no G3, o PO reabre os CA afetados. Implementação depende da AH-0001.

# RN-0001 — Health-check expõe somente informação não sensível

> [TESTE] Origem: DEM-2026-001 · TASK-0002 · **v1.1:** a pendência sobre a versão foi respondida pelo ARQ (ADR-0002 proposto) para exposição interna.

**Regra:** a resposta do health-check (e qualquer apresentação dela no Portal Web) contém apenas o que a solicitação pede — **status, versão e timestamp**. É proibido incluir ou exibir dados pessoais, credenciais, segredos, tokens, e detalhes internos de infraestrutura ou implementação (nomes de máquina, caminhos, IPs, variáveis de ambiente, versões de runtime/dependências, hash de commit, mensagens de exceção/stack trace).

**Sensibilidade da versão (premissa, ADR-0002 proposto):** em exposição **interna** (rede local/interna, contrato interno), a versão do serviço **não** é considerada informação sensível e pode constar na resposta e, no estado saudável, na tela. Se a exposição deixar de ser interna, a regra deve ser reavaliada pelo ARQ (contrato público, R3/N3, nova AH).

**Aplicação:** REQ-0004; CA-05 e CA-07 da US-0001; CA-06 da US-0002.
