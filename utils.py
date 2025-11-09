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


def print_table(data: List[Dict[str, str]], headers: List[str]) -> None:
    print(tabulate(data, headers=headers, tablefmt="grid"))
