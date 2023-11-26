# TODO решите задачу
import json


def task() -> float:
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    need_value = sum([item["score"] * item["weight"] for item in json_data])
    return round(need_value, 3)


print(task())

