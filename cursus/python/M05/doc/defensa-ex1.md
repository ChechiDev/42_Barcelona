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

`get_processors()` devuelve una copia de la lista interna de procesadores. Así se puede inspeccionar el registro desde fuera sin permitir que el código externo modifique directamente el estado interno de `DataStream`.

`print_processors_stats()` delega el formato de cada línea en `_format_processor_stats()`. Esta separación deja el método público centrado en el flujo de impresión y mueve la construcción del texto a un helper pequeño y fácil de probar.

El flujo principal (`main`) demuestra el escenario del enunciado. Construye el stream usando constantes cortas en mayúsculas y helpers reutilizables. Primero se registra solo el procesador numérico, luego se añaden los procesadores de texto y logs, se reprocesa el mismo stream, se consumen elementos con `output()` mediante `put_processor_outputs()` y se muestran las estadísticas actualizadas.

La implementación cumple el subject porque:

- Define `DataStream` con `register_processor`, `process_stream` y `print_processors_stats`.
- Usa una interfaz común para procesadores mediante una clase abstracta.
- Permite añadir procesadores sin cambiar la lógica principal de `DataStream`.
- Imprime errores para datos no soportados.
- Muestra estadísticas de total procesado y elementos pendientes.
- Incluye un escenario ejecutable mediante `main()`, con datos separados en constantes.

## 2. Posibles preguntas de defensa

**¿Dónde está el polimorfismo en este ejercicio?**  
En que `DataStream` trabaja con objetos de tipo `DataProcessor` sin conocer su clase concreta. Solo llama a `validate` e `ingest`, y cada procesador implementa esas operaciones según su tipo de dato.

**¿Por qué `DataStream` no comprueba directamente si un elemento es `int`, `str` o `dict`?**  
Porque esa responsabilidad pertenece a cada procesador. Así el stream queda desacoplado: para añadir un nuevo tipo de dato basta con crear otro procesador y registrarlo.

**¿Qué ocurre si dos procesadores pueden validar el mismo dato?**  
Se usa el primero registrado que devuelve `True` en `validate`. El orden de registro define la prioridad.

**¿Qué ocurre si ningún procesador acepta un elemento?**  
`DataStream` imprime `DataStream error - Can't process element in stream: ...` y continúa con el resto del stream.

**¿Por qué `get_processors()` devuelve una copia?**  
Para proteger la lista interna. Si devolviera la misma lista, un usuario podría añadir, borrar o reordenar procesadores sin pasar por `register_processor()`.

**¿Por qué existe `_format_processor_stats()`?**  
Para separar responsabilidades: `print_processors_stats()` controla cuándo imprimir y el helper sabe cómo construir una línea de estadísticas.

**¿Por qué se excluyen los booleanos del procesador numérico?**  
Porque en Python `bool` es una subclase de `int`, pero semánticamente `True` y `False` no son datos numéricos útiles para este procesador.

**¿Qué significan `get_total_processed()` y `get_data_len()`?**  
`get_total_processed()` devuelve todos los elementos ingeridos históricamente. `get_data_len()` devuelve cuántos elementos siguen almacenados y pendientes de consumir con `output()`.

**¿Qué hace `output()`?**  
Extrae el elemento más antiguo del procesador, devuelve su ranking de salida y el valor almacenado. Si no hay datos, lanza `IndexError`.

**¿Qué casos borde están cubiertos por los tests?**  
Validación de listas mixtas, listas vacías, exclusión de booleanos como números, logs inválidos, salida desde procesador vacío, errores de stream y estadísticas después de consumir datos.

**¿Qué comprobaciones de calidad se pudieron ejecutar?**  
QA final informado: `flake8 M05`, `mypy --strict M05` y `pytest M05/tests`, con 45 tests pasados.
