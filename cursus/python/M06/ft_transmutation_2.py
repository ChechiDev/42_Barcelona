#!/usr/bin/env python3

"""Demonstrate alchemy package transmutation access"""

import alchemy


def main() -> None:
    """Run the transmutation two demonstration"""

    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.lead_to_gold()}")


if __name__ == "__main__":
    main()
