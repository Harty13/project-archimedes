import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from dataloaders.dataloader import DataLoader
from dataloaders.education_dataloader import EducationDataLoader

# Load the education data
dataloader = EducationDataLoader(file_path='data/education/education_dataset.csv', countries=['USA', 'United Kingdom'])
data = dataloader.load_data()

# Create figure with subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(18, 14))

# Subplot 1: Main comparison
usa_data = data[data['country'] == 'USA'].sort_values('year')
uk_data = data[data['country'] == 'United Kingdom'].sort_values('year')

# Plot both countries
ax1.plot(usa_data['year'], usa_data['education'], marker='o', linewidth=3, label='USA', color='blue', markersize=6)
ax1.plot(uk_data['year'], uk_data['education'], marker='s', linewidth=3, label='United Kingdom', color='red', markersize=6)

# Mark regime change periods
# UK dominance period (1870-1914)
ax1.axvspan(1870, 1914, alpha=0.2, color='red', label='UK Dominance Era')
# Transition period (1914-1945)  
ax1.axvspan(1914, 1945, alpha=0.2, color='purple', label='Transition Era (WWI-WWII)')
# US dominance period (1945-2010)
ax1.axvspan(1945, 2010, alpha=0.2, color='blue', label='US Dominance Era')

# Find crossover points
common_years = set(usa_data['year']).intersection(set(uk_data['year']))
crossovers = []
for year in sorted(common_years):
    usa_val = usa_data[usa_data['year'] == year]['education'].iloc[0]
    uk_val = uk_data[uk_data['year'] == year]['education'].iloc[0]
    if year > 1870:
        prev_year = year - 5  # assuming 5-year intervals
        if prev_year in common_years:
            usa_prev = usa_data[usa_data['year'] == prev_year]['education'].iloc[0] if not usa_data[usa_data['year'] == prev_year].empty else None
            uk_prev = uk_data[uk_data['year'] == prev_year]['education'].iloc[0] if not uk_data[uk_data['year'] == prev_year].empty else None
            if usa_prev is not None and uk_prev is not None:
                if (usa_prev < uk_prev and usa_val > uk_val) or (usa_prev > uk_prev and usa_val < uk_val):
                    crossovers.append((year, usa_val))

# Mark crossover points
for year, val in crossovers:
    ax1.plot(year, val, marker='*', markersize=15, color='gold', markeredgecolor='black', markeredgewidth=2, label='Regime Change' if (year, val) == crossovers[0] else "")

ax1.set_title('Education Index: USA vs United Kingdom (Regime Change Analysis)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Education Index', fontsize=12)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Subplot 2: Difference plot
# Get common years and calculate differences
merged_data = pd.merge(usa_data, uk_data, on='year', suffixes=('_usa', '_uk'))
merged_data['difference'] = merged_data['education_usa'] - merged_data['education_uk']

ax2.plot(merged_data['year'], merged_data['difference'], marker='o', linewidth=3, color='green', markersize=6)
ax2.axhline(y=0, color='black', linestyle='--', alpha=0.7, label='Parity Line')
ax2.fill_between(merged_data['year'], merged_data['difference'], 0, 
                 where=(merged_data['difference'] > 0), color='blue', alpha=0.3, label='USA Advantage')
ax2.fill_between(merged_data['year'], merged_data['difference'], 0, 
                 where=(merged_data['difference'] < 0), color='red', alpha=0.3, label='UK Advantage')

# Mark regime periods on difference plot
ax2.axvspan(1870, 1914, alpha=0.1, color='red')
ax2.axvspan(1914, 1945, alpha=0.1, color='purple')  
ax2.axvspan(1945, 2010, alpha=0.1, color='blue')

ax2.set_title('Education Index Difference (USA - UK)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Education Index Difference', fontsize=12)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

# Subplot 3: Education Quantity Comparison
ax3.plot(usa_data['year'], usa_data['educated_quantity'], marker='o', linewidth=3, label='USA Quantity', color='blue', markersize=6)
ax3.plot(uk_data['year'], uk_data['educated_quantity'], marker='s', linewidth=3, label='UK Quantity', color='red', markersize=6)

# Mark regime periods
ax3.axvspan(1870, 1914, alpha=0.1, color='red')
ax3.axvspan(1914, 1945, alpha=0.1, color='purple')  
ax3.axvspan(1945, 2010, alpha=0.1, color='blue')

ax3.set_title('Education Quantity Index (USA vs UK)', fontsize=14, fontweight='bold')
ax3.set_xlabel('Year', fontsize=12)
ax3.set_ylabel('Education Quantity Index', fontsize=12)
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)

# Subplot 4: Education Quality Comparison
ax4.plot(usa_data['year'], usa_data['education_quality'], marker='o', linewidth=3, label='USA Quality', color='blue', markersize=6)
ax4.plot(uk_data['year'], uk_data['education_quality'], marker='s', linewidth=3, label='UK Quality', color='red', markersize=6)

# Mark regime periods
ax4.axvspan(1870, 1914, alpha=0.1, color='red')
ax4.axvspan(1914, 1945, alpha=0.1, color='purple')  
ax4.axvspan(1945, 2010, alpha=0.1, color='blue')

ax4.set_title('Education Quality Index (USA vs UK)', fontsize=14, fontweight='bold')
ax4.set_xlabel('Year', fontsize=12)
ax4.set_ylabel('Education Quality Index', fontsize=12)
ax4.legend(fontsize=10)
ax4.grid(True, alpha=0.3)

plt.tight_layout()

# Show enhanced statistics
print("\nEducation Data Summary:")
print(data.describe())
print(f"\nData shape: {data.shape}")
print(f"Countries included: {data['country'].unique()}")
print(f"Year range: {data['year'].min()} - {data['year'].max()}")

print("\nRegime Change Analysis:")
print("="*50)
usa_avg_early = merged_data[merged_data['year'] <= 1914]['education_usa'].mean()
uk_avg_early = merged_data[merged_data['year'] <= 1914]['education_uk'].mean()
usa_qty_early = merged_data[merged_data['year'] <= 1914]['educated_quantity_usa'].mean()
uk_qty_early = merged_data[merged_data['year'] <= 1914]['educated_quantity_uk'].mean()
usa_qual_early = merged_data[merged_data['year'] <= 1914]['education_quality_usa'].mean()
uk_qual_early = merged_data[merged_data['year'] <= 1914]['education_quality_uk'].mean()

print(f"Early Period (1870-1914):")
print(f"  USA - Overall: {usa_avg_early:.3f}, Quantity: {usa_qty_early:.3f}, Quality: {usa_qual_early:.3f}")
print(f"  UK  - Overall: {uk_avg_early:.3f}, Quantity: {uk_qty_early:.3f}, Quality: {uk_qual_early:.3f}")
print(f"  Advantages (USA - UK): Overall: {usa_avg_early - uk_avg_early:.3f}, Quantity: {usa_qty_early - uk_qty_early:.3f}, Quality: {usa_qual_early - uk_qual_early:.3f}")

usa_avg_late = merged_data[merged_data['year'] >= 1945]['education_usa'].mean()
uk_avg_late = merged_data[merged_data['year'] >= 1945]['education_uk'].mean()
usa_qty_late = merged_data[merged_data['year'] >= 1945]['educated_quantity_usa'].mean()
uk_qty_late = merged_data[merged_data['year'] >= 1945]['educated_quantity_uk'].mean()
usa_qual_late = merged_data[merged_data['year'] >= 1945]['education_quality_usa'].mean()
uk_qual_late = merged_data[merged_data['year'] >= 1945]['education_quality_uk'].mean()

print(f"\nLate Period (1945-2010):")
print(f"  USA - Overall: {usa_avg_late:.3f}, Quantity: {usa_qty_late:.3f}, Quality: {usa_qual_late:.3f}")
print(f"  UK  - Overall: {uk_avg_late:.3f}, Quantity: {uk_qty_late:.3f}, Quality: {uk_qual_late:.3f}")
print(f"  Advantages (USA - UK): Overall: {usa_avg_late - uk_avg_late:.3f}, Quantity: {usa_qty_late - uk_qty_late:.3f}, Quality: {usa_qual_late - uk_qual_late:.3f}")

# Save and show the plot
plt.savefig('education_data_plot.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nEnhanced plot saved as 'education_data_plot.png'")
