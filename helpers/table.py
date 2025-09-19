"""Модуль для получения таблицы"""
from datetime import date
from tasks.tasks import Task


def format_date(d: date) -> str:
    return date.strftime(d, "%Y-%m-%D")


def stringify_table(tasks: list[Task]) -> str:
    headers = ["ID", "Название", "Статус", "Приоритет", "Теги", "Дата"]
    rows = []
    for task in tasks:
        tags = ",".join(sorted(task["tags"])) if task["tags"] else "-"
        rows.append([
            str(task["id"]),
            task["title"],
            task["status"],
            task["priority"],
            tags,
            format_date(task["due"]) if task["due"] else "-"
        ])

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, col in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(col)))

    def fmt_row(row):
        return " | ".join(f"{col:<{col_widths[i]}}" for i, col in enumerate(row))

    out = []
    out.append(fmt_row(headers))
    out.append("-+-".join("-" * w for w in col_widths))
    for row in rows:
        out.append(fmt_row(row))
    return "\n".join(out)
