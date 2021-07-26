.DEFAULT_GOAL := help

NAME	:= {{cookiecutter.repo_name}}
TAG    	:= $$(git log -1 --format=%h)
IMG    	:= ${NAME}:${TAG}
LATEST	:= ${NAME}:latest

help:			## Show this help dialog.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

build:			## Build the Docker image.
	docker build -t ${IMG} .
	docker tag ${IMG} ${LATEST}

format:			## Run pre-commit hooks.
	pre-commit run

run-dev:		## Run the project inside the development container.
	bash src/train.sh

run:			## Run the project inside a Docker container (use `make run gpus=0,1` to specify GPU visibility).
	docker run --rm --gpus all --ipc=host \
		-e NVIDIA_VISIBLE_DEVICES=$(gpus) \
		-v {{cookiecutter.dvc_store}}:/home/docker/workspace/artifacts \
		self-distillation:latest \
		bash src/train.sh

test:			## Runs the tests inside a Docker container (use `make run gpus=0,1` to specify GPU visibility).
	docker run --rm --gpus all --ipc=host \
		-e NVIDIA_VISIBLE_DEVICES=$(gpus) \
		-v {{cookiecutter.dvc_store}}:/home/docker/workspace/artifacts \
		self-distillation:latest \
		pytest tests/