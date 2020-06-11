"""Console script for pdk8s."""
import os
import sys
import collections.abc

import yaml
import click

import pdk8s.synth
from . import k8s


option_output = click.option("--output", default="dist", type=click.Path(file_okay=False), help="Folder in which to store generated chart")
option_format = click.option("--format", "output_format", default="helm", type=click.Choice(['helm', 'kubernetes'], case_sensitive=False), help="Format of output")
option_input = click.option("--input", default="chart.py", type=click.Path(exists=True, dir_okay=False), help="Python file that generates your chart")


@click.group()
def main():
    """Console script for pdk8s."""


def add_subcommands(main, with_input):
    @main.command()

    @option_output
    @option_format
    @click.pass_context
    def synth(ctx, output, output_format, input=None):
        if input:
            chart_variables = {}
            exec(open("hello_world.py").read(), {}, chart_variables)
        else:
            chart_variables = ctx.obj

        return pdk8s.synth.synth(chart_variables, output_format, output)

    if with_input:
        option_input(synth)

    @main.command()
    def init():
        # Call cookiecutter
        print("not yet implemented")
        return 99


    @main.command()
    def watch():
        print("not yet implemented")
        return 99


add_subcommands(main, with_input=True)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
