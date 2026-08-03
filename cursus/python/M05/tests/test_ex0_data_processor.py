#!/usr/bin/env python3

"""Focused tests for exercise 0 data processors"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[1]
EX0 = ROOT / "ex0"
sys.path.insert(0, str(EX0))

from data_processor import (  # noqa: E402
    DataProcessor,
    LogProcessor,
    NumericProcessor,
    TextProcessor,
    build_log_entry,
    run_demo,
)


def test_data_processor_is_abstract() -> None:
    """Ensure the common base class cannot be instantiated directly"""

    with pytest.raises(TypeError):
        DataProcessor()  # type: ignore[abstract]


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (42, True),
        (3.14, True),
        ([1, 2.5, 3], True),
        ([], True),
        (True, False),
        ([1, False], False),
        ("42", False),
        ([1, "2"], False),
    ],
)
def test_numeric_validate(value: object, expected: bool) -> None:
    """Validate numeric accepted and rejected input shapes"""

    assert NumericProcessor().validate(value) is expected


def test_numeric_ingest_outputs_fifo_strings_and_ranks() -> None:
    """Numeric data is stored as strings and emitted in FIFO rank order"""

    processor = NumericProcessor()
    processor.ingest([1, 2.5])
    processor.ingest(3)

    assert processor.get_data_len() == 3
    assert processor.output() == (0, "1")
    assert processor.output() == (1, "2.5")
    assert processor.output() == (2, "3")
    assert processor.get_data_len() == 0


@pytest.mark.parametrize("bad_value", ["foo", [1, "2"], True, [False]])
def test_numeric_ingest_rejects_invalid_data(bad_value: object) -> None:
    """Invalid numeric ingestion raises the required exception"""

    with pytest.raises(ValueError, match="Improper numeric data"):
        NumericProcessor().ingest(bad_value)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("hello", True),
        (["Hello", "Nexus"], True),
        ([], True),
        (42, False),
        (["ok", 1], False),
    ],
)
def test_text_validate(value: object, expected: bool) -> None:
    """Validate text accepted and rejected input shapes"""

    assert TextProcessor().validate(value) is expected


def test_text_ingest_outputs_fifo_values() -> None:
    """Text data is emitted unchanged in FIFO order"""

    processor = TextProcessor()
    processor.ingest(["Hello", "Nexus"])
    processor.ingest("World")

    assert [processor.output(), processor.output(), processor.output()] == [
        (0, "Hello"),
        (1, "Nexus"),
        (2, "World"),
    ]


def test_text_ingest_rejects_invalid_data() -> None:
    """Invalid text ingestion raises the required exception"""

    with pytest.raises(ValueError, match="Improper text data"):
        TextProcessor().ingest(["ok", 1])  # type: ignore[list-item]


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ({"log_level": "NOTICE", "log_message": "connected"}, True),
        ([{"log_level": "ERROR", "log_message": "denied"}], True),
        ({}, True),
        ([], True),
        ({"log_level": 1}, False),
        ({1: "bad"}, False),
        ([{"log_level": "OK"}, {"bad": 1}], False),
        ("hello", False),
    ],
)
def test_log_validate(value: object, expected: bool) -> None:
    """Validate log accepted and rejected input shapes"""

    assert LogProcessor().validate(value) is expected


def test_log_ingest_formats_and_outputs_fifo_values() -> None:
    """Log dictionaries are formatted and emitted in FIFO order"""

    processor = LogProcessor()
    processor.ingest(
        [
            {"log_level": "NOTICE", "log_message": "Connection to server"},
            {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
        ]
    )

    assert processor.output() == (0, "NOTICE: Connection to server")
    assert processor.output() == (1, "ERROR: Unauthorized access!!")


def test_log_ingest_accepts_single_entry() -> None:
    """A single log dictionary is ingested and formatted as one item"""

    processor = LogProcessor()
    processor.ingest({"log_level": "INFO", "log_message": "Started"})

    assert processor.get_data_len() == 1
    assert processor.output() == (0, "INFO: Started")


def test_log_ingest_rejects_invalid_data() -> None:
    """Invalid log ingestion raises the required exception"""

    with pytest.raises(ValueError, match="Improper log data"):
        LogProcessor().ingest({"log_level": 1})  # type: ignore[dict-item]


def test_output_empty_processor_raises_index_error() -> None:
    """Output without queued data reports that there is no data"""

    with pytest.raises(IndexError, match="No data to output"):
        TextProcessor().output()


def test_run_demo_prints_expected_demo_lines(capsys: Any) -> None:
    """Running run_demo executes the subject demonstration"""

    run_demo(
        42,
        "Hello",
        "foo",
        [1, 2, 3, 4, 5],
        42,
        ["Hello", "Nexus", "World"],
        "Hello",
        [
            build_log_entry("NOTICE", "Connection to server"),
            build_log_entry("ERROR", "Unauthorized access!!"),
        ],
        3,
        1,
        2,
    )
    output = capsys.readouterr().out

    assert "=== Code Nexus - Data Processor ===" in output
    assert "Got exception: Improper numeric data" in output
    assert "Numeric value 0: 1" in output
    assert "Text value 0: Hello" in output
    assert "Log entry 1: ERROR: Unauthorized access!!" in output
