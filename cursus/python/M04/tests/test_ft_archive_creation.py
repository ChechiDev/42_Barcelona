#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "ex1" / "ft_archive_creation.py"


def run_script(
    *args: str,
    stdin: str = "",
) -> subprocess.CompletedProcess[str]:
    """ Run the archive creation script with the provided arguments """

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
    assert result.stdout == "Usage: ft_archive_creation.py <file>\n"
    assert result.stderr == ""


def test_missing_input_file_prints_preservation_error(tmp_path: Path) -> None:
    """ Check that missing files print the preservation error output """

    missing_file = tmp_path / "missing_fragment.txt"

    result = run_script(str(missing_file))

    assert result.returncode == 0
    assert result.stdout == (
        "=== Cyber Archives Recovery & Preservation ===\n"
        f"Accessing file '{missing_file}'\n"
        f"Error opening file '{missing_file}': [Errno 2] "
        f"No such file or directory: '{missing_file}'\n"
    )
    assert result.stderr == ""


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
