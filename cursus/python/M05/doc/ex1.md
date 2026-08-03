# Exercise 1: Polymorphic Processing of a Data Stream

## Exercise 1

`data_stream`

- Directory: `ex1/`
- Files to Submit: `data_stream.py`
- Authorized: `builtins`, standard types, `import typing`, `import abc`

## Engineering Briefing

It is time to build an adaptive stream processing workflow that can handle multiple data types simultaneously.

Use your code from Exercise 0 and improve it:

- Create a `DataStream` class that will receive a stream of data containing different types and then will route each element to the appropriate data processor using polymorphic behavior.
- This class will implement the

```python
def register_processor(self, proc: DataProcessor) -> None:
```

method that allows you to register a new data processor to process the data stream.

- This class will implement the

```python
def process_stream(self, stream: list[typing.Any]) -> None:
```

method that will analyze each element of the list received as a parameter and send it to the appropriate registered data processor. Error messages will be printed if no data processor can handle an element.

- Finally, the class will implement the `def print_processors_stats(self) -> None:` method in order to print stream statistics.
- Create a test scenario that demonstrates the correct processing of a data stream. Display statistics on registered data processors, consume elements using the `output` method of each data processor and show updated statistics.

## Example

```text
$> python3 data_stream.py
=== Code Nexus - Data Stream ===
Initialize Data Stream...
== DataStream statistics ==
No processor found, no data
Registering Numeric Processor
Send first batch of data on stream: ['Hello world', [3.14, -1, 2.71], [{'log_level':'WARNING','
log_message':'Telnet access! Use ssh instead'}, {'log_level':'INFO','log_message':'User wil is
connected'}], 42, ['Hi','five']]
DataStream error - Can't process element in stream: Hello world
DataStream error - Can't process element in stream: [{'log_level':'WARNING','log_message':'Telnet
access! Use ssh instead'}, {'log_level':'INFO','log_message':'User wil is connected'}]
DataStream error - Can't process element in stream: ['Hi','five']
== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 4 on processor
Registering other data processors
Send the same batch again
== DataStream statistics ==
Numeric Processor: total 8 items processed, remaining 8 on processor
Text Processor: total 3 items processed, remaining 3 on processor
Log Processor: total 2 items processed, remaining 2 on processor
Consume some elements from the data processors: Numeric 3, Text 2, Log 1
== DataStream statistics ==
Numeric Processor: total 8 items processed, remaining 5 on processor
Text Processor: total 3 items processed, remaining 1 on processor
Log Processor: total 2 items processed, remaining 1 on processor
```

How does polymorphism allow the DataStream to handle different data types in the stream without knowing their specific implementations?

What are the benefits of this design approach?
