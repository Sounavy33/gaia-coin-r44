from scripts.poc.receipt_tool import generate_receipt

def test_generate_receipt():
    receipt = generate_receipt(
        device_id="device-1",
        action_type="processing",
        payload="demo",
        private_key="secret"
    )
    assert "content_hash" in receipt
    assert "signature" in receipt
    assert receipt["device_id"] == "device-1"
