from scripts.poc.claim_simulator import simulate_claim

def test_simulate_claim():
    receipt = {"content_hash": "abc123"}
    result = simulate_claim(receipt, "merkle-root-demo", [], 0.0)
    assert result["approved"] is True
    assert result["balance"] >= 10.0
