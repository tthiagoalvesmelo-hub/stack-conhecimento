---
id: RN-0001
titulo: "Health-check expõe somente informação não sensível"
tipo: rn
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: null
criado_em: 2026-11-26T12:15-03:00
atualizado_em: 2026-11-26T12:15-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0002, REQ-0001, REQ-0004, US-0001, US-0002]
substitui: null
substituido_por: null
---

# RN-0001 — Health-check expõe somente informação não sensível

> [TESTE] Origem: DEM-2026-001 · TASK-0002 · Regra proposta pelo PO; status em-revisao até o G1 (validação do escopo).

**Regra:** a resposta do health-check (e qualquer apresentação dela no Portal Web) contém apenas o que a solicitação pede — **status, versão e timestamp**. É proibido incluir ou exibir dados pessoais, credenciais, segredos, tokens, e detalhes internos de infraestrutura ou implementação (nomes de máquina, caminhos, variáveis de ambiente, mensagens de exceção/stack trace).

**Justificativa:** segurança desde a concepção e LGPD (Contexto Global da Stack); o health-check é consultado por pessoas e sistemas de monitoramento e não deve ampliar a superfície de exposição.

**Pendência (dono ARQ):** se a versão informada pode ser considerada informação sensível conforme a exposição do endpoint (interna vs. pública) — decisão de segurança/arquitetura, não do PO.

**Aplicação:** REQ-0004; CA-05 da US-0001; CA-06 da US-0002.
