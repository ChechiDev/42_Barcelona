#!/usr/bin/env python3

"""Demonstrate package function import for public air creation"""

from alchemy import create_air


def main() -> None:
    """Run the alembic five demonstration"""

    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
