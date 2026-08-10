# Defensa ex2: Space Crew Management

## 1. Explicación del código

Este ejercicio usa modelos anidados de Pydantic. `CrewMember` representa a una persona de la tripulación y `SpaceMission` representa una misión que contiene una lista de `CrewMember` en el campo `crew`.

`Rank` es un `Enum` con los rangos permitidos: `cadet`, `officer`, `lieutenant`, `captain` y `commander`. Esto evita rangos arbitrarios y permite comparar valores de forma clara en las reglas de negocio.

Cada modelo hereda de `BaseModel` y usa `Field` para validaciones simples: longitudes de texto, rangos de edad, años de experiencia, duración, presupuesto y tamaño mínimo/máximo de tripulación. Pydantic valida también los modelos anidados: al validar una `SpaceMission`, valida cada elemento de `crew` como `CrewMember`.

`SpaceMission` usa `@model_validator(mode="after")` para comprobar reglas que dependen de toda la misión:

1. `mission_id` debe empezar por `M`.
2. Debe existir al menos un `Commander` o `Captain`.
3. Si la misión dura más de 365 días, al menos el 50% de la tripulación debe tener 5 o más años de experiencia.
4. Todos los miembros deben estar activos.

El flujo principal construye una tripulación válida, valida una misión y la imprime. Después crea una misión inválida sin rango de mando, captura el `ValidationError` y muestra el mensaje esperado.

La conversión automática aparece en `launch_date`: el diccionario contiene un string ISO y Pydantic lo convierte a `datetime`. También valida y mantiene los rangos como miembros del enum `Rank`.

Decisiones SOLID: `CrewMember` tiene la responsabilidad de validar datos de una persona; `SpaceMission` valida reglas de misión; `has_command_rank()` y `has_expert_crew()` separan condiciones de negocio reutilizables y testeables. La dependencia principal está en modelos y tipos pequeños, no en lógica mezclada dentro del `main()`.

## 2. Preguntas posibles de corrección

- **¿Qué significa que los modelos sean anidados?**
  Que `SpaceMission` contiene una lista de objetos `CrewMember`, y Pydantic valida cada miembro junto con la misión.

- **¿Por qué usar `model_validator` en `SpaceMission`?**
  Porque las reglas importantes dependen de varios campos o de toda la lista de tripulación, no de un único atributo.

- **¿Cómo se comprueba que hay mando en la misión?**
  `has_command_rank()` busca si algún miembro tiene rango `CAPTAIN` o `COMMANDER`.

- **¿Cómo se calcula el 50% de experiencia?**
  `has_expert_crew()` cuenta miembros con al menos 5 años de experiencia y comprueba `experienced_count * 2 >= len(crew)`.

- **¿Qué pasa si un tripulante está inactivo?**
  La validación de misión falla y Pydantic devuelve un `ValidationError` con el mensaje “All crew members must be active”.

- **¿Qué cubren los tests?**
  Validan modelos anidados, ID de misión, existencia de mando, experiencia suficiente en misiones largas, tripulación activa y ejecución directa del script.
