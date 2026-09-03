# Exercise 2: Accessing the Mainframe

Directory: `ex2/`

Files to submit:

- `oracle.py`
- `requirements.txt`
- `.env.example`
- `.gitignore`

Authorized imports:

- `os`
- `sys`
- `python-dotenv` modules
- file operations

## The Oracle

Create a secure configuration system using environment variables and `.env` files. The goal is to learn how to use `.env` files for configuration management with `python-dotenv`, not to implement a custom parser.

## Mission Briefing

Create `oracle.py` so it:

- Loads configuration from environment variables.
- Uses a `.env` file for development settings.
- Demonstrates different configuration for development and production.
- Includes proper error handling for missing configuration.

The development/production difference can be implemented freely, but it must be visible in the program output.

## Configuration Requirements

The program must handle these variables:

- `MATRIX_MODE`: `development` or `production`
- `DATABASE_URL`: connection string for data storage
- `API_KEY`: secret key for external services
- `LOG_LEVEL`: logging verbosity
- `ZION_ENDPOINT`: URL for the resistance network

Never commit real secrets. The real `.env` file must be ignored by `.gitignore`.

## Usage Examples

Without configuration:

```bash
python3 oracle.py
```

Using a `.env` file:

```bash
cp .env.example .env
python3 oracle.py
```

Environment variable override:

```bash
MATRIX_MODE=production API_KEY=secret123 python3 oracle.py
```

## Expected Output Structure

The output should include:

- `ORACLE STATUS: Reading the Matrix...`
- loaded configuration details
- development/production mode visibility
- missing/default configuration warnings when needed
- security checks for secrets and `.env`
- `The Oracle sees all configurations.`
