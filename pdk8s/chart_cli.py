import click

from . import cli

@click.group()
def main():
    pass


cli.add_subcommands(main, with_input=False)
