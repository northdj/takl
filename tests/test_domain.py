import pytest
from datetime import datetime, UTC

from takl import (Area, Task, Session,
                  Title, Birth, TaskPriority, Scheduled, 
                  AreaID, TaskID, SessionID,
                  AreaError, TaskError, SessionError
                 )


clock = datetime

def test_create_area():
    assert Area.create(
                       AreaID.new(), Title('Test Area'), 
                       Birth(clock.now(UTC)), None, None
                      ).name == 'Test Area'

def test_create_task():
    assert Task.create(
                       TaskID.new(), Title('New Task'), Birth(clock.now(UTC)), 
                       AreaID.new(), TaskPriority(3)
                      ).name == 'New Task'


def test_session_plan():
    now = clock.now(UTC)
    assert Session.plan(
                        SessionID.new(), TaskID.new(),
                        Scheduled(now.replace(year=now.year+1))
                       ).scheduled_for.start_time.month == now.month


def test_start_session():
    assert Session.start(
                         SessionID.new(), TaskID.new(),
                         clock.now(UTC)
                        ).finished == None


def test_area_cannot_parent_itself():
    area = Area.create(
                       AreaID.new(), Title('Test Area'), 
                       Birth(clock.now(UTC)), None, None
                      )

    with pytest.raises(AreaError):
        area.assign_to_area(area.id)


def test_task_cannot_parent_itself():
    task = Task.create(
                       TaskID.new(), Title('New Task'), Birth(clock.now(UTC)), 
                       AreaID.new(), TaskPriority(3)
                      )

    with pytest.raises(TaskError):
        task.assign_to_parent_task(task.id)


def test_task_rejects_area_id_as_parent_task():
    task = Task.create(
                       TaskID.new(), Title('New Task'), Birth(clock.now(UTC)), 
                       AreaID.new(), TaskPriority(3)
                      )

    area_id = AreaID.new()

    with pytest.raises(TaskError):
        task.assign_to_parent_task(area_id)
