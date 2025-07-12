import click
import json

from .workflow import (
    load_workflow,
    validate_workflow,
    parse_overrides,
    apply_overrides,
    run_comfyui,
)
from .packaging import run_pyinstaller, bundle_workflows


@click.group()
def cli():
    """GenLoop command line interface."""
    pass


@cli.command()
def version():
    """Show the GenLoop version."""
    click.echo("GenLoop version 0.1.0")


@cli.group()
def generate():
    """Asset generation commands."""
    pass


@generate.command()
@click.option("--workflow", type=click.Path(), help="Workflow JSON file")
@click.option(
    "--override",
    multiple=True,
    help="Override node key=value",
)
@click.option("--debug", is_flag=True, help="Show debug information")
def characters(workflow, override, debug):
    """Generate character assets."""
    if workflow:
        data = load_workflow(workflow)
        overrides = parse_overrides(override)
        data = apply_overrides(data, overrides)
        validate_workflow(data)
        if debug:
            click.echo(json.dumps(data, indent=2))
        run_comfyui(["comfyui", "--workflow", workflow])
    click.echo("Generating characters...")


@generate.command()
@click.option("--workflow", type=click.Path(), help="Workflow JSON file")
@click.option(
    "--override",
    multiple=True,
    help="Override node key=value",
)
@click.option("--debug", is_flag=True, help="Show debug information")
def items(workflow, override, debug):
    """Generate item assets."""
    if workflow:
        data = load_workflow(workflow)
        overrides = parse_overrides(override)
        data = apply_overrides(data, overrides)
        validate_workflow(data)
        if debug:
            click.echo(json.dumps(data, indent=2))
        run_comfyui(["comfyui", "--workflow", workflow])
    click.echo("Generating items...")


@generate.command()
@click.option("--workflow", type=click.Path(), help="Workflow JSON file")
@click.option(
    "--override",
    multiple=True,
    help="Override node key=value",
)
@click.option("--debug", is_flag=True, help="Show debug information")
def environments(workflow, override, debug):
    """Generate environment assets."""
    if workflow:
        data = load_workflow(workflow)
        overrides = parse_overrides(override)
        data = apply_overrides(data, overrides)
        validate_workflow(data)
        if debug:
            click.echo(json.dumps(data, indent=2))
        run_comfyui(["comfyui", "--workflow", workflow])
    click.echo("Generating environments...")


@cli.command()
@click.option("--target", type=click.Choice(["cli", "gui"]), default="cli")
@click.option("--dist", type=click.Path(), default="dist")
def package(target: str, dist: str) -> None:
    """Package the selected application using PyInstaller."""
    if target == "cli":
        entry = "genloop_cli/__main__.py"
        name = "genloop-cli"
    else:
        entry = "genloop_gui/main.py"
        name = "genloop-gui"
    run_pyinstaller(entry, name, dist)
    bundle_workflows(dist)


if __name__ == "__main__":
    cli()
