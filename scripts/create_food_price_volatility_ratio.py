#!/usr/bin/env python3
"""
Script to create food price volatility ratio (US/UK) with 2-year rolling window
and generate CSV and plot
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

# Add the dataloaders directory to the path
sys.path.append('dataloaders')

from agprice_dataloader import AgPriceDataLoader
from us_comm_dataloader import USCommDataLoader

warnings.filterwarnings('ignore')

def load_uk_price_data():
    """Load and process UK agricultural price data"""
    print("Loading UK agricultural price data...")
    
    # Try to load from the processed CSV first
    uk_csv_path = Path("data/food/processed_agprice_data.csv")
    if uk_csv_path.exists():
        uk_data = pd.read_csv(uk_csv_path)
        print(f"Loaded UK data from CSV: {len(uk_data)} records")
    else:
        # Load using the dataloader
        uk_loader = AgPriceDataLoader("data/food/agprice_table_raw.json")
        if uk_loader.load_data():
            uk_loader.process_data()
            uk_data = uk_loader.processed_data.copy()
        else:
            print("Failed to load UK data")
            return pd.DataFrame()
    
    # Use average grain price as the main price indicator
    if 'avg_grain_price' in uk_data.columns:
        uk_data = uk_data[['Year', 'avg_grain_price']].dropna()
        uk_data = uk_data.rename(columns={'avg_grain_price': 'UK_Price'})
    elif 'Wheat' in uk_data.columns:
        uk_data = uk_data[['Year', 'Wheat']].dropna()
        uk_data = uk_data.rename(columns={'Wheat': 'UK_Price'})
    else:
        print("No suitable UK price column found")
        return pd.DataFrame()
    
    uk_data['Year'] = uk_data['Year'].astype(int)
    uk_data = uk_data.sort_values('Year')
    
    print(f"UK price data: {uk_data['Year'].min()}-{uk_data['Year'].max()}")
    return uk_data

def load_us_price_data():
    """Load and process US commodity price data"""
    print("Loading US commodity price data...")
    
    # Try to load from the processed CSV first
    us_csv_path = Path("data/price/processed_us_comm_data.csv")
    if us_csv_path.exists():
        us_data = pd.read_csv(us_csv_path)
        print(f"Loaded US data from CSV: {len(us_data)} records")
    else:
        # Load using the dataloader
        us_loader = USCommDataLoader("data/price/us_comm_price_index_long.csv")
        if us_loader.load_data():
            us_loader.process_data()
            us_data = us_loader.processed_data.copy()
        else:
            print("Failed to load US data")
            return pd.DataFrame()
    
    # Convert monthly data to annual averages
    if 'Price_Index' in us_data.columns and 'Year' in us_data.columns:
        us_annual = us_data.groupby('Year')['Price_Index'].mean().reset_index()
        us_annual = us_annual.rename(columns={'Price_Index': 'US_Price'})
    else:
        print("No suitable US price columns found")
        return pd.DataFrame()
    
    us_annual['Year'] = us_annual['Year'].astype(int)
    us_annual = us_annual.sort_values('Year')
    
    print(f"US price data: {us_annual['Year'].min()}-{us_annual['Year'].max()}")
    return us_annual

def calculate_volatility_ratio(us_data, uk_data, window=2):
    """Calculate price volatility ratio with rolling window on normalized prices"""
    print(f"Calculating volatility ratios with {window}-year window on normalized prices...")
    
    # Merge the datasets on common years
    merged_data = pd.merge(us_data, uk_data, on='Year', how='inner')
    
    if merged_data.empty:
        print("No common years found between US and UK data")
        return pd.DataFrame()
    
    print(f"Common years: {merged_data['Year'].min()}-{merged_data['Year'].max()} ({len(merged_data)} years)")
    
    # Sort by year
    merged_data = merged_data.sort_values('Year').reset_index(drop=True)
    
    # Normalize prices to their respective means (this removes scale differences)
    us_mean = merged_data['US_Price'].mean()
    uk_mean = merged_data['UK_Price'].mean()
    
    merged_data['US_Price_Normalized'] = merged_data['US_Price'] / us_mean
    merged_data['UK_Price_Normalized'] = merged_data['UK_Price'] / uk_mean
    
    print(f"US price normalization: mean = {us_mean:.2f}")
    print(f"UK price normalization: mean = {uk_mean:.2f}")
    
    # Calculate rolling volatility (standard deviation) on normalized prices
    merged_data['US_Volatility_Normalized'] = merged_data['US_Price_Normalized'].rolling(
        window=window, center=True, min_periods=max(1, window//2)
    ).std()
    
    merged_data['UK_Volatility_Normalized'] = merged_data['UK_Price_Normalized'].rolling(
        window=window, center=True, min_periods=max(1, window//2)
    ).std()
    
    # Also calculate volatility on original prices for comparison
    merged_data['US_Volatility'] = merged_data['US_Price'].rolling(
        window=window, center=True, min_periods=max(1, window//2)
    ).std()
    
    merged_data['UK_Volatility'] = merged_data['UK_Price'].rolling(
        window=window, center=True, min_periods=max(1, window//2)
    ).std()
    
    # Calculate the volatility ratio on normalized prices (main metric)
    merged_data['Volatility_Ratio_Normalized'] = (
        merged_data['US_Volatility_Normalized'] / merged_data['UK_Volatility_Normalized']
    )
    
    # Calculate the volatility ratio on original prices (for comparison)
    merged_data['Volatility_Ratio'] = merged_data['US_Volatility'] / merged_data['UK_Volatility']
    
    # Calculate price level ratio for comparison
    merged_data['Price_Ratio'] = merged_data['US_Price'] / merged_data['UK_Price']
    merged_data['Price_Ratio_Normalized'] = merged_data['US_Price_Normalized'] / merged_data['UK_Price_Normalized']
    
    # Calculate year-over-year changes on normalized prices
    merged_data['US_YoY_Change_Normalized'] = merged_data['US_Price_Normalized'].pct_change() * 100
    merged_data['UK_YoY_Change_Normalized'] = merged_data['UK_Price_Normalized'].pct_change() * 100
    
    # Calculate year-over-year changes on original prices
    merged_data['US_YoY_Change'] = merged_data['US_Price'].pct_change() * 100
    merged_data['UK_YoY_Change'] = merged_data['UK_Price'].pct_change() * 100
    
    # Calculate rolling correlation on normalized prices
    merged_data['Price_Correlation_Normalized'] = merged_data['US_Price_Normalized'].rolling(
        window=window*2, center=True, min_periods=window
    ).corr(merged_data['UK_Price_Normalized'])
    
    # Calculate rolling correlation on original prices
    merged_data['Price_Correlation'] = merged_data['US_Price'].rolling(
        window=window*2, center=True, min_periods=window
    ).corr(merged_data['UK_Price'])
    
    # Add period classifications
    merged_data['Period'] = merged_data['Year'].apply(classify_period)
    
    # Remove rows with infinite or NaN volatility ratios
    merged_data = merged_data.replace([np.inf, -np.inf], np.nan)
    
    return merged_data

def classify_period(year):
    """Classify years into historical periods"""
    if year < 1750:
        return 'Early Colonial'
    elif year < 1776:
        return 'Pre-Revolution'
    elif year < 1800:
        return 'Revolutionary Era'
    elif year < 1820:
        return 'Early Republic'
    elif year < 1840:
        return 'Antebellum Early'
    elif year < 1860:
        return 'Antebellum Late'
    else:
        return 'Civil War Era'

def create_volatility_plots(data, save_path=None):
    """Create comprehensive volatility analysis plots using normalized data"""
    if data.empty:
        print("No data available for plotting")
        return
    
    # Set up plotting style
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('US/UK Food Price Volatility Analysis (2-Year Rolling Window on Normalized Prices)', 
                 fontsize=16, fontweight='bold')
    
    # 1. Normalized volatility ratio over time (linear scale)
    ax1 = axes[0, 0]
    valid_data = data[data['Volatility_Ratio_Normalized'].notna()]
    
    ax1.plot(valid_data['Year'], valid_data['Volatility_Ratio_Normalized'], 
             linewidth=2, color='purple', alpha=0.8, label='US/UK Volatility Ratio (Normalized)')
    ax1.axhline(y=1, color='black', linestyle='--', alpha=0.5, label='Equal Volatility')
    
    ax1.set_title('Normalized Food Price Volatility Ratio (US/UK)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Volatility Ratio')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Log scale volatility ratio (NEW)
    ax2 = axes[0, 1]
    # Filter out values <= 0 for log scale
    log_data = valid_data[valid_data['Volatility_Ratio_Normalized'] > 0]
    
    ax2.semilogy(log_data['Year'], log_data['Volatility_Ratio_Normalized'], 
                 linewidth=2, color='purple', alpha=0.8, label='US/UK Volatility Ratio (Log Scale)')
    ax2.axhline(y=1, color='black', linestyle='--', alpha=0.5, label='Equal Volatility')
    
    ax2.set_title('Log Scale: Normalized Food Price Volatility Ratio (US/UK)')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Volatility Ratio (Log Scale)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Individual normalized volatilities
    ax3 = axes[1, 0]
    us_vol_data = data[data['US_Volatility_Normalized'].notna()]
    uk_vol_data = data[data['UK_Volatility_Normalized'].notna()]
    
    ax3.plot(us_vol_data['Year'], us_vol_data['US_Volatility_Normalized'], 
             linewidth=2, color='blue', alpha=0.8, label='US Volatility (Normalized)')
    ax3.plot(uk_vol_data['Year'], uk_vol_data['UK_Volatility_Normalized'], 
             linewidth=2, color='red', alpha=0.8, label='UK Volatility (Normalized)')
    
    ax3.set_title('Individual Normalized Food Price Volatilities')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Normalized Price Volatility (Std Dev)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Period-wise normalized volatility comparison
    ax4 = axes[1, 1]
    
    period_stats = data.groupby('Period').agg({
        'Volatility_Ratio_Normalized': 'mean',
        'US_Volatility_Normalized': 'mean',
        'UK_Volatility_Normalized': 'mean'
    }).dropna()
    
    if not period_stats.empty:
        x_pos = np.arange(len(period_stats))
        width = 0.25
        
        ax4.bar(x_pos - width, period_stats['US_Volatility_Normalized'], width, 
                label='US Volatility (Norm)', alpha=0.7, color='blue')
        ax4.bar(x_pos, period_stats['UK_Volatility_Normalized'], width, 
                label='UK Volatility (Norm)', alpha=0.7, color='red')
        ax4.bar(x_pos + width, period_stats['Volatility_Ratio_Normalized'], width, 
                label='US/UK Ratio (Norm)', alpha=0.7, color='purple')
        
        ax4.set_title('Average Normalized Volatility by Historical Period')
        ax4.set_xlabel('Historical Period')
        ax4.set_ylabel('Normalized Volatility Measure')
        ax4.set_xticks(x_pos)
        ax4.set_xticklabels(period_stats.index, rotation=45, ha='right')
        ax4.legend()
        ax4.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.show()

def generate_summary_statistics(data):
    """Generate summary statistics for the volatility analysis using normalized data"""
    if data.empty:
        print("No data available for summary statistics")
        return
    
    print("\n" + "="*70)
    print("NORMALIZED PRICE VOLATILITY RATIO ANALYSIS SUMMARY")
    print("="*70)
    
    # Basic statistics
    valid_data_norm = data[data['Volatility_Ratio_Normalized'].notna()]
    valid_data_orig = data[data['Volatility_Ratio'].notna()]
    
    print(f"\nBasic Statistics:")
    print(f"Total observations: {len(data)}")
    print(f"Valid normalized volatility ratios: {len(valid_data_norm)}")
    print(f"Year range: {data['Year'].min()}-{data['Year'].max()}")
    
    if not valid_data_norm.empty:
        print(f"\nNormalized Volatility Ratio Statistics:")
        print(f"Mean: {valid_data_norm['Volatility_Ratio_Normalized'].mean():.3f}")
        print(f"Median: {valid_data_norm['Volatility_Ratio_Normalized'].median():.3f}")
        print(f"Std Dev: {valid_data_norm['Volatility_Ratio_Normalized'].std():.3f}")
        print(f"Min: {valid_data_norm['Volatility_Ratio_Normalized'].min():.3f}")
        print(f"Max: {valid_data_norm['Volatility_Ratio_Normalized'].max():.3f}")
        
        # Count periods where US was more volatile than UK (normalized)
        us_more_volatile_norm = (valid_data_norm['Volatility_Ratio_Normalized'] > 1).sum()
        uk_more_volatile_norm = (valid_data_norm['Volatility_Ratio_Normalized'] < 1).sum()
        
        print(f"\nNormalized Volatility Comparison:")
        print(f"Years US more volatile: {us_more_volatile_norm} ({us_more_volatile_norm/len(valid_data_norm)*100:.1f}%)")
        print(f"Years UK more volatile: {uk_more_volatile_norm} ({uk_more_volatile_norm/len(valid_data_norm)*100:.1f}%)")
    
    # Compare with original (non-normalized) results
    if not valid_data_orig.empty:
        print(f"\nComparison with Original (Non-Normalized) Results:")
        print(f"Original ratio mean: {valid_data_orig['Volatility_Ratio'].mean():.3f}")
        print(f"Original ratio median: {valid_data_orig['Volatility_Ratio'].median():.3f}")
        
        us_more_volatile_orig = (valid_data_orig['Volatility_Ratio'] > 1).sum()
        print(f"Original: Years US more volatile: {us_more_volatile_orig} ({us_more_volatile_orig/len(valid_data_orig)*100:.1f}%)")
    
    # Period-wise analysis using normalized data
    print(f"\nPeriod-wise Analysis (Normalized Data):")
    print("-" * 60)
    
    period_stats = data.groupby('Period').agg({
        'Volatility_Ratio_Normalized': ['count', 'mean', 'std'],
        'US_Volatility_Normalized': 'mean',
        'UK_Volatility_Normalized': 'mean',
        'Price_Correlation_Normalized': 'mean'
    }).round(3)
    
    print(period_stats)

def main():
    """Main function to create volatility ratio analysis"""
    print("Price Volatility Ratio Analysis: US vs UK")
    print("=" * 50)
    
    # Load data
    us_data = load_us_price_data()
    uk_data = load_uk_price_data()
    
    if us_data.empty or uk_data.empty:
        print("Failed to load required data")
        return
    
    # Calculate volatility ratios
    volatility_data = calculate_volatility_ratio(us_data, uk_data, window=2)
    
    if volatility_data.empty:
        print("Failed to calculate volatility ratios")
        return
    
    # Generate summary statistics
    generate_summary_statistics(volatility_data)
    
    # Create plots
    create_volatility_plots(volatility_data, save_path="plots/food_price_volatility_ratio_analysis.png")
    
    # Export to CSV
    output_file = "data/ratios/us_uk_food_price_volatility_ratio.csv"
    
    # Ensure the ratios directory exists
    Path("data/ratios").mkdir(exist_ok=True)
    
    # Select relevant columns for export (including normalized data)
    export_columns = [
        'Year', 'US_Price', 'UK_Price', 'US_Price_Normalized', 'UK_Price_Normalized',
        'US_Volatility', 'UK_Volatility', 'US_Volatility_Normalized', 'UK_Volatility_Normalized',
        'Volatility_Ratio', 'Volatility_Ratio_Normalized', 'Price_Ratio', 'Price_Ratio_Normalized',
        'US_YoY_Change', 'UK_YoY_Change', 'US_YoY_Change_Normalized', 'UK_YoY_Change_Normalized',
        'Price_Correlation', 'Price_Correlation_Normalized', 'Period'
    ]
    
    export_data = volatility_data[export_columns].copy()
    export_data.to_csv(output_file, index=False)
    
    print(f"\nNormalized volatility ratio data exported to: {output_file}")
    print(f"Records exported: {len(export_data)}")
    
    # Show sample of the normalized data
    print(f"\nSample of exported data (showing key normalized metrics):")
    print("-" * 70)
    sample_columns = ['Year', 'Volatility_Ratio_Normalized', 'US_Volatility_Normalized', 
                     'UK_Volatility_Normalized', 'Price_Correlation_Normalized', 'Period']
    print(export_data[sample_columns].head(10).to_string(index=False))
    
    return export_data

if __name__ == "__main__":
    main()
