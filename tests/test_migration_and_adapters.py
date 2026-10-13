from pathlib import Path

from scripts.adapter_manager import export_adapter, verify_adapter_package, import_adapter
from scripts.vector_store_export import export_vector_store, import_vector_store


def test_adapter_export_and_verify(tmp_path: Path):
    meta = {'adapter_id': 'test-001', 'base_model': '1.3b', 'author': 'tester', 'created_at': '2026-01-01'}
    files = {'README.patch': b'Test adapter'}
    out = tmp_path / 'adapter.zip'
    p = export_adapter(meta, files, str(out))
    assert Path(p).exists()
    assert verify_adapter_package(p)
    dest = tmp_path / 'import'
    manifest = import_adapter(p, str(dest))
    assert manifest['adapter_id'] == 'test-001'


def test_vector_export_import(tmp_path: Path):
    vectors = [
        {'id': 'v1', 'text': 'hello', 'embedding': [0.1, 0.2], 'meta': {}},
    ]
    out = tmp_path / 'vectors.json'
    export_vector_store(vectors, str(out))
    loaded = import_vector_store(str(out))
    assert len(loaded) == 1
