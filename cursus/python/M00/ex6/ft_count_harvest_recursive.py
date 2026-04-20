#!/usr/bin/env python3

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def recursive(current: int, days: int) -> None:
        if (current > days):
            print("Harvest time!")
            return
        print(f"Day: {current}")
        recursive(current + 1, days)

    recursive(1, days)
