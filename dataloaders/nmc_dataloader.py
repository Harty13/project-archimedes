import pandas as pd

class NMCDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.countries = None
        self.data = None

    def _load_from_csv(self):
        """Load NMC data from a CSV file."""
        raw_pd_data = pd.read_csv(self.file_path, encoding='latin1')
        return raw_pd_data

    def _process_raw_data(self, raw_pd_data):
        """Process the raw NMC data. Returns a DataFrame with selected columns (country, year, milex, milper, irst, tpop, upop)"""
        processed_data = raw_pd_data.copy()
        
        processed_data = processed_data.rename(columns={
            'statenme': 'country'
        })
        
        processed_data = processed_data[['country', 'year', 'milex', 'milper', 'irst', 'tpop', 'upop']]
        
        processed_data = processed_data.dropna(subset=['country', 'year'])
        
        if self.countries is not None:
            processed_data = processed_data[processed_data['country'].isin(self.countries)]
        
        return processed_data

    def load_data(self):
        """Load NMC data from the specified file path. Returns a DataFrame with selected military and demographic indicators."""
        try:
            raw_pd_data = self._load_from_csv()
            data = self._process_raw_data(raw_pd_data)
            return data

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")