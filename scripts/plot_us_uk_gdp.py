#!/usr/bin/env python3
"""
Simplified script to plot GDP per capita comparison between US and UK from 1850-1960
"""

import sys
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# Add the dataloaders directory to the path
sys.path.append('dataloaders')

from gdp_per_capita_dataloader import GDPPerCapitaDataLoader

def main():
    """Main function to create US vs UK GDP per capita plot for 1850-1960"""
    print("GDP per Capita Comparison: United States vs United Kingdom (1850-1960)")
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
    
    # Filter data for the period 1850-1960
    filtered_data = loader.processed_data[
        (loader.processed_data['Year'] >= 1850) & 
        (loader.processed_data['Year'] <= 1960)
    ].copy()
    
    if filtered_data.empty:
        print("No data available for the period 1850-1960")
        return None
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Plot data for each country
    for country in countries:
        country_data = filtered_data[filtered_data['Entity'] == country]
        if not country_data.empty:
            plt.plot(country_data['Year'], country_data['GDP per capita'], 
                    label=country, linewidth=2, marker='o', markersize=4, alpha=0.8)
    
    plt.title('GDP per Capita: United States vs United Kingdom (1850-1960)', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('GDP per Capita (1990 International Dollars)', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('us_uk_gdp_1850_1960.png', dpi=300, bbox_inches='tight')
    print("Plot saved as 'us_uk_gdp_1850_1960.png'")
    plt.show()
    
    # Create and return the DataFrame
    result_df = filtered_data[['Entity', 'Year', 'GDP per capita']].copy()
    result_df = result_df.sort_values(['Entity', 'Year'])
    
    print(f"\nDataFrame created with {len(result_df)} records")
    print(f"Countries: {result_df['Entity'].unique()}")
    print(f"Year range: {result_df['Year'].min()} - {result_df['Year'].max()}")
    
    # Display summary statistics
    print("\nSummary Statistics:")
    print("-" * 30)
    for country in countries:
        country_subset = result_df[result_df['Entity'] == country]
        if not country_subset.empty:
            print(f"\n{country}:")
            print(f"  Records: {len(country_subset)}")
            print(f"  GDP range: ${country_subset['GDP per capita'].min():.0f} - ${country_subset['GDP per capita'].max():.0f}")
            print(f"  Average GDP: ${country_subset['GDP per capita'].mean():.0f}")
    
    # Export the DataFrame
    result_df.to_csv('us_uk_gdp_1850_1960.csv', index=False)
    print(f"\nData exported to 'us_uk_gdp_1850_1960.csv'")
    
    return result_df

if __name__ == "__main__":
    main()
