# Nota de análise (obrigatória antes de codificar) — MODELO

TASK-nnnn · DEM-AAAA-nnn · autor (sigla) · data/hora

| Passo | O que verificar | Onde |
|---|---|---|
| 1. Consultar o requisito | US/REQ/RN e critérios de aceite vigentes (versão no contexto.yaml) | US, REQ, RN |
| 2. Consultar a arquitetura existente | Padrões, ADRs aplicáveis e catálogo de serviços | 02-tecnica/adr, padrões |
| 3. Identificar o serviço responsável | Dono do domínio e dos dados; nunca implementar regra no serviço errado | Catálogo de serviços |
| 4. Avaliar dependências | Serviços, bibliotecas, filas, terceiros, tarefas anteriores | contexto.yaml, Tarefas |
| 5. Consultar os contratos das APIs | Versão vigente, consumidores conhecidos, compatibilidade | 02-tecnica/contratos-api |
| 6. Identificar alterações no banco | Necessidade de migração; acionar o DBA antes de codificar | 02-tecnica/modelos-dados |
| 7. Avaliar impactos no Portal Web e no Mobile | Telas, versões mínimas do app, cache, sessões | Protótipos, EF |
| 8. Confirmar os critérios de aceite | Entendimento escrito de cada CA; lacuna → MSG-COL ao PO | US |
| 9. Apresentar dúvidas e riscos | Registrar no MSG-RET de análise antes de implementar; risco alto → Arquiteto | MSG-RET |
Resultado: “Nota de análise” curta anexada à TASK (itens 1–9 com referências). Sem ela, a TASK não passa a “Em desenvolvimento” (parte da DoR técnica).
