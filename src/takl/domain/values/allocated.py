from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Allocated:
    minutes: int

    def _validate_allocation(self):
        if not isinstance(self.minutes, int):
            raise ValueError('Time allocated must be of type "int"')

        if self.minutes <= 0:
            raise ValueError("Time allocated must be positive")


    def __post_init__(self):
        self._validate_allocation()

