from datetime import datetime
from enum import IntEnum
from typing import Annotated, Optional
from uuid import uuid4

from pydantic import UUID4, BaseModel, ConfigDict, Field, model_validator


class TaskStatus(IntEnum):
    TODO = 1
    IN_PROGRESS = 2
    DONE = 3


class Task(BaseModel):
    """
    Keep the record of the task assigned to a subject enrolled.
    """

    model_config = ConfigDict(
        frozen=True,  # It's suppose that the model is frozen and change with a port, I think.
        json_schema_extra={
            "example": {
                "enrollment": "550e8400-e29b-41d4-a716-446655440000",
                "date_due": "2026-01-30T22:59",
                "title": "Identificar problemas socioeconómicos",
                "instructions": "Subir la tarea en formato .docx",
                "status": 1,
            }
        },
    )

    id: Annotated[UUID4, Field(default_factory=uuid4, description="The task id")]
    enrollment: Annotated[UUID4, Field(description="The enrollment own of the task")]
    due_date: Annotated[datetime, Field(description="Due time for the task")]
    title: Annotated[
        str,
        Field(
            min_length=10,
            max_length=100,
            description="Task title",
        ),
    ]
    instructions: Annotated[
        Optional[str],
        Field(description="Task's instructions"),
    ] = None
    status: Annotated[
        TaskStatus, Field(default=TaskStatus.TODO, description="Task's current status")
    ]
    completed_at: Annotated[
        Optional[datetime], Field(description="When the task was completed")
    ] = None
    value: Annotated[
        Optional[int],
        Field(description="What was the grade obtained on the assignment?"),
    ] = None

    @model_validator(mode="after")
    def validate_task(self):
        # If completed_at has a date, then status is TaskStatus.DONE
        if self.completed_at:
            self.status = TaskStatus.DONE

        # If status is DONE, then completed_at is now
        if self.status == TaskStatus.DONE:
            self.completed_at = datetime.now()

        # Has the task expired?
        if self.due_date <= datetime.now():
            raise ValueError("The task is already expired")

        return self
