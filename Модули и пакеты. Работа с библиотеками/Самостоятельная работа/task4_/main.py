from typing import Any


# TODO написать функцию remove
def remove(list_: list, value: Any) -> list:
    """Функция удаляет последнее искомое значение из списка"""
    if value not in list_:
        raise ValueError(f"Значение {value} не найдено в списке {list_}")

    list_ = list_[::-1].copy()
    del list_[list_.index(value)]
    return list_[::-1]


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
