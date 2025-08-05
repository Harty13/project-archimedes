import pandas as pd
from .dataloader import DataLoader

class ChildMortalityDataLoader(DataLoader):
    def __init__(self, file_path, countries=None):
        super().__init__(file_path)
        self.countries = countries

    def _load_csv(self) -> pd.DataFrame:
        """Loads the child mortality CSV file from the file path."""
        return pd.read_csv(self.file_path)

    def _process_data(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        """
        Process the raw child mortality data.
        Returns a DataFrame with columns: country, year, child_mortality
        Child mortality is deaths per 1000 live births under age 5.
        """
        processed_data = []
        
        # Get year columns (1800 to 2100)
        year_columns = [col for col in raw_data.columns if col.isdigit()]
        
        for _, row in raw_data.iterrows():
            country = row['geo.name']
            
            # Filter by countries if specified
            if self.countries and country not in self.countries:
                continue
                
            for year_col in year_columns:
                year = int(year_col)
                mortality_rate = row[year_col]
                
                # Skip if no data available
                if pd.isna(mortality_rate):
                    continue
                    
                processed_data.append({
                    'country': country,
                    'year': year,
                    'child_mortality': mortality_rate
                })
        
        df = pd.DataFrame(processed_data)
        
        # Sort by country and year
        df = df.sort_values(['country', 'year'])
        
        return df