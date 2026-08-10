# Defensa ex0: Entering the Matrix

## 1. Explicación del código

`ex0/construct.py` inspecciona el intérprete Python que está ejecutando el script. La función clave es `is_virtual_environment()`, que compara `sys.prefix` con `sys.base_prefix`: si son distintos, Python está dentro de un entorno virtual; si son iguales, se está usando el entorno global.

Cuando no hay entorno virtual, `print_global_environment()` muestra el ejecutable actual con `sys.executable`, avisa de que las instalaciones afectarían al entorno global y enseña comandos prácticos para crear y activar un venv (`python -m venv matrix_env`, `source .../activate` o activación en Windows).

Cuando sí hay entorno virtual, `print_virtual_environment()` muestra el nombre del entorno, su ruta (`sys.prefix`), el ejecutable actual y la ruta de instalación de paquetes. Esa ruta sale de `get_package_path()`, que prioriza `site.getsitepackages()` y usa `site.getusersitepackages()` como alternativa.

La responsabilidad está separada en funciones pequeñas: detectar el entorno, obtener datos y pintar cada estado. Esto aplica SRP de SOLID sin complicar el ejercicio. La dependencia está limitada a módulos autorizados por el subject (`sys`, `os`, `site`) y los valores dinámicos vienen del entorno real, no de datos fijos.

## 2. Preguntas posibles de corrección

- **¿Cómo sabes si estás dentro de un venv?** Comparo `sys.prefix` y `sys.base_prefix`; en un venv apuntan a rutas distintas.
- **¿Por qué no se debe subir el entorno virtual?** Porque contiene dependencias instaladas, rutas locales y muchos archivos generados; se debe subir solo el código y las instrucciones/dependencias.
- **¿Qué muestra `sys.executable`?** La ruta del binario Python que ejecuta el script.
- **¿Qué es `site-packages`?** La carpeta donde Python instala paquetes para el entorno activo.
- **¿Qué caso límite cubre el script?** Si `site.getsitepackages()` no devuelve rutas, usa `site.getusersitepackages()` como fallback.
- **¿Qué decisión SOLID hay aquí?** Cada función tiene una responsabilidad clara, por ejemplo detectar el venv o imprimir un caso concreto.
