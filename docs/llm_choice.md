# LLm Choice Guide — Recommendations for Gaia (PT / EN)

PT — Resumo das recomendações

Para priorizar inclusão e cobertura, recomendamos um perfil mínimo 1.3B quantizado (VMR) que roda em muitos celulares intermediários. Como etapa de qualidade, recomendamos 3B quantizado para dispositivos mais poderosos.

Runtimes e ferramentas:
- llama.cpp / ggml (execução local quantizada)
- GPTQ / convert tools para quantização
- whisper.cpp (ASR) para entrada por voz
- ONNX/TFLite para modelos de visão (caption) e encoders leves

Licença: sempre verificar a licença do checkpoint antes de usar. Não armazenar pesos no repositório; fornecer scripts para download/chek de licença.

EN — Recommendations

To maximize inclusion, start with a 1.3B quantized base model (VMR). Offer a 3B quantized upgrade for better quality. Use quantized runtimes such as llama.cpp/ggml and GPTQ conversion. For speech, whisper.cpp; for vision, use tiny captioner models exported to ONNX/TFLite.

Model examples (check license before use):
- VMR: small instruction-tuned 1.3B (Alpaca-style or similar permissive checkpoints)
- Quality: 3B instruction-tuned model (Llama-2-3B converted or other permissive alternatives)

Conversion and installation steps (high level):
1. Download the checkpoint from the model provider (verify license).
2. Convert to ggml/GPTQ using community tools.
3. Place the converted files under `$GAIA_HOME/models/<model-name>/`.
4. Start Gaia runtime and configure `gaia_llm_adapter.model_path` to the converted model.

Notes:
- do not commit model weights into the repository.
- provide clear license references for each recommended model.
