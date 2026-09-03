# Defensa ex0 - The Alembic

## 1. Explicación del código

Este ejercicio demuestra varias formas de importar módulos. `elements.py` define `create_fire()` y `create_water()`. Dentro del paquete `alchemy`, `alchemy/elements.py` define `create_earth()` y `create_air()`.

Los scripts `ft_alembic_0.py` a `ft_alembic_5.py` prueban importaciones distintas: `import elements`, `from elements import ...`, importación directa de `alchemy.elements`, y acceso a la interfaz pública del paquete `alchemy`. La clave está en `alchemy/__init__.py`: para este ejercicio reexporta `create_air`, por eso `alchemy.create_air()` funciona, pero no reexporta `create_earth()`. Aunque el paquete acumula más nombres públicos en ejercicios posteriores, `alchemy.create_earth()` sigue sin existir en la interfaz pública. En `ft_alembic_4.py` ese fallo es intencional y debe acabar en `AttributeError`.

## 2. Preguntas de defensa

- **¿Qué diferencia hay entre `import elements` y `from elements import create_water`?**  
  Con `import elements` accedo con el prefijo `elements.create_fire()`. Con `from ... import ...` importo directamente el nombre y llamo `create_water()`.

- **¿Para qué sirve `__init__.py`?**  
  Inicializa el paquete y define qué nombres se exponen desde `import alchemy` o `from alchemy import ...`.

- **¿Por qué `create_earth()` existe pero `alchemy.create_earth()` falla?**  
  Porque la función existe en `alchemy/elements.py`, pero no se reexporta en `alchemy/__init__.py`.

- **¿Que `alchemy/__init__.py` tenga funciones de ejercicios posteriores cambia ex0?**  
  No. El requisito importante de ex0 se mantiene: `create_air()` está disponible desde `alchemy`, pero `create_earth()` no.

- **¿El error de mypy en `ft_alembic_4.py` es un problema?**  
  No en este ejercicio: es intencional para demostrar que `create_earth` no forma parte de la API pública de `alchemy`.
