from random import randint


# def get_unique_list_numbers() -> list[int]:
#     """Функция для получения списка из 15 уникальных целых чисел от -10 до 10"""
#     random_list = []
#     list_size = 15
#     while len(random_list) != list_size:
#         num = randint(-10, 10)
#         if num not in random_list:
#             random_list.append(num)
#
#     return random_list

def get_unique_list_numbers() -> list[int]:
    """Функция для получения списка из 15 уникальных целых чисел от -10 до 10"""
    random_set = set()
    set_size = 15
    while len(random_set) != set_size:
        random_set.add(randint(-10, 10))

    return list(random_set)


if __name__ == "__main__":
    list_unique_numbers = get_unique_list_numbers()
    print(list_unique_numbers)
    print(len(list_unique_numbers) == len(set(list_unique_numbers)))
