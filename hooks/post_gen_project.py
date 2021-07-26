import os
import subprocess


# Initialise Git repo
subprocess.call(['git', 'init'])

# Initialise DVC
subprocess.call(['dvc', 'init'])
subprocess.call(['ln', '-s', '{{cookiecutter.dvc_store}}', './artifacts'])

if '{{cookiecutter.dvc_remote}}':
    # Specify DVC Remote
    subprocess.call(['dvc', 'remote', 'default', '{{cookiecutter.dvc_remote}}'])

# Setup pre-commit
subprocess.call(['pre-commit', 'install'])

# Create empty directories for data, models, etc.
os.mkdir('artifacts/checkpoints')
os.mkdir('artifacts/data')
os.mkdir('artifacts/metrics')
os.mkdir('artifacts/models')

# Commit files
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
