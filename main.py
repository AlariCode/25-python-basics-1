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
    # %Y - 2025 год
    # %y - 25 год
    # %m - 08 месяцы
    # %d - 19 дни
    # %H - 20 часы
    # %M - 10 минуты
    # %S - 02 секунды
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

    s = "2025-09-17 18:44"
    dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M")
    print(dt)
