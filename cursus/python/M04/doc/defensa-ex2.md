# Defensa ex2: Stream Management

## 1. Explicación del código

Este ejercicio trabaja con los tres flujos estándar del programa y con ficheros de texto: entrada estándar, salida estándar y salida de error.

El programa empieza en `main()`. Primero comprueba `sys.argv`: debe recibir exactamente un argumento además del nombre del script. Si no hay un fichero indicado, muestra el uso correcto y termina sin lanzar una excepción.

Cuando el argumento existe, `process_archive(sys.argv[1])` coordina el flujo principal:

1. Lee el fichero original.
2. Muestra su contenido.
3. Transforma el texto añadiendo `#` al final de cada línea.
4. Pregunta si se quiere guardar el resultado en otro fichero.

La lectura del fichero se hace en `read_file(filename)`. La llamada a `open(filename)` devuelve un objeto de fichero de texto, anotado como `typing.IO[str]`, sobre el que se usa `read()` para obtener todo el contenido. Si `open()` falla, se captura `OSError` y el error se imprime en `sys.stderr` mediante `print_error()`, siempre con el prefijo `[STDERR]`.

El cierre del fichero está dentro de un bloque `finally`. Esto es importante porque garantiza que `file.close()` se ejecuta aunque ocurra un problema después de abrir el fichero. Así se evita dejar recursos abiertos.

La transformación se realiza en `process_content(content)`. La función recorre el texto carácter por carácter. Cuando encuentra un salto de línea (`\n`), añade `#` justo antes de conservar ese salto de línea. Si el contenido no termina con salto de línea, también añade `#` al final de la última línea. Por eso cada línea transformada acaba marcada con `#`.

Para pedir el nombre del fichero de salida no se usa `input()`, porque no está permitido por el subject. En su lugar, el programa muestra el prompt con `print(..., end="")`, fuerza que se vea inmediatamente con `sys.stdout.flush()`, y después lee una línea con `sys.stdin.readline()`. La función `read_line()` elimina el `\n` final si existe.

El guardado es opcional. Si el usuario pulsa Enter sin escribir un nombre, el programa muestra `Not saving data.` y termina sin crear ningún fichero. Si se introduce un nombre, `save_content(filename, content)` abre el fichero en modo escritura con `open(filename, "w")`, escribe el contenido transformado con `write()` y cierra el fichero en un `finally`.

Si el fichero de salida no se puede abrir o escribir por un problema de sistema, se captura `OSError`, el error se envía a `sys.stderr` con `[STDERR]`, y `process_archive()` muestra `Data not saved.` por la salida estándar.

El código respeta las restricciones del ejercicio: usa `sys`, `sys.argv`, `sys.stdin.readline`, `sys.stdout.flush`, `sys.stderr`, `open`, `typing.IO`, `read`, `write`, `close`, `print`, `len` y manejo explícito de errores con `OSError`, sin usar `input()` ni imports no autorizados.

## 2. Posibles preguntas de defensa

**¿Para qué se usa `sys.argv`?**
Para leer los argumentos pasados al script desde la terminal. En este caso se espera un único argumento: el nombre del fichero que se quiere procesar.

**¿Por qué se comprueba `len(sys.argv) != 2`?**
Porque `sys.argv[0]` es el nombre del script y `sys.argv[1]` debe ser el fichero. Si la longitud no es 2, falta o sobra información.

**¿Por qué se usa `sys.stdin.readline()` en vez de `input()`?**
Porque `input()` no está autorizado en el subject. `sys.stdin.readline()` permite leer desde la entrada estándar directamente.

**¿Por qué se llama a `sys.stdout.flush()` después del prompt?**
Porque el prompt se imprime sin salto de línea. `flush()` fuerza que el texto aparezca antes de esperar la entrada del usuario.

**¿Qué diferencia hay entre `sys.stdout` y `sys.stderr`?**
`stdout` se usa para la salida normal del programa. `stderr` se usa para errores. Así se pueden separar resultados válidos de mensajes de error.

**¿Por qué los errores llevan el prefijo `[STDERR]`?**
Porque el subject pide un prefijo claro en los errores. Además facilita comprobar visualmente que ese mensaje es de error.

**¿Qué devuelve `open()`?**
Devuelve un objeto de fichero. En este ejercicio se anota como `typing.IO[str]` porque se trabaja con texto.

**¿Qué métodos se usan sobre el fichero?**
Se usa `read()` para leer todo el contenido, `write()` para guardar el texto transformado y `close()` para cerrar el recurso.

**¿Por qué se usa `try/finally` al cerrar ficheros?**
Porque garantiza que `close()` se ejecuta aunque ocurra un error después de abrir el fichero.

**¿Qué errores captura `OSError`?**
Errores del sistema relacionados con ficheros, por ejemplo fichero inexistente, permisos insuficientes o intentar abrir un directorio como fichero.

**¿Cómo se transforma el contenido?**
Se añade `#` al final de cada línea. Si una línea termina en `\n`, se inserta `#` antes de ese salto. Si la última línea no tiene `\n`, se añade `#` al final.

**¿Qué ocurre si el usuario no escribe nombre de salida?**
No se guarda nada. El programa muestra `Not saving data.` y termina correctamente.

**¿Qué ocurre si falla el guardado?**
El error de apertura se imprime en `sys.stderr` con `[STDERR]` y luego se muestra `Data not saved.` en la salida estándar.

**¿Por qué no se modifica el fichero original?**
Porque el fichero original se abre solo para lectura. El resultado transformado se guarda únicamente si el usuario indica otro nombre de fichero.

**¿Qué imports están autorizados y usados?**
Solo `sys` y `typing`, que son los necesarios para manejar argumentos, streams estándar y anotar el objeto de fichero como `typing.IO[str]`.
