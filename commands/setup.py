import click
import subprocess
import os
import shutil


@click.command()
def setup():
    """Setup project dependencies and configurations"""
    if not os.path.exists(".env"):
        click.secho("No env file detected, copying example file", fg="red")
        shutil.copy(".env.example", ".env")
        click.secho("Env file created", fg="green")
    else:
        click.secho("Env file detected", fg="green")

    subprocess.run(["pre-commit", "install"], check=True)

    subprocess.run(["cli", "db", "migrate"])
