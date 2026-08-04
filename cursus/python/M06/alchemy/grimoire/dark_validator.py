#!/usr/bin/env python3

"""Validate dark spell ingredients with an intentional circular import"""

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients for dark magic"""

    lower_ingredients = ingredients.lower()
    is_valid = any(
        ingredient in lower_ingredients
        for ingredient in dark_spell_allowed_ingredients()
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
