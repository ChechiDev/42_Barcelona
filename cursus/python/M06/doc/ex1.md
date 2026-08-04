# ex1 - Distillation

## Context

The second part introduces nested imports and using code from distant files in the
project package.

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

### `alchemy/potions.py`

Must contain:

- `healing_potion()` returning exactly this structure, with the current return values of
  the earth and air element functions inserted:

  ```text
  Healing potion brewed with '[created earth element]' and '[created air element]'
  ```

  With the required element functions, the final string is:

  ```text
  Healing potion brewed with 'Earth element created' and 'Air element created'
  ```

- `strength_potion()` returning exactly this structure, with the current return values of
  the fire and water element functions inserted:

  ```text
  Strength potion brewed with '[created fire element]' and '[created water element]'
  ```

  With the required element functions, the final string is:

  ```text
  Strength potion brewed with 'Fire element created' and 'Water element created'
  ```

- Any imports needed to access the four fundamental elements.

### `alchemy/__init__.py`

Update it so that:

- `alchemy.strength_potion()` is available.
- `alchemy.heal()` is available as a package alias of `healing_potion()`.

## Scripts to create

### `ft_distillation_0.py`

- Use the `from ... import ...` structure to access `alchemy/potions.py` directly.
- Brew both strength and healing potions.

Expected output:

```text
=== Distillation 0 ===
Direct access to alchemy/potions.py
Testing strength_potion: Strength potion brewed with 'Fire element created' and 'Water element created'
Testing healing_potion: Healing potion brewed with 'Earth element created' and 'Air element created'
```

### `ft_distillation_1.py`

- Use `import alchemy` to access potions through the package interface.
- Brew the original strength potion.
- Brew the special `heal()` potion alias.

Expected output:

```text
=== Distillation 1 ===
Using: 'import alchemy' structure to access potions
Testing strength_potion: Strength potion brewed with 'Fire element created' and 'Water element created'
Testing heal alias: Healing potion brewed with 'Earth element created' and 'Air element created'
```

## Evaluation focus

- How a module inside a package can import from nearby and top-level modules.
- How `__init__.py` can expose selected package functions.
- How aliases in a package interface work.
