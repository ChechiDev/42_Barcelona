#!/usr/bin/env python3

"""Demonstrate direct recipe module import"""

import alchemy.transmutation.recipes


def main() -> None:
    """Run the transmutation zero demonstration"""

    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        "Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}"
    )


if __name__ == "__main__":
    main()
