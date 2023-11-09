import click
import subprocess
import os

PROJECT_DIR = "project"


@click.group()
def app():
    """Manage project apps"""


@app.command()
@click.argument("app_name")
def add(app_name: str):
    """Add a new app to the project"""
    app_dir = os.path.join(PROJECT_DIR, app_name)

    if os.path.isdir(app_dir):
        click.secho(f"App {app_name} already exists", fg="red")
    else:
        os.mkdir(app_dir)
        subprocess.run(["django-admin", "startapp", app_name, app_dir], check=True)
        add_app_to_settings(app_name)


@app.command()
@click.argument("app_name")
def remove(app_name: str):
    """Remove an app from the project"""
    app_dir = os.path.join(PROJECT_DIR, app_name)

    if os.path.isdir(app_dir):
        subprocess.run(["rm", "-r", app_dir], check=True)
        remove_app_from_settings(app_name)
    else:
        click.secho(f"App {app_name} does not exist", fg="red")


def add_app_to_settings(app_name: str) -> None:
    settings_path = os.path.join(PROJECT_DIR, "project/settings.py")
    app_name_to_add = f"    '{app_name}',"

    with open(settings_path, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("INSTALLED_APPS = ["):
            lines.insert(i + 1, app_name_to_add + "\n")
            break

    with open(settings_path, "w") as file:
        file.writelines(lines)


def remove_app_from_settings(app_name: str) -> None:
    settings_path = os.path.join(PROJECT_DIR, "project/settings.py")

    with open(settings_path, "r") as file:
        lines = file.readlines()

    updated_lines = []
    app_found = False

    for line in lines:
        if line.strip() == f"'{app_name}',":
            app_found = True
            continue
        updated_lines.append(line)

    if app_found:
        with open(settings_path, "w") as file:
            file.writelines(updated_lines)


if __name__ == "__main__":
    app()
