import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataloaders.load_trade_data import load_trade_data

# Load the trade data
print("Loading trade data...")
trade_data = load_trade_data()

# Calculate total trade (imports + exports) for each country-year
trade_data['total_trade'] = trade_data['total_exports'] + trade_data['total_imports']

# Calculate global trade totals by year
global_trade_by_year = trade_data.groupby('year')['total_trade'].sum().reset_index()
global_trade_by_year.columns = ['year', 'global_total_trade']

# Filter data for USA and GBR between 1825-1960
target_countries = ['USA', 'GBR']
year_range = (1825, 1960)

us_uk_data = trade_data[
    (trade_data['country'].isin(target_countries)) & 
    (trade_data['year'] >= year_range[0]) & 
    (trade_data['year'] <= year_range[1])
].copy()

print(f"Data for USA and GBR between {year_range[0]}-{year_range[1]}:")
for country in target_countries:
    country_data = us_uk_data[us_uk_data['country'] == country]
    print(f"{country}: {len(country_data)} observations, years {country_data['year'].min()}-{country_data['year'].max()}")

# Merge with global totals to calculate percentages
us_uk_data = us_uk_data.merge(global_trade_by_year, on='year', how='left')

# Calculate each country's trade as percentage of global trade
us_uk_data['trade_share_pct'] = (us_uk_data['total_trade'] / us_uk_data['global_total_trade']) * 100

# Remove any rows where global total is NaN or 0
us_uk_data = us_uk_data.dropna(subset=['global_total_trade'])
us_uk_data = us_uk_data[us_uk_data['global_total_trade'] > 0]

# Create separate dataframes for USA and UK
usa_data = us_uk_data[us_uk_data['country'] == 'USA'][['year', 'total_trade', 'trade_share_pct']].rename(
    columns={'total_trade': 'usa_trade', 'trade_share_pct': 'usa_share'}
)
uk_data = us_uk_data[us_uk_data['country'] == 'GBR'][['year', 'total_trade', 'trade_share_pct']].rename(
    columns={'total_trade': 'uk_trade', 'trade_share_pct': 'uk_share'}
)

# Merge USA and UK data by year
ratio_data = usa_data.merge(uk_data, on='year', how='inner')

# Calculate US/UK ratio (using trade shares)
ratio_data['us_uk_trade_ratio'] = ratio_data['usa_share'] / ratio_data['uk_share']

# Sort by year
ratio_data = ratio_data.sort_values('year')

print(f"\nUS/UK trade ratio data points: {len(ratio_data)}")
print(f"Year range: {ratio_data['year'].min()}-{ratio_data['year'].max()}")

# Create the plot
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

plt.plot(ratio_data['year'], ratio_data['us_uk_trade_ratio'], 
         linewidth=3, color='#d62728', marker='o', markersize=4)

plt.title('US/UK Trade Ratio (1825-1960)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('US Trade Share / UK Trade Share', fontsize=12)
plt.grid(True, alpha=0.3)

# Add a horizontal line at ratio = 1 (parity)
plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Parity (US = UK)')
plt.legend()

plt.tight_layout()
plt.savefig('us_uk_trade_ratio_1825_1960.png', dpi=300, bbox_inches='tight')
plt.close()

# Show summary statistics
print(f"\nUS/UK Trade Ratio Summary (1825-1960):")
print(f"Mean ratio: {ratio_data['us_uk_trade_ratio'].mean():.3f}")
print(f"Median ratio: {ratio_data['us_uk_trade_ratio'].median():.3f}")
print(f"Min ratio: {ratio_data['us_uk_trade_ratio'].min():.3f} in {ratio_data.loc[ratio_data['us_uk_trade_ratio'].idxmin(), 'year']}")
print(f"Max ratio: {ratio_data['us_uk_trade_ratio'].max():.3f} in {ratio_data.loc[ratio_data['us_uk_trade_ratio'].idxmax(), 'year']}")

# Show when US overtook UK (ratio > 1)
crossover_data = ratio_data[ratio_data['us_uk_trade_ratio'] > 1]
if len(crossover_data) > 0:
    first_overtake = crossover_data['year'].min()
    print(f"\nFirst year US trade share exceeded UK: {first_overtake}")
    
# Show some key years
key_years = [1825, 1850, 1875, 1900, 1925, 1950, 1960]
print(f"\nUS/UK trade ratios for key years:")
for year in key_years:
    year_data = ratio_data[ratio_data['year'] == year]
    if len(year_data) > 0:
        ratio = year_data['us_uk_trade_ratio'].iloc[0]
        usa_share = year_data['usa_share'].iloc[0]
        uk_share = year_data['uk_share'].iloc[0]
        print(f"{year}: {ratio:.3f} (US: {usa_share:.1f}%, UK: {uk_share:.1f}%)")

print(f"\nPlot saved as 'us_uk_trade_ratio_1825_1960.png'")

# Also save the ratio data to CSV for future use
ratio_data.to_csv('data/ratios/us_uk_trade_ratio.csv', index=False)
print("Ratio data saved to 'data/ratios/us_uk_trade_ratio.csv'")