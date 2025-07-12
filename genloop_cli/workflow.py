import json
import click
from typing import Sequence
import os
import subprocess


def run_comfyui(cmd: Sequence[str]) -> None:
    """Run ComfyUI and stream its output.

    If the ``GENLOOP_COMFYUI_CMD`` environment variable is set, it will be
    executed instead of ``cmd``. This allows tests or users to supply a custom
    command.
    """
    env_cmd = os.environ.get("GENLOOP_COMFYUI_CMD")
    if env_cmd:
        click.echo(f"Running: {env_cmd}")
        process = subprocess.Popen(
            env_cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
    else:
        click.echo(f"Running: {' '.join(cmd)}")
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
        except FileNotFoundError as e:
            raise click.ClickException(f"ComfyUI not found: {cmd[0]}") from e

    assert process.stdout is not None
    for line in process.stdout:
        click.echo(line.rstrip())
    process.wait()
    if process.returncode != 0:
        raise click.ClickException(
            f"ComfyUI exited with code {process.returncode}"
        )


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
