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
    new_year = datetime.date(2026, 1, 1)
    today = datetime.date.today()
    diff = new_year - today
    print(diff.days)
    next_week = today + datetime.timedelta(weeks=1)
    next_week2 = today + datetime.timedelta(days=7)
    print(next_week2)
    last_month = today - datetime.timedelta(days=30)
    print(last_month)
