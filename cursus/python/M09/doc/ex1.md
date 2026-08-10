# Exercise 1: Alien Contact Logs

Create `ex1/alien_contact.py` using Pydantic v2 custom model validation.

## Requirements

- Define `ContactType` enum values: `radio`, `visual`, `physical`, `telepathic`.
- Define `AlienContact` model.
- Fields:
  - `contact_id`: string, 5-15 characters
  - `timestamp`: datetime
  - `location`: string, 3-100 characters
  - `contact_type`: `ContactType`
  - `signal_strength`: float, 0.0-10.0
  - `duration_minutes`: integer, 1-1440
  - `witness_count`: integer, 1-100
  - `message_received`: optional string, max 500 characters
  - `is_verified`: boolean, default `False`
- Use `@model_validator(mode="after")`.
- Business rules:
  - Contact ID must start with `AC`.
  - Physical contact must be verified.
  - Telepathic contact requires at least 3 witnesses.
  - Strong signals greater than 7.0 must include a message.
- Include `main()` with valid and invalid examples.

## Concepts

- `Enum`
- Pydantic v2 `model_validator`
- Model-level business validation
