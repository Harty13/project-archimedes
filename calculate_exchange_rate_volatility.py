import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data/exchange_rates/processed_exchange_rate_data.csv')

# Calculate percentage returns (year-over-year changes)
df['returns'] = df['usd_per_gbp'].pct_change() * 100

# Calculate volatility (standard deviation of returns)
volatility = df['returns'].std()
annualized_volatility = volatility  # Already annual since we have yearly data

print("Exchange Rate Volatility Analysis")
print("=" * 40)
print(f"Data period: {df['year'].min()} - {df['year'].max()}")
print(f"Annual volatility: {volatility:.2f}%")
print(f"Average exchange rate: {df['usd_per_gbp'].mean():.2f} USD per GBP")
print(f"Min exchange rate: {df['usd_per_gbp'].min():.2f} USD per GBP ({df[df['usd_per_gbp'] == df['usd_per_gbp'].min()]['year'].values[0]})")
print(f"Max exchange rate: {df['usd_per_gbp'].max():.2f} USD per GBP ({df[df['usd_per_gbp'] == df['usd_per_gbp'].max()]['year'].values[0]})")

# Rolling volatility (5-year windows)
df['rolling_volatility'] = df['returns'].rolling(window=5).std()

# Plot the exchange rate and its volatility
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

# Exchange rate over time
ax1.plot(df['year'], df['usd_per_gbp'], linewidth=2, color='blue')
ax1.set_title('USD/GBP Exchange Rate Over Time')
ax1.set_ylabel('USD per GBP')
ax1.grid(True, alpha=0.3)

# Annual returns
ax2.plot(df['year'], df['returns'], linewidth=1, color='red', alpha=0.7)
ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
ax2.set_title('Annual Returns (%)')
ax2.set_ylabel('Return (%)')
ax2.grid(True, alpha=0.3)

# Rolling volatility
ax3.plot(df['year'], df['rolling_volatility'], linewidth=2, color='green')
ax3.set_title('5-Year Rolling Volatility')
ax3.set_xlabel('Year')
ax3.set_ylabel('Volatility (%)')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('exchange_rate_volatility_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Create volatility CSV for ratios folder
volatility_df = df[['year', 'rolling_volatility']].dropna()
volatility_df.columns = ['year', 'volatility']
volatility_df.to_csv('data/ratios/exchange_rate_volatility.csv', index=False)
print(f"\nExchange rate volatility data saved to data/ratios/exchange_rate_volatility.csv")
print(f"Data includes {len(volatility_df)} years with 5-year rolling volatility")

# Print some additional statistics
print("\nAdditional Statistics:")
print(f"Number of positive return years: {(df['returns'] > 0).sum()}")
print(f"Number of negative return years: {(df['returns'] < 0).sum()}")
print(f"Largest single-year gain: {df['returns'].max():.2f}%")
print(f"Largest single-year loss: {df['returns'].min():.2f}%")

# Identify periods of high volatility
high_volatility_threshold = volatility * 1.5
high_vol_years = df[abs(df['returns']) > high_volatility_threshold]['year'].tolist()
if high_vol_years:
    print(f"\nYears with exceptionally high volatility (>{high_volatility_threshold:.1f}%):")
    for year in high_vol_years:
        return_val = df[df['year'] == year]['returns'].values[0]
        print(f"  {year}: {return_val:.2f}%")