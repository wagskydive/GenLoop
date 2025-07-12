import click

from .workflow import load_workflow, validate_workflow

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
def characters(workflow):
    """Generate character assets."""
    if workflow:
        data = load_workflow(workflow)
        validate_workflow(data)
    click.echo("Generating characters...")


@generate.command()
@click.option("--workflow", type=click.Path(), help="Workflow JSON file")
def items(workflow):
    """Generate item assets."""
    if workflow:
        data = load_workflow(workflow)
        validate_workflow(data)
    click.echo("Generating items...")


@generate.command()
@click.option("--workflow", type=click.Path(), help="Workflow JSON file")
def environments(workflow):
    """Generate environment assets."""
    if workflow:
        data = load_workflow(workflow)
        validate_workflow(data)
    click.echo("Generating environments...")

if __name__ == "__main__":
    cli()
