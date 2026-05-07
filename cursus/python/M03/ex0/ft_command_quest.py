#!/usr/bin/env python3

import sys


def main() -> None:
    """ Program that shows the data received as command-line parameters """

    if len(sys.argv) == 1:
        print("=== Command Quest ===")
        print(f"Program name: {sys.argv[0]}")
        print("No arguments provided!")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        for i in range(len(sys.argv)):
            if i == 0:
                print("=== Command Quest ===")
                print(f"Program name: {sys.argv[i]}")
                print(f"Arguments received: {len(sys.argv) - 1}")
            else:
                print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
