#!/usr/bin/env python3

"""Demonstrate an intentional dark grimoire circular import"""


def main() -> None:
    """Run the kaboom one demonstration"""

    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Nightmare", "bats and fog"))


if __name__ == "__main__":
    main()
