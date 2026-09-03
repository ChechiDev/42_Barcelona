#!/usr/bin/env python3

import alchemy.grimoire


SPELL_NAME = "Fantasy"
SPELL_INGREDIENTS = "Earth, wind and fire"


def main() -> None:
    """Run the kaboom zero demonstration"""

    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(
        "Testing record light spell: "
        f"{alchemy.grimoire.light_spell_record(SPELL_NAME, SPELL_INGREDIENTS)}"
    )


if __name__ == "__main__":
    main()
