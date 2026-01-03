from dataclasses import dataclass


@dataclass(frozen=True)
class SubjectCode:
    value: str
    # Optional context fields if they are truly part of the ID
    semester: int | None = None

    def __post_init__(self):
        # Validation Logic implies "Design by Contract"
        # If the string doesn't match the regex pattern -> Raise DomainException
        # If semester is out of bounds -> Raise DomainException
        pass

    def __str__(self) -> str:
        # Return canonical string representation
        return self.value