import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the processed primary enrollment data
df = pd.read_csv('data/education/primary_enrollment_processed.csv')

# Separate data for China and US
china_data = df[df['country'] == 'China'].copy()
us_data = df[df['country'] == 'United States'].copy()

print("Primary School Enrollment Analysis - China vs United States")
print("=" * 60)
print(f"China data period: {china_data['year'].min()} - {china_data['year'].max()}")
print(f"US data period: {us_data['year'].min()} - {us_data['year'].max()}")
print(f"China data points: {len(china_data)}")
print(f"US data points: {len(us_data)}")

# Calculate key statistics
print(f"\nChina Statistics:")
print(f"  Starting enrollment: {china_data['enrollment_rate'].iloc[0]:.2f}% in {china_data['year'].iloc[0]}")
print(f"  Ending enrollment: {china_data['enrollment_rate'].iloc[-1]:.2f}% in {china_data['year'].iloc[-1]}")
print(f"  Peak enrollment: {china_data['enrollment_rate'].max():.2f}% in {china_data[china_data['enrollment_rate'] == china_data['enrollment_rate'].max()]['year'].values[0]}")
print(f"  Average enrollment: {china_data['enrollment_rate'].mean():.2f}%")

print(f"\nUS Statistics:")
print(f"  Starting enrollment: {us_data['enrollment_rate'].iloc[0]:.2f}% in {us_data['year'].iloc[0]}")
print(f"  Ending enrollment: {us_data['enrollment_rate'].iloc[-1]:.2f}% in {us_data['year'].iloc[-1]}")
print(f"  Peak enrollment: {us_data['enrollment_rate'].max():.2f}% in {us_data[us_data['enrollment_rate'] == us_data['enrollment_rate'].max()]['year'].iloc[0]}")
print(f"  Average enrollment: {us_data['enrollment_rate'].mean():.2f}%")

# Create comprehensive visualization
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Time series comparison
ax1.plot(china_data['year'], china_data['enrollment_rate'], linewidth=3, color='red', 
         label='China', marker='o', markersize=4)
ax1.plot(us_data['year'], us_data['enrollment_rate'], linewidth=3, color='blue', 
         label='United States', marker='s', markersize=4)
ax1.set_title('Primary School Enrollment Rates Over Time', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year')
ax1.set_ylabel('Enrollment Rate (%)')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_ylim(0, 105)

# Add milestone markers
ax1.axhline(y=100, color='green', linestyle='--', alpha=0.7, label='Universal Education (100%)')
ax1.axhline(y=50, color='orange', linestyle='--', alpha=0.7, label='50% Threshold')

# Plot 2: Focus on overlapping period (1850-1997)
overlap_start = max(china_data['year'].min(), us_data['year'].min())
overlap_end = min(china_data['year'].max(), us_data['year'].max())
china_overlap = china_data[(china_data['year'] >= overlap_start) & (china_data['year'] <= overlap_end)]
us_overlap = us_data[(us_data['year'] >= overlap_start) & (us_data['year'] <= overlap_end)]

ax2.plot(china_overlap['year'], china_overlap['enrollment_rate'], linewidth=3, color='red', 
         label='China', marker='o', markersize=4)
ax2.plot(us_overlap['year'], us_overlap['enrollment_rate'], linewidth=3, color='blue', 
         label='United States', marker='s', markersize=4)
ax2.set_title(f'Enrollment Rates: Overlapping Period ({overlap_start}-{overlap_end})', 
              fontsize=14, fontweight='bold')
ax2.set_xlabel('Year')
ax2.set_ylabel('Enrollment Rate (%)')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_ylim(0, 105)

# Plot 3: Rate of change analysis
china_data_sorted = china_data.sort_values('year')
us_data_sorted = us_data.sort_values('year')

# Calculate year-over-year change where data is available
china_change = china_data_sorted['enrollment_rate'].diff()
us_change = us_data_sorted['enrollment_rate'].diff()

ax3.plot(china_data_sorted['year'].iloc[1:], china_change.iloc[1:], linewidth=2, color='red', 
         label='China', alpha=0.7)
ax3.plot(us_data_sorted['year'].iloc[1:], us_change.iloc[1:], linewidth=2, color='blue', 
         label='United States', alpha=0.7)
ax3.axhline(y=0, color='black', linestyle='-', alpha=0.5)
ax3.set_title('Year-over-Year Change in Enrollment Rate', fontsize=14, fontweight='bold')
ax3.set_xlabel('Year')
ax3.set_ylabel('Change in Enrollment Rate (%)')
ax3.grid(True, alpha=0.3)
ax3.legend()

# Plot 4: Key milestones and periods
milestone_data = []

# China milestones
china_50_pct = china_data[china_data['enrollment_rate'] >= 50].iloc[0] if len(china_data[china_data['enrollment_rate'] >= 50]) > 0 else None
china_90_pct = china_data[china_data['enrollment_rate'] >= 90].iloc[0] if len(china_data[china_data['enrollment_rate'] >= 90]) > 0 else None

# US milestones
us_50_pct = us_data[us_data['enrollment_rate'] >= 50].iloc[0] if len(us_data[us_data['enrollment_rate'] >= 50]) > 0 else None
us_90_pct = us_data[us_data['enrollment_rate'] >= 90].iloc[0] if len(us_data[us_data['enrollment_rate'] >= 90]) > 0 else None
us_100_pct = us_data[us_data['enrollment_rate'] >= 100].iloc[0] if len(us_data[us_data['enrollment_rate'] >= 100]) > 0 else None

milestones = ['50% Enrollment', '90% Enrollment', '100% Enrollment']
china_years = [
    china_50_pct['year'] if china_50_pct is not None else None,
    china_90_pct['year'] if china_90_pct is not None else None,
    None  # China didn't reach 100% in the dataset
]
us_years = [
    us_50_pct['year'] if us_50_pct is not None else None,
    us_90_pct['year'] if us_90_pct is not None else None,
    us_100_pct['year'] if us_100_pct is not None else None
]

# Create milestone comparison chart
x_pos = range(len(milestones))
china_positions = [y if y is not None else 0 for y in china_years]
us_positions = [y if y is not None else 0 for y in us_years]

bars1 = ax4.bar([x - 0.2 for x in x_pos], china_positions, 0.4, 
                label='China', color='red', alpha=0.7)
bars2 = ax4.bar([x + 0.2 for x in x_pos], us_positions, 0.4, 
                label='United States', color='blue', alpha=0.7)

ax4.set_title('Timeline to Education Milestones', fontsize=14, fontweight='bold')
ax4.set_xlabel('Milestone')
ax4.set_ylabel('Year Achieved')
ax4.set_xticks(x_pos)
ax4.set_xticklabels(milestones)
ax4.legend()
ax4.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for i, (china_year, us_year) in enumerate(zip(china_years, us_years)):
    if china_year is not None:
        ax4.text(i - 0.2, china_year + 5, str(int(china_year)), 
                ha='center', va='bottom', fontweight='bold')
    if us_year is not None:
        ax4.text(i + 0.2, us_year + 5, str(int(us_year)), 
                ha='center', va='bottom', fontweight='bold')

plt.suptitle('Primary School Enrollment: China vs United States\nHistorical Analysis (1820-2022)', 
             fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()

# Ensure plots directory exists
os.makedirs('plots', exist_ok=True)

# Save the plot
plt.savefig('plots/primary_enrollment_china_us_analysis.png', dpi=300, bbox_inches='tight')
print(f"\nVisualization saved to plots/primary_enrollment_china_us_analysis.png")

plt.show()

# Additional detailed analysis
print("\nDetailed Historical Analysis:")
print("-" * 40)

# Identify key periods
print("\nKey Historical Insights:")

if china_50_pct is not None and us_50_pct is not None:
    gap_50 = china_50_pct['year'] - us_50_pct['year']
    print(f"• US reached 50% enrollment {abs(gap_50):.0f} years {'before' if gap_50 > 0 else 'after'} China")

if china_90_pct is not None and us_90_pct is not None:
    gap_90 = china_90_pct['year'] - us_90_pct['year']
    print(f"• US reached 90% enrollment {abs(gap_90):.0f} years {'before' if gap_90 > 0 else 'after'} China")

# Find periods of rapid growth
china_rapid = china_data_sorted[china_change > 10] if len(china_change) > 0 else pd.DataFrame()
us_rapid = us_data_sorted[us_change > 10] if len(us_change) > 0 else pd.DataFrame()

if len(china_rapid) > 0:
    print(f"• China's periods of rapid growth (>10% increase): {[int(year) for year in china_rapid['year'].values]}")
if len(us_rapid) > 0:
    print(f"• US periods of rapid growth (>10% increase): {[int(year) for year in us_rapid['year'].values]}")

# Modern era comparison (1950+)
modern_china = china_data[china_data['year'] >= 1950]
modern_us = us_data[us_data['year'] >= 1950]

if len(modern_china) > 0 and len(modern_us) > 0:
    print(f"\nModern Era (1950+) Comparison:")
    print(f"• China average enrollment: {modern_china['enrollment_rate'].mean():.1f}%")
    print(f"• US average enrollment: {modern_us['enrollment_rate'].mean():.1f}%")