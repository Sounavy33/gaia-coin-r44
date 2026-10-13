# Gaia local MVP
# Arquitetura local e autônoma para o ecossistema SOUNAVY Simbiose.
# O objetivo é priorizar operação local, contexto humano e sistemas opcionais de rede.

"""Módulo de migração e adaptadores para Gaia.

- Exporta/importa um pequeno pacote de adapter.
- Exporta/importa memória vetorial portátil.
- Mantém a lógica de atualização offline e migração entre modelos.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import zipfile
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_KEY_PATH = Path('.gaia') / 'adapter_key'


def ensure_key(path: Path = DEFAULT_KEY_PATH) -> bytes:
    path.parent.mkdir(exist_ok=True)
    if path.exists():
        return path.read_bytes()
    key = hashlib.sha256(b'gaia_adapter_secret_seed').digest()
    path.write_bytes(key)
    return key


def sign_payload(payload_bytes: bytes, key: bytes) -> str:
    mac = hmac.new(key, payload_bytes, digestmod=hashlib.sha256)
    return mac.hexdigest()


def export_adapter(adapter_meta: Dict[str, Any], adapter_files: Dict[str, bytes], out_path: str) -> str:
    key = ensure_key()
    manifest = dict(adapter_meta)
    manifest_bytes = json.dumps(manifest, ensure_ascii=False).encode('utf-8')
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w') as zf:
        zf.writestr('manifest.json', manifest_bytes)
        for fname, content in adapter_files.items():
            zf.writestr(f'adapter/{fname}', content)
    blob = out.read_bytes()
    signature = sign_payload(blob, key)
    sig_path = out.with_suffix(out.suffix + '.sig')
    sig_path.write_text(signature, encoding='utf-8')
    return str(out)


def verify_adapter_package(zip_path: str) -> bool:
    key = ensure_key()
    p = Path(zip_path)
    sig_path = p.with_suffix(p.suffix + '.sig')
    if not p.exists() or not sig_path.exists():
        return False
    expected = sig_path.read_text(encoding='utf-8').strip()
    blob = p.read_bytes()
    calc = sign_payload(blob, key)
    return hmac.compare_digest(calc, expected)


def import_adapter(zip_path: str, dest_dir: str) -> Dict[str, Any]:
    if not verify_adapter_package(zip_path):
        raise RuntimeError('Adapter signature invalid')
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(dest)
    manifest_path = dest / 'manifest.json'
    if not manifest_path.exists():
        raise RuntimeError('Manifest not found in adapter')
    return json.loads(manifest_path.read_text(encoding='utf-8'))


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


__all__ = ['export_adapter', 'verify_adapter_package', 'import_adapter', 'export_vector_store', 'import_vector_store']
