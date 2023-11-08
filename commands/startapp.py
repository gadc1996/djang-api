import click
import subprocess
import os


@click.command()
@click.argument("app_name")
def startapp(app_name):
    """Create a new Django application within your project"""
    dir = f"project/{app_name}"

    if os.path.isdir(dir):
        click.echo()
        click.secho(f"App {app_name} already exists", fg="red")
    else:
        os.mkdir(dir)
        subprocess.run(
            ["django-admin", "startapp", app_name, dir],
            check=True,
        )
