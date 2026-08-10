# Exercise 2: Accessing the Mainframe

Create `ex2/oracle.py`, `ex2/requirements.txt`, `ex2/.env.example`, and `ex2/.gitignore` to demonstrate secure configuration through environment variables.

## Requirements

- Use `python-dotenv` to load `.env` files.
- Read configuration from environment variables.
- Support development and production modes.
- Handle missing configuration safely with warnings/defaults.
- Use these variables:
  - `MATRIX_MODE`
  - `DATABASE_URL`
  - `API_KEY`
  - `LOG_LEVEL`
  - `ZION_ENDPOINT`
- Never commit real `.env` secrets.
- `.env` must be ignored by `.gitignore`.
- Environment variable overrides must take priority over `.env` values.

## Expected concepts

- Secure configuration management.
- Development vs production configuration.
- Secret masking and missing configuration checks.
