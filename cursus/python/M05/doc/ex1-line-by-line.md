# M05 ex1: explicación línea por línea

Este documento vincula cada línea de `ex1/data_stream.py` con lo que hace.

| Línea | Qué hace |
| --- | --- |
| 1 | Indica al sistema que ejecute el archivo con `python3`. |
| 2 | Línea en blanco de separación. |
| 3 | Importa `abc import ABC, abstractmethod`. |
| 4 | Importa `typing import Any`. |
| 5 | Línea en blanco de separación. |
| 6 | Línea en blanco de separación. |
| 7 | Ejecuta `NumericData = int \| float \| list[int \| float]`. |
| 8 | Ejecuta `TextData = str \| list[str]`. |
| 9 | Ejecuta `LogEntry = dict[str, str]`. |
| 10 | Ejecuta `LogData = LogEntry \| list[LogEntry]`. |
| 11 | Línea en blanco de separación. |
| 12 | Ejecuta `TXT_VAL = "Hello world"`. |
| 13 | Ejecuta `NUM_DATA = [3.14, -1, 2.71]`. |
| 14 | Línea en blanco de separación. |
| 15 | Ejecuta `LOG_WARN_LVL = "WARNING"`. |
| 16 | Ejecuta `LOG_WARN_MSG = "Telnet access! Use ssh instead"`. |
| 17 | Ejecuta `LOG_INFO_LVL = "INFO"`. |
| 18 | Ejecuta `LOG_INFO_MSG = "User wil is connected"`. |
| 19 | Línea en blanco de separación. |
| 20 | Ejecuta `NUM_VAL = 42`. |
| 21 | Ejecuta `TXT_DATA = ["Hi", "five"]`. |
| 22 | Línea en blanco de separación. |
| 23 | Ejecuta `NUM_OUT_NB = 3`. |
| 24 | Ejecuta `TXT_OUT_NB = 2`. |
| 25 | Ejecuta `LOG_OUT_NB = 1`. |
| 26 | Línea en blanco de separación. |
| 27 | Línea en blanco de separación. |
| 28 | Declara `class DataProcessor(ABC):`. |
| 29 | Docstring: `""" Define the common interface for all data processors """`. |
| 30 | Línea en blanco de separación. |
| 31 | Declara `def __init__(self, name: str) -> None:`. |
| 32 | Ejecuta `self._name = name`. |
| 33 | Ejecuta `self._items: list[str] = []`. |
| 34 | Ejecuta `self._next_output_rank = 0`. |
| 35 | Ejecuta `self._total_processed = 0`. |
| 36 | Línea en blanco de separación. |
| 37 | Declara `def get_name(self) -> str:`. |
| 38 | Docstring: `""" Return the processor display name """`. |
| 39 | Línea en blanco de separación. |
| 40 | Devuelve `self._name`. |
| 41 | Línea en blanco de separación. |
| 42 | Declara `def get_data_len(self) -> int:`. |
| 43 | Docstring: `""" Return the number of items waiting on the processor """`. |
| 44 | Línea en blanco de separación. |
| 45 | Devuelve `len(self._items)`. |
| 46 | Línea en blanco de separación. |
| 47 | Declara `def get_total_processed(self) -> int:`. |
| 48 | Docstring: `""" Return the total number of ingested items """`. |
| 49 | Línea en blanco de separación. |
| 50 | Devuelve `self._total_processed`. |
| 51 | Línea en blanco de separación. |
| 52 | Aplica el decorador `@abstractmethod`. |
| 53 | Declara `def validate(self, data: Any) -> bool:`. |
| 54 | Docstring: `""" Return whether data can be ingested by this processor """`. |
| 55 | Línea en blanco de separación. |
| 56 | Aplica el decorador `@abstractmethod`. |
| 57 | Declara `def ingest(self, data: Any) -> None:`. |
| 58 | Docstring: `""" Ingest valid data into this processor """`. |
| 59 | Línea en blanco de separación. |
| 60 | Declara `def output(self) -> tuple[int, str]:`. |
| 61 | Docstring: `""" Extract and return the oldest stored item with its rank """`. |
| 62 | Línea en blanco de separación. |
| 63 | Comprueba `not self._items`. |
| 64 | Lanza `IndexError("No data to output")`. |
| 65 | Línea en blanco de separación. |
| 66 | Ejecuta `rank = self._next_output_rank`. |
| 67 | Ejecuta `item = self._items.pop(0)`. |
| 68 | Ejecuta `self._next_output_rank += 1`. |
| 69 | Línea en blanco de separación. |
| 70 | Devuelve `rank, item`. |
| 71 | Línea en blanco de separación. |
| 72 | Declara `def _put_item(self, item: str) -> None:`. |
| 73 | Docstring: `""" Store one processed item and update statistics """`. |
| 74 | Línea en blanco de separación. |
| 75 | Ejecuta `self._items.append(item)`. |
| 76 | Ejecuta `self._total_processed += 1`. |
| 77 | Línea en blanco de separación. |
| 78 | Declara `def _put_items(self, items: list[str]) -> None:`. |
| 79 | Docstring: `""" Store several processed items and update statistics """`. |
| 80 | Línea en blanco de separación. |
| 81 | Ejecuta `self._items.extend(items)`. |
| 82 | Ejecuta `self._total_processed += len(items)`. |
| 83 | Línea en blanco de separación. |
| 84 | Declara `def _put_scalar_or_list(self, data: Any) -> None:`. |
| 85 | Docstring: `""" Store one value or every value from a list as strings """`. |
| 86 | Línea en blanco de separación. |
| 87 | Comprueba `isinstance(data, list)`. |
| 88 | Ejecuta `self._put_items([str(item) for item in data])`. |
| 89 | Devuelve desde la función. |
| 90 | Ejecuta `self._put_item(str(data))`. |
| 91 | Línea en blanco de separación. |
| 92 | Línea en blanco de separación. |
| 93 | Declara `class NumericProcessor(DataProcessor):`. |
| 94 | Docstring: `""" Process numeric values and lists of numeric values """`. |
| 95 | Línea en blanco de separación. |
| 96 | Declara `def __init__(self) -> None:`. |
| 97 | Ejecuta `super().__init__("Numeric Processor")`. |
| 98 | Línea en blanco de separación. |
| 99 | Declara `def validate(self, data: Any) -> bool:`. |
| 100 | Docstring: `""" Return whether data is numeric or a numeric list """`. |
| 101 | Línea en blanco de separación. |
| 102 | Comprueba `isinstance(data, list)`. |
| 103 | Devuelve `all(self._is_numeric(item) for item in data)`. |
| 104 | Devuelve `self._is_numeric(data)`. |
| 105 | Línea en blanco de separación. |
| 106 | Declara `def ingest(self, data: NumericData) -> None:`. |
| 107 | Docstring: `""" Ingest numeric data as separated string items """`. |
| 108 | Línea en blanco de separación. |
| 109 | Comprueba `not self.validate(data)`. |
| 110 | Lanza `ValueError("Improper numeric data")`. |
| 111 | Línea en blanco de separación. |
| 112 | Ejecuta `self._put_scalar_or_list(data)`. |
| 113 | Línea en blanco de separación. |
| 114 | Declara `def _is_numeric(self, data: Any) -> bool:`. |
| 115 | Docstring: `""" Return whether data is a non-boolean number """`. |
| 116 | Línea en blanco de separación. |
| 117 | Devuelve `isinstance(data, (int, float)) and not isinstance(data, bool)`. |
| 118 | Línea en blanco de separación. |
| 119 | Línea en blanco de separación. |
| 120 | Declara `class TextProcessor(DataProcessor):`. |
| 121 | Docstring: `""" Process text values and lists of text values """`. |
| 122 | Línea en blanco de separación. |
| 123 | Declara `def __init__(self) -> None:`. |
| 124 | Ejecuta `super().__init__("Text Processor")`. |
| 125 | Línea en blanco de separación. |
| 126 | Declara `def validate(self, data: Any) -> bool:`. |
| 127 | Docstring: `""" Return whether data is text or a text list """`. |
| 128 | Línea en blanco de separación. |
| 129 | Comprueba `isinstance(data, str)`. |
| 130 | Devuelve `True`. |
| 131 | Comprueba `isinstance(data, list)`. |
| 132 | Devuelve `all(isinstance(item, str) for item in data)`. |
| 133 | Devuelve `False`. |
| 134 | Línea en blanco de separación. |
| 135 | Declara `def ingest(self, data: TextData) -> None:`. |
| 136 | Docstring: `""" Ingest text data as separated string items """`. |
| 137 | Línea en blanco de separación. |
| 138 | Comprueba `not self.validate(data)`. |
| 139 | Lanza `ValueError("Improper text data")`. |
| 140 | Línea en blanco de separación. |
| 141 | Ejecuta `self._put_scalar_or_list(data)`. |
| 142 | Línea en blanco de separación. |
| 143 | Línea en blanco de separación. |
| 144 | Declara `class LogProcessor(DataProcessor):`. |
| 145 | Docstring: `""" Process log dictionaries and lists of log dictionaries """`. |
| 146 | Línea en blanco de separación. |
| 147 | Declara `def __init__(self) -> None:`. |
| 148 | Ejecuta `super().__init__("Log Processor")`. |
| 149 | Línea en blanco de separación. |
| 150 | Declara `def validate(self, data: Any) -> bool:`. |
| 151 | Docstring: `""" Return whether data is a valid log entry or list """`. |
| 152 | Línea en blanco de separación. |
| 153 | Comprueba `isinstance(data, dict)`. |
| 154 | Devuelve `self._is_log_entry(data)`. |
| 155 | Comprueba `isinstance(data, list)`. |
| 156 | Devuelve `all(self._is_log_entry(item) for item in data)`. |
| 157 | Devuelve `False`. |
| 158 | Línea en blanco de separación. |
| 159 | Declara `def ingest(self, data: LogData) -> None:`. |
| 160 | Docstring: `""" Ingest log data as separated formatted strings """`. |
| 161 | Línea en blanco de separación. |
| 162 | Comprueba `not self.validate(data)`. |
| 163 | Lanza `ValueError("Improper log data")`. |
| 164 | Línea en blanco de separación. |
| 165 | Comprueba `isinstance(data, list)`. |
| 166 | Ejecuta `self._put_items([self._format_log_entry(item) for item in data])`. |
| 167 | Devuelve desde la función. |
| 168 | Ejecuta `self._put_item(self._format_log_entry(data))`. |
| 169 | Línea en blanco de separación. |
| 170 | Declara `def _is_log_entry(self, data: Any) -> bool:`. |
| 171 | Docstring: `""" Return whether data is a dictionary with string pairs """`. |
| 172 | Línea en blanco de separación. |
| 173 | Devuelve `isinstance(data, dict) and all(`. |
| 174 | Ejecuta `isinstance(key, str) and isinstance(value, str)`. |
| 175 | Recorre `key, value in data.items()`. |
| 176 | Cierra una estructura o llamada multilínea. |
| 177 | Línea en blanco de separación. |
| 178 | Declara `def _format_log_entry(self, entry: LogEntry) -> str:`. |
| 179 | Docstring: `""" Convert a log entry into the expected output format """`. |
| 180 | Línea en blanco de separación. |
| 181 | Ejecuta `level = entry.get("log_level", "")`. |
| 182 | Ejecuta `message = entry.get("log_message", "")`. |
| 183 | Comprueba `level or message`. |
| 184 | Devuelve `f"{level}: {message}"`. |
| 185 | Devuelve `str(entry)`. |
| 186 | Línea en blanco de separación. |
| 187 | Línea en blanco de separación. |
| 188 | Declara `class DataStream:`. |
| 189 | Docstring: `""" Route stream elements to registered data processors """`. |
| 190 | Línea en blanco de separación. |
| 191 | Declara `def __init__(self) -> None:`. |
| 192 | Ejecuta `self._processors: list[DataProcessor] = []`. |
| 193 | Línea en blanco de separación. |
| 194 | Declara `def get_processors(self) -> list[DataProcessor]:`. |
| 195 | Docstring: `""" Return registered processors """`. |
| 196 | Línea en blanco de separación. |
| 197 | Devuelve `self._processors`. |
| 198 | Línea en blanco de separación. |
| 199 | Declara `def register_processor(self, proc: DataProcessor) -> None:`. |
| 200 | Docstring: `""" Register a data processor for future stream processing """`. |
| 201 | Línea en blanco de separación. |
| 202 | Ejecuta `self._processors.append(proc)`. |
| 203 | Línea en blanco de separación. |
| 204 | Declara `def process_stream(self, stream: list[Any]) -> None:`. |
| 205 | Docstring: `""" Send each stream element to the first compatible processor """`. |
| 206 | Línea en blanco de separación. |
| 207 | Recorre `element in stream`. |
| 208 | Comprueba `not self._put_element(element)`. |
| 209 | Imprime `print(`. |
| 210 | Ejecuta `"DataStream error - Can't process element in stream: "`. |
| 211 | Ejecuta `f"{element}"`. |
| 212 | Cierra una estructura o llamada multilínea. |
| 213 | Línea en blanco de separación. |
| 214 | Declara `def print_processors_stats(self) -> None:`. |
| 215 | Docstring: `""" Print statistics for every registered processor """`. |
| 216 | Línea en blanco de separación. |
| 217 | Imprime `print("== DataStream statistics ==")`. |
| 218 | Comprueba `not self._processors`. |
| 219 | Imprime `print("No processor found, no data")`. |
| 220 | Devuelve desde la función. |
| 221 | Línea en blanco de separación. |
| 222 | Recorre `processor in self._processors`. |
| 223 | Imprime `print(`. |
| 224 | Ejecuta `f"{processor.get_name()}: total "`. |
| 225 | Ejecuta `f"{processor.get_total_processed()} items processed, "`. |
| 226 | Ejecuta `f"remaining {processor.get_data_len()} on processor"`. |
| 227 | Cierra una estructura o llamada multilínea. |
| 228 | Línea en blanco de separación. |
| 229 | Declara `def _put_element(self, element: Any) -> bool:`. |
| 230 | Docstring: `""" Return whether an element was sent to a processor """`. |
| 231 | Línea en blanco de separación. |
| 232 | Recorre `processor in self._processors`. |
| 233 | Comentario: `Polymorphism: DataStream uses the DataProcessor interface only.`. |
| 234 | Comprueba `processor.validate(element)`. |
| 235 | Ejecuta `processor.ingest(element)`. |
| 236 | Devuelve `True`. |
| 237 | Devuelve `False`. |
| 238 | Línea en blanco de separación. |
| 239 | Línea en blanco de separación. |
| 240 | Declara `def put_processor_outputs(processor: DataProcessor, amount: int) -> None:`. |
| 241 | Docstring: `""" Consume a fixed number of values from a processor """`. |
| 242 | Línea en blanco de separación. |
| 243 | Recorre `_ in range(amount)`. |
| 244 | Ejecuta `processor.output()`. |
| 245 | Línea en blanco de separación. |
| 246 | Línea en blanco de separación. |
| 247 | Declara `def build_log_entry(level: str, message: str) -> LogEntry:`. |
| 248 | Docstring: `""" Build one log entry from dynamic values """`. |
| 249 | Línea en blanco de separación. |
| 250 | Devuelve `{`. |
| 251 | Continúa con `"log_level": level,`. |
| 252 | Continúa con `"log_message": message,`. |
| 253 | Cierra una estructura o llamada multilínea. |
| 254 | Línea en blanco de separación. |
| 255 | Línea en blanco de separación. |
| 256 | Declara `def build_stream(*items: Any) -> list[Any]:`. |
| 257 | Docstring: `""" Build a stream from received items """`. |
| 258 | Línea en blanco de separación. |
| 259 | Devuelve `list(items)`. |
| 260 | Línea en blanco de separación. |
| 261 | Línea en blanco de separación. |
| 262 | Declara `def main() -> None:`. |
| 263 | Docstring: `""" Run the script entrypoint """`. |
| 264 | Línea en blanco de separación. |
| 265 | Continúa con `stream = build_stream(`. |
| 266 | Continúa con `TXT_VAL,`. |
| 267 | Continúa con `NUM_DATA,`. |
| 268 | Abre `[`. |
| 269 | Continúa con `build_log_entry(LOG_WARN_LVL, LOG_WARN_MSG),`. |
| 270 | Continúa con `build_log_entry(LOG_INFO_LVL, LOG_INFO_MSG),`. |
| 271 | Cierra una estructura o llamada multilínea. |
| 272 | Continúa con `NUM_VAL,`. |
| 273 | Continúa con `TXT_DATA,`. |
| 274 | Cierra una estructura o llamada multilínea. |
| 275 | Imprime `print("=== Code Nexus - Data Stream ===")`. |
| 276 | Imprime `print()`. |
| 277 | Imprime `print("Initialize Data Stream...")`. |
| 278 | Ejecuta `data_stream = DataStream()`. |
| 279 | Ejecuta `data_stream.print_processors_stats()`. |
| 280 | Línea en blanco de separación. |
| 281 | Ejecuta `numeric_processor = NumericProcessor()`. |
| 282 | Imprime `print("Registering Numeric Processor")`. |
| 283 | Ejecuta `data_stream.register_processor(numeric_processor)`. |
| 284 | Imprime `print(f"Send first batch of data on stream: {stream}")`. |
| 285 | Ejecuta `data_stream.process_stream(stream)`. |
| 286 | Ejecuta `data_stream.print_processors_stats()`. |
| 287 | Línea en blanco de separación. |
| 288 | Ejecuta `text_processor = TextProcessor()`. |
| 289 | Ejecuta `log_processor = LogProcessor()`. |
| 290 | Imprime `print("Registering other data processors")`. |
| 291 | Imprime `print()`. |
| 292 | Ejecuta `data_stream.register_processor(text_processor)`. |
| 293 | Ejecuta `data_stream.register_processor(log_processor)`. |
| 294 | Imprime `print("Send the same batch again")`. |
| 295 | Ejecuta `data_stream.process_stream(stream)`. |
| 296 | Ejecuta `data_stream.print_processors_stats()`. |
| 297 | Línea en blanco de separación. |
| 298 | Imprime `print(`. |
| 299 | Ejecuta `"Consume some elements from the data processors: "`. |
| 300 | Ejecuta `f"Numeric {NUM_OUT_NB}, "`. |
| 301 | Ejecuta `f"Text {TXT_OUT_NB}, "`. |
| 302 | Ejecuta `f"Log {LOG_OUT_NB}"`. |
| 303 | Cierra una estructura o llamada multilínea. |
| 304 | Ejecuta `put_processor_outputs(numeric_processor, NUM_OUT_NB)`. |
| 305 | Ejecuta `put_processor_outputs(text_processor, TXT_OUT_NB)`. |
| 306 | Ejecuta `put_processor_outputs(log_processor, LOG_OUT_NB)`. |
| 307 | Ejecuta `data_stream.print_processors_stats()`. |
| 308 | Línea en blanco de separación. |
| 309 | Línea en blanco de separación. |
| 310 | Comprueba `__name__ == "__main__"`. |
| 311 | Ejecuta `main()`. |
