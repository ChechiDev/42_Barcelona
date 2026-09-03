#!/usr/bin/env python3

from elements import create_fire

from ..elements import create_air
from ..potions import strength_potion


def format_transmutation_recipe(
    source: str,
    target: str,
    air_element: str,
    potion: str,
    fire_element: str,
) -> str:
    """Format a transmutation recipe message"""

    return (
        f"Recipe transmuting {source} to {target}: brew "
        f"'{air_element}' and '{potion}' mixed with '{fire_element}'"
    )


def lead_to_gold() -> str:
    """Transmute lead into gold"""

    return format_transmutation_recipe(
        "Lead",
        "Gold",
        create_air(),
        strength_potion(),
        create_fire(),
    )
