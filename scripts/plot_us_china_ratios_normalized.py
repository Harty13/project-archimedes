import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the US-China dataset
df = pd.read_csv('/Users/erikschnell/Desktop/Dev/TrueWealth Hackathon/Project Archimedes/data/archimedes_dataset_us_china_1989_2024.csv', comment='#')

# Create log-normalized versions of all ratio columns
ratio_columns = [
    'child_mortality_volatility_ratio',
    'food_volatility_ratio', 
    'gdp_volatility_ratio',
    'exchange_rate_volatility'
]

# Apply log transformation (handling zeros and negative values)
log_data = {}
for col in ratio_columns:
    # Add small epsilon to handle zero values, take absolute value for negative values
    values = df[col].replace(0, np.nan)
    values = np.abs(values)
    log_data[f'log_{col}'] = np.log(values)

# Create DataFrame with log-transformed data
log_df = pd.DataFrame(log_data)
log_df['year'] = df['year']

# Create the plot
plt.figure(figsize=(14, 10))

# Plot each log-normalized ratio
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
line_styles = ['-', '--', '-.', ':']

for i, col in enumerate(ratio_columns):
    log_col = f'log_{col}'
    label = col.replace('_', ' ').title().replace('Volatility', 'Vol.')
    plt.plot(log_df['year'], log_df[log_col], 
             color=colors[i], linestyle=line_styles[i], linewidth=2.5, 
             marker='o', markersize=4, alpha=0.8, label=label)

# Customize the plot
plt.title('US vs China Ratios (Log-Normalized)\n1989-2024', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Log-Normalized Ratio Values', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
plt.legend(loc='upper right', fontsize=10, framealpha=0.9)

# Add horizontal line at y=0 for reference
plt.axhline(y=0, color='black', linestyle='-', alpha=0.5, linewidth=1)

# Improve layout
plt.tight_layout()

# Add some styling
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().tick_params(axis='both', which='major', labelsize=10)

# Set x-axis to show every 5 years
plt.xticks(range(1990, 2025, 5))

# Save the plot
plt.savefig('/Users/erikschnell/Desktop/Dev/TrueWealth Hackathon/Project Archimedes/plots/us_china_ratios_log_normalized.png', 
            dpi=300, bbox_inches='tight')
plt.show()

# Print summary statistics
print("\nSummary Statistics (Log-Normalized):")
print("="*50)
for col in ratio_columns:
    log_col = f'log_{col}'
    stats = log_df[log_col].describe()
    print(f"\n{col.replace('_', ' ').title()}:")
    print(f"  Mean: {stats['mean']:.3f}")
    print(f"  Std:  {stats['std']:.3f}")
    print(f"  Min:  {stats['min']:.3f}")
    print(f"  Max:  {stats['max']:.3f}")