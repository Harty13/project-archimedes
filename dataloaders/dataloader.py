import pandas as pd
from abc import ABC, abstractmethod

class DataLoader(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        """Loads and processes the data from file_path."""
        raw_data = self._load_csv()
        return self._process_data(raw_data)

    def _load_csv(self) -> pd.DataFrame:
        """Loads a CSV file from the file path."""
        return pd.read_csv(self.file_path)

    @abstractmethod
    def _process_data(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        """Process raw data. Needs to be implemented by subclasses."""
        pass
