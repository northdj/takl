from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Estimated:
    minutes: int

    def _validate_estimate(self):
        if not isinstance(self.minutes, int):
            raise ValueError('Time estimated must be of type "int"')

        if self.minutes <= 0:
            raise ValueError("Time estimated must be positive")


    def __post_init__(self):
        self._validate_estimate()

