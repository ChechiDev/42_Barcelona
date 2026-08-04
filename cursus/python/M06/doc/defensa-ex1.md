# Defensa ex1 - Distillation

## 1. Explicación del código

Este ejercicio añade `alchemy/potions.py`, que combina funciones de elementos para crear pociones. `strength_potion()` usa el fuego y el agua del módulo raíz `elements.py`; `healing_potion()` usa tierra y aire de `alchemy/elements.py`.

`alchemy/__init__.py` amplía la interfaz pública del paquete: expone `strength_potion()` y crea el alias `heal` apuntando a `healing_potion()`. Así, `ft_distillation_0.py` prueba el acceso directo a `alchemy.potions`, mientras que `ft_distillation_1.py` prueba el acceso mediante `import alchemy`.

## 2. Preguntas de defensa

- **¿Qué demuestra este ejercicio?**  
  Que un módulo dentro de un paquete puede importar código de módulos cercanos y lejanos, y que el paquete puede reexportar funciones útiles.

- **¿Qué es `heal`?**  
  Es un alias público definido en `alchemy/__init__.py`: `healing_potion as heal`.

- **¿Por qué las pociones llaman a funciones de elementos en vez de duplicar strings?**  
  Porque mantiene un flujo reutilizable: si cambia una función de elemento, la poción usa automáticamente su valor actual.

- **¿Qué se valida con los tests?**  
  Que las salidas exactas coinciden con el subject y que `alchemy.strength_potion()` y `alchemy.heal()` están disponibles.
