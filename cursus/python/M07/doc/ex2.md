# Exercise 2: Abstract Strategy

Create an `ex2/` package and a root script `tournament.py` to demonstrate the abstract strategy pattern in Creature battles.

## Files

- `tournament.py`
- `ex2/` as a package with all needed files
- `ex2/__init__.py` is mandatory

## Requirements

- Build on `ex0` and `ex1`.
- Define `BattleStrategy` with `is_valid()` and `act()`.
- Define `NormalStrategy`, `AggressiveStrategy`, and `DefensiveStrategy`.
- `NormalStrategy` is valid for any Creature and uses `attack()`.
- `AggressiveStrategy` is valid for transforming Creatures and calls `transform()`, `attack()`, `revert()`.
- `DefensiveStrategy` is valid for healing Creatures and calls `attack()`, then `heal()`.
- Invalid strategy/Creature combinations must raise a dedicated exception with a clear message when `act()` is called.
- `tournament.py` must define one battle function that makes each opponent fight every other opponent once.

## Expected concepts

- Abstract strategy pattern.
- Capability-aware behavior without hardcoded battle branching.
- Graceful tournament abort on invalid strategy use.
