import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the processed food volatility data
df = pd.read_csv('data/food/food_volatility_processed.csv')

# Filter for China data
china_data = df[df['country'] == 'China'].copy()

# Get comparison data for US, UK and World
us_data = df[df['country'] == 'United States'].copy()
uk_data = df[df['country'] == 'United Kingdom'].copy()
world_data = df[df['country'] == 'World'].copy()

print("Food Price Volatility Analysis - China Focus")
print("=" * 50)
print(f"China data period: {china_data['year'].min()} - {china_data['year'].max()}")
print(f"Number of data points: {len(china_data)}")
print(f"Average volatility: {china_data['volatility'].mean():.2f}%")
print(f"Peak volatility: {china_data['volatility'].max():.2f}% in {china_data[china_data['volatility'] == china_data['volatility'].max()]['year'].values[0]}")
print(f"Lowest volatility: {china_data['volatility'].min():.2f}% in {china_data[china_data['volatility'] == china_data['volatility'].min()]['year'].values[0]}")

# Create comprehensive visualization
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: China volatility over time
ax1.plot(china_data['year'], china_data['volatility'], linewidth=2, color='red', marker='o', markersize=3)
ax1.set_title('China Food Price Volatility Over Time', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year')
ax1.set_ylabel('Volatility (%)')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, china_data['volatility'].max() * 1.1)

# Highlight key periods
high_vol_period = china_data[china_data['volatility'] > 8]
if len(high_vol_period) > 0:
    ax1.axvspan(high_vol_period['year'].min(), high_vol_period['year'].max(), 
                alpha=0.2, color='red', label='High Volatility Period')
    ax1.legend()

# Plot 2: Comparison of China, US, UK, and World volatility
ax2.plot(china_data['year'], china_data['volatility'], linewidth=2, color='red', 
         label='China', marker='o', markersize=2)
ax2.plot(us_data['year'], us_data['volatility'], linewidth=2, color='blue', 
         label='United States', marker='s', markersize=2)
ax2.plot(uk_data['year'], uk_data['volatility'], linewidth=2, color='purple', 
         label='United Kingdom', marker='d', markersize=2)
ax2.plot(world_data['year'], world_data['volatility'], linewidth=2, color='green', 
         label='World', marker='^', markersize=2)
ax2.set_title('Food Price Volatility: China vs US vs UK vs World', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year')
ax2.set_ylabel('Volatility (%)')
ax2.grid(True, alpha=0.3)
ax2.legend()

# Plot 3: Distribution of volatility values
ax3.hist(china_data['volatility'], bins=20, alpha=0.7, color='red', edgecolor='black')
ax3.axvline(china_data['volatility'].mean(), color='darkred', linestyle='--', 
            linewidth=2, label=f'Mean: {china_data["volatility"].mean():.2f}%')
ax3.axvline(china_data['volatility'].median(), color='orange', linestyle='--', 
            linewidth=2, label=f'Median: {china_data["volatility"].median():.2f}%')
ax3.set_title('Distribution of China Food Price Volatility', fontsize=14, fontweight='bold')
ax3.set_xlabel('Volatility (%)')
ax3.set_ylabel('Frequency')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Plot 4: Decade analysis
china_data['decade'] = (china_data['year'] // 10) * 10
decade_stats = china_data.groupby('decade')['volatility'].agg(['mean', 'std', 'count']).reset_index()
decade_stats = decade_stats[decade_stats['count'] >= 3]  # Only decades with sufficient data

bars = ax4.bar(decade_stats['decade'], decade_stats['mean'], 
               yerr=decade_stats['std'], capsize=5, alpha=0.7, color='red', edgecolor='black')
ax4.set_title('China Food Price Volatility by Decade', fontsize=14, fontweight='bold')
ax4.set_xlabel('Decade')
ax4.set_ylabel('Average Volatility (%)')
ax4.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bar, mean_val in zip(bars, decade_stats['mean']):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{mean_val:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.suptitle('China Food Price Volatility Analysis vs Major Powers\n(5-Year Rolling Standard Deviation of Inflation)', 
             fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()

# Ensure plots directory exists
os.makedirs('plots', exist_ok=True)

# Save the plot
plt.savefig('plots/food_volatility_china_uk_us_analysis.png', dpi=300, bbox_inches='tight')
print(f"\nVisualization saved to plots/food_volatility_china_uk_us_analysis.png")

plt.show()

# Additional analysis and insights
print("\nDetailed Analysis:")
print("-" * 30)

# Identify periods of extreme volatility
high_volatility = china_data[china_data['volatility'] > china_data['volatility'].quantile(0.75)]
low_volatility = china_data[china_data['volatility'] < china_data['volatility'].quantile(0.25)]

print(f"\nHigh Volatility Periods (Top 25%):")
for _, row in high_volatility.iterrows():
    print(f"  {row['year']}: {row['volatility']:.2f}%")

print(f"\nLow Volatility Periods (Bottom 25%):")
for _, row in low_volatility.iterrows():
    print(f"  {row['year']}: {row['volatility']:.2f}%")

# Decade comparison
print(f"\nDecade Analysis:")
for _, row in decade_stats.iterrows():
    print(f"  {int(row['decade'])}s: Mean = {row['mean']:.2f}%, Std = {row['std']:.2f}%, Count = {int(row['count'])} years")

# Trend analysis
if len(china_data) > 10:
    recent_years = china_data.tail(10)
    early_years = china_data.head(10)
    print(f"\nTrend Analysis:")
    print(f"  Last 10 years average: {recent_years['volatility'].mean():.2f}%")
    print(f"  First 10 years average: {early_years['volatility'].mean():.2f}%")
    
    # Calculate correlation with time to see if there's a trend
    correlation = china_data['year'].corr(china_data['volatility'])
    print(f"  Correlation with time: {correlation:.3f} ({'decreasing' if correlation < 0 else 'increasing'} trend)")