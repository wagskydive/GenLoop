from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class AssetLogger:
    """Append asset metadata entries to a JSON log file."""

    path: str = "asset_log.json"
    entries: List[Dict] = field(default_factory=list)

    def load(self) -> None:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.entries = json.load(f)
        except FileNotFoundError:
            self.entries = []

    def log(self, data: Dict) -> None:
        self.load()
        self.entries.append(data)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.entries, f, indent=2)
