import click
import inflect
import os
import subprocess
from jinja import Jinja

plural = inflect.engine().plural


@click.group()
def make():
    """Add new project component"""
    pass


@make.command()
def migrations():
    """Create database migration files"""
    subprocess.run(["python", "project/manage.py", "migrate"], check=True)


@make.command()
@click.argument("name")
def command(name):
    """Create a new project command"""
    file_path = os.path.join("commands", f"{name}.py")
    if os.path.exists(file_path):
        click.secho(f"Command {name} already exists", fg="red")
    else:
        try:
            output = Jinja.render("command", {"name": name})
            with open(file_path, "w") as f:
                f.write(output)
            click.echo("Command created successfully", fg="green")
        except Exception as e:
            click.secho(f"Error creating command: {str(e)}", fg="red")


@make.command()
@click.argument("name")
def serializer(name):
    """Create a new model serializer"""
    plural_name = plural(name)

    file_path = os.path.join("project", plural_name, "serializers.py")
    if os.path.exists(file_path):
        click.secho("Serializer already exists", fg="red")
    else:
        try:
            output = Jinja.render("serializer", {"name": name})
            with open(file_path, "w") as f:
                f.write(output)
            click.secho("Serializer created successfully", fg="green")
        except Exception as e:
            click.secho(f"Error creating serializer: {str(e)}", fg="red")
