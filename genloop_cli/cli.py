import click
import json

from .workflow import (
    load_workflow,
    validate_workflow,
    parse_overrides,
    apply_overrides,
    run_comfyui,
)

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
@click.option("--override", multiple=True, help="Override node value key=value")
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
@click.option("--override", multiple=True, help="Override node value key=value")
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
@click.option("--override", multiple=True, help="Override node value key=value")
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

if __name__ == "__main__":
    cli()
