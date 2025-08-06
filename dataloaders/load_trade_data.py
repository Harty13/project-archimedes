import pandas as pd
import numpy as np

def load_trade_data():
    """
    Load and process trade data from TRADHIST_v4.dta
    Returns total exports and imports for each country by year
    """
    
    # Load the .dta file
    file_path = 'data/trade/TRADHIST_v4.dta'
    
    print("Loading trade data...")
    df = pd.read_stata(file_path)
    
    print(f"Loaded {len(df):,} rows with {len(df.columns)} columns")
    
    # Method 1: Use the pre-calculated totals (XPTOT and IPTOT)
    # These appear to be total exports and imports for each country
    
    # Get unique country-year combinations with their total exports/imports
    country_totals = df[['iso_o', 'year', 'XPTOT_o', 'IPTOT_o']].copy()
    country_totals = country_totals.rename(columns={
        'iso_o': 'country',
        'XPTOT_o': 'total_exports',
        'IPTOT_o': 'total_imports'
    })
    
    # Also get destination country data
    dest_totals = df[['iso_d', 'year', 'XPTOT_d', 'IPTOT_d']].copy()
    dest_totals = dest_totals.rename(columns={
        'iso_d': 'country',
        'XPTOT_d': 'total_exports',
        'IPTOT_d': 'total_imports'
    })
    
    # Combine origin and destination data
    all_totals = pd.concat([country_totals, dest_totals], ignore_index=True)
    
    # Remove duplicates and empty country codes
    all_totals = all_totals[all_totals['country'] != '']
    all_totals = all_totals.drop_duplicates(subset=['country', 'year'])
    
    # Remove rows with missing data
    all_totals = all_totals.dropna(subset=['total_exports', 'total_imports'])
    
    # Sort by country and year
    all_totals = all_totals.sort_values(['country', 'year']).reset_index(drop=True)
    
    print(f"\nProcessed data: {len(all_totals):,} country-year observations")
    print(f"Countries: {all_totals['country'].nunique()}")
    print(f"Years: {all_totals['year'].min()}-{all_totals['year'].max()}")
    
    return all_totals

def get_country_summary(trade_data, country_code):
    """Get summary statistics for a specific country"""
    country_data = trade_data[trade_data['country'] == country_code]
    if len(country_data) == 0:
        print(f"No data found for country: {country_code}")
        return None
    
    print(f"\nSummary for {country_code}:")
    print(f"Years available: {country_data['year'].min()}-{country_data['year'].max()}")
    print(f"Total observations: {len(country_data)}")
    print(f"Average annual exports: ${country_data['total_exports'].mean():,.0f}")
    print(f"Average annual imports: ${country_data['total_imports'].mean():,.0f}")
    
    return country_data

if __name__ == "__main__":
    # Load the data
    trade_data = load_trade_data()
    
    # Show sample of the data
    print("\nSample of loaded data:")
    print(trade_data.head(10))
    
    # Show some summary statistics
    print("\nTop 10 countries by average exports:")
    avg_exports = trade_data.groupby('country')['total_exports'].mean().sort_values(ascending=False)
    print(avg_exports.head(10))
    
    # Show available countries
    print(f"\nAll available countries ({trade_data['country'].nunique()} total):")
    countries = sorted(trade_data['country'].unique())
    for i, country in enumerate(countries[:20]):  # Show first 20
        print(f"{i+1:2d}. {country}")
    if len(countries) > 20:
        print(f"... and {len(countries)-20} more countries")
    
    # Example: Get data for specific countries
    print("\n" + "="*50)
    for country in ['USA', 'GBR', 'DEU', 'CHN', 'JPN']:  # Common ISO codes
        get_country_summary(trade_data, country)