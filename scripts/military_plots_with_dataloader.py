import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataloaders.midb_dataloader import MIDBDataLoader

def create_military_conflict_plots():
    """
    Create three time-series plots for military conflict analysis using MIDB data.
    
    Plots:
    1A. Escalation (HiAct) - normalized 0-1 with red dots for Orig=1 & RevState=1
    1B. Hostility (HostLev) - normalized 0-1 with red dots for Orig=1 & RevState=1  
    2.  Human Cost (Fatality) - raw scale 0-6, no dots
    """
    
    # Initialize dataloader
    print("Loading MIDB 5.0 conflict data...")
    loader = MIDBDataLoader('data/military/MIDB 5.0.csv')
    
    # Load and get summary
    conflict_data = loader.load_data()
    print(f"Loaded {len(conflict_data)} conflict records")
    
    # Get top 6 countries by conflict frequency
    top_countries = loader.get_top_countries(n=6)
    country_names = [loader.country_mapping.get(c, f'Code_{c}') for c in top_countries]
    print(f"Top countries: {', '.join(country_names)}")
    
    # Filter data for top countries
    filtered_data = conflict_data[conflict_data['ccode'].isin(top_countries)].copy()
    
    # Set up plotting
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    line_styles = ['-', '--', '-.', ':', '-', '--']
    
    # Create figure with subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 16))
    
    print("Creating time-series plots...")
    
    # Process each country
    for i, ccode in enumerate(top_countries):
        country = loader.country_mapping.get(ccode, f'Code_{ccode}')
        country_data = filtered_data[filtered_data['ccode'] == ccode].copy()
        
        print(f"Processing {country} ({len(country_data)} conflicts)")
        
        # Plot 1A - Escalation (HiAct)
        hiact_data = country_data.dropna(subset=['hiact'])
        if len(hiact_data) > 0:
            # Aggregate by year - maximum HiAct per year
            yearly_hiact = hiact_data.groupby('styear').agg({
                'hiact': 'max',
                'orig': 'sum',
                'revstate': 'sum'
            }).reset_index()
            
            # Normalize HiAct (0-21 -> 0-1)
            yearly_hiact['hiact_norm'] = yearly_hiact['hiact'] / 21
            
            # Plot the line
            ax1.plot(yearly_hiact['styear'], yearly_hiact['hiact_norm'], 
                    color=colors[i], linestyle=line_styles[i], linewidth=1.5, 
                    label=country, alpha=0.8)
            
            # Add red dots for years with Orig=1 AND RevState=1
            red_dot_years = hiact_data[
                (hiact_data['orig'] == 1) & (hiact_data['revstate'] == 1)
            ]['styear'].unique()
            
            if len(red_dot_years) > 0:
                red_dots = yearly_hiact[yearly_hiact['styear'].isin(red_dot_years)]
                ax1.scatter(red_dots['styear'], red_dots['hiact_norm'], 
                           color='red', s=25, alpha=0.8, zorder=5)
        
        # Plot 1B - Hostility (HostLev)
        hostlev_data = country_data.dropna(subset=['hostlev'])
        if len(hostlev_data) > 0:
            # Aggregate by year - maximum HostLev per year
            yearly_hostlev = hostlev_data.groupby('styear').agg({
                'hostlev': 'max',
                'orig': 'sum',
                'revstate': 'sum'
            }).reset_index()
            
            # Normalize HostLev (1-5 -> 0-1)
            yearly_hostlev['hostlev_norm'] = (yearly_hostlev['hostlev'] - 1) / 4
            
            # Plot the line
            ax2.plot(yearly_hostlev['styear'], yearly_hostlev['hostlev_norm'], 
                    color=colors[i], linestyle=line_styles[i], linewidth=1.5, 
                    label=country, alpha=0.8)
            
            # Add red dots for years with Orig=1 AND RevState=1
            red_dot_years = hostlev_data[
                (hostlev_data['orig'] == 1) & (hostlev_data['revstate'] == 1)
            ]['styear'].unique()
            
            if len(red_dot_years) > 0:
                red_dots = yearly_hostlev[yearly_hostlev['styear'].isin(red_dot_years)]
                ax2.scatter(red_dots['styear'], red_dots['hostlev_norm'], 
                           color='red', s=25, alpha=0.8, zorder=5)
        
        # Plot 2 - Human Cost (Fatality)
        fatality_data = country_data.dropna(subset=['fatality'])
        if len(fatality_data) > 0:
            # Aggregate by year - maximum Fatality per year
            yearly_fatality = fatality_data.groupby('styear')['fatality'].max().reset_index()
            
            # Plot the line (no normalization)
            ax3.plot(yearly_fatality['styear'], yearly_fatality['fatality'], 
                    color=colors[i], linestyle=line_styles[i], linewidth=1.5, 
                    label=country, alpha=0.8)
    
    # Configure Plot 1A
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Max Escalation per Year (HiAct/21)')
    ax1.set_title('Plot 1A - Military Escalation Over Time (1816-2014)')
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(1816, 2014)
    ax1.set_ylim(0, 1)
    
    # Configure Plot 1B  
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Max Hostility per Year (HostLev/5)')
    ax2.set_title('Plot 1B - Military Hostility Over Time (1816-2014)')
    ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(1816, 2014)
    ax2.set_ylim(0, 1)
    
    # Configure Plot 2
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Max Human Cost per Year (Fatality 0-6)')
    ax3.set_title('Plot 2 - Military Conflict Human Cost Over Time (1816-2014)')
    ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(1816, 2014)
    ax3.set_ylim(0, 6)
    
    # Adjust layout
    plt.tight_layout()
    plt.subplots_adjust(right=0.84)
    
    # Save plot
    plt.savefig('military_conflict_analysis_dataloader.png', dpi=300, bbox_inches='tight')
    
    print("\n✅ Military conflict plots created successfully!")
    print("📊 Each line shows maximum conflict intensity per year")
    print("🔴 Red dots: Years with conflicts where country was originator AND had regime change")
    print(f"🌍 Countries analyzed: {', '.join(country_names)}")
    
    # Print summary statistics
    summary = loader.get_country_summary()
    print(f"\n📈 Country Summary (Top {len(top_countries)}):")
    print(summary.head(len(top_countries)))

if __name__ == "__main__":
    create_military_conflict_plots()