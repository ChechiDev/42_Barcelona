# Defensa ex1: Alien Contact Logs

## 1. Explicación del código

Este ejercicio define un `Enum` llamado `ContactType` con los tipos permitidos de contacto: `radio`, `visual`, `physical` y `telepathic`. El modelo `AlienContact` hereda de `BaseModel` y usa `Field` para validar restricciones básicas: longitudes, rangos numéricos y límites de texto.

Además de las validaciones de campo, el ejercicio usa `@model_validator(mode="after")` en `validate_contact_rules()`. Este validador se ejecuta cuando Pydantic ya ha convertido y validado los campos individuales, por lo que puede trabajar con tipos finales como `datetime`, `ContactType`, `float` e `int`.

Las reglas de negocio son:

1. `contact_id` debe empezar por `AC`.
2. Un contacto físico debe estar verificado.
3. Un contacto telepático necesita al menos 3 testigos.
4. Una señal mayor que 7.0 debe incluir mensaje recibido.

El flujo del programa crea un contacto válido con `model_validate()` y después intenta crear uno inválido. Cuando una regla falla, el validador lanza `ValueError`; Pydantic lo envuelve como `ValidationError`, que se captura para mostrar el mensaje al usuario.

Pydantic también realiza conversión automática: por ejemplo, el string de `timestamp` se transforma en `datetime`, y el valor de `contact_type` queda representado por el enum `ContactType`.

Decisiones SOLID: `ContactType` limita los valores válidos sin mezclar lógica de negocio; `AlienContact` concentra la invariantes del informe; las funciones de construcción y salida mantienen separadas la demo, la presentación y la validación. Las constantes (`CONTACT_PREFIX`, `STRONG_SIGNAL_LIMIT`, `MIN_TELEPATHIC_WITNESSES`) evitan números mágicos y facilitan cambios.

## 2. Preguntas posibles de corrección

- **¿Por qué usar un `Enum` para `contact_type`?**
  Porque restringe los valores a los cuatro tipos del enunciado y hace el código más seguro y legible.

- **¿Para qué sirve `model_validator(mode="after")`?**
  Sirve para validar reglas que dependen de varios campos una vez que Pydantic ya ha validado y convertido cada campo individual.

- **¿Por qué no poner todas las reglas en `Field`?**
  `Field` valida restricciones de un campo aislado; reglas como “telepathic requiere 3 testigos” dependen de varios campos.

- **¿Qué error se produce si falla una regla de negocio?**
  Se lanza un `ValueError` dentro del validador y Pydantic lo reporta como `ValidationError`.

- **¿Qué demuestra el caso inválido del `main()`?**
  Que un contacto telepático con menos de 3 testigos es rechazado por la validación de modelo.

- **¿Qué cubren los tests?**
  Creación válida, reglas de ID, contacto físico verificado, testigos en contacto telepático y mensaje obligatorio en señales fuertes.
