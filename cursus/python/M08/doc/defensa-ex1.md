# Defensa ex1: Loading Programs

## 1. Explicación del código

`ex1/loading.py` demuestra gestión de dependencias y análisis de datos usando `pandas`, `numpy` y `matplotlib`. El programa usa solo imports autorizados por el subject (`importlib` y `sys`) y carga dependencias dinámicamente con `importlib.import_module()` dentro de `load_module()`, por lo que si falta un paquete no se rompe al arrancar: lo marca como `[MISSING]` y muestra cómo instalarlo.

La gestión con pip está representada por `requirements.txt`, que lista las dependencias directas. La gestión con Poetry está representada por `pyproject.toml`, que incluye metadatos del proyecto y dependencias, y permite generar un lockfile reproducible. El script explica ambas opciones en su salida.

Si todas las dependencias existen, `build_matrix_dataframe()` genera datos simulados con `numpy.random.default_rng(42)`, lo que hace el resultado reproducible. Esos arrays se convierten en un `pandas.DataFrame`. Después, `get_analysis_summary()` calcula métricas numéricas y `save_visualization()` usa `matplotlib` para guardar `matrix_analysis.png`.

El diseño separa responsabilidades: inspección de dependencias, instrucciones de instalación, generación de datos, análisis y visualización. Esta separación facilita pruebas y mantenimiento. Las dependencias externas se reciben como módulos cargados dinámicamente, una decisión simple de inversión de dependencias que evita acoplar el arranque del programa a imports obligatorios.

## 2. Preguntas posibles de corrección

- **¿Por qué importas pandas/numpy/matplotlib dinámicamente?** Para detectar dependencias faltantes de forma controlada y dar instrucciones útiles en vez de lanzar un traceback.
- **¿Por qué no usas `typing` ni `types` para los módulos dinámicos?** Porque no son imports autorizados por el subject; se usan anotaciones simples con `object` y acceso dinámico con `getattr()` para mantener el comportamiento y cumplir las restricciones.
- **¿Cuál es la diferencia entre pip y Poetry?** pip instala paquetes desde `requirements.txt`; Poetry gestiona proyecto, dependencias y lockfile desde `pyproject.toml`.
- **¿Por qué usas `default_rng(42)`?** Para generar datos aleatorios reproducibles; con la misma semilla se obtienen los mismos resultados.
- **¿Se usan listas hardcodeadas o `range()` para el dataset?** No; la fuente de datos simulados son arrays generados con numpy.
- **¿Qué archivo produce el script?** `matrix_analysis.png`, si las dependencias están disponibles.
- **¿Qué decisión SOLID destacarías?** SRP: cada función cambia por un motivo distinto; además, pasar módulos como parámetros reduce acoplamiento y mejora testabilidad.
