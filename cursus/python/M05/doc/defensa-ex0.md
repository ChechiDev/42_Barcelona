# Defensa ex0: Data Processor

## 1. Explicación del código

Este ejercicio crea una arquitectura común para procesar distintos tipos de datos usando clases abstractas.

- `DataProcessor` hereda de `ABC` y define la interfaz común:
  - `validate(self, data: Any) -> bool`: comprueba si un dato es válido para el procesador.
  - `ingest(self, data: Any) -> None`: ingiere datos válidos y los guarda internamente.
  - `output(self) -> tuple[int, str]`: extrae el dato más antiguo guardado y devuelve su rango junto con el valor.
- `DataProcessor` no se puede instanciar directamente porque `validate` e `ingest` son métodos abstractos.
- La cola interna `_items` guarda todos los valores ya procesados como `str`.
- `_next_output_rank` empieza en `0` y aumenta cada vez que se llama a `output`, de forma que cada salida tiene un rango asociado.
- `get_data_len` permite consultar cuántos elementos quedan pendientes.
- Los helpers `_put_item`, `_put_items` y `_put_scalar_or_list` están en la clase base porque el almacenamiento es común a todos los procesadores; así las subclases solo se ocupan de validar y convertir/formatear sus datos.

Procesadores concretos:

- `NumericProcessor` acepta `int`, `float` y listas de `int | float`.
  - Rechaza `bool`, aunque en Python `bool` hereda de `int`, para evitar aceptar `True` o `False` como números.
  - Convierte cada número a `str` antes de almacenarlo.
- `TextProcessor` acepta `str` y listas de `str`.
  - Guarda los textos sin modificarlos.
- `LogProcessor` acepta diccionarios con claves y valores `str`, o listas de esos diccionarios.
  - Si existen las claves `log_level` y/o `log_message`, formatea la salida como `LEVEL: message`.
  - Si el diccionario no contiene esas claves pero sigue siendo válido, usa `str(entry)`.
  - La ingesta de un único diccionario y la ingesta de una lista comparten la misma validación; en ambos casos cada entrada se almacena como un elemento independiente.

Flujo principal:

1. El usuario puede llamar a `validate` para comprobar si los datos son adecuados.
2. Si llama directamente a `ingest` con datos inválidos, el método vuelve a validar y lanza `ValueError`.
3. Los datos válidos se almacenan separados usando los helpers comunes de `DataProcessor`, manteniendo orden FIFO.
4. `output` extrae y elimina el elemento más antiguo; si no hay datos, lanza `IndexError`.

La función `run_demo(...)` permite ejecutar una demostración dinámica: recibe desde fuera los datos de prueba, los valores inválidos y las cantidades de salida. Así el código del ejercicio no contiene datos de ejemplo hardcodeados.

## 2. Posibles preguntas de corrección y respuestas

**¿Por qué `DataProcessor` es abstracta?**  
Porque define una interfaz común, pero no sabe cómo validar ni ingerir datos concretos. Cada subclase implementa esa lógica.

**¿Qué garantiza `validate`?**  
Devuelve `True` solo si el dato tiene la forma esperada por ese procesador. Su firma usa `Any` porque puede recibir cualquier cosa.

**¿Por qué `ingest` también llama a `validate`?**  
Para proteger la clase si el usuario no valida antes. Así los datos inválidos no llegan al almacenamiento interno.

**¿Por qué `_put_items` está en `DataProcessor` y no repetido en cada subclase?**  
Porque almacenar una lista de cadenas es comportamiento compartido. Centralizarlo evita duplicación y no cambia el comportamiento externo.

**¿Qué excepción se lanza con datos inválidos?**  
Cada procesador lanza un `ValueError` con un mensaje específico: `Improper numeric data`, `Improper text data` o `Improper log data`.

**¿Por qué `output` puede lanzar `IndexError`?**  
Porque extraer de un procesador vacío es un error de índice lógico: no existe ningún elemento pendiente.

**¿Qué significa que la salida sea FIFO?**  
Que se devuelve primero el dato que fue almacenado primero. Se implementa con `pop(0)` sobre la lista interna.

**¿Qué representa el rango devuelto por `output`?**  
Es el número de procesamiento dentro de ese procesador. Empieza en `0` y aumenta después de cada extracción.

**¿Por qué los números se almacenan como cadenas?**  
El subject pide que `NumericProcessor` convierta los datos numéricos a `str` antes de guardarlos para su extracción.

**¿Por qué se rechaza `bool` en `NumericProcessor`?**  
Aunque `bool` es una subclase de `int` en Python, conceptualmente no es un dato numérico para este procesador.

**¿Una lista vacía es válida?**  
Sí. `all(...)` sobre una lista vacía devuelve `True`; ingerirla simplemente no añade elementos.

**¿Qué forma debe tener un log válido?**  
Debe ser un `dict` donde todas las claves y todos los valores sean `str`, o una lista de diccionarios con esa misma regla.

**¿Por qué `LogProcessor` usa `entry.get(...)`?**  
Para poder formatear entradas con `log_level` y `log_message` sin fallar si alguna clave no existe.

**¿Qué comportamiento se ha comprobado en tests/revisión?**  
Clase abstracta, validaciones válidas e inválidas, excepciones en ingesta inválida, orden FIFO, rangos, salida en procesador vacío, `LogProcessor` con un único `dict` de entrada y ejecución dinámica de `run_demo(...)` con datos inyectados desde tests.

**¿Cumple el subject?**  
Sí: hay una clase abstracta común, tres procesadores especializados, métodos `validate`, `ingest` y `output`, almacenamiento separado, conversión a `str` cuando corresponde y pruebas/demostración de casos válidos e inválidos.
