import json
from shlex import split
from commands.help import help_command
from commands.add import add_command
from tasks.tasks import Task
from storage.file import save_tasks


def main():
    tasks: list[Task] = []
    next_id = 1
    file_path = "tasks.json"
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
                    save_tasks(file_path, tasks)
                    break
                case _:
                    print("Неизвестная команда")
        except KeyboardInterrupt:
            save_tasks(file_path, tasks)
            print("\nЗавершение приложения...")
            break
        except Exception as e:
            save_tasks(file_path, tasks)
            print(f"[ERROR]: {e}")


if __name__ == "__main__":
    # main()
    # with open("notes.txt", "r", encoding="utf-8") as f:
    # text = f.read()
    # print(text)
    # for line in f:
    # print(">", line.rstrip())
    with open("tasks.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print(data)
