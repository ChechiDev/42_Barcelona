#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for garden-related errors """
    def __init__(self, msg: str = "Unknown garden error"):
        super().__init__(msg)


class PlantError(GardenError):
    """Exception raised for plant-related errors """
    def __init__(self, msg: str = "Unknown plant error"):
        super().__init__(msg)


class WaterError(GardenError):
    """Exception raised for watering-related errors """
    def __init__(self, msg: str = "Unknown water error"):
        super().__init__(msg)


def check_plant() -> None:
    """Raise a PlantError for testing purposes """

    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    """Raise a WaterError for testing purposes """

    raise WaterError("Not enough water in the tank!")


def test_garden_errors() -> None:
    """Test custom garden-related exceptions """

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
    """Run the garden error demo """

    print("=== Custom Garden Error Demo ===\n")
    test_garden_errors()


if __name__ == "__main__":
    main()
