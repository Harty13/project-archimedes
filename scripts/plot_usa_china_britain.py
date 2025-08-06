import matplotlib.pyplot as plt
import seaborn as sns
from dataloaders.load_trade_data import load_trade_data

# Load the trade data
print("Loading trade data...")
trade_data = load_trade_data()

# Calculate total trade (imports + exports) for each country-year
trade_data['total_trade'] = trade_data['total_exports'] + trade_data['total_imports']

# Calculate global trade totals by year
print("Calculating global trade totals by year...")
global_trade_by_year = trade_data.groupby('year')['total_trade'].sum().reset_index()
global_trade_by_year.columns = ['year', 'global_total_trade']

# Countries of interest
target_countries = ['USA', 'CHN', 'GBR']

print("Checking available data for target countries:")
for country in target_countries:
    country_data = trade_data[trade_data['country'] == country]
    if len(country_data) > 0:
        print(f"{country}: {len(country_data)} observations, years {country_data['year'].min()}-{country_data['year'].max()}")
    else:
        print(f"{country}: No data found")

# Filter data for the three countries
selected_countries_data = trade_data[trade_data['country'].isin(target_countries)].copy()

# Merge with global totals to calculate percentages
selected_countries_data = selected_countries_data.merge(global_trade_by_year, on='year', how='left')

# Calculate each country's trade as percentage of global trade
selected_countries_data['trade_share_pct'] = (selected_countries_data['total_trade'] / selected_countries_data['global_total_trade']) * 100

# Remove any rows where global total is NaN or 0
selected_countries_data = selected_countries_data.dropna(subset=['global_total_trade'])
selected_countries_data = selected_countries_data[selected_countries_data['global_total_trade'] > 0]

print(f"\nData points for analysis: {len(selected_countries_data)}")

# Create the plot
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

# Plot each country's trade share over time
colors = {'USA': '#1f77b4', 'CHN': '#d62728', 'GBR': '#2ca02c'}
labels = {'USA': 'United States', 'CHN': 'China', 'GBR': 'Great Britain'}

for country in target_countries:
    country_data = selected_countries_data[selected_countries_data['country'] == country].sort_values('year')
    if len(country_data) > 0:
        plt.plot(country_data['year'], country_data['trade_share_pct'], 
                 label=labels[country], linewidth=3, color=colors[country])

plt.title('Trade Share as % of Global Trade: USA, China, and Great Britain', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Trade Share (% of Global Trade)', fontsize=12)
plt.legend(loc='upper right', fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('usa_china_britain_trade_shares.png', dpi=300, bbox_inches='tight')
plt.close()

# Show summary statistics
print("\nSummary statistics for trade shares (%):")
summary_stats = selected_countries_data.groupby('country')['trade_share_pct'].agg(['mean', 'min', 'max', 'std']).round(2)
print(summary_stats)

# Show peak trade shares for each country
print("\nPeak trade shares:")
for country in target_countries:
    country_data = selected_countries_data[selected_countries_data['country'] == country]
    if len(country_data) > 0:
        max_share = country_data['trade_share_pct'].max()
        max_year = country_data.loc[country_data['trade_share_pct'].idxmax(), 'year']
        min_share = country_data['trade_share_pct'].min()
        min_year = country_data.loc[country_data['trade_share_pct'].idxmin(), 'year']
        print(f"{labels[country]}: Peak {max_share:.2f}% in {max_year}, Low {min_share:.2f}% in {min_year}")

print("\nPlot saved as 'usa_china_britain_trade_shares.png'")