import re

__all__ = ["slugify"]

def slugify(value: str) -> str:
    """Return a filesystem-safe slug."""
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = value.strip("_")
    return value
