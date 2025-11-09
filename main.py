import argparse
from reports.average_rating import AverageRatingReport
from utils import read_csv_files, print_table
from exceptions import UnsupportedReportError


def main():
    parser = argparse.ArgumentParser(description="Обработка csv файлов")
    parser.add_argument("--files", nargs="+", required=True, help="Путь к файлу/файлам")
    parser.add_argument("--report", required=True, choices=["average-rating"], help="Тип отчета")
    args = parser.parse_args()

    data = read_csv_files(args.files)

    if args.report == "average-rating":
        report = AverageRatingReport()
        result = report.generate(data)
        print_table(result)
    else:
        raise UnsupportedReportError(f"Неизвестный тип отчета: {args.report}")


if __name__ == "__main__":
    main()
