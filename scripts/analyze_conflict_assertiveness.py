#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dataloaders.midb_dataloader import MIDBDataLoader
from typing import Tuple, List, Dict
import warnings
warnings.filterwarnings('ignore')

class ConflictAssertivenessAnalyzer:
    """
    Analyzer for country assertiveness in militarized disputes using MIDB data.
    
    Measures and plots assertiveness over time with indicators for status quo changes.
    """
    
    def __init__(self, midb_file_path: str, year_range: Tuple[int, int] = None):
        """
        Initialize the analyzer.
        
        Args:
            midb_file_path: Path to MIDB CSV file
            year_range: Optional tuple of (start_year, end_year) to filter data
        """
        self.midb_file_path = midb_file_path
        self.year_range = year_range
        self.loader = None
        self.assertiveness_data = None
        self.status_quo_changes = None
        
    def load_and_process_data(self) -> None:
        """Load MIDB data and calculate assertiveness scores."""
        print("Loading MIDB data...")
        self.loader = MIDBDataLoader(self.midb_file_path, year_range=self.year_range)
        
        # Calculate assertiveness scores
        print("Calculating assertiveness scores...")
        self.assertiveness_data = self.loader.calculate_assertiveness_score()
        
        # Identify status quo change attempts
        print("Identifying status quo change attempts...")
        self.status_quo_changes = self.loader.identify_status_quo_changes(threshold=0.7)
        
        print(f"Loaded {len(self.assertiveness_data)} conflict records")
        print(f"Identified {len(self.status_quo_changes)} status quo change attempts")
    
    def create_rolling_window_analysis(self, window_years: int = 5) -> pd.DataFrame:
        """
        Create rolling window analysis of assertiveness over time.
        
        Args:
            window_years: Size of rolling window in years
            
        Returns:
            pd.DataFrame: Rolling averages of assertiveness by country-year
        """
        if self.assertiveness_data is None:
            self.load_and_process_data()
        
        print(f"Creating {window_years}-year rolling window analysis...")
        
        # Get yearly maximum assertiveness per country
        yearly_max = self.assertiveness_data.groupby(['ccode', 'country', 'styear']).agg({
            'assertiveness_score': 'max',
            'hostlev': 'max',
            'hiact': 'max',
            'dispnum': 'count'  # Count of disputes per year
        }).reset_index()
        yearly_max.rename(columns={'dispnum': 'dispute_count'}, inplace=True)
        
        # Create complete year range for each country
        if self.year_range:
            year_min, year_max = self.year_range
        else:
            year_min = yearly_max['styear'].min()
            year_max = yearly_max['styear'].max()
        
        all_years = list(range(year_min, year_max + 1))
        countries = yearly_max[['ccode', 'country']].drop_duplicates()
        
        # Create complete country-year combinations
        complete_data = []
        for _, country in countries.iterrows():
            for year in all_years:
                complete_data.append({
                    'ccode': country['ccode'],
                    'country': country['country'],
                    'styear': year
                })
        
        complete_df = pd.DataFrame(complete_data)
        
        # Merge with actual data
        merged = complete_df.merge(yearly_max, on=['ccode', 'country', 'styear'], how='left')
        merged['assertiveness_score'] = merged['assertiveness_score'].fillna(0)
        merged['dispute_count'] = merged['dispute_count'].fillna(0)
        
        # Calculate rolling averages
        rolling_data = []
        for ccode in merged['ccode'].unique():
            country_data = merged[merged['ccode'] == ccode].sort_values('styear')
            
            country_data['assertiveness_rolling'] = country_data['assertiveness_score'].rolling(
                window=window_years, min_periods=1, center=True
            ).mean()
            
            country_data['dispute_count_rolling'] = country_data['dispute_count'].rolling(
                window=window_years, min_periods=1, center=True
            ).mean()
            
            rolling_data.append(country_data)
        
        return pd.concat(rolling_data, ignore_index=True)
    
    def plot_assertiveness_timeseries(self, countries: List[str] = None, 
                                    window_years: int = 5, 
                                    figsize: Tuple[int, int] = (15, 10)) -> None:
        """
        Plot assertiveness time series for selected countries.
        
        Args:
            countries: List of country names to plot (None for top 6)
            window_years: Rolling window size in years
            figsize: Figure size tuple
        """
        if self.assertiveness_data is None:
            self.load_and_process_data()
        
        # Get rolling window data
        rolling_data = self.create_rolling_window_analysis(window_years)
        
        # Select countries to plot
        if countries is None:
            top_countries = self.loader.get_top_countries(6)
            countries = [self.loader.country_mapping.get(code, f'Country_{code}') 
                        for code in top_countries]
        
        # Filter data for selected countries
        plot_data = rolling_data[rolling_data['country'].isin(countries)]
        
        # Create the plot
        fig, axes = plt.subplots(2, 3, figsize=figsize)
        axes = axes.flatten()
        
        # Color palette
        colors = plt.cm.Set1(np.linspace(0, 1, len(countries)))
        
        for i, country in enumerate(countries):
            ax = axes[i]
            country_data = plot_data[plot_data['country'] == country]
            
            if country_data.empty:
                ax.text(0.5, 0.5, f'No data for {country}', 
                       transform=ax.transAxes, ha='center', va='center')
                ax.set_title(country)
                continue
            
            # Plot rolling average assertiveness
            ax.plot(country_data['styear'], country_data['assertiveness_rolling'], 
                   color=colors[i], linewidth=2, alpha=0.8)
            
            # Add status quo change markers (red dots)
            country_code = country_data['ccode'].iloc[0]
            status_quo_country = self.status_quo_changes[
                self.status_quo_changes['ccode'] == country_code
            ]
            
            if not status_quo_country.empty:
                ax.scatter(status_quo_country['styear'], 
                          [rolling_data[(rolling_data['ccode'] == country_code) & 
                                      (rolling_data['styear'] == year)]['assertiveness_rolling'].iloc[0] 
                           if len(rolling_data[(rolling_data['ccode'] == country_code) & 
                                             (rolling_data['styear'] == year)]) > 0 
                           else 0.7  # Default high value if no rolling data
                           for year in status_quo_country['styear']],
                          color='red', s=50, alpha=0.8, zorder=5,
                          label='Status Quo Change')
            
            ax.set_title(f'{country}', fontsize=12, fontweight='bold')
            ax.set_xlabel('Year')
            ax.set_ylabel('Assertiveness Score')
            ax.grid(True, alpha=0.3)
            ax.set_ylim(0, 1)
            
            # Add legend if there are status quo changes
            if not status_quo_country.empty:
                ax.legend(fontsize=8)
        
        # Remove empty subplots
        for j in range(len(countries), len(axes)):
            fig.delaxes(axes[j])
        
        plt.tight_layout()
        plt.suptitle(f'Country Assertiveness Over Time ({window_years}-Year Rolling Average)\n'
                    f'Red dots indicate major status quo change attempts', 
                    y=1.02, fontsize=14)
        
        # Save plot
        plt.savefig('plots/conflict_assertiveness_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print summary statistics
        self._print_analysis_summary(plot_data, countries)
    
    def _print_analysis_summary(self, data: pd.DataFrame, countries: List[str]) -> None:
        """Print summary statistics for the analysis."""
        print("\n" + "="*60)
        print("ASSERTIVENESS ANALYSIS SUMMARY")
        print("="*60)
        
        for country in countries:
            country_data = data[data['country'] == country]
            if country_data.empty:
                continue
                
            country_code = country_data['ccode'].iloc[0]
            status_quo_count = len(self.status_quo_changes[
                self.status_quo_changes['ccode'] == country_code
            ])
            
            avg_assertiveness = country_data['assertiveness_rolling'].mean()
            max_assertiveness = country_data['assertiveness_rolling'].max()
            total_disputes = country_data['dispute_count'].sum()
            
            print(f"\n{country}:")
            print(f"  Average Assertiveness: {avg_assertiveness:.3f}")
            print(f"  Peak Assertiveness: {max_assertiveness:.3f}")
            print(f"  Total Disputes: {int(total_disputes)}")
            print(f"  Status Quo Changes: {status_quo_count}")
    
    def analyze_status_quo_patterns(self) -> pd.DataFrame:
        """
        Analyze patterns in status quo change attempts.
        
        Returns:
            pd.DataFrame: Analysis of status quo change patterns
        """
        if self.status_quo_changes is None:
            self.load_and_process_data()
        
        print("\n" + "="*60)
        print("STATUS QUO CHANGE ANALYSIS")
        print("="*60)
        
        # Group by country
        country_analysis = self.status_quo_changes.groupby(['ccode', 'country']).agg({
            'styear': ['count', 'min', 'max'],
            'assertiveness_score': 'mean',
            'hostlev': 'mean',
            'hiact': 'mean'
        }).round(3)
        
        country_analysis.columns = ['total_attempts', 'first_attempt', 'last_attempt', 
                                   'avg_assertiveness', 'avg_hostility', 'avg_escalation']
        
        print("\nTop Countries by Status Quo Change Attempts:")
        print(country_analysis.sort_values('total_attempts', ascending=False).head(10))
        
        # Temporal analysis
        temporal_analysis = self.status_quo_changes.groupby('styear').size()
        print(f"\nTemporal Distribution:")
        print(f"Most active year: {temporal_analysis.idxmax()} ({temporal_analysis.max()} attempts)")
        print(f"Peak decades: {temporal_analysis.groupby(temporal_analysis.index // 10 * 10).sum().nlargest(3)}")
        
        return country_analysis

def main():
    """Main execution function."""
    # Configuration - using a more focused time range for testing
    MIDB_FILE = 'data/military/MIDB 5.0.csv'
    YEAR_RANGE = (1990, 2010)  # 20-year period for faster testing
    WINDOW_YEARS = 5
    
    print("Starting conflict assertiveness analysis...")
    print(f"Time range: {YEAR_RANGE[0]}-{YEAR_RANGE[1]}")
    print(f"Rolling window: {WINDOW_YEARS} years")
    
    # Initialize analyzer
    analyzer = ConflictAssertivenessAnalyzer(MIDB_FILE, year_range=YEAR_RANGE)
    
    # Run analysis
    try:
        analyzer.load_and_process_data()
        
        # Plot assertiveness time series
        analyzer.plot_assertiveness_timeseries(
            countries=None,  # Will select top 6 countries
            window_years=WINDOW_YEARS
        )
        
        # Analyze status quo patterns
        analyzer.analyze_status_quo_patterns()
        
        print("\nAnalysis complete! Plot saved to 'plots/conflict_assertiveness_analysis.png'")
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()