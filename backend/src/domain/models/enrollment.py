from enum import IntEnum
from typing import Annotated, Optional
from uuid import uuid4

from pydantic import UUID4, BaseModel, ConfigDict, Field, model_validator

MIN_PASSING_GRADE = 60


class EnrollmentStatus(IntEnum):
    ACTIVE = 1
    DROPPED = 2
    COMPLETED = 3
    FAILED = 4

    @property
    def display_name(self) -> str:
        match self:
            case 1:
                return "Active"
            case 2:
                return "Dropped"
            case 3:
                return "Completed"
            case 4:
                return "Failed"
            case _:
                return "Unknown"


class Enrollment(BaseModel):
    """
    An attempt by the student to take a course in a specific period.
    """

    model_config = ConfigDict(
        frozen=True,
        json_schema_extra={
            "example": {
                "subject": "550e8400-e29b-41d4-a716-446655440000",
                "period": "2601",
                "group": 67,
                "professor": "UNASSIGNED PROFESSOR",
                "advisor": "UNASSIGNED ADVISOR",
                "attempt": 1,
                "result": None,
            }
        },
    )

    id: Annotated[
        UUID4,
        Field(
            default_factory=uuid4,
            description="Enrollment ID",
        ),
    ]
    subject: Annotated[UUID4, Field(description="The subject that I enroll")]
    period: Annotated[
        str,
        Field(
            pattern=r"^(2[6-9]|[3][0-4])0[12]$",
            description="The period that I enroll",
        ),
    ]
    group: Annotated[
        int,
        Field(
            default=0,
            description="The group I enroll",
        ),
    ]
    professor: Annotated[
        str,
        Field(min_length=3, max_length=100, description="Professor name"),
    ]
    advisor: Annotated[
        str,
        Field(
            min_length=3,
            max_length=100,
            description="Advisor name",
        ),
    ]
    attempt: Annotated[
        int,
        Field(
            default=1,
            le=3,
            description="The attempt number",
        ),
    ]
    result: Annotated[
        Optional[int],
        Field(
            ge=0,
            le=100,
            description="The result of the enrollment",
        ),
    ] = None
    status: Annotated[
        EnrollmentStatus,
        Field(
            default=EnrollmentStatus.ACTIVE,
            description="The status of the enrollment",
        ),
    ]

    @property
    def is_approved(self) -> bool:
        return self.result is not None and self.result >= MIN_PASSING_GRADE

    @model_validator(mode="after")
    def validate_status_and_result(self):
        # ACTIVE → no result
        if self.status == EnrollmentStatus.ACTIVE:
            if self.result is not None:
                raise ValueError("ACTIVE enrollment cannot have a result")

        # DROPPED → no result
        if self.status == EnrollmentStatus.DROPPED:
            if self.result is not None:
                raise ValueError("DROPPED enrollment cannot have a result")

        # COMPLETED → result >= MIN_PASSING_GRADE
        if self.status == EnrollmentStatus.COMPLETED:
            if self.result is None:
                raise ValueError("COMPLETED enrollment must have a result")
            if self.result < MIN_PASSING_GRADE:
                raise ValueError(
                    f"COMPLETED enrollment requires result >= {MIN_PASSING_GRADE}"
                )

        # FAILED → result < MIN_PASSING_GRADE
        if self.status == EnrollmentStatus.FAILED:
            if self.result is None:
                raise ValueError("FAILED enrollment must have a result")
            if self.result >= MIN_PASSING_GRADE:
                raise ValueError(
                    f"FAILED enrollment requires result < {MIN_PASSING_GRADE}"
                )

        return self
