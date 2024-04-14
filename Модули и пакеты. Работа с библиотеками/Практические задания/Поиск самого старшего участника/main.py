# TODO Напишите функцию get_oldest_participant
def get_oldest_participant(human_list: list[dict]) -> dict:
    """Функция находит самого старшего участника из списка"""
    return max(human_list, key=lambda human: human["age"])


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

    oldest_participant = get_oldest_participant(participants_list)  # TODO Найдите самого старшего участника
    print(oldest_participant)
