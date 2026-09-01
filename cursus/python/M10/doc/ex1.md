# Exercise 1: Higher Realm

Create `ex1/higher_magic.py` to demonstrate higher-order functions.

Required functions:

- `spell_combiner(spell1: Callable, spell2: Callable) -> Callable`: returned spell returns a tuple with both spell results.
- `power_amplifier(base_spell: Callable, multiplier: int) -> Callable`
- `conditional_caster(condition: Callable, spell: Callable) -> Callable`: return `"Spell fizzled"` when the condition fails.
- `spell_sequence(spells: list[Callable]) -> Callable`: returned spell returns a list with all spell results.

Spells use the contract `spell(target: str, power: int) -> str`.
