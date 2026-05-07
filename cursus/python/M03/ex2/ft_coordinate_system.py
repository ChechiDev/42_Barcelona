#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:

    while True:
        coord_input = input(
                "Enter new coordenates as floats in format 'x,y,z': "
            )
        coord = []
        parts = coord_input.strip().split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        else:
            for p in parts:
                try:
                    coord.append(float(p.strip()))
                except ValueError as e:
                    print(f"Error on parameter '{p}': {e}")
            if len(coord) == 3:
                return (coord[0], coord[1], coord[2])


def main() -> None:

    center = (0.0, 0.0, 0.0)
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    cord1 = get_player_pos()
    calc = math.sqrt(
        (cord1[0] - center[0])**2
        + (cord1[1] - center[1])**2
        + (cord1[2] - center[2])**2
        )
    print(
        f"Got a first tuple: {cord1} "
        f"\nIt includes: "
        f"X={cord1[0]}, "
        f"Y={cord1[1]}, "
        f"Z={cord1[2]}"
        f"\nDistance to center: {calc:.4f}"
        )
    print("\nGet a second set of coordinates")
    cord2 = get_player_pos()
    calc = math.sqrt(
        (cord2[0] - cord1[0])**2
        + (cord2[1] - cord1[1])**2
        + (cord2[2] - cord1[2])**2
        )
    print(f"Distance between the 2 sets of coordinates: {calc:.4f}")


if __name__ == "__main__":
    main()
