from typing import List, Dict

import pytest

from reports import average_rating_report


@pytest.fixture
def sample_data() -> List[Dict[str, str]]:
    return [
        {"brand": "apple", "rating": "4.9"},
        {"brand": "apple", "rating": "4.8"},
        {"brand": "samsung", "rating": "4.5"},
    ]


def test_average_rating_report(sample_data):
    result = average_rating_report.generate(sample_data)
    assert isinstance(result, list)
    assert result[0]["brand"] == "apple"
    assert abs(result[0]["rating"] - 4.85) < 1e-2
