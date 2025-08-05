import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Load the child mortality data
df = pd.read_csv('us_uk_child_mortality_1800_1960.csv')

# Create the visualization
plt.figure(figsize=(14, 8))

# Plot both countries
plt.plot(df['year'], df['us_child_mortality'], label='United States', linewidth=2, color='#1f77b4')
plt.plot(df['year'], df['uk_child_mortality'], label='United Kingdom', linewidth=2, color='#ff7f0e')

# Customize the plot
plt.title('Child Mortality Rates: United States vs United Kingdom (1800-1960)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Child Mortality Rate (deaths per 1,000 live births)', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Set axis limits and ticks
plt.xlim(1800, 1960)
plt.xticks(range(1800, 1961, 20))
plt.ylim(0, 350)

# Add some annotations for key periods
plt.annotate('Industrial Revolution', xy=(1850, 250), xytext=(1820, 280),
            arrowprops=dict(arrowstyle='->', color='gray', alpha=0.7),
            fontsize=10, alpha=0.7)

plt.annotate('World War I', xy=(1918, 239), xytext=(1920, 280),
            arrowprops=dict(arrowstyle='->', color='gray', alpha=0.7),
            fontsize=10, alpha=0.7)

plt.annotate('Post-WWII\nPublic Health\nImprovements', xy=(1945, 48), xytext=(1920, 80),
            arrowprops=dict(arrowstyle='->', color='gray', alpha=0.7),
            fontsize=10, alpha=0.7)

# Tight layout
plt.tight_layout()

# Save the plot
plt.savefig('plots/child_mortality_1800_1960.png', dpi=300, bbox_inches='tight')
plt.close()  # Close the figure instead of showing

print("Child mortality visualization saved to: plots/child_mortality_1800_1960.png")

# Print some summary statistics
print(f"\nSummary Statistics (1800-1960):")
print(f"US Child Mortality:")
print(f"  1800: {df['us_child_mortality'].iloc[0]:.1f} deaths per 1,000")
print(f"  1960: {df['us_child_mortality'].iloc[-1]:.1f} deaths per 1,000")
print(f"  Improvement: {((df['us_child_mortality'].iloc[0] - df['us_child_mortality'].iloc[-1]) / df['us_child_mortality'].iloc[0] * 100):.1f}%")

print(f"\nUK Child Mortality:")
print(f"  1800: {df['uk_child_mortality'].iloc[0]:.1f} deaths per 1,000")
print(f"  1960: {df['uk_child_mortality'].iloc[-1]:.1f} deaths per 1,000")
print(f"  Improvement: {((df['uk_child_mortality'].iloc[0] - df['uk_child_mortality'].iloc[-1]) / df['uk_child_mortality'].iloc[0] * 100):.1f}%")