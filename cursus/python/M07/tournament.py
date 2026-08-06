#!/usr/bin/env python3

"""Run Creature tournaments using abstract strategies"""

from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def format_opponents(opponents: list[Opponent]) -> str:
    """Return the tournament opponent summary"""

    labels = [
        f"({factory.get_display_name()}+{strategy.get_display_name()})"
        for factory, strategy in opponents
    ]
    return "[ " + ", ".join(labels) + " ]"


def print_strategy_actions(
    creature_factory: CreatureFactory,
    strategy: BattleStrategy,
) -> None:
    """Print actions for one base Creature using one strategy"""

    creature = creature_factory.create_base()
    for action in strategy.act(creature):
        print(action)


def print_battle(first: Opponent, second: Opponent) -> None:
    """Print one battle between two tournament opponents"""

    first_creature = first[0].create_base()
    second_creature = second[0].create_base()
    print("* Battle *")
    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())
    print("now fight!")
    print_strategy_actions(first[0], first[1])
    print_strategy_actions(second[0], second[1])


def print_tournament(opponents: list[Opponent]) -> None:
    """Print all pair battles for a tournament"""

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for first_index, first in enumerate(opponents):
        for second in opponents[first_index + 1:]:
            print_battle(first, second)


def run_tournament(title: str, opponents: list[Opponent]) -> None:
    """Print one tournament and gracefully report strategy errors"""

    print(title)
    print(format_opponents(opponents))
    try:
        print_tournament(opponents)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    """Run all tournament scenarios"""

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()
    run_tournament(
        "Tournament 0 (basic)",
        [
            (FlameFactory(), normal_strategy),
            (HealingCreatureFactory(), defensive_strategy),
        ],
    )
    run_tournament(
        "Tournament 1 (error)",
        [
            (FlameFactory(), aggressive_strategy),
            (HealingCreatureFactory(), defensive_strategy),
        ],
    )
    run_tournament(
        "Tournament 2 (multiple)",
        [
            (AquaFactory(), normal_strategy),
            (HealingCreatureFactory(), defensive_strategy),
            (TransformCreatureFactory(), aggressive_strategy),
        ],
    )


if __name__ == "__main__":
    main()
