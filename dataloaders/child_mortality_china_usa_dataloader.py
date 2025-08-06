from .dataloader import DataLoader
import pandas as pd

class ChildMortalityChinaUSADataLoader(DataLoader):
    def __init__(self, file_path, countries=None):
        super().__init__(file_path)
        self.countries = countries or ['China', 'United States']

    def _process_data(self, raw_pd_data):
        """Process the raw child mortality data. Returns a DataFrame with (country, year, mortality_rate)"""
        processed_data = raw_pd_data.copy()
        
        # Filter for specified countries
        processed_data = processed_data[processed_data['name'].isin(self.countries)]
        
        # Rename columns for consistency
        processed_data = processed_data.rename(columns={
            'name': 'country',
            'time': 'year',
            'Child mortality': 'mortality_rate'
        })
        
        # Select relevant columns
        processed_data = processed_data[['country', 'year', 'mortality_rate']]
        
        # Convert year to integer and mortality_rate to float
        processed_data['year'] = processed_data['year'].astype(int)
        processed_data['mortality_rate'] = pd.to_numeric(processed_data['mortality_rate'], errors='coerce')
        
        # Remove rows with missing mortality data
        processed_data = processed_data.dropna(subset=['mortality_rate'])
        
        # Round mortality rate to 2 decimal places for cleaner output
        processed_data['mortality_rate'] = processed_data['mortality_rate'].round(2)
        
        # Sort by country and year
        processed_data = processed_data.sort_values(['country', 'year'])
        
        return processed_data

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
        
    def get_statistics(self):
        """Get basic statistics for each country."""
        processed_data = self.load_data()
        stats = {}
        
        for country in processed_data['country'].unique():
            country_data = processed_data[processed_data['country'] == country]
            stats[country] = {
                'years': len(country_data),
                'year_range': f"{country_data['year'].min()}-{country_data['year'].max()}",
                'min_mortality': country_data['mortality_rate'].min(),
                'max_mortality': country_data['mortality_rate'].max(),
                'avg_mortality': country_data['mortality_rate'].mean(),
                'latest_mortality': country_data['mortality_rate'].iloc[-1],
                'latest_year': country_data['year'].iloc[-1]
            }
        
        return stats