# Defensa ex0: Space Station Data

## 1. Explicación del código

Este ejercicio define `SpaceStation`, un modelo de Pydantic v2 que hereda de `BaseModel`. Cada atributo describe un dato esperado de una estación espacial: identificador, nombre, tripulación, niveles de energía y oxígeno, fecha de mantenimiento, estado operativo y notas opcionales.

`Field` se usa para declarar restricciones cerca del propio dato: longitudes mínimas y máximas para strings, rangos numéricos para enteros y floats, y longitud máxima para `notes`. Esto centraliza la validación y evita escribir comprobaciones manuales repetidas.

El flujo principal es:

1. `build_station_data()` crea un diccionario de entrada.
2. `SpaceStation.model_validate()` convierte y valida esos datos.
3. Pydantic convierte automáticamente `last_maintenance` de string ISO a `datetime`.
4. Si los datos son válidos, `print_station()` muestra el modelo ya validado.
5. Si los datos son inválidos, Pydantic lanza `ValidationError` y `print_first_validation_error()` muestra el primer error de forma clara.

El caso inválido usa `crew_size=21`, que supera el máximo permitido de 20. Así se demuestra que las reglas declaradas con `Field` se aplican antes de que el programa acepte el objeto.

Decisiones SOLID: el modelo solo representa y valida datos de estación; las funciones auxiliares separan creación de datos, formato de estado, salida por pantalla y presentación de errores. Esto mantiene responsabilidades pequeñas y facilita probar cada parte.

## 2. Preguntas posibles de corrección

- **¿Por qué hereda de `BaseModel`?**
  Para que Pydantic pueda construir el objeto, convertir tipos y aplicar validaciones automáticamente.

- **¿Qué aporta `Field`?**
  Permite declarar restricciones como `min_length`, `max_length`, `ge` y `le` directamente en cada campo.

- **¿Dónde ocurre la conversión de fecha?**
  En `model_validate()`: Pydantic recibe un string ISO y lo convierte a `datetime` si el formato es válido.

- **¿Qué pasa con un valor fuera de rango?**
  No se crea un modelo válido; Pydantic lanza `ValidationError` con detalles del campo que falla.

- **¿Por qué `notes` es `str | None`?**
  Porque el enunciado indica que es opcional; puede omitirse o ser `None`, pero si existe debe cumplir el máximo de 200 caracteres.

- **¿Cómo se prueba el comportamiento?**
  Con tests que validan creación correcta, conversión automática de fecha y rechazo de `crew_size` mayor que 20.
