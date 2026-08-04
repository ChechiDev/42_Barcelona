#!/usr/bin/env python3

"""Demonstrate package module import for earth creation"""

import alchemy.elements


def main() -> None:
    """Run the alembic two demonstration"""

    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()
