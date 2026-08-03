#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


NumericData = int | float | list[int | float]
TextData = str | list[str]
LogEntry = dict[str, str]
LogData = LogEntry | list[LogEntry]


class DataProcessor(ABC):
    """ Define the common interface for all data processors """

    def __init__(self, name: str) -> None:
        """ Initialize a named processor with empty storage """

        self._name = name
        self._items: list[str] = []
        self._next_output_rank = 0
        self._total_processed = 0

    def get_name(self) -> str:
        """ Return the processor display name """

        return self._name

    def get_data_len(self) -> int:
        """ Return the number of items waiting on the processor """

        return len(self._items)

    def get_total_processed(self) -> int:
        """ Return the total number of ingested items """

        return self._total_processed

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
        """ Store one processed item and update statistics """

        self._items.append(item)
        self._total_processed += 1

    def _put_items(self, items: list[str]) -> None:
        """ Store several processed items and update statistics """

        self._items.extend(items)
        self._total_processed += len(items)

    def _put_scalar_or_list(self, data: Any) -> None:
        """ Store one value or every value from a list as strings """

        if isinstance(data, list):
            self._put_items([str(item) for item in data])
            return
        self._put_item(str(data))


class NumericProcessor(DataProcessor):
    """ Process numeric values and lists of numeric values """

    def __init__(self) -> None:
        """ Initialize a numeric processor """

        super().__init__("Numeric Processor")

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

    def __init__(self) -> None:
        """ Initialize a text processor """

        super().__init__("Text Processor")

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

    def __init__(self) -> None:
        """ Initialize a log processor """

        super().__init__("Log Processor")

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


class DataStream:
    """ Route stream elements to registered data processors """

    def __init__(self) -> None:
        """ Initialize an empty data stream """

        self._processors: list[DataProcessor] = []

    def get_processors(self) -> list[DataProcessor]:
        """ Return registered processors """

        return self._processors

    def register_processor(self, proc: DataProcessor) -> None:
        """ Register a data processor for future stream processing """

        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """ Send each stream element to the first compatible processor """

        for element in stream:
            if not self._put_element(element):
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        """ Print statistics for every registered processor """

        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            print(
                f"{processor.get_name()}: total "
                f"{processor.get_total_processed()} items processed, "
                f"remaining {processor.get_data_len()} on processor"
            )

    def _put_element(self, element: Any) -> bool:
        """ Return whether an element was sent to a processor """

        for processor in self._processors:
            if processor.validate(element):
                processor.ingest(element)
                return True
        return False


def put_processor_outputs(processor: DataProcessor, amount: int) -> None:
    """ Consume a fixed number of values from a processor """

    for _ in range(amount):
        processor.output()


def build_demo_stream() -> list[Any]:
    """ Build the demonstration data stream from the subject """

    return [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]


def run_demo() -> None:
    """ Run the data stream demonstration scenario """

    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    numeric_processor = NumericProcessor()
    print("Registering Numeric Processor")
    data_stream.register_processor(numeric_processor)
    demo_stream = build_demo_stream()
    print(f"Send first batch of data on stream: {demo_stream}")
    data_stream.process_stream(demo_stream)
    data_stream.print_processors_stats()

    text_processor = TextProcessor()
    log_processor = LogProcessor()
    print("Registering other data processors")
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)
    print("Send the same batch again")
    data_stream.process_stream(demo_stream)
    data_stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    put_processor_outputs(numeric_processor, 3)
    put_processor_outputs(text_processor, 2)
    put_processor_outputs(log_processor, 1)
    data_stream.print_processors_stats()


if __name__ == "__main__":
    run_demo()
