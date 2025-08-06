import matplotlib.pyplot as plt
import seaborn as sns
from dataloaders.load_trade_data import load_trade_data

# Load the trade data
print("Loading trade data...")
trade_data = load_trade_data()

# Calculate total trade (imports + exports) for each country-year
trade_data['total_trade'] = trade_data['total_exports'] + trade_data['total_imports']

# Find the 7 countries with highest average total trade
print("\nFinding top 7 countries by total trade...")
avg_total_trade = trade_data.groupby('country')['total_trade'].mean().sort_values(ascending=False)
top_7_countries = avg_total_trade.head(7).index.tolist()

print("Top 7 countries by average total trade:")
for i, country in enumerate(top_7_countries, 1):
    avg_trade = avg_total_trade[country]
    print(f"{i}. {country}: ${avg_trade:,.0f}")

# Filter data for top 7 countries
top_countries_data = trade_data[trade_data['country'].isin(top_7_countries)].copy()

# Create the plot
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

# Plot each country
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
for i, country in enumerate(top_7_countries):
    country_data = top_countries_data[top_countries_data['country'] == country].sort_values('year')
    plt.plot(country_data['year'], country_data['total_trade'] / 1e9, 
             label=country, linewidth=2.5, color=colors[i])

plt.title('Total Trade (Imports + Exports) for Top 7 Trading Countries', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Trade (Billion USD)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Show some statistics
print(f"\nData range: {trade_data['year'].min()}-{trade_data['year'].max()}")
print(f"Total observations plotted: {len(top_countries_data)}")

plt.savefig('top_7_trade_countries.png', dpi=300, bbox_inches='tight')
plt.close()

# Also create a more recent view (post-1950)
plt.figure(figsize=(14, 8))
recent_data = top_countries_data[top_countries_data['year'] >= 1950]

for i, country in enumerate(top_7_countries):
    country_data = recent_data[recent_data['country'] == country].sort_values('year')
    if len(country_data) > 0:
        plt.plot(country_data['year'], country_data['total_trade'] / 1e9, 
                 label=country, linewidth=2.5, color=colors[i])

plt.title('Total Trade (Imports + Exports) for Top 7 Trading Countries (1950-2014)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Trade (Billion USD)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('top_7_trade_countries_recent.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nPlots saved as 'top_7_trade_countries.png' and 'top_7_trade_countries_recent.png'")