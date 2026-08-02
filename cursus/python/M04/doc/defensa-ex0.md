# Defensa ex0: ft_ancient_text

## 1. Explicación del código

Este ejercicio implementa un pequeño programa similar a `cat`: recibe el nombre de un archivo por línea de comandos, lo abre, muestra su contenido y añade los mensajes de cabecera, separación y cierre pedidos por el subject.

El programa empieza en `main()`. Primero comprueba `len(sys.argv)`: `sys.argv` es la lista de argumentos recibidos por el script. En este caso debe tener exactamente dos elementos: el nombre del programa y la ruta del archivo. Si no se cumple, se imprime:

```text
Usage: ft_ancient_text.py <file>
```

Cuando hay un argumento válido, `main()` llama a `display_file(sys.argv[1])`. Esa función imprime la cabecera:

```text
=== Cyber Archives Recovery ===
Accessing file '<file>'
```

Después intenta abrir el archivo con `open(filename)`. La función `open()` devuelve un objeto de archivo, concretamente un objeto de tipo `TextIOWrapper` en modo texto por defecto. Ese objeto permite llamar a métodos como `.read()` para leer el contenido y `.close()` para cerrar el recurso.

Si `open()` falla, por ejemplo porque el archivo no existe o no hay permisos, Python lanza una excepción `OSError` o una subclase suya. El programa la captura con `except OSError as error` e imprime el mensaje con el formato pedido:

```text
Error opening file '<file>': <error>
```

Si el archivo se abre correctamente, el programa imprime `---`, lee todo el contenido con `file.read()` y lo muestra con `print(..., end="")`. Se usa `end=""` para no añadir un salto de línea extra después del contenido leído. Luego imprime otro `---` y cierra el archivo.

El cierre se hace dentro de un bloque `finally`. Esto garantiza que `file.close()` se ejecuta aunque ocurra un error durante la lectura o impresión. No se usa `with open(...) as file` porque el subject autoriza explícitamente `open()`, `read()` y `close()`, y el objetivo del ejercicio es practicar el cierre manual del archivo.

Casos importantes cubiertos:

- Sin argumentos: muestra el mensaje de uso.
- Archivo inexistente: captura `OSError` y muestra el error.
- Archivo inaccesible: también queda cubierto por `OSError`.
- Archivo válido: imprime cabecera, separadores, contenido y mensaje de cierre.
- Contenido con salto final: no se duplica el salto porque se usa `end=""`.

## 2. Posibles preguntas de defensa

**¿Qué contiene `sys.argv`?**
Una lista con los argumentos de línea de comandos. `sys.argv[0]` es el nombre del script y `sys.argv[1]` es el archivo cuando el usuario lo proporciona.

**¿Por qué se comprueba `len(sys.argv) != 2`?**
Porque el programa necesita exactamente un argumento además del nombre del script: la ruta del archivo.

**¿Qué devuelve `open()`?**
Devuelve un objeto de archivo. En modo texto, normalmente es un `TextIOWrapper`, que permite leer con `.read()` y cerrar con `.close()`.

**¿Por qué se captura `OSError`?**
Porque los errores al abrir archivos, como archivo inexistente o permiso denegado, pertenecen a `OSError` o sus subclases.

**¿Por qué no se usa `with open(...)`?**
Porque el subject lista `open()`, `read()` y `close()` como funciones autorizadas, y esta solución muestra explícitamente el cierre manual con `close()`.

**¿Para qué sirve el `finally`?**
Para asegurar que el archivo se cierra siempre después de abrirse correctamente, incluso si ocurre un problema durante la lectura.

**¿Por qué `print(file.read(), end="")`?**
Porque `read()` ya devuelve el contenido con sus saltos de línea originales. `end=""` evita añadir un salto extra que cambiaría el formato esperado.

**¿Qué pasa si el archivo está vacío?**
Se imprimirán la cabecera y los dos separadores. Entre ellos no habrá contenido, y luego se imprimirá el mensaje de cierre.

**¿El archivo se cierra si `open()` falla?**
No, porque no hay ningún archivo abierto que cerrar. El programa imprime el error y termina la función.

**¿Cómo se verifica que cumple el subject?**
La salida coincide con los formatos indicados: uso sin argumentos, error al abrir y lectura correcta con cabecera, separadores, contenido y mensaje de cierre.
