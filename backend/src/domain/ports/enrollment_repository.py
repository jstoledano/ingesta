from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from domain.models.enrollment import Enrollment


class EnrollmentRepository(ABC):
    """
    Abstract class for enrollment repository.
    In DDD y HA is the port (interface) implemented by the protocol.
    """

    @abstractmethod
    async def save(self, enroll: Enrollment) -> Enrollment:
        """Persist a new enrollment update a new one."""
        pass

    @abstractmethod
    async def get_by_id(self, enroll_id: UUID) -> Optional[Enrollment]:
        """Retrieves an Enrollment by its unique ID."""
        pass

    @abstractmethod
    async def get_by_period(self, period: str) -> Optional[List[Enrollment]]:
        """Retrieves a list os Subjects enrolled in a given period."""
        pass

    @abstractmethod
    async def get_by_status(self, status: int) -> Optional[List[Enrollment]]:
        """Retrieves a list os Subjects enrolled in a given status."""
        pass
