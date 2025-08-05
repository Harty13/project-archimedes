import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dataloaders.child_mortality_dataloader import ChildMortalityDataLoader

# Load child mortality data for US and UK
file_path = "data/child_mortality/u5mr-by-gapminder.csv"
countries = ['United States', 'United Kingdom']
loader = ChildMortalityDataLoader(file_path, countries=countries)
data = loader.load_data()

# Filter for 1800-1960
data_filtered = data[(data['year'] >= 1800) & (data['year'] <= 1960)]

# Pivot to have US and UK as separate columns
pivot_data = data_filtered.pivot(index='year', columns='country', values='child_mortality')

# Rename columns for clarity
pivot_data.columns = ['uk_child_mortality', 'us_child_mortality']

# Reset index to have year as a column
pivot_data = pivot_data.reset_index()

# Save to CSV
output_file = "us_uk_child_mortality_1800_1960.csv"
pivot_data.to_csv(output_file, index=False)

print(f"CSV saved to: {output_file}")
print(f"Data shape: {pivot_data.shape}")
print("\nFirst 10 rows:")
print(pivot_data.head(10))
print("\nLast 10 rows:")
print(pivot_data.tail(10))
print(f"\nData summary for 1800-1960:")
print(f"Years covered: {pivot_data['year'].min()} to {pivot_data['year'].max()}")
print(f"US child mortality range: {pivot_data['us_child_mortality'].min():.1f} to {pivot_data['us_child_mortality'].max():.1f}")
print(f"UK child mortality range: {pivot_data['uk_child_mortality'].min():.1f} to {pivot_data['uk_child_mortality'].max():.1f}")