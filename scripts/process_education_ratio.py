import pandas as pd
from dataloaders.education_dataloader import EducationDataLoader

# Load the education data for USA and UK
dataloader = EducationDataLoader(file_path='data/education/education_dataset.csv', countries=['USA', 'United Kingdom'])
data = dataloader.load_data()

# Filter data for USA and UK
usa_data = data[data['country'] == 'USA'][['year', 'education']].sort_values('year')
uk_data = data[data['country'] == 'United Kingdom'][['year', 'education']].sort_values('year')

# Merge data on year to calculate ratio
merged_data = pd.merge(usa_data, uk_data, on='year', suffixes=('_usa', '_uk'))

# Calculate US to UK ratio
merged_data['us_to_uk_ratio'] = merged_data['education_usa'] / merged_data['education_uk']

# Create final dataset with only year and ratio
final_data = merged_data[['year', 'us_to_uk_ratio']].copy()

# Save to CSV
final_data.to_csv('us_uk_education_ratio.csv', index=False)

print(f"Processed education data saved to 'us_uk_education_ratio.csv'")
print(f"Dataset contains {len(final_data)} rows with years from {final_data['year'].min()} to {final_data['year'].max()}")
print("\nFirst few rows:")
print(final_data.head())
print("\nSummary statistics:")
print(final_data.describe())