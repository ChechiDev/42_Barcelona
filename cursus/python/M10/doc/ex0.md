# Exercise 0: Lambda Sanctum

Create `ex0/lambda_spells.py` to demonstrate lambda expressions with `sorted`, `filter`, `map`, `min`, `max`, `sum`, `len`, and `round`.

Required functions:

- `artifact_sorter(artifacts: list[dict]) -> list[dict]`
- `power_filter(mages: list[dict], min_power: int) -> list[dict]`
- `spell_transformer(spells: list[str]) -> list[str]`: add `"* "` prefix and `" *"` suffix.
- `mage_stats(mages: list[dict]) -> dict`: return `max_power`, `min_power`, and `avg_power` rounded to 2 decimals.

All transformations should use lambda expressions where appropriate.
