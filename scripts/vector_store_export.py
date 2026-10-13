"""
Vector store export/import helper (stub)

This module defines a compact JSON export/import format for a small local vector store
used as Gaia's memory. The MVP stores vectors as base64-encoded bytes or placeholder floats.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Any


def export_vector_store(vectors: List[Dict[str, Any]], out_path: str) -> None:
    p = Path(out_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w', encoding='utf-8') as fh:
        json.dump({'vectors': vectors}, fh, ensure_ascii=False, indent=2)


def import_vector_store(in_path: str) -> List[Dict[str, Any]]:
    p = Path(in_path)
    if not p.exists():
        return []
    with p.open('r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data.get('vectors', [])


if __name__ == '__main__':
    demo = [
        {'id': 'v1', 'text': 'Minha primeira memória', 'embedding': [0.1, 0.2, 0.3], 'meta': {'source': 'user'}},
    ]
    export_vector_store(demo, '.gaia/demo_vectors.json')
    print('Exported demo vectors')
