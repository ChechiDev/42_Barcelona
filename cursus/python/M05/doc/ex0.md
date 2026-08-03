# Exercise 0: Data Processor

## Exercise 0

`data_processor`

- Directory: `ex0/`
- Files to Submit: `data_processor.py`
- Authorized: `builtins`, standard types, `import typing`, `import abc`

## Engineering Briefing

Welcome to the Code Nexus! Build the foundation of our data processing system. You will create the base processor architecture and demonstrate how different data types can share common processing interfaces while maintaining their unique characteristics.

This exercise requires the use of abstract classes using `ABC` (Abstract Base Class). We will first create separate classes that share common interfaces. In the next exercise, they will be unified in the same workflow.

Set up the following architecture:

- An abstract class `DataProcessor` that inherits from `ABC` and defines the common processing interface.
- Three specialized classes `NumericProcessor`, `TextProcessor`, and `LogProcessor` that inherit from the `DataProcessor` class and will process different kinds of data.
- Two abstract methods in `DataProcessor`: `validate`, which will check whether the input data are appropriate for the current data processor, and `ingest`, which will process the input data. Each specialized class will need to override these methods.
- One standard method in `DataProcessor`: `output`, which will output ingested data.

You need to comply with the following constraints:

- The `validate` method will be defined as `validate(self, data: Any) -> bool` in the `DataProcessor` class. The overriding methods in the specialized classes will share the same signature, as they cannot know what data will be sent and must accept any type. This method returns a bool that indicates if the provided data can be ingested by this data processor.
- The `ingest` method will be defined as `ingest(self, data: Any) -> None` in the `DataProcessor` class. The overriding methods in the specialized classes will have their own specific signatures to match the types they expect. In case the user does not validate the data before calling `ingest`, and provides invalid data, an exception must be raised.
- The `output` method will be defined as `output(self) -> tuple[int, str]` in the `DataProcessor` class. There is no need to override it in the specialized classes.
- The `NumericProcessor` ingests `int`, `float`, and lists of both types (including mixed-type lists). It then converts the data into strings and stores it internally (keeping each item separated), waiting to be extracted piece by piece using the `output` method. The overriding `ingest` method signature must reflect the accepted types.
- The `TextProcessor` ingests `str` and lists of strings. It stores the data internally (keeping each item separated), waiting to be extracted piece by piece using the `output` method. The overriding `ingest` method signature must reflect the accepted types.
- The `LogProcessor` ingests a `dict` of string key-value pairs, and lists of that type. It then converts the data into strings and stores it internally (keeping each item separated), waiting to be extracted piece by piece using the `output` method. The overriding `ingest` method signature must reflect the accepted types.
- The `output` method will extract the oldest piece of data stored internally in the data processor, along with the associated processing rank within the data processor. The piece of data is then removed from the data processor.

Finally, test your architecture:

- Create instances for each specialized class.
- Test valid and invalid data for each class through the `validate` method.
- Test at least one invalid data item with the `ingest` method without prior validation, and check that it raises an exception. This will leave you with a `mypy` warning, on purpose.
- Ingest various data for each data processor and then extract it using `output`.

## Example

```text
$> python3 data_processor.py
=== Code Nexus - Data Processor ===
Testing Numeric Processor...
Trying to validate input'42': True
Trying to validate input'Hello': False
Test invalid ingestion of string'foo'without prior validation:
Got exception: Improper numeric data
Processing data: [1, 2, 3, 4, 5]
Extracting 3 values...
Numeric value 0: 1
Numeric value 1: 2
Numeric value 2: 3
Testing Text Processor...
Trying to validate input'42': False
Processing data: ['Hello','Nexus','World']
Extracting 1 value...
Text value 0: Hello
Testing Log Processor...
Trying to validate input'Hello': False
Processing data: [{'log_level':'NOTICE','log_message':'Connection to server'}, {'log_level':'ERROR
','log_message':'Unauthorized access!!'}]
Extracting 2 values...
Log entry 0: NOTICE: Connection to server
Log entry 1: ERROR: Unauthorized access!!
```
