#!/usr/bin/env python3

"""Decorator examples for FuncMage Chronicles exercise 4"""

from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any, ParamSpec, TypeVar, cast


P = ParamSpec("P")
R = TypeVar("R")


def spell_timer(func: Callable[P, R]) -> Callable[P, R]:
    """ Return a wrapper that prints spell execution time """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        """ Time the wrapped spell call """

        print(f"Casting {func.__name__}...")
        start_time = perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = perf_counter() - start_time
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result

    return wrapper


def power_validator(
    min_power: int,
) -> Callable[[Callable[P, R]], Callable[P, R | str]]:
    """ Return a decorator that rejects insufficient spell power """

    def decorator(func: Callable[P, R]) -> Callable[P, R | str]:
        """ Decorate a spell with power validation """

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | str:
            """ Validate power before casting """

            power = _get_power_argument(args, kwargs)
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def _get_power_argument(args: tuple[Any, ...], kwargs: dict[str, Any]) -> int:
    """ Return power from wrapped spell arguments """

    if "power" in kwargs:
        return cast(int, kwargs["power"])
    if args:
        return cast(int, args[-1])
    raise ValueError("power argument is required")


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[P, R]], Callable[P, R | str]]:
    """ Return a decorator that retries failed spell casts """

    def decorator(func: Callable[P, R]) -> Callable[P, R | str]:
        """ Decorate a spell with retry behavior """

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | str:
            """ Retry the spell until it succeeds or attempts end """

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """ Represent a mage guild capable of validating and casting spells """

    def __init__(self, guild_name: str) -> None:
        self.guild_name = guild_name

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """ Return whether a mage name follows guild rules """

        return len(name) >= 3 and all(
            character.isalpha() or character.isspace()
            for character in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """ Cast a guild spell with validated power """

        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """ Demonstrate decorators and static method behavior """

    @spell_timer
    def fireball() -> str:
        """ Return a fireball cast result """

        return "Fireball cast!"

    @retry_spell(3)
    def failing_spell() -> str:
        """ Always fail to demonstrate retry exhaustion """

        raise RuntimeError("spell failed")

    guild = MageGuild("Master Guild")

    print("Testing spell timer...")
    print(f"Result: {fireball()}")
    print("Testing retrying spell...")
    print(failing_spell())
    print("Waaaaaaagh spelled !")
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
