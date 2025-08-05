import pandas as pd
import numpy as np

# Load the child mortality data
df = pd.read_csv('us_uk_child_mortality_1800_1960.csv')

# Calculate US to UK ratio
df['us_uk_child_mortality_ratio'] = df['us_child_mortality'] / df['uk_child_mortality']

# Create the ratio CSV with year and ratio columns
ratio_df = df[['year', 'us_uk_child_mortality_ratio']].copy()

# Save the ratio CSV
ratio_df.to_csv('us_uk_child_mortality_ratio_1800_1960.csv', index=False)

print("Child mortality ratio CSV created!")
print(f"Data shape: {ratio_df.shape}")
print("\nFirst 10 rows:")
print(ratio_df.head(10))
print("\nLast 10 rows:")
print(ratio_df.tail(10))

# Summary statistics
print(f"\nRatio Summary (1800-1960):")
print(f"Highest US/UK ratio: {ratio_df['us_uk_child_mortality_ratio'].max():.2f} in {ratio_df.loc[ratio_df['us_uk_child_mortality_ratio'].idxmax(), 'year']}")
print(f"Lowest US/UK ratio: {ratio_df['us_uk_child_mortality_ratio'].min():.2f} in {ratio_df.loc[ratio_df['us_uk_child_mortality_ratio'].idxmin(), 'year']}")
print(f"1800 ratio: {ratio_df['us_uk_child_mortality_ratio'].iloc[0]:.2f}")
print(f"1960 ratio: {ratio_df['us_uk_child_mortality_ratio'].iloc[-1]:.2f}")

# Find when ratio crossed 1.0 (parity)
parity_years = ratio_df[abs(ratio_df['us_uk_child_mortality_ratio'] - 1.0) < 0.05]
if not parity_years.empty:
    print(f"Near parity (ratio ~1.0) around: {parity_years['year'].tolist()}")
else:
    print("No years with near parity found")