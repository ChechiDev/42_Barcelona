# Exercise 2: Memory Depths

Create `ex2/scope_mysteries.py` to demonstrate closures and lexical scoping.

Required functions:

- `mage_counter() -> Callable`
- `spell_accumulator(initial_power: int) -> Callable`
- `enchantment_factory(enchantment_type: str) -> Callable`
- `memory_vault() -> dict[str, Callable]`

The memory vault must return `store(key, value)` and `recall(key)` closures. `recall` returns the stored value or `"Memory not found"`. Use closure state and `nonlocal` where state reassignment is required; do not use global mutable state.
