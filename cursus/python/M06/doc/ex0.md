# ex0 - The Alembic

## Context

The first part introduces Python import mechanisms for local files and package modules.
The goal is to build the first components of the alchemical laboratory and test different
import styles.

## General constraints

- Use Python 3.10 or later.
- Follow flake8 coding standard.
- Add comprehensive type annotations and check with mypy.
- All standard classes, collections, methods, and built-in functions are allowed, except
  `eval()` and `exec()`.
- Only imports of modules and files created in this project are allowed.
- Do not modify `sys.path`.
- Keep functions simple and focused on imports, not complex logic.

## Files to create

### `elements.py`

Must contain:

- `create_fire()` returning exactly:

  ```text
  Fire element created
  ```

- `create_water()` returning exactly:

  ```text
  Water element created
  ```

### `alchemy/elements.py`

Must contain:

- `create_earth()` returning exactly:

  ```text
  Earth element created
  ```

- `create_air()` returning exactly:

  ```text
  Air element created
  ```

### `alchemy/__init__.py`

Must contain anything useful to partially import the `alchemy` module.
It must expose `create_air()` through the package interface for `ft_alembic_4.py` and
`ft_alembic_5.py`, but `create_earth()` must not be exposed through that interface.

## Scripts to create

### `ft_alembic_0.py`

- Use the `import ...` structure to access `elements.py` directly.
- Create fire.

Expected output:

```text
=== Alembic 0 ===
Using: 'import ...' structure to access elements.py
Testing create_fire: Fire element created
```

### `ft_alembic_1.py`

- Use the `from ... import ...` structure to access `elements.py` directly.
- Create water.

Expected output:

```text
=== Alembic 1 ===
Using: 'from ... import ...' structure to access elements.py
Testing create_water: Water element created
```

### `ft_alembic_2.py`

- Use the `import ...` structure to access `alchemy/elements.py` directly.
- Create earth.

Expected output:

```text
=== Alembic 2 ===
Accessing alchemy/elements.py using 'import ...' structure
Testing create_earth: Earth element created
```

### `ft_alembic_3.py`

- Use the `from ... import ...` structure to access `alchemy/elements.py` directly.
- Create air.

Expected output:

```text
=== Alembic 3 ===
Accessing alchemy/elements.py using 'from ... import ...' structure
Testing create_air: Air element created
```

### `ft_alembic_4.py`

- Use `import alchemy` to access the `alchemy` package.
- Create air through the package interface.
- Then demonstrate that `create_earth()` is not exposed through the package interface.
- Calling `alchemy.create_earth()` must raise an exception. This is intentional and
  pedagogical. A mypy error is also expected on purpose.

Expected successful part before the intentional exception:

```text
=== Alembic 4 ===
Accessing the alchemy module using 'import alchemy'
Testing create_air: Air element created
Now show that not all functions can be reached
This will raise an exception!
```

Then the script should raise an `AttributeError` because `alchemy` has no attribute
`create_earth`.

### `ft_alembic_5.py`

- Use the `from alchemy import ...` structure to access the `alchemy` package.
- Create air.

Expected output:

```text
=== Alembic 5 ===
Accessing the alchemy module using 'from alchemy import ...'
Testing create_air: Air element created
```

## Evaluation focus

- Difference between importing a module and importing names from a module.
- Role of `__init__.py` in package initialization and public package interface.
- Why a function can exist in `alchemy/elements.py` but not be available as
  `alchemy.create_earth()`.
