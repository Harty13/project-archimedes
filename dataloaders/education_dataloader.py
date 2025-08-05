from .dataloader import DataLoader

class EducationDataLoader(DataLoader):
    def __init__(self, file_path, countries=None):
        super().__init__(file_path)
        self.countries = countries

    def _process_data(self, raw_pd_data):
        """Process the raw education data. Returns a DataFrame with education values. (country, year, education)"""
        processed_data = raw_pd_data.copy()

        # Weight: 50% on absolute quantity (education rate percentage) and 50% on quality (years of schooling + graduation rate)

        # Calculate quantity using education rate (secondary + tertiary)
        processed_data["educated_quantity"] = (
                processed_data["lpc"] + 
                processed_data["lsc"] + 
                processed_data["lhc"]
        ) / 100


        # Calculate quality using years of schooling + graduation rate
        processed_data["education_quality"] = (
            0.5 * (processed_data["yr_sch"]/18) +
            0.5 * (
                processed_data["lpc"] / processed_data["lp"] +
                processed_data["lsc"] / processed_data["ls"] +
                processed_data["lhc"] / processed_data["lh"]
            )
        )

        # Combine quantity and quality to get a final education value
        processed_data["education"] = (
            0.5 * processed_data["educated_quantity"] + 0.5 * processed_data["education_quality"]
        )
        
        processed_data = processed_data[['country', 'year', 'education', 'educated_quantity', 'education_quality']]
        
        processed_data = processed_data.dropna(subset=['education'])
        
        if self.countries is not None:
            processed_data = processed_data[processed_data['country'].isin(self.countries)]
        
        return processed_data
    


