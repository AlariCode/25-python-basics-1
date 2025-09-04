# Посчитать для каждого дня - всего визитой, уникальных визитов
# Найти ID, кто посетили оба дня
# Найти ID, кто посетили только первый день
# Найти ID, кто посетили только второй день
# Найти ID, кто были только 1 раз

visitors_day1 = [101, 102, 103, 101, 104, 102, 105, 101]
visitors_day2 = [101, 108, 100, 101, 105, 107]

u_visitors_day1 = set(visitors_day1)
u_visitors_day2 = set(visitors_day2)

print(
    f"Входов день 1: {len(visitors_day1)}, уникальных {len(u_visitors_day1)}")
print(
    f"Входов день 2: {len(visitors_day2)}, уникальных {len(u_visitors_day2)}")

print("Были оба дня: ", u_visitors_day1 & u_visitors_day2)
print("Были в первый день: ", u_visitors_day1 - u_visitors_day2)
print("Были во второй день: ", u_visitors_day2 - u_visitors_day1)
print("Были в один из дней: ", u_visitors_day2 ^ u_visitors_day1)
