import os
import subprocess


# Initialise Git repo
subprocess.call(['git', 'init'])

# Initialise DVC
subprocess.call(['dvc', 'init'])
subprocess.call(['dvc', 'remote', 'default', '{{cookiecutter.dvc_remote}}'])

# Setup pre-commit
subprocess.call(['pre-commit', 'install'])

# Create empty directories for data, models, etc.
os.mkdir('checkpoints')
os.mkdir('data')
os.mkdir('metrics')
os.mkdir('models')

# Commit files
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
