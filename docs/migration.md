# Migração entre modelos (ex: 1.3B -> 3B)

Este documento descreve um fluxo prático para migrar um dispositivo Gaia que usa um modelo muito leve (1.3B) para um modelo de maior qualidade (3B), preservando a maior parte do contexto e aprendizado do usuário.

Princípios
- Não incluir pesos no repositório.
- Manter a memória vetorial (vectors.json) e adapters/LoRA patches portáveis.
- Preferir retrieval + prompts ao invés de fine-tuning local quando possível.

Passos recomendados
1. Exportar memória vetorial local
   - `python -m scripts.vector_store_export export` (ou usar a API export_vector_store)
   - salva vectors.json que será reimportado pelo novo runtime

2. Exportar Adapter Patch (se houver adaptação local)
   - `scripts/adapter_manager.export_adapter(manifest, files, out.zip)`
   - o pacote conterá pequenos patches e metadados

3. Preparar o novo modelo local (não incluído)
   - baixe e converta o modelo 3B para o formato compatível (ggml/gptq) usando as instruções em docs/llm_choice.md

4. Aplicar patches e reimportar memória
   - copie vectors.json para o device que roda o modelo 3B
   - importe adapter: `scripts/adapter_manager.import_adapter('out.zip', '.gaia/import')`
   - reindex vectors na nova runtime (se aplicável)

5. Testes de sanidade
   - execute uma bateria de prompts de validação para garantir a coerência do contexto (ex.: perguntas sobre preferências do usuário)

6. Backups e reversão
   - mantenha backups em `.gaia/backups` antes de aplicar qualquer mudança

Notas
- Se o adapter não for compatível (diferença de arquitetura), manter memória vetorial e usar retrieval + prompts para fornecer histórico ao novo modelo.
- LoRA/adapter patches requerem compatibilidade de arquitetura; em caso de incompatibilidade, considerar um processo de distillation/transfer fora do dispositivo (servidor seguro) para gerar novo adapter.
