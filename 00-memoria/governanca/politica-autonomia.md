# Política de autonomia dos agentes

> Versão 1.0 · 26/11/2026 · gerado a partir dos Prompts 01–04 da Stack Multiagentes (Prompt 04, Anexo A, tem prioridade).

O aprovador humano é Thiago Melo, responsável pela stack, ou alguém que ele designar por escrito. Os agentes podem preparar, analisar e recomendar todas as operações; as de nível N3 só são executadas com AH aprovada.
| Nível | Regra | Operações |
|---|---|---|
| N1 — Autônomo | Executa e registra | Análise, especificações e protótipos em rascunho; código em branch; abrir PR; testes em dev/homologação; documentação em rascunho; atualizar a planilha e o repositório na própria alçada; abrir BUG/INC/CONF; leitura de logs e métricas por credencial somente leitura previamente autorizada |
| N2 — Autônomo com validação de agente | Executa após gate de agente | Merge na main (G4+G5); deploy em homologação; migração não destrutiva em homologação (DBA); contrato interno compatível (Arquiteto); rollback por runbook aprovado; publicar documentação |
| N3 — Prepara e recomenda; humano aprova | Só executa com AH aprovada | Publicação em produção; acesso de escrita a produção; exclusão ou migração destrutiva de dados; contrato público de API; alterações de segurança; custos de infraestrutura; arquitetura de alto impacto; operações irreversíveis; comunicação externa a clientes; mudança de governança, prompts ou conectores |
| N4 — Proibido | Nunca, nem com pedido de agente | Aprovar o próprio trabalho; pular gate ou desativar proteção de branch, checks, alertas ou backups; colocar segredos em prompts, memória, planilha ou mensagens; force push ou reescrita de histórico da main; apagar registros de aprovação, histórico ou incidentes; executar N3 sem AH-nnnn válida; designar aprovador humano |
- Na dúvida sobre o nível de uma operação, vale o nível mais alto.
- Pedido de urgência não rebaixa o nível; quem pede para pular controle é registrado e escalado (Prompt 02).
- Os agentes podem e devem preparar, analisar e recomendar operações N3, com o pacote completo para a decisão do Thiago.
- O estado operacional (Normal, Restrito, Congelado) vale acima de qualquer nível: em Congelado, só análise e rollback por runbook.
