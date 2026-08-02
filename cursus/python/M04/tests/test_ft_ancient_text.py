#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "ex0" / "ft_ancient_text.py"


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    """ Run the ancient text script with the provided arguments """

    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def test_no_arguments_prints_usage() -> None:
    """ Check that missing arguments print the usage message """

    result = run_script()

    assert result.returncode == 0
    assert result.stdout == "Usage: ft_ancient_text.py <file>\n"
    assert result.stderr == ""


def test_nonexistent_file_prints_recovery_header_and_error(
    tmp_path: Path,
) -> None:
    """ Check that missing files print the recovery error output """

    missing_file = tmp_path / "missing_fragment.txt"

    result = run_script(str(missing_file))

    assert result.returncode == 0
    assert result.stdout == (
        "=== Cyber Archives Recovery ===\n"
        f"Accessing file '{missing_file}'\n"
        f"Error opening file '{missing_file}': [Errno 2] "
        f"No such file or directory: '{missing_file}'\n"
    )
    assert result.stderr == ""


def test_valid_file_prints_wrapped_contents_and_close_message(
    tmp_path: Path,
) -> None:
    """ Check that valid files print wrapped contents and close message """

    fragment_file = tmp_path / "ancient_fragment.txt"
    fragment_file.write_text(
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )

    result = run_script(str(fragment_file))

    assert result.returncode == 0
    assert result.stdout == (
        "=== Cyber Archives Recovery ===\n"
        f"Accessing file '{fragment_file}'\n"
        "---\n"
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
        "---\n"
        f"File '{fragment_file}' closed.\n"
    )
    assert result.stderr == ""
