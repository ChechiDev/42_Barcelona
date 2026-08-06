#!/usr/bin/env python3

"""Focused tests for M05 exercise 2 data pipeline behavior"""

import ast
import subprocess
import sys
from pathlib import Path
from typing import Any


MODULE_DIR = Path(__file__).resolve().parents[1]
EX2_DIR = MODULE_DIR / "ex2"
SOURCE = EX2_DIR / "data_pipeline.py"
sys.path.insert(0, str(EX2_DIR))

from data_pipeline import (  # noqa: E402
    CSVExportPlugin,
    DataStream,
    JSONExportPlugin,
    LogProcessor,
    NumericProcessor,
    TextProcessor,
    build_log_entry,
    build_stream,
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


def test_output_pipeline_exports_from_each_processor(capsys: Any) -> None:
    """ Export available output from all processors """

    data_stream = DataStream()
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    data_stream.process_stream(build_stream(
        42,
        [1, 2],
        "Hello",
        ["Hi", "five"],
        [build_log_entry("INFO", "Connected")],
    ))

    data_stream.output_pipeline(2, CSVExportPlugin())
    output = capsys.readouterr().out

    assert "CSV Output:\n42,1" in output
    assert "CSV Output:\nHello,Hi" in output
    assert "CSV Output:\nINFO: Connected" in output


def test_get_processors_returns_copy_without_exposing_pipeline_order() -> None:
    """ Keep pipeline processor registration protected from callers """

    data_stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    data_stream.register_processor(numeric)

    processors = data_stream.get_processors()
    processors.insert(0, text)

    assert data_stream.get_processors() == [numeric]


def test_json_export_plugin_uses_output_ranks(capsys: Any) -> None:
    """ Export JSON keys using processor output ranks """

    plugin = JSONExportPlugin()

    plugin.process_output([(3, "value"), (4, 'quote " ok\n')])
    output = capsys.readouterr().out

    assert "JSON Output:" in output
    assert '{"item_3": "value", "item_4": "quote \\" ok\\n"}' in output


def test_script_execution_demonstrates_required_pipeline() -> None:
    """ Execute data_pipeline.py and verify key subject output """

    result = subprocess.run(
        [sys.executable, str(SOURCE)],
        check=True,
        text=True,
        capture_output=True,
    )
    output = result.stdout

    assert "=== Code Nexus - Data Pipeline ===" in output
    assert "CSV Output:\n3.14,-1,2.71" in output
    assert "JSON Output:" in output
    assert '"item_3": "42"' in output
    assert "Numeric Processor: total 11 items processed" in output
