import pandas as pd
import numpy as np
from .dataloader import DataLoader

class MIDBDataLoader(DataLoader):
    """
    Dataloader for Militarized Interstate Dispute Database (MIDB) 5.0
    
    Loads and processes military conflict data with proper handling of:
    - Missing values (negative values treated as NaN)
    - Country code mapping
    - Temporal filtering
    """
    
    def __init__(self, file_path: str, countries: list = None, year_range: tuple = None):
        super().__init__(file_path)
        self.countries = countries  # List of country codes to filter
        self.year_range = year_range  # Tuple of (start_year, end_year)
        
        # COW country code mapping
        self.country_mapping = {
            2: 'USA',      # United States
            200: 'GBR',    # United Kingdom  
            220: 'FRA',    # France
            255: 'DEU',    # Germany
            365: 'RUS',    # Russia
            710: 'CHN',    # China
            740: 'JPN',    # Japan
            325: 'ITA',    # Italy
            630: 'IRN',    # Iran
            640: 'TUR',    # Turkey
            900: 'AUS',    # Australia
            20: 'CAN',     # Canada
            70: 'MEX',     # Mexico
            135: 'URU',    # Uruguay
            160: 'ARG',    # Argentina
            155: 'BRA',    # Brazil
        }
    
    def _process_data(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        """
        Process raw MIDB data with cleaning and filtering.
        
        Returns:
            pd.DataFrame: Processed conflict data with columns:
                - styear: Start year of conflict
                - ccode: Country code (COW)
                - country: Country name (mapped from ccode)  
                - revstate: Regime change indicator
                - fatality: Fatality level (0-6)
                - hiact: Highest action level (0-21)
                - hostlev: Hostility level (1-5)
                - orig: Originator indicator
        """
        # Select required columns
        required_cols = ['styear', 'ccode', 'revstate', 'fatality', 'hiact', 'hostlev', 'orig']
        
        # Check if all required columns exist
        missing_cols = [col for col in required_cols if col not in raw_data.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        processed_data = raw_data[required_cols].copy()
        
        # Treat negative values as missing data
        for col in required_cols:
            if col != 'styear':  # Don't treat negative years as missing
                processed_data[col] = processed_data[col].replace(
                    {val: np.nan for val in processed_data[col].unique() if val < 0}
                )
        
        # Add country name mapping
        processed_data['country'] = processed_data['ccode'].map(self.country_mapping)
        processed_data['country'] = processed_data['country'].fillna(f'Unknown')
        
        # Filter by countries if specified
        if self.countries is not None:
            if isinstance(self.countries[0], str):
                # Filter by country names
                processed_data = processed_data[processed_data['country'].isin(self.countries)]
            else:
                # Filter by country codes
                processed_data = processed_data[processed_data['ccode'].isin(self.countries)]
        
        # Filter by year range if specified
        if self.year_range is not None:
            start_year, end_year = self.year_range
            processed_data = processed_data[
                (processed_data['styear'] >= start_year) & 
                (processed_data['styear'] <= end_year)
            ]
        
        # Drop rows where essential columns are missing
        processed_data = processed_data.dropna(subset=['styear', 'ccode'])
        
        # Sort by year and country
        processed_data = processed_data.sort_values(['styear', 'ccode']).reset_index(drop=True)
        
        return processed_data
    
    def get_country_summary(self) -> pd.DataFrame:
        """
        Get summary statistics for each country.
        
        Returns:
            pd.DataFrame: Summary with conflict counts per country
        """
        if not hasattr(self, '_data') or self._data is None:
            self._data = self.load_data()
        
        summary = self._data.groupby(['ccode', 'country']).agg({
            'styear': ['count', 'min', 'max'],
            'hiact': 'mean',
            'hostlev': 'mean',
            'fatality': 'mean',
            'orig': 'sum',
            'revstate': 'sum'
        }).round(2)
        
        summary.columns = ['total_conflicts', 'first_conflict', 'last_conflict', 
                          'avg_escalation', 'avg_hostility', 'avg_fatality',
                          'conflicts_originated', 'regime_changes']
        
        return summary.sort_values('total_conflicts', ascending=False)
    
    def aggregate_by_year(self, aggregation_method: str = 'max') -> pd.DataFrame:
        """
        Aggregate conflict data by year for time-series analysis.
        
        Args:
            aggregation_method: 'max', 'mean', 'sum', or 'count'
            
        Returns:
            pd.DataFrame: Yearly aggregated data per country
        """
        if not hasattr(self, '_data') or self._data is None:
            self._data = self.load_data()
        
        if aggregation_method == 'count':
            # Count number of conflicts per year
            yearly_data = self._data.groupby(['styear', 'ccode', 'country']).size().reset_index(name='conflict_count')
        else:
            # Aggregate numeric columns
            numeric_cols = ['hiact', 'hostlev', 'fatality']
            agg_func = {col: aggregation_method for col in numeric_cols}
            agg_func.update({'orig': 'sum', 'revstate': 'sum'})
            
            yearly_data = self._data.groupby(['styear', 'ccode', 'country']).agg(agg_func).reset_index()
        
        return yearly_data.sort_values(['styear', 'ccode'])
    
    def get_top_countries(self, n: int = 6) -> list:
        """
        Get the top N countries by total number of conflicts.
        
        Args:
            n: Number of top countries to return
            
        Returns:
            list: Country codes of top conflict countries
        """
        if not hasattr(self, '_data') or self._data is None:
            self._data = self.load_data()
        
        country_counts = self._data['ccode'].value_counts().head(n)
        return country_counts.index.tolist()