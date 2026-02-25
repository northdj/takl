
# TAKL Engine

> Version 0.1.0
> Status: Experimental


## Overview

***TAKL*** is a domain-driven task and time tracking engine written in Python.

The goal of this project is to explore clean architecture, domain modelling,
and temporal analysis of work through sessions of focused activity.

This repository contains the **core domain model** only.
Application services, persistence, and user interfaces are introduced in later versions.

---

## Philosophy

***TAKL*** is built around three core concepts:

- **Areas** — spaces of responsibility
- **Tasks** — intentional goals within an area
- **Sessions** — time spent executing tasks

Sessions provide the factual timeline that enables planning,
execution tracking, and later analysis.

---

## Design Goals

* Strong domain boundaries
* Immutable value objects
* Explicit invariants
* Replaceable infrastructure
* Testable business logic
* Temporal analytics capability

---

## Architecture

TAKL follows a layered architecture inspired by Clean Architecture and Domain-Driven Design:

- **Domain** contains the core business model (entities and value objects)
- **Application** orchestrates use-cases
- **Infrastructure** provides persistence and external integrations
- **UI** interacts with the system through application use-cases

**UI → Application → Domain ← Infrastructure**

Dependencies always point inward toward the domain layer, which contains no I/O, no framework dependencies, and no knowledge of persistence.

---

## Why?

Most productivity tools track tasks. Few track time spent in a structured, analyzable way.

***TAKL*** aims to combine *task management*, *time tracking*, and *behavioral insight* into a cohesive engine.

---

## Current Status (v0.1)
- v0.1 — Domain Model

### Implemented:

- Entities
  - Task
  - Session
  - Area

- Value Objects
  - IDs (UUID-based)
  - Title / Description
  - TimeRange
  - Birth / Completed
  - Deadline / Scheduled
  - Estimated / Allocated
  - TaskPriority

- Aggregate invariants
- Domain errors

### Planned:

- v0.2 — Application Use-Cases
- v0.3 — Repository + SQLite Persistence
- v0.4 — CLI / TUI Interface
- v0.5 — Analysis and Reporting Features
- v0.6 — API

---

## Example

```python
from datetime import datetime, UTC
from takl import (Area, Task, Session,
                  AreaID, TaskID, SessionID,
                  Title, Birth, TaskPriority
                 )

area = Area.create(
    area_id=AreaID.new(),
    name=Title("Takl Project"),
    created_at=Birth(datetime.now(UTC))
)

task = Task.create(
    task_id=TaskID.new(),
    name=Title("Write documentation"),
    created_at=Birth(datetime.now(UTC)),
    area_id=area.id,
    priority=TaskPriority(1)
)

session = Session.start(
    session_id=SessionID.new(),
    task_id=task.id,
    start_time=datetime.now(UTC)
)
```
---


## Installation

Requires Python 3.11+
To install in development mode:
```
git clone https://github.com/northdj/takl
cd takl
pip install -e .
```

---

## Running TAKL

TAKL can be used in three ways: as a command-line tool, as a Python module, or interactively for experimentation.  
  
**Command Line:**

After installation:
```
takl
```
or:
```
python -m takl
```
Both commands execute the built-in demo and print example objects.  
  
  
**Interactive Exploration:**

For experimentation during development:
```
python -i src/takl/demo.py
```

This launches Python with pre-created domain objects:
```
area
task
session
```

You can then inspect or modify them directly:
```python
>>> area.name
>>> task.priority
>>> session.started
```  
  
  
**Using as a Library:**

TAKL can also be imported into your own projects:
```python
from takl import Area, Task, Session
```  
  
---

## Tests

Run:
```
pytest
```

---

## License

MIT — see LICENSE
