#!/usr/bin/env python3

"""Define Creature abstract factories"""

from abc import ABC, abstractmethod

from .creatures import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    """Create a base and evolved Creature from one family"""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base Creature of this family"""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved Creature of this family"""

    @abstractmethod
    def get_display_name(self) -> str:
        """Return the family display name for demos"""


class FlameFactory(CreatureFactory):
    """Create fire family Creatures"""

    def create_base(self) -> Creature:
        """Create the base fire Creature"""

        return Flameling()

    def create_evolved(self) -> Creature:
        """Create the evolved fire Creature"""

        return Pyrodon()

    def get_display_name(self) -> str:
        """Return the fire family display name"""

        return "Flameling"


class AquaFactory(CreatureFactory):
    """Create water family Creatures"""

    def create_base(self) -> Creature:
        """Create the base water Creature"""

        return Aquabub()

    def create_evolved(self) -> Creature:
        """Create the evolved water Creature"""

        return Torragon()

    def get_display_name(self) -> str:
        """Return the water family display name"""

        return "Aquabub"
