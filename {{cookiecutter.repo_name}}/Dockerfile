FROM pytorch/pytorch:latest

# TODO: Create new files as $USER instead of root

# Copy files to a new 'work' directory
RUN mkdir -p /work/
COPY ./ /work/

# Install requirements
RUN apt update && apt install -y git
RUN pip install --ignore-installed -r /work/requirements.txt

# Set the working directory
WORKDIR /work/

# Setup pre-commit hooks
RUN pre-commit install
