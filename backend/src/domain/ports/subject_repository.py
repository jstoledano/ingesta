from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from src.domain.models.subject import Subject


class SubjectRepository(ABC):
    """
    Interface (Port) for Subject data access.
    Infrastructure layer must implement this protocol.
    """

    @abstractmethod
    async def save(self, subject: Subject) -> None:
        """Persists a new Subject or updates an existing one."""
        pass

    @abstractmethod
    async def get_by_id(self, subject_id: UUID) -> Optional[Subject]:
        """Retrieves a Subject by its unique ID."""
        pass

    @abstractmethod
    async def get_by_code(self, code: str) -> Optional[Subject]:
        """Retrieves a Subject by its official code (e.g., '15141101')."""
        pass

    @abstractmethod
    async def list_all(self) -> List[Subject]:
        """Retrieves all subjects. TODO: Add pagination filters."""
        pass
