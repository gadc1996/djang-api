import click
import subprocess


@click.command()
def serve():
    """Launch django development server"""
    subprocess.run(["python", "project/manage.py", "runserver"])
