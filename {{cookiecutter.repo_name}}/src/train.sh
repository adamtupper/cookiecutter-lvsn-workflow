#!/bin/bash

# Run pipeline
dvc repro --no-commit

# Copy gitignore and dvc.lock files to the DVC store (so that they persist)
mv .gitignore dvcstore/
mv dvc.lock dvcstore/