# Defensa ex0: Lambda Sanctum

## Explicación del código

`ex0/lambda_spells.py` implementa cuatro helpers independientes sobre listas:

- `artifact_sorter` devuelve una lista nueva ordenada por `power` de mayor a menor usando `sorted` y una `lambda` como clave.
- `power_filter` conserva solo los magos con `power >= min_power` usando `filter`.
- `spell_transformer` transforma cada hechizo en el formato exacto `"* hechizo *"` usando `map`.
- `mage_stats` calcula `max_power`, `min_power` y `avg_power`; la media se redondea a 2 decimales. Si la lista está vacía devuelve poderes a `0` y media `0.0`.

El flujo es simple: los datos entran como listas de diccionarios o strings, se procesan sin modificar la entrada original y se devuelve una nueva estructura. El bloque `main()` permite ejecutar el archivo directamente y muestra una demo con datos equivalentes a los ejemplos del PDF, pero la lógica evaluable sigue estando en las funciones reutilizables. No se usa Pydantic ni librerías externas: el subject prohíbe dependencias instaladas con `pip` y este módulo se centra en patrones funcionales básicos.

No hay generador integrado en este ejercicio: cualquier helper generator del proyecto es solo una ayuda externa para crear/extraer material de documentación o ejemplos, no una dependencia del comportamiento requerido por el subject.

## Preguntas posibles de defensa

- **¿Por qué usar `lambda` aquí?** Porque el ejercicio pide practicar `lambda` con `sorted`, `filter`, `map`, `min`, `max`, `sum`, `len` y `round`.
- **¿`artifact_sorter` modifica la lista original?** No. `sorted` crea y devuelve una lista nueva.
- **¿Qué pasa si `mages` está vacío en `mage_stats`?** Se evita dividir por cero y se devuelve `{"max_power": 0, "min_power": 0, "avg_power": 0.0}`.
- **¿Cómo se calcula la media?** Sumando los poderes, dividiendo por el número de magos y aplicando `round(..., 2)`.
- **¿Para qué sirve el `main()`?** Solo para demostrar la salida al ejecutar `python ex0/lambda_spells.py`; los tests importan y validan las funciones.
- **¿Qué decisión SOLID aplica?** Cada función tiene una única responsabilidad y no mezcla entrada/salida, validación externa ni demostraciones.
