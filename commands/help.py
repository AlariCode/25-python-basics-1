"""Модуль вовода помощь пользователю"""


def help_command():
    print("""Команды:
add <title> [prio=low|med|high] [due=YYYY-MM-DD] [tags=a,b,c] - Добавить
list [by=prio|due] - Показать список
done <id> - Выполнить
edit <id> [title=...] [prio=...] [due=YYYY-MM-DD] - Изменить
remove <id> - Удалить
tags <id> add|remove <tag> - Изменить теги
help - Помощь
exit - Выход
""")
