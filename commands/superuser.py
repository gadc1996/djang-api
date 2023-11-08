import click
import subprocess

@click.command()
def superuser():
    """Create a superuser account with administrative privileges."""
    subprocess.run(
        [
            "python",
            "project/manage.py",
            "createsuperuser",
            "--no-input",
        ],
        check=True,
    )