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
| 7 | Ejecuta `NumericData = int \| float \| list[int \| float]`. |
| 8 | Ejecuta `TextData = str \| list[str]`. |
| 9 | Ejecuta `LogEntry = dict[str, str]`. |
| 10 | Ejecuta `LogData = LogEntry \| list[LogEntry]`. |
| 11 | Línea en blanco de separación. |
| 12 | Ejecuta `NUM_VAL = 42`. |
| 13 | Ejecuta `NUM_INV_VAL = "Hello"`. |
| 14 | Ejecuta `NUM_INV_ING = "foo"`. |
| 15 | Ejecuta `NUM_DATA = [1, 2, 3, 4, 5]`. |
| 16 | Ejecuta `NUM_OUT_NB = 3`. |
| 17 | Línea en blanco de separación. |
| 18 | Ejecuta `TXT_INV_VAL = 42`. |
| 19 | Ejecuta `TXT_DATA = ["Hello", "Nexus", "World"]`. |
| 20 | Ejecuta `TXT_OUT_NB = 1`. |
| 21 | Línea en blanco de separación. |
| 22 | Ejecuta `LOG_INV_VAL = "Hello"`. |
| 23 | Ejecuta `LOG_NOTICE_LVL = "NOTICE"`. |
| 24 | Ejecuta `LOG_NOTICE_MSG = "Connection to server"`. |
| 25 | Ejecuta `LOG_ERR_LVL = "ERROR"`. |
| 26 | Ejecuta `LOG_ERR_MSG = "Unauthorized access!!"`. |
| 27 | Ejecuta `LOG_OUT_NB = 2`. |
| 28 | Línea en blanco de separación. |
| 29 | Línea en blanco de separación. |
| 30 | Declara `class DataProcessor(ABC):`. |
| 31 | Docstring: `""" Define the common interface for all data processors """`. |
| 32 | Línea en blanco de separación. |
| 33 | Declara `def __init__(self) -> None:`. |
| 34 | Ejecuta `self._items: list[str] = []`. |
| 35 | Ejecuta `self._next_output_rank = 0`. |
| 36 | Línea en blanco de separación. |
| 37 | Declara `def get_data_len(self) -> int:`. |
| 38 | Docstring: `""" Return the number of items waiting on the processor """`. |
| 39 | Línea en blanco de separación. |
| 40 | Devuelve `len(self._items)`. |
| 41 | Línea en blanco de separación. |
| 42 | Aplica el decorador `@abstractmethod`. |
| 43 | Declara `def validate(self, data: Any) -> bool:`. |
| 44 | Docstring: `""" Return whether data can be ingested by this processor """`. |
| 45 | Línea en blanco de separación. |
| 46 | Aplica el decorador `@abstractmethod`. |
| 47 | Declara `def ingest(self, data: Any) -> None:`. |
| 48 | Docstring: `""" Ingest valid data into this processor """`. |
| 49 | Línea en blanco de separación. |
| 50 | Declara `def output(self) -> tuple[int, str]:`. |
| 51 | Docstring: `""" Extract and return the oldest stored item with its rank """`. |
| 52 | Línea en blanco de separación. |
| 53 | Comprueba `not self._items`. |
| 54 | Lanza `IndexError("No data to output")`. |
| 55 | Línea en blanco de separación. |
| 56 | Ejecuta `rank = self._next_output_rank`. |
| 57 | Ejecuta `item = self._items.pop(0)`. |
| 58 | Ejecuta `self._next_output_rank += 1`. |
| 59 | Línea en blanco de separación. |
| 60 | Devuelve `rank, item`. |
| 61 | Línea en blanco de separación. |
| 62 | Declara `def _put_item(self, item: str) -> None:`. |
| 63 | Docstring: `""" Store one processed item """`. |
| 64 | Línea en blanco de separación. |
| 65 | Ejecuta `self._items.append(item)`. |
| 66 | Línea en blanco de separación. |
| 67 | Declara `def _put_items(self, items: list[str]) -> None:`. |
| 68 | Docstring: `""" Store several processed items """`. |
| 69 | Línea en blanco de separación. |
| 70 | Ejecuta `self._items.extend(items)`. |
| 71 | Línea en blanco de separación. |
| 72 | Declara `def _put_scalar_or_list(self, data: Any) -> None:`. |
| 73 | Docstring: `""" Store one value or every value from a list as strings """`. |
| 74 | Línea en blanco de separación. |
| 75 | Comprueba `isinstance(data, list)`. |
| 76 | Ejecuta `self._put_items([str(item) for item in data])`. |
| 77 | Devuelve desde la función. |
| 78 | Ejecuta `self._put_item(str(data))`. |
| 79 | Línea en blanco de separación. |
| 80 | Línea en blanco de separación. |
| 81 | Declara `class NumericProcessor(DataProcessor):`. |
| 82 | Docstring: `""" Process numeric values and lists of numeric values """`. |
| 83 | Línea en blanco de separación. |
| 84 | Declara `def validate(self, data: Any) -> bool:`. |
| 85 | Docstring: `""" Return whether data is numeric or a numeric list """`. |
| 86 | Línea en blanco de separación. |
| 87 | Comprueba `isinstance(data, list)`. |
| 88 | Devuelve `all(self._is_numeric(item) for item in data)`. |
| 89 | Devuelve `self._is_numeric(data)`. |
| 90 | Línea en blanco de separación. |
| 91 | Declara `def ingest(self, data: NumericData) -> None:`. |
| 92 | Docstring: `""" Ingest numeric data as separated string items """`. |
| 93 | Línea en blanco de separación. |
| 94 | Comprueba `not self.validate(data)`. |
| 95 | Lanza `ValueError("Improper numeric data")`. |
| 96 | Línea en blanco de separación. |
| 97 | Ejecuta `self._put_scalar_or_list(data)`. |
| 98 | Línea en blanco de separación. |
| 99 | Declara `def _is_numeric(self, data: Any) -> bool:`. |
| 100 | Docstring: `""" Return whether data is a non-boolean number """`. |
| 101 | Línea en blanco de separación. |
| 102 | Devuelve `isinstance(data, (int, float)) and not isinstance(data, bool)`. |
| 103 | Línea en blanco de separación. |
| 104 | Línea en blanco de separación. |
| 105 | Declara `class TextProcessor(DataProcessor):`. |
| 106 | Docstring: `""" Process text values and lists of text values """`. |
| 107 | Línea en blanco de separación. |
| 108 | Declara `def validate(self, data: Any) -> bool:`. |
| 109 | Docstring: `""" Return whether data is text or a text list """`. |
| 110 | Línea en blanco de separación. |
| 111 | Comprueba `isinstance(data, str)`. |
| 112 | Devuelve `True`. |
| 113 | Comprueba `isinstance(data, list)`. |
| 114 | Devuelve `all(isinstance(item, str) for item in data)`. |
| 115 | Devuelve `False`. |
| 116 | Línea en blanco de separación. |
| 117 | Declara `def ingest(self, data: TextData) -> None:`. |
| 118 | Docstring: `""" Ingest text data as separated string items """`. |
| 119 | Línea en blanco de separación. |
| 120 | Comprueba `not self.validate(data)`. |
| 121 | Lanza `ValueError("Improper text data")`. |
| 122 | Línea en blanco de separación. |
| 123 | Ejecuta `self._put_scalar_or_list(data)`. |
| 124 | Línea en blanco de separación. |
| 125 | Línea en blanco de separación. |
| 126 | Declara `class LogProcessor(DataProcessor):`. |
| 127 | Docstring: `""" Process log dictionaries and lists of log dictionaries """`. |
| 128 | Línea en blanco de separación. |
| 129 | Declara `def validate(self, data: Any) -> bool:`. |
| 130 | Docstring: `""" Return whether data is a valid log entry or list """`. |
| 131 | Línea en blanco de separación. |
| 132 | Comprueba `isinstance(data, dict)`. |
| 133 | Devuelve `self._is_log_entry(data)`. |
| 134 | Comprueba `isinstance(data, list)`. |
| 135 | Devuelve `all(self._is_log_entry(item) for item in data)`. |
| 136 | Devuelve `False`. |
| 137 | Línea en blanco de separación. |
| 138 | Declara `def ingest(self, data: LogData) -> None:`. |
| 139 | Docstring: `""" Ingest log data as separated formatted strings """`. |
| 140 | Línea en blanco de separación. |
| 141 | Comprueba `not self.validate(data)`. |
| 142 | Lanza `ValueError("Improper log data")`. |
| 143 | Línea en blanco de separación. |
| 144 | Comprueba `isinstance(data, list)`. |
| 145 | Ejecuta `self._put_items([self._format_log_entry(item) for item in data])`. |
| 146 | Devuelve desde la función. |
| 147 | Ejecuta `self._put_item(self._format_log_entry(data))`. |
| 148 | Línea en blanco de separación. |
| 149 | Declara `def _is_log_entry(self, data: Any) -> bool:`. |
| 150 | Docstring: `""" Return whether data is a dictionary with string pairs """`. |
| 151 | Línea en blanco de separación. |
| 152 | Devuelve `isinstance(data, dict) and all(`. |
| 153 | Ejecuta `isinstance(key, str) and isinstance(value, str)`. |
| 154 | Recorre `key, value in data.items()`. |
| 155 | Cierra una estructura o llamada multilínea. |
| 156 | Línea en blanco de separación. |
| 157 | Declara `def _format_log_entry(self, entry: LogEntry) -> str:`. |
| 158 | Docstring: `""" Convert a log entry into the expected output format """`. |
| 159 | Línea en blanco de separación. |
| 160 | Ejecuta `level = entry.get("log_level", "")`. |
| 161 | Ejecuta `message = entry.get("log_message", "")`. |
| 162 | Comprueba `level or message`. |
| 163 | Devuelve `f"{level}: {message}"`. |
| 164 | Devuelve `str(entry)`. |
| 165 | Línea en blanco de separación. |
| 166 | Línea en blanco de separación. |
| 167 | Declara `def print_validation(processor: DataProcessor, value: Any) -> None:`. |
| 168 | Docstring: `""" Print the validation result for one value """`. |
| 169 | Línea en blanco de separación. |
| 170 | Imprime `print(f"Trying to validate input'{value}': {processor.validate(value)}")`. |
| 171 | Línea en blanco de separación. |
| 172 | Línea en blanco de separación. |
| 173 | Declara `def print_outputs(`. |
| 174 | Continúa con `processor: DataProcessor,`. |
| 175 | Continúa con `amount: int,`. |
| 176 | Continúa con `label: str,`. |
| 177 | Ejecuta `) -> None:`. |
| 178 | Docstring: `""" Print a fixed number of processor outputs """`. |
| 179 | Línea en blanco de separación. |
| 180 | Recorre `_ in range(amount)`. |
| 181 | Ejecuta `rank, value = processor.output()`. |
| 182 | Imprime `print(f"{label} {rank}: {value}")`. |
| 183 | Línea en blanco de separación. |
| 184 | Línea en blanco de separación. |
| 185 | Declara `def build_log_entry(level: str, message: str) -> LogEntry:`. |
| 186 | Docstring: `""" Build one log entry from dynamic values """`. |
| 187 | Línea en blanco de separación. |
| 188 | Devuelve `{`. |
| 189 | Continúa con `"log_level": level,`. |
| 190 | Continúa con `"log_message": message,`. |
| 191 | Cierra una estructura o llamada multilínea. |
| 192 | Línea en blanco de separación. |
| 193 | Línea en blanco de separación. |
| 194 | Declara `def run_numeric_processor_demo(`. |
| 195 | Continúa con `valid_value: Any,`. |
| 196 | Continúa con `invalid_value: Any,`. |
| 197 | Continúa con `invalid_ingest: Any,`. |
| 198 | Continúa con `numeric_data: NumericData,`. |
| 199 | Continúa con `output_amount: int,`. |
| 200 | Ejecuta `) -> None:`. |
| 201 | Docstring: `""" Run the numeric processor demo """`. |
| 202 | Línea en blanco de separación. |
| 203 | Ejecuta `processor = NumericProcessor()`. |
| 204 | Imprime `print()`. |
| 205 | Imprime `print("Testing Numeric Processor...")`. |
| 206 | Ejecuta `print_validation(processor, valid_value)`. |
| 207 | Ejecuta `print_validation(processor, invalid_value)`. |
| 208 | Imprime `print(`. |
| 209 | Ejecuta `"Test invalid ingestion of "`. |
| 210 | Ejecuta `f"string'{invalid_ingest}'without prior validation:"`. |
| 211 | Cierra una estructura o llamada multilínea. |
| 212 | Línea en blanco de separación. |
| 213 | Inicia un bloque `try`. |
| 214 | Ejecuta `processor.ingest(invalid_ingest)  # type: ignore[arg-type]`. |
| 215 | Captura `ValueError as error`. |
| 216 | Imprime `print(f"Got exception: {error}")`. |
| 217 | Línea en blanco de separación. |
| 218 | Imprime `print(f"Processing data: {numeric_data}")`. |
| 219 | Ejecuta `processor.ingest(numeric_data)`. |
| 220 | Imprime `print(f"Extracting {output_amount} values...")`. |
| 221 | Ejecuta `print_outputs(processor, output_amount, "Numeric value")`. |
| 222 | Línea en blanco de separación. |
| 223 | Línea en blanco de separación. |
| 224 | Declara `def run_text_processor_demo(`. |
| 225 | Continúa con `invalid_value: Any,`. |
| 226 | Continúa con `text_data: TextData,`. |
| 227 | Continúa con `output_amount: int,`. |
| 228 | Ejecuta `) -> None:`. |
| 229 | Docstring: `""" Run the text processor demo """`. |
| 230 | Línea en blanco de separación. |
| 231 | Ejecuta `processor = TextProcessor()`. |
| 232 | Imprime `print()`. |
| 233 | Imprime `print("Testing Text Processor...")`. |
| 234 | Ejecuta `print_validation(processor, invalid_value)`. |
| 235 | Imprime `print(f"Processing data: {text_data}")`. |
| 236 | Ejecuta `processor.ingest(text_data)`. |
| 237 | Imprime `print(f"Extracting {output_amount} value...")`. |
| 238 | Ejecuta `print_outputs(processor, output_amount, "Text value")`. |
| 239 | Línea en blanco de separación. |
| 240 | Línea en blanco de separación. |
| 241 | Declara `def run_log_processor_demo(`. |
| 242 | Continúa con `invalid_value: Any,`. |
| 243 | Continúa con `log_data: LogData,`. |
| 244 | Continúa con `output_amount: int,`. |
| 245 | Ejecuta `) -> None:`. |
| 246 | Docstring: `""" Run the log processor demo """`. |
| 247 | Línea en blanco de separación. |
| 248 | Ejecuta `processor = LogProcessor()`. |
| 249 | Imprime `print()`. |
| 250 | Imprime `print("Testing Log Processor...")`. |
| 251 | Ejecuta `print_validation(processor, invalid_value)`. |
| 252 | Imprime `print(f"Processing data: {log_data}")`. |
| 253 | Ejecuta `processor.ingest(log_data)`. |
| 254 | Imprime `print(f"Extracting {output_amount} values...")`. |
| 255 | Ejecuta `print_outputs(processor, output_amount, "Log entry")`. |
| 256 | Línea en blanco de separación. |
| 257 | Línea en blanco de separación. |
| 258 | Declara `def main() -> None:`. |
| 259 | Docstring: `""" Run the script entrypoint """`. |
| 260 | Línea en blanco de separación. |
| 261 | Imprime `print("=== Code Nexus - Data Processor ===")`. |
| 262 | Continúa con `run_numeric_processor_demo(`. |
| 263 | Continúa con `NUM_VAL,`. |
| 264 | Continúa con `NUM_INV_VAL,`. |
| 265 | Continúa con `NUM_INV_ING,`. |
| 266 | Continúa con `NUM_DATA,`. |
| 267 | Continúa con `NUM_OUT_NB,`. |
| 268 | Cierra una estructura o llamada multilínea. |
| 269 | Ejecuta `run_text_processor_demo(TXT_INV_VAL, TXT_DATA, TXT_OUT_NB)`. |
| 270 | Continúa con `run_log_processor_demo(`. |
| 271 | Continúa con `LOG_INV_VAL,`. |
| 272 | Abre `[`. |
| 273 | Continúa con `build_log_entry(LOG_NOTICE_LVL, LOG_NOTICE_MSG),`. |
| 274 | Continúa con `build_log_entry(LOG_ERR_LVL, LOG_ERR_MSG),`. |
| 275 | Cierra una estructura o llamada multilínea. |
| 276 | Continúa con `LOG_OUT_NB,`. |
| 277 | Cierra una estructura o llamada multilínea. |
| 278 | Línea en blanco de separación. |
| 279 | Línea en blanco de separación. |
| 280 | Comprueba `__name__ == "__main__"`. |
| 281 | Ejecuta `main()`. |
