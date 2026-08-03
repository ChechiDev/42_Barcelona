# M05 ex0: explicación línea por línea

Este documento vincula cada línea de `ex0/data_processor.py` con lo que hace.

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
| 12 | Asigna `42` a `NUM_VAL`. |
| 13 | Asigna `"Hello"` a `NUM_INV_VAL`. |
| 14 | Asigna `"foo"` a `NUM_INV_ING`. |
| 15 | Asigna `[1, 2, 3, 4, 5]` a `NUM_DATA`. |
| 16 | Asigna `3` a `NUM_OUT_NB`. |
| 17 | Línea en blanco de separación. |
| 18 | Asigna `42` a `TXT_INV_VAL`. |
| 19 | Asigna `["Hello", "Nexus", "World"]` a `TXT_DATA`. |
| 20 | Asigna `1` a `TXT_OUT_NB`. |
| 21 | Línea en blanco de separación. |
| 22 | Asigna `"Hello"` a `LOG_INV_VAL`. |
| 23 | Asigna `"NOTICE"` a `LOG_NOTICE_LVL`. |
| 24 | Asigna `"Connection to server"` a `LOG_NOTICE_MSG`. |
| 25 | Asigna `"ERROR"` a `LOG_ERR_LVL`. |
| 26 | Asigna `"Unauthorized access!!"` a `LOG_ERR_MSG`. |
| 27 | Asigna `2` a `LOG_OUT_NB`. |
| 28 | Línea en blanco de separación. |
| 29 | Línea en blanco de separación. |
| 30 | Declara `class DataProcessor(ABC):`. |
| 31 | Docstring: `""" Define the common interface for all data processors """`. |
| 32 | Línea en blanco de separación. |
| 33 | Declara `def __init__(self) -> None:`. |
| 34 | Docstring: `""" Initialize an empty processor storage """`. |
| 35 | Línea en blanco de separación. |
| 36 | Ejecuta `self._items: list[str] = []`. |
| 37 | Ejecuta `self._next_output_rank = 0`. |
| 38 | Línea en blanco de separación. |
| 39 | Declara `def get_data_len(self) -> int:`. |
| 40 | Docstring: `""" Return the number of items waiting on the processor """`. |
| 41 | Línea en blanco de separación. |
| 42 | Devuelve `len(self._items)`. |
| 43 | Línea en blanco de separación. |
| 44 | Aplica el decorador `@abstractmethod`. |
| 45 | Declara `def validate(self, data: Any) -> bool:`. |
| 46 | Docstring: `""" Return whether data can be ingested by this processor """`. |
| 47 | Línea en blanco de separación. |
| 48 | Aplica el decorador `@abstractmethod`. |
| 49 | Declara `def ingest(self, data: Any) -> None:`. |
| 50 | Docstring: `""" Ingest valid data into this processor """`. |
| 51 | Línea en blanco de separación. |
| 52 | Declara `def output(self) -> tuple[int, str]:`. |
| 53 | Docstring: `""" Extract and return the oldest stored item with its rank """`. |
| 54 | Línea en blanco de separación. |
| 55 | Comprueba `not self._items`. |
| 56 | Lanza `IndexError("No data to output")`. |
| 57 | Línea en blanco de separación. |
| 58 | Asigna `self._next_output_rank` a `rank`. |
| 59 | Ejecuta `item = self._items.pop(0)`. |
| 60 | Ejecuta `self._next_output_rank += 1`. |
| 61 | Línea en blanco de separación. |
| 62 | Devuelve `rank, item`. |
| 63 | Línea en blanco de separación. |
| 64 | Declara `def _put_item(self, item: str) -> None:`. |
| 65 | Docstring: `""" Store one processed item """`. |
| 66 | Línea en blanco de separación. |
| 67 | Ejecuta `self._items.append(item)`. |
| 68 | Línea en blanco de separación. |
| 69 | Declara `def _put_items(self, items: list[str]) -> None:`. |
| 70 | Docstring: `""" Store several processed items """`. |
| 71 | Línea en blanco de separación. |
| 72 | Ejecuta `self._items.extend(items)`. |
| 73 | Línea en blanco de separación. |
| 74 | Declara `def _put_scalar_or_list(self, data: Any) -> None:`. |
| 75 | Docstring: `""" Store one value or every value from a list as strings """`. |
| 76 | Línea en blanco de separación. |
| 77 | Comprueba `isinstance(data, list)`. |
| 78 | Ejecuta `self._put_items([str(item) for item in data])`. |
| 79 | Devuelve desde la función. |
| 80 | Ejecuta `self._put_item(str(data))`. |
| 81 | Línea en blanco de separación. |
| 82 | Línea en blanco de separación. |
| 83 | Declara `class NumericProcessor(DataProcessor):`. |
| 84 | Docstring: `""" Process numeric values and lists of numeric values """`. |
| 85 | Línea en blanco de separación. |
| 86 | Declara `def validate(self, data: Any) -> bool:`. |
| 87 | Docstring: `""" Return whether data is numeric or a numeric list """`. |
| 88 | Línea en blanco de separación. |
| 89 | Comprueba `isinstance(data, list)`. |
| 90 | Devuelve `all(self._is_numeric(item) for item in data)`. |
| 91 | Devuelve `self._is_numeric(data)`. |
| 92 | Línea en blanco de separación. |
| 93 | Declara `def ingest(self, data: NumericData) -> None:`. |
| 94 | Docstring: `""" Ingest numeric data as separated string items """`. |
| 95 | Línea en blanco de separación. |
| 96 | Comprueba `not self.validate(data)`. |
| 97 | Lanza `ValueError("Improper numeric data")`. |
| 98 | Línea en blanco de separación. |
| 99 | Ejecuta `self._put_scalar_or_list(data)`. |
| 100 | Línea en blanco de separación. |
| 101 | Declara `def _is_numeric(self, data: Any) -> bool:`. |
| 102 | Docstring: `""" Return whether data is a non-boolean number """`. |
| 103 | Línea en blanco de separación. |
| 104 | Devuelve `isinstance(data, (int, float)) and not isinstance(data, bool)`. |
| 105 | Línea en blanco de separación. |
| 106 | Línea en blanco de separación. |
| 107 | Declara `class TextProcessor(DataProcessor):`. |
| 108 | Docstring: `""" Process text values and lists of text values """`. |
| 109 | Línea en blanco de separación. |
| 110 | Declara `def validate(self, data: Any) -> bool:`. |
| 111 | Docstring: `""" Return whether data is text or a text list """`. |
| 112 | Línea en blanco de separación. |
| 113 | Comprueba `isinstance(data, str)`. |
| 114 | Devuelve `True`. |
| 115 | Comprueba `isinstance(data, list)`. |
| 116 | Devuelve `all(isinstance(item, str) for item in data)`. |
| 117 | Devuelve `False`. |
| 118 | Línea en blanco de separación. |
| 119 | Declara `def ingest(self, data: TextData) -> None:`. |
| 120 | Docstring: `""" Ingest text data as separated string items """`. |
| 121 | Línea en blanco de separación. |
| 122 | Comprueba `not self.validate(data)`. |
| 123 | Lanza `ValueError("Improper text data")`. |
| 124 | Línea en blanco de separación. |
| 125 | Ejecuta `self._put_scalar_or_list(data)`. |
| 126 | Línea en blanco de separación. |
| 127 | Línea en blanco de separación. |
| 128 | Declara `class LogProcessor(DataProcessor):`. |
| 129 | Docstring: `""" Process log dictionaries and lists of log dictionaries """`. |
| 130 | Línea en blanco de separación. |
| 131 | Declara `def validate(self, data: Any) -> bool:`. |
| 132 | Docstring: `""" Return whether data is a valid log entry or list """`. |
| 133 | Línea en blanco de separación. |
| 134 | Comprueba `isinstance(data, dict)`. |
| 135 | Devuelve `self._is_log_entry(data)`. |
| 136 | Comprueba `isinstance(data, list)`. |
| 137 | Devuelve `all(self._is_log_entry(item) for item in data)`. |
| 138 | Devuelve `False`. |
| 139 | Línea en blanco de separación. |
| 140 | Declara `def ingest(self, data: LogData) -> None:`. |
| 141 | Docstring: `""" Ingest log data as separated formatted strings """`. |
| 142 | Línea en blanco de separación. |
| 143 | Comprueba `not self.validate(data)`. |
| 144 | Lanza `ValueError("Improper log data")`. |
| 145 | Línea en blanco de separación. |
| 146 | Comprueba `isinstance(data, list)`. |
| 147 | Ejecuta `self._put_items([self._format_log_entry(item) for item in data])`. |
| 148 | Devuelve desde la función. |
| 149 | Ejecuta `self._put_item(self._format_log_entry(data))`. |
| 150 | Línea en blanco de separación. |
| 151 | Declara `def _is_log_entry(self, data: Any) -> bool:`. |
| 152 | Docstring: `""" Return whether data is a dictionary with string pairs """`. |
| 153 | Línea en blanco de separación. |
| 154 | Devuelve `isinstance(data, dict) and all(`. |
| 155 | Ejecuta `isinstance(key, str) and isinstance(value, str)`. |
| 156 | Recorre `key, value in data.items()`. |
| 157 | Cierra una estructura o llamada multilínea. |
| 158 | Línea en blanco de separación. |
| 159 | Declara `def _format_log_entry(self, entry: LogEntry) -> str:`. |
| 160 | Docstring: `""" Convert a log entry into the expected output format """`. |
| 161 | Línea en blanco de separación. |
| 162 | Ejecuta `level = entry.get("log_level", "")`. |
| 163 | Ejecuta `message = entry.get("log_message", "")`. |
| 164 | Comprueba `level or message`. |
| 165 | Devuelve `f"{level}: {message}"`. |
| 166 | Devuelve `str(entry)`. |
| 167 | Línea en blanco de separación. |
| 168 | Línea en blanco de separación. |
| 169 | Declara `def print_validation(processor: DataProcessor, value: Any) -> None:`. |
| 170 | Docstring: `""" Print the validation result for one value """`. |
| 171 | Línea en blanco de separación. |
| 172 | Imprime `print(f"Trying to validate input'{value}': {processor.validate(value)}")`. |
| 173 | Línea en blanco de separación. |
| 174 | Línea en blanco de separación. |
| 175 | Declara `def print_outputs(`. |
| 176 | Continúa con `processor: DataProcessor,`. |
| 177 | Continúa con `amount: int,`. |
| 178 | Continúa con `label: str,`. |
| 179 | Cierra una estructura o llamada multilínea. |
| 180 | Docstring: `""" Print a fixed number of processor outputs """`. |
| 181 | Línea en blanco de separación. |
| 182 | Recorre `_ in range(amount)`. |
| 183 | Ejecuta `rank, value = processor.output()`. |
| 184 | Imprime `print(f"{label} {rank}: {value}")`. |
| 185 | Línea en blanco de separación. |
| 186 | Línea en blanco de separación. |
| 187 | Declara `def build_log_entry(level: str, message: str) -> LogEntry:`. |
| 188 | Docstring: `""" Build one log entry from dynamic values """`. |
| 189 | Línea en blanco de separación. |
| 190 | Devuelve `{`. |
| 191 | Continúa con `"log_level": level,`. |
| 192 | Continúa con `"log_message": message,`. |
| 193 | Cierra una estructura o llamada multilínea. |
| 194 | Línea en blanco de separación. |
| 195 | Línea en blanco de separación. |
| 196 | Declara `def run_numeric_processor_demo(`. |
| 197 | Continúa con `valid_value: Any,`. |
| 198 | Continúa con `invalid_value: Any,`. |
| 199 | Continúa con `invalid_ingest: Any,`. |
| 200 | Continúa con `numeric_data: NumericData,`. |
| 201 | Continúa con `output_amount: int,`. |
| 202 | Cierra una estructura o llamada multilínea. |
| 203 | Docstring: `""" Run the numeric processor demo """`. |
| 204 | Línea en blanco de separación. |
| 205 | Ejecuta `processor = NumericProcessor()`. |
| 206 | Imprime `print()`. |
| 207 | Imprime `print("Testing Numeric Processor...")`. |
| 208 | Ejecuta `print_validation(processor, valid_value)`. |
| 209 | Ejecuta `print_validation(processor, invalid_value)`. |
| 210 | Imprime `print(`. |
| 211 | Continúa con `"Test invalid ingestion of "`. |
| 212 | Continúa con `f"string'{invalid_ingest}'without prior validation:"`. |
| 213 | Cierra una estructura o llamada multilínea. |
| 214 | Línea en blanco de separación. |
| 215 | Inicia un bloque `try`. |
| 216 | Continúa con `processor.ingest(invalid_ingest)  # type: ignore[arg-type]`. |
| 217 | Captura `ValueError as error`. |
| 218 | Imprime `print(f"Got exception: {error}")`. |
| 219 | Línea en blanco de separación. |
| 220 | Imprime `print(f"Processing data: {numeric_data}")`. |
| 221 | Ejecuta `processor.ingest(numeric_data)`. |
| 222 | Imprime `print(f"Extracting {output_amount} values...")`. |
| 223 | Ejecuta `print_outputs(processor, output_amount, "Numeric value")`. |
| 224 | Línea en blanco de separación. |
| 225 | Línea en blanco de separación. |
| 226 | Declara `def run_text_processor_demo(`. |
| 227 | Continúa con `invalid_value: Any,`. |
| 228 | Continúa con `text_data: TextData,`. |
| 229 | Continúa con `output_amount: int,`. |
| 230 | Cierra una estructura o llamada multilínea. |
| 231 | Docstring: `""" Run the text processor demo """`. |
| 232 | Línea en blanco de separación. |
| 233 | Ejecuta `processor = TextProcessor()`. |
| 234 | Imprime `print()`. |
| 235 | Imprime `print("Testing Text Processor...")`. |
| 236 | Ejecuta `print_validation(processor, invalid_value)`. |
| 237 | Imprime `print(f"Processing data: {text_data}")`. |
| 238 | Ejecuta `processor.ingest(text_data)`. |
| 239 | Imprime `print(f"Extracting {output_amount} value...")`. |
| 240 | Ejecuta `print_outputs(processor, output_amount, "Text value")`. |
| 241 | Línea en blanco de separación. |
| 242 | Línea en blanco de separación. |
| 243 | Declara `def run_log_processor_demo(`. |
| 244 | Continúa con `invalid_value: Any,`. |
| 245 | Continúa con `log_data: LogData,`. |
| 246 | Continúa con `output_amount: int,`. |
| 247 | Cierra una estructura o llamada multilínea. |
| 248 | Docstring: `""" Run the log processor demo """`. |
| 249 | Línea en blanco de separación. |
| 250 | Ejecuta `processor = LogProcessor()`. |
| 251 | Imprime `print()`. |
| 252 | Imprime `print("Testing Log Processor...")`. |
| 253 | Ejecuta `print_validation(processor, invalid_value)`. |
| 254 | Imprime `print(f"Processing data: {log_data}")`. |
| 255 | Ejecuta `processor.ingest(log_data)`. |
| 256 | Imprime `print(f"Extracting {output_amount} values...")`. |
| 257 | Ejecuta `print_outputs(processor, output_amount, "Log entry")`. |
| 258 | Línea en blanco de separación. |
| 259 | Línea en blanco de separación. |
| 260 | Declara `def run_demo(`. |
| 261 | Continúa con `numeric_valid_value: Any,`. |
| 262 | Continúa con `numeric_invalid_value: Any,`. |
| 263 | Continúa con `numeric_invalid_ingest: Any,`. |
| 264 | Continúa con `numeric_data: NumericData,`. |
| 265 | Continúa con `text_invalid_value: Any,`. |
| 266 | Continúa con `text_data: TextData,`. |
| 267 | Continúa con `log_invalid_value: Any,`. |
| 268 | Continúa con `log_data: LogData,`. |
| 269 | Continúa con `numeric_output_amount: int,`. |
| 270 | Continúa con `text_output_amount: int,`. |
| 271 | Continúa con `log_output_amount: int,`. |
| 272 | Cierra una estructura o llamada multilínea. |
| 273 | Docstring: `""" Run the data processor demo """`. |
| 274 | Línea en blanco de separación. |
| 275 | Imprime `print("=== Code Nexus - Data Processor ===")`. |
| 276 | Continúa con `run_numeric_processor_demo(`. |
| 277 | Continúa con `numeric_valid_value,`. |
| 278 | Continúa con `numeric_invalid_value,`. |
| 279 | Continúa con `numeric_invalid_ingest,`. |
| 280 | Continúa con `numeric_data,`. |
| 281 | Continúa con `numeric_output_amount,`. |
| 282 | Cierra una estructura o llamada multilínea. |
| 283 | Ejecuta `run_text_processor_demo(text_invalid_value, text_data, text_output_amount)`. |
| 284 | Ejecuta `run_log_processor_demo(log_invalid_value, log_data, log_output_amount)`. |
| 285 | Línea en blanco de separación. |
| 286 | Línea en blanco de separación. |
| 287 | Declara `def main() -> None:`. |
| 288 | Docstring: `""" Run the script entrypoint """`. |
| 289 | Línea en blanco de separación. |
| 290 | Continúa con `run_demo(`. |
| 291 | Continúa con `NUM_VAL,`. |
| 292 | Continúa con `NUM_INV_VAL,`. |
| 293 | Continúa con `NUM_INV_ING,`. |
| 294 | Continúa con `NUM_DATA,`. |
| 295 | Continúa con `TXT_INV_VAL,`. |
| 296 | Continúa con `TXT_DATA,`. |
| 297 | Continúa con `LOG_INV_VAL,`. |
| 298 | Continúa con `[`. |
| 299 | Continúa con `build_log_entry(LOG_NOTICE_LVL, LOG_NOTICE_MSG),`. |
| 300 | Continúa con `build_log_entry(LOG_ERR_LVL, LOG_ERR_MSG),`. |
| 301 | Cierra una estructura o llamada multilínea. |
| 302 | Continúa con `NUM_OUT_NB,`. |
| 303 | Continúa con `TXT_OUT_NB,`. |
| 304 | Continúa con `LOG_OUT_NB,`. |
| 305 | Cierra una estructura o llamada multilínea. |
| 306 | Línea en blanco de separación. |
| 307 | Línea en blanco de separación. |
| 308 | Comprueba `__name__ == "__main__"`. |
| 309 | Ejecuta `main()`. |
