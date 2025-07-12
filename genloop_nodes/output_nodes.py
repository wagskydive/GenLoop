from __future__ import annotations
import json
import os
from dataclasses import dataclass, field

from .utils import safe_path
from .asset_log import AssetLogger

__all__ = [
    "GenLoopOutputNode",
    "GenLoopOutputCharacterNode",
    "GenLoopOutputItemNode",
    "GenLoopOutputEnvironmentNode",
]


@dataclass
class GenLoopOutputNode:
    """Base class for GenLoop output nodes."""

    output_dir: str = "outputs"
    file_prefix: str = ""
    asset_type: str = field(init=False, default="")

    def _make_path(self, name: str) -> str:
        name = safe_path(name)
        os.makedirs(self.output_dir, exist_ok=True)
        return os.path.join(self.output_dir, f"{self.file_prefix}{name}.png")

    def save(self, image: bytes, metadata: dict, name: str = "output") -> str:
        path = self._make_path(name)
        with open(path, "wb") as f:
            f.write(image)
        with open(path + ".json", "w", encoding="utf-8") as f:
            json.dump(metadata, f)
        AssetLogger().log({"path": path, "metadata": metadata})
        return path


class GenLoopOutputCharacterNode(GenLoopOutputNode):
    asset_type: str = "character"


class GenLoopOutputItemNode(GenLoopOutputNode):
    asset_type: str = "item"


class GenLoopOutputEnvironmentNode(GenLoopOutputNode):
    asset_type: str = "environment"
