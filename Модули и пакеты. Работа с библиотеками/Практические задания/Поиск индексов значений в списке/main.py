# TODO написать функцию index
from typing import Any


def index(list_: list, val: Any) -> list[int]:
    """Функция находит индексы определенного значения в списке"""
    if val not in list_:
        raise ValueError(f"Ошибка!!! Значение {val} не найдено в списке {list_}.")
    return [index for index, value in enumerate(list_) if value == val]


if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
