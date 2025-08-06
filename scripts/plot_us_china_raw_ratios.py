#!/usr/bin/env python3
"""
Plot raw China/US ratios for US-China dataset (1989-2024)
Shows actual ratio values without log transformation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

def load_us_china_data():
    """Load US-China datasets"""
    print("Loading US-China datasets...")
    
    # Load main US-China dataset
    main_data = pd.read_csv('data/archimedes_dataset_us_china_1989_2024.csv', comment='#')
    print(f"Loaded main dataset: {len(main_data)} records (1989-2024)")
    
    # Load education data
    education_data = pd.read_csv('data/ratios/US_China/education_enrollment_ratio.csv')
    print(f"Loaded education data: {len(education_data)} records ({education_data['year'].min()}-{education_data['year'].max()})")
    
    return main_data, education_data

def prepare_raw_ratios(main_data, education_data):
    """Prepare raw ratios for plotting"""
    print("\nPreparing raw ratios...")
    
    # Merge datasets on year
    merged_data = pd.merge(main_data, education_data, on='year', how='left')
    merged_data = merged_data.rename(columns={'ratio': 'education_ratio'})
    
    # Create raw ratios (China/US ratios)
    plot_data = pd.DataFrame({
        'year': merged_data['year'],
        'child_mortality_volatility_ratio': merged_data['child_mortality_volatility_ratio'],
        'food_volatility_ratio': merged_data['food_volatility_ratio'],
        'gdp_volatility_ratio': merged_data['gdp_volatility_ratio'],
        'education_ratio': merged_data['education_ratio'],
        'exchange_rate_volatility': merged_data['exchange_rate_volatility']  # Not a ratio, use as is
    })
    
    print(f"Prepared data: {len(plot_data)} records")
    print("Available data by variable:")
    for col in plot_data.columns:
        if col != 'year':
            available = plot_data[col].notna().sum()
            print(f"  {col}: {available} years")
    
    return plot_data

def create_individual_raw_plots(plot_data):
    """Create individual raw ratio plots"""
    print("\nCreating individual raw ratio plots...")
    
    # Set up the plot style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('US-China Raw Ratios: Individual Variable Analysis (1989-2024)', 
                 fontsize=16, fontweight='bold')
    
    # Define variables to plot
    variables = [
        {
            'name': 'child_mortality_volatility_ratio',
            'title': 'Child Mortality Volatility Ratio',
            'description': 'China/US Child Mortality Volatility',
            'color': 'blue'
        },
        {
            'name': 'food_volatility_ratio', 
            'title': 'Food Price Volatility Ratio',
            'description': 'China/US Food Price Volatility',
            'color': 'green'
        },
        {
            'name': 'gdp_volatility_ratio',
            'title': 'GDP Volatility Ratio', 
            'description': 'China/US GDP Volatility',
            'color': 'red'
        },
        {
            'name': 'education_ratio',
            'title': 'Education Enrollment Ratio',
            'description': 'China/US Education Enrollment',
            'color': 'purple'
        },
        {
            'name': 'exchange_rate_volatility',
            'title': 'Exchange Rate Volatility',
            'description': 'USD/CNY Exchange Rate Volatility',
            'color': 'orange'
        }
    ]
    
    # Plot each variable
    for i, var in enumerate(variables):
        if i < 5:  # We have 5 variables
            row = i // 3
            col = i % 3
            ax = axes[row, col]
            
            # Get data for this variable
            data = plot_data[['year', var['name']]].dropna()
            
            if len(data) > 0:
                # Plot the time series
                ax.plot(data['year'], data[var['name']], 
                       color=var['color'], linewidth=2, marker='o', markersize=4, alpha=0.8)
                
                # Add horizontal line at 1 (equal ratio) for ratio variables
                if 'ratio' in var['name'] and var['name'] != 'exchange_rate_volatility':
                    ax.axhline(y=1, color='black', linestyle='--', alpha=0.5, linewidth=1, label='Equal (1:1)')
                
                # Formatting
                ax.set_title(var['title'], fontsize=12, fontweight='bold')
                ax.set_xlabel('Year', fontsize=10)
                if 'ratio' in var['name'] and var['name'] != 'exchange_rate_volatility':
                    ax.set_ylabel('Ratio (China/US)', fontsize=10)
                else:
                    ax.set_ylabel('Volatility', fontsize=10)
                ax.grid(True, alpha=0.3)
                
                # Add text box with description
                ax.text(0.02, 0.98, var['description'], 
                       transform=ax.transAxes, fontsize=9,
                       verticalalignment='top', 
                       bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
                
                # Add interpretation text
                if 'ratio' in var['name'] and var['name'] != 'exchange_rate_volatility':
                    interpretation = "Above 1: China > US\nBelow 1: US > China"
                else:
                    interpretation = "Higher values:\nMore volatility"
                
                ax.text(0.98, 0.02, interpretation,
                       transform=ax.transAxes, fontsize=8,
                       verticalalignment='bottom', horizontalalignment='right',
                       bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))
                
                # Set reasonable y-limits
                y_data = data[var['name']]
                if len(y_data) > 0:
                    y_min, y_max = y_data.min(), y_data.max()
                    
                    # For ratios, ensure we can see the 1:1 line
                    if 'ratio' in var['name'] and var['name'] != 'exchange_rate_volatility':
                        y_min = min(y_min, 0.5)
                        y_max = max(y_max, 2.0)
                    
                    y_range = y_max - y_min
                    y_margin = y_range * 0.1
                    ax.set_ylim(max(0, y_min - y_margin), y_max + y_margin)
                
                # Add legend if we have the 1:1 line
                if 'ratio' in var['name'] and var['name'] != 'exchange_rate_volatility':
                    ax.legend(loc='upper right', fontsize=8)
                
            else:
                ax.text(0.5, 0.5, 'No Data Available', 
                       transform=ax.transAxes, ha='center', va='center',
                       fontsize=14, color='gray')
                ax.set_title(var['title'], fontsize=12, fontweight='bold')
    
    # Hide the last subplot (we only have 5 variables)
    axes[1, 2].set_visible(False)
    
    # Add overall description
    fig.text(0.02, 0.02, 
             'Note: Ratios show China/US comparisons. Values above 1 indicate China > US, values below 1 indicate US > China.\n' +
             'Exchange rate volatility is not a ratio but shows USD/CNY volatility over time.',
             fontsize=10, style='italic')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.93, bottom=0.1)
    
    # Save the plot
    output_file = 'plots/us_china_raw_ratios_1989_2024.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Plot saved to '{output_file}'")
    plt.show()

def create_summary_statistics(plot_data):
    """Create summary statistics for the raw ratios"""
    print("\nCreating summary statistics...")
    
    summary_stats = []
    
    for col in plot_data.columns:
        if col != 'year':
            data = plot_data[col].dropna()
            if len(data) > 0:
                stats = {
                    'variable': col,
                    'count': len(data),
                    'mean': data.mean(),
                    'median': data.median(),
                    'std': data.std(),
                    'min': data.min(),
                    'max': data.max(),
                    'first_year': plot_data[plot_data[col].notna()]['year'].min(),
                    'last_year': plot_data[plot_data[col].notna()]['year'].max()
                }
                summary_stats.append(stats)
    
    summary_df = pd.DataFrame(summary_stats)
    
    # Save summary statistics
    output_file = 'data/us_china_raw_ratios_summary.csv'
    summary_df.to_csv(output_file, index=False)
    print(f"Summary statistics saved to '{output_file}'")
    
    # Print summary
    print("\nSummary Statistics:")
    print("=" * 80)
    for _, row in summary_df.iterrows():
        print(f"{row['variable']}:")
        print(f"  Period: {row['first_year']:.0f}-{row['last_year']:.0f} ({row['count']} observations)")
        print(f"  Mean: {row['mean']:.3f}, Median: {row['median']:.3f}, Std: {row['std']:.3f}")
        print(f"  Range: [{row['min']:.3f}, {row['max']:.3f}]")
        if 'ratio' in row['variable'] and row['variable'] != 'exchange_rate_volatility':
            if row['mean'] > 1:
                print(f"  Interpretation: China typically higher than US (mean ratio = {row['mean']:.2f})")
            else:
                print(f"  Interpretation: US typically higher than China (mean ratio = {row['mean']:.2f})")
        print()

def main():
    """Main function to create US-China raw ratio plots"""
    print("US-CHINA RAW RATIOS VISUALIZATION")
    print("=" * 50)
    
    # Ensure plots directory exists
    Path("plots").mkdir(exist_ok=True)
    Path("data").mkdir(exist_ok=True)
    
    # Load data
    main_data, education_data = load_us_china_data()
    
    # Prepare raw ratios
    plot_data = prepare_raw_ratios(main_data, education_data)
    
    # Create individual plots
    create_individual_raw_plots(plot_data)
    
    # Create summary statistics
    create_summary_statistics(plot_data)
    
    print("\n" + "="*50)
    print("VISUALIZATION COMPLETE")
    print("="*50)
    print("Generated files:")
    print("  - plots/us_china_raw_ratios_1989_2024.png")
    print("  - data/us_china_raw_ratios_summary.csv")

if __name__ == "__main__":
    main()
