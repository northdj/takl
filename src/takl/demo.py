from takl import (Area, Task, Session,
                  AreaID, TaskID, SessionID,
                  AreaError, TaskError, SessionError,
                  Title, Birth, Completed, Deadline,
                  Description, Estimated, Allocated,
                  TaskPriority, Scheduled, TimeRange 
                 )

from datetime import datetime, UTC


def takl_header():
    print("\033[2J\033[H\n :: TAKL ::\n v0.1\n\n")

def now():
    return datetime.now(UTC)


def demo():
    timestamp = now()

    area_id = AreaID.new()
    task_id = TaskID.new()
    session_id = SessionID.new()

    area_name = "Area ONE"
    task_name = "Task ONE"

    area = Area.create(
                       area_id=area_id,
                       name=Title(area_name),
                       created_at=Birth(timestamp)
                      )

    task = Task.create(
                       task_id=task_id,
                       name=Title(task_name),
                       created_at=Birth(timestamp),
                       area_id=area.id,
                       priority=TaskPriority(1)
                      )

    session = Session.start(
                           session_id=session_id,
                           task_id=task.id,
                           start_time=timestamp
                          )

    return area, task, session

def show_area(area):
    print("AREA\n----")
    print(f"name: \"{area.name}\"\n  id: {area.id}\n\n")

def show_task(task):
    print("TASK\n----")
    print(f"name: \"{task.name}\"\n  id: {task.id}\n"\
            f" pid: {task.area}\n\n")

def show_session(session):
    print("SESSION\n-------")
    print(f"  id: {session.id}\n"\
            f" pid: {session.task}\n"\
            f" session started at: {session.started}\n\n")


def main():
    takl_header()
    area, task, session = demo()
    show_area(area)
    show_task(task)
    show_session(session)

def interactive_demo():
    takl_header()
    return demo() 


if __name__ == "__main__":
    area, task, session = interactive_demo()


