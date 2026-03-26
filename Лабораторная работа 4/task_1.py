# TODO решите задачу
import json

# TODO решите задачу
def task() -> float:
    with open("input.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # Используем sum и генератор для вычисления суммы произведений
    return round(sum([item["score"] * item["weight"] for item in json_data]), 3)


print(task())