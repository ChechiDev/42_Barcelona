#!/usr/bin/env python3

from ex0 import AquaFactory, CreatureFactory, FlameFactory


def print_creature_actions(factory: CreatureFactory) -> None:
    """Print base and evolved Creature actions for one factory"""

    print("Testing factory")
    for creature in (factory.create_base(), factory.create_evolved()):
        print(creature.describe())
        print(creature.attack())


def print_base_battle(
    first_factory: CreatureFactory,
    second_factory: CreatureFactory,
) -> None:
    """Print a battle between base Creatures from two factories"""

    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()
    print("Testing battle")
    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())
    print("fight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    """Run the abstract factory demonstration"""

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    print_creature_actions(flame_factory)
    print_creature_actions(aqua_factory)
    print_base_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
