from dataclasses import dataclass
from datetime import datetime
from ..values.allocated import Allocated
from ..values.deadline import Deadline
from ..values.scheduled import Scheduled
from ..values.timerange import TimeRange
from ..ids.session_id import SessionID
from ..ids.task_id import TaskID
from ..errors import SessionError


@dataclass(slots=True)
class Session:
    _id: SessionID
    _task: TaskID
    
    _allocated_time: Allocated | None = None
    _curfew: Deadline | None = None
    _scheduled_for: Scheduled | None = None

    _time_range: TimeRange | None = None

    @property
    def id(self):
        return self._id

    @property
    def task(self):
        return self._task

    @property
    def allocated_time(self):
        return self._allocated_time

    @property
    def curfew(self):
        return self._curfew

    @property
    def scheduled_for(self):
        return self._scheduled_for

    @property
    def time_range(self):
        return self._time_range

    @property
    def started(self):
        if self._time_range and self._time_range.started:
            return self._time_range.started

    @property
    def finished(self):
        if self._time_range and self._time_range.finished:
            return self._time_range.finished


    # Business Logic:

    @classmethod
    def plan(
             cls, 
             session_id: SessionID,
             task_id: TaskID,
             scheduled_for: Scheduled,
             allocated_time: Allocated | None = None,
             curfew: Deadline | None = None
            ):

        new_planned_session =  cls(
                                   _id=session_id,
                                   _task=task_id,
                                   _allocated_time=allocated_time,
                                   _curfew=curfew,
                                   _scheduled_for=scheduled_for,
                                   _time_range=None
                                  )

        new_planned_session._validate_plan()

        return new_planned_session


    @classmethod
    def start(
              cls, 
              session_id: SessionID,
              task_id: TaskID,
              start_time: datetime,
              allocated_time: Allocated | None = None,
              curfew: Deadline | None = None,
              scheduled_for: Scheduled | None = None
             ):

        time_range = TimeRange(start_time)

        started_session = cls(
                              _id=session_id,
                              _task=task_id,
                              _allocated_time=allocated_time,
                              _curfew=curfew,
                              _scheduled_for=scheduled_for,
                              _time_range=time_range
                             )

        started_session._validate_start()

        return started_session


    def finish(self, now: datetime):
        if self._validate_finish(now):
            self._time_range = TimeRange(
                                   started=self.started,
                                   finished=now
                                  )


    def reassign(self, task_id: TaskID):
        if self._validate_task(task_id):
            self._task = task_id


    def allocate_time_needed(self, allocation: Allocated):
        if self._validate_allocation(allocation):
            self._allocated_time = allocation


    def set_curfew(self, curfew: Deadline):
        if self._validate_curfew(curfew):
            self._curfew = curfew


    # Aggregate Rules:

    def _validate_id(self, session_id):
        if not isinstance(session_id, SessionID):
            raise SessionError('Session ID must be of type "SessionID"')
        return True


    def _validate_task(self, parent):
        if not isinstance(parent, TaskID):
            raise SessionError('Session parent must be of type "TaskID"')

        # rules/situations to consider (possibly for higher layer):
        # - assigned to a parent which is already complete

        return True


    def _validate_allocation(self, allocation):
        if not isinstance(allocation, Allocated) \
        and not allocation == None:
            raise SessionError('Time allocated must be of type "Allocated" or None')

        # rules/situations to consider (possibly for higher layer):
        # - session allocated (schedule + allocate) to finish after curfew 

        return True


    def _validate_curfew(self, deadline):
        if not isinstance(deadline, Deadline) \
        and not deadline == None:
            raise SessionError('Session curfew must be of type "Deadline" or None')

        if deadline and deadline < self.started:
            raise SessionError("Session deadline cannot be before it started")

        # rules/situations to consider (possibly for higher layer):
        # - scheduled to start after curfew 

        return True


    def _validate_schedule(self, schedule):
        if not isinstance(schedule, Scheduled) \
        and not schedule == None:
            raise SessionError('Session schedule must be of type "Scheduled" or None')

        return True


    def _validate_timerange(self, timerange):
        if not isinstance(timerange, TimeRange) \
        and not timerange == None:
            raise SessionError('Session time range must be of type "TimeRange"')

        if timerange and self.curfew and timerange.started > self.curfew:
            raise SessionError('Session cannot start after its deadline')

        # rules/situations to consider (possibly for higher layer):
        # - session started before scheduled start time
        # - session finished before scheduled start time
        # - sessin finished after curfew

        return True


    def _validate_plan(self):
        if not isinstance(self.scheduled_for, Scheduled):
            raise SessionError('Session cannot be fully planned without a scheduled start-time of type "Scheduled"')


    def _validate_start(self):
        if not isinstance(self._time_range.started, datetime):
            raise SessionError('Session cannot be started without a start time')

        if isinstance(self._time_range.finished, datetime):
            raise SessionError('Session already finished')


    def _validate_finish(self, finish_time):
        if not self.finished == None:
            raise SessionError("Session already finished")

        if finish_time and finish_time <= self.started:
            raise SessionError("Session finish must be after it's start-time")
        return True


    def __post_init__(self):
        self._validate_id(self._id)
        self._validate_task(self._task)
        self._validate_allocation(self._allocated_time)
        self._validate_curfew(self._curfew)
        self._validate_schedule(self._scheduled_for)
        self._validate_timerange(self._time_range)
