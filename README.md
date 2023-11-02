# Django REST Api
## Setting Up

To set up your development environment for this project, follow these steps:

1. Install [Visual Studio Code Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

   You can install this extension from the Visual Studio Code Marketplace. It allows you to develop in a Docker container, which is useful for isolating your project's dependencies and ensuring consistency across different development environments.

2. Clone the Repository

   Clone this project repository to your local machine using Git. You can use the following command:

   ```shell
   git clone https://github.com/gadc1996/django-api
   
   Navigate to the Project Folder

## Script Descriptions

This project uses Pipenv for managing dependencies and running scripts. Below are the available commands and their descriptions:

### Django specic scripts
- `setup`: Initialize environment configuration
- `app`: Create a new Django application in the "src" folder.
- `migrations`: Generate migrations for the Django database.
- `migrate`: Apply migrations to the database.
- `serve`: Start the Django development server.
- `superuser`: Create a superuser in the Django database.
- `shell`: Open the interactive Django shell.
- `test [name]`: Run Django tests for a specific application `[name]`.
- `eb-init`: Initialize Elastic Beanstalk with Docker.
- `create`: Create an Elastic Beanstalk environment``.
- `eb-terminate`: Terminate Elastic Beanstalk environment.

### Usage

To run any of the above commands, use the following format:

```shell
pipenv run [command]
