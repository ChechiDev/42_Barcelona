#!/usr/bin/env python3

"""Focused tests for M05 exercise 1 data stream behavior"""

import ast
import sys
from pathlib import Path
from typing import Any

import pytest


MODULE_DIR = Path(__file__).resolve().parents[1]
EX1_DIR = MODULE_DIR / "ex1"
SOURCE = EX1_DIR / "data_stream.py"
sys.path.insert(0, str(EX1_DIR))

from data_stream import (  # noqa: E402
    DataStream,
    DataProcessor,
    LogProcessor,
    NumericProcessor,
    TextProcessor,
    build_log_entry,
    build_stream,
    main,
    put_processor_outputs,
)


def drain(processor: DataProcessor) -> list[tuple[int, str]]:
    """ Return all pending processor outputs """

    return [processor.output() for _ in range(processor.get_data_len())]


def build_subject_stream() -> list[Any]:
    """ Build the stream used by the subject scenario tests """

    return build_stream(
        "Hello world",
        [3.14, -1, 2.71],
        [
            build_log_entry("WARNING", "Telnet access! Use ssh instead"),
            build_log_entry("INFO", "User wil is connected"),
        ],
        42,
        ["Hi", "five"],
    )


def test_source_uses_only_authorized_imports() -> None:
    """ Reject imports outside the exercise allowlist """

    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")

    assert set(imports) <= {"abc", "typing"}


def test_process_stream_routes_to_registered_processors_and_reports_errors(
    capsys: Any,
) -> None:
    """ Route elements polymorphically and report unsupported data """

    stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    stream.process_stream([
        "Hello world",
        [3.14, -1, 2.71],
        [{"log_level": "INFO", "log_message": "Connected"}],
        42,
        ["Hi", "five"],
        [1, "mixed"],
    ])

    captured = capsys.readouterr().out
    assert (
        "DataStream error - Can't process element in stream: [1, 'mixed']"
        in captured
    )
    assert drain(numeric) == [
        (0, "3.14"),
        (1, "-1"),
        (2, "2.71"),
        (3, "42"),
    ]
    assert drain(text) == [(0, "Hello world"), (1, "Hi"), (2, "five")]
    assert drain(log) == [(0, "INFO: Connected")]


def test_stats_match_subject_counts_after_processing_and_consuming(
    capsys: Any,
) -> None:
    """ Print stream statistics with total and remaining counts """

    stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    stream.print_processors_stats()
    initial_stats = capsys.readouterr().out
    assert "== DataStream statistics ==" in initial_stats
    assert "No processor found, no data" in initial_stats

    stream.register_processor(numeric)
    stream.process_stream(build_subject_stream())
    capsys.readouterr()
    stream.register_processor(text)
    stream.register_processor(log)
    stream.process_stream(build_subject_stream())
    put_processor_outputs(numeric, 3)
    put_processor_outputs(text, 2)
    put_processor_outputs(log, 1)

    stream.print_processors_stats()
    stats = capsys.readouterr().out
    assert (
        "Numeric Processor: total 8 items processed, remaining 5 on processor"
        in stats
    )
    assert (
        "Text Processor: total 3 items processed, remaining 1 on processor"
        in stats
    )
    assert (
        "Log Processor: total 2 items processed, remaining 1 on processor"
        in stats
    )


def test_get_processors_returns_copy_without_exposing_registration() -> None:
    """ Keep registered processor storage protected from callers """

    stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    stream.register_processor(numeric)

    processors = stream.get_processors()
    processors.append(text)

    assert stream.get_processors() == [numeric]


def test_processor_validation_edge_cases_and_empty_output() -> None:
    """ Cover validation boundaries and empty output errors """

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    assert not numeric.validate(True)
    assert numeric.validate([])
    assert text.validate([])
    assert log.validate([])
    assert log.validate({"any": "string pairs are valid"})
    assert not log.validate({"log_level": "INFO", "count": 1})

    with pytest.raises(ValueError, match="Improper numeric data"):
        numeric.ingest([1, True])
    with pytest.raises(ValueError, match="Improper text data"):
        text.ingest(["ok", 1])  # type: ignore[list-item]
    with pytest.raises(ValueError, match="Improper log data"):
        log.ingest({
            "log_level": "INFO",
            "count": 1,  # type: ignore[dict-item]
        })
    with pytest.raises(IndexError, match="No data to output"):
        numeric.output()


def test_main_demonstrates_required_scenario(capsys: Any) -> None:
    """ Execute main and verify key subject output """

    main()
    output = capsys.readouterr().out
    assert "=== Code Nexus - Data Stream ===" in output
    assert "Registering Numeric Processor" in output
    assert "Registering other data processors" in output
    assert (
        "DataStream error - Can't process element in stream: Hello world"
        in output
    )
    assert (
        "Numeric Processor: total 8 items processed, remaining 5 on processor"
        in output
    )
    assert (
        "Text Processor: total 3 items processed, remaining 1 on processor"
        in output
    )
    assert (
        "Log Processor: total 2 items processed, remaining 1 on processor"
        in output
    )
