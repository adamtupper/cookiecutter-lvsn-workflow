import sys

# Check for dependencies
try:
    import dvc
except ImportError:
    print('Error: DVC is not installed! Install using `pip install dvc`.')

    # exits with status 1 to indicate failure
    sys.exit(1)
