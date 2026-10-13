"""
Pipeline de transcrição e redução — MVP stub.

- asr_stub(audio_path) -> raw transcription (pt)
- reduce_text(text, max_sentences) -> extractive reduction
- translate_stub(text, target_lang) -> placeholder translation
- process_audio_pipeline(audio_path, user_id, dict_manager) -> performs flow and updates dictionary
"""

from __future__ import annotations

import re
from typing import Optional

from scripts import nomenclature
from scripts.dictionary_manager import DictionaryManager


def asr_stub(audio_path: str) -> str:
    # Placeholder ASR: read a .txt with same name for demo
    try:
        txt = open(audio_path.replace('.wav', '.txt'), 'r', encoding='utf-8').read().strip()
        return txt
    except Exception:
        # fallback
        return "[ASR] áudio transcrito automaticamente (demo)"


def _split_sentences(text: str):
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p for p in parts if p]


def reduce_text(text: str, max_sentences: int = 2) -> str:
    sents = _split_sentences(text)
    if not sents:
        return text[:160]
    return ' '.join(sents[:max(1, min(max_sentences, len(sents)))])


def translate_stub(text: str, target_lang: str = 'en') -> str:
    # Simple placeholder
    return f"[{target_lang}] " + text


def process_audio_pipeline(audio_path: str, user_id: str, dict_path: Optional[str] = None):
    dm = DictionaryManager(dict_path) if dict_path else DictionaryManager()
    raw = asr_stub(audio_path)
    reduced = reduce_text(raw, 2)
    translation = translate_stub(reduced, 'en')
    # Update dictionary with short phrases
    dm.add_entry(canonical_phrase=reduced, variants=[raw], language='pt', translations=[translation])
    return {
        'raw': raw,
        'reduced': reduced,
        'translation': translation,
    }


if __name__ == '__main__':
    print(process_audio_pipeline('example.wav', 'Sounavy33'))
