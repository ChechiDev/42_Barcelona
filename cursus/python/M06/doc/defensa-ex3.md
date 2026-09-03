# Defensa ex3 - Avoid the Explosion

## 1. Explicación del código

Este ejercicio enseña dependencias circulares. En la parte segura, `light_spellbook.py` define los ingredientes permitidos y `light_spell_record()`. Para evitar el ciclo, importa `validate_ingredients()` dentro de la función, cuando ya se ha cargado el módulo. `light_validator.py` puede consultar `light_spell_allowed_ingredients()` y validar de forma case-insensitive si el texto contiene al menos un ingrediente permitido. La comprobación se ha separado en `has_allowed_ingredient()`, y `light_spellbook.py` usa `is_valid_validation()` para decidir si registra o rechaza el hechizo a partir del resultado del validador.

En la parte peligrosa, `dark_spellbook.py` y `dark_validator.py` se importan entre sí a nivel de módulo. Al importar `dark_spellbook`, Python intenta importar `dark_validator`, que intenta importar de nuevo desde un `dark_spellbook` todavía parcialmente inicializado. Por eso `ft_kaboom_1.py` falla intencionalmente con `ImportError` de import circular.

## 2. Preguntas de defensa

- **¿Qué es una dependencia circular?**  
  Ocurre cuando dos módulos se necesitan mutuamente durante la importación, antes de que alguno termine de inicializarse.

- **¿Cómo se evita en la versión light?**  
  Moviendo el import del validador dentro de `light_spell_record()`, retrasándolo hasta el momento de uso.

- **¿Qué otras soluciones existen?**  
  Extraer los datos comunes a un tercer módulo, cambiar la dirección de la dependencia, o pasar datos por parámetro.

- **¿Cómo decide el validador si algo es válido?**  
  `has_allowed_ingredient()` convierte el texto a minúsculas y comprueba si contiene algún ingrediente permitido. Después `validate_ingredients()` añade `VALID` o `INVALID` al mensaje.

- **¿Por qué existe `is_valid_validation()`?**  
  Para aislar la decisión de registro/rechazo y evitar un falso positivo: `INVALID` también termina en `VALID`, por eso se comprueba que acabe en `VALID` pero no en `INVALID`.

- **¿Por qué `ft_kaboom_1.py` no captura el error?**  
  Porque el subject quiere demostrar claramente la explosión por import circular mediante una excepción no capturada.
