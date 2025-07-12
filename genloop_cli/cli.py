import click

@click.group()
def cli():
    """GenLoop command line interface."""
    pass

@cli.command()
def version():
    """Show the GenLoop version."""
    click.echo("GenLoop version 0.1.0")

if __name__ == "__main__":
    cli()
