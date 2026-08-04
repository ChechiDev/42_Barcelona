# Defensa ex2 - The Great Transmutation

## 1. Explicación del código

Este ejercicio introduce `alchemy/transmutation/recipes.py` y la función `lead_to_gold()`. La receta construye el string final combinando aire, una poción de fuerza y fuego.

El archivo usa los dos estilos pedidos por el subject: un import absoluto (`from elements import create_fire`) para llegar al módulo raíz, y imports relativos (`from ..elements import create_air`, `from ..potions import strength_potion`) para acceder a módulos del paquete `alchemy`.

`alchemy/transmutation/__init__.py` reexporta `lead_to_gold()` para poder usar `alchemy.transmutation.lead_to_gold()`. Además, `alchemy/__init__.py` lo reexporta de nuevo para permitir `alchemy.lead_to_gold()`.

## 2. Preguntas de defensa

- **¿Qué es un import absoluto?**  
  Es una importación desde una ruta completa resoluble desde el directorio de ejecución o el paquete, por ejemplo `from elements import create_fire`.

- **¿Qué es un import relativo?**  
  Es una importación basada en la posición del módulo actual dentro del paquete, por ejemplo `from ..potions import strength_potion`.

- **¿Cuándo usarías cada uno?**  
  Absolutos para rutas claras desde fuera o módulos raíz; relativos para dependencias cercanas dentro del mismo paquete.

- **¿Por qué hay dos `__init__.py` implicados?**  
  Uno expone la receta desde `alchemy.transmutation`; el otro la expone desde el paquete principal `alchemy`.
