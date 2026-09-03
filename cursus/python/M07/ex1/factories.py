#!/usr/bin/env python3

from ex0.creatures import Creature
from ex0.factories import CreatureFactory

from .creatures import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    """Create healing family Creatures"""

    def create_base(self) -> Creature:
        """Create the base healing Creature"""

        return Sproutling()

    def create_evolved(self) -> Creature:
        """Create the evolved healing Creature"""

        return Bloomelle()

    def get_display_name(self) -> str:
        """Return the healing family display name"""

        return "Healing"


class TransformCreatureFactory(CreatureFactory):
    """Create transforming family Creatures"""

    def create_base(self) -> Creature:
        """Create the base transforming Creature"""

        return Shiftling()

    def create_evolved(self) -> Creature:
        """Create the evolved transforming Creature"""

        return Morphagon()

    def get_display_name(self) -> str:
        """Return the transforming family display name"""

        return "Transform"
