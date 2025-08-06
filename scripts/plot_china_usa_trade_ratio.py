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

# Filter data for China and USA from 1875 to current
target_countries = ['CHN', 'USA']
year_range = (1875, trade_data['year'].max())

china_usa_data = trade_data[
    (trade_data['country'].isin(target_countries)) & 
    (trade_data['year'] >= year_range[0]) & 
    (trade_data['year'] <= year_range[1])
].copy()

print(f"Data for China and USA between {year_range[0]}-{year_range[1]}:")
for country in target_countries:
    country_data = china_usa_data[china_usa_data['country'] == country]
    print(f"{country}: {len(country_data)} observations, years {country_data['year'].min()}-{country_data['year'].max()}")

# Merge with global totals to calculate percentages
china_usa_data = china_usa_data.merge(global_trade_by_year, on='year', how='left')

# Calculate each country's trade as percentage of global trade
china_usa_data['trade_share_pct'] = (china_usa_data['total_trade'] / china_usa_data['global_total_trade']) * 100

# Remove any rows where global total is NaN or 0
china_usa_data = china_usa_data.dropna(subset=['global_total_trade'])
china_usa_data = china_usa_data[china_usa_data['global_total_trade'] > 0]

# Create separate dataframes for China and USA
china_data = china_usa_data[china_usa_data['country'] == 'CHN'][['year', 'total_trade', 'trade_share_pct']].rename(
    columns={'total_trade': 'china_trade', 'trade_share_pct': 'china_share'}
)
usa_data = china_usa_data[china_usa_data['country'] == 'USA'][['year', 'total_trade', 'trade_share_pct']].rename(
    columns={'total_trade': 'usa_trade', 'trade_share_pct': 'usa_share'}
)

# Merge China and USA data by year
ratio_data = china_data.merge(usa_data, on='year', how='inner')

# Calculate China/USA ratio (using trade shares)
ratio_data['china_usa_trade_ratio'] = ratio_data['china_share'] / ratio_data['usa_share']

# Sort by year
ratio_data = ratio_data.sort_values('year')

print(f"\nChina/USA trade ratio data points: {len(ratio_data)}")
print(f"Year range: {ratio_data['year'].min()}-{ratio_data['year'].max()}")

# Create the plot
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

plt.plot(ratio_data['year'], ratio_data['china_usa_trade_ratio'], 
         linewidth=3, color='#d62728', marker='o', markersize=4)

plt.title(f'China/USA Trade Ratio ({ratio_data["year"].min()}-{ratio_data["year"].max()})', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('China Trade Share / USA Trade Share', fontsize=12)
plt.grid(True, alpha=0.3)

# Add a horizontal line at ratio = 1 (parity)
plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Parity (China = USA)')
plt.legend()

plt.tight_layout()
plt.savefig(f'china_usa_trade_ratio_{ratio_data["year"].min()}_{ratio_data["year"].max()}.png', dpi=300, bbox_inches='tight')
plt.close()

# Show summary statistics
print(f"\nChina/USA Trade Ratio Summary ({ratio_data['year'].min()}-{ratio_data['year'].max()}):")
print(f"Mean ratio: {ratio_data['china_usa_trade_ratio'].mean():.3f}")
print(f"Median ratio: {ratio_data['china_usa_trade_ratio'].median():.3f}")
print(f"Min ratio: {ratio_data['china_usa_trade_ratio'].min():.3f} in {ratio_data.loc[ratio_data['china_usa_trade_ratio'].idxmin(), 'year']}")
print(f"Max ratio: {ratio_data['china_usa_trade_ratio'].max():.3f} in {ratio_data.loc[ratio_data['china_usa_trade_ratio'].idxmax(), 'year']}")

# Show when China overtook USA (ratio > 1)
crossover_data = ratio_data[ratio_data['china_usa_trade_ratio'] > 1]
if len(crossover_data) > 0:
    first_overtake = crossover_data['year'].min()
    print(f"\nFirst year China trade share exceeded USA: {first_overtake}")
    
# Show some key years
key_years = [1875, 1900, 1925, 1950, 1975, 2000, 2020]
print(f"\nChina/USA trade ratios for key years:")
for year in key_years:
    year_data = ratio_data[ratio_data['year'] == year]
    if len(year_data) > 0:
        ratio = year_data['china_usa_trade_ratio'].iloc[0]
        china_share = year_data['china_share'].iloc[0]
        usa_share = year_data['usa_share'].iloc[0]
        print(f"{year}: {ratio:.3f} (China: {china_share:.1f}%, USA: {usa_share:.1f}%)")

print(f"\nPlot saved as 'china_usa_trade_ratio_{ratio_data['year'].min()}_{ratio_data['year'].max()}.png'")

# Save the ratio data to CSV for future use
ratio_data.to_csv('data/ratios/china_usa_trade_ratio.csv', index=False)
print("Ratio data saved to 'data/ratios/china_usa_trade_ratio.csv'")