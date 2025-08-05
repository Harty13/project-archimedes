import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

class GDPPerCapitaDataLoader:
    """
    Dataloader for GDP per capita data from the Maddison Project Database
    Focuses on historical GDP per capita comparisons between countries
    """
    
    def __init__(self, data_file="data/gdp/gdp-per-capita-maddison-project-database.csv"):
        self.data_file = Path(data_file)
        self.raw_data = pd.DataFrame()
        self.processed_data = pd.DataFrame()
        self.country_data = {}
        
    def load_data(self):
        """Load GDP per capita data from the Maddison Project Database CSV"""
        print("Loading GDP per capita data from Maddison Project Database...")
        
        try:
            # Load the CSV file
            self.raw_data = pd.read_csv(self.data_file)
            
            print(f"Successfully loaded {len(self.raw_data)} records")
            print(f"Columns: {list(self.raw_data.columns)}")
            print(f"Countries available: {len(self.raw_data['Entity'].unique())}")
            print(f"Year range: {self.raw_data['Year'].min()} - {self.raw_data['Year'].max()}")
            
            # Basic data cleaning
            self.raw_data = self.raw_data.dropna(subset=['GDP per capita'])
            self.raw_data['GDP per capita'] = pd.to_numeric(self.raw_data['GDP per capita'], errors='coerce')
            self.raw_data = self.raw_data.dropna(subset=['GDP per capita'])
            
            print(f"After cleaning: {len(self.raw_data)} valid records")
            
        except Exception as e:
            print(f"Error loading GDP per capita data: {e}")
            
    def process_data(self, countries=None):
        """
        Process and filter data for specific countries
        
        Args:
            countries (list): List of country names to include. If None, includes all countries.
        """
        if self.raw_data.empty:
            print("No data loaded. Please run load_data() first.")
            return
            
        print("Processing GDP per capita data...")
        
        # If no countries specified, use all available countries
        if countries is None:
            countries = self.raw_data['Entity'].unique()
            
        # Filter data for specified countries
        filtered_data = self.raw_data[self.raw_data['Entity'].isin(countries)].copy()
        
        if filtered_data.empty:
            print(f"No data found for countries: {countries}")
            available_countries = self.raw_data['Entity'].unique()
            print(f"Available countries include: {list(available_countries[:10])}...")
            return
            
        # Create processed dataset
        self.processed_data = filtered_data.copy()
        self.processed_data = self.processed_data.sort_values(['Entity', 'Year'])
        
        # Store country-specific data
        for country in countries:
            country_subset = self.processed_data[self.processed_data['Entity'] == country].copy()
            if not country_subset.empty:
                self.country_data[country] = country_subset
                
        print(f"Processed data for {len(self.country_data)} countries:")
        for country, data in self.country_data.items():
            year_range = f"{data['Year'].min()}-{data['Year'].max()}"
            print(f"  {country}: {len(data)} records ({year_range})")
            
    def get_country_data(self, country_name):
        """
        Get data for a specific country
        
        Args:
            country_name (str): Name of the country
            
        Returns:
            pd.DataFrame: Country-specific GDP per capita data
        """
        if country_name in self.country_data:
            return self.country_data[country_name].copy()
        else:
            print(f"No data available for {country_name}")
            print(f"Available countries: {list(self.country_data.keys())}")
            return pd.DataFrame()
            
    def plot_comparison(self, countries=None, start_year=None, end_year=None, save_path=None):
        """
        Create comprehensive comparison plots for GDP per capita
        
        Args:
            countries (list): List of countries to compare
            start_year (int): Start year for analysis
            end_year (int): End year for analysis
            save_path (str): Path to save the plot
        """
        if self.processed_data.empty:
            print("No processed data available. Please run process_data() first.")
            return
            
        # Use all processed countries if none specified
        if countries is None:
            countries = list(self.country_data.keys())
            
        # Filter by year range if specified
        plot_data = self.processed_data[self.processed_data['Entity'].isin(countries)].copy()
        
        if start_year:
            plot_data = plot_data[plot_data['Year'] >= start_year]
        if end_year:
            plot_data = plot_data[plot_data['Year'] <= end_year]
            
        if plot_data.empty:
            print("No data available for the specified criteria")
            return
            
        print(f"Creating comparison plots for {len(countries)} countries...")
        
        # Set up the plotting style
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        year_range_str = ""
        if start_year or end_year:
            start = start_year or plot_data['Year'].min()
            end = end_year or plot_data['Year'].max()
            year_range_str = f" ({start}-{end})"
            
        fig.suptitle(f'GDP per Capita Comparison{year_range_str}', fontsize=16, fontweight='bold')
        
        # 1. Time series comparison
        ax1 = axes[0, 0]
        
        colors = plt.cm.Set1(np.linspace(0, 1, len(countries)))
        
        for i, country in enumerate(countries):
            country_subset = plot_data[plot_data['Entity'] == country]
            if not country_subset.empty:
                ax1.plot(country_subset['Year'], country_subset['GDP per capita'], 
                        label=country, linewidth=2, alpha=0.8, color=colors[i])
                        
        ax1.set_title('GDP per Capita Over Time')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('GDP per Capita (1990 International Dollars)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Log scale comparison (better for long-term growth)
        ax2 = axes[0, 1]
        
        for i, country in enumerate(countries):
            country_subset = plot_data[plot_data['Entity'] == country]
            if not country_subset.empty:
                ax2.semilogy(country_subset['Year'], country_subset['GDP per capita'], 
                           label=country, linewidth=2, alpha=0.8, color=colors[i])
                           
        ax2.set_title('GDP per Capita Over Time (Log Scale)')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('GDP per Capita (Log Scale)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # 3. Growth rates comparison
        ax3 = axes[1, 0]
        
        for i, country in enumerate(countries):
            country_subset = plot_data[plot_data['Entity'] == country].copy()
            if len(country_subset) > 1:
                # Calculate year-over-year growth rates
                country_subset = country_subset.sort_values('Year')
                country_subset['growth_rate'] = country_subset['GDP per capita'].pct_change() * 100
                
                # Remove extreme outliers for better visualization
                growth_data = country_subset['growth_rate'].dropna()
                q1, q3 = growth_data.quantile([0.05, 0.95])
                filtered_growth = country_subset[
                    (country_subset['growth_rate'] >= q1) & 
                    (country_subset['growth_rate'] <= q3)
                ]
                
                if not filtered_growth.empty:
                    ax3.plot(filtered_growth['Year'], filtered_growth['growth_rate'], 
                           label=country, alpha=0.7, color=colors[i])
                           
        ax3.set_title('GDP per Capita Growth Rates')
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Growth Rate (%)')
        ax3.axhline(y=0, color='black', linestyle='--', alpha=0.5)
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Relative comparison (ratio to base year or country)
        ax4 = axes[1, 1]
        
        # Use the first country as base for comparison
        base_country = countries[0]
        base_data = plot_data[plot_data['Entity'] == base_country]
        
        if not base_data.empty:
            for i, country in enumerate(countries):
                country_subset = plot_data[plot_data['Entity'] == country]
                if not country_subset.empty:
                    # Find common years for comparison
                    common_years = set(base_data['Year']) & set(country_subset['Year'])
                    if common_years:
                        common_years = sorted(list(common_years))
                        
                        base_values = base_data[base_data['Year'].isin(common_years)].set_index('Year')['GDP per capita']
                        country_values = country_subset[country_subset['Year'].isin(common_years)].set_index('Year')['GDP per capita']
                        
                        ratio = country_values / base_values
                        
                        ax4.plot(common_years, ratio, label=f'{country} / {base_country}', 
                               linewidth=2, alpha=0.8, color=colors[i])
                               
        ax4.set_title(f'Relative GDP per Capita (vs {base_country})')
        ax4.set_xlabel('Year')
        ax4.set_ylabel('Ratio')
        ax4.axhline(y=1, color='black', linestyle='--', alpha=0.5)
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
            
        plt.show()
        
    def calculate_growth_statistics(self, countries=None, start_year=None, end_year=None):
        """
        Calculate growth statistics for specified countries and time period
        
        Args:
            countries (list): List of countries to analyze
            start_year (int): Start year for analysis
            end_year (int): End year for analysis
            
        Returns:
            pd.DataFrame: Growth statistics summary
        """
        if self.processed_data.empty:
            print("No processed data available.")
            return pd.DataFrame()
            
        if countries is None:
            countries = list(self.country_data.keys())
            
        results = []
        
        for country in countries:
            country_data = self.get_country_data(country)
            if country_data.empty:
                continue
                
            # Filter by year range
            if start_year:
                country_data = country_data[country_data['Year'] >= start_year]
            if end_year:
                country_data = country_data[country_data['Year'] <= end_year]
                
            if len(country_data) < 2:
                continue
                
            country_data = country_data.sort_values('Year')
            
            # Calculate statistics
            start_gdp = country_data['GDP per capita'].iloc[0]
            end_gdp = country_data['GDP per capita'].iloc[-1]
            start_year_actual = country_data['Year'].iloc[0]
            end_year_actual = country_data['Year'].iloc[-1]
            
            # Compound annual growth rate
            years_span = end_year_actual - start_year_actual
            if years_span > 0:
                cagr = ((end_gdp / start_gdp) ** (1/years_span) - 1) * 100
            else:
                cagr = 0
                
            # Average annual growth rate
            country_data['growth_rate'] = country_data['GDP per capita'].pct_change() * 100
            avg_growth = country_data['growth_rate'].mean()
            
            # Volatility (standard deviation of growth rates)
            volatility = country_data['growth_rate'].std()
            
            results.append({
                'Country': country,
                'Start Year': start_year_actual,
                'End Year': end_year_actual,
                'Start GDP per Capita': start_gdp,
                'End GDP per Capita': end_gdp,
                'Total Growth (%)': ((end_gdp / start_gdp - 1) * 100),
                'CAGR (%)': cagr,
                'Avg Annual Growth (%)': avg_growth,
                'Growth Volatility (%)': volatility,
                'Data Points': len(country_data)
            })
            
        return pd.DataFrame(results)
        
    def generate_summary_statistics(self, countries=None):
        """Generate comprehensive summary statistics"""
        if self.processed_data.empty:
            print("No processed data available.")
            return
            
        if countries is None:
            countries = list(self.country_data.keys())
            
        print("\n" + "="*70)
        print("GDP PER CAPITA SUMMARY STATISTICS")
        print("="*70)
        
        # Overall statistics
        print(f"\nTotal records: {len(self.processed_data)}")
        print(f"Countries analyzed: {len(countries)}")
        print(f"Year range: {self.processed_data['Year'].min()} - {self.processed_data['Year'].max()}")
        
        # Country-wise statistics
        print("\nCOUNTRY-WISE STATISTICS:")
        print("-" * 50)
        
        for country in countries:
            country_data = self.get_country_data(country)
            if not country_data.empty:
                print(f"\n{country}:")
                print(f"  Records: {len(country_data)}")
                print(f"  Year range: {country_data['Year'].min()} - {country_data['Year'].max()}")
                print(f"  GDP per capita range: ${country_data['GDP per capita'].min():.0f} - ${country_data['GDP per capita'].max():.0f}")
                print(f"  Average GDP per capita: ${country_data['GDP per capita'].mean():.0f}")
                print(f"  Median GDP per capita: ${country_data['GDP per capita'].median():.0f}")
                
                # Calculate growth if enough data points
                if len(country_data) > 1:
                    start_gdp = country_data['GDP per capita'].iloc[0]
                    end_gdp = country_data['GDP per capita'].iloc[-1]
                    total_growth = ((end_gdp / start_gdp - 1) * 100)
                    print(f"  Total growth: {total_growth:.1f}%")
                    
        # Growth analysis for recent periods
        periods = [
            (1950, 2020, "Post-WWII Era"),
            (1990, 2020, "Recent Decades"),
            (2000, 2020, "21st Century")
        ]
        
        print("\nGROWTH ANALYSIS BY PERIOD:")
        print("-" * 35)
        
        for start_year, end_year, period_name in periods:
            print(f"\n{period_name} ({start_year}-{end_year}):")
            
            growth_stats = self.calculate_growth_statistics(countries, start_year, end_year)
            if not growth_stats.empty:
                for _, row in growth_stats.iterrows():
                    if row['Data Points'] > 5:  # Only show if sufficient data
                        print(f"  {row['Country']}: {row['CAGR (%)']:.2f}% CAGR")
                        
    def export_data(self, countries=None, filename="gdp_per_capita_data.csv"):
        """
        Export processed data to CSV
        
        Args:
            countries (list): List of countries to export
            filename (str): Output filename
        """
        if self.processed_data.empty:
            print("No processed data to export.")
            return
            
        if countries is None:
            export_data = self.processed_data.copy()
        else:
            export_data = self.processed_data[self.processed_data['Entity'].isin(countries)].copy()
            
        if not export_data.empty:
            export_data.to_csv(filename, index=False)
            print(f"Data exported to {filename}")
            print(f"Exported {len(export_data)} records for {len(export_data['Entity'].unique())} countries")
        else:
            print("No data to export for specified countries")


def main():
    """Main function to demonstrate the GDP per capita dataloader"""
    print("GDP per Capita Data Loader - Maddison Project Database")
    print("=" * 60)
    
    # Initialize the dataloader
    loader = GDPPerCapitaDataLoader()
    
    # Load data
    loader.load_data()
    
    # Process data for specific countries (example with major economies)
    example_countries = ['United States', 'United Kingdom', 'Germany', 'France', 'Japan']
    loader.process_data(countries=example_countries)
    
    # Generate summary statistics
    loader.generate_summary_statistics()
    
    # Create comparison plots
    if not loader.processed_data.empty:
        loader.plot_comparison(
            countries=example_countries,
            start_year=1950,
            save_path="gdp_per_capita_comparison.png"
        )
        
        # Export data
        loader.export_data(countries=example_countries)
        
        # Show growth statistics
        print("\nGROWTH STATISTICS (1950-2020):")
        print("-" * 40)
        growth_stats = loader.calculate_growth_statistics(
            countries=example_countries, 
            start_year=1950, 
            end_year=2020
        )
        if not growth_stats.empty:
            print(growth_stats.to_string(index=False))
    else:
        print("No data was successfully processed.")


if __name__ == "__main__":
    main()