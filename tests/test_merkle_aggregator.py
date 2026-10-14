from scripts.poc.merkle_aggregator import build_merkle_batch

def test_build_merkle_batch():
    receipts = [{"content_hash": "a"}, {"content_hash": "b"}, {"content_hash": "c"}]
    result = build_merkle_batch(receipts)
    assert result["batch_size"] == 3
    assert "merkle_root" in result
