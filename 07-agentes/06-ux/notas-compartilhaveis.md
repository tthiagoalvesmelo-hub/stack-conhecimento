---
id: AGT-UX-NOTAS
titulo: "Notas compartilháveis — Bruno Tavares (UX/UI Designer)"
tipo: agente
versao: 1.2
status: vigente
dono: UX
autores: [UX]
aprovado_por: Thiago Melo
criado_em: 2026-11-26T11:00-03:00
atualizado_em: 2026-11-26T13:13-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0004, US-0002, UX-0001, DEC-PO-0005]
substitui: null
substituido_por: null
---

# Notas compartilháveis — Bruno Tavares · UX/UI Designer

Conhecimento da especialidade que outros agentes podem precisar. Informação da memória nativa que influencie outro agente deve ser publicada aqui (ou na área dona) no mesmo dia, com MSG-COL ao afetado.

## 26/11/2026 — DEM-2026-001 [TESTE] · TASK-0004 (ponteiros; a fonte é o artefato)
- Entrega de UX **UX-0001** (alias; `id` da especificação permanece `UX-ESPEC-DEM-2026-001-TASK-0004`).
- Especificação de interface da tela de status (US-0002) **v1.1, vigente** (aprovada com ressalvas, DEC-PO-0005, commit af208f2): `07-agentes/06-ux/prototipos/DEM-2026-001-US-0002-tela-status/especificacao-interface-tela-status.md`.
- Protótipo navegável **v1.1** (`tipo: prototipo`; HTML estático autocontido, dados fictícios; sem mudança de comportamento em relação à v1.0): `.../prototipo-tela-status.html`.
- Regras de interface que afetam FS/QA: estado inicial = Carregando; só `status === "ok"` é saudável; ao atualizar, valores anteriores saem do DOM (CA-04); mensagens de erro são constantes genéricas; 503 (CA-03 caso b) = erro sem versão/timestamp (RE-02); dados inseridos só como texto (seção 7.5). Oráculo do CA-01: D-UX-05 e D-UX-08 (valores brutos + UTC; formatação Brasília adicional).
- RE-01 e RE-05 opcionais; RE-03 rejeitada nesta demanda; RE-04 só demanda futura. ADR-0002/0003 ainda propostos. Público confirmado pela CPO (DEC-PO-0002).
- Paleta neutra e tokens provisórios (sem identidade visual): seção 8 da especificação.
