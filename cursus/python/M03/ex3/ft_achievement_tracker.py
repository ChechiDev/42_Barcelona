#!/usr/bin/env python3

import random


ACH: list[str] = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
    "Hidden Path Finder",
    "Dragon Tamer",
    "Shadow Walker"
]


def gen_player_achievements() -> set[str]:
    """ Return a set of random achievements for a single player """
    rnd_ach = random.randint(4, 10)
    result = set(random.sample(ACH, rnd_ach))
    return result


def main() -> None:
    """ Generate 4 players and display achievement set analytics """
    players: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements())
    ]
    print("=== Achievement Tracker System ===\n")

    # Union
    distinct: set[str] = set()
    common: set[str] = players[0][1]
    for name, arch in players:
        print(f"Player {name}: {arch}")
        distinct = distinct.union(arch)
        common = common.intersection(arch)

    print(f"\nAll distinct achievements: {distinct}")
    print(f"\nCommon achievements: {common}\n")

    # Difference
    for name, arch in players:
        other: set[str] = set()
        for other_n, other_s in players:
            if other_n != name:
                other = other.union(other_s)
        diff = arch.difference(other)
        print(f"Only {name} has: {diff}")
    print()

    # Missing
    ach_set: set[str] = set(ACH)
    for name, arch in players:
        missing = ach_set.difference(arch)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
