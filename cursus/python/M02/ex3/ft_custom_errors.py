#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, msg: str = "Unknown garden error"):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown plant error"):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown water error"):
        super().__init__(msg)


def check_plant() -> None:
    """ Error plant check function """
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    """ Error water check function """
    raise WaterError("Not enough water in the tank!")


def test_garden_errors() -> None:
    """ Test custom exception function """
    try:
        print("Testing PlantError...")
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    try:
        print("Testing WaterError...")
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    try:
        print("Testing catching all garden errors...")
        check_plant()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


def main() -> None:
    print("=== Custom Garden Error Demo ===\n")
    test_garden_errors()


if __name__ == "__main__":
    main()
