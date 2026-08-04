#!/usr/bin/env python3

"""Demonstrate direct module import for fire creation"""

import elements


def main() -> None:
    """Run the alembic zero demonstration"""

    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
