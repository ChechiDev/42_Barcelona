# Exercise 1: Capabilities

Create an `ex1/` package and a root script `capacitor.py` to add capabilities to Creature cards while keeping capabilities separate from the Creature base class.

## Files

- `capacitor.py`
- `ex1/` as a package with all needed files
- `ex1/__init__.py` is mandatory

## Requirements

- Build this exercise on the content of `ex0`.
- Define `HealCapability` with `heal()`.
- Define `TransformCapability` with `transform()` and `revert()`.
- Transforming creatures must keep persistent state that affects `attack()`.
- Define `Sproutling` and `Bloomelle`, exposed through `HealingCreatureFactory`.
- Define `Shiftling` and `Morphagon`, exposed through `TransformCreatureFactory`.
- The `ex1` package must expose factories, not concrete Creature classes.
- `capacitor.py` must demonstrate healing and transforming families.

## Expected concepts

- Capability interfaces separated from Creature inheritance.
- Multiple inheritance through focused abstractions.
- Persistent transform state affecting attack behavior.
