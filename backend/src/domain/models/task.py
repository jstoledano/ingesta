from datetime import datetime
from enum import IntEnum
from typing import Annotated, Optional
from uuid import uuid4

from pydantic import UUID4, BaseModel, ConfigDict, Field, model_validator, ValidationError


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
                "date_due": "2026-01-30T22:59:00",
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
        Field(min_length=10, max_length=100, description="Task title"),
    ]
    instructions: Annotated[
        Optional[str],
        Field(optional=None, description="Task's instructions"),
    ]
    status: Annotated[
        TaskStatus, Field(default=TaskStatus.TODO, description="Task's current status")
    ]
    completed_at: Annotated[
        Optional[datetime], Field(default=None, description="When the task was completed")
    ]
    value: Annotated[
        Optional[int],
        Field(default=None, description="What was the grade obtained on the assignment?"),
    ]

    @model_validator(mode="after")
    def validate_task_consistency(self):
        # Rule 1: If is DONE, must have a completed_ad timestamp
        if self.status == TaskStatus.DONE:
            if self.completed_at is None:
                raise ValidationError("Task is DONE but lacks of a completed date")

        # Rule 2: If is not DONE, completed_at must be None
        if self.status != TaskStatus.DONE:
            if self.completed_at is not None:
                raise ValidationError("Task is DONE but task has completed timestamp")

        return self
