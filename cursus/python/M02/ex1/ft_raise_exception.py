#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    """ Convert a str to an int and validate plant-safe temperature range """

    temp = int(temp_str)
    if (temp < 0):
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    elif (temp > 40):
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    """ Test temperature conversion and range validation."""

    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("Input data is 'abc'")
    try:
        temp2 = input_temperature("abc")
        print(f"Temperature is now {temp2}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("Input data is '100'")
    try:
        temp3 = input_temperature("100")
        print(f"Temperature is now {temp3}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("Input data is '-50'")
    try:
        temp4 = input_temperature("-50")
        print(f"Temperature is now {temp4}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


def main() -> None:
    """ Run the temperature validation demo """

    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
