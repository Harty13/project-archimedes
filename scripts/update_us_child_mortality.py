import pandas as pd

# Load the existing CSV
df = pd.read_csv('us_uk_child_mortality_1800_1960.csv')

# Historical US values for 1800-1880 (every 5 years)
us_historical_values = [
    462.89,  # 1800-1804
    462.31,  # 1805-1809
    461.35,  # 1810-1814
    459.34,  # 1815-1819
    456.65,  # 1820-1824
    447.87,  # 1825-1829
    440.01,  # 1830-1834
    430.12,  # 1835-1839
    416.08,  # 1840-1844
    399.27,  # 1845-1849
    374.17,  # 1850-1854
    343.53,  # 1855-1859
    325.74,  # 1860-1864
    316.5,   # 1865-1869
    325.81,  # 1870-1874
    347.49   # 1875-1879
]

# Create a mapping for each year from 1800-1879
year_value_map = {}
for i, value in enumerate(us_historical_values):
    start_year = 1800 + (i * 5)
    for year_offset in range(5):
        year = start_year + year_offset
        if year < 1880:  # Only up to 1879
            year_value_map[year] = value

# Update the DataFrame
for index, row in df.iterrows():
    year = row['year']
    if year in year_value_map:
        df.at[index, 'us_child_mortality'] = year_value_map[year]

# Save the updated CSV
df.to_csv('us_uk_child_mortality_1800_1960.csv', index=False)

print("Updated US child mortality data for 1800-1880")
print(f"Total rows updated: {len(year_value_map)}")
print("\nFirst 10 rows of updated data:")
print(df.head(10))
print("\nData around 1880 transition:")
print(df[(df['year'] >= 1875) & (df['year'] <= 1885)])