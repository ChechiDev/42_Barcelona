# Defensa ex1: Archive Creation

## 1. Explicación del código

Este ejercicio implementa un pequeño flujo de preservación de archivos:

1. El programa recibe por `sys.argv` el nombre del archivo que se quiere leer.
2. Abre el archivo con `open()` y guarda el resultado en una variable tipada como `typing.IO[str]`, es decir, un objeto de archivo de texto.
3. Lee el contenido con `read()`.
4. Muestra el contenido original.
5. Cierra el archivo con `close()` dentro de un `finally`, para asegurar que se cierra incluso si ocurre un error durante la lectura o la impresión.
6. Transforma el contenido añadiendo el carácter `#` al final de cada línea.
7. Muestra el contenido transformado.
8. Pide con `input()` un nombre de archivo de destino.
9. Si el usuario deja la entrada vacía, no guarda nada.
10. Si el usuario escribe un nombre, abre ese archivo con `open(filename, "w")`, escribe el contenido transformado con `write()` y lo cierra con `close()`.

La función `main()` valida que haya exactamente un argumento además del nombre del script. Para eso usa `len(sys.argv)`. Si no se cumple, imprime un mensaje de uso y termina sin intentar abrir ningún archivo.

La lectura se hace en `read_file()`. Primero se intenta abrir el archivo dentro de un `try`. Si `open()` falla, por ejemplo porque el archivo no existe o no hay permisos, se captura `OSError`, se muestra un mensaje claro y se devuelve `None`. Si el archivo se abre correctamente, el cierre queda protegido por `try/finally`.

La transformación está en `process_content()`. Recorre el texto carácter por carácter. Cuando encuentra un salto de línea (`\n`), añade `#\n`, así el `#` queda al final de esa línea. Si el archivo no termina con salto de línea, añade un `#` final para marcar también la última línea. Si el contenido está vacío, devuelve una cadena vacía.

El guardado opcional se hace en `process_archive()`. Después de mostrar el contenido transformado, el programa llama a `input("Enter new file name (or empty): ")`. Si el resultado es una cadena vacía, imprime `Not saving data.`. Si hay un nombre, llama a `save_content()`.

`save_content()` abre o reemplaza el archivo de destino usando modo escritura (`"w"`). También captura `OSError` si no puede abrir el archivo. Una vez abierto, escribe el contenido con `write()` y siempre cierra el archivo en un `finally`.

No se usan clases ni métodos abstractos porque el enunciado pide un script simple, procedural y centrado en funciones autorizadas. Añadir clases no aportaría claridad ni flexibilidad real en este caso; sería sobreingeniería para una secuencia lineal: leer, transformar, preguntar y guardar.

El código respeta las funciones e imports autorizados del subject: `import sys`, `sys.argv`, `len()`, `open()`, `import typing`, `typing.IO`, `read()`, `write()`, `close()`, `print()` e `input()`.

## 2. Posibles preguntas de defensa

**¿Para qué se usa `sys.argv`?**
Para leer los argumentos de línea de comandos. En este ejercicio, `sys.argv[1]` contiene el nombre del archivo de entrada.

**¿Por qué se comprueba `len(sys.argv) != 2`?**
Porque el programa espera exactamente dos elementos: el nombre del script y el nombre del archivo. Si falta o sobra un argumento, se muestra el uso correcto.

**¿Qué devuelve `open()`?**
Devuelve un objeto de archivo. Aquí se tipa como `typing.IO[str]` porque se trabaja con texto, no con bytes.

**¿Por qué se usa `typing.IO[str]`?**
Para expresar que la variable contiene un archivo de texto. Ayuda a documentar la intención y facilita el análisis estático de tipos.

**¿Qué hacen `read()`, `write()` y `close()`?**
`read()` obtiene el contenido del archivo, `write()` escribe texto en un archivo y `close()` libera el recurso abierto.

**¿Por qué se cierra el archivo en un `finally`?**
Porque `finally` se ejecuta aunque ocurra un error dentro del bloque `try`. Así se evita dejar archivos abiertos.

**¿Qué errores captura `OSError`?**
Errores del sistema relacionados con archivos, como archivo inexistente, permisos insuficientes o rutas inválidas.

**¿Cómo se añade el `#` al final de cada línea?**
La transformación reemplaza cada salto de línea por `#\n`. Si la última línea no termina en salto de línea, se añade un `#` al final.

**¿Qué pasa si el usuario no escribe nombre de archivo al guardar?**
`input()` devuelve una cadena vacía. El programa detecta eso, imprime `Not saving data.` y no crea ningún archivo nuevo.

**¿Qué pasa si el archivo de salida ya existe?**
Se abre con modo `"w"`, por lo que Python lo reemplaza con el nuevo contenido.

**¿Por qué no hay clases?**
Porque el problema no necesita estado complejo ni polimorfismo. Las funciones simples hacen el flujo más claro y cumplen mejor el objetivo del ejercicio.

**¿Por qué no hay métodos abstractos?**
Porque no hay una jerarquía de clases ni varias implementaciones intercambiables. Usarlos sería innecesario para este subject.

**¿Qué comportamiento se probó?**
Se cubren argumentos ausentes, archivo de entrada inexistente, lectura correcta, transformación del contenido, no guardar si la entrada está vacía y guardar si se proporciona un nombre.

**¿Por qué el código cumple el subject?**
Porque lee un archivo indicado por argumento, muestra el contenido, añade `#` al final de cada línea, muestra la transformación, pregunta si debe guardar y guarda el resultado solo si el usuario proporciona un nombre.
