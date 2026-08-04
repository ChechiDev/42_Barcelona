#!/usr/bin/env python3

"""Record dark magic spells with an intentional circular import"""

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return allowed dark magic ingredients"""

    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record or reject a dark spell"""

    validation = validate_ingredients(ingredients)
    if validation.endswith("VALID") and not validation.endswith("INVALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
