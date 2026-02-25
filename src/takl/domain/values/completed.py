from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class Completed:
    in_full: datetime

    def _validate_completion(self):
        if not isinstance(self.in_full, datetime):
            raise ValueError('Completion time must be of type "datetime"')

    def __post_init__(self):
        self._validate_completion()

