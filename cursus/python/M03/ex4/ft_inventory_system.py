#!/usr/bin/env python3
import sys


def parse_argument(arg: str) -> tuple[str, int] | None:
    """ Parse a single 'name:qty' argument, return tuple or None on failure """
    # Compruebo  syntax:
    arg = arg.strip()
    if arg.count(":") != 1:
        print(f"Error - invalid parameter '{arg}'")
        return None
    # Parto el name y qty:
    name, qty_str = arg.split(":")
    name = name.strip()
    qty_str = qty_str.strip()
    # Pruebo de convertir qty en int:
    try:
        qty = int(qty_str)
    except ValueError as e:
        print(f"Quantity error for '{name}': {e}")
        return None
    return (name, qty)


def build_inventory(args: list[str]) -> dict[str, int]:
    """ Build inventory dict from command-line arguments """
    inventory: dict[str, int] = {}
    for arg in args:
        parsed = parse_argument(arg)
        if parsed is None:
            continue
        name, qty = parsed
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        inventory[name] = qty
    return inventory


def display_stats(inventory: dict[str, int]) -> None:
    """ Display inventory stats including totals, percentages and extremes """
    if len(inventory) == 0:
        print("Got inventory: {}")
    else:
        items = list(inventory.keys())
        total = sum(inventory.values())
        max_name = items[0]
        min_name = items[0]
        print(
            f"Got inventory: {inventory}\n"
            f"Item list: {items}\n"
            f"Total quantity of the {len(items)} items: {total}"
            )
        # Percent:
        for name in inventory.keys():
            qty = inventory[name]
            pct = round((qty / total) * 100, 1)
            print(f"Item {name} represents {pct}%")
        # Max:
        for name in inventory.keys():
            if inventory[name] > inventory[max_name]:
                max_name = name
        print(
            f"Item most abundant: "
            f"{max_name} with quantity {inventory[max_name]}"
        )
        # Min:
        for name in inventory.keys():
            if inventory[name] < inventory[min_name]:
                min_name = name
        print(
            f"Item least abundant: "
            f"{min_name} with quantity {inventory[min_name]}"
        )


def main() -> None:
    """ Orchestrate inventory building, stats display and item addition """
    print("=== Inventory System Analysis ===")
    inventory = build_inventory(sys.argv[1:])
    display_stats(inventory)
    # Actualizamos el inventory
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
