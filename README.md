# Cookiecutter Template for LVSN Projects

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for my LVSN workflow. Utilises [Git](https://git-scm.com) for version control, [Data Version Control (DVC)](https://dvc.org/doc) for artifact tracking, [pre-commit](https://pre-commit.com) for encouraging code quality, and [Docker](https://docs.docker.com) for deploying experiments on the LVSN servers.

## Usage

Once you have Cookiecutter installed, you can setup a local project using this template by running

```shell
cookiecutter https://github.com/adamtupper/cookiecutter-lvsn-workflow.git
```

## Developing Inside a Container

Projects based on this template are designed to be deployed in containers on LVSN servers. For streamlined development, they are also configured to support the Visual Studio Code [Remote - Containers extension](https://code.visualstudio.com/docs/remote/containers). This lets you use the Docker container as a full-featured development environment, rather than packaging your code after the fact for deployment.

To develop inside the container, run the **Remote-Containers: Reopen in Container** command after opening the project in VS Code (you may need to install the extension first). When developing inside the container, you can execute your code from the VS Code integrated terminal using

```shell
python src/main.py --save-model --dry-run
```

## MNIST Example with DVC

Projects build using this template are configured to use DVC to run and track experiments (using DVC pipelines). A modified version of the [PyTorch MNIST example](https://github.com/pytorch/examples/blob/master/mnist/main.py) (see `main.py`) is included to demonstrate how to use DVC. The pipeline is defined in `dvc.yaml` and the hyperparameters for each pipeline stage are defined in `params.yaml`. The pipeline can be run using

```shell
dvc repro
```

## Syncing Git and DVC

Each time you would like to push some artifacts or data to the DVC remote, commit all the source and metadata files to Git and run

```shell
dvc push
```

When cloning a repository or pulling changes, run

```shell
dvc pull
```

afterwards to pull the artifacts associated with the latest commit.

## Deployment

To deploy the project on an LVSN server, you can build the Docker image using

```shell
docker build -t "my-image:dev" .
```

and run the main experiment script using

```shell
docker run --rm --gpus all my-image:dev main.py --save-model --dry-run
```

Developing your project as described above should prevent any surprises when deploying the container.

## Contributing

If you notice any bugs, would like to contribute a bug-fix, or have a suggestion please open an [issue](https://github.com/adamtupper/cookiecutter-lvsn-workflow/issues).
