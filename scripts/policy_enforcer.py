#!/usr/bin/env python3
"""Policy enforcer for Gaia local, with transparent and auditable safety decisions.

This module applies a simple local safety policy to prompt/answer content. It is not a
replacement for legal advice or a full moderation stack, but it offers a practical
layer for transparent local governance.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class GaiaPolicyEnforcer:
    def __init__(self, policy_path: str = "policy.json"):
        self.policy_path = Path(policy_path)
        self.policy = self._load_policy()

    def _load_policy(self) -> Dict[str, Any]:
        if not self.policy_path.exists():
            return {"mode": "balanced", "rules": []}
        with self.policy_path.open("r", encoding="utf-8") as fh:
            return json.load(fh)

    def evaluate(self, text: str) -> Dict[str, Any]:
        text_l = text.lower()
        for rule in self.policy.get("rules", []):
            matches = rule.get("match", [])
            for keyword in matches:
                if keyword.lower() in text_l:
                    return {
                        "verdict": rule.get("type", "allow"),
                        "rule_id": rule.get("id", "unknown"),
                        "message": rule.get("message", "Policy rule triggered."),
                    }
        return {"verdict": "allow", "rule_id": "none", "message": "No blocking rule triggered."}

    def safe_reply(self, text: str, fallback: str = "Eu não posso ajudar com isso.") -> str:
        result = self.evaluate(text)
        verdict = result["verdict"]
        if verdict == "block":
            return fallback
        if verdict == "warn":
            return "Aviso: a resposta foi ajustada para evitar assédio ou abuso.\n\n" + text
        return text


__all__ = ["GaiaPolicyEnforcer"]
