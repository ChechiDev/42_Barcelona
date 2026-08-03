# Defensa M05 ex1 - data_stream

## 1. Explicación del código

Este ejercicio implementa un flujo de datos (`DataStream`) que recibe una lista con elementos de tipos distintos y los envía al procesador adecuado usando polimorfismo.

La clase abstracta `DataProcessor` define la interfaz común de todos los procesadores:

- `validate(data)`: decide si ese procesador puede aceptar un dato.
- `ingest(data)`: guarda el dato ya procesado.
- `output()`: consume el dato más antiguo y devuelve una tupla `(rank, value)`.
- `get_total_processed()` y `get_data_len()` permiten imprimir estadísticas.
- `get_name()` devuelve el nombre visible del procesador.

Los procesadores concretos son:

- `NumericProcessor`: acepta `int`, `float` y listas compuestas solo por números. Excluye `bool`, aunque en Python `bool` hereda de `int`, para evitar tratar `True` o `False` como números del stream.
- `TextProcessor`: acepta `str` y listas compuestas solo por strings.
- `LogProcessor`: acepta diccionarios con claves y valores string, o listas de estos diccionarios. Si existen las claves `log_level` y `log_message`, formatea la salida como `LEVEL: message`.

`DataStream` mantiene una lista de procesadores registrados. En `process_stream`, recorre cada elemento recibido y pregunta a cada procesador si puede validarlo. El primer procesador compatible lo ingiere. Si ningún procesador puede procesar el elemento, se imprime el error requerido por el subject.

El flujo principal (`run_demo`) demuestra el escenario del enunciado de forma dinámica: recibe el stream y las cantidades de consumo desde fuera. Primero registra solo el procesador numérico, luego añade los procesadores de texto y logs, reprocesa el mismo stream, consume elementos con `output()` mediante `put_processor_outputs()` y muestra las estadísticas actualizadas.

La implementación cumple el subject porque:

- Define `DataStream` con `register_processor`, `process_stream` y `print_processors_stats`.
- Usa una interfaz común para procesadores mediante una clase abstracta.
- Permite añadir procesadores sin cambiar la lógica principal de `DataStream`.
- Imprime errores para datos no soportados.
- Muestra estadísticas de total procesado y elementos pendientes.
- Incluye un escenario reutilizable mediante `run_demo(...)`, sin datos de ejemplo hardcodeados en el archivo entregable.

## 2. Posibles preguntas de defensa

**¿Dónde está el polimorfismo en este ejercicio?**  
En que `DataStream` trabaja con objetos de tipo `DataProcessor` sin conocer su clase concreta. Solo llama a `validate` e `ingest`, y cada procesador implementa esas operaciones según su tipo de dato.

**¿Por qué `DataStream` no comprueba directamente si un elemento es `int`, `str` o `dict`?**  
Porque esa responsabilidad pertenece a cada procesador. Así el stream queda desacoplado: para añadir un nuevo tipo de dato basta con crear otro procesador y registrarlo.

**¿Qué ocurre si dos procesadores pueden validar el mismo dato?**  
Se usa el primero registrado que devuelve `True` en `validate`. El orden de registro define la prioridad.

**¿Qué ocurre si ningún procesador acepta un elemento?**  
`DataStream` imprime `DataStream error - Can't process element in stream: ...` y continúa con el resto del stream.

**¿Por qué se excluyen los booleanos del procesador numérico?**  
Porque en Python `bool` es una subclase de `int`, pero semánticamente `True` y `False` no son datos numéricos útiles para este procesador.

**¿Qué significan `get_total_processed()` y `get_data_len()`?**  
`get_total_processed()` devuelve todos los elementos ingeridos históricamente. `get_data_len()` devuelve cuántos elementos siguen almacenados y pendientes de consumir con `output()`.

**¿Qué hace `output()`?**  
Extrae el elemento más antiguo del procesador, devuelve su ranking de salida y el valor almacenado. Si no hay datos, lanza `IndexError`.

**¿Qué casos borde están cubiertos por los tests?**  
Validación de listas mixtas, listas vacías, exclusión de booleanos como números, logs inválidos, salida desde procesador vacío, errores de stream y estadísticas después de consumir datos.

**¿Qué comprobaciones de calidad se pudieron ejecutar?**  
En este entorno se confirmó `py_compile`. Según el recheck disponible, `pytest`, `flake8` y `mypy --strict` no están instalados, así que quedan como comprobación recomendada en un entorno completo.
