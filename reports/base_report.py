from abc import ABC, abstractmethod
from typing import List, Dict


class BaseReport(ABC):
    @abstractmethod
    def generate(self, data: List[Dict[str, str]]) -> List[Dict[str, str]]:
        pass
