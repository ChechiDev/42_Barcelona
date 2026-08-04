#!/usr/bin/env python3

"""Validate light spell ingredients"""

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients for light magic"""

    lower_ingredients = ingredients.lower()
    is_valid = any(
        ingredient in lower_ingredients
        for ingredient in light_spell_allowed_ingredients()
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
