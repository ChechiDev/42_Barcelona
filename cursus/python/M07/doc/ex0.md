# Exercise 0: Creature Factory

Create an `ex0/` package and a root script `battle.py` to demonstrate the abstract factory pattern with Creature cards.

## Files

- `battle.py`
- `ex0/` as a package with all needed files
- `ex0/__init__.py` is mandatory

## Requirements

- Define an abstract `Creature` class with name and type attributes.
- `Creature` has an abstract `attack()` method.
- `Creature` has a concrete `describe()` method returning `<name> is a <type> type Creature`.
- Define concrete Creatures: `Flameling`, `Pyrodon`, `Aquabub`, and `Torragon`.
- Define an abstract `CreatureFactory` with `create_base()` and `create_evolved()`.
- Define `FlameFactory` and `AquaFactory`.
- The `ex0` package must expose factories, not concrete Creature classes.
- `battle.py` must use one function to test factories and another function to make base Creatures fight.

## Expected concepts

- Abstract factory pattern.
- Creature family creation through a common factory interface.
- Dynamic demo logic without hardcoding behavior inside processing functions.
