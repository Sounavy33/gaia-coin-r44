"""
Gerenciador de dicionário pessoal (bilingue por padrão).

Armazena entradas em .gaia/dictionary.json
Formato simplificado:
[{
  'id': 'uuid',
  'canonical': 'texto',
  'variants': [],
  'language': 'pt',
  'translations': ['en ...'],
  'usage_count': 1,
  'first_seen': 'iso',
  'last_seen': 'iso'
}]
"""

from __future__ import annotations

import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Optional


class DictionaryManager:
    def __init__(self, path: Optional[str] = None, bilingual: bool = True):
        self.path = Path(path) if path else Path('.gaia') / 'dictionary.json'
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.bilingual = bilingual
        self._load()

    def _load(self):
        if not self.path.exists():
            self.data = []
            return
        try:
            self.data = json.loads(self.path.read_text(encoding='utf-8'))
        except Exception:
            self.data = []

    def _save(self):
        self.path.write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding='utf-8')

    def add_entry(self, canonical_phrase: str, variants: List[str] = None, language: str = 'pt', translations: List[str] = None) -> dict:
        variants = variants or []
        translations = translations or ([] if self.bilingual else [])
        now = datetime.utcnow().isoformat() + 'Z'
        # find existing
        for e in self.data:
            if e.get('canonical') == canonical_phrase:
                e['variants'] = sorted(list(set(e.get('variants', []) + variants)))
                e['translations'] = sorted(list(set(e.get('translations', []) + translations)))
                e['usage_count'] = e.get('usage_count', 0) + 1
                e['last_seen'] = now
                self._save()
                return e
        entry = {
            'id': str(uuid.uuid4()),
            'canonical': canonical_phrase,
            'variants': variants,
            'language': language,
            'translations': translations,
            'usage_count': 1,
            'first_seen': now,
            'last_seen': now,
        }
        self.data.append(entry)
        self._save()
        return entry

    def lookup(self, text: str) -> Optional[dict]:
        for e in self.data:
            if e.get('canonical') == text or text in e.get('variants', []):
                return e
        return None

    def export(self, out_path: str):
        Path(out_path).write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    dm = DictionaryManager()
    print(dm.add_entry('Olá, tudo bem?', ['Oi tudo bem'], 'pt', ['Hello, how are you?']))
