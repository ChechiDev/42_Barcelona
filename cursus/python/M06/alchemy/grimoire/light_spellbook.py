#!/usr/bin/env python3

LIGHT_ALLOWED_INGREDIENTS = ["earth", "air", "fire", "water"]
VALID_STATUS = "VALID"
INVALID_STATUS = "INVALID"


def light_spell_allowed_ingredients() -> list[str]:
    """Return allowed light magic ingredients"""

    return LIGHT_ALLOWED_INGREDIENTS.copy()


def is_valid_validation(validation: str) -> bool:
    """Return whether a validation result is successful"""

    return (
        validation.endswith(VALID_STATUS)
        and not validation.endswith(INVALID_STATUS)
    )


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record or reject a light spell"""

    from .light_validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    if is_valid_validation(validation):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
