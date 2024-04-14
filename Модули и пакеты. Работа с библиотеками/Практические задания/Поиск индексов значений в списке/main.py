# TODO написать функцию index
from typing import Any


def index(list_: list, val_: Any) -> list:
    """Функция возвращает все индексы значения в списке"""
    if val_ not in list_:
        raise ValueError(f"Значение {val_} отсутствует в списке {list_}")
    return [index_ for index_, value in enumerate(list_) if value == val_]


if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
