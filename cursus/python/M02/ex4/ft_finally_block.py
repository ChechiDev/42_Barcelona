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


def water_plant(plant_name: str) -> None:
    """Water a plant if its name is capitalized, otherwise raise PlantError """

    if not (plant_name.capitalize() == plant_name):
        raise PlantError(f"Invalid plant name to water: {plant_name}")
    print(f"Watering {plant_name} [OK]")


def test_watering_system() -> None:
    """Run tests for the watering system with valid and invalid plant names """

    # Valid
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Letucce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("...ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    # Invalid
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("letucce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("...ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


def main() -> None:
    """Run the garden watering system demo """

    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
