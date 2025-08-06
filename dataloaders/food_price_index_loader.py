from .dataloader import DataLoader
import pandas as pd
import numpy as np

class FoodPriceIndexLoader(DataLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _load_csv(self) -> pd.DataFrame:
        """Override to handle the specific format of this CSV file."""
        # Skip the first 4 lines (metadata) and read from line 5
        return pd.read_csv(self.file_path, skiprows=4)

    def _process_data(self, raw_pd_data):
        """Process the raw food price index data. Returns a DataFrame with (country, year, volatility)"""
        processed_data = raw_pd_data.copy()
        
        # Filter for relevant countries (US, China, UK, and World data)
        countries_of_interest = ['United States', 'China', 'United Kingdom', 'World']
        processed_data = processed_data[processed_data['Country Name'].isin(countries_of_interest)]
        
        # Melt the dataframe to convert years from columns to rows
        id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']
        year_columns = [col for col in processed_data.columns if col.isdigit()]
        
        melted_data = processed_data.melt(
            id_vars=id_vars,
            value_vars=year_columns,
            var_name='year',
            value_name='inflation_rate'
        )
        
        # Convert year to integer and inflation_rate to float
        melted_data['year'] = melted_data['year'].astype(int)
        melted_data['inflation_rate'] = pd.to_numeric(melted_data['inflation_rate'], errors='coerce')
        
        # Remove rows with missing inflation data
        melted_data = melted_data.dropna(subset=['inflation_rate'])
        
        # Calculate volatility (rolling 5-year standard deviation of inflation rates)
        result_data = []
        
        for country in countries_of_interest:
            country_data = melted_data[melted_data['Country Name'] == country].copy()
            country_data = country_data.sort_values('year')
            
            # Calculate 5-year rolling volatility
            country_data['volatility'] = country_data['inflation_rate'].rolling(
                window=5, min_periods=3
            ).std()
            
            # Only include rows with volatility data
            country_volatility = country_data.dropna(subset=['volatility'])
            
            for _, row in country_volatility.iterrows():
                result_data.append({
                    'country': row['Country Name'],
                    'year': row['year'],
                    'volatility': row['volatility']
                })
        
        final_data = pd.DataFrame(result_data)
        
        # Sort by country and year
        final_data = final_data.sort_values(['country', 'year'])
        
        return final_data

    def save_processed_data(self, output_path):
        """Load, process and save the data to a new CSV file."""
        processed_data = self.load_data()
        processed_data.to_csv(output_path, index=False)
        return processed_data