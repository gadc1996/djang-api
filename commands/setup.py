import click
import subprocess
import os
import shutil


@click.command()
def setup():
    """Setup project dependencies and configurations"""
    subprocess.run(["pre-commit", "install"], check=True)

    subprocess.run(["cli", "db", "migrate"])
