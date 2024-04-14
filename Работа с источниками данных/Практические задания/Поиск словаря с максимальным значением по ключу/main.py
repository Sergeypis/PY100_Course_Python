import json


FILENAME = "input.json"


def task() -> dict:
    # TODO считать содержимое JSON файла
    with open(FILENAME, "r") as input_json:
        json_data = json.load(input_json)
        return max(json_data, key=lambda x: x["score"])

    # TODO найти максимальный элемент по ключу score


if __name__ == '__main__':
    print(task())
