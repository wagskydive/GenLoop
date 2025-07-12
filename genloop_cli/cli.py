import click

from .workflow import (
    load_workflow,
    validate_workflow,
    parse_overrides,
    apply_overrides,
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
def characters(workflow, override):
    """Generate character assets."""
    if workflow:
        data = load_workflow(workflow)
        overrides = parse_overrides(override)
        data = apply_overrides(data, overrides)
        validate_workflow(data)
    click.echo("Generating characters...")


@generate.command()
@click.option("--workflow", type=click.Path(), help="Workflow JSON file")
@click.option("--override", multiple=True, help="Override node value key=value")
def items(workflow, override):
    """Generate item assets."""
    if workflow:
        data = load_workflow(workflow)
        overrides = parse_overrides(override)
        data = apply_overrides(data, overrides)
        validate_workflow(data)
    click.echo("Generating items...")


@generate.command()
@click.option("--workflow", type=click.Path(), help="Workflow JSON file")
@click.option("--override", multiple=True, help="Override node value key=value")
def environments(workflow, override):
    """Generate environment assets."""
    if workflow:
        data = load_workflow(workflow)
        overrides = parse_overrides(override)
        data = apply_overrides(data, overrides)
        validate_workflow(data)
    click.echo("Generating environments...")

if __name__ == "__main__":
    cli()
