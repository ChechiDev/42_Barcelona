# Defensa ex2: Abstract Strategy

## 1. Explicación del código

Este ejercicio implementa el patrón **Strategy** para elegir cómo actúa una criatura en combate sin meter condicionales de tipo en la lógica del torneo.

- `BattleStrategy` es la interfaz abstracta con `is_valid()` y `act()`.
- `NormalStrategy` es válida para cualquier `Creature` y solo llama a `attack()`.
- `AggressiveStrategy` es válida para criaturas con `TransformCapability`: llama a `transform()`, luego `attack()` y finalmente `revert()`.
- `DefensiveStrategy` es válida para criaturas con `HealCapability`: llama a `attack()` y después a `heal()`.
- `InvalidStrategyError` es una excepción dedicada para combinaciones inválidas de criatura y estrategia.
- `tournament.py` asocia cada fábrica con una estrategia. La función de torneo hace que cada oponente luche contra cada otro oponente una sola vez usando índices (`first_index + 1`).
- Si una estrategia no es válida para una criatura, `act()` lanza `InvalidStrategyError` y `run_tournament()` aborta el torneo de forma controlada con un mensaje claro.

Decisiones SOLID principales:

- **SRP**: cada estrategia contiene una política de combate concreta; el torneo solo organiza combates.
- **OCP**: añadir una nueva estrategia no requiere cambiar las criaturas ni la función principal del torneo.
- **ISP**: cada estrategia depende solo de la capability que necesita: transformar o curar.
- **DIP**: el torneo trabaja con `BattleStrategy` y `CreatureFactory`, no con implementaciones concretas.
- **LSP**: cualquier estrategia concreta puede usarse donde se espera una `BattleStrategy` porque implementa `is_valid()` y `act()`.

## 2. Preguntas posibles de defensa

**¿Qué problema resuelve Strategy aquí?**  
Permite cambiar el comportamiento de combate sin modificar las criaturas ni llenar el torneo de `if` para cada tipo.

**¿Qué diferencia hay entre `is_valid()` y `act()`?**  
`is_valid()` permite consultar si la estrategia sirve para una criatura. `act()` ejecuta la acción y, si la combinación es inválida, lanza una excepción clara.

**¿Por qué `AggressiveStrategy` llama a `revert()` al final?**  
Para dejar la criatura en un estado estable después del ataque y evitar que el estado transformado se filtre a acciones futuras.

**¿Cómo se gestionan combinaciones inválidas?**  
`_validate_or_raise()` comprueba `is_valid()` y lanza `InvalidStrategyError` con el nombre de la criatura y de la estrategia.

**¿Cómo evita el torneo repetir combates?**  
Usa un doble bucle donde el segundo empieza en `first_index + 1`, así cada pareja combate una sola vez.

**¿Qué se ha probado?**  
La salida de `tournament.py`, la validación de estrategias, la excepción dedicada, y los checks `flake8`, `mypy --strict` y `pytest`.
