# Defensa ex1: Capabilities

## 1. Explicación del código

Este ejercicio amplía el modelo de criaturas añadiendo **capabilities** separadas de la clase base `Creature`.

- `HealCapability` define el contrato `heal()` para criaturas que pueden curarse.
- `TransformCapability` define `transform()`, `revert()` y mantiene el estado persistente `_is_transformed`.
- `Sproutling` y `Bloomelle` heredan de `Creature` y `HealCapability`: atacan y además pueden curarse.
- `Shiftling` y `Morphagon` heredan de `Creature` y `TransformCapability`: pueden transformarse, y su estado transformado cambia el resultado de `attack()`.
- `HealingCreatureFactory` y `TransformCreatureFactory` crean las dos nuevas familias, respetando la interfaz de `CreatureFactory` de ex0.
- `capacitor.py` demuestra cada familia usando las capacidades mediante `isinstance` contra las abstracciones de capability, no contra clases concretas.

Decisiones SOLID principales:

- **SRP**: `Creature` no se llena de métodos que no todas las criaturas necesitan; curar y transformar están en interfaces separadas.
- **ISP**: una criatura curativa no está obligada a implementar transformación, y una transformadora no está obligada a curar.
- **OCP**: se pueden añadir nuevas capabilities sin modificar la clase base `Creature`.
- **LSP**: las criaturas con capabilities siguen funcionando como `Creature`, porque mantienen `describe()` y `attack()`.
- **DIP**: las demos y estrategias dependen de abstracciones (`HealCapability`, `TransformCapability`) en vez de clases concretas.

## 2. Preguntas posibles de defensa

**¿Por qué no poner `heal()` y `transform()` directamente en `Creature`?**  
Porque no todas las criaturas tienen esas habilidades. Separarlas evita métodos vacíos o inválidos en clases que no los necesitan.

**¿Qué significa que la transformación tenga estado persistente?**  
Después de llamar a `transform()`, `_is_transformed` queda a `True` y `attack()` devuelve un ataque potenciado hasta que se llama a `revert()`.

**¿Por qué se usa herencia múltiple?**  
Para combinar el contrato común de `Creature` con una capability específica sin duplicar lógica ni contaminar la clase base.

**¿Cómo se demuestra la capability de curación?**  
`capacitor.py` crea criaturas con `HealingCreatureFactory`, comprueba que implementan `HealCapability` y llama a `heal()`.

**¿Cómo se demuestra la capability de transformación?**  
Se llama a `attack()`, luego `transform()`, después `attack()` otra vez para ver el cambio de estado, y finalmente `revert()`.

**¿Qué edge case importante cubre el diseño?**  
Una criatura sin una capability no debería recibir llamadas a métodos que no soporta; por eso la demo valida contra la capability abstracta.
