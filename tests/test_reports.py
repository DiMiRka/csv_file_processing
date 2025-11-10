import pytest
from reports import average_rating_report
from utils import print_table


@pytest.fixture
def sample_data(tmp_path):
    """Создаёт временные CSV-файлы для тестов."""
    data1 = tmp_path / "products1.csv"
    data2 = tmp_path / "products2.csv"

    data1.write_text("name,brand,price,rating\niphone,apple,999,4.9\ngalaxy,samsung,899,4.8\n")
    data2.write_text("name,brand,price,rating\nredmi,xiaomi,199,4.6\nmacbook,apple,1999,4.2\n")

    return [str(data1), str(data2)]


def test_average_rating_report(sample_data):
    """Проверяет корректность формирования отчёта по среднему рейтингу."""
    result = average_rating_report.generate(sample_data)
    assert isinstance(result, list)
    assert all("brand" in row and "rating" in row for row in result)
    assert result[0]["brand"] == "apple"
    assert round(result[0]["rating"], 2) == 4.55


@pytest.mark.parametrize("tablefmt", ["simple_outline", "github"])
def test_print_table_formats(capsys, tablefmt):
    """Проверяет вывод таблицы в разных форматах."""
    data = [
        {"brand": "apple", "rating": 4.55},
        {"brand": "samsung", "rating": 4.53},
    ]
    print_table(data)
    output = capsys.readouterr().out
    assert "apple" in output
    assert "samsung" in output
    assert "|" in output  # таблица имеет формат