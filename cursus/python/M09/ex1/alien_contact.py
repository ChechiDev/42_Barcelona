#!/usr/bin/env python3

"""Validate alien contact reports with Pydantic business rules"""

from datetime import datetime
from enum import Enum
from typing import Self

from pydantic import BaseModel, Field, ValidationError, model_validator


SEPARATOR = "=" * 38
CONTACT_PREFIX = "AC"
STRONG_SIGNAL_LIMIT = 7.0
MIN_TELEPATHIC_WITNESSES = 3


class ContactType(str, Enum):
    """Define supported alien contact types"""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Represent a validated alien contact report"""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact_rules(self) -> Self:
        """Validate alien contact business rules"""

        if not self.contact_id.startswith(CONTACT_PREFIX):
            raise ValueError("Contact ID must start with AC")
        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type is ContactType.TELEPATHIC
            and self.witness_count < MIN_TELEPATHIC_WITNESSES
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if (
            self.signal_strength > STRONG_SIGNAL_LIMIT
            and not self.message_received
        ):
            raise ValueError("Strong signals must include received messages")
        return self


def build_contact_data(
    contact_type: ContactType,
    witness_count: int,
) -> dict[str, object]:
    """Build dynamic alien contact data for validation demos"""

    return {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-03-20T22:15:00",
        "location": "Area 51, Nevada",
        "contact_type": contact_type,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": witness_count,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False,
    }


def print_contact(contact: AlienContact) -> None:
    """Print validated alien contact details"""

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")


def print_first_validation_error(error: ValidationError) -> None:
    """Print the first Pydantic validation error message"""

    first_error = error.errors()[0]
    print(first_error["msg"].removeprefix("Value error, "))


def main() -> None:
    """Run the alien contact validation demo"""

    print("Alien Contact Log Validation")
    print(SEPARATOR)
    contact = AlienContact.model_validate(
        build_contact_data(ContactType.RADIO, 5),
    )
    print_contact(contact)
    print(SEPARATOR)
    print("Expected validation error:")
    try:
        AlienContact.model_validate(
            build_contact_data(ContactType.TELEPATHIC, 1),
        )
    except ValidationError as error:
        print_first_validation_error(error)


if __name__ == "__main__":
    main()
