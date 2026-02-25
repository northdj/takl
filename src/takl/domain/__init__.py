"""
TAKL Domain Layer

This package contains the core business model:

Entities:
    - Area
    - Task
    - Session

Value Objects:
    - Title
    - Description
    - TimeRange
    - Birth
    - Deadline
    - Scheduled
    - Estimated
    - Allocated
    - Completed
    - TaskPriority

Identifiers:
    - AreaID
    - TaskID
    - SessionID

Errors:
    - AreaError
    - TaskError
    - SessionError
"""

__version__ = "0.1.0"


# ========================
# Entities
# ========================

from .entities.area import Area
from .entities.task import Task
from .entities.session import Session


# ========================
# IDs
# ========================

from .ids.area_id import AreaID
from .ids.task_id import TaskID
from .ids.session_id import SessionID


# ========================
# Values
# ========================

from .values.title import Title
from .values.description import Description

from .values.birth import Birth
from .values.completed import Completed
from .values.deadline import Deadline
from .values.scheduled import Scheduled

from .values.estimated import Estimated
from .values.allocated import Allocated

from .values.timerange import TimeRange

from .values.priorities import TaskPriority


# ========================
# Errors
# ========================

from .errors import AreaError, TaskError, SessionError


# ========================
# Public API
# ========================

__all__ = [
    # Entities
    "Area",
    "Task",
    "Session",

    # IDs
    "AreaID",
    "TaskID",
    "SessionID",

    # Values
    "Title",
    "Description",
    "Birth",
    "Completed",
    "Deadline",
    "Scheduled",
    "Estimated",
    "Allocated",
    "TimeRange",
    "TaskPriority",

    # Errors
    "AreaError",
    "TaskError",
    "SessionError",
]
