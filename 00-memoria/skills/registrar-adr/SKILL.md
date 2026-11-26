SKILL — registrar-adr
---
name: registrar-adr
description: Use quando o Arquiteto Líder precisar registrar ou substituir uma decisão arquitetural.
---
# Registrar decisão arquitetural (ADR)
1. Reserve ADR-nnnn; use modelos/adr.md.
2. Preencha: contexto, decisão, alternativas avaliadas, justificativa, consequências/impactos (Portal Web, Mobile, serviços, dados, infra), status, relacionados.
3. Proposto → PR → Aceito (somente o Arquiteto aprova). ADR aceito é imutável.
4. Para mudar uma decisão, crie novo ADR com `substitui: ADR-xxxx` e atualize o antigo para `substituido_por`.
5. Inclua o ADR em `decisoes` das demandas afetadas e avise desenvolvedores, DBA e DevOps.
