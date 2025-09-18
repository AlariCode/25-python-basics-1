from commands.help import help_command
import datetime


def main():
    print("Task менеджер. help - для справки")
    while True:
        try:
            raw = input("> ").strip()
            parts = raw.split()
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
                    help_command()
                case "add":
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
    d1 = datetime.datetime(2025, 9, 17)
    d2 = datetime.datetime(2025, 12, 31)
    print(d1 < d2)
    print(d1 == d2)
    print(d1 > d2)

    now = datetime.datetime.now()
    deadline = datetime.datetime(2025, 10, 12, 18, 0, 0)

    if now < deadline:
        print("Ещё успеваю")
    else:
        print("Опаздал")
