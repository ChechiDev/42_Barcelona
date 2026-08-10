# Exercise 2: Space Crew Management

Create `ex2/space_crew.py` using nested Pydantic models.

## Requirements

- Define `Rank` enum values: `cadet`, `officer`, `lieutenant`, `captain`, `commander`.
- Define `CrewMember` model.
- Define `SpaceMission` model with a nested crew list.
- Mission validation rules:
  - Mission ID must start with `M`.
  - Must have at least one Commander or Captain.
  - Long missions greater than 365 days require at least 50% crew with 5+ years experience.
  - All crew members must be active.
- Include `main()` with valid and invalid examples.

## Concepts

- Nested Pydantic models
- Enum fields
- Cross-field validation with `model_validator`
