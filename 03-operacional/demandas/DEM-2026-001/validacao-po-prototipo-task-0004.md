---
id: DEC-PO-0005
titulo: "Validação do protótipo e da spec da tela de status (TASK-0004) e decisões RE-01..RE-05"
tipo: dec
versao: 1.0
status: em-revisao
dono: PO
autores: [PO]
aprovado_por: PO
criado_em: 2026-11-26T12:32-03:00
atualizado_em: 2026-11-26T12:32-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0004, TASK-0005, US-0002, REQ-0002, REQ-0003, REQ-0004, RN-0001, RN-0002, DEC-PO-0002, DEC-PO-0006, ADR-0003, UX-ESPEC-DEM-2026-001-TASK-0004]
substitui: null
substituido_por: null
---

# DEC-PO-0005 — Validação do protótipo/spec da tela de status (DEM-2026-001 · TASK-0004)

> [TESTE] 26/11/2026 12:32, America/Sao_Paulo · Alçada do PO: validação **funcional** frente aos CA/RN. Nenhuma decisão de interface (além de aceitar ou recusar o comportamento proposto) e nenhuma decisão de arquitetura.

## Resultado: Aprovado com ressalvas

O protótipo HTML v1.0 e a especificação de interface v1.0 (id UX-ESPEC-DEM-2026-001-TASK-0004, commit `1290f25`) **atendem aos CA-01 a CA-06 da US-0002** (v1.0 e, com as decisões abaixo, v1.1), a REQ-0002/0003/0004 e a RN-0001/RN-0002. O artefato pode ser insumo da DoR da TASK-0008 e do G1, com as ressalvas da seção 4.

## 1. Fontes e conferência
- US-0002, REQ-0002/0003/0004, RN-0001/0002 (v1.0 na conferência; decisões refletidas na v1.1).
- Spec: `07-agentes/06-ux/prototipos/DEM-2026-001-US-0002-tela-status/especificacao-interface-tela-status.md` v1.0.
- Protótipo: `.../prototipo-tela-status.html` v1.0.
- ADR-0003 v1.0 proposto (commit 362ea35), apenas como premissa de formatos/valores.
- Conferência em Chrome headless (`google-chrome --headless=new`, 26/11/2026, America/Sao_Paulo), estados `#estado=saudavel|carregando|erro` e carga inicial (após o atraso, estado saudável), larguras 1100 px e 390 px. Capturas e DOM dump em ambiente local, **não versionados**.

### Evidência da conferência (DOM após o JS)
| Estado | Cartão | Valores `status`/`version`/`timestamp` no DOM | Botão | Anúncio |
|---|---|---|---|---|
| Saudável | visível; selo "Saudável"; "API operacional" | `ok` / `0.1.0` / local `26/11/2026 12:34:56` + UTC `2026-11-26T15:34:56.789Z` | `aria-disabled=false` | polite: "API operacional. Versão 0.1.0." |
| Carregando | visível; "Verificando status da API…"; esqueleto | **vazios** (removidos) | `aria-disabled=true`; `aria-busy=true` | polite: "Verificando status da API." |
| Erro | visível; selo "Erro"; "Status indisponível"; mensagem genérica; sem tela em branco | **vazios** (sem versão/timestamp) | `aria-disabled=false` | alert: "Status indisponível. Não foi possível obter o status da API." |

O estado saudável combina ícone, título, selo textual e borda, não só cor (CA-02). Não há dados pessoais, segredos nem detalhes internos na tela (CA-06, RN-0001). A recuperação (erro → atualizar → carregando → saudável) está no fluxo do protótipo (CA-05). A visão móvel (360 px) empilha rótulo/valor e alarga o botão, conforme a spec; a captura a 390 px do painel do protótipo ficou longa (o painel não faz parte da tela).

## 2. Rastreio funcional CA × protótipo/spec
| CA (US-0002) | Veredito | Observação |
|---|---|---|
| CA-01 | Atende | Valores brutos iguais à amostra da "mesma consulta"; UTC explícito + horário de Brasília (D-UX-05/08 **aceitos**, oráculo mantido). |
| CA-02 | Atende | Ícone + "API operacional" + selo "Saudável" + borda sólida. |
| CA-03 | Atende, com decisão RE-02 | Um estado de erro genérico para todas as causas, inclusive 503; sem valores, sem mensagem técnica, sem tela em branco (RN-0002). |
| CA-04 | Atende | Estado de carregamento sem valores nem erro; na atualização os valores anteriores são removidos do DOM (D-UX-02, promovido ao CA na v1.1). |
| CA-05 | Atende | Botão "Atualizar status" e recarga; fluxo demonstrado no painel. |
| CA-06 | Atende | Só os três campos (no saudável) e mensagens fixas; inserção por `textContent`. |

## 3. Decisões RE-01..RE-05 e D-UX-05/08
| ID | Decisão | Justificativa |
|---|---|---|
| **RE-01** (dica "sem conexão do dispositivo") | **Aceitar como opcional**, sem novo CA e sem ampliar o escopo. | Já coberto pelo CA-03 (caso a). A dica pode complementar a mensagem genérica, desde que **não** exponha detalhe técnico (CORS, código HTTP, host). A forma da dica é do UX. Não é obrigatória para o aceite. |
| **RE-02** / D-UX-03 (503 com `status: "unavailable"` ocultar versão/timestamp) | **Aceitar.** Confirmado. | 503 é caminho de indisponibilidade (DEC-PO-0006, alternativa A; US-0001 CA-07). Na tela é o mesmo estado de erro genérico do CA-03, caso (b): **não exibe versão nem timestamp**. Isso não altera o contrato da API (o 503 **pode** trazer os três campos); só a apresentação. Evita tratar o payload do 503 como leitura atual confiável e mantém um único estado de erro (D-UX-06, RN-0002). |
| **RE-03** ("Última tentativa em HH:MM:SS" no erro) | **Rejeitar nesta demanda.** | Acrescentaria um dado que o CA-06 não prevê (só status, versão, timestamp e mensagens genéricas). Não há ajuste do CA-06 para caber esse campo. Pode ser proposta futura. |
| **RE-04** (polling automático) | **Aceitar apenas como demanda futura.** | Fora do escopo atual (P-UX-07; ADR-0003: polling fora de escopo). Não entra nesta DEM. |
| **RE-05** (título da aba refletindo o estado) | **Aceitar como opcional**, sem novo CA. | Não conflita com os CA; não é obrigatório para o aceite. Se implementado, o título não pode vazar detalhe técnico (RN-0001). Forma: UX/FS. |
| **D-UX-05 / D-UX-08** (valores brutos + UTC e horário de Brasília) | **Aceitar.** | Fecha o oráculo do CA-01 (igualdade com a mesma consulta) sem exigir que a string formatada em pt-BR seja idêntica à da API. Resposta à observação da QA na TASK-0005. |

## 4. Ressalvas (não são defeitos do protótipo)
1. Formatos, valores de `status`, tempo limite de 5 s e tela sem login são **premissa** dos ADR-0002/0003 **propostos**. Se o ARQ alterar na aceitação, o UX revisa rótulos e regras antes da implementação (TASK-0008).
2. Público da tela ainda não confirmado pela CPO (DEC-PO-0002). Se o público mudar, o vocabulário e a exibição do valor bruto devem ser revistos.
3. Tempo limite definitivo e tolerância do timestamp: AS na ET (L6).
4. Leitor de tela real, outros navegadores e zoom 400% não foram verificados aqui (já marcados "V" na spec, para FS/QA).
5. Identidade visual inexistente (paleta neutra provisória, P-UX-03): aceitável no teste; não bloqueia.

## 5. O que não foi decidido pelo PO
Layout, tipografia, tokens, microcopy exata (além do comportamento exigido pelos CA), rota `/status` e cabeçalho "Portal Web" provisório: alçada do UX (e, no acesso/rota, do ARQ/FS). Stack do Portal: ARQ / AH-0001.

## 6. Próximos passos
- ORQ: registrar este parecer em `contexto.yaml` (`prototipos[].validacao_po`), apontar DEC-PO-0005 e mergear o ramo `doc/DEC-PO-0005-validacao-prototipo` (histórico), se encaminhado.
- UX: não é obrigatório republicar o protótipo; as decisões opcionais (RE-01, RE-05) ficam a critério dele. Se republicar, informar a versão.
- FS (TASK-0008): implementar a versão validada (seções 7–10 da spec), após G1/G2/G3 e AH-0001, respeitando RE-02 e CA-04 v1.1.
- QA (TASK-0010): oráculos = US-0002 v1.1 + spec v1.0 + este parecer.
