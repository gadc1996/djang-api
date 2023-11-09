import click
import os


@click.group()
def add():
    """Add new project components using template files"""
    pass


@add.command()
@click.argument("command_name")
def command(command_name):
    """Create a new project command"""
    if os.path.exists(f"commands/{command_name}.py"):
        click.secho(f"Command {command_name} already exists", fg="red")
    else:
        with open("templates/command.txt", "r") as template:
            template = template.read()

        template = template.replace("{name}", command_name)

        with open(f"commands/{command_name}.py", "w") as file:
            file.write(template)
