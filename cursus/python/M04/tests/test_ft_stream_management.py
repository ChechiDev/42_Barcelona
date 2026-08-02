#!/usr/bin/env python3

import ast
import subprocess
import sys
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "ex2"
    / "ft_stream_management.py"
)


def run_script(
    *args: str,
    stdin: str = "",
) -> subprocess.CompletedProcess[str]:
    """ Run the stream management script with the provided arguments """

    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=False,
        capture_output=True,
        input=stdin,
        text=True,
    )


def test_no_arguments_prints_usage() -> None:
    """ Check that missing arguments print the usage message """

    result = run_script()

    assert result.returncode == 0
    assert result.stdout == "Usage: ft_stream_management.py <file>\n"
    assert result.stderr == ""


def test_missing_input_file_prints_prefixed_error_to_stderr(
    tmp_path: Path,
) -> None:
    """ Check that missing files report prefixed errors on stderr """

    missing_file = tmp_path / "missing_fragment.txt"

    result = run_script(str(missing_file))

    assert result.returncode == 0
    assert result.stdout == (
        "=== Cyber Archives Recovery & Preservation ===\n"
        f"Accessing file '{missing_file}'\n"
    )
    assert result.stderr == (
        f"[STDERR] Error opening file '{missing_file}': [Errno 2] "
        f"No such file or directory: '{missing_file}'\n"
    )


def test_valid_file_with_empty_save_name_does_not_create_output(
    tmp_path: Path,
) -> None:
    """ Check that empty save names avoid saving transformed data """

    fragment_file = tmp_path / "ancient_fragment.txt"
    fragment_file.write_text(
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )

    result = run_script(str(fragment_file), stdin="\n")

    assert result.returncode == 0
    assert result.stdout == (
        "=== Cyber Archives Recovery & Preservation ===\n"
        f"Accessing file '{fragment_file}'\n"
        "---\n"
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
        "---\n"
        f"File '{fragment_file}' closed.\n"
        "Transform data:\n"
        "---\n"
        "[FRAGMENT 001] Digital preservation protocols established 2087#\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars#\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion#\n"
        "---\n"
        "Enter new file name (or empty): Not saving data.\n"
    )
    assert result.stderr == ""
    assert list(tmp_path.iterdir()) == [fragment_file]


def test_valid_file_with_save_name_writes_transformed_output(
    tmp_path: Path,
) -> None:
    """ Check that provided save names write transformed archive data """

    fragment_file = tmp_path / "ancient_fragment.txt"
    output_file = tmp_path / "new_fragment.txt"
    fragment_file.write_text(
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )

    result = run_script(str(fragment_file), stdin=f"{output_file}\n")

    expected_content = (
        "[FRAGMENT 001] Digital preservation protocols established 2087#\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars#\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion#\n"
    )
    assert result.returncode == 0
    assert result.stdout == (
        "=== Cyber Archives Recovery & Preservation ===\n"
        f"Accessing file '{fragment_file}'\n"
        "---\n"
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
        "---\n"
        f"File '{fragment_file}' closed.\n"
        "Transform data:\n"
        "---\n"
        f"{expected_content}"
        "---\n"
        "Enter new file name (or empty): "
        f"Saving data to '{output_file}'\n"
        f"Data saved in file '{output_file}'.\n"
    )
    assert result.stderr == ""
    assert output_file.read_text() == expected_content


def test_save_failure_prints_prefixed_error_to_stderr(
    tmp_path: Path,
) -> None:
    """ Check that save failures report prefixed errors on stderr """

    fragment_file = tmp_path / "ancient_fragment.txt"
    invalid_output = tmp_path / "archive_directory"
    fragment_file.write_text("Preserve this line\n")
    invalid_output.mkdir()

    result = run_script(str(fragment_file), stdin=f"{invalid_output}\n")

    assert result.returncode == 0
    assert result.stdout == (
        "=== Cyber Archives Recovery & Preservation ===\n"
        f"Accessing file '{fragment_file}'\n"
        "---\n"
        "Preserve this line\n"
        "---\n"
        f"File '{fragment_file}' closed.\n"
        "Transform data:\n"
        "---\n"
        "Preserve this line#\n"
        "---\n"
        "Enter new file name (or empty): "
        f"Saving data to '{invalid_output}'\n"
        "Data not saved.\n"
    )
    assert result.stderr.startswith(
        f"[STDERR] Error opening file '{invalid_output}': [Errno "
    )


def test_source_uses_streams_without_input_builtin() -> None:
    """ Check that source uses stdin readline and never input """

    tree = ast.parse(SCRIPT.read_text())
    calls = [
        node.func for node in ast.walk(tree) if isinstance(node, ast.Call)
    ]

    assert not any(
        isinstance(call, ast.Name) and call.id == "input" for call in calls
    )
    assert any(
        isinstance(call, ast.Attribute)
        and call.attr == "readline"
        and isinstance(call.value, ast.Attribute)
        and call.value.attr == "stdin"
        and isinstance(call.value.value, ast.Name)
        and call.value.value.id == "sys"
        for call in calls
    )


def test_source_imports_only_authorized_modules() -> None:
    """ Check that source imports stay within subject constraints """

    tree = ast.parse(SCRIPT.read_text())

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert {alias.name for alias in node.names} <= {"sys", "typing"}
        if isinstance(node, ast.ImportFrom):
            raise AssertionError("from imports are not authorized")


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
