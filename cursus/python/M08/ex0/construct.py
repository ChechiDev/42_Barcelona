#!/usr/bin/env python3

import os
import site
import sys


ENV_NAME = "matrix_env"


def is_virtual_environment() -> bool:
    """Return whether Python is running inside a virtual environment"""

    return sys.prefix != sys.base_prefix


def get_environment_name(environment_path: str) -> str:
    """Return the display name for an environment path"""

    return os.path.basename(environment_path)


def get_package_path() -> str:
    """Return the preferred package installation path"""

    package_paths = site.getsitepackages()
    if package_paths:
        return package_paths[0]
    return site.getusersitepackages()


def print_global_environment() -> None:
    """Print guidance for the global Python environment"""

    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print(f"python -m venv {ENV_NAME}")
    print(f"source {ENV_NAME}/bin/activate # On Unix")
    print(f"{ENV_NAME}\\Scripts\\activate # On Windows")
    print("Then run this program again.")


def print_virtual_environment() -> None:
    """Print details for the active virtual environment"""

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_environment_name(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    print(get_package_path())


def main() -> None:
    """Run the construct environment inspection"""

    if is_virtual_environment():
        print_virtual_environment()
        return
    print_global_environment()


if __name__ == "__main__":
    main()
