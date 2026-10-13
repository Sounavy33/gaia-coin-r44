from scripts.audit_sign import create_receipt, ensure_key, verify_signature, sign_content


def test_sign_and_verify(tmp_path):
    key = ensure_key()
    data = b'teste de assinatura'
    sig = sign_content(data, key)
    ok = verify_signature(data, sig, key)
    assert ok
    r = create_receipt(data, {'user': 'test'})
    assert 'signature' in r and 'hash' in r
