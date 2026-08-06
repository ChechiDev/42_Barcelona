# Defensa M05 ex2 - data_pipeline

## 1. Explicación del código

Este ejercicio amplía el flujo de `ex1` con una fase de salida mediante plugins.

- `ExportPlugin` hereda de `Protocol` y define la interfaz esperada por cualquier plugin:
  - `process_output(self, data: list[tuple[int, str]]) -> None`
- `DataProcessor` mantiene la interfaz común:
  - `validate`
  - `ingest`
  - `output`
- `NumericProcessor`, `TextProcessor` y `LogProcessor` mantienen la misma responsabilidad que en ejercicios anteriores.
- `DataStream` conserva el routing polimórfico de entrada y añade `output_pipeline(nb, plugin)`.
- `output_pipeline` recorre todos los procesadores registrados, consume hasta `nb` elementos disponibles de cada uno y los envía al plugin recibido.
- `get_processors()` devuelve una copia de la lista registrada para evitar que código externo pueda mutar directamente el estado interno del stream.
- `print_processors_stats()` usa el helper `_format_processor_stats()` para concentrar el formato de estadísticas en un método pequeño y mantener el método público centrado en el flujo de impresión.

Plugins implementados:

- `CSVExportPlugin`: imprime los valores separados por comas, sin usar el módulo `csv`.
- `_format_csv_line()` concentra la construcción de la línea CSV; `process_output()` solo se encarga de imprimir la cabecera y el resultado.
- `JSONExportPlugin`: crea manualmente un objeto JSON con claves `item_<rank>`, sin usar el módulo `json`.

La demo usa constantes cortas en mayúsculas y construye estructuras compuestas en `main()` con helpers como `build_log_entry()` y `build_stream()`. Así los datos de ejemplo quedan separados de la lógica principal.

## 2. Posibles preguntas de defensa

**¿Dónde se usa duck typing?**  
En `output_pipeline`: el método solo necesita que el objeto recibido tenga `process_output`. No depende de una clase base concreta en runtime.

**¿Por qué se usa `Protocol`?**  
Porque el subject pide una interfaz estructural para plugins. Cualquier clase con `process_output(data)` es compatible.

**¿Dónde se mantiene el polimorfismo de entrada?**  
En `DataStream._put_element`, que usa la interfaz `DataProcessor` y llama a `validate` e `ingest` sin conocer la clase concreta.

**¿Por qué `output_pipeline` consume hasta `nb` y no siempre exactamente `nb`?**  
Porque un procesador puede tener menos elementos pendientes. Consumir solo los disponibles evita errores al llamar a `output()` en vacío.

**¿Por qué no se importan `csv` ni `json`?**  
Porque el subject indica crear strings CSV y JSON manualmente.

**¿Por qué el formato CSV está en `_format_csv_line()`?**  
Para separar el formateo de la impresión. Esto hace el plugin más claro y permite comprobar el CSV generado sin depender de la salida por pantalla.

**¿Por qué `get_processors()` devuelve una copia?**  
Para mantener encapsulado el estado de `DataStream`: quien recibe la lista puede leerla, pero no modificar directamente la lista interna.

**¿Por qué se usa `_format_processor_stats()`?**  
Para reutilizar exactamente el mismo formato de estadísticas y evitar duplicar la construcción del texto.

**¿Qué representan las claves JSON `item_3`, `item_4`, etc.?**  
Representan el rank devuelto por `output()` para cada dato extraído del procesador.

**¿Cumple el subject?**  
Sí. Implementa `ExportPlugin`, `output_pipeline`, un plugin CSV, un plugin JSON, mantiene el procesamiento de streams y ofrece una demo ejecutable con `python3 data_pipeline.py`.

**¿Qué comprobaciones de calidad se ejecutaron?**  
QA final informado: `flake8 M05`, `mypy --strict M05` y `pytest M05/tests`, con 45 tests pasados.
