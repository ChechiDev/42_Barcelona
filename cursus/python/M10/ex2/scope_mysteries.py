#!/usr/bin/env python3

"""Closure-based helpers for FuncMage Chronicles exercise 2"""

from collections.abc import Callable


VaultValue = object
VaultOperation = Callable[..., VaultValue]


def mage_counter() -> Callable[[], int]:
    """ Return a counter that remembers created mages """

    count = 0

    def count_mage() -> int:
        """ Increment and return the mage count """

        nonlocal count
        count += 1
        return count

    return count_mage


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """ Return an accumulator that remembers spell power """

    total_power = initial_power

    def put_power(power: int) -> int:
        """ Add power and return the accumulated total """

        nonlocal total_power
        total_power += power
        return total_power

    return put_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """ Return an item enchanter for the selected type """

    def enchant_item(item: str) -> str:
        """ Apply the stored enchantment to an item """

        return f"{enchantment_type} {item}"

    return enchant_item


def memory_vault() -> dict[str, VaultOperation]:
    """ Return closure-based memory vault operations """

    memories: dict[str, VaultValue] = {}

    def store(key: str, value: VaultValue) -> VaultValue:
        """ Store a memory and report the operation """

        memories[key] = value
        return value

    def recall(key: str) -> VaultValue:
        """ Return a stored memory or a missing-memory message """

        return memories.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    """ Demonstrate closure and lexical scoping helpers """

    counter_a = mage_counter()
    counter_b = mage_counter()
    accumulator = spell_accumulator(100)
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    vault = memory_vault()

    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("Testing spell accumulator...")
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")
    print("Testing enchantment factory...")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print("Testing memory vault...")
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
