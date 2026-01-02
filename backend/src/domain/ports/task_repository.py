from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from domain.models.task import Task


class TaskRepository(ABC):
    """
    Implements a port(interface) for task repository.
    """

    @abstractmethod
    async def save(self, task: Task) -> None:
        """Saves the task repository."""
        pass

    @abstractmethod
    async def get_by_id(self, task_id: UUID) -> Optional[Task]:
        """Retrieves a task by its ID."""
        pass

    @abstractmethod
    async def get_by_enrollment(self, enrollment_id: UUID) -> List[Task]:
        """Retrieves all task for an enrollment subject."""
        pass

    @abstractmethod
    async def get_todo_tasks(self) -> List[Task]:
        """Retrieves all task with status TO DO"""
        pass
