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
| 7 | Asigna `int \| float \| list[int \| float]` a `NumericData`. |
| 8 | Asigna `str \| list[str]` a `TextData`. |
| 9 | Asigna `dict[str, str]` a `LogEntry`. |
| 10 | Asigna `LogEntry \| list[LogEntry]` a `LogData`. |
| 11 | Línea en blanco de separación. |
| 12 | Asigna `"Hello world"` a `TXT_VAL`. |
| 13 | Asigna `[3.14, -1, 2.71]` a `NUM_DATA`. |
| 14 | Línea en blanco de separación. |
| 15 | Asigna `"WARNING"` a `LOG_WARN_LVL`. |
| 16 | Asigna `"Telnet access! Use ssh instead"` a `LOG_WARN_MSG`. |
| 17 | Asigna `"INFO"` a `LOG_INFO_LVL`. |
| 18 | Asigna `"User wil is connected"` a `LOG_INFO_MSG`. |
| 19 | Línea en blanco de separación. |
| 20 | Asigna `42` a `NUM_VAL`. |
| 21 | Asigna `["Hi", "five"]` a `TXT_DATA`. |
| 22 | Línea en blanco de separación. |
| 23 | Asigna `3` a `NUM_OUT_NB`. |
| 24 | Asigna `2` a `TXT_OUT_NB`. |
| 25 | Asigna `1` a `LOG_OUT_NB`. |
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
| 66 | Asigna `self._next_output_rank` a `rank`. |
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
| 97 | Docstring: `""" Initialize a numeric processor """`. |
| 98 | Línea en blanco de separación. |
| 99 | Ejecuta `super().__init__("Numeric Processor")`. |
| 100 | Línea en blanco de separación. |
| 101 | Declara `def validate(self, data: Any) -> bool:`. |
| 102 | Docstring: `""" Return whether data is numeric or a numeric list """`. |
| 103 | Línea en blanco de separación. |
| 104 | Comprueba `isinstance(data, list)`. |
| 105 | Devuelve `all(self._is_numeric(item) for item in data)`. |
| 106 | Devuelve `self._is_numeric(data)`. |
| 107 | Línea en blanco de separación. |
| 108 | Declara `def ingest(self, data: NumericData) -> None:`. |
| 109 | Docstring: `""" Ingest numeric data as separated string items """`. |
| 110 | Línea en blanco de separación. |
| 111 | Comprueba `not self.validate(data)`. |
| 112 | Lanza `ValueError("Improper numeric data")`. |
| 113 | Línea en blanco de separación. |
| 114 | Ejecuta `self._put_scalar_or_list(data)`. |
| 115 | Línea en blanco de separación. |
| 116 | Declara `def _is_numeric(self, data: Any) -> bool:`. |
| 117 | Docstring: `""" Return whether data is a non-boolean number """`. |
| 118 | Línea en blanco de separación. |
| 119 | Devuelve `isinstance(data, (int, float)) and not isinstance(data, bool)`. |
| 120 | Línea en blanco de separación. |
| 121 | Línea en blanco de separación. |
| 122 | Declara `class TextProcessor(DataProcessor):`. |
| 123 | Docstring: `""" Process text values and lists of text values """`. |
| 124 | Línea en blanco de separación. |
| 125 | Declara `def __init__(self) -> None:`. |
| 126 | Docstring: `""" Initialize a text processor """`. |
| 127 | Línea en blanco de separación. |
| 128 | Ejecuta `super().__init__("Text Processor")`. |
| 129 | Línea en blanco de separación. |
| 130 | Declara `def validate(self, data: Any) -> bool:`. |
| 131 | Docstring: `""" Return whether data is text or a text list """`. |
| 132 | Línea en blanco de separación. |
| 133 | Comprueba `isinstance(data, str)`. |
| 134 | Devuelve `True`. |
| 135 | Comprueba `isinstance(data, list)`. |
| 136 | Devuelve `all(isinstance(item, str) for item in data)`. |
| 137 | Devuelve `False`. |
| 138 | Línea en blanco de separación. |
| 139 | Declara `def ingest(self, data: TextData) -> None:`. |
| 140 | Docstring: `""" Ingest text data as separated string items """`. |
| 141 | Línea en blanco de separación. |
| 142 | Comprueba `not self.validate(data)`. |
| 143 | Lanza `ValueError("Improper text data")`. |
| 144 | Línea en blanco de separación. |
| 145 | Ejecuta `self._put_scalar_or_list(data)`. |
| 146 | Línea en blanco de separación. |
| 147 | Línea en blanco de separación. |
| 148 | Declara `class LogProcessor(DataProcessor):`. |
| 149 | Docstring: `""" Process log dictionaries and lists of log dictionaries """`. |
| 150 | Línea en blanco de separación. |
| 151 | Declara `def __init__(self) -> None:`. |
| 152 | Docstring: `""" Initialize a log processor """`. |
| 153 | Línea en blanco de separación. |
| 154 | Ejecuta `super().__init__("Log Processor")`. |
| 155 | Línea en blanco de separación. |
| 156 | Declara `def validate(self, data: Any) -> bool:`. |
| 157 | Docstring: `""" Return whether data is a valid log entry or list """`. |
| 158 | Línea en blanco de separación. |
| 159 | Comprueba `isinstance(data, dict)`. |
| 160 | Devuelve `self._is_log_entry(data)`. |
| 161 | Comprueba `isinstance(data, list)`. |
| 162 | Devuelve `all(self._is_log_entry(item) for item in data)`. |
| 163 | Devuelve `False`. |
| 164 | Línea en blanco de separación. |
| 165 | Declara `def ingest(self, data: LogData) -> None:`. |
| 166 | Docstring: `""" Ingest log data as separated formatted strings """`. |
| 167 | Línea en blanco de separación. |
| 168 | Comprueba `not self.validate(data)`. |
| 169 | Lanza `ValueError("Improper log data")`. |
| 170 | Línea en blanco de separación. |
| 171 | Comprueba `isinstance(data, list)`. |
| 172 | Ejecuta `self._put_items([self._format_log_entry(item) for item in data])`. |
| 173 | Devuelve desde la función. |
| 174 | Ejecuta `self._put_item(self._format_log_entry(data))`. |
| 175 | Línea en blanco de separación. |
| 176 | Declara `def _is_log_entry(self, data: Any) -> bool:`. |
| 177 | Docstring: `""" Return whether data is a dictionary with string pairs """`. |
| 178 | Línea en blanco de separación. |
| 179 | Devuelve `isinstance(data, dict) and all(`. |
| 180 | Ejecuta `isinstance(key, str) and isinstance(value, str)`. |
| 181 | Recorre `key, value in data.items()`. |
| 182 | Cierra una estructura o llamada multilínea. |
| 183 | Línea en blanco de separación. |
| 184 | Declara `def _format_log_entry(self, entry: LogEntry) -> str:`. |
| 185 | Docstring: `""" Convert a log entry into the expected output format """`. |
| 186 | Línea en blanco de separación. |
| 187 | Ejecuta `level = entry.get("log_level", "")`. |
| 188 | Ejecuta `message = entry.get("log_message", "")`. |
| 189 | Comprueba `level or message`. |
| 190 | Devuelve `f"{level}: {message}"`. |
| 191 | Devuelve `str(entry)`. |
| 192 | Línea en blanco de separación. |
| 193 | Línea en blanco de separación. |
| 194 | Declara `class DataStream:`. |
| 195 | Docstring: `""" Route stream elements to registered data processors """`. |
| 196 | Línea en blanco de separación. |
| 197 | Declara `def __init__(self) -> None:`. |
| 198 | Docstring: `""" Initialize an empty data stream """`. |
| 199 | Línea en blanco de separación. |
| 200 | Ejecuta `self._processors: list[DataProcessor] = []`. |
| 201 | Línea en blanco de separación. |
| 202 | Declara `def get_processors(self) -> list[DataProcessor]:`. |
| 203 | Docstring: `""" Return registered processors """`. |
| 204 | Línea en blanco de separación. |
| 205 | Devuelve `self._processors`. |
| 206 | Línea en blanco de separación. |
| 207 | Declara `def register_processor(self, proc: DataProcessor) -> None:`. |
| 208 | Docstring: `""" Register a data processor for future stream processing """`. |
| 209 | Línea en blanco de separación. |
| 210 | Ejecuta `self._processors.append(proc)`. |
| 211 | Línea en blanco de separación. |
| 212 | Declara `def process_stream(self, stream: list[Any]) -> None:`. |
| 213 | Docstring: `""" Send each stream element to the first compatible processor """`. |
| 214 | Línea en blanco de separación. |
| 215 | Recorre `element in stream`. |
| 216 | Comprueba `not self._put_element(element)`. |
| 217 | Imprime `print(`. |
| 218 | Continúa con `"DataStream error - Can't process element in stream: "`. |
| 219 | Continúa con `f"{element}"`. |
| 220 | Cierra una estructura o llamada multilínea. |
| 221 | Línea en blanco de separación. |
| 222 | Declara `def print_processors_stats(self) -> None:`. |
| 223 | Docstring: `""" Print statistics for every registered processor """`. |
| 224 | Línea en blanco de separación. |
| 225 | Imprime `print("== DataStream statistics ==")`. |
| 226 | Comprueba `not self._processors`. |
| 227 | Imprime `print("No processor found, no data")`. |
| 228 | Devuelve desde la función. |
| 229 | Línea en blanco de separación. |
| 230 | Recorre `processor in self._processors`. |
| 231 | Imprime `print(`. |
| 232 | Continúa con `f"{processor.get_name()}: total "`. |
| 233 | Continúa con `f"{processor.get_total_processed()} items processed, "`. |
| 234 | Continúa con `f"remaining {processor.get_data_len()} on processor"`. |
| 235 | Cierra una estructura o llamada multilínea. |
| 236 | Línea en blanco de separación. |
| 237 | Declara `def _put_element(self, element: Any) -> bool:`. |
| 238 | Docstring: `""" Return whether an element was sent to a processor """`. |
| 239 | Línea en blanco de separación. |
| 240 | Recorre `processor in self._processors`. |
| 241 | Comentario: `Polymorphism: DataStream uses the DataProcessor interface only.`. |
| 242 | Comprueba `processor.validate(element)`. |
| 243 | Ejecuta `processor.ingest(element)`. |
| 244 | Devuelve `True`. |
| 245 | Devuelve `False`. |
| 246 | Línea en blanco de separación. |
| 247 | Línea en blanco de separación. |
| 248 | Declara `def put_processor_outputs(processor: DataProcessor, amount: int) -> None:`. |
| 249 | Docstring: `""" Consume a fixed number of values from a processor """`. |
| 250 | Línea en blanco de separación. |
| 251 | Recorre `_ in range(amount)`. |
| 252 | Ejecuta `processor.output()`. |
| 253 | Línea en blanco de separación. |
| 254 | Línea en blanco de separación. |
| 255 | Declara `def build_log_entry(level: str, message: str) -> LogEntry:`. |
| 256 | Docstring: `""" Build one log entry from dynamic values """`. |
| 257 | Línea en blanco de separación. |
| 258 | Devuelve `{`. |
| 259 | Continúa con `"log_level": level,`. |
| 260 | Continúa con `"log_message": message,`. |
| 261 | Cierra una estructura o llamada multilínea. |
| 262 | Línea en blanco de separación. |
| 263 | Línea en blanco de separación. |
| 264 | Declara `def build_stream(*items: Any) -> list[Any]:`. |
| 265 | Docstring: `""" Build a stream from received items """`. |
| 266 | Línea en blanco de separación. |
| 267 | Devuelve `list(items)`. |
| 268 | Línea en blanco de separación. |
| 269 | Línea en blanco de separación. |
| 270 | Declara `def run_demo(`. |
| 271 | Continúa con `stream: list[Any],`. |
| 272 | Continúa con `numeric_output_amount: int,`. |
| 273 | Continúa con `text_output_amount: int,`. |
| 274 | Continúa con `log_output_amount: int,`. |
| 275 | Cierra una estructura o llamada multilínea. |
| 276 | Docstring: `""" Run the data stream demonstration scenario """`. |
| 277 | Línea en blanco de separación. |
| 278 | Imprime `print("=== Code Nexus - Data Stream ===")`. |
| 279 | Imprime `print()`. |
| 280 | Imprime `print("Initialize Data Stream...")`. |
| 281 | Ejecuta `data_stream = DataStream()`. |
| 282 | Ejecuta `data_stream.print_processors_stats()`. |
| 283 | Línea en blanco de separación. |
| 284 | Ejecuta `numeric_processor = NumericProcessor()`. |
| 285 | Imprime `print("Registering Numeric Processor")`. |
| 286 | Ejecuta `data_stream.register_processor(numeric_processor)`. |
| 287 | Imprime `print(f"Send first batch of data on stream: {stream}")`. |
| 288 | Ejecuta `data_stream.process_stream(stream)`. |
| 289 | Ejecuta `data_stream.print_processors_stats()`. |
| 290 | Línea en blanco de separación. |
| 291 | Ejecuta `text_processor = TextProcessor()`. |
| 292 | Ejecuta `log_processor = LogProcessor()`. |
| 293 | Imprime `print("Registering other data processors")`. |
| 294 | Imprime `print()`. |
| 295 | Ejecuta `data_stream.register_processor(text_processor)`. |
| 296 | Ejecuta `data_stream.register_processor(log_processor)`. |
| 297 | Imprime `print("Send the same batch again")`. |
| 298 | Ejecuta `data_stream.process_stream(stream)`. |
| 299 | Ejecuta `data_stream.print_processors_stats()`. |
| 300 | Línea en blanco de separación. |
| 301 | Imprime `print(`. |
| 302 | Continúa con `"Consume some elements from the data processors: "`. |
| 303 | Continúa con `f"Numeric {numeric_output_amount}, "`. |
| 304 | Continúa con `f"Text {text_output_amount}, "`. |
| 305 | Continúa con `f"Log {log_output_amount}"`. |
| 306 | Cierra una estructura o llamada multilínea. |
| 307 | Ejecuta `put_processor_outputs(numeric_processor, numeric_output_amount)`. |
| 308 | Ejecuta `put_processor_outputs(text_processor, text_output_amount)`. |
| 309 | Ejecuta `put_processor_outputs(log_processor, log_output_amount)`. |
| 310 | Ejecuta `data_stream.print_processors_stats()`. |
| 311 | Línea en blanco de separación. |
| 312 | Línea en blanco de separación. |
| 313 | Declara `def main() -> None:`. |
| 314 | Docstring: `""" Run the script entrypoint """`. |
| 315 | Línea en blanco de separación. |
| 316 | Asigna `build_stream(` a `stream`. |
| 317 | Continúa con `TXT_VAL,`. |
| 318 | Continúa con `NUM_DATA,`. |
| 319 | Continúa con `[`. |
| 320 | Continúa con `build_log_entry(LOG_WARN_LVL, LOG_WARN_MSG),`. |
| 321 | Continúa con `build_log_entry(LOG_INFO_LVL, LOG_INFO_MSG),`. |
| 322 | Cierra una estructura o llamada multilínea. |
| 323 | Continúa con `NUM_VAL,`. |
| 324 | Continúa con `TXT_DATA,`. |
| 325 | Cierra una estructura o llamada multilínea. |
| 326 | Ejecuta `run_demo(stream, NUM_OUT_NB, TXT_OUT_NB, LOG_OUT_NB)`. |
| 327 | Línea en blanco de separación. |
| 328 | Línea en blanco de separación. |
| 329 | Comprueba `__name__ == "__main__"`. |
| 330 | Ejecuta `main()`. |
