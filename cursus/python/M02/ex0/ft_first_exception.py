#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    """ Function that converts str into int """
    return int(temp_str)


def test_temperature() -> None:
    """ test temperature typing """

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

    print("All tests completed - program didn't crash!")


def main():
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
