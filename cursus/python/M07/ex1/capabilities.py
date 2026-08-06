#!/usr/bin/env python3

"""Define Creature capability abstractions"""

from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Define healing behavior independent from Creature inheritance"""

    @abstractmethod
    def heal(self) -> str:
        """Return a healing action message"""


class TransformCapability(ABC):
    """Define transforming behavior independent from Creature inheritance"""

    def __init__(self) -> None:
        self._is_transformed = False

    def is_transformed(self) -> bool:
        """Return whether the object is currently transformed"""

        return self._is_transformed

    @abstractmethod
    def transform(self) -> str:
        """Transform and return a transformation message"""

    @abstractmethod
    def revert(self) -> str:
        """Revert and return a reversion message"""
