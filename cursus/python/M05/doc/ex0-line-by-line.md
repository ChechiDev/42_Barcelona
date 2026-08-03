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
| 7 | Asigna `int | float | list[int | float]` a `NumericData`. |
| 8 | Asigna `str | list[str]` a `TextData`. |
| 9 | Asigna `dict[str, str]` a `LogEntry`. |
| 10 | Asigna `LogEntry | list[LogEntry]` a `LogData`. |
| 11 | Línea en blanco de separación. |
| 12 | Línea en blanco de separación. |
| 13 | Declara la clase `DataProcessor`. |
| 14 | Docstring: `""" Define the common interface for all data processors """`. |
| 15 | Línea en blanco de separación. |
| 16 | Declara la función o método `__init__`. |
| 17 | Docstring: `""" Initialize an empty processor storage """`. |
| 18 | Línea en blanco de separación. |
| 19 | Asigna `[]` a `self._items: list[str]`. |
| 20 | Asigna `0` a `self._next_output_rank`. |
| 21 | Línea en blanco de separación. |
| 22 | Declara la función o método `get_data_len`. |
| 23 | Docstring: `""" Return the number of items waiting on the processor """`. |
| 24 | Línea en blanco de separación. |
| 25 | Devuelve `len(self._items)`. |
| 26 | Línea en blanco de separación. |
| 27 | Marca el método siguiente como abstracto. |
| 28 | Declara la función o método `validate`. |
| 29 | Docstring: `""" Return whether data can be ingested by this processor """`. |
| 30 | Línea en blanco de separación. |
| 31 | Marca el método siguiente como abstracto. |
| 32 | Declara la función o método `ingest`. |
| 33 | Docstring: `""" Ingest valid data into this processor """`. |
| 34 | Línea en blanco de separación. |
| 35 | Declara la función o método `output`. |
| 36 | Docstring: `""" Extract and return the oldest stored item with its rank """`. |
| 37 | Línea en blanco de separación. |
| 38 | Comprueba `not self._items`. |
| 39 | Lanza `IndexError("No data to output")`. |
| 40 | Línea en blanco de separación. |
| 41 | Asigna `self._next_output_rank` a `rank`. |
| 42 | Asigna `self._items.pop(0)` a `item`. |
| 43 | Asigna `1` a `self._next_output_rank +`. |
| 44 | Línea en blanco de separación. |
| 45 | Devuelve `rank, item`. |
| 46 | Línea en blanco de separación. |
| 47 | Declara la función o método `_put_item`. |
| 48 | Docstring: `""" Store one processed item """`. |
| 49 | Línea en blanco de separación. |
| 50 | Ejecuta `self._items.append(item)`. |
| 51 | Línea en blanco de separación. |
| 52 | Declara la función o método `_put_items`. |
| 53 | Docstring: `""" Store several processed items """`. |
| 54 | Línea en blanco de separación. |
| 55 | Ejecuta `self._items.extend(items)`. |
| 56 | Línea en blanco de separación. |
| 57 | Declara la función o método `_put_scalar_or_list`. |
| 58 | Docstring: `""" Store one value or every value from a list as strings """`. |
| 59 | Línea en blanco de separación. |
| 60 | Comprueba `isinstance(data, list)`. |
| 61 | Ejecuta `self._put_items([str(item) for item in data])`. |
| 62 | Sale de la función o método. |
| 63 | Ejecuta `self._put_item(str(data))`. |
| 64 | Línea en blanco de separación. |
| 65 | Línea en blanco de separación. |
| 66 | Declara la clase `NumericProcessor`. |
| 67 | Docstring: `""" Process numeric values and lists of numeric values """`. |
| 68 | Línea en blanco de separación. |
| 69 | Declara la función o método `validate`. |
| 70 | Docstring: `""" Return whether data is numeric or a numeric list """`. |
| 71 | Línea en blanco de separación. |
| 72 | Comprueba `isinstance(data, list)`. |
| 73 | Devuelve `all(self._is_numeric(item) for item in data)`. |
| 74 | Devuelve `self._is_numeric(data)`. |
| 75 | Línea en blanco de separación. |
| 76 | Declara la función o método `ingest`. |
| 77 | Docstring: `""" Ingest numeric data as separated string items """`. |
| 78 | Línea en blanco de separación. |
| 79 | Comprueba `not self.validate(data)`. |
| 80 | Lanza `ValueError("Improper numeric data")`. |
| 81 | Línea en blanco de separación. |
| 82 | Ejecuta `self._put_scalar_or_list(data)`. |
| 83 | Línea en blanco de separación. |
| 84 | Declara la función o método `_is_numeric`. |
| 85 | Docstring: `""" Return whether data is a non-boolean number """`. |
| 86 | Línea en blanco de separación. |
| 87 | Devuelve `isinstance(data, (int, float)) and not isinstance(data, bool)`. |
| 88 | Línea en blanco de separación. |
| 89 | Línea en blanco de separación. |
| 90 | Declara la clase `TextProcessor`. |
| 91 | Docstring: `""" Process text values and lists of text values """`. |
| 92 | Línea en blanco de separación. |
| 93 | Declara la función o método `validate`. |
| 94 | Docstring: `""" Return whether data is text or a text list """`. |
| 95 | Línea en blanco de separación. |
| 96 | Comprueba `isinstance(data, str)`. |
| 97 | Devuelve `True`. |
| 98 | Comprueba `isinstance(data, list)`. |
| 99 | Devuelve `all(isinstance(item, str) for item in data)`. |
| 100 | Devuelve `False`. |
| 101 | Línea en blanco de separación. |
| 102 | Declara la función o método `ingest`. |
| 103 | Docstring: `""" Ingest text data as separated string items """`. |
| 104 | Línea en blanco de separación. |
| 105 | Comprueba `not self.validate(data)`. |
| 106 | Lanza `ValueError("Improper text data")`. |
| 107 | Línea en blanco de separación. |
| 108 | Ejecuta `self._put_scalar_or_list(data)`. |
| 109 | Línea en blanco de separación. |
| 110 | Línea en blanco de separación. |
| 111 | Declara la clase `LogProcessor`. |
| 112 | Docstring: `""" Process log dictionaries and lists of log dictionaries """`. |
| 113 | Línea en blanco de separación. |
| 114 | Declara la función o método `validate`. |
| 115 | Docstring: `""" Return whether data is a valid log entry or list """`. |
| 116 | Línea en blanco de separación. |
| 117 | Comprueba `isinstance(data, dict)`. |
| 118 | Devuelve `self._is_log_entry(data)`. |
| 119 | Comprueba `isinstance(data, list)`. |
| 120 | Devuelve `all(self._is_log_entry(item) for item in data)`. |
| 121 | Devuelve `False`. |
| 122 | Línea en blanco de separación. |
| 123 | Declara la función o método `ingest`. |
| 124 | Docstring: `""" Ingest log data as separated formatted strings """`. |
| 125 | Línea en blanco de separación. |
| 126 | Comprueba `not self.validate(data)`. |
| 127 | Lanza `ValueError("Improper log data")`. |
| 128 | Línea en blanco de separación. |
| 129 | Comprueba `isinstance(data, list)`. |
| 130 | Ejecuta `self._put_items([self._format_log_entry(item) for item in data])`. |
| 131 | Sale de la función o método. |
| 132 | Ejecuta `self._put_item(self._format_log_entry(data))`. |
| 133 | Línea en blanco de separación. |
| 134 | Declara la función o método `_is_log_entry`. |
| 135 | Docstring: `""" Return whether data is a dictionary with string pairs """`. |
| 136 | Línea en blanco de separación. |
| 137 | Devuelve `isinstance(data, dict) and all(`. |
| 138 | Ejecuta `isinstance(key, str) and isinstance(value, str)`. |
| 139 | Recorre `key, value in data.items()`. |
| 140 | Cierra una llamada o expresión multilínea. |
| 141 | Línea en blanco de separación. |
| 142 | Declara la función o método `_format_log_entry`. |
| 143 | Docstring: `""" Convert a log entry into the expected output format """`. |
| 144 | Línea en blanco de separación. |
| 145 | Asigna `entry.get("log_level", "")` a `level`. |
| 146 | Asigna `entry.get("log_message", "")` a `message`. |
| 147 | Comprueba `level or message`. |
| 148 | Devuelve `f"{level}: {message}"`. |
| 149 | Devuelve `str(entry)`. |
| 150 | Línea en blanco de separación. |
| 151 | Línea en blanco de separación. |
| 152 | Declara la función o método `print_validation`. |
| 153 | Docstring: `""" Print the validation result for one value """`. |
| 154 | Línea en blanco de separación. |
| 155 | Imprime un mensaje por pantalla. |
| 156 | Línea en blanco de separación. |
| 157 | Línea en blanco de separación. |
| 158 | Declara la función o método `print_outputs`. |
| 159 | Continúa una estructura o llamada con `processor: DataProcessor,`. |
| 160 | Continúa una estructura o llamada con `amount: int,`. |
| 161 | Continúa una estructura o llamada con `label: str,`. |
| 162 | Cierra una firma multilínea de función o método. |
| 163 | Docstring: `""" Print a fixed number of processor outputs """`. |
| 164 | Línea en blanco de separación. |
| 165 | Recorre `_ in range(amount)`. |
| 166 | Asigna `processor.output()` a `rank, value`. |
| 167 | Imprime un mensaje por pantalla. |
| 168 | Línea en blanco de separación. |
| 169 | Línea en blanco de separación. |
| 170 | Declara la función o método `build_log_entry`. |
| 171 | Docstring: `""" Build one log entry from dynamic values """`. |
| 172 | Línea en blanco de separación. |
| 173 | Devuelve `{`. |
| 174 | Continúa una estructura o llamada con `"log_level": level,`. |
| 175 | Continúa una estructura o llamada con `"log_message": message,`. |
| 176 | Cierra el diccionario. |
| 177 | Línea en blanco de separación. |
| 178 | Línea en blanco de separación. |
| 179 | Declara la función o método `run_numeric_processor_demo`. |
| 180 | Continúa una estructura o llamada con `valid_value: Any,`. |
| 181 | Continúa una estructura o llamada con `invalid_value: Any,`. |
| 182 | Continúa una estructura o llamada con `invalid_ingest: Any,`. |
| 183 | Continúa una estructura o llamada con `numeric_data: NumericData,`. |
| 184 | Continúa una estructura o llamada con `output_amount: int,`. |
| 185 | Cierra una firma multilínea de función o método. |
| 186 | Docstring: `""" Run the numeric processor demo """`. |
| 187 | Línea en blanco de separación. |
| 188 | Asigna `NumericProcessor()` a `processor`. |
| 189 | Imprime un mensaje por pantalla. |
| 190 | Imprime un mensaje por pantalla. |
| 191 | Ejecuta `print_validation(processor, valid_value)`. |
| 192 | Ejecuta `print_validation(processor, invalid_value)`. |
| 193 | Imprime un mensaje por pantalla. |
| 194 | Ejecuta `"Test invalid ingestion of "`. |
| 195 | Ejecuta `f"string'{invalid_ingest}'without prior validation:"`. |
| 196 | Cierra una llamada o expresión multilínea. |
| 197 | Línea en blanco de separación. |
| 198 | Inicia un bloque `try`. |
| 199 | Ejecuta `processor.ingest(invalid_ingest)  # type: ignore[arg-type]`. |
| 200 | Captura `ValueError as error`. |
| 201 | Imprime un mensaje por pantalla. |
| 202 | Línea en blanco de separación. |
| 203 | Imprime un mensaje por pantalla. |
| 204 | Ejecuta `processor.ingest(numeric_data)`. |
| 205 | Imprime un mensaje por pantalla. |
| 206 | Ejecuta `print_outputs(processor, output_amount, "Numeric value")`. |
| 207 | Línea en blanco de separación. |
| 208 | Línea en blanco de separación. |
| 209 | Declara la función o método `run_text_processor_demo`. |
| 210 | Continúa una estructura o llamada con `invalid_value: Any,`. |
| 211 | Continúa una estructura o llamada con `text_data: TextData,`. |
| 212 | Continúa una estructura o llamada con `output_amount: int,`. |
| 213 | Cierra una firma multilínea de función o método. |
| 214 | Docstring: `""" Run the text processor demo """`. |
| 215 | Línea en blanco de separación. |
| 216 | Asigna `TextProcessor()` a `processor`. |
| 217 | Imprime un mensaje por pantalla. |
| 218 | Imprime un mensaje por pantalla. |
| 219 | Ejecuta `print_validation(processor, invalid_value)`. |
| 220 | Imprime un mensaje por pantalla. |
| 221 | Ejecuta `processor.ingest(text_data)`. |
| 222 | Imprime un mensaje por pantalla. |
| 223 | Ejecuta `print_outputs(processor, output_amount, "Text value")`. |
| 224 | Línea en blanco de separación. |
| 225 | Línea en blanco de separación. |
| 226 | Declara la función o método `run_log_processor_demo`. |
| 227 | Continúa una estructura o llamada con `invalid_value: Any,`. |
| 228 | Continúa una estructura o llamada con `log_data: LogData,`. |
| 229 | Continúa una estructura o llamada con `output_amount: int,`. |
| 230 | Cierra una firma multilínea de función o método. |
| 231 | Docstring: `""" Run the log processor demo """`. |
| 232 | Línea en blanco de separación. |
| 233 | Asigna `LogProcessor()` a `processor`. |
| 234 | Imprime un mensaje por pantalla. |
| 235 | Imprime un mensaje por pantalla. |
| 236 | Ejecuta `print_validation(processor, invalid_value)`. |
| 237 | Imprime un mensaje por pantalla. |
| 238 | Ejecuta `processor.ingest(log_data)`. |
| 239 | Imprime un mensaje por pantalla. |
| 240 | Ejecuta `print_outputs(processor, output_amount, "Log entry")`. |
| 241 | Línea en blanco de separación. |
| 242 | Línea en blanco de separación. |
| 243 | Declara la función o método `run_demo`. |
| 244 | Continúa una estructura o llamada con `numeric_valid_value: Any,`. |
| 245 | Continúa una estructura o llamada con `numeric_invalid_value: Any,`. |
| 246 | Continúa una estructura o llamada con `numeric_invalid_ingest: Any,`. |
| 247 | Continúa una estructura o llamada con `numeric_data: NumericData,`. |
| 248 | Continúa una estructura o llamada con `text_invalid_value: Any,`. |
| 249 | Continúa una estructura o llamada con `text_data: TextData,`. |
| 250 | Continúa una estructura o llamada con `log_invalid_value: Any,`. |
| 251 | Continúa una estructura o llamada con `log_data: LogData,`. |
| 252 | Continúa una estructura o llamada con `numeric_output_amount: int,`. |
| 253 | Continúa una estructura o llamada con `text_output_amount: int,`. |
| 254 | Continúa una estructura o llamada con `log_output_amount: int,`. |
| 255 | Cierra una firma multilínea de función o método. |
| 256 | Docstring: `""" Run the data processor demo """`. |
| 257 | Línea en blanco de separación. |
| 258 | Imprime un mensaje por pantalla. |
| 259 | Ejecuta `run_numeric_processor_demo(`. |
| 260 | Continúa una estructura o llamada con `numeric_valid_value,`. |
| 261 | Continúa una estructura o llamada con `numeric_invalid_value,`. |
| 262 | Continúa una estructura o llamada con `numeric_invalid_ingest,`. |
| 263 | Continúa una estructura o llamada con `numeric_data,`. |
| 264 | Continúa una estructura o llamada con `numeric_output_amount,`. |
| 265 | Cierra una llamada o expresión multilínea. |
| 266 | Ejecuta `run_text_processor_demo(text_invalid_value, text_data, text_output_amount)`. |
| 267 | Ejecuta `run_log_processor_demo(log_invalid_value, log_data, log_output_amount)`. |
