#!/usr/bin/env python3

"""Define base Creature abstractions and concrete families"""

from abc import ABC, abstractmethod


class Creature(ABC):
    """Represent a typed Creature card with common behavior"""

    def __init__(self, name: str, creature_type: str) -> None:
        self._name = name
        self._creature_type = creature_type

    def get_name(self) -> str:
        """Return the Creature name"""

        return self._name

    def get_creature_type(self) -> str:
        """Return the Creature type"""

        return self._creature_type

    def describe(self) -> str:
        """Return a standard Creature description"""

        return f"{self._name} is a {self._creature_type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        """Return this Creature attack message"""


class Flameling(Creature):
    """Represent the base fire Creature"""

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """Return the Flameling attack message"""

        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """Represent the evolved fire Creature"""

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """Return the Pyrodon attack message"""

        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    """Represent the base water Creature"""

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """Return the Aquabub attack message"""

        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    """Represent the evolved water Creature"""

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """Return the Torragon attack message"""

        return "Torragon uses Hydro Pump!"
