"""Модуль для редактирования задачи"""


from helpers.args import parse_edit
from helpers.table import stringify_table
from tasks.tasks import Task, update_task, find_task


def edit_command(tasks: list[Task], args: list[str]):
    task_id, changes = parse_edit(args)
    task = find_task(tasks, task_id)
    if task is None:
        print("Задача не найдена")
        return
    update_task(task, **changes)
    print(stringify_table([task]))
