from shlex import split
from commands.help import help_command
from commands.add import add_command
from commands.list import list_command
from tasks.tasks import Task
from storage.file import save_tasks, load_tasks


def main():
    file_path = "tasks.json"
    tasks, next_id = load_tasks(file_path)
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
                    list_command(tasks, args)
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
    main()
    # FileNotFoundError
    # json.JSONDecodeError
