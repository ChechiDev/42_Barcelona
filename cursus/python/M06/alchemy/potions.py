#!/usr/bin/env python3

from elements import create_fire, create_water

from .elements import create_air, create_earth


def format_potion(name: str, first_element: str, second_element: str) -> str:
    """Format a potion brewing message"""

    return (
        f"{name} potion brewed with '{first_element}' and "
        f"'{second_element}'"
    )


def healing_potion() -> str:
    """Brew a healing potion"""

    return format_potion("Healing", create_earth(), create_air())


def strength_potion() -> str:
    """Brew a strength potion"""

    return format_potion("Strength", create_fire(), create_water())
