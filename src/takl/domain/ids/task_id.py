from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class TaskID:
    value: UUID

    @classmethod
    def new(cls) -> "TaskID":
        return cls(uuid4())

    @classmethod
    def from_string(cls, value: str) -> "TaskID":
        return cls(UUID(value))

    def __str__(self) -> str:
        return str(self.value)
