# Gaia Edge MVP
# Arquitetura local e autônoma para o ecossistema SOUNAVY Simbiose.
# Prioriza operação local, contexto humano, e integração com o Bill no GitHub.

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


class GaiaContext:
    def __init__(self, user_name: str = "Sounavy", storage_dir: Optional[str] = None):
        self.user_name = user_name
        self.storage_dir = Path(storage_dir) if storage_dir else Path(".gaia")
        self.storage_dir.mkdir(exist_ok=True)
        self.history: List[Dict[str, Any]] = []
        self.preferences: Dict[str, Any] = {
            "language": "pt",
            "persona": "amigável",
            "offline_first": True,
            "allow_online": False,
        }
        self.load()

    def _file_path(self) -> Path:
        return self.storage_dir / "context.json"

    def add(self, role: str, text: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        entry = {
            "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "role": role,
            "text": text,
            "metadata": metadata or {},
        }
        self.history.append(entry)
        self.save()
        return entry

    def summarize(self, limit: int = 5) -> str:
        if not self.history:
            return "Sem contexto registrado ainda."
        recent = self.history[-limit:]
        parts = [entry["text"] for entry in recent if entry["text"].strip()]
        return " | ".join(parts)

    def save(self) -> None:
        payload = {
            "user_name": self.user_name,
            "preferences": self.preferences,
            "history": self.history,
        }
        self._file_path().write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def load(self) -> None:
        p = self._file_path()
        if not p.exists():
            return
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            self.user_name = data.get("user_name", self.user_name)
            self.preferences.update(data.get("preferences", {}))
            self.history = data.get("history", [])
        except Exception:
            self.history = []

    def export(self) -> Dict[str, Any]:
        return {
            "user_name": self.user_name,
            "preferences": self.preferences,
            "history": self.history,
        }


class GaiaLLMAdapter:
    def __init__(self, model_path: Optional[str] = None, allow_online: bool = False):
        self.model_path = model_path
        self.allow_online = allow_online

    def is_local_available(self) -> bool:
        return bool(self.model_path and Path(self.model_path).exists())

    def infer(self, prompt: str, lang: str = "pt") -> str:
        if self.is_local_available():
            return f"[LLM LOCAL] ({lang}) Resposta do modelo local para: {prompt[:160]}"
        if self.allow_online:
            return f"[LLM ONLINE] ({lang}) Resposta via rede para: {prompt[:160]}"
        return (
            f"[MODO OFFLINE] ({lang}) Sem modelo local ativado. "
            "Gaia continua operando em modo seguro e local, sem depender de API externa."
        )


class GaiaReport:
    def __init__(self, context: GaiaContext, adapter: GaiaLLMAdapter):
        self.context = context
        self.adapter = adapter

    def _hash_text(self, text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def build(self, prompt: str, lang: str = "pt") -> Dict[str, Any]:
        summary = self.context.summarize(limit=5)
        answer = self.adapter.infer(prompt, lang=lang)
        report = {
            "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "user": self.context.user_name,
            "language": lang,
            "prompt": prompt,
            "summary": summary,
            "answer": answer,
            "hash": self._hash_text(prompt + answer + summary),
            "mode": "local" if not self.adapter.allow_online else "hybrid",
        }
        return report


__all__ = ["GaiaContext", "GaiaLLMAdapter", "GaiaReport"]
