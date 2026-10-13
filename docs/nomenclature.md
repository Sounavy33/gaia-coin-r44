# Nomenclatura Inteligente — Esquema e Metadados

A nomenclatura inteligente gera nomes canônicos que contêm informações úteis sobre o conteúdo sem abrir o arquivo. O objetivo é permitir indexação rápida, deduplicação e entendimento imediato.

Formato de nome canônico (exemplo):

YYYYMMDDTHHMMSSZ_userXX_box_type_hashslug_summaryslug.ext

Componentes:
- timestamp: formato ISO simplificado sem separadores (UTC)
- userXX: 6 caracteres derivado do hash do usuário
- box: violet|blue|red|black
- type: note|audio|image|doc|patch
- hashslug: primeiros 8 chars do SHA256 do conteúdo (dedupe)
- summaryslug: resumo curto slugified (até 6 palavras)

Metadados auxiliares (arquivo .meta.json):
- id: uuid
- created_at: timestamp
- created_by: user id
- origin_device: device id / descriptor
- geohash: optional (se autorizado)
- consent_flags: {health: bool, location: bool, audio: bool}
- signature: ed25519/placeholder
- embedding_id: pointer para vetor na vector store
- version: semantic

Regras:
- Nome do arquivo + .meta.json devem ser mantidos juntos.
- O hash é usado para deduplicação e verificação de integridade.
- Para privacidade, geohash e localização só são incluídos se o usuário autorizar.

Exemplo:
20261013T123045Z_a1b2c3_violet_audio_9af4e7b2_minhaspalavras.wav
20261013T123045Z_a1b2c3_violet_audio_9af4e7b2_minhaspalavras.wav.meta.json
