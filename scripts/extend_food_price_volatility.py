#!/usr/bin/env python3
"""
Script to extend the US/UK food price volatility ratio to 1960
by incorporating US wheat price data from the Excel file
"""

import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add the dataloaders directory to the path
sys.path.append('dataloaders')

from agprice_dataloader import AgPriceDataLoader

def load_us_wheat_data():
    """Load US wheat price data from Excel file"""
    print("Loading US wheat price data from Excel file...")
    
    try:
        # Read the Table01 sheet which contains wheat prices
        df = pd.read_excel('data/food/Wheat Data-All Years (2).xlsx', sheet_name='Table01')
        
        # Clean up the data - skip header rows and get the relevant columns
        # The data starts from row 1 (0-indexed), with marketing year and price
        df_clean = df.iloc[1:].copy()  # Skip the header row
        
        # Extract year and price columns
        # Marketing year is in column 1, price is in column 6
        df_clean = df_clean[['Unnamed: 1', 'Unnamed: 6']].copy()
        df_clean.columns = ['Marketing_Year', 'Price']
        
        # Clean the data
        df_clean = df_clean.dropna()
        
        # Extract year from marketing year (e.g., "1866/67" -> 1866)
        df_clean['Year'] = df_clean['Marketing_Year'].astype(str).str.split('/').str[0]
        df_clean['Year'] = pd.to_numeric(df_clean['Year'], errors='coerce')
        
        # Clean price data
        df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce')
        
        # Remove invalid data
        df_clean = df_clean.dropna()
        df_clean = df_clean[df_clean['Year'] >= 1860]  # Start from 1860
        df_clean = df_clean[df_clean['Year'] <= 1960]  # End at 1960
        
        # Keep only Year and Price columns
        us_wheat = df_clean[['Year', 'Price']].copy()
        us_wheat = us_wheat.sort_values('Year').reset_index(drop=True)
        
        print(f"Loaded US wheat data: {len(us_wheat)} records ({us_wheat['Year'].min():.0f}-{us_wheat['Year'].max():.0f})")
        return us_wheat
        
    except Exception as e:
        print(f"Error loading US wheat data: {e}")
        return pd.DataFrame()

def load_uk_grain_data():
    """Load UK grain price data from chicago_uk_grain_prices.csv"""
    print("Loading UK grain price data...")
    
    try:
        # Load the combined grain prices file
        df = pd.read_csv("data/food/chicago_uk_grain_prices.csv")
        
        # Filter for UK data
        uk_data = df[df['country'] == 'UK'].copy()
        
        if uk_data.empty:
            print("No UK data found in chicago_uk_grain_prices.csv")
            return pd.DataFrame()
        
        # Convert to annual averages
        uk_annual = uk_data.groupby('year')['grain_price'].mean().reset_index()
        uk_annual.columns = ['Year', 'Price']
        
        # Filter to reasonable year range
        uk_annual = uk_annual[uk_annual['Year'] >= 1860]
        uk_annual = uk_annual[uk_annual['Year'] <= 1960]
        
        uk_annual = uk_annual.sort_values('Year').reset_index(drop=True)
        
        print(f"UK grain data: {uk_annual['Year'].min()}-{uk_annual['Year'].max()} ({len(uk_annual)} records)")
        return uk_annual
        
    except Exception as e:
        print(f"Error loading UK grain data: {e}")
        return pd.DataFrame()

def calculate_extended_volatility_ratio(us_data, uk_data, window=2):
    """Calculate extended price volatility ratio with rolling window on normalized prices"""
    print(f"Calculating extended volatility ratios with {window}-year window...")
    
    # Merge the datasets on common years
    merged_data = pd.merge(us_data, uk_data, on='Year', how='inner', suffixes=('_US', '_UK'))
    
    if merged_data.empty:
        print("No common years found between US and UK data")
        return pd.DataFrame()
    
    print(f"Common years: {merged_data['Year'].min()}-{merged_data['Year'].max()} ({len(merged_data)} years)")
    
    # Sort by year
    merged_data = merged_data.sort_values('Year').reset_index(drop=True)
    
    # Normalize prices to their respective means (removes scale differences)
    us_mean = merged_data['Price_US'].mean()
    uk_mean = merged_data['Price_UK'].mean()
    
    merged_data['US_Price_Normalized'] = merged_data['Price_US'] / us_mean
    merged_data['UK_Price_Normalized'] = merged_data['Price_UK'] / uk_mean
    
    print(f"US price normalization: mean = {us_mean:.2f}")
    print(f"UK price normalization: mean = {uk_mean:.2f}")
    
    # Calculate rolling volatility (standard deviation) on normalized prices
    merged_data['US_Volatility_Normalized'] = merged_data['US_Price_Normalized'].rolling(
        window=window, center=True, min_periods=max(1, window//2)
    ).std()
    
    merged_data['UK_Volatility_Normalized'] = merged_data['UK_Price_Normalized'].rolling(
        window=window, center=True, min_periods=max(1, window//2)
    ).std()
    
    # Calculate the volatility ratio on normalized prices
    merged_data['Volatility_Ratio_Normalized'] = (
        merged_data['US_Volatility_Normalized'] / merged_data['UK_Volatility_Normalized']
    )
    
    # Calculate year-over-year changes on normalized prices
    merged_data['US_YoY_Change_Normalized'] = merged_data['US_Price_Normalized'].pct_change() * 100
    merged_data['UK_YoY_Change_Normalized'] = merged_data['UK_Price_Normalized'].pct_change() * 100
    
    # Calculate rolling correlation on normalized prices
    merged_data['Price_Correlation_Normalized'] = merged_data['US_Price_Normalized'].rolling(
        window=window*2, center=True, min_periods=window
    ).corr(merged_data['UK_Price_Normalized'])
    
    # Add period classifications
    merged_data['Period'] = merged_data['Year'].apply(classify_period)
    
    # Remove rows with infinite or NaN volatility ratios
    merged_data = merged_data.replace([np.inf, -np.inf], np.nan)
    
    # Rename columns to match existing format
    result_df = merged_data.rename(columns={
        'Price_US': 'US_Price',
        'Price_UK': 'UK_Price',
        'US_Volatility_Normalized': 'US_Volatility_Normalized',
        'UK_Volatility_Normalized': 'UK_Volatility_Normalized'
    })
    
    return result_df

def classify_period(year):
    """Classify years into historical periods"""
    if year < 1870:
        return 'Post-Civil War'
    elif year < 1890:
        return 'Gilded Age'
    elif year < 1914:
        return 'Progressive Era'
    elif year < 1929:
        return 'Post-WWI'
    elif year < 1941:
        return 'Great Depression'
    elif year < 1960:
        return 'WWII & Post-War'
    else:
        return 'Modern'

def main():
    """Main function to extend food price volatility ratio"""
    print("Extending US/UK Food Price Volatility Ratio to 1960")
    print("=" * 60)
    
    # Load US wheat data
    us_wheat = load_us_wheat_data()
    if us_wheat.empty:
        print("Failed to load US wheat data")
        return
    
    # Load UK grain data
    uk_grain = load_uk_grain_data()
    if uk_grain.empty:
        print("Failed to load UK grain data")
        return
    
    # Calculate extended volatility ratios
    extended_data = calculate_extended_volatility_ratio(us_wheat, uk_grain, window=2)
    
    if extended_data.empty:
        print("Failed to calculate extended volatility ratios")
        return
    
    # Export the extended data
    output_file = "data/ratios/us_uk_food_price_volatility_ratio_extended.csv"
    
    # Select relevant columns for export
    export_columns = [
        'Year', 'US_Price', 'UK_Price', 'US_Price_Normalized', 'UK_Price_Normalized',
        'US_Volatility_Normalized', 'UK_Volatility_Normalized',
        'Volatility_Ratio_Normalized', 'US_YoY_Change_Normalized', 'UK_YoY_Change_Normalized',
        'Price_Correlation_Normalized', 'Period'
    ]
    
    export_data = extended_data[export_columns].copy()
    export_data.to_csv(output_file, index=False)
    
    print(f"\nExtended food price volatility data exported to: {output_file}")
    print(f"Records exported: {len(export_data)}")
    print(f"Year range: {export_data['Year'].min():.0f}-{export_data['Year'].max():.0f}")
    
    # Show sample of the data
    print(f"\nSample of extended data:")
    print("-" * 50)
    sample_columns = ['Year', 'Volatility_Ratio_Normalized', 'US_Volatility_Normalized', 
                     'UK_Volatility_Normalized', 'Period']
    print(export_data[sample_columns].head(10).to_string(index=False))
    
    # Generate summary statistics
    valid_data = export_data[export_data['Volatility_Ratio_Normalized'].notna()]
    if not valid_data.empty:
        print(f"\nExtended Data Summary:")
        print(f"Valid volatility ratios: {len(valid_data)}")
        print(f"Mean ratio: {valid_data['Volatility_Ratio_Normalized'].mean():.3f}")
        print(f"Median ratio: {valid_data['Volatility_Ratio_Normalized'].median():.3f}")
        print(f"US more volatile: {(valid_data['Volatility_Ratio_Normalized'] > 1).sum()} years")
        print(f"UK more volatile: {(valid_data['Volatility_Ratio_Normalized'] < 1).sum()} years")
    
    return export_data

if __name__ == "__main__":
    main()
