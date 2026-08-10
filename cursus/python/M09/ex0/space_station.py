#!/usr/bin/env python3

"""Validate cosmic space station data with Pydantic"""

from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


SEPARATOR = "=" * 40


class SpaceStation(BaseModel):
    """Represent validated space station telemetry"""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def build_station_data(crew_size: int) -> dict[str, object]:
    """Build dynamic station data for validation demos"""

    return {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": crew_size,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2024-01-15T08:30:00",
        "notes": "Nominal orbital operations",
    }


def format_status(station: SpaceStation) -> str:
    """Return the operational display status"""

    if station.is_operational:
        return "Operational"
    return "Offline"


def print_station(station: SpaceStation) -> None:
    """Print validated station details"""

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {format_status(station)}")


def print_first_validation_error(error: ValidationError) -> None:
    """Print the first Pydantic validation error message"""

    first_error = error.errors()[0]
    print(first_error["msg"])


def main() -> None:
    """Run the space station validation demo"""

    print("Space Station Data Validation")
    print(SEPARATOR)
    station = SpaceStation.model_validate(build_station_data(6))
    print_station(station)
    print(SEPARATOR)
    print("Expected validation error:")
    try:
        SpaceStation.model_validate(build_station_data(21))
    except ValidationError as error:
        print_first_validation_error(error)


if __name__ == "__main__":
    main()
