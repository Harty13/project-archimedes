import matplotlib.pyplot as plt
import seaborn as sns
from dataloaders.load_trade_data import load_trade_data

# Load the trade data
print("Loading trade data...")
trade_data = load_trade_data()

# Calculate total trade (imports + exports) for each country-year
trade_data['total_trade'] = trade_data['total_exports'] + trade_data['total_imports']

# Get the top 7 countries by average total trade
print("\nIdentifying top 7 countries...")
avg_total_trade = trade_data.groupby('country')['total_trade'].mean().sort_values(ascending=False)
top_7_countries = avg_total_trade.head(7).index.tolist()

print("Top 7 countries by average total trade:")
for i, country in enumerate(top_7_countries, 1):
    avg_trade = avg_total_trade[country]
    print(f"{i}. {country}: ${avg_trade:,.0f}")

# Calculate global trade totals by year
print("\nCalculating global trade totals by year...")
global_trade_by_year = trade_data.groupby('year')['total_trade'].sum().reset_index()
global_trade_by_year.columns = ['year', 'global_total_trade']

print(f"Global trade data available for years: {global_trade_by_year['year'].min()}-{global_trade_by_year['year'].max()}")

# Filter data for top 7 countries
top_countries_data = trade_data[trade_data['country'].isin(top_7_countries)].copy()

# Merge with global totals to calculate percentages
top_countries_data = top_countries_data.merge(global_trade_by_year, on='year', how='left')

# Calculate each country's trade as percentage of global trade
top_countries_data['trade_share_pct'] = (top_countries_data['total_trade'] / top_countries_data['global_total_trade']) * 100

# Remove any rows where global total is NaN or 0
top_countries_data = top_countries_data.dropna(subset=['global_total_trade'])
top_countries_data = top_countries_data[top_countries_data['global_total_trade'] > 0]

print(f"Data points for analysis: {len(top_countries_data)}")

# Create the normalized plot
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

# Plot each country's trade share over time
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
for i, country in enumerate(top_7_countries):
    country_data = top_countries_data[top_countries_data['country'] == country].sort_values('year')
    if len(country_data) > 0:
        plt.plot(country_data['year'], country_data['trade_share_pct'], 
                 label=country, linewidth=2.5, color=colors[i])

plt.title('Top 7 Countries: Trade Share as % of Global Trade Over Time', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Trade Share (% of Global Trade)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('trade_shares_normalized.png', dpi=300, bbox_inches='tight')
plt.close()

# Also create a more recent view (post-1950)
plt.figure(figsize=(14, 8))
recent_data = top_countries_data[top_countries_data['year'] >= 1950]

for i, country in enumerate(top_7_countries):
    country_data = recent_data[recent_data['country'] == country].sort_values('year')
    if len(country_data) > 0:
        plt.plot(country_data['year'], country_data['trade_share_pct'], 
                 label=country, linewidth=2.5, color=colors[i])

plt.title('Top 7 Countries: Trade Share as % of Global Trade (1950-2014)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Trade Share (% of Global Trade)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('trade_shares_normalized_recent.png', dpi=300, bbox_inches='tight')
plt.close()

# Show some summary statistics
print("\nSummary statistics for trade shares (%):")
summary_stats = top_countries_data.groupby('country')['trade_share_pct'].agg(['mean', 'min', 'max', 'std']).round(2)
print(summary_stats)

# Show peak trade shares for each country
print("\nPeak trade shares:")
for country in top_7_countries:
    country_data = top_countries_data[top_countries_data['country'] == country]
    if len(country_data) > 0:
        max_share = country_data['trade_share_pct'].max()
        max_year = country_data.loc[country_data['trade_share_pct'].idxmax(), 'year']
        print(f"{country}: {max_share:.2f}% in {max_year}")

print("\nPlots saved as 'trade_shares_normalized.png' and 'trade_shares_normalized_recent.png'")