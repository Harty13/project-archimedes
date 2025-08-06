import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataloaders.load_trade_data import load_trade_data

print("Loading trade data...")
trade_data = load_trade_data()

# Filter for UK, USA, and China
countries = ['GBR', 'USA', 'CHN']
data = trade_data[trade_data['country'].isin(countries)].copy()

# Remove rows with zero values
data = data[(data['total_exports'] > 0) & (data['total_imports'] > 0)]

# Calculate export/import ratio
data['ratio'] = data['total_exports'] / data['total_imports']

print("Data summary:")
for country in countries:
    c_data = data[data['country'] == country]
    print(f"{country}: {len(c_data)} observations, {c_data['year'].min()}-{c_data['year'].max()}")

# Plot
plt.figure(figsize=(12, 7))
colors = {'GBR': 'blue', 'USA': 'red', 'CHN': 'green'}
labels = {'GBR': 'UK', 'USA': 'USA', 'CHN': 'China'}

for country in countries:
    c_data = data[data['country'] == country].sort_values('year')
    plt.plot(c_data['year'], c_data['ratio'], 
             color=colors[country], label=labels[country], linewidth=2)

plt.axhline(y=1, color='black', linestyle='--', alpha=0.5, label='Balance')
plt.title('Export/Import Ratios: UK, USA, China')
plt.xlabel('Year')
plt.ylabel('Export/Import Ratio')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('plots/export_import_ratios.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nSummary statistics:")
for country in countries:
    c_data = data[data['country'] == country]
    print(f"{labels[country]}: mean={c_data['ratio'].mean():.2f}, median={c_data['ratio'].median():.2f}")