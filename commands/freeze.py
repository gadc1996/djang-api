import click
import subprocess


@click.command()
def freeze():
    """Freeze project dependencies into requirements.txt file"""
    pip_freeze_output = subprocess.check_output(["pip", "freeze"], text=True)

    # Filter out lines containing '-e' (editable packages)
    filtered_lines = [
        line for line in pip_freeze_output.splitlines() if not line.startswith("-e")
    ]

    # Write the filtered lines to requirements.txt
    with open("requirements.txt", "w") as requirements_file:
        requirements_file.write("\n".join(filtered_lines))
