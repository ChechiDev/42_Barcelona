#!/usr/bin/env python3

"""Validate nested space crew mission data with Pydantic"""

from datetime import datetime
from enum import Enum
from typing import Self

from pydantic import BaseModel, Field, ValidationError, model_validator


SEPARATOR = "=" * 41
LONG_MISSION_DAYS = 365
EXPERIENCED_YEARS = 5


class Rank(str, Enum):
    """Define supported crew ranks"""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Represent one validated crew member"""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Represent a validated space mission with nested crew"""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> Self:
        """Validate mission safety requirements"""

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")
        if not has_command_rank(self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > LONG_MISSION_DAYS and not has_expert_crew(
            self.crew,
        ):
            raise ValueError(
                "Long missions need 50% experienced crew"
            )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def has_command_rank(crew: list[CrewMember]) -> bool:
    """Return whether crew has a Captain or Commander"""

    command_ranks = {Rank.CAPTAIN, Rank.COMMANDER}
    return any(member.rank in command_ranks for member in crew)


def has_expert_crew(crew: list[CrewMember]) -> bool:
    """Return whether at least half the crew has enough experience"""

    experienced_count = sum(
        member.years_experience >= EXPERIENCED_YEARS
        for member in crew
    )
    return experienced_count * 2 >= len(crew)


def build_crew_member(
    member_id: str,
    name: str,
    rank: Rank,
    specialization: str,
    years_experience: int,
) -> CrewMember:
    """Build one active crew member for mission demos"""

    return CrewMember(
        member_id=member_id,
        name=name,
        rank=rank,
        age=35,
        specialization=specialization,
        years_experience=years_experience,
    )


def build_valid_crew() -> list[CrewMember]:
    """Build valid crew for a long mission"""

    return [
        build_crew_member(
            "CM001",
            "Sarah Connor",
            Rank.COMMANDER,
            "Mission Command",
            12,
        ),
        build_crew_member(
            "CM002",
            "John Smith",
            Rank.LIEUTENANT,
            "Navigation",
            7,
        ),
        build_crew_member(
            "CM003",
            "Alice Johnson",
            Rank.OFFICER,
            "Engineering",
            4,
        ),
    ]


def build_mission_data(crew: list[CrewMember]) -> dict[str, object]:
    """Build dynamic mission data for validation demos"""

    return {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2024-09-01T09:00:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": crew,
    }


def print_mission(mission: SpaceMission) -> None:
    """Print validated space mission details"""

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )


def print_first_validation_error(error: ValidationError) -> None:
    """Print the first Pydantic validation error message"""

    first_error = error.errors()[0]
    print(first_error["msg"].removeprefix("Value error, "))


def main() -> None:
    """Run the space mission validation demo"""

    print("Space Mission Crew Validation")
    print(SEPARATOR)
    mission = SpaceMission.model_validate(
        build_mission_data(build_valid_crew()),
    )
    print_mission(mission)
    print(SEPARATOR)
    print("Expected validation error:")
    invalid_crew = [
        build_crew_member("CM004", "Bob Stone", Rank.LIEUTENANT, "Science", 8),
        build_crew_member("CM005", "Eve Ross", Rank.OFFICER, "Medical", 6),
    ]
    try:
        SpaceMission.model_validate(build_mission_data(invalid_crew))
    except ValidationError as error:
        print_first_validation_error(error)


if __name__ == "__main__":
    main()
