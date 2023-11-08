import click
import subprocess

@click.command()
def migrate():
    """Updates your database schema to match your models."""
    subprocess.run(["python", "project/manage.py", "migrate"], check=True)