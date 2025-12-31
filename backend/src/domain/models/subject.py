from enum import Enum, IntEnum
from typing import Annotated, Optional, Set
from uuid import uuid4

from pydantic import UUID4, BaseModel, ConfigDict, Field


class Module(IntEnum):
    BASIC = 1
    DISCIPLINARY = 2
    DISCIPLINARY_ADVANCED = 3
    PROFESSIONAL = 4

    @property
    def display_name(self) -> str:
        # We use match against the current value (self)
        match self:
            case 1:
                return "Basic Education"
            case 2:
                return "Disciplinary Education"
            case 3:
                return "Disciplinary Education"
            case 4:
                return "Professional Education"
            case _:
                return "Unknown"


class Semester(IntEnum):
    SEM_1 = 1
    SEM_2 = 2
    SEM_3 = 3
    SEM_4 = 4
    SEM_5 = 5
    SEM_6 = 6
    SEM_7 = 7
    SEM_8 = 8


class Block(IntEnum):
    ZERO = 0
    FIRST = 1
    SECOND = 2


class Credits(float, Enum):
    FIVE = 5.0
    SIX = 6.0
    SIX_AND_HALF = 6.5


class Subject(BaseModel):
    """
    Represents a Subject in the curriculum.
    Policy: Immutable once instantiated.
    """

    model_config = ConfigDict(
        frozen=True,
        json_schema_extra={
            "example": {
                "module": 1,
                "semester": 2,
                "block": 1,
                "name": "Data Structures",
                "code": "15142419",
                "credits": 6.0,
            }
        },
    )

    id: Annotated[
        UUID4,
        Field(default_factory=uuid4, description="Subject ID")
    ]
    module: Annotated[
        Module,
        Field(description="Academic module"),
    ]
    semester: Annotated[Semester, Field(description="Semester")]
    block: Annotated[Block, Field(description="Block")]
    code: Annotated[
        str,
        Field(
            pattern=r"^1514[1-4][1-8](0[1-9]|[1-3][0-9]|4[0-6])$",
            description="Unique code (e.g. 15141101)",
        ),
    ]
    acronym: Annotated[
        Optional[str],
        Field(pattern=r"^(D[A-Z]{3})?$", description="Acronym / Initialism")
    ] = None
    name: Annotated[
        str,
        Field(min_length=3, max_length=100, description="Name"),
    ]
    credits: Annotated[Credits, Field(description="Credits")]
    prerequisites: Set[UUID4] = Field(
        default_factory=set, description="Prerequisite subject IDs"
    )
