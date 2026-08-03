# Project instructions

- Every Python source file must start with this exact shebang as the first line:

  ```python
  #!/usr/bin/env python3
  ```

- Add exactly one blank line after the shebang before imports, module docstrings, or code.

- Apply this naming standard when writing Python code, unless an exercise subject requires a specific public name:
  - `get_`: return or retrieve data.
  - `set_`: assign or replace state.
  - `put_`: add, store, enqueue, send, or append data.
  - `is_`: return a boolean about state, type, or condition.
  - `has_`: return a boolean about existence or presence.
  - `can_`: return a boolean about capability or permission.
  - `build_`: create and return a new object, collection, or fixture.
  - `print_`: print to standard output.
  - `run_`: execute a workflow, demo, or scenario.
  - `load_`: load data from a file or external source.
  - `save_`: save data to a file or external destination.
  - `parse_`: convert raw text/data into structured data.
  - `format_`: convert structured data into display/export text.
  - `validate_`: validate data when the subject or clarity requires that prefix.
  - `test_`: pytest test functions.

- Required subject APIs always take priority over the naming standard. Keep names such as `validate`, `ingest`, or `output` unchanged when the subject requires them.
