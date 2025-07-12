from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class SlotMemory:
    """Persist mapping of slot names to locked style tags."""

    path: str = "slots.json"
    slots: Dict[str, str] = field(default_factory=dict)

    def load(self) -> Dict[str, str]:
        """Load slot memory from ``path`` if it exists."""
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.slots = json.load(f)
        except FileNotFoundError:
            self.slots = {}
        return self.slots

    def save(self) -> None:
        """Save slot memory to ``path``."""
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.slots, f, indent=2)

    def lock_style(self, slot: str, style: str) -> None:
        """Assign ``style`` to ``slot``."""
        self.slots[slot] = style

    def unlock_style(self, slot: str) -> None:
        """Remove any locked style from ``slot``."""
        self.slots.pop(slot, None)
