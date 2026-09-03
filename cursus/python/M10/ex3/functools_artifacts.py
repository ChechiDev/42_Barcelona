#!/usr/bin/env python3

from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """ Reduce spell powers using the requested operation """

    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    if not spells:
        return 0
    return reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    """ Return predefined partial enchantment functions """

    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """ Return the nth Fibonacci number using cache """

    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def _dispatch_spell(value: Any) -> str:
    """ Dispatch unknown spell values """

    return "Unknown spell type"


@_dispatch_spell.register
def _dispatch_int(value: int) -> str:
    """ Dispatch integer spell power """

    return f"Damage spell: {value} damage"


@_dispatch_spell.register
def _dispatch_str(value: str) -> str:
    """ Dispatch string spell name """

    return f"Enchantment: {value}"


@_dispatch_spell.register(list)
def _dispatch_list(value: list[Any]) -> str:
    """ Dispatch spell sequences """

    return f"Multi-cast: {len(value)} spells"


def spell_dispatcher() -> Callable[[Any], str]:
    """ Return the configured single-dispatch spell function """

    return _dispatch_spell


def main() -> None:
    """ Demonstrate functools artifacts with sample values """

    spell_powers = [10, 20, 30, 40]
    dispatcher = spell_dispatcher()

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("Testing spell dispatcher...")
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher({"unknown": True}))


if __name__ == "__main__":
    main()
