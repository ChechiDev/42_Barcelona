# Defensa ex2: Accessing the Mainframe

## 1. Explicación del código

`ex2/oracle.py` carga configuración de forma segura usando variables de entorno y, si está disponible, `python-dotenv`. La función `load_environment_file()` llama a `load_dotenv(override=False)`, de modo que un valor ya definido en el entorno real tiene prioridad sobre el valor de `.env`, cumpliendo el requisito de overrides.

La configuración se construye en `build_config()` leyendo `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL` y `ZION_ENDPOINT`. Hay valores por defecto seguros para modo (`development`) y log level (`DEBUG`), mientras que claves sensibles o necesarias pueden quedar vacías para ser reportadas como faltantes.

`OracleConfig` encapsula los valores de configuración. Las funciones `format_database_status()`, `format_api_status()` y `format_zion_status()` muestran estados seguros sin imprimir secretos reales. Por ejemplo, si existe `API_KEY`, solo indica `Authenticated`, pero nunca revela la clave. `get_missing_keys()` detecta configuraciones obligatorias ausentes y `print_security_check()` informa avisos sin detener el programa.

La seguridad se apoya también en archivos del ejercicio: `.env.example` documenta variables sin secretos reales, `requirements.txt` declara `python-dotenv` y `.gitignore` ignora `.env` para evitar subir credenciales. En SOLID, el código separa carga, construcción, validación/formato y presentación, manteniendo responsabilidades pequeñas y fáciles de probar.

## 2. Preguntas posibles de corrección

- **¿Por qué usar variables de entorno?** Permiten configurar la aplicación sin hardcodear secretos ni cambiar código entre entornos.
- **¿Qué hace `python-dotenv`?** Carga variables desde un archivo `.env` local para desarrollo.
- **¿Por qué `override=False` es importante?** Porque respeta las variables ya exportadas en el sistema; así producción puede sobrescribir valores del `.env`.
- **¿Se imprime la API key?** No. Solo se muestra si hay autenticación o si falta la variable.
- **¿Qué diferencia hay entre desarrollo y producción?** `MATRIX_MODE` cambia mensajes de estado, por ejemplo local instance frente a production mainframe.
- **¿Cómo se evita commitear secretos?** `.gitignore` incluye `.env` y el repositorio solo debe incluir `.env.example` con valores de ejemplo.
- **¿Qué decisión SOLID destacarías?** `OracleConfig` encapsula datos y las funciones de formato/validación tienen responsabilidades separadas, evitando mezclar carga, seguridad y salida.
