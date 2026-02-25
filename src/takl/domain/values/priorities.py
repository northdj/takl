from enum import Enum, IntEnum

class TaskPriority(IntEnum):
    TO_DO = 1
    TODAY = 2
    ASAP = 3
    NEXT = 4
    NOW = 5

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class ProductionStatus(IntEnum):
    PRE_PRODUCTION = 1
    IN_PRODUCTION = 2
    POST_PRODUCTION = 3

