from .dataloader import DataLoader
import pandas as pd
import numpy as np

class GDPVolatilityDataLoader(DataLoader):
    def __init__(self, file_path, window=5, min_periods=3):
        super().__init__(file_path)
        self.window = window  # Rolling window size for volatility calculation
        self.min_periods = min_periods  # Minimum periods required for calculation

    def _process_data(self, raw_pd_data):
        """Process the raw GDP data and calculate volatility. Returns a DataFrame with (country, year, volatility)"""
        raw_data = raw_pd_data.copy()
        
        # Ensure year column is integer
        raw_data['year'] = raw_data['year'].astype(int)
        
        # Convert data from wide to long format
        result_data = []
        
        # Process US data
        us_data = raw_data[['year', 'GDP_US']].copy()
        us_data = us_data.rename(columns={'GDP_US': 'gdp'})
        us_data = us_data.sort_values('year')
        
        # Calculate year-over-year GDP growth rate for US
        us_data['gdp_growth'] = us_data['gdp'].pct_change() * 100
        
        # Calculate rolling volatility (standard deviation of growth rates)
        us_data['volatility'] = us_data['gdp_growth'].rolling(
            window=self.window, min_periods=self.min_periods
        ).std()
        
        # Add US data to results
        us_volatility = us_data.dropna(subset=['volatility'])
        for _, row in us_volatility.iterrows():
            result_data.append({
                'country': 'United States',
                'year': row['year'],
                'volatility': row['volatility']
            })
        
        # Process China data
        china_data = raw_data[['year', 'GDP_China']].copy()
        china_data = china_data.rename(columns={'GDP_China': 'gdp'})
        china_data = china_data.sort_values('year')
        
        # Calculate year-over-year GDP growth rate for China
        china_data['gdp_growth'] = china_data['gdp'].pct_change() * 100
        
        # Calculate rolling volatility (standard deviation of growth rates)
        china_data['volatility'] = china_data['gdp_growth'].rolling(
            window=self.window, min_periods=self.min_periods
        ).std()
        
        # Add China data to results
        china_volatility = china_data.dropna(subset=['volatility'])
        for _, row in china_volatility.iterrows():
            result_data.append({
                'country': 'China',
                'year': row['year'],
                'volatility': row['volatility']
            })
        
        # Create final dataframe
        final_data = pd.DataFrame(result_data)
        
        # Round volatility to 4 decimal places for cleaner output
        final_data['volatility'] = final_data['volatility'].round(4)
        
        # Sort by country and year
        final_data = final_data.sort_values(['country', 'year'])
        
        return final_data

    def save_processed_data(self, output_path):
        """Load, process and save the data to a new CSV file."""
        processed_data = self.load_data()
        processed_data.to_csv(output_path, index=False)
        return processed_data
        
    def get_country_data(self, country_name):
        """Get data for a specific country."""
        processed_data = self.load_data()
        return processed_data[processed_data['country'] == country_name].copy()
        
    def get_year_range(self):
        """Get the year range of the data."""
        processed_data = self.load_data()
        return processed_data['year'].min(), processed_data['year'].max()
        
    def get_raw_data_with_growth(self):
        """Get the raw data with growth rates calculated."""
        raw_data = self._load_csv()
        raw_data['year'] = raw_data['year'].astype(int)
        raw_data = raw_data.sort_values('year')
        
        # Calculate growth rates
        raw_data['US_growth'] = raw_data['GDP_US'].pct_change() * 100
        raw_data['China_growth'] = raw_data['GDP_China'].pct_change() * 100
        
        return raw_data
        
    def get_statistics(self):
        """Get basic statistics for each country's volatility."""
        processed_data = self.load_data()
        stats = {}
        
        for country in processed_data['country'].unique():
            country_data = processed_data[processed_data['country'] == country]
            stats[country] = {
                'years': len(country_data),
                'year_range': f"{country_data['year'].min()}-{country_data['year'].max()}",
                'min_volatility': country_data['volatility'].min(),
                'max_volatility': country_data['volatility'].max(),
                'avg_volatility': country_data['volatility'].mean(),
                'latest_volatility': country_data['volatility'].iloc[-1],
                'latest_year': country_data['year'].iloc[-1]
            }
        
        return stats