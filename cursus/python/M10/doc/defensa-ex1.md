# Defensa ex1: Higher Realm

## Explicación del código

`ex1/higher_magic.py` demuestra funciones de orden superior: funciones que reciben o devuelven otras funciones. Todas respetan el contrato de hechizo `spell(target: str, power: int) -> str`.

- `spell_combiner` recibe dos hechizos y devuelve una función que ejecuta ambos con el mismo `target` y `power`, devolviendo una tupla con los dos resultados.
- `power_amplifier` devuelve un wrapper que multiplica el poder antes de llamar al hechizo base.
- `conditional_caster` evalúa una condición; si es verdadera ejecuta el hechizo y si no devuelve exactamente `"Spell fizzled"`.
- `spell_sequence` devuelve una función que ejecuta una lista de hechizos en orden y devuelve una lista de resultados.

El estado necesario queda capturado por closures. El bloque `main()` permite ejecutar el archivo directamente y reproduce una demo alineada con los ejemplos del PDF, sin afectar al contrato público de las funciones. No se usa Pydantic ni librerías externas porque el subject no permite dependencias instaladas con `pip` y el objetivo aquí son funciones de orden superior.

No hay generador integrado: el comportamiento público son solo estas funciones retornadas. Si existe un helper generator en el proyecto, se trata como herramienta auxiliar externa de documentación o ejemplos, no como parte del ejercicio.

## Preguntas posibles de defensa

- **¿Qué es una función de orden superior?** Una función que recibe otra función como argumento o devuelve una función.
- **¿Dónde se usa closure?** En las funciones internas, que recuerdan `spell1`, `spell2`, `base_spell`, `multiplier`, `condition` o la lista `spells`.
- **¿Qué devuelve `conditional_caster` si falla la condición?** La cadena exacta `"Spell fizzled"`.
- **¿Se cambia el orden en `spell_sequence`?** No, se respeta el orden original de la lista.
- **¿La demo directa cambia la corrección?** No. `main()` solo imprime ejemplos al ejecutar el archivo; las funciones siguen siendo importables y testeables.
- **¿Qué decisión SOLID aplica?** Cada combinador tiene una responsabilidad concreta y depende del contrato callable, no de implementaciones concretas de hechizos.
