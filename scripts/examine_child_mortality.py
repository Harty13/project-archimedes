import pandas as pd

# Load the CSV file to understand its structure
file_path = "/Users/erikschnell/Desktop/Dev/TrueWealth Hackathon/Project Archimedes/data/child_mortality/u5mr-by-gapminder.csv"

# Read the CSV file
df = pd.read_csv(file_path)
print("Shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# Check for US and UK data
print("\nCountries containing 'United States':")
us_matches = df[df['geo.name'].str.contains('United States', na=False, case=False)]
print(us_matches['geo.name'].unique())

print("\nCountries containing 'United Kingdom' or 'UK':")
uk_matches = df[df['geo.name'].str.contains('United Kingdom|UK', na=False, case=False)]
print(uk_matches['geo.name'].unique())

# Let's also check for variations
print("\nAll unique country names (first 20):")
print(df['geo.name'].unique()[:20])

# Check for 1800-1960 data availability for US
if not us_matches.empty:
    us_row = us_matches.iloc[0]
    years_1800_1960 = [str(year) for year in range(1800, 1961)]
    available_years = []
    for year in years_1800_1960:
        if not pd.isna(us_row[year]):
            available_years.append(year)
    print(f"\nUS data available years (1800-1960): {len(available_years)} years")
    if available_years:
        print(f"First available year: {available_years[0]}")
        print(f"Last available year: {available_years[-1]}")

if not uk_matches.empty:
    uk_row = uk_matches.iloc[0]
    years_1800_1960 = [str(year) for year in range(1800, 1961)]
    available_years = []
    for year in years_1800_1960:
        if not pd.isna(uk_row[year]):
            available_years.append(year)
    print(f"\nUK data available years (1800-1960): {len(available_years)} years")
    if available_years:
        print(f"First available year: {available_years[0]}")
        print(f"Last available year: {available_years[-1]}")