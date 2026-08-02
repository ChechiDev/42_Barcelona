#!/usr/bin/env python3

import sys


def display_file(filename: str) -> None:
    """ Display the target file with archive recovery headers """

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename)
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    try:
        print("---")
        print(file.read(), end="")
        print("---")
    finally:
        file.close()
        print(f"File '{filename}' closed.")


def main() -> None:
    """ Validate arguments and launch the file display workflow """

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    display_file(sys.argv[1])


if __name__ == "__main__":
    main()
