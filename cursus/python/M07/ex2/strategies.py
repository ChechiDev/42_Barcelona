#!/usr/bin/env python3

"""Define battle strategies for Creature tournament actions"""

from abc import ABC, abstractmethod

from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Represent an invalid Creature and strategy combination"""


class BattleStrategy(ABC):
    """Define the strategy interface for Creature battle actions"""

    def __init__(self, display_name: str) -> None:
        self._display_name = display_name

    def get_display_name(self) -> str:
        """Return the strategy display name"""

        return self._display_name

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return whether this strategy can act with a Creature"""

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        """Return battle action messages for one Creature"""

    def _validate_or_raise(self, creature: Creature) -> None:
        """Raise a strategy error when the Creature is invalid"""

        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.get_name()}' for this "
                f"{self._display_name.lower()} strategy"
            )


class NormalStrategy(BattleStrategy):
    """Attack normally with any Creature"""

    def __init__(self) -> None:
        super().__init__("Normal")

    def is_valid(self, creature: Creature) -> bool:
        """Return whether any Creature can use this strategy"""

        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> list[str]:
        """Return a normal attack action"""

        self._validate_or_raise(creature)
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    """Transform, attack, and revert a transforming Creature"""

    def __init__(self) -> None:
        super().__init__("Aggressive")

    def is_valid(self, creature: Creature) -> bool:
        """Return whether a Creature has transform capabilities"""

        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        """Return aggressive transform battle actions"""

        self._validate_or_raise(creature)
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError("Creature cannot transform")
        return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):
    """Attack and heal with a healing Creature"""

    def __init__(self) -> None:
        super().__init__("Defensive")

    def is_valid(self, creature: Creature) -> bool:
        """Return whether a Creature has healing capabilities"""

        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        """Return defensive attack and healing actions"""

        self._validate_or_raise(creature)
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError("Creature cannot heal")
        return [creature.attack(), creature.heal()]
