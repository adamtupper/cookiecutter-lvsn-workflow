#!/bin/bash

# Run pipeline
dvc repro --no-commit

# Copy gitignore and dvc.lock files to the DVC store (so that they persist)
mv .gitignore {{cookiecutter.dvc_store}}
mv dvc.lock {{cookiecutter.dvc_store}}