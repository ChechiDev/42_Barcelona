# M05 ex2: explicación línea por línea

Este documento vincula cada línea de `ex2/data_pipeline.py` con lo que hace.

| Línea | Qué hace |
| --- | --- |
| 1 | Indica al sistema que ejecute el archivo con `python3`. |
| 2 | Línea en blanco de separación. |
| 3 | Importa `abc import ABC, abstractmethod`. |
| 4 | Importa `typing import Any, Protocol`. |
| 5 | Línea en blanco de separación. |
| 6 | Línea en blanco de separación. |
| 7 | Ejecuta `NumericData = int \| float \| list[int \| float]`. |
| 8 | Ejecuta `TextData = str \| list[str]`. |
| 9 | Ejecuta `LogEntry = dict[str, str]`. |
| 10 | Ejecuta `LogData = LogEntry \| list[LogEntry]`. |
| 11 | Ejecuta `OutputData = list[tuple[int, str]]`. |
| 12 | Línea en blanco de separación. |
| 13 | Ejecuta `TXT_VAL = "Hello world"`. |
| 14 | Ejecuta `NUM_DATA = [3.14, -1, 2.71]`. |
| 15 | Línea en blanco de separación. |
| 16 | Ejecuta `LOG_WARN_LVL = "WARNING"`. |
| 17 | Ejecuta `LOG_WARN_MSG = "Telnet access! Use ssh instead"`. |
| 18 | Ejecuta `LOG_INFO_LVL = "INFO"`. |
| 19 | Ejecuta `LOG_INFO_MSG = "User wil is connected"`. |
| 20 | Línea en blanco de separación. |
| 21 | Ejecuta `NUM_VAL = 42`. |
| 22 | Ejecuta `TXT_DATA = ["Hi", "five"]`. |
| 23 | Línea en blanco de separación. |
| 24 | Ejecuta `CSV_OUT_NB = 3`. |
| 25 | Línea en blanco de separación. |
| 26 | Ejecuta `NUM_VAL_2 = 21`. |
| 27 | Ejecuta `TXT_DATA_2 = ["I love AI", "LLMs are wonderful", "Stay healthy"]`. |
| 28 | Ejecuta `LOG_ERR_LVL = "ERROR"`. |
| 29 | Ejecuta `LOG_ERR_MSG = "500 server crash"`. |
| 30 | Ejecuta `LOG_NOTICE_LVL = "NOTICE"`. |
| 31 | Ejecuta `LOG_NOTICE_MSG = "Certificate expires in 10 days"`. |
| 32 | Ejecuta `NUM_DATA_2 = [32, 42, 64, 84, 128, 168]`. |
| 33 | Ejecuta `TXT_VAL_2 = "World hello"`. |
| 34 | Línea en blanco de separación. |
| 35 | Ejecuta `JSON_OUT_NB = 5`. |
| 36 | Línea en blanco de separación. |
| 37 | Línea en blanco de separación. |
| 38 | Declara `class ExportPlugin(Protocol):`. |
| 39 | Docstring: `""" Define the output plugin protocol """`. |
| 40 | Línea en blanco de separación. |
| 41 | Declara `def process_output(self, data: OutputData) -> None:`. |
| 42 | Docstring: `""" Process output data from one processor """`. |
| 43 | Línea en blanco de separación. |
| 44 | Línea en blanco de separación. |
| 45 | Declara `class DataProcessor(ABC):`. |
| 46 | Docstring: `""" Define the common interface for all data processors """`. |
| 47 | Línea en blanco de separación. |
| 48 | Declara `def __init__(self, name: str) -> None:`. |
| 49 | Ejecuta `self._name = name`. |
| 50 | Ejecuta `self._items: list[str] = []`. |
| 51 | Ejecuta `self._next_output_rank = 0`. |
| 52 | Ejecuta `self._total_processed = 0`. |
| 53 | Línea en blanco de separación. |
| 54 | Declara `def get_name(self) -> str:`. |
| 55 | Docstring: `""" Return the processor display name """`. |
| 56 | Línea en blanco de separación. |
| 57 | Devuelve `self._name`. |
| 58 | Línea en blanco de separación. |
| 59 | Declara `def get_data_len(self) -> int:`. |
| 60 | Docstring: `""" Return the number of items waiting on the processor """`. |
| 61 | Línea en blanco de separación. |
| 62 | Devuelve `len(self._items)`. |
| 63 | Línea en blanco de separación. |
| 64 | Declara `def get_total_processed(self) -> int:`. |
| 65 | Docstring: `""" Return the total number of ingested items """`. |
| 66 | Línea en blanco de separación. |
| 67 | Devuelve `self._total_processed`. |
| 68 | Línea en blanco de separación. |
| 69 | Aplica el decorador `@abstractmethod`. |
| 70 | Declara `def validate(self, data: Any) -> bool:`. |
| 71 | Docstring: `""" Return whether data can be ingested by this processor """`. |
| 72 | Línea en blanco de separación. |
| 73 | Aplica el decorador `@abstractmethod`. |
| 74 | Declara `def ingest(self, data: Any) -> None:`. |
| 75 | Docstring: `""" Ingest valid data into this processor """`. |
| 76 | Línea en blanco de separación. |
| 77 | Declara `def output(self) -> tuple[int, str]:`. |
| 78 | Docstring: `""" Extract and return the oldest stored item with its rank """`. |
| 79 | Línea en blanco de separación. |
| 80 | Comprueba `not self._items`. |
| 81 | Lanza `IndexError("No data to output")`. |
| 82 | Línea en blanco de separación. |
| 83 | Ejecuta `rank = self._next_output_rank`. |
| 84 | Ejecuta `item = self._items.pop(0)`. |
| 85 | Ejecuta `self._next_output_rank += 1`. |
| 86 | Línea en blanco de separación. |
| 87 | Devuelve `rank, item`. |
| 88 | Línea en blanco de separación. |
| 89 | Declara `def _put_item(self, item: str) -> None:`. |
| 90 | Docstring: `""" Store one processed item and update statistics """`. |
| 91 | Línea en blanco de separación. |
| 92 | Ejecuta `self._items.append(item)`. |
| 93 | Ejecuta `self._total_processed += 1`. |
| 94 | Línea en blanco de separación. |
| 95 | Declara `def _put_items(self, items: list[str]) -> None:`. |
| 96 | Docstring: `""" Store several processed items and update statistics """`. |
| 97 | Línea en blanco de separación. |
| 98 | Ejecuta `self._items.extend(items)`. |
| 99 | Ejecuta `self._total_processed += len(items)`. |
| 100 | Línea en blanco de separación. |
| 101 | Declara `def _put_scalar_or_list(self, data: Any) -> None:`. |
| 102 | Docstring: `""" Store one value or every value from a list as strings """`. |
| 103 | Línea en blanco de separación. |
| 104 | Comprueba `isinstance(data, list)`. |
| 105 | Ejecuta `self._put_items([str(item) for item in data])`. |
| 106 | Termina la función y devuelve `None` implícitamente. |
| 107 | Ejecuta `self._put_item(str(data))`. |
| 108 | Línea en blanco de separación. |
| 109 | Línea en blanco de separación. |
| 110 | Declara `class NumericProcessor(DataProcessor):`. |
| 111 | Docstring: `""" Process numeric values and lists of numeric values """`. |
| 112 | Línea en blanco de separación. |
| 113 | Declara `def __init__(self) -> None:`. |
| 114 | Ejecuta `super().__init__("Numeric Processor")`. |
| 115 | Línea en blanco de separación. |
| 116 | Declara `def validate(self, data: Any) -> bool:`. |
| 117 | Docstring: `""" Return whether data is numeric or a numeric list """`. |
| 118 | Línea en blanco de separación. |
| 119 | Comprueba `isinstance(data, list)`. |
| 120 | Devuelve `all(self._is_numeric(item) for item in data)`. |
| 121 | Devuelve `self._is_numeric(data)`. |
| 122 | Línea en blanco de separación. |
| 123 | Declara `def ingest(self, data: NumericData) -> None:`. |
| 124 | Docstring: `""" Ingest numeric data as separated string items """`. |
| 125 | Línea en blanco de separación. |
| 126 | Comprueba `not self.validate(data)`. |
| 127 | Lanza `ValueError("Improper numeric data")`. |
| 128 | Línea en blanco de separación. |
| 129 | Ejecuta `self._put_scalar_or_list(data)`. |
| 130 | Línea en blanco de separación. |
| 131 | Declara `def _is_numeric(self, data: Any) -> bool:`. |
| 132 | Docstring: `""" Return whether data is a non-boolean number """`. |
| 133 | Línea en blanco de separación. |
| 134 | Devuelve `isinstance(data, (int, float)) and not isinstance(data, bool)`. |
| 135 | Línea en blanco de separación. |
| 136 | Línea en blanco de separación. |
| 137 | Declara `class TextProcessor(DataProcessor):`. |
| 138 | Docstring: `""" Process text values and lists of text values """`. |
| 139 | Línea en blanco de separación. |
| 140 | Declara `def __init__(self) -> None:`. |
| 141 | Ejecuta `super().__init__("Text Processor")`. |
| 142 | Línea en blanco de separación. |
| 143 | Declara `def validate(self, data: Any) -> bool:`. |
| 144 | Docstring: `""" Return whether data is text or a text list """`. |
| 145 | Línea en blanco de separación. |
| 146 | Comprueba `isinstance(data, str)`. |
| 147 | Devuelve `True`. |
| 148 | Comprueba `isinstance(data, list)`. |
| 149 | Devuelve `all(isinstance(item, str) for item in data)`. |
| 150 | Devuelve `False`. |
| 151 | Línea en blanco de separación. |
| 152 | Declara `def ingest(self, data: TextData) -> None:`. |
| 153 | Docstring: `""" Ingest text data as separated string items """`. |
| 154 | Línea en blanco de separación. |
| 155 | Comprueba `not self.validate(data)`. |
| 156 | Lanza `ValueError("Improper text data")`. |
| 157 | Línea en blanco de separación. |
| 158 | Ejecuta `self._put_scalar_or_list(data)`. |
| 159 | Línea en blanco de separación. |
| 160 | Línea en blanco de separación. |
| 161 | Declara `class LogProcessor(DataProcessor):`. |
| 162 | Docstring: `""" Process log dictionaries and lists of log dictionaries """`. |
| 163 | Línea en blanco de separación. |
| 164 | Declara `def __init__(self) -> None:`. |
| 165 | Ejecuta `super().__init__("Log Processor")`. |
| 166 | Línea en blanco de separación. |
| 167 | Declara `def validate(self, data: Any) -> bool:`. |
| 168 | Docstring: `""" Return whether data is a valid log entry or list """`. |
| 169 | Línea en blanco de separación. |
| 170 | Comprueba `isinstance(data, dict)`. |
| 171 | Devuelve `self._is_log_entry(data)`. |
| 172 | Comprueba `isinstance(data, list)`. |
| 173 | Devuelve `all(self._is_log_entry(item) for item in data)`. |
| 174 | Devuelve `False`. |
| 175 | Línea en blanco de separación. |
| 176 | Declara `def ingest(self, data: LogData) -> None:`. |
| 177 | Docstring: `""" Ingest log data as separated formatted strings """`. |
| 178 | Línea en blanco de separación. |
| 179 | Comprueba `not self.validate(data)`. |
| 180 | Lanza `ValueError("Improper log data")`. |
| 181 | Línea en blanco de separación. |
| 182 | Comprueba `isinstance(data, list)`. |
| 183 | Ejecuta `self._put_items([self._format_log_entry(item) for item in data])`. |
| 184 | Termina la función y devuelve `None` implícitamente. |
| 185 | Ejecuta `self._put_item(self._format_log_entry(data))`. |
| 186 | Línea en blanco de separación. |
| 187 | Declara `def _is_log_entry(self, data: Any) -> bool:`. |
| 188 | Docstring: `""" Return whether data is a dictionary with string pairs """`. |
| 189 | Línea en blanco de separación. |
| 190 | Devuelve `isinstance(data, dict) and all(`. |
| 191 | Ejecuta `isinstance(key, str) and isinstance(value, str)`. |
| 192 | Inicia un bucle sobre `key, value in data.items()`. |
| 193 | Cierra la estructura con `)`. |
| 194 | Línea en blanco de separación. |
| 195 | Declara `def _format_log_entry(self, entry: LogEntry) -> str:`. |
| 196 | Docstring: `""" Convert a log entry into the expected output format """`. |
| 197 | Línea en blanco de separación. |
| 198 | Ejecuta `level = entry.get("log_level", "")`. |
| 199 | Ejecuta `message = entry.get("log_message", "")`. |
| 200 | Comprueba `level or message`. |
| 201 | Devuelve `f"{level}: {message}"`. |
| 202 | Devuelve `str(entry)`. |
| 203 | Línea en blanco de separación. |
| 204 | Línea en blanco de separación. |
| 205 | Declara `class DataStream:`. |
| 206 | Docstring: `""" Route stream elements and export processor output """`. |
| 207 | Línea en blanco de separación. |
| 208 | Declara `def __init__(self) -> None:`. |
| 209 | Ejecuta `self._processors: list[DataProcessor] = []`. |
| 210 | Línea en blanco de separación. |
| 211 | Declara `def get_processors(self) -> list[DataProcessor]:`. |
| 212 | Docstring: `""" Return registered processors """`. |
| 213 | Línea en blanco de separación. |
| 214 | Devuelve `self._processors`. |
| 215 | Línea en blanco de separación. |
| 216 | Declara `def register_processor(self, proc: DataProcessor) -> None:`. |
| 217 | Docstring: `""" Register a data processor for future stream processing """`. |
| 218 | Línea en blanco de separación. |
| 219 | Ejecuta `self._processors.append(proc)`. |
| 220 | Línea en blanco de separación. |
| 221 | Declara `def process_stream(self, stream: list[Any]) -> None:`. |
| 222 | Docstring: `""" Send each stream element to the first compatible processor """`. |
| 223 | Línea en blanco de separación. |
| 224 | Inicia un bucle sobre `element in stream`. |
| 225 | Comprueba `not self._put_element(element)`. |
| 226 | Ejecuta `print(`. |
| 227 | Ejecuta `"DataStream error - Can't process element in stream: "`. |
| 228 | Ejecuta `f"{element}"`. |
| 229 | Cierra la estructura con `)`. |
| 230 | Línea en blanco de separación. |
| 231 | Declara `def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:`. |
| 232 | Docstring: `""" Export up to nb outputs from every registered processor """`. |
| 233 | Línea en blanco de separación. |
| 234 | Inicia un bucle sobre `processor in self._processors`. |
| 235 | Ejecuta `output_data = self._get_processor_outputs(processor, nb)`. |
| 236 | Ejecuta `plugin.process_output(output_data)`. |
| 237 | Línea en blanco de separación. |
| 238 | Declara `def print_processors_stats(self) -> None:`. |
| 239 | Docstring: `""" Print statistics for every registered processor """`. |
| 240 | Línea en blanco de separación. |
| 241 | Ejecuta `print("== DataStream statistics ==")`. |
| 242 | Comprueba `not self._processors`. |
| 243 | Ejecuta `print("No processor found, no data")`. |
| 244 | Termina la función y devuelve `None` implícitamente. |
| 245 | Línea en blanco de separación. |
| 246 | Inicia un bucle sobre `processor in self._processors`. |
| 247 | Ejecuta `print(`. |
| 248 | Ejecuta `f"{processor.get_name()}: total "`. |
| 249 | Ejecuta `f"{processor.get_total_processed()} items processed, "`. |
| 250 | Ejecuta `f"remaining {processor.get_data_len()} on processor"`. |
| 251 | Cierra la estructura con `)`. |
| 252 | Línea en blanco de separación. |
| 253 | Declara `def _put_element(self, element: Any) -> bool:`. |
| 254 | Docstring: `""" Return whether an element was sent to a processor """`. |
| 255 | Línea en blanco de separación. |
| 256 | Inicia un bucle sobre `processor in self._processors`. |
| 257 | Comentario: `# Polymorphism: DataStream uses the DataProcessor interface only.`. |
| 258 | Comprueba `processor.validate(element)`. |
| 259 | Ejecuta `processor.ingest(element)`. |
| 260 | Devuelve `True`. |
| 261 | Devuelve `False`. |
| 262 | Línea en blanco de separación. |
| 263 | Declara `def _get_processor_outputs(`. |
| 264 | Ejecuta `self,`. |
| 265 | Ejecuta `processor: DataProcessor,`. |
| 266 | Ejecuta `amount: int,`. |
| 267 | Ejecuta `) -> OutputData:`. |
| 268 | Docstring: `""" Return available outputs from one processor """`. |
| 269 | Línea en blanco de separación. |
| 270 | Ejecuta `outputs: OutputData = []`. |
| 271 | Inicia un bucle sobre `_ in range(amount)`. |
| 272 | Comprueba `processor.get_data_len() == 0`. |
| 273 | Interrumpe el bucle actual. |
| 274 | Ejecuta `outputs.append(processor.output())`. |
| 275 | Devuelve `outputs`. |
| 276 | Línea en blanco de separación. |
| 277 | Línea en blanco de separación. |
| 278 | Declara `class CSVExportPlugin:`. |
| 279 | Docstring: `""" Export processor output as CSV text """`. |
| 280 | Línea en blanco de separación. |
| 281 | Declara `def process_output(self, data: OutputData) -> None:`. |
| 282 | Docstring: `""" Print output data as a CSV line """`. |
| 283 | Línea en blanco de separación. |
| 284 | Ejecuta `print("CSV Output:")`. |
| 285 | Ejecuta `print(",".join(value for _, value in data))`. |
| 286 | Línea en blanco de separación. |
| 287 | Línea en blanco de separación. |
| 288 | Declara `class JSONExportPlugin:`. |
| 289 | Docstring: `""" Export processor output as JSON text """`. |
| 290 | Línea en blanco de separación. |
| 291 | Declara `def process_output(self, data: OutputData) -> None:`. |
| 292 | Docstring: `""" Print output data as a JSON object """`. |
| 293 | Línea en blanco de separación. |
| 294 | Ejecuta `print("JSON Output:")`. |
| 295 | Ejecuta `print(self._format_json_object(data))`. |
| 296 | Línea en blanco de separación. |
| 297 | Declara `def _format_json_object(self, data: OutputData) -> str:`. |
| 298 | Docstring: `""" Return output data formatted as a JSON object """`. |
| 299 | Línea en blanco de separación. |
| 300 | Ejecuta `pairs = [`. |
| 301 | Ejecuta `f'"item_{rank}": "{self._format_json_string(value)}"'`. |
| 302 | Inicia un bucle sobre `rank, value in data`. |
| 303 | Cierra la estructura con `]`. |
| 304 | Devuelve `"{" + ", ".join(pairs) + "}"`. |
| 305 | Línea en blanco de separación. |
| 306 | Declara `def _format_json_string(self, value: str) -> str:`. |
| 307 | Docstring: `""" Return a manually escaped JSON string value """`. |
| 308 | Línea en blanco de separación. |
| 309 | Ejecuta `escaped = value.replace("\\", "\\\\")`. |
| 310 | Ejecuta `escaped = escaped.replace('"', '\\"')`. |
| 311 | Ejecuta `escaped = escaped.replace("\n", "\\n")`. |
| 312 | Ejecuta `escaped = escaped.replace("\r", "\\r")`. |
| 313 | Devuelve `escaped.replace("\t", "\\t")`. |
| 314 | Línea en blanco de separación. |
| 315 | Línea en blanco de separación. |
| 316 | Declara `def build_log_entry(level: str, message: str) -> LogEntry:`. |
| 317 | Docstring: `""" Build one log entry from dynamic values """`. |
| 318 | Línea en blanco de separación. |
| 319 | Devuelve `{`. |
| 320 | Ejecuta `"log_level": level,`. |
| 321 | Ejecuta `"log_message": message,`. |
| 322 | Cierra la estructura con `}`. |
| 323 | Línea en blanco de separación. |
| 324 | Línea en blanco de separación. |
| 325 | Declara `def build_stream(*items: Any) -> list[Any]:`. |
| 326 | Docstring: `""" Build a stream from received items """`. |
| 327 | Línea en blanco de separación. |
| 328 | Devuelve `list(items)`. |
| 329 | Línea en blanco de separación. |
| 330 | Línea en blanco de separación. |
| 331 | Declara `def put_processors(`. |
| 332 | Ejecuta `data_stream: DataStream,`. |
| 333 | Ejecuta `processors: list[DataProcessor],`. |
| 334 | Ejecuta `) -> None:`. |
| 335 | Docstring: `""" Register processors in one data stream """`. |
| 336 | Línea en blanco de separación. |
| 337 | Inicia un bucle sobre `processor in processors`. |
| 338 | Ejecuta `data_stream.register_processor(processor)`. |
| 339 | Línea en blanco de separación. |
| 340 | Línea en blanco de separación. |
| 341 | Declara `def main() -> None:`. |
| 342 | Docstring: `""" Run the script entrypoint """`. |
| 343 | Línea en blanco de separación. |
| 344 | Ejecuta `first_stream = build_stream(`. |
| 345 | Ejecuta `TXT_VAL,`. |
| 346 | Ejecuta `NUM_DATA,`. |
| 347 | Ejecuta `[`. |
| 348 | Ejecuta `build_log_entry(LOG_WARN_LVL, LOG_WARN_MSG),`. |
| 349 | Ejecuta `build_log_entry(LOG_INFO_LVL, LOG_INFO_MSG),`. |
| 350 | Ejecuta `],`. |
| 351 | Ejecuta `NUM_VAL,`. |
| 352 | Ejecuta `TXT_DATA,`. |
| 353 | Cierra la estructura con `)`. |
| 354 | Ejecuta `second_stream = build_stream(`. |
| 355 | Ejecuta `NUM_VAL_2,`. |
| 356 | Ejecuta `TXT_DATA_2,`. |
| 357 | Ejecuta `[`. |
| 358 | Ejecuta `build_log_entry(LOG_ERR_LVL, LOG_ERR_MSG),`. |
| 359 | Ejecuta `build_log_entry(LOG_NOTICE_LVL, LOG_NOTICE_MSG),`. |
| 360 | Ejecuta `],`. |
| 361 | Ejecuta `NUM_DATA_2,`. |
| 362 | Ejecuta `TXT_VAL_2,`. |
| 363 | Cierra la estructura con `)`. |
| 364 | Ejecuta `data_stream = DataStream()`. |
| 365 | Línea en blanco de separación. |
| 366 | Ejecuta `print("=== Code Nexus - Data Pipeline ===")`. |
| 367 | Ejecuta `print("Initialize Data Stream...")`. |
| 368 | Ejecuta `data_stream.print_processors_stats()`. |
| 369 | Línea en blanco de separación. |
| 370 | Ejecuta `print("Registering Processors")`. |
| 371 | Ejecuta `put_processors(`. |
| 372 | Ejecuta `data_stream,`. |
| 373 | Ejecuta `[`. |
| 374 | Ejecuta `NumericProcessor(),`. |
| 375 | Ejecuta `TextProcessor(),`. |
| 376 | Ejecuta `LogProcessor(),`. |
| 377 | Ejecuta `],`. |
| 378 | Cierra la estructura con `)`. |
| 379 | Ejecuta `print(f"Send first batch of data on stream: {first_stream}")`. |
| 380 | Ejecuta `data_stream.process_stream(first_stream)`. |
| 381 | Ejecuta `data_stream.print_processors_stats()`. |
| 382 | Línea en blanco de separación. |
| 383 | Ejecuta `print(`. |
| 384 | Ejecuta `f"Send {CSV_OUT_NB} processed data from each processor "`. |
| 385 | Ejecuta `"to a CSV plugin:"`. |
| 386 | Cierra la estructura con `)`. |
| 387 | Ejecuta `data_stream.output_pipeline(CSV_OUT_NB, CSVExportPlugin())`. |
| 388 | Ejecuta `data_stream.print_processors_stats()`. |
| 389 | Línea en blanco de separación. |
| 390 | Ejecuta `print(f"Send another batch of data: {second_stream}")`. |
| 391 | Ejecuta `data_stream.process_stream(second_stream)`. |
| 392 | Ejecuta `data_stream.print_processors_stats()`. |
| 393 | Línea en blanco de separación. |
| 394 | Ejecuta `print(`. |
| 395 | Ejecuta `f"Send {JSON_OUT_NB} processed data from each processor "`. |
| 396 | Ejecuta `"to a JSON plugin:"`. |
| 397 | Cierra la estructura con `)`. |
| 398 | Ejecuta `data_stream.output_pipeline(JSON_OUT_NB, JSONExportPlugin())`. |
| 399 | Ejecuta `data_stream.print_processors_stats()`. |
| 400 | Línea en blanco de separación. |
| 401 | Línea en blanco de separación. |
| 402 | Comprueba `__name__ == "__main__"`. |
| 403 | Ejecuta `main()`. |
