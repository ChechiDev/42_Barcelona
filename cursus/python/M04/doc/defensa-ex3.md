# Defensa ex3: Vault Security

## 1. Explicación del código

El ejercicio implementa `secure_archive(filename, action="read", content="")`, una función que accede a archivos de forma segura para leer o escribir.

La función siempre devuelve una tupla de dos elementos:

- `(True, texto)` si la operación funciona.
- `(False, mensaje_de_error)` si ocurre un error de sistema al abrir, leer o escribir el archivo.

Para leer, se usa la acción por defecto `"read"`. La función abre el archivo con `with open(filename) as file:` y devuelve el contenido con `file.read()`.

Para escribir, se pasa la acción `"write"`. La función abre el archivo con `with open(filename, "w") as file:`, escribe `content` con `file.write(content)` y devuelve el mensaje `"Content successfully written to file"`.

El punto central del ejercicio es el uso de `with`, que es un context manager. Esto garantiza que el archivo se cierre automáticamente al salir del bloque, tanto si la operación termina bien como si ocurre un error. Por eso este ejercicio usa `with` en lugar de escribir manualmente un `try/finally`: el objetivo del subject es practicar el cierre automático y seguro de recursos sin tener que llamar a `close()` explícitamente.

Los errores se capturan con `except OSError as e`. `OSError` cubre fallos habituales de archivos, como rutas inexistentes, permisos insuficientes o problemas del sistema operativo. La variable `e` contiene el error original y se convierte a texto para devolverlo en la tupla.

El archivo no usa imports. Esto respeta la restricción del subject: las operaciones relevantes se limitan a `open()`, `read()`, `write()` y `print()`.

La función `main()` muestra una demo con cuatro casos:

1. Leer un archivo inexistente.
2. Leer `/etc/master.passwd`, que puede fallar distinto según el sistema.
3. Leer `ancient_fragment.txt`.
4. Escribir ese contenido en `new_fragment.txt`.

En macOS, `/etc/master.passwd` suele existir pero no ser accesible, por eso puede devolver `Errno 13 Permission denied`. En Linux puede no existir, por eso puede devolver `Errno 2 No such file or directory`. Ambas respuestas son correctas porque dependen del entorno, no de la lógica del programa.

`new_fragment.txt` es un archivo generado por la demo. No forma parte del código fuente ni de los archivos a entregar; es una salida producida al ejecutar el programa para demostrar que la escritura funciona.

## 2. Posibles preguntas de defensa

### ¿Qué devuelve `secure_archive`?

Devuelve una tupla `(bool, str)`. El booleano indica éxito o fallo, y el string contiene el contenido leído, el mensaje de éxito al escribir, o el mensaje de error.

### ¿Qué acciones soporta la función?

Soporta lectura por defecto con `"read"` y escritura con `"write"`. Si la acción es `"write"`, escribe el contenido recibido; en caso contrario intenta leer el archivo.

### ¿Por qué se usa `with open(...) as file`?

Porque `with` gestiona el recurso automáticamente. Al salir del bloque, Python cierra el archivo aunque haya ocurrido un error.

### ¿Por qué no se usa `try/finally` para cerrar el archivo?

Porque el objetivo del ejercicio es practicar context managers. `with` expresa mejor la intención, evita olvidarse de cerrar el archivo y reduce código manual.

### ¿Qué captura `except OSError as e`?

Captura errores relacionados con operaciones de sistema y archivos, como archivo inexistente, permisos insuficientes o fallos al abrir/escribir. `e` es el objeto de error original.

### ¿Por qué puede cambiar el resultado de `/etc/master.passwd`?

Porque depende del sistema operativo. Si el archivo existe pero no hay permisos, aparece `Errno 13`. Si no existe, aparece `Errno 2`. Los dos casos demuestran que el error se gestiona correctamente.

### ¿Se respetan las funciones autorizadas?

Sí. El código no importa módulos y solo usa las operaciones necesarias del subject: abrir archivos, leer, escribir y mostrar la demo con `print()`.

### ¿Qué demuestra la salida de la demo?

Demuestra que la función devuelve errores controlados, puede leer un archivo válido y puede escribir el contenido leído en un nuevo archivo.

### ¿Por qué `new_fragment.txt` no se entrega?

Porque es una salida generada al ejecutar el programa. El subject pide entregar `ft_vault_security.py`; `new_fragment.txt` solo sirve para comprobar que la escritura funciona.

### ¿Qué pasa si la lectura de `ancient_fragment.txt` falla?

`secure_archive` devuelve `(False, mensaje_de_error)`. En la demo, si eso ocurre, se escribe una cadena vacía en `new_fragment.txt` para mantener la ejecución controlada.
