import pandas as pd

# Load the current CSV
df = pd.read_csv('us_uk_child_mortality_1800_1960.csv')

# Historical US values for 1800-1880 (every 5 years as provided)
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

print("Before update - US values 1800-1880:")
print(df[(df['year'] >= 1800) & (df['year'] <= 1880)][['year', 'us_child_mortality']].head(10))

# Apply values only to years 1800-1879 (before 1880)
for i, value in enumerate(us_historical_values):
    start_year = 1800 + (i * 5)
    end_year = min(start_year + 5, 1880)  # Don't go past 1879
    
    # Update all years in this 5-year range
    mask = (df['year'] >= start_year) & (df['year'] < end_year)
    df.loc[mask, 'us_child_mortality'] = value
    
    print(f"Updated {start_year}-{end_year-1}: {value}")

print(f"\nAfter update - US values 1800-1880:")
print(df[(df['year'] >= 1800) & (df['year'] <= 1880)][['year', 'us_child_mortality']].head(10))

print(f"\nTransition at 1880:")
print(df[(df['year'] >= 1878) & (df['year'] <= 1882)][['year', 'us_child_mortality']])

# Save the corrected CSV
df.to_csv('us_uk_child_mortality_1800_1960.csv', index=False)
print(f"\nUpdated CSV saved!")