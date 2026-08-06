#!/usr/bin/env python3

import ast
import runpy
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import cast


EXERCISE_DIR = Path(__file__).resolve().parents[1] / "ex3"
SCRIPT = EXERCISE_DIR / "ft_vault_security.py"
FRAGMENT = EXERCISE_DIR / "ancient_fragment.txt"
GENERATED_FRAGMENT = EXERCISE_DIR / "new_fragment.txt"


def load_secure_archive() -> Callable[[str, str, str], tuple[bool, str]]:
    """ Load secure_archive from the exercise script without running main """

    namespace = runpy.run_path(str(SCRIPT), run_name="ft_vault_security")
    return cast(
        Callable[[str, str, str], tuple[bool, str]],
        namespace["secure_archive"],
    )


def run_script_from_exercise_dir() -> subprocess.CompletedProcess[str]:
    """ Run the vault security script from its exercise directory """

    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        check=False,
        capture_output=True,
        cwd=EXERCISE_DIR,
        text=True,
    )


def test_secure_archive_reads_existing_file() -> None:
    """ Check that secure_archive returns successful file contents """

    secure_archive = load_secure_archive()

    result = secure_archive(str(FRAGMENT), "read", "")

    assert result == (True, FRAGMENT.read_text())


def test_secure_archive_reports_read_failure(tmp_path: Path) -> None:
    """ Check that secure_archive returns false and an error string """

    secure_archive = load_secure_archive()
    missing_file = tmp_path / "missing_fragment.txt"

    success, message = secure_archive(str(missing_file), "read", "")

    assert success is False
    assert "No such file or directory" in message
    assert str(missing_file) in message


def test_secure_archive_writes_file_successfully(tmp_path: Path) -> None:
    """ Check that secure_archive writes content and returns success """

    secure_archive = load_secure_archive()
    output_file = tmp_path / "new_fragment.txt"
    content = "Preserved archive data\n"

    result = secure_archive(str(output_file), "write", content)

    assert result == (True, "Content successfully written to file")
    assert output_file.read_text() == content


def test_script_demo_prints_subject_structure_and_writes_output() -> None:
    """ Check that the demo output structure writes the new fragment """

    if GENERATED_FRAGMENT.exists():
        GENERATED_FRAGMENT.unlink()

    try:
        result = run_script_from_exercise_dir()

        assert result.returncode == 0
        assert result.stderr == ""
        assert result.stdout.startswith(
            "=== Cyber Archives Security ===\n"
            "Using 'secure_archive' to read from a nonexistent file:\n"
            "(False, \"[Errno 2] No such file or directory: "
        )
        assert (
            "Using 'secure_archive' to read from an inaccessible file:\n"
            in result.stdout
        )
        assert (
            "Using 'secure_archive' to read from a regular file:\n"
            in result.stdout
        )
        assert repr(FRAGMENT.read_text()) in result.stdout
        assert result.stdout.endswith(
            "Using 'secure_archive' to write previous content to a new file:\n"
            "(True, 'Content successfully written to file')\n"
        )
        assert GENERATED_FRAGMENT.read_text() == FRAGMENT.read_text()
    finally:
        if GENERATED_FRAGMENT.exists():
            GENERATED_FRAGMENT.unlink()


def test_source_defines_secure_archive_contract_and_context_manager() -> None:
    """ Check the required function and context manager usage """

    tree = ast.parse(SCRIPT.read_text())
    secure_archive_nodes = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "secure_archive"
    ]

    assert len(secure_archive_nodes) == 1
    assert any(
        isinstance(node, ast.With)
        for node in ast.walk(tree)
    )
    assert any(
        isinstance(node, ast.Return)
        and isinstance(node.value, ast.Tuple)
        and len(node.value.elts) == 2
        for node in ast.walk(secure_archive_nodes[0])
    )


def test_source_uses_only_authorized_imports_and_calls() -> None:
    """ Check source stays focused on authorized file operations """

    tree = ast.parse(SCRIPT.read_text())
    allowed_name_calls = {
        "is_read_action",
        "is_write_action",
        "main",
        "open",
        "print",
        "read_archive",
        "secure_archive",
        "write_archive",
    }
    allowed_attribute_calls = {"read", "write"}

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            raise AssertionError("imports are not authorized")
        if isinstance(node, ast.Call):
            function = node.func
            if isinstance(function, ast.Name):
                assert function.id in allowed_name_calls
            elif isinstance(function, ast.Attribute):
                assert function.attr in allowed_attribute_calls
            else:
                raise AssertionError(
                    f"unexpected call node: {ast.dump(function)}"
                )


def test_source_uses_exception_alias_e() -> None:
    """ Check that handled exceptions use the expected alias """

    tree = ast.parse(SCRIPT.read_text())
    handlers = [
        node for node in ast.walk(tree) if isinstance(node, ast.ExceptHandler)
    ]

    assert handlers
    assert all(handler.name == "e" for handler in handlers)


def test_source_layout_and_docstring_conventions() -> None:
    """ Check shebang spacing and one-line function docstrings """

    lines = SCRIPT.read_text().splitlines()
    tree = ast.parse("\n".join(lines))
    function_nodes = [
        node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    ]

    assert lines[0] == "#!/usr/bin/env python3"
    assert lines[1] == ""

    for node in function_nodes:
        assert node.lineno >= 3
        assert lines[node.lineno - 2] == ""
        assert lines[node.lineno - 3] == ""
        assert isinstance(node.body[0], ast.Expr)
        assert isinstance(node.body[0].value, ast.Constant)
        assert isinstance(node.body[0].value.value, str)

        docstring_line = lines[node.body[0].lineno - 1]
        assert docstring_line.startswith('    """ ')
        assert docstring_line.endswith(' """')
        assert docstring_line.count('"""') == 2
        assert not node.body[0].value.value.endswith(".")
        assert lines[node.body[0].lineno] == ""
