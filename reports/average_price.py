from typing import List, Dict
from collections import defaultdict
from reports.base_report import BaseReport


class AveragePriceReport(BaseReport):

    def generate(self, data: List[Dict[str, str]]) -> List[Dict[str, str]]:
        brand_prices: dict[str, list[float]] = defaultdict(list)

        for row in data:
            try:
                brand = row["brand"].strip().lower()
                prise = int(row["price"])
                brand_prices[brand].append(prise)
            except (KeyError, ValueError, AttributeError):
                continue

        avg_prices = [
            {"brand": brand, "price": round(sum(values) / len(values), 0)}
            for brand, values in brand_prices.items()
            if values
        ]
        return sorted(avg_prices, key=lambda x: x["price"], reverse=True)
