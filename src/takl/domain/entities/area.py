from dataclasses import dataclass
from ..values.title import Title
from ..values.birth import Birth
from ..values.description import Description
from ..ids.area_id import AreaID
from ..errors import AreaError


@dataclass(slots=True)
class Area:
    _id: AreaID
    _name: Title
    _created_at: Birth
    
    _parent: AreaID | None = None
    _description: Description | None = None


    # Attributes:

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def parent(self):
        return self._parent

    @property
    def created_at(self):
        return self._created_at

    @property
    def description(self):
        return self._description


    # Business Logic

    @classmethod
    def create(
               cls,
               area_id: AreaID,
               name: Title,
               created_at: Birth,
               parent: AreaID | None = None,
               description: Description | None = None
              ):

        return cls(
                   _id=area_id,
                   _name=name,
                   _created_at=created_at,
                   _parent=parent,
                   _description=description
                  )

    def rename(self, new_name: Title):
        if self._validate_name(new_name):
            self._name = new_name

    def describe(self, description: Description):
        if self._validate_description(description):
            self._description = description

    def assign_to_area(self, area_id: AreaID):
        if self._validate_parent(area_id):
            self._parent = area_id


    # Aggregate Rules:

    def _validate_id(self, area_id):
        if not isinstance(area_id, AreaID):
            raise AreaError('Area ID must be of type "AreaID"')

        return True


    def _validate_name(self, name):
        if not isinstance(name, Title):
            raise AreaError('Area name must be of type "Title"')

        return True


    def _validate_parent(self, parent_id):
        if not isinstance(parent_id, AreaID) \
        and not parent_id == None:
            raise AreaError('Area parent must be of type "AreaID" or None')

        if parent_id == self._id:
            raise AreaError('Area cannot parent itself')

        return True


    def _validate_birth(self, birth):
        if not isinstance(birth, Birth):
            raise AreaError('Area birth must be of type "Birth"')

        return True


    def _validate_description(self, description):
        if not isinstance(description, Description) \
        and not description == None:
            raise AreaError('Area description must be of type "Description" or None')

        return True


    def __post_init__(self):
        self._validate_id(self._id)
        self._validate_name(self._name)
        self._validate_birth(self._created_at)
        self._validate_parent(self._parent)
        self._validate_description(self._description)
