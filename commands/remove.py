"""Модуль для удаления"""

from tasks.tasks import Task, remove_task


def remove_command(tasks: list[Task], args: list[str]):
    task_id = None
    try:
        task_id = int(args[0])
    except ValueError:
        print("[ERROR]: id должен быть числом")

    if remove_task(tasks, task_id):
        print(f"Задача {task_id} удалена")
    else:
        print(f"Задача {task_id} не найдена")
