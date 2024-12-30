import subprocess


def run_command(command):
    try:
        # Run the command
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        # Print the command's output
        print("Output:\n", result.stdout)
        # Print any error output
        print("Errors:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")


def main():
    commands = ['python setup.py bdist_wheel sdist', 'twine check dist/*', 'pip install .']
    for command in commands:
        run_command(command)
"""
twine upload -r testpypi dist/* 
enter credentials
twine upload dist/* 
"""

if __name__ == "__main__":
    main()
