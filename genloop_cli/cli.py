import click

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
def characters():
    """Generate character assets."""
    click.echo("Generating characters...")


@generate.command()
def items():
    """Generate item assets."""
    click.echo("Generating items...")


@generate.command()
def environments():
    """Generate environment assets."""
    click.echo("Generating environments...")

if __name__ == "__main__":
    cli()
