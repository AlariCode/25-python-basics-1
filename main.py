
def main():
    print("Task менеджер. help - для справки")
    while True:
        raw = input("> ").strip()
        parts = raw.split()
        cmd, args = parts[0], parts[1:]
        match cmd:
            case "help":
                pass
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


main()
