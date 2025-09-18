from commands.help import help_command
from datetime import datetime
from zoneinfo import ZoneInfo


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
    now_utc = datetime.now(ZoneInfo("UTC"))
    now = datetime.now()
    print(now)
    print(now_utc)
    now_ny = datetime.now(ZoneInfo("America/New_York"))
    print(now_ny)

    meeting = datetime(2025, 9, 17, 12, 0, tzinfo=ZoneInfo("Europe/Moscow"))
    meeting_ny = meeting.astimezone(ZoneInfo("America/New_York"))
    print(meeting_ny)
