import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        lines = [row for row in reader]

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile:
        json.dump(lines, jsonfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    task()

    # Для проверки
    with open(OUTPUT_FILENAME, "r", encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
