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
    now = datetime.datetime.now()
    print(now)
    today = datetime.date.today()
    print(today)
    current_time = now.time()
    print(current_time)

    d = datetime.date(2025, 9, 17)
    print(d.weekday())
    print(d)
    t = datetime.time(19, 0, 45)
    print(t)
    dt = datetime.datetime(2025, 9, 17, 19, 0, 45)
    print(dt)
