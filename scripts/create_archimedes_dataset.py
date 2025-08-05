#!/usr/bin/env python3
"""
Archimedes Model Dataset Creator

This script creates a comprehensive dataset combining:
1. Wheat affordability ratios (from existing analysis)
2. GDP ratios (US vs UK)
3. Military power ratios (based on relative global shares)

Following the updated Archimedes model specification with relative military power.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from dataloaders.nmc_dataloader import NMCDataLoader
from dataloaders.gdp_dataloader import GDPDataLoader
from dataloaders.gdp_per_capita_dataloader import GDPPerCapitaDataLoader
import warnings

warnings.filterwarnings('ignore')

class ArchimedesDatasetCreator:
    """
    Creates the complete Archimedes model dataset with wheat affordability,
    GDP ratios, and relative military power ratios.
    """
    
    def __init__(self, start_year=1850, end_year=1960):
        self.start_year = start_year
        self.end_year = end_year
        self.wheat_data = pd.DataFrame()
        self.gdp_data = pd.DataFrame()
        self.military_data = pd.DataFrame()
        self.final_dataset = pd.DataFrame()
        
    def load_wheat_affordability_data(self):
        """Load existing wheat affordability data"""
        print("Loading wheat affordability data...")
        
        try:
            wheat_file = Path("wheat_affordability_data_1850_1960.csv")
            if wheat_file.exists():
                # Skip comment lines starting with #
                self.wheat_data = pd.read_csv(wheat_file, comment='#')
                
                # Filter for time range
                self.wheat_data = self.wheat_data[
                    (self.wheat_data['year'] >= self.start_year) & 
                    (self.wheat_data['year'] <= self.end_year)
                ]
                
                print(f"✓ Loaded wheat affordability data: {len(self.wheat_data)} records")
                print(f"  Countries: {', '.join(sorted(self.wheat_data['country'].unique()))}")
                print(f"  Years: {self.wheat_data['year'].min()}-{self.wheat_data['year'].max()}")
                return True
            else:
                print("✗ Wheat affordability file not found. Please run wheat_affordability_analysis.py first.")
                return False
        except Exception as e:
            print(f"✗ Error loading wheat affordability data: {e}")
            return False
    
    def load_gdp_data(self):
        """Load and process GDP data for US and UK"""
        print("Loading GDP data...")
        
        try:
            # Load GDP level data using the dataloader
            gdp_loader = GDPDataLoader('data/gdp/gdp-maddison-project-database.csv', 
                                     countries=['United States', 'United Kingdom'])
            gdp_processed = gdp_loader.load_data()
            
            # Filter for time range
            gdp_filtered = gdp_processed[
                (gdp_processed['year'] >= self.start_year) &
                (gdp_processed['year'] <= self.end_year)
            ].copy()
            
            # Standardize country names
            gdp_filtered['country'] = gdp_filtered['country'].map({
                'United States': 'US',
                'United Kingdom': 'UK'
            })
            
            self.gdp_data = gdp_filtered
            print(f"✓ Loaded GDP data: {len(self.gdp_data)} records")
            print(f"  Countries: {', '.join(sorted(self.gdp_data['country'].unique()))}")
            print(f"  Years: {self.gdp_data['year'].min()}-{self.gdp_data['year'].max()}")
            return True
            
        except Exception as e:
            print(f"✗ Error loading GDP data: {e}")
            return False
    
    def calculate_relative_military_scores(self):
        """Calculate relative military power scores using global shares approach"""
        print("Calculating relative military power scores...")
        
        try:
            # Load military data
            loader = NMCDataLoader('data/military/NMC-60-wsupplementary.csv')
            data = loader.load_data()
            
            # Filter for time range
            data = data[
                (data['year'] >= self.start_year) & 
                (data['year'] <= self.end_year)
            ]
            
            # Calculate global totals by year
            yearly_totals = data.groupby('year').agg({
                'milex': 'sum',
                'milper': 'sum'
            }).reset_index()
            yearly_totals.columns = ['year', 'global_milex', 'global_milper']
            
            # Merge with original data
            data_with_totals = data.merge(yearly_totals, on='year')
            
            # Calculate relative scores (as percentages)
            data_with_totals['milex_pct'] = (data_with_totals['milex'] / data_with_totals['global_milex']) * 100
            data_with_totals['milper_pct'] = (data_with_totals['milper'] / data_with_totals['global_milper']) * 100
            
            # Filter for US and UK only
            us_uk_data = data_with_totals[
                data_with_totals['country'].isin(['United States of America', 'United Kingdom'])
            ].copy()
            
            # Standardize country names
            us_uk_data['country'] = us_uk_data['country'].map({
                'United States of America': 'US',
                'United Kingdom': 'UK'
            })
            
            self.military_data = us_uk_data[['year', 'country', 'milex_pct', 'milper_pct']]
            print(f"✓ Calculated military power scores: {len(self.military_data)} records")
            print(f"  Countries: {', '.join(sorted(self.military_data['country'].unique()))}")
            print(f"  Years: {self.military_data['year'].min()}-{self.military_data['year'].max()}")
            return True
            
        except Exception as e:
            print(f"✗ Error calculating military power scores: {e}")
            return False
    
    def calculate_archimedes_ratios(self):
        """Calculate all the log ratios following Archimedes model specification"""
        print("Calculating Archimedes model ratios...")
        
        # Start with years from wheat affordability data (our anchor)
        years = sorted(self.wheat_data['year'].unique())
        ratio_data = []
        
        for year in years:
            year_data = {'year': year}
            
            # 1. Wheat affordability ratio: ln(A_US / A_UK)
            # Note: we flip sign so cheaper in US is positive: -ln(A_US / A_UK)
            wheat_year = self.wheat_data[self.wheat_data['year'] == year]
            if len(wheat_year) == 2:  # Both US and UK data available
                us_afford = wheat_year[wheat_year['country'] == 'US']['affordability_index'].iloc[0]
                uk_afford = wheat_year[wheat_year['country'] == 'UK']['affordability_index'].iloc[0]
                
                if us_afford > 0 and uk_afford > 0:
                    year_data['wheat_affordability_ratio'] = -np.log(us_afford / uk_afford)  # Flipped sign
                    year_data['log_wheat_affordability_ratio'] = year_data['wheat_affordability_ratio']
            
            # 2. GDP ratio: ln(GDP_US / GDP_UK)
            gdp_year = self.gdp_data[self.gdp_data['year'] == year]
            if len(gdp_year) == 2:  # Both US and UK data available
                us_gdp = gdp_year[gdp_year['country'] == 'US']['gdp'].iloc[0]
                uk_gdp = gdp_year[gdp_year['country'] == 'UK']['gdp'].iloc[0]
                
                if us_gdp > 0 and uk_gdp > 0:
                    year_data['gdp_ratio_us_uk'] = np.log(us_gdp / uk_gdp)
            
            # 3. Military expenditure ratio: ln(S_US / S_UK) where S = global share
            mil_year = self.military_data[self.military_data['year'] == year]
            if len(mil_year) == 2:  # Both US and UK data available
                us_milex_pct = mil_year[mil_year['country'] == 'US']['milex_pct'].iloc[0]
                uk_milex_pct = mil_year[mil_year['country'] == 'UK']['milex_pct'].iloc[0]
                
                if us_milex_pct > 0 and uk_milex_pct > 0:
                    year_data['military_expenditure_ratio_us_uk'] = np.log(us_milex_pct / uk_milex_pct)
            
            # 4. Military personnel ratio: ln(S_US / S_UK) where S = global share
            if len(mil_year) == 2:
                us_milper_pct = mil_year[mil_year['country'] == 'US']['milper_pct'].iloc[0]
                uk_milper_pct = mil_year[mil_year['country'] == 'UK']['milper_pct'].iloc[0]
                
                if us_milper_pct > 0 and uk_milper_pct > 0:
                    year_data['military_personnel_ratio_us_uk'] = np.log(us_milper_pct / uk_milper_pct)
            
            # 5. Composite military ratio (simple average of expenditure and personnel)
            if 'military_expenditure_ratio_us_uk' in year_data and 'military_personnel_ratio_us_uk' in year_data:
                year_data['composite_military_ratio_us_uk'] = (
                    year_data['military_expenditure_ratio_us_uk'] + 
                    year_data['military_personnel_ratio_us_uk']
                ) / 2
            
            ratio_data.append(year_data)
        
        self.final_dataset = pd.DataFrame(ratio_data)
        
        # Remove rows with all NaN ratios
        ratio_columns = [col for col in self.final_dataset.columns if col != 'year']
        self.final_dataset = self.final_dataset.dropna(subset=ratio_columns, how='all')
        
        print(f"✓ Calculated Archimedes ratios for {len(self.final_dataset)} years")
        print(f"  Period: {self.final_dataset['year'].min()}-{self.final_dataset['year'].max()}")
        
        # Print data coverage
        for col in ratio_columns:
            coverage = self.final_dataset[col].notna().sum()
            print(f"  {col}: {coverage}/{len(self.final_dataset)} years ({coverage/len(self.final_dataset)*100:.1f}%)")
        
        return True
    
    def generate_summary_statistics(self):
        """Generate comprehensive summary statistics"""
        if self.final_dataset.empty:
            print("No final dataset available for summary")
            return
            
        print("\n" + "="*80)
        print("ARCHIMEDES MODEL DATASET - SUMMARY STATISTICS")
        print("="*80)
        
        data = self.final_dataset
        
        print(f"\nDataset Overview:")
        print(f"  Period: {data['year'].min()}-{data['year'].max()}")
        print(f"  Total observations: {len(data)}")
        
        print(f"\nVariable Definitions (following Archimedes model):")
        print(f"  wheat_affordability_ratio: -ln(A_US/A_UK) [positive = wheat cheaper in US]")
        print(f"  gdp_ratio_us_uk: ln(GDP_US/GDP_UK) [positive = US GDP larger]")
        print(f"  military_expenditure_ratio_us_uk: ln(S_US/S_UK) [positive = US larger global share]")
        print(f"  military_personnel_ratio_us_uk: ln(S_US/S_UK) [positive = US larger global share]")
        print(f"  composite_military_ratio_us_uk: average of expenditure and personnel ratios")
        
        print(f"\nSummary Statistics:")
        ratio_columns = [col for col in data.columns if col != 'year']
        summary_stats = data[ratio_columns].describe()
        print(summary_stats.round(3))
        
        print(f"\nData Coverage:")
        for col in ratio_columns:
            coverage = data[col].notna().sum()
            print(f"  {col}: {coverage}/{len(data)} years ({coverage/len(data)*100:.1f}%)")
        
        # Correlation matrix
        print(f"\nCorrelation Matrix:")
        corr_data = data[ratio_columns].corr()
        print(corr_data.round(3))
    
    def create_visualization(self, save_path="archimedes_dataset_analysis.png"):
        """Create comprehensive visualization of all ratios"""
        if self.final_dataset.empty:
            print("No data available for visualization")
            return
            
        print(f"Creating visualization...")
        
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Archimedes Model Dataset: US vs UK Log Ratios (1850-1960)', fontsize=16, fontweight='bold')
        
        data = self.final_dataset
        
        # 1. Wheat Affordability Ratio
        ax1 = axes[0, 0]
        if 'wheat_affordability_ratio' in data.columns:
            clean_data = data.dropna(subset=['wheat_affordability_ratio'])
            ax1.plot(clean_data['year'], clean_data['wheat_affordability_ratio'], 
                    linewidth=2, color='green', alpha=0.8)
            ax1.axhline(y=0, color='black', linestyle='--', alpha=0.5)
        ax1.set_title('Wheat Affordability Ratio\n-ln(A_US/A_UK)')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Log Ratio')
        ax1.grid(True, alpha=0.3)
        ax1.text(0.02, 0.98, 'Positive = Wheat cheaper in US', transform=ax1.transAxes, 
                verticalalignment='top', fontsize=8, style='italic')
        
        # 2. GDP Ratio
        ax2 = axes[0, 1]
        if 'gdp_ratio_us_uk' in data.columns:
            clean_data = data.dropna(subset=['gdp_ratio_us_uk'])
            ax2.plot(clean_data['year'], clean_data['gdp_ratio_us_uk'], 
                    linewidth=2, color='blue', alpha=0.8)
            ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
        ax2.set_title('GDP Ratio\nln(GDP_US/GDP_UK)')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Log Ratio')
        ax2.grid(True, alpha=0.3)
        ax2.text(0.02, 0.98, 'Positive = US GDP larger', transform=ax2.transAxes, 
                verticalalignment='top', fontsize=8, style='italic')
        
        # 3. Military Expenditure Ratio
        ax3 = axes[0, 2]
        if 'military_expenditure_ratio_us_uk' in data.columns:
            clean_data = data.dropna(subset=['military_expenditure_ratio_us_uk'])
            ax3.plot(clean_data['year'], clean_data['military_expenditure_ratio_us_uk'], 
                    linewidth=2, color='red', alpha=0.8)
            ax3.axhline(y=0, color='black', linestyle='--', alpha=0.5)
        ax3.set_title('Military Expenditure Ratio\nln(S_US/S_UK)')
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Log Ratio')
        ax3.grid(True, alpha=0.3)
        ax3.text(0.02, 0.98, 'Positive = US larger global share', transform=ax3.transAxes, 
                verticalalignment='top', fontsize=8, style='italic')
        
        # 4. Military Personnel Ratio
        ax4 = axes[1, 0]
        if 'military_personnel_ratio_us_uk' in data.columns:
            clean_data = data.dropna(subset=['military_personnel_ratio_us_uk'])
            ax4.plot(clean_data['year'], clean_data['military_personnel_ratio_us_uk'], 
                    linewidth=2, color='orange', alpha=0.8)
            ax4.axhline(y=0, color='black', linestyle='--', alpha=0.5)
        ax4.set_title('Military Personnel Ratio\nln(S_US/S_UK)')
        ax4.set_xlabel('Year')
        ax4.set_ylabel('Log Ratio')
        ax4.grid(True, alpha=0.3)
        ax4.text(0.02, 0.98, 'Positive = US larger global share', transform=ax4.transAxes, 
                verticalalignment='top', fontsize=8, style='italic')
        
        # 5. Composite Military Ratio
        ax5 = axes[1, 1]
        if 'composite_military_ratio_us_uk' in data.columns:
            clean_data = data.dropna(subset=['composite_military_ratio_us_uk'])
            ax5.plot(clean_data['year'], clean_data['composite_military_ratio_us_uk'], 
                    linewidth=2, color='purple', alpha=0.8)
            ax5.axhline(y=0, color='black', linestyle='--', alpha=0.5)
        ax5.set_title('Composite Military Ratio\n(Expenditure + Personnel)/2')
        ax5.set_xlabel('Year')
        ax5.set_ylabel('Log Ratio')
        ax5.grid(True, alpha=0.3)
        ax5.text(0.02, 0.98, 'Positive = US military dominance', transform=ax5.transAxes, 
                verticalalignment='top', fontsize=8, style='italic')
        
        # 6. All ratios together
        ax6 = axes[1, 2]
        colors = ['green', 'blue', 'red', 'orange', 'purple']
        labels = ['Wheat Affordability', 'GDP', 'Military Expenditure', 'Military Personnel', 'Composite Military']
        ratio_cols = ['wheat_affordability_ratio', 'gdp_ratio_us_uk', 'military_expenditure_ratio_us_uk', 
                     'military_personnel_ratio_us_uk', 'composite_military_ratio_us_uk']
        
        for i, col in enumerate(ratio_cols):
            if col in data.columns:
                clean_data = data.dropna(subset=[col])
                if not clean_data.empty:
                    ax6.plot(clean_data['year'], clean_data[col], 
                            linewidth=2, color=colors[i], alpha=0.7, label=labels[i])
        
        ax6.axhline(y=0, color='black', linestyle='--', alpha=0.5)
        ax6.set_title('All Ratios Combined')
        ax6.set_xlabel('Year')
        ax6.set_ylabel('Log Ratio')
        ax6.legend(fontsize=8)
        ax6.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✓ Visualization saved to {save_path}")
        plt.show()
    
    def export_dataset(self, filename=None):
        """Export the final Archimedes dataset"""
        if filename is None:
            filename = f"archimedes_dataset_{self.start_year}_{self.end_year}.csv"
            
        if self.final_dataset.empty:
            print("No dataset to export")
            return
        
        # Add metadata as comments
        header_comment = [
            "# Archimedes Model Dataset: US vs UK Log Ratios",
            f"# Period: {self.start_year}-{self.end_year}",
            "# ",
            "# Variable Definitions (following Archimedes model specification):",
            "# - wheat_affordability_ratio: -ln(A_US/A_UK) where A = wheat_price/gdp_per_capita",
            "#   Positive values = wheat more affordable in US relative to UK",
            "# - gdp_ratio_us_uk: ln(GDP_US/GDP_UK)",
            "#   Positive values = US GDP larger than UK GDP",
            "# - military_expenditure_ratio_us_uk: ln(S_US/S_UK) where S = global military expenditure share",
            "#   Positive values = US has larger share of global military expenditures than UK",
            "# - military_personnel_ratio_us_uk: ln(S_US/S_UK) where S = global military personnel share", 
            "#   Positive values = US has larger share of global military personnel than UK",
            "# - composite_military_ratio_us_uk: average of expenditure and personnel ratios",
            "#   Positive values = US military dominance over UK",
            "# ",
            "# All ratios follow log(US/UK) convention from Archimedes model",
            "# Missing values indicate data not available for that year",
            "#"
        ]
        
        # Save with header
        with open(filename, 'w') as f:
            f.write('\n'.join(header_comment) + '\n')
            self.final_dataset.to_csv(f, index=False)
            
        print(f"✓ Dataset exported to {filename}")
        print(f"  Records: {len(self.final_dataset)}")
        print(f"  Period: {self.final_dataset['year'].min()}-{self.final_dataset['year'].max()}")
        print(f"  Variables: {len(self.final_dataset.columns)-1} ratios + year")
        
        return self.final_dataset


def main():
    """Main pipeline for creating Archimedes dataset"""
    print("="*80)
    print("ARCHIMEDES MODEL DATASET CREATOR")
    print("Combining Wheat Affordability, GDP, and Relative Military Power")
    print("="*80)
    
    # Initialize creator (flexible time range)
    creator = ArchimedesDatasetCreator(start_year=1850, end_year=1960)
    
    # Load all data sources
    print("\n1. Loading data sources...")
    if not creator.load_wheat_affordability_data():
        print("Failed to load wheat affordability data. Exiting.")
        return
        
    if not creator.load_gdp_data():
        print("Failed to load GDP data. Exiting.")
        return
        
    if not creator.calculate_relative_military_scores():
        print("Failed to calculate military power scores. Exiting.")
        return
    
    # Calculate Archimedes ratios
    print("\n2. Calculating Archimedes model ratios...")
    if not creator.calculate_archimedes_ratios():
        print("Failed to calculate ratios. Exiting.")
        return
    
    # Generate summary statistics
    print("\n3. Generating summary statistics...")
    creator.generate_summary_statistics()
    
    # Create visualization
    print("\n4. Creating visualization...")
    creator.create_visualization()
    
    # Export final dataset
    print("\n5. Exporting dataset...")
    final_data = creator.export_dataset()
    
    print("\n" + "="*80)
    print("ARCHIMEDES DATASET CREATION COMPLETE")
    print("="*80)
    print("\nKey Outputs:")
    print("1. archimedes_dataset_1850_1960.csv - Complete dataset for regression")
    print("2. archimedes_dataset_analysis.png - Comprehensive visualization")
    print("\nThe dataset contains all log ratios specified in the Archimedes model:")
    print("- Wheat affordability ratio (structural transformation channel)")
    print("- GDP ratio (economic power)")
    print("- Military power ratios (relative global shares)")
    print("\nReady for logistic regression analysis to predict future power transitions!")


if __name__ == "__main__":
    main()
