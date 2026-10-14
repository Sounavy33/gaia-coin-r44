import json

def verify_claim(receipt: dict, merkle_root: str, proof_path: list) -> bool:
    # protótipo simplificado
    # aqui, em produção, o usuário apresentaria proof path real com Merkle
    if "content_hash" not in receipt:
        return False
    if receipt["content_hash"] and merkle_root:
        return True
    return False

def simulate_claim(receipt: dict, merkle_root: str, proof_path: list, current_balance: float) -> dict:
    approved = verify_claim(receipt, merkle_root, proof_path)
    if not approved:
        return {
            "approved": False,
            "balance": current_balance,
            "reason": "invalid claim",
        }

    claimed = 10.0
    return {
        "approved": True,
        "amount": claimed,
        "balance": current_balance + claimed,
        "reason": "valid merkle proof",
    }

if __name__ == "__main__":
    receipt = {
        "content_hash": "abc123",
    }
    result = simulate_claim(receipt, "merkle-root-demo", [], 0.0)
    print(json.dumps(result, indent=2))
