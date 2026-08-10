#!/usr/bin/env python3

"""Test M09 Pydantic validation exercises"""

import ast
import subprocess
import sys
from pathlib import Path

import pytest
from pydantic import ValidationError


M09_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(M09_DIR / "ex0"))
sys.path.insert(0, str(M09_DIR / "ex1"))
sys.path.insert(0, str(M09_DIR / "ex2"))

from alien_contact import (  # noqa: E402
    AlienContact,
    ContactType,
    build_contact_data,
)
from space_crew import (  # noqa: E402
    CrewMember,
    Rank,
    SpaceMission,
    build_mission_data,
    build_valid_crew,
)
from space_station import SpaceStation, build_station_data  # noqa: E402


def run_script(script_path: Path) -> subprocess.CompletedProcess[str]:
    """Run one M09 script and capture output"""

    return subprocess.run(
        [sys.executable, str(script_path)],
        cwd=script_path.parent,
        check=False,
        capture_output=True,
        text=True,
    )


def test_space_station_validates_fields_and_datetime_conversion() -> None:
    """Check station field constraints and datetime conversion"""

    station = SpaceStation.model_validate(build_station_data(6))

    assert station.station_id == "ISS001"
    assert station.crew_size == 6
    assert station.last_maintenance.year == 2024
    with pytest.raises(ValidationError, match="less than or equal to 20"):
        SpaceStation.model_validate(build_station_data(21))


def test_alien_contact_business_rules() -> None:
    """Check alien contact model-level validation rules"""

    contact = AlienContact.model_validate(
        build_contact_data(ContactType.RADIO, 5),
    )
    assert contact.contact_type is ContactType.RADIO
    with pytest.raises(ValidationError, match="requires at least 3 witnesses"):
        AlienContact.model_validate(
            build_contact_data(ContactType.TELEPATHIC, 1),
        )
    data = build_contact_data(ContactType.PHYSICAL, 5)
    data["is_verified"] = False
    with pytest.raises(ValidationError, match="must be verified"):
        AlienContact.model_validate(data)
    data = build_contact_data(ContactType.VISUAL, 5)
    data["contact_id"] = "XX001"
    with pytest.raises(ValidationError, match="Contact ID must start with AC"):
        AlienContact.model_validate(data)
    data = build_contact_data(ContactType.RADIO, 5)
    data["message_received"] = None
    with pytest.raises(ValidationError, match="Strong signals"):
        AlienContact.model_validate(data)


def test_space_mission_nested_validation_rules() -> None:
    """Check nested crew and mission safety validation"""

    mission = SpaceMission.model_validate(
        build_mission_data(build_valid_crew()),
    )
    assert mission.destination == "Mars"
    assert len(mission.crew) == 3
    invalid_crew = [
        CrewMember(
            member_id="CM100",
            name="Bob Stone",
            rank=Rank.LIEUTENANT,
            age=30,
            specialization="Science",
            years_experience=8,
        )
    ]
    with pytest.raises(ValidationError, match="Commander or Captain"):
        SpaceMission.model_validate(build_mission_data(invalid_crew))
    data = build_mission_data(build_valid_crew())
    data["mission_id"] = "X2024"
    with pytest.raises(ValidationError, match="Mission ID must start with M"):
        SpaceMission.model_validate(data)


def test_space_mission_rejects_unsafe_long_or_inactive_crew() -> None:
    """Check long missions require experienced and active crew"""

    inexperienced_crew = [
        CrewMember(
            member_id="CM200",
            name="Ada Ray",
            rank=Rank.COMMANDER,
            age=41,
            specialization="Command",
            years_experience=6,
        ),
        CrewMember(
            member_id="CM201",
            name="Leo Moon",
            rank=Rank.OFFICER,
            age=29,
            specialization="Biology",
            years_experience=1,
        ),
        CrewMember(
            member_id="CM202",
            name="Mia Star",
            rank=Rank.CADET,
            age=25,
            specialization="Robotics",
            years_experience=2,
        ),
    ]
    with pytest.raises(ValidationError, match="50% experienced crew"):
        SpaceMission.model_validate(build_mission_data(inexperienced_crew))
    inactive_crew = build_valid_crew()
    inactive_crew[0].is_active = False
    with pytest.raises(
        ValidationError,
        match="All crew members must be active",
    ):
        SpaceMission.model_validate(build_mission_data(inactive_crew))


@pytest.mark.parametrize(
    ("script_name", "expected_title"),
    [
        ("ex0/space_station.py", "Space Station Data Validation"),
        ("ex1/alien_contact.py", "Alien Contact Log Validation"),
        ("ex2/space_crew.py", "Space Mission Crew Validation"),
    ],
)
def test_scripts_print_subject_demo(
    script_name: str,
    expected_title: str,
) -> None:
    """Check scripts execute demos and print expected titles"""

    result = run_script(M09_DIR / script_name)

    assert result.returncode == 0
    assert result.stderr == ""
    assert expected_title in result.stdout
    assert "Expected validation error:" in result.stdout


def test_functions_and_classes_follow_project_docstring_style() -> None:
    """Check M09 function and class docstrings follow project style"""

    for source_path in M09_DIR.rglob("*.py"):
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef),
            ):
                docstring = ast.get_docstring(node, clean=False)
                if (
                    isinstance(node, ast.FunctionDef)
                    and node.name == "__init__"
                ):
                    assert docstring is None, f"{source_path}:{node.lineno}"
                    continue
                assert docstring is not None, f"{source_path}:{node.lineno}"
                assert "\n" not in docstring, f"{source_path}:{node.lineno}"
                assert not docstring.endswith("."), (
                    f"{source_path}:{node.lineno}"
                )
