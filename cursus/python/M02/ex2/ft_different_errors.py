#!/src/bin/env python3


def garden_operations(operation_number: int) -> None:
    """ Function that validate an specific opereation """
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        1 / 0
    elif (operation_number == 2):
        open("/non/existent/file")
    elif (operation_number == 3):
        "int" + 1  # Mypy: Ignore


def test_error_types() -> None:
    """ Show speficic Exception """
    try:
        print("Testing operation 0...")
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    try:
        print("Testing operation 1...")
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    try:
        print("Testing operation 2...")
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    try:
        print("Testing operation 3...")
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    print("Testing operation 4...")
    print("Operation completed successfully\n")
    print("All error types tested successfully")


def main():
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    main()
