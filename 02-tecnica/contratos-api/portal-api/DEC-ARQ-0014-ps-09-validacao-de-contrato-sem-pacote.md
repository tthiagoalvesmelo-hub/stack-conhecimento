---
id: DEC-ARQ-0014
titulo: "PS-09: validação do corpo contra o contrato OpenAPI nos testes, sem pacote de validação de esquema"
tipo: dec
versao: 1.0
status: vigente
dono: ARQ
autores: [ARQ]
aprovado_por: ARQ
criado_em: 2026-11-26T15:54-03:00
atualizado_em: 2026-11-26T15:54-03:00
revisar_ate: 2027-02-26
relacionados: [DEM-2026-001, TASK-0007, TASK-0008, TASK-0010, PT-0001, CT-0004, CT-0005, CT-0049, ADR-0001, DEC-ARQ-0007, ET-0001, openapi.yaml, R2, R5, PS-09]
substitui: null
substituido_por: null
---

# DEC-ARQ-0014 — PS-09: validação de contrato sem pacote

> [TESTE] Aprova a escolha do PS-09 (ET-0001 §6; ADR-0001 v2 D4 e Lacuna 4; L-03 do parecer G2 da QA). **Custo zero** e nenhuma dependência nova. Medições e metadados: `07-agentes/07-arq/evidencias-lacunas-pt-0001/` (06, 07). Pesquisa de licenças e dependências em 26/11/2026 no NuGet (nuspec dos pacotes) e nos repositórios oficiais.

## Requisitos
Gratuita; licença compatível; ler o contrato OpenAPI 3.1 (JSON Schema 2020-12); aplicar `format: date-time` (R2: `2026-02-31T10:00:00.000Z` passa no `pattern` e deve ser reprovado); `const`, `additionalProperties: false`, `required`, `pattern`, `allOf`/`$ref` (as palavras-chave que os esquemas do `openapi.yaml` 1.0.0 usam).

## Opções avaliadas
| Opção | Licença / custo | Resultado |
|---|---|---|
| **JsonSchema.Net 9.7.0** | O pacote do NuGet traz o **Open Source Maintenance Fee EULA (OSMF)**: o código é MIT, mas o **binário publicado** cobra taxa de manutenção de quem o usa em atividade que gera receita com faturamento anual ≥ US$ 10.000 (isento: abaixo disso ou quem paga suporte aos mantenedores). Suporta 2020-12 (documentação oficial) | **Não adotada.** Pode implicar **custo**, e custo exige AH. Compilar o código-fonte por conta própria evitaria a taxa, mas cria manutenção de build que não cabe aqui |
| **NJsonSchema 11.6.2** (+ NJsonSchema.Yaml) | MIT; traz Newtonsoft.Json 13.0.3, System.Text.Json 9.0.9, Namotion.Reflection, YamlDotNet | **Não atende** (medido contra os esquemas reais): **ignora `const`** (aceitou `status: "unavailable"` no 200, `title` errado e `type` com URL no problem+json) e **não aplicou `format: date-time`** (aceitou `2026-02-31`); não resolve `#/components/schemas/...` num documento OpenAPI sem reescrever as referências |
| **Corvus.Json.Validator 5.8.12** | Apache-2.0; depende de Roslyn (`Microsoft.CodeAnalysis.CSharp`) e de mais de dez pacotes (geração de código) | **Não adotada** por desproporção (não testada): o contrato tem 8 esquemas pequenos |
| **Microsoft.OpenApi 3.11.1** | MIT | **Não serve:** é modelo/leitor/escritor de documento OpenAPI (descrição oficial do pacote), não validador de instância JSON |
| **Validação explícita, sem pacote** | Custo zero; sem dependência | **Adotada.** Medido: `DateTimeOffset.TryParseExact` com `yyyy-MM-dd'T'HH:mm:ss.fff'Z'` reprova `2026-02-31`, `24:00:00`, sem milissegundos e `\n` final; o `pattern` com `\z` reprova `\n` final (R5) |

## Decisão
1. **Nenhuma biblioteca de validação de esquema é adotada.** O FS escreve, no projeto de testes (TASK-0008), um **validador explícito** (código de teste) que cobre exatamente as palavras-chave usadas pelos esquemas do contrato 1.0.0: `type`, `const`, `required`, `additionalProperties: false`, `pattern`, `format: date-time`, `allOf` e `$ref` para os esquemas `ServiceVersion`, `Timestamp`, `HealthOk`, `HealthUnavailable`, `ProblemBase` e os problemas 404/405/500.
2. **Regras do validador:** `pattern` avaliado com `\z` no lugar do `$` final (R5; ADR-0001 v2 D8 item 12); `format: date-time` por `DateTimeOffset.TryParseExact(valor, "yyyy-MM-dd'T'HH:mm:ss.fff'Z'", CultureInfo.InvariantCulture, DateTimeStyles.AssumeUniversal, out _)` **além** do `pattern` (R2).
3. **Aderência ao contrato** (a fonte única é o `openapi.yaml` no stack-conhecimento; o repositório do Portal não guarda cópia): as constantes de `pattern`/`const` do validador citam a versão do contrato (1.0.0) e o commit; **QA/CR conferem a igualdade** com o `openapi.yaml` no G4/G5 por extração textual dos `pattern:` e `const:`, e anexam a evidência. Se o FS preferir ler o YAML no teste, **`YamlDotNet` (MIT, apenas no projeto de testes) fica pré-aprovado** como alternativa; qualquer outro pacote volta ao ARQ.
4. **Controles negativos obrigatórios** (CT-0004 e CT-0049): o validador reprova `2026-02-31T10:00:00.000Z`, timestamp sem ou com 7 casas de milissegundos, `version` com `+commit`, `status` trocado (const), campo extra e problem+json com `traceId`, `title` errado ou `type` com URL; e aceita o valor válido. Validador que aceita um negativo **não vale como evidência**.
5. A **PS-09 fica aprovada** nos termos acima. Edição da ET-0001 (ela diz "biblioteca ainda não escolhida") é da AS, em versão editorial futura; este DEC é a referência até lá.

## Impacto
Sem dependência nova e sem custo. Horas: o validador entra nas 11 h de testes do FS; sem mudança no plano G2 v1.2. CA, contrato e esquemas: nenhum muda.

## Histórico
| Versão | Data/hora (America/Sao_Paulo) | Autor | Mudança |
|---|---|---|---|
| 1.0 | 26/11/2026 15:54 | ARQ | Criação (PS-09) |
