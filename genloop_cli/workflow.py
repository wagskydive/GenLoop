import json
import click
from typing import Sequence


def run_comfyui(cmd: Sequence[str]) -> None:
    """Placeholder to invoke ComfyUI."""
    quoted = ' '.join(cmd)
    click.echo(f"Would run: {quoted}")


def load_workflow(path: str) -> dict:
    """Load a workflow JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise click.ClickException(f"Workflow file not found: {path}") from e
    except json.JSONDecodeError as e:
        raise click.ClickException(f"Invalid workflow JSON: {e}") from e
    click.echo(f"Loaded workflow from {path}")
    return data


def validate_workflow(data: dict) -> None:
    """Validate presence of required GenLoop nodes."""
    nodes = data.get("nodes", [])
    has_input = any(n.get("type") == "GenLoopInputNode" for n in nodes)
    has_output = any(str(n.get("type", "")).startswith("GenLoopOutput") for n in nodes)
    if not (has_input and has_output):
        raise click.ClickException("Invalid workflow: missing GenLoop nodes")


def parse_overrides(values: tuple[str]) -> dict:
    """Parse key=value pairs from CLI."""
    overrides: dict[str, str] = {}
    for item in values:
        if '=' not in item:
            raise click.ClickException(f"Invalid override '{item}' (expected key=value)")
        key, value = item.split('=', 1)
        overrides[key] = value
    return overrides


def apply_overrides(data: dict, overrides: dict) -> dict:
    """Apply overrides to workflow data for now by storing them."""
    if overrides:
        data.setdefault('overrides', {}).update(overrides)
        click.echo(f"Applied overrides: {overrides}")
    return data
