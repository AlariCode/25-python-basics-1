# Список покупок
# 	1.	Общую сумму всех заказов.
#   2.	Количество всех проданных товаров.

from functools import reduce


orders = [
    {"id": 1, "user": "Anton", "items": [
        {"name": "Laptop", "price": 1000},
        {"name": "Mouse", "price": 50}
    ]},
    {"id": 2, "user": "Kate", "items": [
        {"name": "Phone", "price": 700}
    ]},
    {"id": 3, "user": "Oleg", "items": [
        {"name": "Monitor", "price": 300},
        {"name": "Keyboard", "price": 100}
    ]}
]
# {"total_price": 1000, "total_items": 10}


def aggregate(acc: dict, order: dict) -> dict:
    order_sum = sum(item["price"] for item in order["items"])
    order_count = len(order["items"])
    return {
        "total_price": acc["total_price"] + order_sum,
        "total_items": acc["total_items"] + order_count
    }


result = reduce(aggregate, orders, {"total_price": 0,  "total_items": 0})
print(result)
