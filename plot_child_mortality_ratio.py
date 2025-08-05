import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Load the ratio data
df = pd.read_csv('us_uk_child_mortality_ratio_1800_1960.csv')

# Create the visualization
plt.figure(figsize=(14, 8))

# Plot the ratio
plt.plot(df['year'], df['us_uk_child_mortality_ratio'], linewidth=2, color='#2E8B57', label='US/UK Child Mortality Ratio')

# Add horizontal line at ratio = 1.0 (parity)
plt.axhline(y=1.0, color='red', linestyle='--', alpha=0.7, linewidth=2, label='Parity (US = UK)')

# Fill areas above and below parity
plt.fill_between(df['year'], df['us_uk_child_mortality_ratio'], 1.0, 
                 where=(df['us_uk_child_mortality_ratio'] > 1.0), alpha=0.3, color='orange', 
                 label='US Worse than UK')
plt.fill_between(df['year'], df['us_uk_child_mortality_ratio'], 1.0, 
                 where=(df['us_uk_child_mortality_ratio'] < 1.0), alpha=0.3, color='lightblue', 
                 label='US Better than UK')

# Customize the plot
plt.title('US to UK Child Mortality Rate Ratio (1800-1960)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ratio (US/UK Child Mortality Rate)', fontsize=12)
plt.legend(fontsize=11, loc='upper right')
plt.grid(True, alpha=0.3)

# Set axis limits and ticks
plt.xlim(1800, 1960)
plt.xticks(range(1800, 1961, 20))
plt.ylim(0.7, 1.7)

# Add annotations for key periods
plt.annotate('US 66% worse\n(1841)', xy=(1841, 1.66), xytext=(1820, 1.55),
            arrowprops=dict(arrowstyle='->', color='gray', alpha=0.7),
            fontsize=10, alpha=0.7)

plt.annotate('US 26% better\n(1941)', xy=(1941, 0.74), xytext=(1920, 0.8),
            arrowprops=dict(arrowstyle='->', color='gray', alpha=0.7),
            fontsize=10, alpha=0.7)

plt.annotate('Multiple crossings\nof parity', xy=(1920, 1.0), xytext=(1880, 1.4),
            arrowprops=dict(arrowstyle='->', color='gray', alpha=0.7),
            fontsize=10, alpha=0.7)

# Tight layout
plt.tight_layout()

# Save the plot
plt.savefig('plots/child_mortality_ratio_1800_1960.png', dpi=300, bbox_inches='tight')
plt.close()

print("Child mortality ratio visualization saved to: plots/child_mortality_ratio_1800_1960.png")

# Additional analysis
print(f"\nDetailed Ratio Analysis:")
print(f"1800: US was {((df['us_uk_child_mortality_ratio'].iloc[0] - 1) * 100):.1f}% worse than UK")
print(f"1960: US was {((df['us_uk_child_mortality_ratio'].iloc[-1] - 1) * 100):.1f}% worse than UK")

# Find periods where US was better
us_better = df[df['us_uk_child_mortality_ratio'] < 1.0]
if not us_better.empty:
    print(f"US was better than UK during {len(us_better)} years:")
    print(f"  From {us_better['year'].min()} to {us_better['year'].max()}")
    print(f"  Best US performance: {us_better['us_uk_child_mortality_ratio'].min():.3f} in {us_better.loc[us_better['us_uk_child_mortality_ratio'].idxmin(), 'year']}")

# Convergence trend
early_avg = df[df['year'] <= 1820]['us_uk_child_mortality_ratio'].mean()
late_avg = df[df['year'] >= 1940]['us_uk_child_mortality_ratio'].mean()
print(f"\nConvergence trend:")
print(f"Early period (1800-1820) average ratio: {early_avg:.2f}")
print(f"Late period (1940-1960) average ratio: {late_avg:.2f}")
print(f"Convergence toward parity: {((early_avg - late_avg) / early_avg * 100):.1f}% reduction in gap")