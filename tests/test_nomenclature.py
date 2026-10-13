from scripts.nomenclature import canonical_filename, metadata_for_file


def test_canonical_filename_consistency():
    user = 'user-test'
    data = b'conteudo'
    fname = canonical_filename(user, 'violet', 'doc', data, 'minha nota', 'txt')
    assert 'violet' in fname
    assert fname.endswith('.txt')


def test_metadata_contains_keys():
    user = 'user-test'
    data = b'conteudo'
    meta = metadata_for_file(user, 'device-1', 'blue', 'note', data, 'minha nota')
    assert 'id' in meta and 'created_at' in meta and 'short_hash' in meta
