from dataclasses import dataclass
import re


SUBJECT_CODE_PATTERN = re.compile(r"^1514[1-4][1-8](0[1-9]|[1-3][0-9]|4[0-6])$")


class InvalidSubjectCodeError(ValueError):
    """
    Raised when a SubjectCode cannot be created due to domain rule violations.

    Examples:
        - Input is None or Empty.
        - Input format is not 8 digits (e.g., "123").
        - Input contains non-numeric characters (e.g., "1514110A").
    """
    pass


@dataclass(frozen=True)
class SubjectCode:
    value: str
    # Optional context fields if they are truly part of the ID
    semester: int | None = None

    def __post_init__(self):
        # Validation Logic implies "Design by Contract"
        # If the string doesn't match the regex pattern -> Raise DomainException
        # If semester is out of bounds -> Raise DomainException
        if not SUBJECT_CODE_PATTERN.match(self.value):
            raise InvalidSubjectCodeError

    def __str__(self) -> str:
        # Return canonical string representation
        return self.value