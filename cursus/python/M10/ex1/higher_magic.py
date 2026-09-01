#!/usr/bin/env python3

"""Higher-order spell helpers for FuncMage Chronicles exercise 1"""

from collections.abc import Callable


Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def spell_combiner(
    spell1: Spell,
    spell2: Spell,
) -> Callable[[str, int], tuple[str, str]]:
    """ Return a spell that casts two spells on the same target """

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        """ Cast both configured spells """

        return spell1(target, power), spell2(target, power)

    return combined_spell


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    """ Return a spell that multiplies incoming power """

    def amplified_spell(target: str, power: int) -> str:
        """ Cast the configured spell with amplified power """

        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Condition, spell: Spell) -> Spell:
    """ Return a spell that casts only when the condition passes """

    def conditional_spell(target: str, power: int) -> str:
        """ Cast or report a failed condition """

        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    """ Return a spell that casts a sequence of spells """

    def sequenced_spell(target: str, power: int) -> list[str]:
        """ Cast every configured spell in order """

        return [spell(target, power) for spell in spells]

    return sequenced_spell


def main() -> None:
    """ Demonstrate higher-order spell modifiers """

    def fireball(target: str, power: int) -> str:
        """ Return a fireball spell result """

        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        """ Return a healing spell result """

        return f"Heals {target}"

    def power_echo(target: str, power: int) -> str:
        """ Return the received spell power """

        return str(power)

    combined = spell_combiner(fireball, heal)
    amplified = power_amplifier(power_echo, 3)

    print("Testing spell combiner...")
    print(f"Combined spell result: {', '.join(combined('Dragon', 10))}")
    print("Testing power amplifier...")
    print(
        f"Original: {power_echo('Dragon', 10)}, "
        f"Amplified: {amplified('Dragon', 10)}"
    )


if __name__ == "__main__":
    main()
