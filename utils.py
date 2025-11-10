import csv
from typing import List, Dict

from tabulate import tabulate


def read_csv_files(file_list: List[str]) -> List[Dict[str, str]]:
    data: List[Dict[str, str]] = []
    for file in file_list:
        try:
            with open(file, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data.extend(list(reader))
        except FileNotFoundError:
            print(f"Файл {file} не найден")
    return data


def print_table(data: List[Dict], report: str) -> None:
    if not data:
        print("Нет данных для отображения.")
        return

    for i, row in enumerate(data, 1):
        row["№"] = i

    ordered_data: List[Dict]
    if report == "average-rating":
        ordered_data = [
            {"№": row["№"], "brand": row["brand"], "rating": row["rating"]} for row in data
        ]
    elif report == "average-price":
        ordered_data = [
            {"№": row["№"], "brand": row["brand"], "prise": row["prise"]} for row in data
        ]

    print(
        tabulate(
            ordered_data,
            headers="keys",
            tablefmt="simple_outline",
            numalign="center",
            stralign="center",
        )
    )
