import click
import subprocess


@click.command()
def lint():
    """Lint all python files in current project"""
    subprocess.run(["black", "."])
