#!/usr/bin/env python3
"""
Script to combine old and new food price volatility data to get the full range
"""

import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add the dataloaders directory to the path
sys.path.append('dataloaders')

from agprice_dataloader import AgPriceDataLoader
from us_comm_dataloader import USCommDataLoader

def load_old_us_data():
    """Load old US commodity price data (1732-1861)"""
    print("Loading old US commodity price data...")
    
    try:
        # Try to load from processed CSV first
        us_csv_path = Path("data/price/processed_us_comm_data.csv")
        if us_csv_path.exists():
            us_data = pd.read_csv(us_csv_path)
            print(f"Loaded old US data from CSV: {len(us_data)} records")
        else:
            # Load using the dataloader
            us_loader = USCommDataLoader("data/price/us_comm_price_index_raw.json")
            if us_loader.load_data():
                us_loader.process_data()
                us_data = us_loader.processed_data.copy()
            else:
                print("Failed to load old US data")
                return pd.DataFrame()
        
        # Use price index as the main price indicator
        if 'Price_Index' in us_data.columns:
            us_data = us_data[['Year', 'Price_Index']].dropna()
            us_data = us_data.rename(columns={'Price_Index': 'Price'})
        elif 'avg_price' in us_data.columns:
            us_data = us_data[['Year', 'avg_price']].dropna()
            us_data = us_data.rename(columns={'avg_price': 'Price'})
        elif 'Average_Price' in us_data.columns:
            us_data = us_data[['Year', 'Average_Price']].dropna()
            us_data = us_data.rename(columns={'Average_Price': 'Price'})
        else:
            print("Available columns:", us_data.columns.tolist())
            print("No suitable US price column found in old data")
            return pd.DataFrame()
        
        us_data['Year'] = us_data['Year'].astype(int)
        us_data = us_data.sort_values('Year')
        
        # Filter to the old data range
        us_data = us_data[us_data['Year'] <= 1861]
        
        print(f"Old US data: {us_data['Year'].min()}-{us_data['Year'].max()} ({len(us_data)} records)")
        return us_data
        
    except Exception as e:
        print(f"Error loading old US data: {e}")
        return pd.DataFrame()

def load_old_uk_data():
    """Load old UK agricultural price data (1209-1914)"""
    print("Loading old UK agricultural price data...")
    
    try:
        # Load using the dataloader
        uk_loader = AgPriceDataLoader("data/food/agprice_table_raw.json")
        if uk_loader.load_data():
            uk_loader.process_data()
            uk_data = uk_loader.processed_data.copy()
        else:
            print("Failed to load old UK data")
            return pd.DataFrame()
        
        # Use average grain price as the main price indicator
        if 'avg_grain_price' in uk_data.columns:
            uk_data = uk_data[['Year', 'avg_grain_price']].dropna()
            uk_data = uk_data.rename(columns={'avg_grain_price': 'Price'})
        elif 'Wheat' in uk_data.columns:
            uk_data = uk_data[['Year', 'Wheat']].dropna()
            uk_data = uk_data.rename(columns={'Wheat': 'Price'})
        else:
            print("No suitable UK price column found in old data")
            return pd.DataFrame()
        
        uk_data['Year'] = uk_data['Year'].astype(int)
        uk_data = uk_data.sort_values('Year')
        
        print(f"Old UK data: {uk_data['Year'].min()}-{uk_data['Year'].max()} ({len(uk_data)} records)")
        return uk_data
        
    except Exception as e:
        print(f"Error loading old UK data: {e}")
        return pd.DataFrame()

def load_new_us_data():
    """Load new US wheat price data from Excel file (1866-1960)"""
    print("Loading new US wheat price data from Excel file...")
    
    try:
        # Read the Table01 sheet which contains wheat prices
        df = pd.read_excel('data/food/Wheat Data-All Years (2).xlsx', sheet_name='Table01')
        
        # Clean up the data - skip header rows and get the relevant columns
        df_clean = df.iloc[1:].copy()  # Skip the header row
        
        # Extract year and price columns
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
        
        print(f"New US wheat data: {us_wheat['Year'].min():.0f}-{us_wheat['Year'].max():.0f} ({len(us_wheat)} records)")
        return us_wheat
        
    except Exception as e:
        print(f"Error loading new US wheat data: {e}")
        return pd.DataFrame()

def load_new_uk_data():
    """Load new UK grain price data from chicago_uk_grain_prices.csv"""
    print("Loading new UK grain price data...")
    
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
        
        print(f"New UK grain data: {uk_annual['Year'].min()}-{uk_annual['Year'].max()} ({len(uk_annual)} records)")
        return uk_annual
        
    except Exception as e:
        print(f"Error loading new UK grain data: {e}")
        return pd.DataFrame()

def combine_us_data(old_us, new_us):
    """Combine old and new US data"""
    print("Combining US data...")
    
    if old_us.empty and new_us.empty:
        return pd.DataFrame()
    elif old_us.empty:
        return new_us
    elif new_us.empty:
        return old_us
    
    # Find overlap years
    old_max = old_us['Year'].max()
    new_min = new_us['Year'].min()
    
    print(f"Old US data ends: {old_max}, New US data starts: {new_min}")
    
    # If there's a gap, keep both datasets
    # If there's overlap, prefer the newer data for overlapping years
    if new_min <= old_max:
        # Remove overlapping years from old data
        old_us_filtered = old_us[old_us['Year'] < new_min].copy()
        combined = pd.concat([old_us_filtered, new_us], ignore_index=True)
        print(f"Removed {len(old_us) - len(old_us_filtered)} overlapping years from old US data")
    else:
        # No overlap, just concatenate
        combined = pd.concat([old_us, new_us], ignore_index=True)
    
    combined = combined.sort_values('Year').reset_index(drop=True)
    print(f"Combined US data: {combined['Year'].min()}-{combined['Year'].max()} ({len(combined)} records)")
    
    return combined

def combine_uk_data(old_uk, new_uk):
    """Combine old and new UK data"""
    print("Combining UK data...")
    
    if old_uk.empty and new_uk.empty:
        return pd.DataFrame()
    elif old_uk.empty:
        return new_uk
    elif new_uk.empty:
        return old_uk
    
    # Find overlap years
    old_max = old_uk['Year'].max()
    new_min = new_uk['Year'].min()
    
    print(f"Old UK data ends: {old_max}, New UK data starts: {new_min}")
    
    # If there's overlap, prefer the newer data for overlapping years
    if new_min <= old_max:
        # Remove overlapping years from old data
        old_uk_filtered = old_uk[old_uk['Year'] < new_min].copy()
        combined = pd.concat([old_uk_filtered, new_uk], ignore_index=True)
        print(f"Removed {len(old_uk) - len(old_uk_filtered)} overlapping years from old UK data")
    else:
        # No overlap, just concatenate
        combined = pd.concat([old_uk, new_uk], ignore_index=True)
    
    combined = combined.sort_values('Year').reset_index(drop=True)
    print(f"Combined UK data: {combined['Year'].min()}-{combined['Year'].max()} ({len(combined)} records)")
    
    return combined

def calculate_combined_volatility_ratio(us_data, uk_data, window=2):
    """Calculate volatility ratio with rolling window on normalized prices"""
    print(f"Calculating combined volatility ratios with {window}-year window...")
    
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
        'Price_UK': 'UK_Price'
    })
    
    return result_df

def classify_period(year):
    """Classify years into historical periods"""
    if year < 1750:
        return 'Early Colonial'
    elif year < 1776:
        return 'Pre-Revolution'
    elif year < 1800:
        return 'Revolutionary Era'
    elif year < 1830:
        return 'Early Republic'
    elif year < 1850:
        return 'Antebellum Early'
    elif year < 1861:
        return 'Antebellum Late'
    elif year < 1870:
        return 'Civil War Era'
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
    """Main function to combine food price volatility data"""
    print("Combining US/UK Food Price Volatility Data for Full Range")
    print("=" * 65)
    
    # Load old data (1732-1861)
    old_us = load_old_us_data()
    old_uk = load_old_uk_data()
    
    # Load new data (1866-1955)
    new_us = load_new_us_data()
    new_uk = load_new_uk_data()
    
    # Combine datasets
    combined_us = combine_us_data(old_us, new_us)
    combined_uk = combine_uk_data(old_uk, new_uk)
    
    if combined_us.empty or combined_uk.empty:
        print("Failed to combine data")
        return
    
    # Calculate combined volatility ratios
    combined_data = calculate_combined_volatility_ratio(combined_us, combined_uk, window=2)
    
    if combined_data.empty:
        print("Failed to calculate combined volatility ratios")
        return
    
    # Export the combined data
    output_file = "data/ratios/us_uk_food_price_volatility_ratio.csv"
    
    # Select relevant columns for export
    export_columns = [
        'Year', 'US_Price', 'UK_Price', 'US_Price_Normalized', 'UK_Price_Normalized',
        'US_Volatility_Normalized', 'UK_Volatility_Normalized',
        'Volatility_Ratio_Normalized', 'US_YoY_Change_Normalized', 'UK_YoY_Change_Normalized',
        'Price_Correlation_Normalized', 'Period'
    ]
    
    export_data = combined_data[export_columns].copy()
    export_data.to_csv(output_file, index=False)
    
    print(f"\nCombined food price volatility data exported to: {output_file}")
    print(f"Records exported: {len(export_data)}")
    print(f"Year range: {export_data['Year'].min():.0f}-{export_data['Year'].max():.0f}")
    
    # Show sample of the data
    print(f"\nSample of combined data:")
    print("-" * 50)
    sample_columns = ['Year', 'Volatility_Ratio_Normalized', 'US_Volatility_Normalized', 
                     'UK_Volatility_Normalized', 'Period']
    print(export_data[sample_columns].head(10).to_string(index=False))
    print("...")
    print(export_data[sample_columns].tail(10).to_string(index=False))
    
    # Generate summary statistics
    valid_data = export_data[export_data['Volatility_Ratio_Normalized'].notna()]
    if not valid_data.empty:
        print(f"\nCombined Data Summary:")
        print(f"Valid volatility ratios: {len(valid_data)}")
        print(f"Mean ratio: {valid_data['Volatility_Ratio_Normalized'].mean():.3f}")
        print(f"Median ratio: {valid_data['Volatility_Ratio_Normalized'].median():.3f}")
        print(f"US more volatile: {(valid_data['Volatility_Ratio_Normalized'] > 1).sum()} years")
        print(f"UK more volatile: {(valid_data['Volatility_Ratio_Normalized'] < 1).sum()} years")
        
        # Period-wise summary
        print(f"\nPeriod-wise Summary:")
        period_summary = valid_data.groupby('Period').agg({
            'Volatility_Ratio_Normalized': ['count', 'mean', 'median']
        }).round(3)
        print(period_summary)
    
    return export_data

if __name__ == "__main__":
    main()
