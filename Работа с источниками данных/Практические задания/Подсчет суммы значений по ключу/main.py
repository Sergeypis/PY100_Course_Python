import json


FILENAME = "input.json"


def task() -> int:
    # TODO Десериализуйте содержимое JSON файла
    # with open(FILENAME, "r", encoding="utf-8") as json_file:
        # appeals = 0
        # json_data = json.load(json_file)
        # for item in json_data:
        #     appeals += item.get("contains_improvement_appeals")
        # return appeals
    with open(FILENAME, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        appeals_list = [item["contains_improvement_appeals"] for item in json_data]
        return sum(appeals_list)

    # TODO Просуммируйте все значения по ключу contains_improvement_appeals


if __name__ == '__main__':
    print(task())
