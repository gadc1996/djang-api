import click
import importlib
import os


@click.group()
def cli():
    """Command líne interface for project development""" 
    pass


# Dynamically import and register commands from the 'commands' directory
commands_folder = "commands"
for command_file in os.listdir(commands_folder):
    if command_file.endswith(".py") and command_file != "__init__.py":
        command_module = importlib.import_module(
            f"{commands_folder}.{command_file[:-3]}"
        )
        cli.add_command(getattr(command_module, command_file[:-3]))

if __name__ == "__main__":
    cli()
