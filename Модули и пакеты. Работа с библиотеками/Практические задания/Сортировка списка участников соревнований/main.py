# TODO Напишите функцию sort_participants
from pprint import pprint

def sort_participants(person_list: list[dict]) -> list[dict]:
    """Функция сортирует по имени список участников соревнований"""
    return sorted(person_list, key=lambda x: x["name"])


if __name__ == "__main__":
    participants_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    # pprint(sort_participants(participants_list))
    print(sort_participants(participants_list))
