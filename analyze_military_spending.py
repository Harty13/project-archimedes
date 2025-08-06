import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the SIPRI military expenditure data
file_path = 'data/military/SIPRI-Milex-data-1949-2024_2.xlsx'

# Load the constant US$ sheet
df = pd.read_excel(file_path, sheet_name='Constant (2023) US$')

# The data needs cleaning - row 4 contains years, starting from row 5+ contains countries
# Let's properly parse this data
header_row = df.iloc[4]  # Row with years
data_start = 5  # Data starts from row 5

# Create proper column names from header row
years = []
for col in header_row:
    if pd.notna(col) and str(col).isdigit():
        years.append(int(col))
    elif col == 'Country':
        years.append('Country')
    else:
        years.append(col)

# Extract the data starting from row 5
clean_df = df.iloc[data_start:].copy()
clean_df.columns = years

# Reset index
clean_df = clean_df.reset_index(drop=True)

# Find US and China rows
first_col = clean_df.iloc[:, 0]
us_mask = first_col.astype(str).str.contains('United States', case=False, na=False)
china_mask = first_col.astype(str).str.contains('China', case=False, na=False)

print(f"Found US: {us_mask.sum()} entries")
print(f"Found China: {china_mask.sum()} entries")

# Extract US and China data
us_data = clean_df[us_mask].iloc[0] if us_mask.sum() > 0 else None
china_data = clean_df[china_mask].iloc[0] if china_mask.sum() > 0 else None

if us_data is not None:
    print(f"US country name: {us_data.iloc[0]}")
if china_data is not None:
    print(f"China country name: {china_data.iloc[0]}")

# Get year columns (numeric columns)
year_cols = [col for col in clean_df.columns if isinstance(col, int)]
year_cols.sort()
print(f"Available years: {year_cols[0]} to {year_cols[-1]}")

# Extract spending data for plotting
us_spending = []
china_spending = []
valid_years = []

for year in year_cols:
    us_val = us_data[year] if us_data is not None else None
    china_val = china_data[year] if china_data is not None else None
    
    # Convert to numeric, handling missing data
    try:
        us_num = float(us_val) if pd.notna(us_val) and str(us_val) not in ['.', '..', 'xxx'] else None
        china_num = float(china_val) if pd.notna(china_val) and str(china_val) not in ['.', '..', 'xxx'] else None
        
        if us_num is not None or china_num is not None:
            valid_years.append(year)
            us_spending.append(us_num)
            china_spending.append(china_num)
    except (ValueError, TypeError):
        continue

print(f"Data points found: {len(valid_years)} years from {min(valid_years)} to {max(valid_years)}")

# Create the plot
plt.figure(figsize=(12, 8))
plt.plot(valid_years, us_spending, 'b-', label='United States', linewidth=2, marker='o', markersize=3)
plt.plot(valid_years, china_spending, 'r-', label='China', linewidth=2, marker='s', markersize=3)

plt.title('Military Expenditure: US vs China (Constant 2023 US$ millions)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Military Spending (Constant 2023 US$ millions)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Format y-axis to show values in thousands for readability
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}B' if x >= 1000 else f'${x:.0f}M'))

# Save the plot
plt.savefig('us_china_military_spending.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nPlot saved as 'us_china_military_spending.png'")