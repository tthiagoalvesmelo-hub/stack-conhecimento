# Matriz de aprovações

> Versão 1.1 · 26/11/2026 · gerado a partir dos Prompts 01–04 da Stack Multiagentes (Prompt 04, Anexo A, tem prioridade). v1.1 (ORQ, AH-0004): item 7 do procedimento de AH atualizado (GitHub conectado).

## Modos de validação

| Modo | Como funciona | Exemplos |
|---|---|---|
| Automatizada | Verificação objetiva por pipeline, checklist ou regra registrada; o Orquestrador registra o gate citando a evidência. Nenhum agente opina. | Ex.: CI verde, ausência de migração no diff, template completo |
| Manual pelo agente validador | O agente dono do ponto analisa e emite parecer (aprovado / com observações / reprovado) registrado em aprovacoes.md. | Ex.: CR-nnnn, PQ-nnnn, parecer do DBA |
| Aprovação humana (AH) | Thiago Melo (ou designado) aprova por mensagem explícita; registro AH-nnnn na aba Aprovações humanas e em aprovacoes.md. | Ex.: publicar em produção, migração destrutiva |


## Matriz dos 10 pontos de aprovação × gates

| Ponto (seção 10 do Prompt 04) | Validador | Gate(s) | Validação manual obrigatória quando | Pode ser automatizada quando |
|---|---|---|---|---|
| 1. Alinhamento estratégico | CPO | G0 | Funcionalidade nova; melhoria funcional com compromisso ou impacto no roadmap; infraestrutura com custo; conflito de prioridade | Correção de defeito P2/P3, refatoração e atualização sem impacto ao usuário dentro da reserva de capacidade aprovada pelo CPO no Roadmap; INC P0/P1 (G0 implícito, CPO informado) |
| 2. Escopo e critérios de aceite | PO | G1 (escopo); G6 (pré-aceite); G8 (confirmação) | Fluxo 01 e BUG com mudança de comportamento: G1, G6 e G8 sempre manuais | Fluxo 02 sem impacto funcional (PO informado); G8 de correções P3 visuais com testes de aceitação automatizados aprovados em produção |
| 3. Especificação | Analista de Sistemas | G1/G2 | Nova API ou integração, regra complexa, R2/R3 | R1 sem mudança de especificação: verificação automática de que a EF/ET vigente cobre a TASK |
| 4. Arquitetura | Arquiteto Líder | G1 (F02), G2, G3 (contratos), G4 (2ª aprovação) | R3, novo serviço, nova tecnologia/biblioteca, contrato, mudança de comunicação, alteração crítica | R1 dentro de padrões vigentes: checagem automatizada de conformidade (dependências permitidas, estrutura) com registro no G2 |
| 5. Modelo de dados | DBA | G3 e G6 (banco validado) | Toda alteração de estrutura, índice em tabela grande, migração de dados | Sem alteração de banco: verificação automática (sem scripts de migração no diff) |
| 6. Código | Code Reviewer (+ Arquiteto) | G4 | Sempre: todo código tem revisão de agente diferente do autor | Somente os pré-requisitos (CI, análise estática, varredura) são automáticos; nunca substituem o parecer |
| 7. Testes | QA | G5 | R2 e R3; toda demanda funcional | R1 de configuração ou texto: PQ gerado a partir da suíte automatizada verde, com confirmação do QA por amostragem |
| 8. Infraestrutura e deploy | DevOps | G6 (ambiente e rollback); G7 | Produção sempre (plano, execução, estabilidade); mudança de infraestrutura | Deploy em desenvolvimento e homologação pela pipeline; coleta de métricas na janela de observação |
| 9. Documentação | Analista de Documentação | G6 (pronta); G8 (publicada) | Mudança visível ao usuário, contrato de API, runbook, release | Mudança interna sem impacto: changelog gerado a partir dos PRs + checklist |
| 10. Resolução do incidente | Analista de Suporte | G8 do INC | Sempre; RCA obrigatória em P0/P1 | Não se aplica |

## Operações que exigem aprovação humana (AH)

| Operação | Quando exige AH | Quem prepara | Pacote mínimo para decisão |
|---|---|---|---|
| Publicação em produção | Sempre (fase atual) | DevOps prepara; responsável do fluxo solicita via Orquestrador | G6 completo, REL candidata, plano de rollback, resultado de homologação, riscos |
| Acesso de escrita a produção (shell, banco, console) | Sempre, por operação e com prazo de validade | DevOps ou DBA | Motivo, comandos previstos, duração, plano de reversão |
| Exclusão ou migração destrutiva de dados | Sempre | DBA | Backup verificado, script, volume afetado, reversão/compensação |
| Mudança em contrato público de API | Sempre (nova versão maior ou remoção) | Arquiteto Líder | Consumidores afetados, convivência, comunicação, prazo de descontinuação |
| Alterações de segurança | Autenticação/autorização, permissões, rotação ou revogação de chaves, rede/firewall, exceção de vulnerabilidade | Arquiteto Líder (DevOps para infraestrutura) | Ameaça, impacto, teste de segurança, reversão |
| Custos de infraestrutura | Qualquer recurso pago novo ou aumento de capacidade (limite em valor: a definir pelo Thiago) | DevOps (Arquiteto avalia) | Custo estimado mensal, alternativa, duração |
| Arquitetura de alto impacto | Novo serviço, nova tecnologia de banco/mensageria/framework, mudança de padrão de comunicação | Arquiteto Líder | ADR proposto, alternativas, riscos, plano de migração |
| Operações irreversíveis | Exclusão de recurso, DNS, revogação, encerramento de conta, envio externo a clientes | Quem executaria | O que se perde, por que é necessário, confirmação de backup |
| Mudança de governança | Alterar este documento, níveis de autonomia, prompts ou conectores | Orquestrador (com Documentação) | Diferença proposta e justificativa |

## Autorização final de publicação em produção

> RESOLUÇÃO DA PENDÊNCIA DO PROMPT 02
> DECISÃO: A AUTORIZAÇÃO FINAL PARA PUBLICAR EM PRODUÇÃO É DO THIAGO MELO (OU DE QUEM ELE DESIGNAR POR ESCRITO).
> Fase atual (testes internos e estabilização): toda publicação em produção exige AH-nnnn, inclusive hotfix.
> Pré-requisitos para pedir: G6 completo (banco validado, documentação pronta, pré-aceite do PO ou do Arquiteto, ambiente e rollback validados pelo DevOps) e G4/G5 da mesma versão.
> Rollback para a versão anterior por runbook aprovado não exige AH (é a ação que reduz risco); Thiago é informado na hora.
> Mudanças padrão pré-autorizadas: depois de pelo menos 30 dias de operação com taxa de falha em mudanças abaixo de 15% e nenhum P0 causado por mudança, Thiago pode listar por escrito, em 00-memoria/governanca/mudancas-padrao.md, categorias R1 reversíveis (sem contrato, banco, segurança ou custo) que dispensam AH individual. Elas continuam exigindo G0–G7 e aparecem no resumo diário.
> Emergência P0/P1: AH expressa; se o Thiago não responder em 30 min, o Orquestrador aciona o designado; sem aprovação, só mitigação por runbook ou rollback, nunca código novo em produção.
> Designação de substituto: só vale por mensagem do próprio Thiago, registrada em 00-memoria/governanca/aprovadores.md, com escopo e validade. Nenhum agente se autodesigna ou designa outro.

Procedimento de aprovação humana
1. O agente responsável prepara o pacote: operação, categoria, DEM/INC, classe de risco, evidências, plano de rollback, riscos e janela.
2. O Orquestrador confere se o G6 (ou o pré-requisito da categoria) está completo; se faltar algo, devolve sem pedir a aprovação.
3. O Orquestrador registra AH-nnnn (aba Aprovações humanas: status Solicitada) e envia ao Thiago o pedido no modelo MSG-AH, na própria conversa do Orquestrador.
4. Thiago responde de forma explícita: “Aprovo AH-nnnn”, “Aprovo AH-nnnn com condição: …” ou “Nego AH-nnnn: …”. Silêncio, “ok” solto ou resposta ambígua não é aprovação.
5. O Orquestrador transcreve a decisão (texto literal, data/hora America/Sao_Paulo, quem decidiu) na planilha e em aprovacoes.md e só então libera o DevOps.
6. Validade: a AH vale para a versão e a janela descritas; mudou o artefato ou passou a validade (padrão 24 h), nova AH.
7. GitHub está conectado (AH-0004). Recomenda-se também que a publicação em produção exija aprovação da conta pessoal do Thiago no ambiente de produção da pipeline (segunda barreira técnica, a confirmar).

> MODELO — MSG-AH (PEDIDO DE APROVAÇÃO HUMANA)
> MSG-AH — PEDIDO DE APROVAÇÃO HUMANA
> ID: AH-nnnn · Demanda/incidente: DEM-AAAA-nnn / INC-AAAA-nnn
> Operação solicitada: [o que será feito, onde, por quem]
> Categoria: [produção | acesso a produção | migração destrutiva | contrato público | segurança | custo | arquitetura | irreversível | governança]
> Classe de risco: R1 / R2 / R3 · Prioridade/severidade: [ ]
> Por que agora: [ ]
> Evidências: [G4 CR-nnnn · G5 PQ-nnnn · DBA · homologação · REL candidata]
> Riscos e impacto: [ ]
> Plano de rollback: [link + tempo estimado]
> Janela proposta / validade: [data/hora America/Sao_Paulo] / [24 h]
> Recomendação do responsável: [aprovar / aprovar com condição / não aprovar]
> Para decidir, responda: “Aprovo AH-nnnn”, “Aprovo AH-nnnn com condição: …” ou “Nego AH-nnnn: motivo”.
