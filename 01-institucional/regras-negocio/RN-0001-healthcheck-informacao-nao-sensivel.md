---
id: RN-0001
titulo: "Health-check expõe somente informação não sensível"
tipo: rn
versao: 1.3
status: vigente
dono: PO
autores: [PO]
aprovado_por: PO (G1, DEM-2026-001)
criado_em: 2026-11-26T12:15-03:00
atualizado_em: 2026-11-26T15:12-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, TASK-0003, REQ-0001, REQ-0004, US-0001, US-0002, ADR-0002, DEC-PO-0008, AH-0003]
substitui: null
substituido_por: null
---

> **Vigente desde 26/11/2026 12:41 (America/Sao_Paulo)** — promovido pelo PO após o G1 (Aprovado com observações, aprovacoes.md, commit b083eef). **Ressalva (1) do G1 (atualizada em 26/11/2026 15:12 (America/Sao_Paulo), DEC-PO-0008):** os ADR-0001 v2.0, ADR-0002 v1.1 e ADR-0003 v1.1 foram **aceitos** (AH-0003 aprovada em 26/11/2026 14:54, America/Sao_Paulo, que substitui a AH-0001; G3 registrado em `a271ac1`). Os formatos, caminhos 503/405/500, tempo limite de 5 s e “sem login” seguem esses ADR aceitos. **Ressalva do G3:** R1..R5 (aprovacoes.md, 26/11/2026 15:08) — R1 (ET-0001 v1.4 da AS, condição para liberar a TASK-0008); R2 (teste de contrato com `format: date-time`); ressalva R3 do G3 (itens PV do ADR-0001 v2 D8 como testes obrigatórios antes do G4); R4 (SDK .NET 10 + Angular CLI e spike do encerramento gracioso em ASP.NET Core antes do CA-07); R5 (usar `\z` nas regex .NET). A implementação não depende mais da AH-0001.
>
> **v1.3** (26/11/2026 15:12 (America/Sao_Paulo)) — revisão editorial (DEC-PO-0008): premissa do ADR-0002 atualizada para v1.1 aceito. Nenhum CA foi reaberto nem alterado. Status **vigente** mantido.

# RN-0001 — Health-check expõe somente informação não sensível

> [TESTE] Origem: DEM-2026-001 · TASK-0002 · **v1.1:** a pendência sobre a versão foi respondida pelo ARQ (ADR-0002 proposto) para exposição interna.

**Regra:** a resposta do health-check (e qualquer apresentação dela no Portal Web) contém apenas o que a solicitação pede — **status, versão e timestamp**. É proibido incluir ou exibir dados pessoais, credenciais, segredos, tokens, e detalhes internos de infraestrutura ou implementação (nomes de máquina, caminhos, IPs, variáveis de ambiente, versões de runtime/dependências, hash de commit, mensagens de exceção/stack trace).

**Sensibilidade da versão (premissa, ADR-0002 v1.1 aceito):** em exposição **interna** (rede local/interna, contrato interno), a versão do serviço **não** é considerada informação sensível e pode constar na resposta e, no estado saudável, na tela. Se a exposição deixar de ser interna, a regra deve ser reavaliada pelo ARQ (contrato público, R3/N3, nova AH).

**Aplicação:** REQ-0004; CA-05 e CA-07 da US-0001; CA-06 da US-0002.
