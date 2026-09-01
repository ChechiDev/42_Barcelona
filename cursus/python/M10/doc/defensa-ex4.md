# Defensa ex4: Master's Tower

## Explicación del código

`ex4/decorator_mastery.py` demuestra decoradores, `functools.wraps`, validación, reintentos y `staticmethod`.

- `spell_timer` envuelve una función, imprime `Casting function_name...`, mide con `perf_counter` y después imprime `Spell completed in X.XXX seconds`.
- `power_validator(min_power)` crea un decorador que obtiene el argumento `power`; si es menor que el mínimo devuelve `"Insufficient power for this spell"`, si no ejecuta la función original.
- `retry_spell(max_attempts)` reintenta una función cuando lanza excepción; entre intentos imprime el mensaje de retry y, si todos fallan, devuelve `"Spell casting failed after max_attempts attempts"` con el número real.
- `MageGuild.validate_mage_name` es `@staticmethod` porque no necesita estado de instancia; acepta nombres de al menos 3 caracteres con solo letras y espacios.
- `MageGuild.cast_spell` usa `@power_validator(10)` y, si el poder es suficiente, devuelve `"Successfully cast spell_name with <power> power"`.

`wraps` conserva metadatos de la función original. El bloque `main()` permite ejecutar el archivo directamente para ver la demo de temporización, reintentos, validación de nombres y validación de poder con salidas alineadas con el PDF. No se usa Pydantic ni ninguna dependencia externa porque el subject prohíbe librerías instaladas con `pip` y los decoradores funcionan directamente sobre callables.

El generador no está integrado en este ejercicio; si existe como helper del proyecto, se trata como herramienta auxiliar para documentación o ejemplos, no como parte de la solución evaluable.

## Preguntas posibles de defensa

- **¿Por qué usar `wraps`?** Para conservar `__name__`, docstring y metadatos de la función decorada.
- **¿Cómo encuentra `power_validator` el poder?** Primero busca `power` en kwargs y, si no está, usa el último argumento posicional.
- **¿Qué devuelve si el poder es insuficiente?** Exactamente `"Insufficient power for this spell"`.
- **¿Cuándo imprime `retry_spell` el mensaje de retry?** Solo si falla un intento y aún quedan intentos disponibles.
- **¿Qué aporta la ejecución directa?** Permite defensa manual rápida con `python ex4/decorator_mastery.py`; al importar el módulo no se ejecuta la demo.
- **¿Qué decisión SOLID aplica?** Temporización, validación, reintentos y reglas del gremio están separados en componentes pequeños y reutilizables.
