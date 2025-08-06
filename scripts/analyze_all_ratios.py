#!/usr/bin/env python3
"""
Script to analyze all US/UK ratios from the data/ratios folder
Creates a joint dataframe and plots each ratio with log scale
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

def load_ratio_data():
    """Load all ratio CSV files from data/ratios folder"""
    ratios_dir = Path("data/ratios")
    ratio_files = list(ratios_dir.glob("*.csv"))
    
    # Filter out generated files to avoid duplicates
    excluded_files = ['all_ratios_combined_long.csv', 'all_ratios_combined_wide.csv', 'all_ratios_summary_statistics.csv']
    ratio_files = [f for f in ratio_files if f.name not in excluded_files]
    
    print(f"Found {len(ratio_files)} ratio files:")
    for file in ratio_files:
        print(f"  - {file.name}")
    
    all_ratios = {}
    
    for file_path in ratio_files:
        try:
            df = pd.read_csv(file_path)
            
            # Determine the file type and extract relevant columns
            file_name = file_path.stem
            
            if "gdp_ratio" in file_name:
                ratio_col = "us_to_uk_gdp_ratio"
                year_col = "year"
                label = "GDP Ratio"
            elif "education_ratio" in file_name:
                ratio_col = "us_to_uk_ratio"
                year_col = "year"
                label = "Education Ratio"
            elif "child_mortality_ratio" in file_name:
                # Skip child mortality ratio as requested
                print(f"  - Skipping {file_name} (child mortality ratio excluded)")
                continue
            elif "military_ratio" in file_name:
                # Find ratio column
                ratio_cols = [col for col in df.columns if "ratio" in col.lower()]
                if ratio_cols:
                    ratio_col = ratio_cols[0]
                else:
                    ratio_col = df.columns[1]  # Assume second column is ratio
                year_col = df.columns[0]  # Assume first column is year
                label = "Military Power Ratio"
            elif "food_price_volatility" in file_name or "price_volatility" in file_name:
                # Look for normalized volatility ratio
                if "Volatility_Ratio_Normalized" in df.columns:
                    ratio_col = "Volatility_Ratio_Normalized"
                elif "Volatility_Ratio" in df.columns:
                    ratio_col = "Volatility_Ratio"
                else:
                    ratio_col = df.columns[1]
                year_col = "Year"
                label = "Food Price Volatility Ratio"
            elif "exchange_rate" in file_name:
                # Exchange rate volatility
                if "volatility_ratio" in df.columns:
                    ratio_col = "volatility_ratio"
                else:
                    ratio_col = df.columns[1]
                year_col = df.columns[0]
                label = "Exchange Rate Volatility"
            else:
                # Generic handling
                ratio_col = df.columns[1]  # Assume second column is ratio
                year_col = df.columns[0]   # Assume first column is year
                label = file_name.replace("us_uk_", "").replace("_", " ").title()
            
            # Clean and prepare data
            if year_col in df.columns and ratio_col in df.columns:
                clean_df = df[[year_col, ratio_col]].copy()
                clean_df = clean_df.dropna()
                clean_df[year_col] = pd.to_numeric(clean_df[year_col], errors='coerce')
                clean_df[ratio_col] = pd.to_numeric(clean_df[ratio_col], errors='coerce')
                clean_df = clean_df.dropna()
                
                if len(clean_df) > 0:
                    clean_df = clean_df.rename(columns={year_col: 'Year', ratio_col: 'Ratio'})
                    clean_df['Category'] = label
                    all_ratios[label] = clean_df
                    print(f"  ✓ Loaded {label}: {len(clean_df)} records ({clean_df['Year'].min():.0f}-{clean_df['Year'].max():.0f})")
                else:
                    print(f"  ✗ No valid data in {file_name}")
            else:
                print(f"  ✗ Could not find appropriate columns in {file_name}")
                print(f"    Available columns: {list(df.columns)}")
                
        except Exception as e:
            print(f"  ✗ Error loading {file_path.name}: {e}")
    
    return all_ratios

def create_joint_dataframe(all_ratios):
    """Combine all ratio data into a single dataframe"""
    if not all_ratios:
        return pd.DataFrame()
    
    # Combine all dataframes
    combined_df = pd.concat(all_ratios.values(), ignore_index=True)
    
    print(f"\nJoint dataframe created:")
    print(f"Total records: {len(combined_df)}")
    print(f"Categories: {combined_df['Category'].unique()}")
    print(f"Year range: {combined_df['Year'].min():.0f}-{combined_df['Year'].max():.0f}")
    
    return combined_df

def create_comprehensive_plots(combined_df, all_ratios):
    """Create comprehensive plots of all ratios filtered to 1825-1960"""
    if combined_df.empty:
        print("No data to plot")
        return
    
    # Filter data to 1825-1960 range
    start_year = 1825
    end_year = 1960
    
    # Set up the plotting style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Calculate number of subplots needed
    n_categories = len(all_ratios)
    n_cols = 3
    n_rows = (n_categories + n_cols - 1) // n_cols
    
    # Create individual plots for each ratio
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 6*n_rows))
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    
    fig.suptitle(f'US/UK Ratios Analysis ({start_year}-{end_year}) - Individual Log Plots', fontsize=16, fontweight='bold')
    
    for i, (category, data) in enumerate(all_ratios.items()):
        row = i // n_cols
        col = i % n_cols
        ax = axes[row, col]
        
        # Filter data to specified year range and positive values for log scale
        filtered_data = data[(data['Year'] >= start_year) & (data['Year'] <= end_year) & (data['Ratio'] > 0)].copy()
        
        if len(filtered_data) > 0:
            # Plot on log scale
            ax.semilogy(filtered_data['Year'], filtered_data['Ratio'], 
                       linewidth=2, marker='o', markersize=3, alpha=0.8, label=category)
            
            # Add horizontal line at y=1 (equal ratio)
            ax.axhline(y=1, color='black', linestyle='--', alpha=0.5, label='Equal (US=UK)')
            
            ax.set_title(f'{category} (Log Scale)')
            ax.set_xlabel('Year')
            ax.set_ylabel('Ratio (Log Scale)')
            ax.set_xlim(start_year, end_year)
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            # Add some statistics for filtered data
            mean_ratio = filtered_data['Ratio'].mean()
            median_ratio = filtered_data['Ratio'].median()
            ax.text(0.02, 0.98, f'Mean: {mean_ratio:.2f}\nMedian: {median_ratio:.2f}\nN: {len(filtered_data)}', 
                   transform=ax.transAxes, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        else:
            ax.text(0.5, 0.5, f'No data for {category}\nin {start_year}-{end_year}', 
                   transform=ax.transAxes, ha='center', va='center')
            ax.set_title(f'{category} (No Data)')
            ax.set_xlim(start_year, end_year)
    
    # Hide empty subplots
    for i in range(n_categories, n_rows * n_cols):
        row = i // n_cols
        col = i % n_cols
        axes[row, col].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(f'plots/all_ratios_individual_log_plots_{start_year}_{end_year}.png', dpi=300, bbox_inches='tight')
    print(f"Individual log plots saved to 'plots/all_ratios_individual_log_plots_{start_year}_{end_year}.png'")
    plt.show()

def generate_summary_statistics(combined_df, all_ratios):
    """Generate comprehensive summary statistics"""
    if combined_df.empty:
        print("No data for summary statistics")
        return
    
    print("\n" + "="*80)
    print("COMPREHENSIVE US/UK RATIOS ANALYSIS SUMMARY")
    print("="*80)
    
    print(f"\nOverall Statistics:")
    print(f"Total records: {len(combined_df)}")
    print(f"Categories analyzed: {len(all_ratios)}")
    print(f"Year range: {combined_df['Year'].min():.0f}-{combined_df['Year'].max():.0f}")
    
    print(f"\nCategory-wise Statistics:")
    print("-" * 60)
    
    summary_stats = []
    
    for category, data in all_ratios.items():
        positive_data = data[data['Ratio'] > 0]
        
        if len(positive_data) > 0:
            stats = {
                'Category': category,
                'Records': len(data),
                'Positive_Records': len(positive_data),
                'Year_Range': f"{data['Year'].min():.0f}-{data['Year'].max():.0f}",
                'Mean_Ratio': positive_data['Ratio'].mean(),
                'Median_Ratio': positive_data['Ratio'].median(),
                'Std_Ratio': positive_data['Ratio'].std(),
                'Min_Ratio': positive_data['Ratio'].min(),
                'Max_Ratio': positive_data['Ratio'].max(),
                'US_Advantage_Years': (positive_data['Ratio'] > 1).sum(),
                'UK_Advantage_Years': (positive_data['Ratio'] < 1).sum(),
                'US_Advantage_Pct': (positive_data['Ratio'] > 1).mean() * 100
            }
            summary_stats.append(stats)
            
            print(f"\n{category}:")
            print(f"  Records: {stats['Records']} ({stats['Year_Range']})")
            print(f"  Mean ratio: {stats['Mean_Ratio']:.3f}")
            print(f"  Median ratio: {stats['Median_Ratio']:.3f}")
            print(f"  Range: {stats['Min_Ratio']:.3f} - {stats['Max_Ratio']:.3f}")
            print(f"  US advantage: {stats['US_Advantage_Years']} years ({stats['US_Advantage_Pct']:.1f}%)")
            print(f"  UK advantage: {stats['UK_Advantage_Years']} years ({100-stats['US_Advantage_Pct']:.1f}%)")
    
    # Create summary dataframe
    summary_df = pd.DataFrame(summary_stats)
    
    # Export summary statistics
    summary_df.to_csv('data/ratios/all_ratios_summary_statistics.csv', index=False)
    print(f"\nSummary statistics exported to 'data/ratios/all_ratios_summary_statistics.csv'")
    
    return summary_df

def export_joint_data(combined_df):
    """Export the joint dataframe"""
    if not combined_df.empty:
        # Create a pivot table for easier analysis
        pivot_df = combined_df.pivot_table(index='Year', columns='Category', values='Ratio', aggfunc='first')
        
        # Export both formats
        combined_df.to_csv('data/ratios/all_ratios_combined_long.csv', index=False)
        pivot_df.to_csv('data/ratios/all_ratios_combined_wide.csv')
        
        print(f"\nJoint data exported:")
        print(f"  - Long format: data/ratios/all_ratios_combined_long.csv ({len(combined_df)} records)")
        print(f"  - Wide format: data/ratios/all_ratios_combined_wide.csv ({len(pivot_df)} years)")
        
        return pivot_df
    
    return pd.DataFrame()

def main():
    """Main function to analyze all ratios"""
    print("Comprehensive US/UK Ratios Analysis")
    print("=" * 50)
    
    # Ensure plots directory exists
    Path("plots").mkdir(exist_ok=True)
    
    # Load all ratio data
    all_ratios = load_ratio_data()
    
    if not all_ratios:
        print("No ratio data found!")
        return
    
    # Create joint dataframe
    combined_df = create_joint_dataframe(all_ratios)
    
    # Generate summary statistics
    summary_df = generate_summary_statistics(combined_df, all_ratios)
    
    # Create comprehensive plots
    create_comprehensive_plots(combined_df, all_ratios)
    
    # Export joint data
    pivot_df = export_joint_data(combined_df)
    
    print(f"\n" + "="*50)
    print("ANALYSIS COMPLETE")
    print("="*50)
    print("Generated files:")
    print("  - plots/all_ratios_individual_log_plots.png")
    print("  - plots/all_ratios_combined_log_plot.png")
    print("  - data/ratios/all_ratios_combined_long.csv")
    print("  - data/ratios/all_ratios_combined_wide.csv")
    print("  - data/ratios/all_ratios_summary_statistics.csv")
    
    return combined_df, all_ratios, summary_df

if __name__ == "__main__":
    main()
