"""Модуль для добавления команды"""
from tasks.tasks import Task, make_task
from helpers.args import parse_add


def add_command(tasks: list[Task], args: list[str], next_id: int) -> int:
    try:
        title, prio, due, tags = parse_add(args)
        task = make_task(1, title, due, prio, tags)
        tasks.append(task)
        print("Добавлена задача")
        print(task)
        return next_id + 1
    except ValueError as e:
        print(f"Ошибка {e}")
        return next_id
