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

Plugins implementados:

- `CSVExportPlugin`: imprime los valores separados por comas, sin usar el módulo `csv`.
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

**¿Qué representan las claves JSON `item_3`, `item_4`, etc.?**  
Representan el rank devuelto por `output()` para cada dato extraído del procesador.

**¿Cumple el subject?**  
Sí. Implementa `ExportPlugin`, `output_pipeline`, un plugin CSV, un plugin JSON, mantiene el procesamiento de streams y ofrece una demo ejecutable con `python3 data_pipeline.py`.
