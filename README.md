# Django REST Api

[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/gadc1996/django-api)

## Setting Up

To set up your development environment for this project, follow these steps:

1. Install [Visual Studio Code Remote - Containers extension](vscode:extension/ms-vscode-remote.remote-containers).

   You can install this extension from the Visual Studio Code Marketplace. It allows you to develop in a Docker container, which is useful for isolating your project's dependencies and ensuring consistency across different development environments.

2. Clone the Repository

   Clone this project repository to your local machine using Git. You can use the following command:

   ```shell
   git clone https://github.com/gadc1996/django-api
   
   Navigate to the Project Folder

3. Navigate to project folder

   Change your current directory to the project folder:

   ```shell
   cd django-api
   
4. Copy the Environment Configuration


   Duplicate the .env.example file to create your local environment configuration. You can do this using the following command:

   ```shell
   cp .env.example .env

## Script Descriptions

This project uses Pipenv for managing dependencies and running scripts. Below are the available commands and their descriptions:

- `app`: Create a new Django application in the "src" folder.
- `migrations`: Generate migrations for the Django database.
- `migrate`: Apply migrations to the database.
- `serve`: Start the Django development server.
- `update-dependencies`: Update the "requirements.txt" file with installed dependencies.
- `install [name]`: Install a specified dependency in the `[name]` argument and update "requirements.txt."
- `setup`: Install all dependencies specified in "requirements.txt."
- `superuser`: Create a superuser in the Django database.
- `shell`: Open the interactive Django shell.
- `test [name]`: Run Django tests for a specific application `[name]`.
- `eb-init`: Initialize Elastic Beanstalk with Docker.
- `create [EB_ENV_NAME]`: Create an Elastic Beanstalk environment with the specified name `[EB_ENV_NAME]`.
- `eb-deploy`: Deploy the application to Elastic Beanstalk.
- `eb-terminate [your-environment-name]`: Terminate a specified Elastic Beanstalk environment.

### Usage

To run any of the above commands, use the following format:

```shell
pipenv run [command]
