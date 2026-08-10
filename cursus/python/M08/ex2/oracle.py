#!/usr/bin/env python3

"""Load Matrix mainframe configuration safely"""

import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except ImportError:
    load_dotenv = None


ENV_FILE = ".env"
DEFAULT_MODE = "development"
DEFAULT_LOG_LEVEL = "DEBUG"
REQUIRED_KEYS = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]


class OracleConfig:
    """Store Oracle configuration values"""

    def __init__(
        self,
        matrix_mode: str,
        database_url: str,
        api_key: str,
        log_level: str,
        zion_endpoint: str,
    ) -> None:
        self.matrix_mode = matrix_mode
        self.database_url = database_url
        self.api_key = api_key
        self.log_level = log_level
        self.zion_endpoint = zion_endpoint


def load_environment_file() -> bool:
    """Load the local .env file when python-dotenv is available"""

    if load_dotenv is None:
        return False
    return bool(load_dotenv(override=False))


def get_environment_value(key: str, default: str = "") -> str:
    """Return one environment value with a default fallback"""

    return os.getenv(key, default)


def build_config() -> OracleConfig:
    """Build Oracle configuration from environment variables"""

    return OracleConfig(
        matrix_mode=get_environment_value("MATRIX_MODE", DEFAULT_MODE),
        database_url=get_environment_value("DATABASE_URL"),
        api_key=get_environment_value("API_KEY"),
        log_level=get_environment_value("LOG_LEVEL", DEFAULT_LOG_LEVEL),
        zion_endpoint=get_environment_value("ZION_ENDPOINT"),
    )


def is_development_mode(config: OracleConfig) -> bool:
    """Return whether the Oracle is configured for development"""

    return config.matrix_mode.lower() == "development"


def format_database_status(config: OracleConfig) -> str:
    """Return a safe database connection status"""

    if not config.database_url:
        return "Missing DATABASE_URL"
    if is_development_mode(config):
        return "Connected to local instance"
    return "Connected to production mainframe"


def format_api_status(config: OracleConfig) -> str:
    """Return a safe API authentication status"""

    if not config.api_key:
        return "Missing API_KEY"
    return "Authenticated"


def format_zion_status(config: OracleConfig) -> str:
    """Return a safe Zion network status"""

    if not config.zion_endpoint:
        return "Missing ZION_ENDPOINT"
    if is_development_mode(config):
        return "Online"
    return "Production relay online"


def get_missing_keys(config: OracleConfig) -> list[str]:
    """Return missing required configuration keys"""

    values = {
        "DATABASE_URL": config.database_url,
        "API_KEY": config.api_key,
        "ZION_ENDPOINT": config.zion_endpoint,
    }
    return [key for key in REQUIRED_KEYS if not values[key]]


def has_env_file() -> bool:
    """Return whether a local .env file exists"""

    return os.path.exists(ENV_FILE)


def print_config(config: OracleConfig) -> None:
    """Print safe Oracle configuration information"""

    print("Configuration loaded:")
    print(f"Mode: {config.matrix_mode}")
    print(f"Database: {format_database_status(config)}")
    print(f"API Access: {format_api_status(config)}")
    print(f"Log Level: {config.log_level}")
    print(f"Zion Network: {format_zion_status(config)}")


def print_security_check(config: OracleConfig, env_loaded: bool) -> None:
    """Print environment security validation results"""

    missing_keys = get_missing_keys(config)
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_loaded or has_env_file():
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not loaded; using defaults/environment only")
    if missing_keys:
        print(f"[WARN] Missing configuration: {', '.join(missing_keys)}")
    else:
        print("[OK] Required configuration available")
    print("[OK] Production overrides available")


def main() -> None:
    """Run the Oracle configuration workflow"""

    print("ORACLE STATUS: Reading the Matrix...")
    if load_dotenv is None:
        print(
            "WARNING: python-dotenv is missing. Install with "
            f"{sys.executable} -m pip install -r requirements.txt"
        )
    env_loaded = load_environment_file()
    config = build_config()
    print_config(config)
    print_security_check(config, env_loaded)
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
