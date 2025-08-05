from .dataloader import DataLoader

class GDPDataLoader(DataLoader):
    def __init__(self, file_path, countries=None):
        super().__init__(file_path)
        self.countries = countries
        self.data = None

    def _process_data(self, raw_pd_data):
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
