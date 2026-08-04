#!/usr/bin/env python3

"""Record light magic spells safely"""


def light_spell_allowed_ingredients() -> list[str]:
    """Return allowed light magic ingredients"""

    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record or reject a light spell"""

    from .light_validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    if validation.endswith("VALID") and not validation.endswith("INVALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
