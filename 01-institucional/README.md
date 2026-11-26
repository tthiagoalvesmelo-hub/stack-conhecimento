# Institucional — o que existe e o que ainda está a confirmar

> Versão 1.0 · 26/11/2026 · gerado a partir dos Prompts 01–04 da Stack Multiagentes (Prompt 04, Anexo A, tem prioridade).


**Fase de testes internos, projetos do zero.** Esta pasta está praticamente vazia de propósito: ela só recebe conteúdo confirmado. Nada abaixo deve ser tratado como decidido enquanto estiver marcado “A CONFIRMAR”.

## A confirmar (premissas — não assumir)
| Item | Situação | Quem define | Quando |
|---|---|---|---|
| Linguagens e frameworks do backend e do Portal Web | A CONFIRMAR (não informado) | Arquiteto Líder (Thiago informa) | Antes do primeiro desenvolvimento |
| Mobile: Java; plataforma-alvo (premissa: Android nativo) e versão mínima | Java confirmado; o restante A CONFIRMAR | Arquiteto Líder + PO | Antes do primeiro desenvolvimento |
| Banco(s) de dados por serviço | A CONFIRMAR | DBA + Arquiteto Líder | Antes do primeiro desenvolvimento |
| Mensageria/eventos e API Gateway | A CONFIRMAR | Arquiteto Líder | Antes do primeiro desenvolvimento |
| Nuvem/hospedagem, containers/orquestração, CI/CD, observabilidade | A CONFIRMAR | DevOps + Arquiteto Líder | Antes do primeiro desenvolvimento |
| Autenticação/autorização | A CONFIRMAR | Arquiteto Líder | Antes do primeiro desenvolvimento |
| Ambientes existentes (dev, homologação, produção) e qual é tratado como “produção” nos testes | A CONFIRMAR | Thiago Melo | Antes de qualquer implantação |
| GitHub: conta/organização, repositório inicial (vazio), identidades dos agentes | PENDENTE — credenciais virão do Thiago | Thiago Melo | Quando houver necessidade |
| Google Sheets: planilha “Stack Multiagentes — Operação” | PENDENTE — conector e credenciais virão do Thiago; espelho CSV em uso | Thiago Melo | Quando houver necessidade |
| Jira (backlog/roadmap) | Destino futuro; migração após os testes internos | Thiago Melo | Após os testes |
| Janela padrão de publicação, horário de disponibilidade para AH, limite de custo que exige AH | A CONFIRMAR (sugestão: dias úteis 10h–16h, fora de véspera de feriado e sexta à tarde; custo: qualquer aumento) | Thiago Melo | Antes de produção |
| Reserva de capacidade para débito técnico e segurança | Sugestão 20% — A CONFIRMAR | Thiago Melo | Primeira revisão |
| Política de retenção (Git e aprovações permanentes; snapshots 24 meses; logs conforme LGPD) | Proposta — A CONFIRMAR | Thiago Melo | Primeira revisão |
| Canal de alertas e conectores de monitoramento (Sentry, PagerDuty, Slack, Teams, Outlook) | A CONFIRMAR | Thiago Melo | Antes de produção |
| Controle de acesso por agente na pasta compartilhada | Premissa: não existe; todos leem e escrevem — por isso nada sensível é guardado | — | — |

## Bases de conhecimento do Thiago
Diretórios de **base de conhecimento e propostas de solução** serão compartilhados depois, principalmente com os agentes de negócio (CPO, PO, Product Marketing, Analista de Negócio). Quando chegarem, a Documentação os cataloga aqui (produto, regras de negócio) com `fonte`, `versao` e `dono`; até lá, **ninguém deve presumir o conteúdo**.

## Estrutura
`produto/` · `regras-negocio/` · `arquitetura/` · `padroes/` · `microsservicos/` · `integracoes/` · `portal-web/` · `mobile/` · `bancos/` · `ambientes/` · `seguranca/` (cada uma com `.gitkeep` até receber conteúdo). Arquivos de topo previstos: `tecnologias.md`, `restricoes-tecnicas.md`.
