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

    print(
        "\nMATRIX STATUS: You're still plugged in\n\n"
        f"Current Python: {sys.executable}\n"
        f"Virtual Environment: None detected\n\n"
        f"WARNING: You're in the global environment!\n"
        f"The machines can see everything you install.\n\n"
        f"To enter the construct, run:\n"
        f"python -m venv {ENV_NAME}\n"
        f"source {ENV_NAME}/bin/activate # On Unix\n"
        f"{ENV_NAME}\\Scripts\\activate # On Windows\n\n"
        f"Then run this program again."
    )

def print_virtual_environment() -> None:

    print(
        "\nMATRIX STATUS: Welcome to the construct\n\n"
        f"Current Python: {sys.executable}\n"
        f"Virtual Environment: {get_environment_name(sys.prefix)}\n"
        f"Environment Path: {sys.prefix}\n\n"
        f"SUCCESS: You're in an isolated environment!\n"
        f"Safe to install packages without affecting\n"
        f"the global system.\n\n"
        f"Package installation path:"
    )
    print(get_package_path())


def main() -> None:

    if is_virtual_environment():
        print_virtual_environment()
        return
    print_global_environment()


if __name__ == "__main__":
    main()
