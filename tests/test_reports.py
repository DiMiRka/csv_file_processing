from typing import List, Dict

import pytest

from reports import average_rating_report, average_price_report


@pytest.fixture
def sample_data() -> List[Dict[str, str]]:
    return [
        {"brand": "apple", "rating": "4.9", "price": "1200"},
        {"brand": "apple", "rating": "4.8", "price": "1300"},
        {"brand": "samsung", "rating": "4.5", "price": "1000"},
    ]


def test_average_rating_report(sample_data):
    result = average_rating_report.generate(sample_data)
    assert isinstance(result, list)

    apple_entry = next((x for x in result if x["brand"] == "apple"), None)
    assert apple_entry is not None
    assert abs(apple_entry["rating"] - 4.85) < 1e-2


def test_average_price_report(sample_data):
    result = average_price_report.generate(sample_data)
    assert isinstance(result, list)

    apple_entry = next((x for x in result if x["brand"] == "apple"), None)
    samsung_entry = next((x for x in result if x["brand"] == "samsung"), None)

    assert apple_entry is not None
    assert samsung_entry is not None
    assert apple_entry["price"] == 1250
    assert samsung_entry["price"] == 1000
