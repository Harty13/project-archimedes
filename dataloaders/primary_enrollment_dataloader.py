from .dataloader import DataLoader
import pandas as pd

class PrimaryEnrollmentDataLoader(DataLoader):
    def __init__(self, file_path, countries=None):
        super().__init__(file_path)
        self.countries = countries

    def _process_data(self, raw_pd_data):
        """Process the raw primary enrollment data. Returns a DataFrame with (country, year, enrollment_rate)"""
        processed_data = raw_pd_data.copy()
        
        # Rename columns for consistency
        processed_data = processed_data.rename(columns={
            'Entity': 'country',
            'Year': 'year',
            'Combined total net enrolment rate, primary, both sexes': 'enrollment_rate'
        })
        
        # Filter for specific countries if provided
        if self.countries:
            processed_data = processed_data[processed_data['country'].isin(self.countries)]
        
        # Select relevant columns (ignore Code column)
        processed_data = processed_data[['country', 'year', 'enrollment_rate']]
        
        # Convert year to integer and enrollment_rate to float
        processed_data['year'] = processed_data['year'].astype(int)
        processed_data['enrollment_rate'] = pd.to_numeric(processed_data['enrollment_rate'], errors='coerce')
        
        # Remove rows with missing enrollment data
        processed_data = processed_data.dropna(subset=['enrollment_rate'])
        
        # Filter out rows where enrollment rate is 0 (likely no data rather than actual 0% enrollment)
        processed_data = processed_data[processed_data['enrollment_rate'] > 0]
        
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
        
    def get_countries_comparison(self, countries_list):
        """Get data for multiple countries for comparison."""
        processed_data = self.load_data()
        return processed_data[processed_data['country'].isin(countries_list)].copy()