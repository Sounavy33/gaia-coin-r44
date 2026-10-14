import hashlib
import json
import time
from dataclasses import dataclass, asdict
from typing import Any, Dict

@dataclass
class Receipt:
    device_id: str
    action_type: str
    payload: str
    timestamp: str
    nonce: str

    def to_payload(self) -> Dict[str, Any]:
        return asdict(self)

    def content_hash(self) -> str:
        raw = json.dumps(self.to_payload(), sort_keys=True).encode("utf-8")
        return "sha256:" + hashlib.sha256(raw).hexdigest()

    def sign(self, private_key: str) -> str:
        # placeholder signature for prototype
        payload = json.dumps(self.to_payload(), sort_keys=True) + "|" + private_key
        return "ed25519:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()

def generate_receipt(device_id: str, action_type: str, payload: str, private_key: str) -> Dict[str, Any]:
    receipt = Receipt(
        device_id=device_id,
        action_type=action_type,
        payload=payload,
        timestamp=str(time.time()),
        nonce=hashlib.sha256(f"{device_id}:{time.time()}".encode("utf-8")).hexdigest()[:16],
    )

    return {
        "device_id": receipt.device_id,
        "action_type": receipt.action_type,
        "payload": receipt.payload,
        "timestamp": receipt.timestamp,
        "nonce": receipt.nonce,
        "content_hash": receipt.content_hash(),
        "signature": receipt.sign(private_key),
    }

if __name__ == "__main__":
    sample = generate_receipt(
        device_id="device-001",
        action_type="processing",
        payload="sample contribution",
        private_key="demo-private-key",
    )
    print(json.dumps(sample, indent=2))
