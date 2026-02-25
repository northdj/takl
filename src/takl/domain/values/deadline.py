from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class Deadline:
    date: datetime

    def _validate_deadline(self):
        if not isinstance(self.date, datetime):
            raise ValueError('Deadline must be of type "datetime"')

    def __post_init__(self):
        self._validate_deadline()
