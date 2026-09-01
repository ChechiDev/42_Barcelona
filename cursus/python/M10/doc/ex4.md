# Exercise 4: Master's Tower

Create `ex4/decorator_mastery.py` to demonstrate decorators and `staticmethod`.

Required functions and class:

- `spell_timer(func: Callable) -> Callable`: print `Casting function_name...` before execution and `Spell completed in X.XXX seconds` after execution.
- `power_validator(min_power: int) -> Callable`: return `"Insufficient power for this spell"` when power is too low.
- `retry_spell(max_attempts: int) -> Callable`: print retry messages and return `"Spell casting failed after max_attempts attempts"` after all failures.
- `MageGuild.validate_mage_name(name: str) -> bool`
- `MageGuild.cast_spell(self, spell_name: str, power: int) -> str`

`MageGuild.validate_mage_name` accepts names with at least 3 characters containing only letters and spaces. `MageGuild.cast_spell` must use `power_validator(10)` and return `"Successfully cast spell_name with <power> power"` when valid. Use `functools.wraps` and `@staticmethod`.
