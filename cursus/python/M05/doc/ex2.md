# Exercise 2: Data Pipeline

## Exercise 2

`data_pipeline`

- Directory: `ex2/`
- Files to Submit: `data_pipeline.py`
- Authorized: `builtins`, standard types, `import typing`, `import abc`

## Engineering Briefing

Your final challenge is to integrate everything into a complete data processing pipeline that demonstrates mastery of polymorphic architecture at an enterprise scale.

Use your code from Exercise 1 and improve it in order to obtain a complete data pipeline. Your `DataStream` class already handles input streams correctly. You need now to handle the output part of the pipeline. This will be achieved by using a plugin system for export classes, made export-compatible through duck typing.

Implement the following:

- A new `ExportPlugin` class that inherits from the special `Protocol` class.
- This class will define the following method, which will act as a constraint for each export plugin:

```python
def process_output(self, data: list[tuple[int, str]]) -> None:
```

The type of the `data` parameter is a list of tuples that matches the return value of the `output` method from the `DataProcessor` class.

- The `DataStream` class will now implement the

```python
def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
```

method, to be used after calling `process_stream`, that will consume `nb` elements from all registered data processors and export them using the provided compatible plugin.

- Create at least a CSV export plugin and a JSON export plugin. No need to use a specific import for these plugins, manually create valid CSV and JSON strings.

## Example

```text
$> python3 data_pipeline.py
=== Code Nexus - Data Pipeline ===
Initialize Data Stream...
== DataStream statistics ==
No processor found, no data
Registering Processors
Send first batch of data on stream: ['Hello world', [3.14, -1, 2.71], [{'log_level':'WARNING','
log_message':'Telnet access! Use ssh instead'}, {'log_level':'INFO','log_message':'User wil is
connected'}], 42, ['Hi','five']]
== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 4 on processor
Text Processor: total 3 items processed, remaining 3 on processor
Log Processor: total 2 items processed, remaining 2 on processor
Send 3 processed data from each processor to a CSV plugin:
CSV Output:
3.14,-1,2.71
CSV Output:
Hello world,Hi,five
CSV Output:
WARNING: Telnet access! Use ssh instead,INFO: User wil is connected
== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 1 on processor
Text Processor: total 3 items processed, remaining 0 on processor
Log Processor: total 2 items processed, remaining 0 on processor
Send another batch of data: [21, ['I love AI','LLMs are wonderful','Stay healthy'], [{'log_level':'
ERROR','log_message':'500 server crash'}, {'log_level':'NOTICE','log_message':'Certificate
expires in 10 days'}], [32, 42, 64, 84, 128, 168],'World hello']
== DataStream statistics ==
Numeric Processor: total 11 items processed, remaining 8 on processor
Text Processor: total 7 items processed, remaining 4 on processor
Log Processor: total 4 items processed, remaining 2 on processor
Send 5 processed data from each processor to a JSON plugin:
JSON Output:
{"item_3": "42", "item_4": "21", "item_5": "32", "item_6": "42", "item_7": "64"}
JSON Output:
{"item_3": "I love AI", "item_4": "LLMs are wonderful", "item_5": "Stay healthy", "item_6": "World hello
"}
JSON Output:
{"item_2": "ERROR: 500 server crash", "item_3": "NOTICE: Certificate expires in 10 days"}
== DataStream statistics ==
Numeric Processor: total 11 items processed, remaining 3 on processor
Text Processor: total 7 items processed, remaining 0 on processor
Log Processor: total 4 items processed, remaining 0 on processor
```
