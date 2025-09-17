
from typing import TypedDict


class Task(TypedDict):
    id: int
    title: str
    priority: str
    status: str


t: Task = {
    "id": 1,
    "title": "Вытерить пыль",
    "priority": "low",
    "status": "new"
}
