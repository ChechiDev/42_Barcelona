#!/usr/bin/env python3

"""Test M08 environment, dependency, and configuration exercises"""

import ast
import os
import subprocess
import sys
from pathlib import Path


M08_DIR = Path(__file__).resolve().parents[1]


def run_script(script_path: Path) -> subprocess.CompletedProcess[str]:
    """Run one M08 script and capture text output"""

    return subprocess.run(
        [sys.executable, str(script_path)],
        cwd=script_path.parent,
        check=False,
        capture_output=True,
        text=True,
    )


def test_construct_reports_current_environment() -> None:
    """Check construct prints environment status and executable"""

    result = run_script(M08_DIR / "ex0" / "construct.py")

    assert result.returncode == 0
    assert "MATRIX STATUS:" in result.stdout
    assert "Current Python:" in result.stdout
    assert "Virtual Environment:" in result.stdout


def test_loading_reports_dependencies_or_runs_analysis() -> None:
    """Check loading handles dependency state without crashing"""

    result = run_script(M08_DIR / "ex1" / "loading.py")

    assert result.returncode == 0
    assert "LOADING STATUS: Loading programs..." in result.stdout
    assert "Checking dependencies:" in result.stdout
    assert "Dependency management comparison:" in result.stdout
    assert (
        "Missing programs detected." in result.stdout
        or "Analysis complete!" in result.stdout
    )


def test_oracle_reports_missing_configuration_without_dotenv() -> None:
    """Check oracle runs safely with default or missing configuration"""

    result = run_script(M08_DIR / "ex2" / "oracle.py")

    assert result.returncode == 0
    assert "ORACLE STATUS: Reading the Matrix..." in result.stdout
    assert "Configuration loaded:" in result.stdout
    assert "Environment security check:" in result.stdout
    assert "The Oracle sees all configurations." in result.stdout


def test_oracle_uses_environment_overrides() -> None:
    """Check oracle reads direct environment overrides"""

    environment = os.environ.copy()
    environment.update({
        "MATRIX_MODE": "production",
        "DATABASE_URL": "postgresql://mainframe",
        "API_KEY": "secret123",
        "LOG_LEVEL": "INFO",
        "ZION_ENDPOINT": "https://zion.example",
    })
    result = subprocess.run(
        [sys.executable, str(M08_DIR / "ex2" / "oracle.py")],
        cwd=M08_DIR / "ex2",
        check=False,
        capture_output=True,
        text=True,
        env=environment,
    )
    assert result.returncode == 0
    assert "Mode: production" in result.stdout
    assert "Database: Connected to production mainframe" in result.stdout
    assert "API Access: Authenticated" in result.stdout
    assert "Zion Network: Production relay online" in result.stdout


def test_required_dependency_files_exist() -> None:
    """Check subject dependency and configuration files exist"""

    assert (M08_DIR / "ex1" / "requirements.txt").exists()
    assert (M08_DIR / "ex1" / "pyproject.toml").exists()
    assert (M08_DIR / "ex2" / "requirements.txt").exists()
    assert (M08_DIR / "ex2" / ".env.example").exists()
    assert (M08_DIR / "ex2" / ".gitignore").exists()
    assert ".env" in (M08_DIR / "ex2" / ".gitignore").read_text()


def test_functions_and_classes_follow_project_docstring_style() -> None:
    """Check M08 function and class docstrings follow project style"""

    for source_path in M08_DIR.rglob("*.py"):
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef),
            ):
                docstring = ast.get_docstring(node, clean=False)
                if (
                    isinstance(node, ast.FunctionDef)
                    and node.name == "__init__"
                ):
                    assert docstring is None, f"{source_path}:{node.lineno}"
                    continue
                assert docstring is not None, f"{source_path}:{node.lineno}"
                assert "\n" not in docstring, f"{source_path}:{node.lineno}"
                assert not docstring.endswith("."), (
                    f"{source_path}:{node.lineno}"
                )
