import hashlib
import json
from typing import List, Dict, Any

def sha256_hex(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def merkle_root(leaves: List[str]) -> str:
    if not leaves:
        return ""
    level = [leaf for leaf in leaves]
    while len(level) > 1:
        next_level = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i + 1] if i + 1 < len(level) else level[i]
            next_level.append(sha256_hex(left + right))
        level = next_level
    return level[0]

def build_merkle_batch(receipts: List[Dict[str, Any]]) -> Dict[str, Any]:
    leaves = [r["content_hash"] for r in receipts]
    root = merkle_root(leaves)
    return {
        "batch_size": len(receipts),
        "merkle_root": root,
        "receipts": receipts,
    }

if __name__ == "__main__":
    sample_receipts = [
        {"content_hash": "a"},
        {"content_hash": "b"},
        {"content_hash": "c"},
        {"content_hash": "d"},
    ]
    batch = build_merkle_batch(sample_receipts)
    print(json.dumps(batch, indent=2))
