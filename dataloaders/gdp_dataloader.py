import pandas as pd

class GDPDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.countries = None
        self.data = None


    def _load_from_csv(self):
        """Load GDP data from a CSV file."""
        raw_pd_data = pd.read_csv(self.file_path)
        return raw_pd_data

    def _process_raw_data(self, raw_pd_data):
        """Process the raw GDP data. Returns a DataFrame with GDP values. (country, year, gdp)"""
        processed_data = raw_pd_data.copy()
        
        processed_data = processed_data.rename(columns={
            'Entity': 'country',
            'Year': 'year',
            'Gross domestic product (GDP)': 'gdp'
        })
        
        processed_data = processed_data[['country', 'year', 'gdp']]
        
        processed_data = processed_data.dropna(subset=['gdp'])
        
        if self.countries is not None:
            processed_data = processed_data[processed_data['country'].isin(self.countries)]
        
        return processed_data


    def load_data(self):
        """Load GDP data from the specified file path. Returns a DataFrame with GDP values for the specified countries."""
        try:
            raw_pd_data = self._load_from_csv()
            data = self._process_raw_data(raw_pd_data)
            return data

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

