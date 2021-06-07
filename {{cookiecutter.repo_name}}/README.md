# {{cookiecutter.repo_name}}

{{cookiecutter.short_description}}

## Development

### Developing Inside a Container

This project is designed to be deployed in a container on LVSN servers. For streamlined development, it is configured to support the Visual Studio Code [Remote - Containers extension](https://code.visualstudio.com/docs/remote/containers). This lets you use the Docker container as a full-featured development environment, rather than packaging your code after the fact for deployment.

To develop inside the container, run the **Remote-Containers: Reopen in Container** command after opening this project in VS Code (you may need to install the extension first). When developing inside the container, you can execute your code from the VS Code integrated terminal using

```shell
python src/main.py --save-model --dry-run
```

### Syncing Git and DVC

Each time you would like to push some artifacts or data to the DVC remote, commit all the source and metadata files to Git and run

```shell
dvc push
```

When cloning a repository or pulling changes, run

```shell
dvc pull
```

afterwards to pull the artifacts associated with the latest commit.

### Deployment

To deploy this project on an LVSN server, you can build the Docker image using

```shell
docker build -t "my-image:dev" .
```

and run the main experiment script using

```shell
docker run --rm --gpus all my-image:dev python src/main.py --save-model --dry-run
```

Developing your project as described above should prevent any surprises when deploying the container.

---

This project was generated with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) using the
[cookiecutter-lvsn-workflow](https://github.com/adamtupper/cookiecutter-lvsn-workflow) template.
