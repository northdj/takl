from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class TimeRange:
    started: datetime | None = None
    finished: datetime | None = None

    def _validate_start_time(self):
        if not isinstance(self.started, datetime):
            raise ValueError('Time range start-time must be of type "datetime"')

        if self.finished and self.started > self.finished:
            raise ValueError('Time range start-time cannot be after finish-time')


    def _validate_finish_time(self):
        if not isinstance(self.finished, datetime) \
        and not self.finished == None:
            raise ValueError('Time range finish-time must be of type "datetime"')

        if not self.started:
            raise ValueError('Time range finish-time cannot be set without a start-time')



    def __post_init__(self):
        self._validate_start_time()
        self._validate_finish_time()

