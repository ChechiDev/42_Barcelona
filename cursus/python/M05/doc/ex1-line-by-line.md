# M05 ex1: explicación línea por línea

Este documento vincula cada línea de `ex1/data_stream.py` con lo que hace.

| Línea | Qué hace |
| --- | --- |
| 1 | Indica al sistema que ejecute el archivo con `python3`. |
| 2 | Línea en blanco obligatoria después del shebang. |
| 3 | Importa `ABC` y `abstractmethod` para crear clases abstractas. |
| 4 | Importa `Any` para anotar datos de cualquier tipo. |
| 5 | Línea en blanco de separación. |
| 6 | Línea en blanco de separación. |
| 7 | Define el alias `NumericData` para números o listas de números. |
| 8 | Define el alias `TextData` para texto o listas de texto. |
| 9 | Define el alias `LogEntry` como diccionario de claves y valores `str`. |
| 10 | Define el alias `LogData` como un log o una lista de logs. |
| 11 | Línea en blanco de separación. |
| 12 | Línea en blanco de separación. |
| 13 | Declara la clase abstracta base `DataProcessor`. |
| 14 | Docstring de la clase base. |
| 15 | Línea en blanco antes del constructor. |
| 16 | Declara el constructor, recibiendo el nombre visible del procesador. |
| 17 | Docstring del constructor. |
| 18 | Línea en blanco antes del cuerpo. |
| 19 | Guarda el nombre visible del procesador. |
| 20 | Inicializa la cola interna de elementos procesados. |
| 21 | Inicializa el ranking de salida. |
| 22 | Inicializa el contador total de elementos procesados. |
| 23 | Línea en blanco de separación. |
| 24 | Declara `get_name`. |
| 25 | Docstring de `get_name`. |
| 26 | Línea en blanco antes del cuerpo. |
| 27 | Devuelve el nombre visible del procesador. |
| 28 | Línea en blanco de separación. |
| 29 | Declara `get_data_len`. |
| 30 | Docstring de `get_data_len`. |
| 31 | Línea en blanco antes del cuerpo. |
| 32 | Devuelve cuántos elementos quedan pendientes. |
| 33 | Línea en blanco de separación. |
| 34 | Declara `get_total_processed`. |
| 35 | Docstring de `get_total_processed`. |
| 36 | Línea en blanco antes del cuerpo. |
| 37 | Devuelve el total histórico de elementos ingeridos. |
| 38 | Línea en blanco de separación. |
| 39 | Marca `validate` como método abstracto. |
| 40 | Declara `validate`, obligatorio en subclases. |
| 41 | Docstring de `validate`. |
| 42 | Línea en blanco; no hay implementación por ser abstracto. |
| 43 | Marca `ingest` como método abstracto. |
| 44 | Declara `ingest`, obligatorio en subclases. |
| 45 | Docstring de `ingest`. |
| 46 | Línea en blanco; no hay implementación por ser abstracto. |
| 47 | Declara `output`, común para todos los procesadores. |
| 48 | Docstring de `output`. |
| 49 | Línea en blanco antes del cuerpo. |
| 50 | Comprueba si el procesador no tiene datos pendientes. |
| 51 | Lanza `IndexError` si no hay nada que extraer. |
| 52 | Línea en blanco de separación lógica. |
| 53 | Guarda el ranking actual de salida. |
| 54 | Extrae el elemento más antiguo de la cola. |
| 55 | Incrementa el ranking para la siguiente salida. |
| 56 | Línea en blanco de separación lógica. |
| 57 | Devuelve la tupla `(rank, item)`. |
| 58 | Línea en blanco de separación. |
| 59 | Declara `_put_item`. |
| 60 | Docstring de `_put_item`. |
| 61 | Línea en blanco antes del cuerpo. |
| 62 | Añade un elemento procesado a la cola. |
| 63 | Incrementa el contador total procesado. |
| 64 | Línea en blanco de separación. |
| 65 | Declara `_put_items`. |
| 66 | Docstring de `_put_items`. |
| 67 | Línea en blanco antes del cuerpo. |
| 68 | Añade varios elementos procesados a la cola. |
| 69 | Incrementa el contador total según el número de elementos añadidos. |
| 70 | Línea en blanco de separación. |
| 71 | Declara `_put_scalar_or_list`. |
| 72 | Docstring de `_put_scalar_or_list`. |
| 73 | Línea en blanco antes del cuerpo. |
| 74 | Comprueba si el dato recibido es una lista. |
| 75 | Convierte los elementos a `str` y los guarda en bloque. |
| 76 | Sale tras guardar la lista. |
| 77 | Convierte un dato individual a `str` y lo guarda. |
| 78 | Línea en blanco de separación. |
| 79 | Línea en blanco de separación. |
| 80 | Declara `NumericProcessor`, heredando de `DataProcessor`. |
| 81 | Docstring del procesador numérico. |
| 82 | Línea en blanco antes del constructor. |
| 83 | Declara el constructor de `NumericProcessor`. |
| 84 | Docstring del constructor numérico. |
| 85 | Línea en blanco antes del cuerpo. |
| 86 | Inicializa la clase base con el nombre `Numeric Processor`. |
| 87 | Línea en blanco de separación. |
| 88 | Implementa `validate` para datos numéricos. |
| 89 | Docstring de la validación numérica. |
| 90 | Línea en blanco antes del cuerpo. |
| 91 | Comprueba si el dato es una lista. |
| 92 | Valida que todos los elementos sean números no booleanos. |
| 93 | Valida un dato individual como número no booleano. |
| 94 | Línea en blanco de separación. |
| 95 | Implementa `ingest` para `NumericData`. |
| 96 | Docstring de la ingesta numérica. |
| 97 | Línea en blanco antes del cuerpo. |
| 98 | Comprueba si el dato numérico es inválido. |
| 99 | Lanza `ValueError` con el mensaje requerido para números. |
| 100 | Línea en blanco antes de almacenar. |
| 101 | Guarda número o lista de números como strings. |
| 102 | Línea en blanco de separación. |
| 103 | Declara `_is_numeric`. |
| 104 | Docstring de `_is_numeric`. |
| 105 | Línea en blanco antes del cuerpo. |
| 106 | Devuelve `True` para `int` o `float`, rechazando `bool`. |
| 107 | Línea en blanco de separación. |
| 108 | Línea en blanco de separación. |
| 109 | Declara `TextProcessor`, heredando de `DataProcessor`. |
| 110 | Docstring del procesador de texto. |
| 111 | Línea en blanco antes del constructor. |
| 112 | Declara el constructor de `TextProcessor`. |
| 113 | Docstring del constructor de texto. |
| 114 | Línea en blanco antes del cuerpo. |
| 115 | Inicializa la clase base con el nombre `Text Processor`. |
| 116 | Línea en blanco de separación. |
| 117 | Implementa `validate` para texto. |
| 118 | Docstring de la validación de texto. |
| 119 | Línea en blanco antes del cuerpo. |
| 120 | Comprueba si el dato es un string. |
| 121 | Acepta el string individual. |
| 122 | Comprueba si el dato es una lista. |
| 123 | Valida que todos los elementos de la lista sean strings. |
| 124 | Rechaza cualquier otro tipo. |
| 125 | Línea en blanco de separación. |
| 126 | Implementa `ingest` para `TextData`. |
| 127 | Docstring de la ingesta de texto. |
| 128 | Línea en blanco antes del cuerpo. |
| 129 | Comprueba si el texto es inválido. |
| 130 | Lanza `ValueError` con el mensaje requerido para texto. |
| 131 | Línea en blanco antes de almacenar. |
| 132 | Guarda string o lista de strings. |
| 133 | Línea en blanco de separación. |
| 134 | Línea en blanco de separación. |
| 135 | Declara `LogProcessor`, heredando de `DataProcessor`. |
| 136 | Docstring del procesador de logs. |
| 137 | Línea en blanco antes del constructor. |
| 138 | Declara el constructor de `LogProcessor`. |
| 139 | Docstring del constructor de logs. |
| 140 | Línea en blanco antes del cuerpo. |
| 141 | Inicializa la clase base con el nombre `Log Processor`. |
| 142 | Línea en blanco de separación. |
| 143 | Implementa `validate` para logs. |
| 144 | Docstring de la validación de logs. |
| 145 | Línea en blanco antes del cuerpo. |
| 146 | Comprueba si el dato es un diccionario. |
| 147 | Valida un único diccionario de log. |
| 148 | Comprueba si el dato es una lista. |
| 149 | Valida que todos los elementos sean logs válidos. |
| 150 | Rechaza cualquier otro tipo. |
| 151 | Línea en blanco de separación. |
| 152 | Implementa `ingest` para `LogData`. |
| 153 | Docstring de la ingesta de logs. |
| 154 | Línea en blanco antes del cuerpo. |
| 155 | Comprueba si el log es inválido. |
| 156 | Lanza `ValueError` con el mensaje requerido para logs. |
| 157 | Línea en blanco antes de almacenar. |
| 158 | Comprueba si el dato es una lista de logs. |
| 159 | Formatea cada log y guarda todos los resultados. |
| 160 | Sale tras guardar la lista. |
| 161 | Formatea y guarda un único log. |
| 162 | Línea en blanco de separación. |
| 163 | Declara `_is_log_entry`. |
| 164 | Docstring de `_is_log_entry`. |
| 165 | Línea en blanco antes del cuerpo. |
| 166 | Comprueba que el dato sea diccionario y evalúa sus pares. |
| 167 | Comprueba que cada clave y valor sean strings. |
| 168 | Recorre todos los pares clave-valor del diccionario. |
| 169 | Cierra la expresión y devuelve el resultado. |
| 170 | Línea en blanco de separación. |
| 171 | Declara `_format_log_entry`. |
| 172 | Docstring de `_format_log_entry`. |
| 173 | Línea en blanco antes del cuerpo. |
| 174 | Obtiene `log_level` o string vacío. |
| 175 | Obtiene `log_message` o string vacío. |
| 176 | Comprueba si existe nivel o mensaje. |
| 177 | Devuelve el formato `LEVEL: message`. |
| 178 | Si no hay claves conocidas, devuelve el diccionario como string. |
| 179 | Línea en blanco de separación. |
| 180 | Línea en blanco de separación. |
| 181 | Declara la clase `DataStream`. |
| 182 | Docstring de `DataStream`. |
| 183 | Línea en blanco antes del constructor. |
| 184 | Declara el constructor de `DataStream`. |
| 185 | Docstring del constructor de stream. |
| 186 | Línea en blanco antes del cuerpo. |
| 187 | Inicializa la lista de procesadores registrados. |
| 188 | Línea en blanco de separación. |
| 189 | Declara `get_processors`. |
| 190 | Docstring de `get_processors`. |
| 191 | Línea en blanco antes del cuerpo. |
| 192 | Devuelve la lista de procesadores registrados. |
| 193 | Línea en blanco de separación. |
| 194 | Declara `register_processor`, método requerido por el subject. |
| 195 | Docstring de `register_processor`. |
| 196 | Línea en blanco antes del cuerpo. |
| 197 | Añade el procesador recibido al stream. |
| 198 | Línea en blanco de separación. |
| 199 | Declara `process_stream`, método requerido por el subject. |
| 200 | Docstring de `process_stream`. |
| 201 | Línea en blanco antes del cuerpo. |
| 202 | Recorre cada elemento del stream recibido. |
| 203 | Intenta enviar el elemento a algún procesador registrado. |
| 204 | Empieza el `print` multilínea de error si nadie lo procesa. |
| 205 | Primera parte del mensaje de error requerido. |
| 206 | Añade el elemento no procesado al mensaje. |
| 207 | Cierra el `print` de error. |
| 208 | Línea en blanco de separación. |
| 209 | Declara `print_processors_stats`, método requerido por el subject. |
| 210 | Docstring de `print_processors_stats`. |
| 211 | Línea en blanco antes del cuerpo. |
| 212 | Imprime el título de estadísticas. |
| 213 | Comprueba si no hay procesadores registrados. |
| 214 | Imprime el mensaje de stream vacío. |
| 215 | Sale porque no hay estadísticas que mostrar. |
| 216 | Línea en blanco de separación lógica. |
| 217 | Recorre todos los procesadores registrados. |
| 218 | Empieza el `print` multilínea de estadísticas. |
| 219 | Imprime el nombre del procesador y empieza el total. |
| 220 | Añade el total de elementos procesados. |
| 221 | Añade los elementos pendientes en el procesador. |
| 222 | Cierra el `print` de estadísticas. |
| 223 | Línea en blanco de separación. |
| 224 | Declara el helper interno `_put_element`. |
| 225 | Docstring de `_put_element`. |
| 226 | Línea en blanco antes del cuerpo. |
| 227 | Recorre los procesadores registrados por orden. |
| 228 | Pregunta al procesador si puede aceptar el elemento. |
| 229 | Ingiere el elemento en el primer procesador compatible. |
| 230 | Devuelve `True` porque el elemento fue procesado. |
| 231 | Devuelve `False` si ningún procesador aceptó el elemento. |
| 232 | Línea en blanco de separación. |
| 233 | Línea en blanco de separación. |
| 234 | Declara `put_processor_outputs`. |
| 235 | Docstring de `put_processor_outputs`. |
| 236 | Línea en blanco antes del cuerpo. |
| 237 | Repite la extracción tantas veces como indique `amount`. |
| 238 | Consume un elemento llamando a `output`. |
| 239 | Línea en blanco de separación. |
| 240 | Línea en blanco de separación. |
| 241 | Declara `build_demo_stream`. |
| 242 | Docstring de `build_demo_stream`. |
| 243 | Línea en blanco antes del cuerpo. |
| 244 | Empieza la lista del stream de demostración. |
| 245 | Primer elemento: texto simple. |
| 246 | Segundo elemento: lista numérica. |
| 247 | Tercer elemento: lista de logs. |
| 248 | Empieza el primer log. |
| 249 | Define el nivel del primer log. |
| 250 | Define el mensaje del primer log. |
| 251 | Cierra el primer log. |
| 252 | Define el segundo log en una línea. |
| 253 | Cierra la lista de logs. |
| 254 | Cuarto elemento: número individual. |
| 255 | Quinto elemento: lista de strings. |
| 256 | Cierra y devuelve la lista del stream. |
| 257 | Línea en blanco de separación. |
| 258 | Línea en blanco de separación. |
| 259 | Declara `run_demo`. |
| 260 | Docstring de `run_demo`. |
| 261 | Línea en blanco antes del cuerpo. |
| 262 | Imprime el título principal del ejercicio. |
| 263 | Imprime el mensaje de inicialización. |
| 264 | Crea un `DataStream`. |
| 265 | Imprime estadísticas sin procesadores. |
| 266 | Línea en blanco de separación lógica. |
| 267 | Crea el procesador numérico. |
| 268 | Imprime que se registra el procesador numérico. |
| 269 | Registra el procesador numérico en el stream. |
| 270 | Construye el stream de demostración. |
| 271 | Imprime el primer lote de datos. |
| 272 | Procesa el primer lote con solo el procesador numérico. |
| 273 | Imprime estadísticas tras el primer lote. |
| 274 | Línea en blanco de separación lógica. |
| 275 | Crea el procesador de texto. |
| 276 | Crea el procesador de logs. |
| 277 | Imprime que se registran los demás procesadores. |
| 278 | Registra el procesador de texto. |
| 279 | Registra el procesador de logs. |
| 280 | Imprime que se reenviará el mismo lote. |
| 281 | Procesa el mismo stream con los tres procesadores. |
| 282 | Imprime estadísticas actualizadas. |
| 283 | Línea en blanco de separación lógica. |
| 284 | Empieza el `print` multilínea sobre el consumo de datos. |
| 285 | Primera parte del mensaje de consumo. |
| 286 | Segunda parte del mensaje de consumo. |
| 287 | Cierra el `print` de consumo. |
| 288 | Consume tres salidas del procesador numérico. |
| 289 | Consume dos salidas del procesador de texto. |
| 290 | Consume una salida del procesador de logs. |
| 291 | Imprime estadísticas finales. |
| 292 | Línea en blanco de separación. |
| 293 | Línea en blanco de separación. |
| 294 | Comprueba si el archivo se ejecuta directamente. |
| 295 | Ejecuta la demo principal. |
