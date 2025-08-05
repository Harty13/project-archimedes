#!/usr/bin/env python3
"""
Script to check the earliest available GDP data for US and UK
"""

import sys
from pathlib import Path
import pandas as pd

# Add the dataloaders directory to the path
sys.path.append('dataloaders')

from gdp_per_capita_dataloader import GDPPerCapitaDataLoader

def main():
    """Main function to check earliest available GDP data"""
    print("Checking Earliest Available GDP Data for US and UK")
    print("=" * 55)
    
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
    
    print(f"\nAll available data:")
    print(f"Total records: {len(all_data)}")
    print(f"Year range: {all_data['Year'].min()} - {all_data['Year'].max()}")
    
    # Check earliest data for each country
    print(f"\nEarliest available data by country:")
    print("-" * 40)
    
    for country in countries:
        country_data = all_data[all_data['Entity'] == country]
        if not country_data.empty:
            earliest_year = country_data['Year'].min()
            latest_year = country_data['Year'].max()
            earliest_gdp = country_data[country_data['Year'] == earliest_year]['GDP per capita'].iloc[0]
            
            print(f"{country}:")
            print(f"  Earliest year: {earliest_year}")
            print(f"  Latest year: {latest_year}")
            print(f"  Total records: {len(country_data)}")
            print(f"  GDP in {earliest_year}: ${earliest_gdp:.0f}")
            
            # Show first 10 years of data
            early_data = country_data.head(10)
            print(f"  First 10 data points:")
            for _, row in early_data.iterrows():
                print(f"    {int(row['Year'])}: ${row['GDP per capita']:.0f}")
            print()
    
    # Find the earliest year where both countries have data
    us_data = all_data[all_data['Entity'] == 'United States']
    uk_data = all_data[all_data['Entity'] == 'United Kingdom']
    
    us_years = set(us_data['Year'])
    uk_years = set(uk_data['Year'])
    common_years = sorted(list(us_years & uk_years))
    
    if common_years:
        earliest_common = min(common_years)
        latest_common = max(common_years)
        
        print(f"Common data availability:")
        print(f"  Earliest year with both countries: {earliest_common}")
        print(f"  Latest year with both countries: {latest_common}")
        print(f"  Total common years: {len(common_years)}")
        
        # Show data for the earliest common year
        print(f"\nGDP data for {earliest_common}:")
        for country in countries:
            country_row = all_data[(all_data['Entity'] == country) & (all_data['Year'] == earliest_common)]
            if not country_row.empty:
                gdp_value = country_row['GDP per capita'].iloc[0]
                print(f"  {country}: ${gdp_value:.0f}")
    
    return all_data

if __name__ == "__main__":
    main()
