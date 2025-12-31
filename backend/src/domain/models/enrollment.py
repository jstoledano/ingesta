from pydantic import BaseModel, UUID4, Field
from typing import Annotated, Optional


class Enrollment(BaseModel):
    """
    Represents an enrollment for a subject in a
    particular period.
    """

    id: UUID4
    subject: Annotated[
        UUID4,
        Field(description="The subject that I enroll")
    ]
    period: Annotated[
        str,
        Field(
            pattern=r"^(2[6-9]|[3][0-4])0[12]$",
            description="The period that I enroll",
        )
    ]
    group: Annotated[
        int,
        Field(
            default=0,
            description="The group I enroll",
        )
    ]
    professor: Annotated[
        str,
        Field(
            Field(min_length=3, max_length=100, description="Professor name"),
        )
    ]
    advisor: Annotated[
        str,
        Field(
            min_length=3,
            max_length=100,
            description="Advisor name",
        )
    ]
    approved: Annotated[
        bool,
        Field(
            default=False,
            description="Whether or not the enrollment is approved",
        )
    ]
    attempt: Annotated[
        int,
        Field(
            default=1,
            le=3,
            description="The attempt number",
        )
    ]
    result: Annotated[
        Optional[int],
        Field(
            ge=0, le=100,
            description="The result of the enrollment",
        )
    ] = None