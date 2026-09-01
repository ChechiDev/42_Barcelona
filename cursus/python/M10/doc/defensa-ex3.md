# Defensa ex3: Ancient Library

## Explicación del código

`ex3/functools_artifacts.py` usa herramientas de `functools` y `operator` según el subject.

- `spell_reducer` selecciona una operación (`add`, `multiply`, `max`, `min`) y aplica `functools.reduce`. Si la lista está vacía devuelve `0`; si la operación no existe lanza `ValueError`.
- `partial_enchanter` recibe una función base `(power, element, target)` y devuelve partials para `fire`, `ice` y `lightning`, todos con `power=50`.
- `memoized_fibonacci` usa `@lru_cache` para memorizar resultados; acepta `n >= 0` y lanza `ValueError` en negativos.
- `spell_dispatcher` devuelve una función `singledispatch`: `int` produce daño, `str` encantamiento, `list` multi-cast y cualquier otro tipo `"Unknown spell type"`.

El dispatch queda separado en funciones registradas para mantener claridad. El bloque `main()` permite ejecutar el archivo directamente y enseña `reduce`, Fibonacci cacheado y `singledispatch` con ejemplos equivalentes al PDF. No se usa Pydantic ni librerías externas: además de estar prohibidas por el subject, serían innecesarias para practicar `functools` y `operator`.

No hay generador integrado; solo existen los helpers pedidos por el PDF y la documentación del ejercicio. Cualquier helper generator del repositorio queda tratado como herramienta auxiliar de documentación o creación de ejemplos, nunca como dependencia de runtime.

## Preguntas posibles de defensa

- **¿Por qué `spell_reducer([])` devuelve `0`?** Es el comportamiento definido para una lista vacía y evita llamar a `reduce` sin valor inicial.
- **¿Qué pasa con una operación desconocida?** Se lanza `ValueError` para señalar un uso inválido.
- **¿Qué aporta `partial`?** Crea funciones nuevas con argumentos prefijados, dejando solo el `target` pendiente.
- **¿Qué aporta `lru_cache` en Fibonacci?** Evita recalcular subproblemas repetidos.
- **¿Qué demuestra la ejecución directa?** Que los helpers se pueden probar manualmente con los casos del PDF sin mezclar esa demo con la lógica principal.
- **¿Qué decisión SOLID aplica?** La selección de operaciones y los handlers de dispatch están aislados, facilitando extender tipos u operaciones sin mezclar responsabilidades.
