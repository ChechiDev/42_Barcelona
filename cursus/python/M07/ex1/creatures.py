#!/usr/bin/env python3

"""Define Creature families with extra capabilities"""

from ex0.creatures import Creature

from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Represent the base healing Creature"""

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        """Return the Sproutling attack message"""

        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        """Return the Sproutling healing message"""

        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Represent the evolved healing Creature"""

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        """Return the Bloomelle attack message"""

        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        """Return the Bloomelle healing message"""

        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Represent the base transforming Creature"""

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Return the Shiftling attack message for current state"""

        if self.is_transformed():
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        """Transform Shiftling and return its message"""

        self._is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        """Revert Shiftling and return its message"""

        self._is_transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    """Represent the evolved transforming Creature"""

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Return the Morphagon attack message for current state"""

        if self.is_transformed():
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        """Transform Morphagon and return its message"""

        self._is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        """Revert Morphagon and return its message"""

        self._is_transformed = False
        return "Morphagon stabilizes its form."
