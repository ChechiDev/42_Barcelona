#!/usr/bin/env python3

"""Lambda-based helpers for FuncMage Chronicles exercise 0"""

from typing import Any


Mage = dict[str, Any]
Artifact = dict[str, Any]


def artifact_sorter(artifacts: list[Artifact]) -> list[Artifact]:
    """ Return artifacts sorted by descending power """

    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    """ Return mages with at least the requested power """

    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """ Return spells wrapped with magical markers """

    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[Mage]) -> dict[str, float | int]:
    """ Return aggregate power statistics for mages """

    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(map(lambda mage: int(mage["power"]), mages)) / len(mages),
            2,
        ),
    }


def main() -> None:
    """ Demonstrate lambda spell helpers with sample data """

    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
    ]
    spells = ["fireball", "heal", "shield"]

    sorted_artifacts = artifact_sorter(artifacts)
    transformed_spells = spell_transformer(spells)

    print("Testing artifact sorter...")
    first_artifact = sorted_artifacts[0]
    second_artifact = sorted_artifacts[1]
    print(
        f"{first_artifact['name']} ({first_artifact['power']} power) "
        f"comes before {second_artifact['name']} "
        f"({second_artifact['power']} power)"
    )
    print("Testing spell transformer...")
    print(" ".join(transformed_spells))


if __name__ == "__main__":
    main()
