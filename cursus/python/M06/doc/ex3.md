# ex3 - Avoid the Explosion

## Context

The fourth part introduces circular dependencies. The goal is to demonstrate one safe
design that avoids a circular import and one intentionally dangerous design that raises
an import error.

## General constraints

- Use Python 3.10 or later.
- Follow flake8 coding standard.
- Add comprehensive type annotations and check with mypy.
- All standard classes, collections, methods, and built-in functions are allowed, except
  `eval()` and `exec()`.
- Only imports of modules and files created in this project are allowed.
- Do not modify `sys.path`.
- Keep functions simple and focused on imports, not complex logic.

## Files to create or update

### `alchemy/grimoire/light_spellbook.py`

Must contain:

- `light_spell_allowed_ingredients()` returning a list of allowed ingredients for light
  magic:

  ```python
  ["earth", "air", "fire", "water"]
  ```

- `light_spell_record(spell_name: str, ingredients: str)` returning a string that says
  whether the spell is recorded or rejected. The decision comes from the light validator.

### `alchemy/grimoire/light_validator.py`

Must contain:

- `validate_ingredients(ingredients: str)` returning a string with the ingredients and
  either `VALID` or `INVALID`.
- Ingredients are valid if they include at least one allowed light ingredient from the
  spellbook.
- Validation is case-insensitive.
- This light implementation must avoid circular import failure.

### `alchemy/grimoire/dark_spellbook.py`

Duplicate the light spellbook structure and adapt names to dark magic.

Dark magic allowed ingredients are:

```python
["bats", "frogs", "arsenic", "eyeball"]
```

The dark implementation must intentionally create a dangerous circular dependency with
`dark_validator.py`.

### `alchemy/grimoire/dark_validator.py`

Duplicate the light validator structure and adapt names to dark magic.

The dark implementation must intentionally participate in the circular dependency with
`dark_spellbook.py`.

### `alchemy/grimoire/__init__.py`

Create or update it so that `ft_kaboom_0.py` can access the light spell recording flow
through the `grimoire` module directly.

## Scripts to create

### `ft_kaboom_0.py`

- Access the `grimoire` module directly.
- Record a light spell successfully.
- Demonstrate that light magic avoids circular dependencies.

Expected output:

```text
=== Kaboom 0 ===
Using grimoire module directly
Testing record light spell: Spell recorded: Fantasy (Earth, wind and fire - VALID)
```

### `ft_kaboom_1.py`

- Access `alchemy/grimoire/dark_spellbook.py` directly.
- Try to record a dark spell.
- This must fail and raise an uncaught exception caused by the intentional circular
  dependency.

Expected successful part before the intentional exception:

```text
=== Kaboom 1 ===
Access to alchemy/grimoire/dark_spellbook.py directly
Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION
```

Then importing from `dark_spellbook.py` must raise an `ImportError` caused by a circular
import with `dark_validator.py`.

## Evaluation focus

- What circular imports are and why they happen.
- Different ways to avoid circular dependencies.
- Why moving imports, extracting shared data, or changing dependency direction can solve
  circular import problems.
- Why the dark spellbook intentionally explodes while the light spellbook does not.
