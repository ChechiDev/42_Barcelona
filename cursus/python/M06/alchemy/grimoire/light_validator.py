#!/usr/bin/env python3

from .light_spellbook import light_spell_allowed_ingredients

VALID_STATUS = "VALID"
INVALID_STATUS = "INVALID"


def has_allowed_ingredient(ingredients: str, allowed: list[str]) -> bool:
    """Return whether ingredients contain an allowed value"""

    lower_ingredients = ingredients.lower()
    return any(ingredient in lower_ingredients for ingredient in allowed)


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients for light magic"""

    is_valid = has_allowed_ingredient(
        ingredients,
        light_spell_allowed_ingredients(),
    )
    status = VALID_STATUS if is_valid else INVALID_STATUS
    return f"{ingredients} - {status}"
