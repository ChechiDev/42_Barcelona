#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


NumericData = int | float | list[int | float]
TextData = str | list[str]
LogEntry = dict[str, str]
LogData = LogEntry | list[LogEntry]


class DataProcessor(ABC):
    """ Define the common interface for all data processors """

    def __init__(self) -> None:
        self._items: list[str] = []
        self._next_output_rank = 0

    def get_data_len(self) -> int:
        """ Return the number of items waiting on the processor """

        return len(self._items)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """ Return whether data can be ingested by this processor """

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """ Ingest valid data into this processor """

    def output(self) -> tuple[int, str]:
        """ Extract and return the oldest stored item with its rank """

        if not self._items:
            raise IndexError("No data to output")

        rank = self._next_output_rank
        item = self._items.pop(0)
        self._next_output_rank += 1

        return rank, item

    def _put_item(self, item: str) -> None:
        """ Store one processed item """

        self._items.append(item)

    def _put_items(self, items: list[str]) -> None:
        """ Store several processed items """

        self._items.extend(items)

    def _put_scalar_or_list(self, data: Any) -> None:
        """ Store one value or every value from a list as strings """

        if isinstance(data, list):
            self._put_items([str(item) for item in data])
            return
        self._put_item(str(data))


class NumericProcessor(DataProcessor):
    """ Process numeric values and lists of numeric values """

    def validate(self, data: Any) -> bool:
        """ Return whether data is numeric or a numeric list """

        if isinstance(data, list):
            return all(self._is_numeric(item) for item in data)
        return self._is_numeric(data)

    def ingest(self, data: NumericData) -> None:
        """ Ingest numeric data as separated string items """

        if not self.validate(data):
            raise ValueError("Improper numeric data")

        self._put_scalar_or_list(data)

    def _is_numeric(self, data: Any) -> bool:
        """ Return whether data is a non-boolean number """

        return isinstance(data, (int, float)) and not isinstance(data, bool)


class TextProcessor(DataProcessor):
    """ Process text values and lists of text values """

    def validate(self, data: Any) -> bool:
        """ Return whether data is text or a text list """

        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: TextData) -> None:
        """ Ingest text data as separated string items """

        if not self.validate(data):
            raise ValueError("Improper text data")

        self._put_scalar_or_list(data)


class LogProcessor(DataProcessor):
    """ Process log dictionaries and lists of log dictionaries """

    def validate(self, data: Any) -> bool:
        """ Return whether data is a valid log entry or list """

        if isinstance(data, dict):
            return self._is_log_entry(data)
        if isinstance(data, list):
            return all(self._is_log_entry(item) for item in data)
        return False

    def ingest(self, data: LogData) -> None:
        """ Ingest log data as separated formatted strings """

        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            self._put_items([self._format_log_entry(item) for item in data])
            return
        self._put_item(self._format_log_entry(data))

    def _is_log_entry(self, data: Any) -> bool:
        """ Return whether data is a dictionary with string pairs """

        return isinstance(data, dict) and all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in data.items()
        )

    def _format_log_entry(self, entry: LogEntry) -> str:
        """ Convert a log entry into the expected output format """

        level = entry.get("log_level", "")
        message = entry.get("log_message", "")
        if level or message:
            return f"{level}: {message}"
        return str(entry)


def print_validation(processor: DataProcessor, value: Any) -> None:
    """ Print the validation result for one value """

    print(f"Trying to validate input'{value}': {processor.validate(value)}")


def print_outputs(
    processor: DataProcessor,
    amount: int,
    label: str,
) -> None:
    """ Print a fixed number of processor outputs """

    for _ in range(amount):
        rank, value = processor.output()
        print(f"{label} {rank}: {value}")


def run_numeric_processor_demo() -> None:
    """ Run the numeric processor demo """

    processor = NumericProcessor()
    print()
    print("Testing Numeric Processor...")
    print_validation(processor, 42)
    print_validation(processor, "Hello")
    print("Test invalid ingestion of string'foo'without prior validation:")

    try:
        processor.ingest("foo")  # type: ignore[arg-type]
    except ValueError as error:
        print(f"Got exception: {error}")

    numeric_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    processor.ingest(numeric_data)
    print("Extracting 3 values...")
    print_outputs(processor, 3, "Numeric value")


def run_text_processor_demo() -> None:
    """ Run the text processor demo """

    processor = TextProcessor()
    print()
    print("Testing Text Processor...")
    print_validation(processor, 42)
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    processor.ingest(text_data)
    print("Extracting 1 value...")
    print_outputs(processor, 1, "Text value")


def run_log_processor_demo() -> None:
    """ Run the log processor demo """

    processor = LogProcessor()
    print()
    print("Testing Log Processor...")
    print_validation(processor, "Hello")
    log_data = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f"Processing data: {log_data}")
    processor.ingest(log_data)
    print("Extracting 2 values...")
    print_outputs(processor, 2, "Log entry")


def run_demo() -> None:
    """ Run the data processor demo"""

    print("=== Code Nexus - Data Processor ===")
    run_numeric_processor_demo()
    run_text_processor_demo()
    run_log_processor_demo()


if __name__ == "__main__":
    run_demo()
