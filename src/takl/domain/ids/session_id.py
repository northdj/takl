from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class SessionID:
    value: UUID

    @classmethod
    def new(cls) -> "SessionID":
        return cls(uuid4())

    @classmethod
    def from_string(cls, value: str) -> "SessionID":
        return cls(UUID(value))

    def __str__(self) -> str:
        return str(self.value)
