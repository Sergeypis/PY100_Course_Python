import json


FILENAME = "input.json"


def task() -> list[dict]:
    with open(FILENAME) as f:
        json_data = json.load(f)
        return sorted(json_data, key=lambda item: item["id"])

    # TODO отсортировать и вернуть список словарей


if __name__ == '__main__':
    # Необходимо для проверки
    data = task()
    print(json.dumps(data, indent=4))
