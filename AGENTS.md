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

- Exercise demo and entrypoint standard:
  - Prefer `main()` as the executable entrypoint for scripts.
  - Use `if __name__ == "__main__": main()` when the subject expects direct script execution.
  - Avoid a separate `run_demo()` when the same flow can stay readable inside `main()`.
  - Keep exercise logic dynamic and reusable; do not hide fixed example data inside processing logic.
  - Put script/demo data in module-level constants when direct execution needs sample data.
  - Constants must use short `UPPER_CASE` names, without a `DEMO_` prefix, such as `NUM_VAL`, `NUM_INV_VAL`, `NUM_INV_ING`, `NUM_DATA`, `NUM_OUT_NB`, `TXT_DATA`, `LOG_ERR_MSG`.
  - Build compound demo structures in `main()` from constants and helper builders such as `build_log_entry()` or `build_stream()`.
  - Keep public exercise APIs and subject-required output text unchanged even when applying these conventions.

- Getter/setter style:
  - Prefer explicit `get_...()` methods over `@property` when following the project naming standard.
  - Do not add setters for internal processor state unless the subject or design requires external state replacement.
  - Preserve validation boundaries: data should normally enter through subject APIs such as `ingest()` and leave through `output()`.

- Docstring style:
  - Add a one-line English docstring immediately after every function or class header, formatted as `""" Text without final period """`, followed by one blank line.
  - Do not add docstrings to `__init__` methods.
