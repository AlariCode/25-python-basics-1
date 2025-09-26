"""Модуль для редактирования задачи"""


from helpers.args import parse_edit
from helpers.table import stringify_table
from tasks.tasks import Task, update_task


def edit_command(tasks: list[Task], args: list[str]):
    task_id, changes = parse_edit(args)
    task = list(filter(lambda t: t["id"] == task_id, tasks))
    if len(task) == 0:
        print("Задача не найдена")
        return
    update_task(task[0], **changes)
    stringify_table(task)
