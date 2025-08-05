from .dataloader import DataLoader
import pandas as pd

class ExchangeRateDataLoader(DataLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _load_csv(self) -> pd.DataFrame:
        """Override to handle the specific format of this CSV file."""
        # Skip the first 2 lines (description and citation) and read from line 3
        return pd.read_csv(self.file_path, skiprows=2)

    def _process_data(self, raw_pd_data):
        """Process the raw exchange rate data. Returns a DataFrame with (year, usd_per_gbp)"""
        processed_data = raw_pd_data.copy()
        
        # Rename columns for consistency
        processed_data = processed_data.rename(columns={
            'Year': 'year',
            'Rate': 'usd_per_gbp'
        })
        
        # Select relevant columns (ignore the Unit column)
        processed_data = processed_data[['year', 'usd_per_gbp']]
        
        # Convert year to integer and rate to float
        processed_data['year'] = processed_data['year'].astype(int)
        processed_data['usd_per_gbp'] = processed_data['usd_per_gbp'].astype(float)
        
        # Remove any rows with missing data
        processed_data = processed_data.dropna()
        
        # Sort by year
        processed_data = processed_data.sort_values('year')
        
        return processed_data
