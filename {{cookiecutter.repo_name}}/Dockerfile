FROM nvcr.io/nvidia/pytorch:21.05-py3

# TODO: Create new files as $USER instead of root

# Copy files to a new 'work' directory
RUN mkdir -p /work/
COPY ./ /work/

# Install requirements
RUN pip install --ignore-installed -r /work/requirements.txt

# Set the working directory
WORKDIR /work/
