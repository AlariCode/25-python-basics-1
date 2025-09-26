
from typing import TypedDict, Optional
from datetime import date

PRIORITIES = {"low", "med", "high"}


class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: Optional[list[str]]
    status: str
    due: Optional[date]


def make_task(id_: int, title: str, due: Optional[date] = None, priority: str = "med", tags: Optional[list[str]] = None) -> Task:
    if priority not in PRIORITIES:
        raise ValueError("Неверный приоритет. Можно только low | med | high")
    task: Task = {
        "id": id_,
        "title": title.strip(),
        "priority": priority,
        "tags": tags,
        "status": "new",
        "due": due
    }
    return task


def remove_task(tasks: list[Task], task_id) -> bool:
    before_len = len(tasks)
    tasks[:] = list(filter(lambda t: t["id"] != task_id, tasks))
    return len(tasks) < before_len
