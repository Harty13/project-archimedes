from .dataloader import DataLoader
import pandas as pd

class CNYExchangeRateDataLoader(DataLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _process_data(self, raw_pd_data):
        """Process the raw CNY to USD exchange rate data. Returns a DataFrame with (year, exchange_rate)"""
        processed_data = raw_pd_data.copy()
        
        # Convert observation_date to datetime
        processed_data['observation_date'] = pd.to_datetime(processed_data['observation_date'])
        
        # Extract year from date
        processed_data['year'] = processed_data['observation_date'].dt.year
        
        # Rename EXCHUS column to exchange_rate for clarity
        processed_data = processed_data.rename(columns={
            'EXCHUS': 'exchange_rate'
        })
        
        # Calculate annual average exchange rate (since data is monthly)
        annual_data = processed_data.groupby('year')['exchange_rate'].mean().reset_index()
        
        # Round to 4 decimal places for cleaner output
        annual_data['exchange_rate'] = annual_data['exchange_rate'].round(4)
        
        # Sort by year
        annual_data = annual_data.sort_values('year')
        
        return annual_data

    def save_processed_data(self, output_path):
        """Load, process and save the data to a new CSV file."""
        processed_data = self.load_data()
        processed_data.to_csv(output_path, index=False)
        return processed_data
        
    def get_monthly_data(self):
        """Get the original monthly data with year column added."""
        raw_data = self._load_csv()
        raw_data['observation_date'] = pd.to_datetime(raw_data['observation_date'])
        raw_data['year'] = raw_data['observation_date'].dt.year
        raw_data['month'] = raw_data['observation_date'].dt.month
        raw_data = raw_data.rename(columns={'EXCHUS': 'exchange_rate'})
        return raw_data[['year', 'month', 'observation_date', 'exchange_rate']].sort_values('observation_date')
        
    def get_year_range(self):
        """Get the year range of the data."""
        processed_data = self.load_data()
        return processed_data['year'].min(), processed_data['year'].max()