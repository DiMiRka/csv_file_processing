import argparse
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser(description="Обработка csv файлов")
    parser.add_argument("--file", nargs="+", required=True, help="Путь к файлу/файлам")
    parser.add_argument("--report", required=True, choices=["average-rating"], help="Тип отчета")
    args = parser.parse_args()

    # entries = parse_log_files(args.file, args.date)
