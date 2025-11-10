import argparse
from reports import average_rating_report, average_rating_price
from utils import read_csv_files, print_table
from exceptions import UnsupportedReportError


def main():
    parser = argparse.ArgumentParser(description="Обработка csv файлов")
    parser.add_argument("--files", nargs="+", required=True, help="Путь к файлу/файлам")
    parser.add_argument(
        "--report", required=True, choices=["average-rating", "average-price"], help="Тип отчета"
    )
    args = parser.parse_args()

    data = read_csv_files(args.files)

    if args.report == "average-rating":
        result = average_rating_report.generate(data)
        print_table(result, args.report)
    elif args.report == "average-price":
        result = average_rating_price.generate(data)
        print_table(result, args.report)
    else:
        raise UnsupportedReportError(f"Неизвестный тип отчета: {args.report}")


if __name__ == "__main__":
    main()
