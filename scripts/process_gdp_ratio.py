import pandas as pd
from dataloaders.gdp_per_capita_dataloader import GDPPerCapitaDataLoader

# Initialize the dataloader
loader = GDPPerCapitaDataLoader(data_file='data/gdp/gdp-per-capita-maddison-project-database.csv')

# Load the data
loader.load_data()

# Process data for USA and UK
countries = ['United States', 'United Kingdom']
loader.process_data(countries=countries)

if loader.processed_data.empty:
    print("No data could be loaded for US and UK")
    exit(1)

# Get the processed data
data = loader.processed_data

# Filter data for USA and UK and rename for consistency
usa_data = data[data['Entity'] == 'United States'][['Year', 'GDP per capita']].copy()
usa_data = usa_data.rename(columns={'Year': 'year', 'GDP per capita': 'gdp_per_capita'})

uk_data = data[data['Entity'] == 'United Kingdom'][['Year', 'GDP per capita']].copy()
uk_data = uk_data.rename(columns={'Year': 'year', 'GDP per capita': 'gdp_per_capita'})

# Sort by year
usa_data = usa_data.sort_values('year')
uk_data = uk_data.sort_values('year')

# Merge data on year to calculate ratio
merged_data = pd.merge(usa_data, uk_data, on='year', suffixes=('_usa', '_uk'))

# Calculate US to UK ratio
merged_data['us_to_uk_gdp_ratio'] = merged_data['gdp_per_capita_usa'] / merged_data['gdp_per_capita_uk']

# Create final dataset with only year and ratio
final_data = merged_data[['year', 'us_to_uk_gdp_ratio']].copy()

# Save to CSV
final_data.to_csv('us_uk_gdp_ratio.csv', index=False)

print(f"Processed GDP data saved to 'us_uk_gdp_ratio.csv'")
print(f"Dataset contains {len(final_data)} rows with years from {final_data['year'].min()} to {final_data['year'].max()}")
print("\nFirst few rows:")
print(final_data.head())
print("\nSummary statistics:")
print(final_data.describe())