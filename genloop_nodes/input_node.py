from dataclasses import dataclass

__all__ = ["GenLoopInputNode"]

@dataclass
class GenLoopInputNode:
    """Minimal representation of the GenLoopInputNode."""

    prompt: str
    style_tag: str = ""
    asset_type: str = ""
    variant_count: int = 1
    output_path: str = ""
    check_existing: bool = True

    def prepare(self) -> dict:
        formatted = f"{self.style_tag} {self.prompt}".strip()
        metadata = {
            "prompt": self.prompt,
            "style_tag": self.style_tag,
            "asset_type": self.asset_type,
        }
        return {
            "formatted_prompt": formatted,
            "metadata": metadata,
            "current_prompt": formatted,
        }
