import json
import click


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
