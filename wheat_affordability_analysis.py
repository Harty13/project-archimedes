#!/usr/bin/env python3
"""
Wheat Affordability Analysis: Income-Deflated Price Index (Option A)

This script implements Option A from the theoretical framework:
A_{i,t} = p_{i,t} / y^{pc}_{i,t}

Where:
- A_{i,t} = affordability index (fraction of annual income needed to buy 1 kg wheat)
- p_{i,t} = nominal wheat price (local currency/kg)
- y^{pc}_{i,t} = GDP per capita (same currency/year)

The script creates a cross-country comparable measure of wheat affordability
for the UK and US during 1850-1960, suitable for structural transformation analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

class WheatAffordabilityAnalyzer:
    """
    Analyzer for creating income-deflated wheat affordability indices
    following Option A methodology from the theoretical framework.
    """
    
    def __init__(self):
        self.gdp_data = pd.DataFrame()
        self.grain_data = pd.DataFrame()
        self.affordability_data = pd.DataFrame()
        
    def load_data(self):
        """Load GDP per capita and grain price data"""
        print("Loading data for wheat affordability analysis...")
        
        # Load GDP per capita data
        try:
            gdp_file = Path("data/us_uk_gdp_per_capita.csv")
            if gdp_file.exists():
                self.gdp_data = pd.read_csv(gdp_file)
                print(f"✓ Loaded GDP data: {len(self.gdp_data)} records")
            else:
                print("✗ GDP per capita file not found")
                return False
        except Exception as e:
            print(f"✗ Error loading GDP data: {e}")
            return False
            
        # Load grain price data
        try:
            grain_file = Path("data/chicago_uk_grain_prices.csv")
            if grain_file.exists():
                self.grain_data = pd.read_csv(grain_file)
                print(f"✓ Loaded grain price data: {len(self.grain_data)} records")
            else:
                print("✗ Grain price file not found")
                return False
        except Exception as e:
            print(f"✗ Error loading grain price data: {e}")
            return False
            
        return True
        
    def clean_and_prepare_data(self, start_year=1850, end_year=1960):
        """
        Clean and prepare data for the specified time period
        
        Args:
            start_year (int): Start year for analysis (default: 1850)
            end_year (int): End year for analysis (default: 1960)
        """
        print(f"Preparing data for period {start_year}-{end_year}...")
        
        # Clean GDP data
        gdp_clean = self.gdp_data.copy()
        gdp_clean = gdp_clean[(gdp_clean['Year'] >= start_year) & (gdp_clean['Year'] <= end_year)]
        gdp_clean = gdp_clean[gdp_clean['Entity'].isin(['United Kingdom', 'United States'])]
        gdp_clean = gdp_clean.dropna(subset=['GDP per capita'])
        
        # Standardize country names
        gdp_clean['country'] = gdp_clean['Entity'].map({
            'United Kingdom': 'UK',
            'United States': 'US'
        })
        
        gdp_clean = gdp_clean[['Year', 'country', 'GDP per capita']].rename(columns={
            'Year': 'year',
            'GDP per capita': 'gdp_per_capita'
        })
        
        print(f"✓ GDP data: {len(gdp_clean)} records for {gdp_clean['country'].nunique()} countries")
        
        # Clean grain price data
        grain_clean = self.grain_data.copy()
        grain_clean = grain_clean[(grain_clean['year'] >= start_year) & (grain_clean['year'] <= end_year)]
        grain_clean = grain_clean.dropna(subset=['grain_price'])
        
        # Remove obvious outliers (e.g., the 298.75 value in UK data)
        grain_clean = grain_clean[grain_clean['grain_price'] < 300]
        
        # Aggregate monthly data to annual averages
        grain_annual = grain_clean.groupby(['year', 'country']).agg({
            'grain_price': 'mean'
        }).reset_index()
        
        print(f"✓ Grain price data: {len(grain_annual)} annual records for {grain_annual['country'].nunique()} countries")
        
        # Store cleaned data
        self.gdp_clean = gdp_clean
        self.grain_clean = grain_annual
        
        return True
        
    def calculate_affordability_index(self):
        """
        Calculate the affordability index A_{i,t} = p_{i,t} / y^{pc}_{i,t}
        
        This creates a unit-free measure of wheat affordability that is
        cross-country comparable and suitable for regression analysis.
        """
        print("Calculating affordability indices...")
        
        # Merge GDP and grain price data
        merged_data = pd.merge(
            self.gdp_clean,
            self.grain_clean,
            on=['year', 'country'],
            how='inner'
        )
        
        if merged_data.empty:
            print("✗ No overlapping data found between GDP and grain prices")
            return False
            
        print(f"✓ Merged data: {len(merged_data)} records")
        
        # Calculate affordability index: A_{i,t} = p_{i,t} / y^{pc}_{i,t}
        # This represents the fraction of annual income needed to buy 1 kg of wheat
        merged_data['affordability_index'] = merged_data['grain_price'] / merged_data['gdp_per_capita']
        
        # Calculate log affordability for regression use: x_{i,t} = ln(A_{i,t})
        merged_data['log_affordability'] = np.log(merged_data['affordability_index'])
        
        # Calculate alternative interpretation: kg purchasable with 1% of GDP per capita
        merged_data['kg_per_1pct_gdp'] = 0.01 / merged_data['affordability_index']
        
        # Add some summary statistics
        merged_data['affordability_pct'] = merged_data['affordability_index'] * 100  # As percentage
        
        self.affordability_data = merged_data
        
        print("✓ Affordability indices calculated:")
        print(f"  - Affordability index (fraction of income): {merged_data['affordability_index'].min():.6f} to {merged_data['affordability_index'].max():.6f}")
        print(f"  - Log affordability: {merged_data['log_affordability'].min():.3f} to {merged_data['log_affordability'].max():.3f}")
        print(f"  - Kg per 1% of GDP: {merged_data['kg_per_1pct_gdp'].min():.1f} to {merged_data['kg_per_1pct_gdp'].max():.1f}")
        
        return True
        
    def generate_summary_statistics(self):
        """Generate comprehensive summary statistics"""
        if self.affordability_data.empty:
            print("No affordability data available for summary")
            return
            
        print("\n" + "="*80)
        print("WHEAT AFFORDABILITY ANALYSIS - SUMMARY STATISTICS")
        print("="*80)
        
        data = self.affordability_data
        
        print(f"\nDataset Overview:")
        print(f"  Period: {data['year'].min()}-{data['year'].max()}")
        print(f"  Countries: {', '.join(sorted(data['country'].unique()))}")
        print(f"  Total observations: {len(data)}")
        
        print(f"\nCountry-wise Coverage:")
        coverage = data.groupby('country').agg({
            'year': ['min', 'max', 'count'],
            'affordability_index': ['mean', 'std', 'min', 'max']
        }).round(6)
        print(coverage)
        
        print(f"\nAffordability Index Statistics:")
        print(f"  Interpretation: Fraction of annual income needed to buy 1 kg wheat")
        print(f"  Overall mean: {data['affordability_index'].mean():.6f}")
        print(f"  Overall std:  {data['affordability_index'].std():.6f}")
        print(f"  Range: {data['affordability_index'].min():.6f} to {data['affordability_index'].max():.6f}")
        
        print(f"\nLog Affordability (for regression):")
        print(f"  Mean: {data['log_affordability'].mean():.3f}")
        print(f"  Std:  {data['log_affordability'].std():.3f}")
        print(f"  Range: {data['log_affordability'].min():.3f} to {data['log_affordability'].max():.3f}")
        
        print(f"\nAlternative Interpretation (kg per 1% of GDP per capita):")
        print(f"  Mean: {data['kg_per_1pct_gdp'].mean():.1f} kg")
        print(f"  Range: {data['kg_per_1pct_gdp'].min():.1f} to {data['kg_per_1pct_gdp'].max():.1f} kg")
        
        # Period analysis
        print(f"\nTrend Analysis:")
        for country in sorted(data['country'].unique()):
            country_data = data[data['country'] == country].sort_values('year')
            if len(country_data) > 1:
                start_afford = country_data['affordability_index'].iloc[0]
                end_afford = country_data['affordability_index'].iloc[-1]
                change_pct = ((end_afford - start_afford) / start_afford) * 100
                
                print(f"  {country}:")
                print(f"    {country_data['year'].iloc[0]}: {start_afford:.6f}")
                print(f"    {country_data['year'].iloc[-1]}: {end_afford:.6f}")
                print(f"    Change: {change_pct:+.1f}%")
                
    def create_visualization(self, save_path="wheat_affordability_1850_1960.png"):
        """
        Create comprehensive visualization of wheat affordability trends
        
        Args:
            save_path (str): Path to save the plot
        """
        if self.affordability_data.empty:
            print("No data available for visualization")
            return
            
        print(f"Creating visualization...")
        
        # Set up the plot style
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        data = self.affordability_data
        
        # Color scheme
        colors = {'UK': '#1f77b4', 'US': '#ff7f0e'}
        
        # 1. Affordability Index Over Time
        ax1 = axes[0, 0]
        for country in sorted(data['country'].unique()):
            country_data = data[data['country'] == country].sort_values('year')
            ax1.plot(country_data['year'], country_data['affordability_index'], 
                    label=country, linewidth=2, color=colors[country], alpha=0.8)
                    
        ax1.set_title('Wheat Affordability Index (1850-1960)', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Affordability Index\n(Fraction of Annual Income)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        
        # 2. Log Affordability (for regression)
        ax2 = axes[0, 1]
        for country in sorted(data['country'].unique()):
            country_data = data[data['country'] == country].sort_values('year')
            ax2.plot(country_data['year'], country_data['log_affordability'], 
                    label=country, linewidth=2, color=colors[country], alpha=0.8)
                    
        ax2.set_title('Log Affordability Index (Regression Variable)', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('ln(Affordability Index)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # 3. Alternative Interpretation: kg per 1% of GDP
        ax3 = axes[1, 0]
        for country in sorted(data['country'].unique()):
            country_data = data[data['country'] == country].sort_values('year')
            ax3.plot(country_data['year'], country_data['kg_per_1pct_gdp'], 
                    label=country, linewidth=2, color=colors[country], alpha=0.8)
                    
        ax3.set_title('Wheat Purchasing Power\n(kg per 1% of GDP per capita)', fontsize=14, fontweight='bold')
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Kilograms of Wheat')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Comparative Analysis: Ratio
        ax4 = axes[1, 1]
        
        # Calculate UK/US ratio for comparison
        uk_data = data[data['country'] == 'UK'].set_index('year')['affordability_index']
        us_data = data[data['country'] == 'US'].set_index('year')['affordability_index']
        
        # Find common years
        common_years = uk_data.index.intersection(us_data.index)
        if len(common_years) > 0:
            ratio_data = uk_data[common_years] / us_data[common_years]
            ax4.plot(common_years, ratio_data, linewidth=2, color='green', alpha=0.8)
            ax4.axhline(y=1, color='black', linestyle='--', alpha=0.5, label='Equal Affordability')
            
        ax4.set_title('Relative Affordability\n(UK/US Ratio)', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Year')
        ax4.set_ylabel('UK Affordability / US Affordability')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        # Add overall title and description
        fig.suptitle('Income-Deflated Wheat Affordability Analysis (Option A)\n' + 
                    'A_{i,t} = p_{i,t} / y^{pc}_{i,t}', 
                    fontsize=16, fontweight='bold', y=0.98)
        
        # Add methodology note
        fig.text(0.5, 0.02, 
                'Methodology: Affordability Index = Wheat Price / GDP per capita (unit-free, cross-country comparable)\n' +
                'Lower values indicate wheat is more affordable (requires smaller fraction of income)',
                ha='center', fontsize=10, style='italic')
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.93, bottom=0.08)
        
        # Save the plot
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✓ Visualization saved to {save_path}")
        
        plt.show()
        
    def export_data(self, filename="wheat_affordability_data_1850_1960.csv"):
        """
        Export the final affordability dataset
        
        Args:
            filename (str): Output filename
        """
        if self.affordability_data.empty:
            print("No data to export")
            return
            
        # Prepare export data with clear column names
        export_data = self.affordability_data.copy()
        export_data = export_data.sort_values(['country', 'year'])
        
        # Reorder and rename columns for clarity
        export_columns = {
            'year': 'year',
            'country': 'country', 
            'grain_price': 'wheat_price_nominal',
            'gdp_per_capita': 'gdp_per_capita',
            'affordability_index': 'affordability_index',
            'log_affordability': 'log_affordability_index',
            'kg_per_1pct_gdp': 'kg_wheat_per_1pct_gdp',
            'affordability_pct': 'affordability_percentage'
        }
        
        export_data = export_data[list(export_columns.keys())].rename(columns=export_columns)
        
        # Add metadata as comments in the CSV
        header_comment = [
            "# Wheat Affordability Analysis: Income-Deflated Price Index (Option A)",
            "# Methodology: A_{i,t} = p_{i,t} / y^{pc}_{i,t}",
            "# ",
            "# Column Definitions:",
            "# - affordability_index: Fraction of annual income needed to buy 1 kg wheat (unit-free)",
            "# - log_affordability_index: Natural log of affordability index (for regression)",
            "# - kg_wheat_per_1pct_gdp: Kg of wheat purchasable with 1% of GDP per capita",
            "# - affordability_percentage: Affordability index as percentage",
            "# ",
            "# Lower affordability_index values = wheat more affordable",
            "# Higher kg_wheat_per_1pct_gdp values = wheat more affordable",
            "#"
        ]
        
        # Save with header
        with open(filename, 'w') as f:
            f.write('\n'.join(header_comment) + '\n')
            export_data.to_csv(f, index=False)
            
        print(f"✓ Data exported to {filename}")
        print(f"  Records: {len(export_data)}")
        print(f"  Countries: {', '.join(sorted(export_data['country'].unique()))}")
        print(f"  Period: {export_data['year'].min()}-{export_data['year'].max()}")
        
        return export_data


def main():
    """Main analysis pipeline"""
    print("="*80)
    print("WHEAT AFFORDABILITY ANALYSIS")
    print("Income-Deflated Price Index Implementation (Option A)")
    print("="*80)
    
    # Initialize analyzer
    analyzer = WheatAffordabilityAnalyzer()
    
    # Load data
    if not analyzer.load_data():
        print("Failed to load data. Exiting.")
        return
        
    # Clean and prepare data for 1850-1960 period
    if not analyzer.clean_and_prepare_data(start_year=1850, end_year=1960):
        print("Failed to prepare data. Exiting.")
        return
        
    # Calculate affordability indices
    if not analyzer.calculate_affordability_index():
        print("Failed to calculate affordability indices. Exiting.")
        return
        
    # Generate summary statistics
    analyzer.generate_summary_statistics()
    
    # Create visualization
    analyzer.create_visualization()
    
    # Export final dataset
    final_data = analyzer.export_data()
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print("\nKey Outputs:")
    print("1. wheat_affordability_1850_1960.png - Comprehensive visualization")
    print("2. wheat_affordability_data_1850_1960.csv - Final dataset for regression")
    print("\nThe affordability index A_{i,t} = p_{i,t} / y^{pc}_{i,t} is now ready for use")
    print("in your structural transformation model as the key explanatory variable.")
    print("\nExpected relationship: β₁ < 0 (cheaper wheat → higher urbanization)")


if __name__ == "__main__":
    main()
