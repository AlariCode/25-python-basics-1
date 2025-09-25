import json
from shlex import split
from commands.help import help_command
from commands.add import add_command
from tasks.tasks import Task


def main():
    tasks: list[Task] = []
    next_id = 1
    print("Task менеджер. help - для справки")
    while True:
        try:
            raw = input("> ").strip()
            parts = split(raw)
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
                    help_command()
                case "add":
                    next_id = add_command(tasks, args, next_id)
                case "list":
                    pass
                case "remove":
                    pass
                case "edit":
                    pass
                case "tags":
                    pass
                case "exit":
                    break
                case _:
                    print("Неизвестная команда")
        except KeyboardInterrupt:
            print("\nЗавершение приложения...")
            break
        except Exception as e:
            print(f"[ERROR]: {e}")


if __name__ == "__main__":
    # main()
    # res = json.dumps({"a": True, "b": [1, 2, 3]})
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump({"id": 1, "title": "Задача"},
                  f, ensure_ascii=False, indent=2)
