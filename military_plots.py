import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and prepare data
df = pd.read_csv('data/military/MIDB 5.0.csv')
cols = ['styear', 'ccode', 'revstate', 'fatality', 'hiact', 'hostlev', 'orig']
df_filtered = df[cols].copy()

# Treat values < 0 as missing
df_filtered = df_filtered.replace({col: {val: np.nan for val in df_filtered[col].unique() if val < 0} for col in df_filtered.columns})

# Country mapping
country_mapping = {
    2: 'USA',
    365: 'RUS', 
    200: 'GBR',
    710: 'CHN',
    640: 'TUR',
    220: 'FRA'
}

# Select top 6 countries
top_countries = [2, 365, 200, 710, 640, 220]

# Filter data for selected countries
df_plot = df_filtered[df_filtered['ccode'].isin(top_countries)].copy()
df_plot['country'] = df_plot['ccode'].map(country_mapping)

# Set up the plotting style
plt.style.use('default')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
line_styles = ['-', '--', '-.', ':', '-', '--']

# Create figure with subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 15))

# Plot 1A - Escalation (HiAct)
print("Creating Plot 1A - Escalation (HiAct)")
for i, (ccode, country) in enumerate(zip(top_countries, [country_mapping[c] for c in top_countries])):
    country_data = df_plot[df_plot['ccode'] == ccode].copy()
    
    # Remove rows with missing HiAct values
    country_data = country_data.dropna(subset=['hiact'])
    
    if len(country_data) > 0:
        # Aggregate by year - using maximum HiAct value per year
        yearly_data = country_data.groupby('styear').agg({
            'hiact': 'max',  # Maximum escalation level in that year
            'orig': 'sum',   # Count of conflicts where country was originator
            'revstate': 'sum'  # Count of conflicts with regime change
        }).reset_index()
        
        # Normalize HiAct (0-21 -> 0-1)
        yearly_data['hiact_norm'] = yearly_data['hiact'] / 21
        
        # Plot the line
        ax1.plot(yearly_data['styear'], yearly_data['hiact_norm'], 
                color=colors[i], linestyle=line_styles[i], linewidth=1.5, 
                label=country, alpha=0.8)
        
        # Add red dots where there was at least one conflict with Orig=1 AND RevState=1
        red_dot_years = country_data[(country_data['orig'] == 1) & (country_data['revstate'] == 1)]['styear'].unique()
        if len(red_dot_years) > 0:
            red_dot_data = yearly_data[yearly_data['styear'].isin(red_dot_years)]
            ax1.scatter(red_dot_data['styear'], red_dot_data['hiact_norm'], 
                       color='red', s=20, alpha=0.7, zorder=5)

ax1.set_xlabel('Year')
ax1.set_ylabel('Escalation (HiAct/21)')
ax1.set_title('Plot 1A - Military Escalation Over Time (1816-2014)')
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(1816, 2014)
ax1.set_ylim(0, 1)

# Plot 1B - Hostility (HostLev)
print("Creating Plot 1B - Hostility (HostLev)")
for i, (ccode, country) in enumerate(zip(top_countries, [country_mapping[c] for c in top_countries])):
    country_data = df_plot[df_plot['ccode'] == ccode].copy()
    
    # Remove rows with missing HostLev values
    country_data = country_data.dropna(subset=['hostlev'])
    
    if len(country_data) > 0:
        # Aggregate by year - using maximum HostLev value per year
        yearly_data = country_data.groupby('styear').agg({
            'hostlev': 'max',  # Maximum hostility level in that year
            'orig': 'sum',   # Count of conflicts where country was originator
            'revstate': 'sum'  # Count of conflicts with regime change
        }).reset_index()
        
        # Normalize HostLev (1-5 -> 0-1)
        yearly_data['hostlev_norm'] = (yearly_data['hostlev'] - 1) / 4
        
        # Plot the line
        ax2.plot(yearly_data['styear'], yearly_data['hostlev_norm'], 
                color=colors[i], linestyle=line_styles[i], linewidth=1.5, 
                label=country, alpha=0.8)
        
        # Add red dots where there was at least one conflict with Orig=1 AND RevState=1
        red_dot_years = country_data[(country_data['orig'] == 1) & (country_data['revstate'] == 1)]['styear'].unique()
        if len(red_dot_years) > 0:
            red_dot_data = yearly_data[yearly_data['styear'].isin(red_dot_years)]
            ax2.scatter(red_dot_data['styear'], red_dot_data['hostlev_norm'], 
                       color='red', s=20, alpha=0.7, zorder=5)

ax2.set_xlabel('Year')
ax2.set_ylabel('Hostility (HostLev/5)')
ax2.set_title('Plot 1B - Military Hostility Over Time (1816-2014)')
ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1816, 2014)
ax2.set_ylim(0, 1)

# Plot 2 - Human Cost (Fatality)
print("Creating Plot 2 - Human Cost (Fatality)")
for i, (ccode, country) in enumerate(zip(top_countries, [country_mapping[c] for c in top_countries])):
    country_data = df_plot[df_plot['ccode'] == ccode].copy()
    
    # Remove rows with missing Fatality values
    country_data = country_data.dropna(subset=['fatality'])
    
    if len(country_data) > 0:
        # Aggregate by year - using maximum Fatality value per year
        yearly_data = country_data.groupby('styear')['fatality'].max().reset_index()
        
        # Plot the line (no normalization for fatality)
        ax3.plot(yearly_data['styear'], yearly_data['fatality'], 
                color=colors[i], linestyle=line_styles[i], linewidth=1.5, 
                label=country, alpha=0.8)

ax3.set_xlabel('Year')
ax3.set_ylabel('Human Cost (Fatality Category 0-6)')
ax3.set_title('Plot 2 - Military Conflict Human Cost Over Time (1816-2014)')
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax3.grid(True, alpha=0.3)
ax3.set_xlim(1816, 2014)
ax3.set_ylim(0, 6)

# Adjust layout to prevent legend cutoff
plt.tight_layout()
plt.subplots_adjust(right=0.85)

# Save the plot
plt.savefig('military_conflict_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nPlots created successfully!")
print("Red dots indicate conflicts where the country was both the originator (Orig=1) and experienced regime change (RevState=1)")
print(f"Selected countries: {', '.join([country_mapping[c] for c in top_countries])}")