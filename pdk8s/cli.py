"""Console script for pdk8s."""
import os
import sys
import collections.abc

import yaml
import click

import pdk8s.synth
from . import k8s


option_input = click.option("-i", "--input", "input_path", default="chart.py", type=click.Path(exists=True, dir_okay=False), help="Python file that generates your chart")
option_output = click.option("-o", "--output", "output_path", default="dist", type=click.Path(file_okay=False), help="Folder in which to store generated chart")
option_format = click.option("--format", "output_format", default="helm", type=click.Choice(['helm', 'kubernetes'], case_sensitive=False), help="Format of output")


@click.group()
def main():
    """Console script for pdk8s."""


def load_chart_from_file(path):
    chart_variables = {}
    exec(open(path).read(), {}, chart_variables)
    return chart_variables


def add_subcommands(main, with_input):
    @main.command()

    @option_output
    @option_format
    @click.pass_context
    def synth(ctx, output_path, output_format, input_path=None):
        if input_path:
            chart_variables = load_chart_from_file(input_path)
        else:
            chart_variables = ctx.obj

        return pdk8s.synth.synth(chart_variables, output_format, output_path)

    if with_input:
        option_input(synth)

    @main.command()
    def init():
        import pkg_resources
        import cookiecutter.main

        path = pkg_resources.resource_filename("pdk8s", "cookiecutter")
        cookiecutter.main.cookiecutter(path)

    @main.command()
    def watch():
        print("not yet implemented")
        return 99


add_subcommands(main, with_input=True)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
