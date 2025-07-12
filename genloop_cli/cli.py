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

if __name__ == "__main__":
    cli()
