# M05 ex0: explicación línea por línea

Este documento vincula cada línea de `ex0/data_processor.py` con lo que hace.

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
| 14 | Docstring que explica la responsabilidad común de la clase. |
| 15 | Línea en blanco antes del método. |
| 16 | Declara el constructor de `DataProcessor`. |
| 17 | Docstring del constructor. |
| 18 | Línea en blanco antes del cuerpo. |
| 19 | Crea la lista interna `_items` para guardar datos procesados como strings. |
| 20 | Inicializa el ranking de salida en `0`. |
| 21 | Línea en blanco de separación. |
| 22 | Declara `get_data_len`, que devuelve cuántos datos quedan guardados. |
| 23 | Docstring de `get_data_len`. |
| 24 | Línea en blanco antes del cuerpo. |
| 25 | Devuelve la longitud de la lista interna `_items`. |
| 26 | Línea en blanco de separación. |
| 27 | Marca el siguiente método como abstracto. |
| 28 | Declara `validate`, que las subclases deben implementar. |
| 29 | Docstring de `validate`. |
| 30 | Línea en blanco; el método no tiene implementación por ser abstracto. |
| 31 | Marca el siguiente método como abstracto. |
| 32 | Declara `ingest`, que las subclases deben implementar. |
| 33 | Docstring de `ingest`. |
| 34 | Línea en blanco; el método no tiene implementación por ser abstracto. |
| 35 | Declara `output`, común para todos los procesadores. |
| 36 | Docstring de `output`. |
| 37 | Línea en blanco antes del cuerpo. |
| 38 | Comprueba si no hay elementos pendientes. |
| 39 | Lanza `IndexError` si se intenta extraer de un procesador vacío. |
| 40 | Guarda el ranking actual de salida. |
| 41 | Extrae y elimina el elemento más antiguo de `_items`. |
| 42 | Incrementa el ranking para la próxima salida. |
| 43 | Devuelve la tupla `(rank, item)`. |
| 44 | Línea en blanco de separación. |
| 45 | Declara el helper interno `_put_item`. |
| 46 | Docstring de `_put_item`. |
| 47 | Línea en blanco antes del cuerpo. |
| 48 | Añade un elemento ya procesado a `_items`. |
| 49 | Línea en blanco de separación. |
| 50 | Declara el helper interno `_put_items`. |
| 51 | Docstring de `_put_items`. |
| 52 | Línea en blanco antes del cuerpo. |
| 53 | Añade varios elementos ya procesados a `_items`. |
| 54 | Línea en blanco de separación. |
| 55 | Declara el helper interno `_put_scalar_or_list`. |
| 56 | Docstring de `_put_scalar_or_list`. |
| 57 | Línea en blanco antes del cuerpo. |
| 58 | Comprueba si el dato recibido es una lista. |
| 59 | Convierte cada elemento de la lista a `str` y los guarda. |
| 60 | Sale del método después de guardar una lista. |
| 61 | Convierte un dato individual a `str` y lo guarda. |
| 62 | Línea en blanco de separación. |
| 63 | Línea en blanco de separación. |
| 64 | Declara `NumericProcessor`, heredando de `DataProcessor`. |
| 65 | Docstring de `NumericProcessor`. |
| 66 | Línea en blanco antes del método. |
| 67 | Implementa `validate` para datos numéricos. |
| 68 | Docstring de la validación numérica. |
| 69 | Línea en blanco antes del cuerpo. |
| 70 | Comprueba si el dato recibido es una lista. |
| 71 | Devuelve `True` solo si todos los elementos de la lista son numéricos válidos. |
| 72 | Para datos individuales, devuelve si el dato es numérico válido. |
| 73 | Línea en blanco de separación. |
| 74 | Implementa `ingest` con el tipo específico `NumericData`. |
| 75 | Docstring de la ingesta numérica. |
| 76 | Línea en blanco antes del cuerpo. |
| 77 | Comprueba si el dato no es válido para este procesador. |
| 78 | Lanza `ValueError` si el dato numérico es incorrecto. |
| 79 | Línea en blanco antes de guardar. |
| 80 | Guarda el dato numérico, individual o lista, convertido a `str`. |
| 81 | Línea en blanco de separación. |
| 82 | Declara el helper interno `_is_numeric`. |
| 83 | Docstring de `_is_numeric`. |
| 84 | Línea en blanco antes del cuerpo. |
| 85 | Devuelve `True` para `int` o `float`, pero rechaza `bool`. |
| 86 | Línea en blanco de separación. |
| 87 | Línea en blanco de separación. |
| 88 | Declara `TextProcessor`, heredando de `DataProcessor`. |
| 89 | Docstring de `TextProcessor`. |
| 90 | Línea en blanco antes del método. |
| 91 | Implementa `validate` para texto. |
| 92 | Docstring de la validación de texto. |
| 93 | Línea en blanco antes del cuerpo. |
| 94 | Comprueba si el dato es un string. |
| 95 | Acepta el string individual. |
| 96 | Comprueba si el dato recibido es una lista. |
| 97 | Devuelve `True` solo si todos los elementos de la lista son strings. |
| 98 | Rechaza cualquier otro tipo de dato. |
| 99 | Línea en blanco de separación. |
| 100 | Implementa `ingest` con el tipo específico `TextData`. |
| 101 | Docstring de la ingesta de texto. |
| 102 | Línea en blanco antes del cuerpo. |
| 103 | Comprueba si el dato no es válido para este procesador. |
| 104 | Lanza `ValueError` si el dato de texto es incorrecto. |
| 105 | Línea en blanco antes de guardar. |
| 106 | Guarda texto individual o lista de textos. |
| 107 | Línea en blanco de separación. |
| 108 | Línea en blanco de separación. |
| 109 | Declara `LogProcessor`, heredando de `DataProcessor`. |
| 110 | Docstring de `LogProcessor`. |
| 111 | Línea en blanco antes del método. |
| 112 | Implementa `validate` para logs. |
| 113 | Docstring de la validación de logs. |
| 114 | Línea en blanco antes del cuerpo. |
| 115 | Comprueba si el dato es un diccionario. |
| 116 | Valida un único diccionario como entrada de log. |
| 117 | Comprueba si el dato recibido es una lista. |
| 118 | Valida que todos los elementos de la lista sean logs válidos. |
| 119 | Rechaza cualquier otro tipo de dato. |
| 120 | Línea en blanco de separación. |
| 121 | Implementa `ingest` con el tipo específico `LogData`. |
| 122 | Docstring de la ingesta de logs. |
| 123 | Línea en blanco antes del cuerpo. |
| 124 | Comprueba si el dato no es válido para este procesador. |
| 125 | Lanza `ValueError` si el dato de log es incorrecto. |
| 126 | Línea en blanco antes de guardar. |
| 127 | Comprueba si el dato válido es una lista de logs. |
| 128 | Formatea cada log de la lista y guarda todos los resultados. |
| 129 | Sale del método después de guardar una lista. |
| 130 | Formatea y guarda un único log. |
| 131 | Línea en blanco de separación. |
| 132 | Declara el helper interno `_is_log_entry`. |
| 133 | Docstring de `_is_log_entry`. |
| 134 | Línea en blanco antes del cuerpo. |
| 135 | Comprueba que el dato sea diccionario y empieza la validación de pares. |
| 136 | Comprueba que cada clave y cada valor sean strings. |
| 137 | Recorre todos los pares clave-valor del diccionario. |
| 138 | Cierra la expresión de validación y devuelve el resultado. |
| 139 | Línea en blanco de separación. |
| 140 | Declara el helper interno `_format_log_entry`. |
| 141 | Docstring de `_format_log_entry`. |
| 142 | Línea en blanco antes del cuerpo. |
| 143 | Obtiene el nivel del log o `""` si no existe. |
| 144 | Obtiene el mensaje del log o `""` si no existe. |
| 145 | Comprueba si hay nivel o mensaje para usar formato especial. |
| 146 | Devuelve el log formateado como `LEVEL: message`. |
| 147 | Si no hay claves conocidas, devuelve el diccionario como string. |
| 148 | Línea en blanco de separación. |
| 149 | Línea en blanco de separación. |
| 150 | Declara `print_validation`, helper para imprimir validaciones. |
| 151 | Docstring de `print_validation`. |
| 152 | Línea en blanco antes del cuerpo. |
| 153 | Imprime el dato probado y el resultado de `validate`. |
| 154 | Línea en blanco de separación. |
| 155 | Línea en blanco de separación. |
| 156 | Empieza la declaración multilínea de `print_outputs`. |
| 157 | Primer parámetro: procesador del que se extraerán datos. |
| 158 | Segundo parámetro: cantidad de datos a extraer. |
| 159 | Tercer parámetro: etiqueta que se imprimirá antes del valor. |
| 160 | Cierra la firma de `print_outputs`. |
| 161 | Docstring de `print_outputs`. |
| 162 | Línea en blanco antes del cuerpo. |
| 163 | Repite la extracción tantas veces como indique `amount`. |
| 164 | Llama a `output` y desempaqueta ranking y valor. |
| 165 | Imprime etiqueta, ranking y valor extraído. |
| 166 | Línea en blanco de separación. |
| 167 | Línea en blanco de separación. |
| 168 | Declara la demo del procesador numérico. |
| 169 | Docstring de la demo numérica. |
| 170 | Línea en blanco antes del cuerpo. |
| 171 | Crea una instancia de `NumericProcessor`. |
| 172 | Imprime el título de la sección numérica. |
| 173 | Imprime la validación de un número válido. |
| 174 | Imprime la validación de un string inválido para números. |
| 175 | Imprime el texto que anuncia una ingesta inválida. |
| 176 | Inicia el bloque `try` para capturar la excepción esperada. |
| 177 | Intenta ingerir un string inválido en el procesador numérico. |
| 178 | Captura el `ValueError` esperado. |
| 179 | Imprime el mensaje de la excepción capturada. |
| 180 | Crea una lista de números para la demo. |
| 181 | Imprime los datos que se van a procesar. |
| 182 | Ingiere la lista numérica válida. |
| 183 | Imprime que se extraerán tres valores. |
| 184 | Extrae e imprime tres valores numéricos. |
| 185 | Línea en blanco de separación. |
| 186 | Línea en blanco de separación. |
| 187 | Declara la demo del procesador de texto. |
| 188 | Docstring de la demo de texto. |
| 189 | Línea en blanco antes del cuerpo. |
| 190 | Crea una instancia de `TextProcessor`. |
| 191 | Imprime el título de la sección de texto. |
| 192 | Imprime la validación de un número inválido para texto. |
| 193 | Crea una lista de strings para la demo. |
| 194 | Imprime los textos que se van a procesar. |
| 195 | Ingiere la lista de texto válida. |
| 196 | Imprime que se extraerá un valor. |
| 197 | Extrae e imprime un valor de texto. |
| 198 | Línea en blanco de separación. |
| 199 | Línea en blanco de separación. |
| 200 | Declara la demo del procesador de logs. |
| 201 | Docstring de la demo de logs. |
| 202 | Línea en blanco antes del cuerpo. |
| 203 | Crea una instancia de `LogProcessor`. |
| 204 | Imprime el título de la sección de logs. |
| 205 | Imprime la validación de un string inválido para logs. |
| 206 | Empieza la lista de logs de ejemplo. |
| 207 | Empieza el primer diccionario de log. |
| 208 | Define el nivel `NOTICE` del primer log. |
| 209 | Define el mensaje del primer log. |
| 210 | Cierra el primer diccionario de log. |
| 211 | Empieza el segundo diccionario de log. |
| 212 | Define el nivel `ERROR` del segundo log. |
| 213 | Define el mensaje del segundo log. |
| 214 | Cierra el segundo diccionario de log. |
| 215 | Cierra la lista de logs. |
| 216 | Imprime los logs que se van a procesar. |
| 217 | Ingiere la lista de logs válida. |
| 218 | Imprime que se extraerán dos valores. |
| 219 | Extrae e imprime dos logs formateados. |
| 220 | Línea en blanco de separación. |
| 221 | Línea en blanco de separación. |
| 222 | Declara `run_demo`, punto de entrada de la demostración. |
| 223 | Docstring de `run_demo`. |
| 224 | Línea en blanco antes del cuerpo. |
| 225 | Imprime el título principal del ejercicio. |
| 226 | Ejecuta la demo del procesador numérico. |
| 227 | Ejecuta la demo del procesador de texto. |
| 228 | Ejecuta la demo del procesador de logs. |
| 229 | Línea en blanco de separación. |
| 230 | Línea en blanco de separación. |
| 231 | Comprueba si el archivo se está ejecutando directamente. |
| 232 | Ejecuta la demo principal cuando el archivo es el programa principal. |
