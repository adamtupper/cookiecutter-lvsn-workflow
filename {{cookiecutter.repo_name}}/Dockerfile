FROM pytorch/pytorch:latest

ENV PATH="${PATH}:/home/docker/.local/bin"

RUN apt-get update && \
    apt-get install -y sudo

# Add (and switch to) new 'docker' user
RUN groupadd -g 110 usergroup
RUN adduser --disabled-password --gecos '' --uid {{cookiecutter.uid}} --gid {{cookiecutter.gid}} docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER docker

# Copy files to a new 'workspace' directory
RUN mkdir -p /home/docker/workspace/
COPY --chown={{cookiecutter.uid}}:{{cookiecutter.gid}} ./ /home/docker/workspace/

# Install requirements
RUN sudo apt-get update && \
    sudo apt-get install -y git python3 python3-pip
RUN pip install --ignore-installed -r /work/requirements.txt

# Set the working directory
WORKDIR /home/docker/workspace/

# Setup pre-commit hooks
RUN pre-commit install
