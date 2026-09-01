# Exercise 3: Ancient Library

Create `ex3/functools_artifacts.py` to demonstrate `functools` and `operator`.

Required functions:

- `spell_reducer(spells: list[int], operation: str) -> int`: return `0` for an empty spell list and handle unknown operations properly.
- `partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]`: base enchantment has signature `(power: int, element: str, target: str) -> str`; create three partials with `power=50` and prefilled elements.
- `memoized_fibonacci(n: int) -> int`
- `spell_dispatcher() -> Callable[[Any], str]`

Use `functools.reduce`, `functools.partial`, `functools.lru_cache`, and `functools.singledispatch`. Dispatch strings must follow the subject examples: damage spell for `int`, enchantment for `str`, multi-cast for `list`, and unknown spell type otherwise.
