# Pacote de contexto — MODELO

Gerado pelo Orquestrador para cada MSG-SOL. Local: /workspace/stack-memoria/pacotes-contexto/<DEM>/<TASK>.md. Selecione o contexto pelo papel do destinatário; nunca envie o histórico completo.

```
PACOTE DE CONTEXTO — <DEM-AAAA-nnn> / <TASK-nnnn> (para <Nome>, <cargo>)
Gerado por: Orquestrador (Otávio Mendes) em <data/hora America/Sao_Paulo> · versão do contexto da demanda: <n>
Objetivo da demanda (1 linha):
Sua atividade:
Leitura obrigatória (ponteiros: ID + caminho + versão):
- 
Decisões que afetam você (ADR/DEC/RN):
Dependências:
Bloqueios conhecidos:
Não incluído (consultar se precisar):
Classe de risco / prioridade / severidade:
Retorno esperado: MSG-RET com <entregável>, evidências, fontes consultadas e riscos.
```

## Exemplo de preenchimento (do Prompt 03; os IDs são fictícios)

```
PACOTE DE CONTEXTO — DEM-2026-041 / TASK-0411 (para André Nogueira, Java Mobile)
Gerado por: Orquestrador (Otávio Mendes) em 27/11/2026 10:05 · versão do contexto da demanda: 6
Objetivo da demanda (1 linha): permitir anexar foto de comprovante ao pedido no app e visualizar no Portal.
Sua atividade: implementar upload de até 3 fotos com fila offline (US-0301).
Leitura obrigatória (ponteiros):
- 03-operacional/demandas/DEM-2026-041/historias/US-0301.md (critérios de aceite CA-301.1 a 301.5)
- 02-tecnica/especificacoes/ET-0088.md v2 (seções 3 e 5)
- 02-tecnica/adr/ADR-0031-upload-url-preassinada.md (aceito)
- 02-tecnica/contratos-api/pedidos/openapi.yaml 1.4.0 (POST /pedidos/{id}/anexos)
- 01-institucional/mobile/versoes-suportadas.md
Decisões que afetam você: ADR-0031 (upload via URL pré-assinada); RN-0212 (até 5 MB).
Dependências: TASK-0405 (contrato) concluída · TASK-0408 (bucket, DevOps) em andamento — use mock até G3.
Bloqueios conhecidos: nenhum.
Não incluído (consultar se precisar): histórico completo da demanda, demandas anteriores do serviço de pedidos.
Retorno esperado: MSG-RET com PR, evidências de teste e riscos.
```
