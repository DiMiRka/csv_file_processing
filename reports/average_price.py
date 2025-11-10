from typing import List, Dict
from collections import defaultdict
from reports.base_report import BaseReport


class AveragePriceReport(BaseReport):

    def generate(self, data: List[Dict[str, str]]) -> List[Dict[str, str]]:
        brand_ratings: dict[str, list[float]] = defaultdict(list)

        for row in data:
            try:
                brand = row["brand"].strip().lower()
                rating = float(row["prise"])
                brand_ratings[brand].append(rating)
            except (KeyError, ValueError, AttributeError):
                continue

        avg_ratings = [
            {"brand": brand, "prise": round(sum(values) / len(values), 2)}
            for brand, values in brand_ratings.items()
            if values
        ]
        return sorted(avg_ratings, key=lambda x: x["prise"], reverse=True)
