from dataclasses import dataclass
from ..values.title import Title
from ..values.birth import Birth
from ..values.completed import Completed
from ..values.estimated import Estimated
from ..values.deadline import Deadline
from ..values.priorities import TaskPriority 
from ..values.description import Description
from ..ids.task_id import TaskID
from ..ids.area_id import AreaID
from ..errors import TaskError


@dataclass(slots=True)
class Task:
    _id: TaskID
    _name: Title
    _created_at: Birth

    _area: AreaID
    _priority: TaskPriority

    _parent: TaskID | None = None

    _completed: Completed | None = None
    _estimated_time: Estimated | None = None
    _deadline: Deadline | None = None

    _description: Description | None = None
    # checklist_items: List[ChecklistItem]


    # Attributes:

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def area(self):
        return self._area

    @property
    def parent(self):
        return self._parent

    @property
    def created_at(self):
        return self._created_at

    @property
    def completed(self):
        return self._completed

    @property
    def estimated_time(self):
        return self._estimated_time

    @property
    def deadline(self):
        return self._deadline

    @property
    def priority(self):
        return self._priority

    @property
    def description(self):
        return self._description


    # Business Logic:

    @classmethod
    def create(
               cls,
               task_id: TaskID,
               name: Title,
               created_at: Birth,
               area_id: AreaID,
               priority: TaskPriority,
               parent_id: TaskID | None = None,
               completed: Completed | None = None,
               estimated_time: Estimated | None = None,
               deadline: Deadline | None = None,
               description: Description | None = None
              ):

        return cls(
                   _id=task_id,
                   _name=name,
                   _created_at=created_at,
                   _area=area_id,
                   _priority=priority,
                   _parent=parent_id,
                   _completed=completed,
                   _estimated_time=estimated_time,
                   _deadline=deadline,
                   _description=description
                  )

    def rename(self, new_name: Title):
        if self._validate_name(new_name):
            self._name = new_name

    def assign_to_area(self, area_id: AreaID):
        if self._validate_area(area_id):
            self._area = area_id

    def assign_to_parent_task(self, task_id: TaskID):
        if self._validate_parent(task_id):
            self._parent = task_id

    def complete(self, completion_time):
        if self._validate_completion(completion_time):
            self._completed = completion_time

    def estimate_time_needed(self, estimate):
        if self._validate_estimate(estimate):
            self._estimated_time = estimate

    def set_deadline(self, deadline):
        if self._validate_deadline(deadline):
            self._deadline = deadline

    def update_priority(self, priority):
        if self._validate_priority(priority):
            self._priority = priority

    def describe(self, description: Description):
        if self._validate_description(description):
            self._description = description


    # Aggregate Rules:

    def _validate_id(self, task_id):
        if not isinstance(task_id, TaskID):
            raise TaskError('Task ID must be of type "TaskID"')

        return True


    def _validate_name(self, name):
        if not isinstance(name, Title):
            raise TaskError('Task name must be of type "Title"')

        return True


    def _validate_area(self, area_id):
        if not isinstance(area_id, AreaID):
            raise TaskError('Area ID must be of type "AreaID"')

        return True


    def _validate_parent(self, parent_id):
        if not isinstance(parent_id, TaskID) \
        and not parent_id == None:
            raise TaskError('Task parent must be of type "TaskID" or None')

        if parent_id == self._id:
            raise TaskError('Task cannot parent itself')

        return True


    def _validate_birth(self, birth):
        if not isinstance(birth, Birth):
            raise TaskError('Task birth must be of type "Birth"')

        return True


    def _validate_completion(self, completed):
        if not isinstance(completed, Completed) \
        and not completed == None:
            raise TaskError('Task completion must be of type "Completed" or None')

        if completed and completed < self._created_at:
            raise TaskError('Task cannot be completed before it was created')

        # rules/situations to consider (possibly for higher layer):
        # - task completed before scheduled start
        # - task completed after deadline

        return True


    def _validate_estimate(self, estimate):
        if not isinstance(estimate, Estimated) \
        and not estimate == None:
            raise TaskError('Task estimate must be of type "Estimated" or None')

        # rules/situations to consider (possibly for higher layer):
        # - estimated to finish after deadline

        return True


    def _validate_deadline(self, deadline):
        if not isinstance(deadline, Deadline) \
        and not deadline == None:
            raise TaskError('Task deadline must be of type "Deadline" or None')

        if deadline and deadline < self._created_at:
            raise TaskError("Task deadline cannot be before it's birth")

        # rules/situations to consider (possibly for higher layer):
        # - scheduled start-time after deadline

        return True


    def _validate_priority(self, taskpriority):
        if not isinstance(taskpriority, TaskPriority):
            raise TaskError('Task priority must be of type "TaskPriority"')

        # rules/situations to consider (possibly for higher layer):
        # - deadline within 24hrs but task not prioritised

        return True


    def _validate_description(self, description):
        if not isinstance(description, Description) \
        and not description == None:
            raise TaskError('Task description must be of type "Description" or None')

        return True


    def __post_init__(self):
        self._validate_id(self._id)
        self._validate_name(self._name)
        self._validate_birth(self._created_at)
        self._validate_area(self._area)
        self._validate_priority(self._priority)
        self._validate_parent(self._parent)
        self._validate_completion(self._completed)
        self._validate_estimate(self._estimated_time)
        self._validate_deadline(self._deadline)
        self._validate_description(self._description)
