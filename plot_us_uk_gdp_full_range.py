#!/usr/bin/env python3
"""
Script to plot GDP per capita comparison between US and UK for the full available data range
"""

import sys
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Add the dataloaders directory to the path
sys.path.append('dataloaders')

from gdp_per_capita_dataloader import GDPPerCapitaDataLoader

def main():
    """Main function to create US vs UK GDP per capita plot for full data range"""
    print("GDP per Capita Comparison: United States vs United Kingdom (Full Range)")
    print("=" * 75)
    
    # Initialize the dataloader
    loader = GDPPerCapitaDataLoader()
    
    # Load the data
    loader.load_data()
    
    # Process data specifically for US and UK
    countries = ['United States', 'United Kingdom']
    loader.process_data(countries=countries)
    
    if loader.processed_data.empty:
        print("No data could be loaded for US and UK")
        return None
    
    # Get all available data (no year filtering)
    all_data = loader.processed_data.copy()
    
    # Filter to only years where both countries have data for better comparison
    us_data = all_data[all_data['Entity'] == 'United States']
    uk_data = all_data[all_data['Entity'] == 'United Kingdom']
    
    us_years = set(us_data['Year'])
    uk_years = set(uk_data['Year'])
    common_years = sorted(list(us_years & uk_years))
    
    # Create dataset with common years
    common_data = all_data[all_data['Year'].isin(common_years)].copy()
    common_data = common_data.sort_values(['Entity', 'Year'])
    
    print(f"\nFull range data summary:")
    print(f"UK data: {uk_data['Year'].min()} - {uk_data['Year'].max()} ({len(uk_data)} records)")
    print(f"US data: {us_data['Year'].min()} - {us_data['Year'].max()} ({len(us_data)} records)")
    print(f"Common years: {min(common_years)} - {max(common_years)} ({len(common_years)} years)")
    
    # Create comprehensive plots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('GDP per Capita: United States vs United Kingdom (Full Historical Range)', 
                 fontsize=16, fontweight='bold')
    
    # 1. Full range linear plot
    ax1 = axes[0, 0]
    for country in countries:
        country_data = common_data[common_data['Entity'] == country]
        if not country_data.empty:
            ax1.plot(country_data['Year'], country_data['GDP per capita'], 
                    label=country, linewidth=2, marker='o', markersize=2, alpha=0.8)
    
    ax1.set_title('GDP per Capita Over Time (Linear Scale)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('GDP per Capita (1990 International Dollars)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Log scale plot (better for long-term trends)
    ax2 = axes[0, 1]
    for country in countries:
        country_data = common_data[common_data['Entity'] == country]
        if not country_data.empty:
            ax2.semilogy(country_data['Year'], country_data['GDP per capita'], 
                        label=country, linewidth=2, marker='o', markersize=2, alpha=0.8)
    
    ax2.set_title('GDP per Capita Over Time (Log Scale)')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('GDP per Capita (Log Scale)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Ratio plot (US/UK)
    ax3 = axes[1, 0]
    us_common = common_data[common_data['Entity'] == 'United States'].set_index('Year')['GDP per capita']
    uk_common = common_data[common_data['Entity'] == 'United Kingdom'].set_index('Year')['GDP per capita']
    
    ratio = us_common / uk_common
    ax3.plot(ratio.index, ratio.values, linewidth=2, color='purple', alpha=0.8)
    ax3.axhline(y=1, color='black', linestyle='--', alpha=0.5, label='Equal GDP per capita')
    ax3.set_title('GDP per Capita Ratio (US / UK)')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Ratio')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Modern era focus (1800 onwards)
    ax4 = axes[1, 1]
    modern_data = common_data[common_data['Year'] >= 1800]
    
    for country in countries:
        country_data = modern_data[modern_data['Entity'] == country]
        if not country_data.empty:
            ax4.plot(country_data['Year'], country_data['GDP per capita'], 
                    label=country, linewidth=2, marker='o', markersize=3, alpha=0.8)
    
    ax4.set_title('GDP per Capita: Modern Era (1800 onwards)')
    ax4.set_xlabel('Year')
    ax4.set_ylabel('GDP per Capita (1990 International Dollars)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('us_uk_gdp_full_range.png', dpi=300, bbox_inches='tight')
    print("Plot saved as 'us_uk_gdp_full_range.png'")
    plt.show()
    
    # Export the full common data to CSV
    result_df = common_data[['Entity', 'Year', 'GDP per capita']].copy()
    result_df = result_df.sort_values(['Entity', 'Year'])
    
    result_df.to_csv('us_uk_gdp_full_range.csv', index=False)
    print(f"Full range data exported to 'us_uk_gdp_full_range.csv'")
    
    # Also export all available data (including non-common years)
    all_result_df = all_data[['Entity', 'Year', 'GDP per capita']].copy()
    all_result_df = all_result_df.sort_values(['Entity', 'Year'])
    all_result_df.to_csv('us_uk_gdp_all_available.csv', index=False)
    print(f"All available data exported to 'us_uk_gdp_all_available.csv'")
    
    print(f"\nDataset Summary:")
    print(f"Common years dataset: {len(result_df)} records")
    print(f"All available dataset: {len(all_result_df)} records")
    print(f"Countries: {result_df['Entity'].unique()}")
    print(f"Common year range: {result_df['Year'].min()} - {result_df['Year'].max()}")
    
    # Display summary statistics for key periods
    periods = [
        (1650, 1700, "Early Colonial"),
        (1700, 1800, "18th Century"),
        (1800, 1850, "Early Industrial"),
        (1850, 1900, "Late Industrial"),
        (1900, 1950, "Early Modern"),
        (1950, 2000, "Post-War"),
        (2000, 2022, "21st Century")
    ]
    
    print(f"\nSummary by Historical Periods:")
    print("-" * 50)
    
    for start_year, end_year, period_name in periods:
        period_data = result_df[
            (result_df['Year'] >= start_year) & 
            (result_df['Year'] <= end_year)
        ]
        
        if not period_data.empty:
            print(f"\n{period_name} ({start_year}-{end_year}):")
            for country in countries:
                country_period = period_data[period_data['Entity'] == country]
                if not country_period.empty:
                    avg_gdp = country_period['GDP per capita'].mean()
                    start_gdp = country_period['GDP per capita'].iloc[0] if len(country_period) > 0 else None
                    end_gdp = country_period['GDP per capita'].iloc[-1] if len(country_period) > 0 else None
                    
                    growth = ((end_gdp / start_gdp - 1) * 100) if start_gdp and end_gdp and start_gdp > 0 else 0
                    
                    print(f"  {country}: Avg ${avg_gdp:.0f}, Growth {growth:.1f}%")
    
    return result_df

if __name__ == "__main__":
    main()
