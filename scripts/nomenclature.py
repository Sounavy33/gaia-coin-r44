"""
Utilitário para gerar nomenclatura inteligente e metadados.
"""

from __future__ import annotations

import hashlib
import json
import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict


def _slugify(text: str, max_words: int = 6) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    words = [w for w in text.split() if w]
    return "_".join(words[:max_words])[:80]


def short_user_id(user_id: str) -> str:
    h = hashlib.sha256(user_id.encode("utf-8")).hexdigest()
    return h[:6]


def content_short_hash(content_bytes: bytes) -> str:
    return hashlib.sha256(content_bytes).hexdigest()[:8]


def canonical_filename(user_id: str, box: str, ftype: str, content_bytes: bytes, summary: str, ext: str) -> str:
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    uid = short_user_id(user_id)
    h = content_short_hash(content_bytes)
    slug = _slugify(summary)
    return f"{ts}_{uid}_{box}_{ftype}_{h}_{slug}.{ext}"


def metadata_for_file(user_id: str, origin_device: str, box: str, ftype: str, content_bytes: bytes, summary: str, extra: Dict = None) -> Dict:
    meta = {
        "id": str(uuid.uuid4()),
        "created_at": datetime.utcnow().isoformat() + "Z",
        "created_by": user_id,
        "origin_device": origin_device,
        "box": box,
        "type": ftype,
        "short_hash": content_short_hash(content_bytes),
        "summary": summary,
        "consent_flags": {"health": False, "location": False, "audio": False},
        "version": "0.1.0",
    }
    if extra:
        meta.update(extra)
    return meta


def save_file_with_meta(path: str, content_bytes: bytes, meta: Dict) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(content_bytes)
    meta_path = p.with_name(p.name + ".meta.json")
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == '__main__':
    # Demo
    user = "Sounavy33"
    data = b"Conteudo de exemplo"
    fname = canonical_filename(user, "violet", "doc", data, "Resumo do documento", "txt")
    meta = metadata_for_file(user, "telefone-01", "violet", "doc", data, "Resumo do documento")
    save_file_with_meta(fname, data, meta)
    print("Saved:", fname)
