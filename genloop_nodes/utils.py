import re

__all__ = ["slugify", "safe_path"]

def slugify(value: str) -> str:
    """Return a filesystem-safe slug."""
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = value.strip("_")
    return value


def safe_path(path: str) -> str:
    """Return a path safe for file operations."""
    return re.sub(r"[^a-zA-Z0-9_/.-]", "_", path)
