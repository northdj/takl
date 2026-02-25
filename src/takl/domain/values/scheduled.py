from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class Scheduled:
    start_time: datetime

    def _validate_schedule(self):
        if not isinstance(self.start_time, datetime):
            raise ValueError('Scheduled start-time must be of type "datetime"')

    def __post_init__(self):
        self._validate_schedule()
