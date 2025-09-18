
from typing import TypedDict, Optional

PRIORITIES = {"low", "med", "high"}


class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: Optional[list[str]]
    status: str


def make_task(id_: int, title: str, priority: str = "med", tags: Optional[list[str]] = None) -> Task:
    if priority not in PRIORITIES:
        raise ValueError("Неверный приоритет. Можно только low | med | high")
    task: Task = {
        "id": id_,
        "title": title.strip(),
        "priority": priority,
        "tags": tags,
        "status": "new"
    }
    return task
