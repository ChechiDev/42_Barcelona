# ex2 - The Great Transmutation

## Context

The third part explores absolute and relative imports: two different paths to reach the
same code from inside a package.

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

### `alchemy/transmutation/recipes.py`

Must contain:

- `lead_to_gold()` returning exactly this structure:

  ```text
  Recipe transmuting Lead to Gold: brew '[created air]' and '[created strength potion]' mixed with '[created fire]'
  ```

  With the required functions, the final string is:

  ```text
  Recipe transmuting Lead to Gold: brew 'Air element created' and 'Strength potion brewed with 'Fire element created' and 'Water element created'' mixed with 'Fire element created'
  ```

- At least one absolute import.
- At least one relative import.

### `alchemy/transmutation/__init__.py`

Create or update it so that importing the `alchemy.transmutation` module directly can
access the lead-to-gold recipe.

### `alchemy/__init__.py`

Update it so that importing only `alchemy` can access the lead-to-gold recipe.

## Scripts to create

### `ft_transmutation_0.py`

- Use the `import ...` structure to access `alchemy/transmutation/recipes.py` directly.
- Achieve transformation of lead into gold.

Expected output:

```text
=== Transmutation 0 ===
Using file alchemy/transmutation/recipes.py directly
Testing lead to gold: Recipe transmuting Lead to Gold: brew 'Air element created' and 'Strength potion brewed with 'Fire element created' and 'Water element created'' mixed with 'Fire element created'
```

### `ft_transmutation_1.py`

- Use the `import ...` structure to import the `transmutation` module directly.
- Achieve transformation of lead into gold.

Expected output:

```text
=== Transmutation 1 ===
Import transmutation module directly
Testing lead to gold: Recipe transmuting Lead to Gold: brew 'Air element created' and 'Strength potion brewed with 'Fire element created' and 'Water element created'' mixed with 'Fire element created'
```

### `ft_transmutation_2.py`

- Use the `import ...` structure to import the `alchemy` module only.
- Achieve transformation of lead into gold.

Expected output:

```text
=== Transmutation 2 ===
Import alchemy module only
Testing lead to gold: Recipe transmuting Lead to Gold: brew 'Air element created' and 'Strength potion brewed with 'Fire element created' and 'Water element created'' mixed with 'Fire element created'
```

## Evaluation focus

- Difference between absolute imports and relative imports.
- When absolute imports are clearer from outside a package.
- When relative imports are useful for nearby modules inside the same package.
- How `__init__.py` can re-export functions from nested modules.
