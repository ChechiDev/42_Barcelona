#!/usr/bin/env python3

"""Demonstrate Creature capabilities"""

from ex0.creatures import Creature
from ex0.factories import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def print_healing_creature(label: str, creature: Creature) -> None:
    """Print healing Creature actions"""

    print(label)
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, HealCapability):
        print(creature.heal())


def print_transforming_creature(label: str, creature: Creature) -> None:
    """Print transforming Creature actions"""

    print(label)
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def print_factory_creatures(
    factory: CreatureFactory,
    printer_name: str,
) -> None:
    """Print base and evolved Creature actions using selected capability"""

    printers = {
        "healing": print_healing_creature,
        "transform": print_transforming_creature,
    }
    printer = printers[printer_name]
    printer("base:", factory.create_base())
    printer("evolved:", factory.create_evolved())


def main() -> None:
    """Run the capabilities demonstration"""

    print("Testing Creature with healing capability")
    print_factory_creatures(HealingCreatureFactory(), "healing")
    print("Testing Creature with transform capability")
    print_factory_creatures(TransformCreatureFactory(), "transform")


if __name__ == "__main__":
    main()
