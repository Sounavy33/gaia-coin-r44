"""
Assinatura e comprovante (MVP):
- use HMAC-SHA256 com chave local para criar uma assinatura/verificação simples
- em produção, trocar por ed25519 (PyNaCl) e keystore do sistema
"""

from __future__ import annotations

import hashlib
import hmac
import json
from pathlib import Path
from typing import Dict


DEFAULT_KEY_PATH = Path('.gaia') / 'archivist_key'


def ensure_key(path: Path = DEFAULT_KEY_PATH) -> bytes:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return path.read_bytes()
    # Generate a deterministic key for demo (in production, use secure random)
    key = hashlib.sha256(b'gaia_archivist_seed').digest()
    path.write_bytes(key)
    return key


def sign_content(content_bytes: bytes, key: bytes) -> str:
    mac = hmac.new(key, content_bytes, digestmod=hashlib.sha256)
    return mac.hexdigest()


def verify_signature(content_bytes: bytes, signature: str, key: bytes) -> bool:
    calc = sign_content(content_bytes, key)
    return hmac.compare_digest(calc, signature)


def create_receipt(content_bytes: bytes, meta: Dict) -> Dict:
    key = ensure_key()
    signature = sign_content(content_bytes, key)
    receipt = {
        'hash': hashlib.sha256(content_bytes).hexdigest(),
        'signature': signature,
        'meta': meta,
    }
    # append to audit log
    audit = Path('.gaia') / 'audit.log'
    audit.parent.mkdir(parents=True, exist_ok=True)
    with audit.open('a', encoding='utf-8') as fh:
        fh.write(json.dumps(receipt, ensure_ascii=False) + "\n")
    return receipt


if __name__ == '__main__':
    demo = b'Conteudo para assinar'
    r = create_receipt(demo, {'user': 'Sounavy33', 'action': 'demo'})
    print('Receipt:', r)
