# Defensa ex2: Memory Depths

## Explicación del código

`ex2/scope_mysteries.py` practica closures, ámbito léxico y `nonlocal` cuando hace falta reasignar estado cerrado.

- `mage_counter` crea un contador privado `count`; cada llamada incrementa y devuelve el total.
- `spell_accumulator` guarda `total_power` iniciado con `initial_power`; cada llamada suma el nuevo poder y devuelve el acumulado.
- `enchantment_factory` guarda el tipo de encantamiento y devuelve una función que lo aplica a un item con el formato `"tipo item"`.
- `memory_vault` crea un diccionario privado `memories` y devuelve dos closures: `store(key, value)` guarda y devuelve el valor, y `recall(key)` devuelve el valor guardado o `"Memory not found"`.

No se usa estado global mutable. Cada llamada a la factory crea su propio estado independiente. El bloque `main()` permite ejecutar el archivo directamente para ver una demo de contadores, acumuladores, factories y vault siguiendo los ejemplos del PDF, pero no introduce estado global ni cambia las APIs evaluables. No se usa Pydantic ni ninguna dependencia externa: el subject lo prohíbe y este ejercicio busca practicar closures y ámbito léxico.

El generador no está integrado en este ejercicio; si se usa un helper generator en el proyecto, es solo una herramienta auxiliar externa para documentación o ejemplos, no una pieza de runtime.

## Preguntas posibles de defensa

- **¿Qué es una closure?** Una función interna que recuerda variables del ámbito donde fue creada.
- **¿Por qué se usa `nonlocal` en el contador y acumulador?** Porque se reasignan variables cerradas (`count` y `total_power`).
- **¿Por qué no se usa `nonlocal` para el diccionario del vault?** Porque se muta el contenido del diccionario, no se reasigna la variable `memories`.
- **¿Qué devuelve `recall` si la clave no existe?** Exactamente `"Memory not found"`.
- **¿Por qué la demo directa es segura?** Porque se ejecuta solo bajo `if __name__ == "__main__"`; al importar el módulo para tests no se lanza.
- **¿Qué decisión SOLID aplica?** Cada factory encapsula su propio estado y expone una interfaz mínima.
