#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


NumericData = int | float | list[int | float]
TextData = str | list[str]
LogEntry = dict[str, str]
LogData = LogEntry | list[LogEntry]
OutputData = list[tuple[int, str]]

TXT_VAL = "Hello world"
NUM_DATA = [3.14, -1, 2.71]

LOG_WARN_LVL = "WARNING"
LOG_WARN_MSG = "Telnet access! Use ssh instead"
LOG_INFO_LVL = "INFO"
LOG_INFO_MSG = "User wil is connected"

NUM_VAL = 42
TXT_DATA = ["Hi", "five"]

CSV_OUT_NB = 3

NUM_VAL_2 = 21
TXT_DATA_2 = ["I love AI", "LLMs are wonderful", "Stay healthy"]
LOG_ERR_LVL = "ERROR"
LOG_ERR_MSG = "500 server crash"
LOG_NOTICE_LVL = "NOTICE"
LOG_NOTICE_MSG = "Certificate expires in 10 days"
NUM_DATA_2 = [32, 42, 64, 84, 128, 168]
TXT_VAL_2 = "World hello"

JSON_OUT_NB = 5


class ExportPlugin(Protocol):
    """ Define the output plugin protocol """

    def process_output(self, data: OutputData) -> None:
        """ Process output data from one processor """


class DataProcessor(ABC):
    """ Define the common interface for all data processors """

    def __init__(self, name: str) -> None:
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
    """ Route stream elements and export processor output """

    def __init__(self) -> None:
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """ Export up to nb outputs from every registered processor """

        for processor in self._processors:
            plugin.process_output(self._get_processor_outputs(processor, nb))

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
            # Polymorphism: DataStream uses the DataProcessor interface only.
            if processor.validate(element):
                processor.ingest(element)
                return True
        return False

    def _get_processor_outputs(
        self,
        processor: DataProcessor,
        amount: int,
    ) -> OutputData:
        """ Return available outputs from one processor """

        outputs: OutputData = []
        for _ in range(amount):
            if processor.get_data_len() == 0:
                break
            outputs.append(processor.output())
        return outputs


class CSVExportPlugin:
    """ Export processor output as CSV text """

    def process_output(self, data: OutputData) -> None:
        """ Print output data as a CSV line """

        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin:
    """ Export processor output as JSON text """

    def process_output(self, data: OutputData) -> None:
        """ Print output data as a JSON object """

        print("JSON Output:")
        print(self._format_json_object(data))

    def _format_json_object(self, data: OutputData) -> str:
        """ Return output data formatted as a JSON object """

        pairs = [
            f'"item_{rank}": "{self._format_json_string(value)}"'
            for rank, value in data
        ]
        return "{" + ", ".join(pairs) + "}"

    def _format_json_string(self, value: str) -> str:
        """ Return a manually escaped JSON string value """

        escaped = value.replace("\\", "\\\\")
        escaped = escaped.replace('"', '\\"')
        escaped = escaped.replace("\n", "\\n")
        escaped = escaped.replace("\r", "\\r")
        return escaped.replace("\t", "\\t")


def build_log_entry(level: str, message: str) -> LogEntry:
    """ Build one log entry from dynamic values """

    return {
        "log_level": level,
        "log_message": message,
    }


def build_stream(*items: Any) -> list[Any]:
    """ Build a stream from received items """

    return list(items)


def put_processors(data_stream: DataStream) -> None:
    """ Register all subject processors in one data stream """

    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())


def main() -> None:
    """ Run the script entrypoint """

    first_stream = build_stream(
        TXT_VAL,
        NUM_DATA,
        [
            build_log_entry(LOG_WARN_LVL, LOG_WARN_MSG),
            build_log_entry(LOG_INFO_LVL, LOG_INFO_MSG),
        ],
        NUM_VAL,
        TXT_DATA,
    )
    second_stream = build_stream(
        NUM_VAL_2,
        TXT_DATA_2,
        [
            build_log_entry(LOG_ERR_LVL, LOG_ERR_MSG),
            build_log_entry(LOG_NOTICE_LVL, LOG_NOTICE_MSG),
        ],
        NUM_DATA_2,
        TXT_VAL_2,
    )
    data_stream = DataStream()

    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    data_stream.print_processors_stats()

    print("Registering Processors")
    put_processors(data_stream)
    print(f"Send first batch of data on stream: {first_stream}")
    data_stream.process_stream(first_stream)
    data_stream.print_processors_stats()

    print(
        f"Send {CSV_OUT_NB} processed data from each processor "
        "to a CSV plugin:"
    )
    data_stream.output_pipeline(CSV_OUT_NB, CSVExportPlugin())
    data_stream.print_processors_stats()

    print(f"Send another batch of data: {second_stream}")
    data_stream.process_stream(second_stream)
    data_stream.print_processors_stats()

    print(
        f"Send {JSON_OUT_NB} processed data from each processor "
        "to a JSON plugin:"
    )
    data_stream.output_pipeline(JSON_OUT_NB, JSONExportPlugin())
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
