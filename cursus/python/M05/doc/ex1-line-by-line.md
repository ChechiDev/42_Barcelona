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
| 17 | Asigna `name` a `self._name`. |
| 18 | Asigna `[]` a `self._items: list[str]`. |
| 19 | Asigna `0` a `self._next_output_rank`. |
| 20 | Asigna `0` a `self._total_processed`. |
| 21 | Línea en blanco de separación. |
| 22 | Declara la función o método `get_name`. |
| 23 | Docstring: `""" Return the processor display name """`. |
| 24 | Línea en blanco de separación. |
| 25 | Devuelve `self._name`. |
| 26 | Línea en blanco de separación. |
| 27 | Declara la función o método `get_data_len`. |
| 28 | Docstring: `""" Return the number of items waiting on the processor """`. |
| 29 | Línea en blanco de separación. |
| 30 | Devuelve `len(self._items)`. |
| 31 | Línea en blanco de separación. |
| 32 | Declara la función o método `get_total_processed`. |
| 33 | Docstring: `""" Return the total number of ingested items """`. |
| 34 | Línea en blanco de separación. |
| 35 | Devuelve `self._total_processed`. |
| 36 | Línea en blanco de separación. |
| 37 | Marca el método siguiente como abstracto. |
| 38 | Declara la función o método `validate`. |
| 39 | Docstring: `""" Return whether data can be ingested by this processor """`. |
| 40 | Línea en blanco de separación. |
| 41 | Marca el método siguiente como abstracto. |
| 42 | Declara la función o método `ingest`. |
| 43 | Docstring: `""" Ingest valid data into this processor """`. |
| 44 | Línea en blanco de separación. |
| 45 | Declara la función o método `output`. |
| 46 | Docstring: `""" Extract and return the oldest stored item with its rank """`. |
| 47 | Línea en blanco de separación. |
| 48 | Comprueba `not self._items`. |
| 49 | Lanza `IndexError("No data to output")`. |
| 50 | Línea en blanco de separación. |
| 51 | Asigna `self._next_output_rank` a `rank`. |
| 52 | Asigna `self._items.pop(0)` a `item`. |
| 53 | Asigna `1` a `self._next_output_rank +`. |
| 54 | Línea en blanco de separación. |
| 55 | Devuelve `rank, item`. |
| 56 | Línea en blanco de separación. |
| 57 | Declara la función o método `_put_item`. |
| 58 | Docstring: `""" Store one processed item and update statistics """`. |
| 59 | Línea en blanco de separación. |
| 60 | Ejecuta `self._items.append(item)`. |
| 61 | Asigna `1` a `self._total_processed +`. |
| 62 | Línea en blanco de separación. |
| 63 | Declara la función o método `_put_items`. |
| 64 | Docstring: `""" Store several processed items and update statistics """`. |
| 65 | Línea en blanco de separación. |
| 66 | Ejecuta `self._items.extend(items)`. |
| 67 | Asigna `len(items)` a `self._total_processed +`. |
| 68 | Línea en blanco de separación. |
| 69 | Declara la función o método `_put_scalar_or_list`. |
| 70 | Docstring: `""" Store one value or every value from a list as strings """`. |
| 71 | Línea en blanco de separación. |
| 72 | Comprueba `isinstance(data, list)`. |
| 73 | Ejecuta `self._put_items([str(item) for item in data])`. |
| 74 | Sale de la función o método. |
| 75 | Ejecuta `self._put_item(str(data))`. |
| 76 | Línea en blanco de separación. |
| 77 | Línea en blanco de separación. |
| 78 | Declara la clase `NumericProcessor`. |
| 79 | Docstring: `""" Process numeric values and lists of numeric values """`. |
| 80 | Línea en blanco de separación. |
| 81 | Declara la función o método `__init__`. |
| 82 | Docstring: `""" Initialize a numeric processor """`. |
| 83 | Línea en blanco de separación. |
| 84 | Ejecuta `super().__init__("Numeric Processor")`. |
| 85 | Línea en blanco de separación. |
| 86 | Declara la función o método `validate`. |
| 87 | Docstring: `""" Return whether data is numeric or a numeric list """`. |
| 88 | Línea en blanco de separación. |
| 89 | Comprueba `isinstance(data, list)`. |
| 90 | Devuelve `all(self._is_numeric(item) for item in data)`. |
| 91 | Devuelve `self._is_numeric(data)`. |
| 92 | Línea en blanco de separación. |
| 93 | Declara la función o método `ingest`. |
| 94 | Docstring: `""" Ingest numeric data as separated string items """`. |
| 95 | Línea en blanco de separación. |
| 96 | Comprueba `not self.validate(data)`. |
| 97 | Lanza `ValueError("Improper numeric data")`. |
| 98 | Línea en blanco de separación. |
| 99 | Ejecuta `self._put_scalar_or_list(data)`. |
| 100 | Línea en blanco de separación. |
| 101 | Declara la función o método `_is_numeric`. |
| 102 | Docstring: `""" Return whether data is a non-boolean number """`. |
| 103 | Línea en blanco de separación. |
| 104 | Devuelve `isinstance(data, (int, float)) and not isinstance(data, bool)`. |
| 105 | Línea en blanco de separación. |
| 106 | Línea en blanco de separación. |
| 107 | Declara la clase `TextProcessor`. |
| 108 | Docstring: `""" Process text values and lists of text values """`. |
| 109 | Línea en blanco de separación. |
| 110 | Declara la función o método `__init__`. |
| 111 | Docstring: `""" Initialize a text processor """`. |
| 112 | Línea en blanco de separación. |
| 113 | Ejecuta `super().__init__("Text Processor")`. |
| 114 | Línea en blanco de separación. |
| 115 | Declara la función o método `validate`. |
| 116 | Docstring: `""" Return whether data is text or a text list """`. |
| 117 | Línea en blanco de separación. |
| 118 | Comprueba `isinstance(data, str)`. |
| 119 | Devuelve `True`. |
| 120 | Comprueba `isinstance(data, list)`. |
| 121 | Devuelve `all(isinstance(item, str) for item in data)`. |
| 122 | Devuelve `False`. |
| 123 | Línea en blanco de separación. |
| 124 | Declara la función o método `ingest`. |
| 125 | Docstring: `""" Ingest text data as separated string items """`. |
| 126 | Línea en blanco de separación. |
| 127 | Comprueba `not self.validate(data)`. |
| 128 | Lanza `ValueError("Improper text data")`. |
| 129 | Línea en blanco de separación. |
| 130 | Ejecuta `self._put_scalar_or_list(data)`. |
| 131 | Línea en blanco de separación. |
| 132 | Línea en blanco de separación. |
| 133 | Declara la clase `LogProcessor`. |
| 134 | Docstring: `""" Process log dictionaries and lists of log dictionaries """`. |
| 135 | Línea en blanco de separación. |
| 136 | Declara la función o método `__init__`. |
| 137 | Docstring: `""" Initialize a log processor """`. |
| 138 | Línea en blanco de separación. |
| 139 | Ejecuta `super().__init__("Log Processor")`. |
| 140 | Línea en blanco de separación. |
| 141 | Declara la función o método `validate`. |
| 142 | Docstring: `""" Return whether data is a valid log entry or list """`. |
| 143 | Línea en blanco de separación. |
| 144 | Comprueba `isinstance(data, dict)`. |
| 145 | Devuelve `self._is_log_entry(data)`. |
| 146 | Comprueba `isinstance(data, list)`. |
| 147 | Devuelve `all(self._is_log_entry(item) for item in data)`. |
| 148 | Devuelve `False`. |
| 149 | Línea en blanco de separación. |
| 150 | Declara la función o método `ingest`. |
| 151 | Docstring: `""" Ingest log data as separated formatted strings """`. |
| 152 | Línea en blanco de separación. |
| 153 | Comprueba `not self.validate(data)`. |
| 154 | Lanza `ValueError("Improper log data")`. |
| 155 | Línea en blanco de separación. |
| 156 | Comprueba `isinstance(data, list)`. |
| 157 | Ejecuta `self._put_items([self._format_log_entry(item) for item in data])`. |
| 158 | Sale de la función o método. |
| 159 | Ejecuta `self._put_item(self._format_log_entry(data))`. |
| 160 | Línea en blanco de separación. |
| 161 | Declara la función o método `_is_log_entry`. |
| 162 | Docstring: `""" Return whether data is a dictionary with string pairs """`. |
| 163 | Línea en blanco de separación. |
| 164 | Devuelve `isinstance(data, dict) and all(`. |
| 165 | Ejecuta `isinstance(key, str) and isinstance(value, str)`. |
| 166 | Recorre `key, value in data.items()`. |
| 167 | Cierra una llamada o expresión multilínea. |
| 168 | Línea en blanco de separación. |
| 169 | Declara la función o método `_format_log_entry`. |
| 170 | Docstring: `""" Convert a log entry into the expected output format """`. |
| 171 | Línea en blanco de separación. |
| 172 | Asigna `entry.get("log_level", "")` a `level`. |
| 173 | Asigna `entry.get("log_message", "")` a `message`. |
| 174 | Comprueba `level or message`. |
| 175 | Devuelve `f"{level}: {message}"`. |
| 176 | Devuelve `str(entry)`. |
| 177 | Línea en blanco de separación. |
| 178 | Línea en blanco de separación. |
| 179 | Declara la clase `DataStream`. |
| 180 | Docstring: `""" Route stream elements to registered data processors """`. |
| 181 | Línea en blanco de separación. |
| 182 | Declara la función o método `__init__`. |
| 183 | Docstring: `""" Initialize an empty data stream """`. |
| 184 | Línea en blanco de separación. |
| 185 | Asigna `[]` a `self._processors: list[DataProcessor]`. |
| 186 | Línea en blanco de separación. |
| 187 | Declara la función o método `get_processors`. |
| 188 | Docstring: `""" Return registered processors """`. |
| 189 | Línea en blanco de separación. |
| 190 | Devuelve `self._processors`. |
| 191 | Línea en blanco de separación. |
| 192 | Declara la función o método `register_processor`. |
| 193 | Docstring: `""" Register a data processor for future stream processing """`. |
| 194 | Línea en blanco de separación. |
| 195 | Ejecuta `self._processors.append(proc)`. |
| 196 | Línea en blanco de separación. |
| 197 | Declara la función o método `process_stream`. |
| 198 | Docstring: `""" Send each stream element to the first compatible processor """`. |
| 199 | Línea en blanco de separación. |
| 200 | Recorre `element in stream`. |
| 201 | Comprueba `not self._put_element(element)`. |
| 202 | Imprime un mensaje por pantalla. |
| 203 | Ejecuta `"DataStream error - Can't process element in stream: "`. |
| 204 | Ejecuta `f"{element}"`. |
| 205 | Cierra una llamada o expresión multilínea. |
| 206 | Línea en blanco de separación. |
| 207 | Declara la función o método `print_processors_stats`. |
| 208 | Docstring: `""" Print statistics for every registered processor """`. |
| 209 | Línea en blanco de separación. |
| 210 | Imprime un mensaje por pantalla. |
| 211 | Comprueba `not self._processors`. |
| 212 | Imprime un mensaje por pantalla. |
| 213 | Sale de la función o método. |
| 214 | Línea en blanco de separación. |
| 215 | Recorre `processor in self._processors`. |
| 216 | Imprime un mensaje por pantalla. |
| 217 | Ejecuta `f"{processor.get_name()}: total "`. |
| 218 | Ejecuta `f"{processor.get_total_processed()} items processed, "`. |
| 219 | Ejecuta `f"remaining {processor.get_data_len()} on processor"`. |
| 220 | Cierra una llamada o expresión multilínea. |
| 221 | Línea en blanco de separación. |
| 222 | Declara la función o método `_put_element`. |
| 223 | Docstring: `""" Return whether an element was sent to a processor """`. |
| 224 | Línea en blanco de separación. |
| 225 | Recorre `processor in self._processors`. |
| 226 | Comentario: `Polymorphism: DataStream uses the DataProcessor interface only.`. |
| 227 | Comprueba `processor.validate(element)`. |
| 228 | Ejecuta `processor.ingest(element)`. |
| 229 | Devuelve `True`. |
| 230 | Devuelve `False`. |
| 231 | Línea en blanco de separación. |
| 232 | Línea en blanco de separación. |
| 233 | Declara la función o método `put_processor_outputs`. |
| 234 | Docstring: `""" Consume a fixed number of values from a processor """`. |
| 235 | Línea en blanco de separación. |
| 236 | Recorre `_ in range(amount)`. |
| 237 | Ejecuta `processor.output()`. |
| 238 | Línea en blanco de separación. |
| 239 | Línea en blanco de separación. |
| 240 | Declara la función o método `build_log_entry`. |
| 241 | Docstring: `""" Build one log entry from dynamic values """`. |
| 242 | Línea en blanco de separación. |
| 243 | Devuelve `{`. |
| 244 | Continúa una estructura o llamada con `"log_level": level,`. |
| 245 | Continúa una estructura o llamada con `"log_message": message,`. |
| 246 | Cierra el diccionario. |
| 247 | Línea en blanco de separación. |
| 248 | Línea en blanco de separación. |
| 249 | Declara la función o método `build_stream`. |
| 250 | Docstring: `""" Build a stream from received items """`. |
| 251 | Línea en blanco de separación. |
| 252 | Devuelve `list(items)`. |
| 253 | Línea en blanco de separación. |
| 254 | Línea en blanco de separación. |
| 255 | Declara la función o método `run_demo`. |
| 256 | Continúa una estructura o llamada con `stream: list[Any],`. |
| 257 | Continúa una estructura o llamada con `numeric_output_amount: int,`. |
| 258 | Continúa una estructura o llamada con `text_output_amount: int,`. |
| 259 | Continúa una estructura o llamada con `log_output_amount: int,`. |
| 260 | Cierra una firma multilínea de función o método. |
| 261 | Docstring: `""" Run the data stream demonstration scenario """`. |
| 262 | Línea en blanco de separación. |
| 263 | Imprime un mensaje por pantalla. |
| 264 | Imprime un mensaje por pantalla. |
| 265 | Imprime un mensaje por pantalla. |
| 266 | Asigna `DataStream()` a `data_stream`. |
| 267 | Ejecuta `data_stream.print_processors_stats()`. |
| 268 | Línea en blanco de separación. |
| 269 | Asigna `NumericProcessor()` a `numeric_processor`. |
| 270 | Imprime un mensaje por pantalla. |
| 271 | Ejecuta `data_stream.register_processor(numeric_processor)`. |
| 272 | Imprime un mensaje por pantalla. |
| 273 | Ejecuta `data_stream.process_stream(stream)`. |
| 274 | Ejecuta `data_stream.print_processors_stats()`. |
| 275 | Línea en blanco de separación. |
| 276 | Asigna `TextProcessor()` a `text_processor`. |
| 277 | Asigna `LogProcessor()` a `log_processor`. |
| 278 | Imprime un mensaje por pantalla. |
| 279 | Imprime un mensaje por pantalla. |
| 280 | Ejecuta `data_stream.register_processor(text_processor)`. |
| 281 | Ejecuta `data_stream.register_processor(log_processor)`. |
| 282 | Imprime un mensaje por pantalla. |
| 283 | Ejecuta `data_stream.process_stream(stream)`. |
| 284 | Ejecuta `data_stream.print_processors_stats()`. |
| 285 | Línea en blanco de separación. |
| 286 | Imprime un mensaje por pantalla. |
| 287 | Ejecuta `"Consume some elements from the data processors: "`. |
| 288 | Ejecuta `f"Numeric {numeric_output_amount}, "`. |
| 289 | Ejecuta `f"Text {text_output_amount}, "`. |
| 290 | Ejecuta `f"Log {log_output_amount}"`. |
| 291 | Cierra una llamada o expresión multilínea. |
| 292 | Ejecuta `put_processor_outputs(numeric_processor, numeric_output_amount)`. |
| 293 | Ejecuta `put_processor_outputs(text_processor, text_output_amount)`. |
| 294 | Ejecuta `put_processor_outputs(log_processor, log_output_amount)`. |
| 295 | Ejecuta `data_stream.print_processors_stats()`. |
