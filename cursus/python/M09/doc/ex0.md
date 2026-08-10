# Exercise 0: Space Station Data

Create `ex0/space_station.py` using Pydantic v2.

## Requirements

- Define a `SpaceStation` Pydantic model.
- Fields:
  - `station_id`: string, 3-10 characters
  - `name`: string, 1-50 characters
  - `crew_size`: integer, 1-20
  - `power_level`: float, 0.0-100.0
  - `oxygen_level`: float, 0.0-100.0
  - `last_maintenance`: datetime
  - `is_operational`: boolean, default `True`
  - `notes`: optional string, max 200 characters
- Include `main()` that creates a valid station and then an invalid station.
- Display the validation error clearly.

## Concepts

- `BaseModel`
- `Field`
- Built-in validation and automatic datetime conversion
