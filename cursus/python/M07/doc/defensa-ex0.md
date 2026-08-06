# Defensa ex0: Creature Factory

## 1. Explicación del código

Este ejercicio implementa el patrón **Abstract Factory** para crear familias de `Creature` sin que el script principal dependa de las clases concretas.

- `Creature` es una clase abstracta con estado común (`name` y `creature_type`), un método abstracto `attack()` y un método concreto `describe()`.
- `Flameling`, `Pyrodon`, `Aquabub` y `Torragon` son criaturas concretas. Cada una define su propio ataque.
- `CreatureFactory` define la interfaz común: `create_base()` y `create_evolved()` crean la criatura base y evolucionada de una familia.
- `FlameFactory` crea la familia de fuego y `AquaFactory` crea la familia de agua.
- `ex0/__init__.py` expone solo las fábricas, no las criaturas concretas. Así el usuario del paquete trabaja con abstracciones.
- `battle.py` usa las fábricas para imprimir acciones y hacer luchar a las criaturas base. La lógica no pregunta si una criatura es de fuego o agua: solo llama a `describe()` y `attack()`.

Decisiones SOLID principales:

- **SRP**: las criaturas saben describirse y atacar; las fábricas saben crear familias; el script solo demuestra el flujo.
- **OCP**: se puede añadir una nueva familia creando otra fábrica sin cambiar la lógica de batalla.
- **DIP**: `battle.py` depende de `CreatureFactory` y `Creature`, no de las clases concretas.
- **LSP**: cualquier criatura concreta puede usarse donde se espera una `Creature` porque implementa `attack()`.

## 2. Preguntas posibles de defensa

**¿Qué patrón se usa y por qué?**  
Abstract Factory, porque necesitamos crear familias relacionadas de objetos (`base` y `evolved`) mediante una interfaz común.

**¿Por qué `Creature` es abstracta?**  
Porque define el contrato común y obliga a que cada criatura concreta implemente su propio `attack()`.

**¿Qué ventaja tiene exponer solo las fábricas en `__init__.py`?**  
Evita acoplar el código externo a criaturas concretas y fuerza el uso del patrón pedido por el subject.

**¿Cómo fluye la información en `battle.py`?**  
El script recibe fábricas, crea criaturas con `create_base()` o `create_evolved()`, y después llama a métodos comunes (`describe()` y `attack()`).

**¿Cómo añadirías una familia nueva?**  
Crearía nuevas clases de criatura y una nueva fábrica que implemente `create_base()` y `create_evolved()`, sin modificar la batalla.

**¿Qué se ha probado?**  
La salida de `battle.py`, que los paquetes exponen fábricas y no criaturas concretas, y la compatibilidad con flake8 y mypy strict.
