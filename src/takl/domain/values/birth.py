from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Birth:
    birth: datetime

    def _validate_birth(self):
        if not isinstance(self.birth, datetime):
            raise ValueError('Birth must be of type "datetime"')

    def __post_init__(self):
        self._validate_birth()
