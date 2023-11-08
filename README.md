# Django REST Api
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Setting Up

To set up your development environment for this project, follow these steps:

1. Install [Visual Studio Code Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

   You can install this extension from the Visual Studio Code Marketplace. It allows you to develop in a Docker container, which is useful for isolating your project's dependencies and ensuring consistency across different development environments.

2. Clone the Repository

   Clone this project repository to your local machine using Git. You can use the following command:

   ```shell
   git clone https://github.com/gadc1996/django-api
   
   Navigate to the Project Folder
   ```

## Cli

The project includes a cli utility, powered by [Click](https://click.palletsprojects.com/en/8.1.x/)to manage development common work flows, for more information on available commands use:

```shell
cli command <command_name>
```

### Extending cli
You can use command:
```shell
cli command <command_name>
```
To generate a new cli using the project template, new commands are registered automatically,check [cli.py](./cli.py) for more information. 
   
