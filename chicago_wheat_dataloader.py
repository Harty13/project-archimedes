import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

class ChicagoWheatDataLoader:
    """
    Dataloader for Chicago wheat prices (1841-1960) and UK grain price comparison
    """
    
    def __init__(self):
        self.chicago_data = pd.DataFrame()
        self.uk_data = pd.DataFrame()
        self.combined_data = pd.DataFrame()
        
    def load_chicago_wheat_data(self, file_path="data/m04001a_wheat_chicago_1841_1960.dat"):
        """Load Chicago wheat price data from the .dat file"""
        print("Loading Chicago wheat price data...")
        
        try:
            # Read the data file
            data = []
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) >= 3:
                        year = int(parts[0])
                        month = int(parts[1])
                        price_str = parts[2]
                        
                        # Handle missing values (represented as '.')
                        if price_str != '.':
                            price = float(price_str)
                            data.append({
                                'year': year,
                                'month': month,
                                'price': price,
                                'date': datetime(year, month, 1)
                            })
            
            # Convert to DataFrame
            self.chicago_data = pd.DataFrame(data)
            
            # Add additional columns
            self.chicago_data['country'] = 'US'
            self.chicago_data['region'] = 'Chicago'
            self.chicago_data['commodity'] = 'Wheat'
            self.chicago_data['dataset'] = 'chicago_wheat'
            
            print(f"Successfully loaded {len(self.chicago_data)} Chicago wheat price records")
            print(f"Date range: {self.chicago_data['year'].min()} - {self.chicago_data['year'].max()}")
            print(f"Price range: ${self.chicago_data['price'].min():.2f} - ${self.chicago_data['price'].max():.2f}")
            
        except Exception as e:
            print(f"Error loading Chicago wheat data: {e}")
            
    def load_uk_grain_data(self):
        """Load UK grain data from the dataverse files"""
        print("\nLoading UK grain price data...")
        
        data_dir = Path("data/dataverse_files")
        all_uk_data = []
        
        # Load England Grain Data (1841-1929)
        england1_path = data_dir / "England Grain" / "englandgrain1.xls"
        if england1_path.exists():
            try:
                df1 = pd.read_excel(england1_path)
                
                if len(df1.columns) >= 2:
                    year_col = df1.columns[0]
                    price_cols = df1.columns[1:]
                    
                    # Process monthly data
                    for _, row in df1.iterrows():
                        year = pd.to_numeric(row[year_col], errors='coerce')
                        if pd.isna(year) or year < 1800:
                            continue
                            
                        for i, col in enumerate(price_cols):
                            price = pd.to_numeric(row[col], errors='coerce')
                            if not pd.isna(price):
                                # Map column names to months (assuming September to August)
                                month_mapping = {
                                    'September': 9, 'October': 10, 'November': 11, 'December': 12,
                                    'January': 1, 'February': 2, 'March': 3, 'April': 4,
                                    'May': 5, 'June': 6, 'July': 7, 'August': 8
                                }
                                month = month_mapping.get(col, i + 1)
                                
                                all_uk_data.append({
                                    'year': int(year),
                                    'month': month,
                                    'price': price,
                                    'date': datetime(int(year), month, 1),
                                    'country': 'UK',
                                    'region': 'England',
                                    'commodity': 'Grain',
                                    'dataset': 'england_grain_1841_1929'
                                })
                                
                print(f"Loaded England grain data (1841-1929)")
                
            except Exception as e:
                print(f"Error loading England grain data: {e}")
        
        # Load England Grain Data (1929-1955)
        england2_path = data_dir / "England Grain" / "englandgrain2.xls"
        if england2_path.exists():
            try:
                df2 = pd.read_excel(england2_path)
                
                if len(df2.columns) >= 2:
                    year_col = df2.columns[0]
                    price_cols = df2.columns[1:]
                    
                    for _, row in df2.iterrows():
                        year = pd.to_numeric(row[year_col], errors='coerce')
                        if pd.isna(year) or year < 1900:
                            continue
                            
                        for i, col in enumerate(price_cols):
                            price = pd.to_numeric(row[col], errors='coerce')
                            if not pd.isna(price):
                                month_mapping = {
                                    'September': 9, 'October': 10, 'November': 11, 'December': 12,
                                    'January': 1, 'February': 2, 'March': 3, 'April': 4,
                                    'May': 5, 'June': 6, 'July': 7, 'August': 8
                                }
                                month = month_mapping.get(col, i + 1)
                                
                                all_uk_data.append({
                                    'year': int(year),
                                    'month': month,
                                    'price': price,
                                    'date': datetime(int(year), month, 1),
                                    'country': 'UK',
                                    'region': 'England',
                                    'commodity': 'Grain',
                                    'dataset': 'england_grain_1929_1955'
                                })
                                
                print(f"Loaded England grain data (1929-1955)")
                
            except Exception as e:
                print(f"Error loading England grain data (1929-1955): {e}")
        
        # Load Winchester data
        winchester_path = data_dir / "Winchester" / "winchester.xls"
        if winchester_path.exists():
            try:
                df_win = pd.read_excel(winchester_path)
                
                if len(df_win.columns) >= 2:
                    year_col = df_win.columns[0]
                    price_cols = df_win.columns[1:]
                    
                    for _, row in df_win.iterrows():
                        year = pd.to_numeric(row[year_col], errors='coerce')
                        if pd.isna(year) or year < 1600 or year > 1900:
                            continue
                            
                        # Average the seasonal prices for annual comparison
                        prices = []
                        for col in price_cols:
                            price = pd.to_numeric(row[col], errors='coerce')
                            if not pd.isna(price):
                                prices.append(price)
                        
                        if prices:
                            avg_price = np.mean(prices)
                            all_uk_data.append({
                                'year': int(year),
                                'month': 6,  # Use June as representative month
                                'price': avg_price,
                                'date': datetime(int(year), 6, 1),
                                'country': 'UK',
                                'region': 'Winchester',
                                'commodity': 'Wheat',
                                'dataset': 'winchester'
                            })
                            
                print(f"Loaded Winchester data")
                
            except Exception as e:
                print(f"Error loading Winchester data: {e}")
        
        if all_uk_data:
            self.uk_data = pd.DataFrame(all_uk_data)
            print(f"Successfully loaded {len(self.uk_data)} UK grain price records")
        else:
            print("No UK data could be loaded")
            
    def combine_data(self):
        """Combine Chicago and UK data for comparison"""
        print("\nCombining Chicago and UK data...")
        
        all_data = []
        
        # Add Chicago data
        if not self.chicago_data.empty:
            chicago_copy = self.chicago_data.copy()
            chicago_copy['grain_price'] = chicago_copy['price']
            all_data.append(chicago_copy)
            
        # Add UK data
        if not self.uk_data.empty:
            uk_copy = self.uk_data.copy()
            uk_copy['grain_price'] = uk_copy['price']
            all_data.append(uk_copy)
            
        if all_data:
            self.combined_data = pd.concat(all_data, ignore_index=True)
            print(f"Combined dataset contains {len(self.combined_data)} records")
            print(f"Countries: {self.combined_data['country'].unique()}")
            print(f"Year range: {self.combined_data['year'].min()} - {self.combined_data['year'].max()}")
        else:
            print("No data to combine")
            
    def plot_comparison(self, save_path=None):
        """Create comprehensive comparison plots"""
        if self.combined_data.empty:
            print("No data to plot. Please load and combine data first.")
            return
            
        print("\nCreating comparison plots...")
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Historical Grain Prices: Chicago Wheat vs UK Grain (1841-1960)', 
                     fontsize=16, fontweight='bold')
        
        # 1. Monthly time series comparison
        ax1 = axes[0, 0]
        
        # Chicago data
        chicago_subset = self.combined_data[self.combined_data['country'] == 'US']
        if not chicago_subset.empty:
            ax1.plot(chicago_subset['date'], chicago_subset['grain_price'], 
                    label='Chicago Wheat', alpha=0.7, color='red', linewidth=1)
        
        # UK data
        uk_subset = self.combined_data[self.combined_data['country'] == 'UK']
        if not uk_subset.empty:
            # Plot different UK regions
            for region in uk_subset['region'].unique():
                region_data = uk_subset[uk_subset['region'] == region]
                ax1.plot(region_data['date'], region_data['grain_price'], 
                        label=f'UK {region}', alpha=0.7, linewidth=1)
        
        ax1.set_title('Monthly Price Comparison')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Price (cents/shillings per unit)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Annual averages comparison
        ax2 = axes[0, 1]
        
        # Calculate annual averages
        annual_data = self.combined_data.groupby(['year', 'country'])['grain_price'].mean().reset_index()
        
        chicago_annual = annual_data[annual_data['country'] == 'US']
        uk_annual = annual_data[annual_data['country'] == 'UK']
        
        if not chicago_annual.empty:
            ax2.plot(chicago_annual['year'], chicago_annual['grain_price'], 
                    label='Chicago Wheat (Annual Avg)', linewidth=2, color='red', marker='o', markersize=3)
        
        if not uk_annual.empty:
            ax2.plot(uk_annual['year'], uk_annual['grain_price'], 
                    label='UK Grain (Annual Avg)', linewidth=2, color='blue', marker='s', markersize=3)
        
        ax2.set_title('Annual Average Prices')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Average Price')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # 3. Price volatility comparison (rolling standard deviation)
        ax3 = axes[1, 0]
        
        # Calculate 5-year rolling volatility
        chicago_volatility = []
        uk_volatility = []
        years = []
        
        for year in range(1845, 1956, 2):  # Every 2 years
            year_range = (self.combined_data['year'] >= year - 2) & (self.combined_data['year'] <= year + 2)
            
            chicago_subset = self.combined_data[(self.combined_data['country'] == 'US') & year_range]
            uk_subset = self.combined_data[(self.combined_data['country'] == 'UK') & year_range]
            
            if len(chicago_subset) > 5:
                chicago_vol = chicago_subset['grain_price'].std()
                chicago_volatility.append(chicago_vol)
            else:
                chicago_volatility.append(np.nan)
                
            if len(uk_subset) > 5:
                uk_vol = uk_subset['grain_price'].std()
                uk_volatility.append(uk_vol)
            else:
                uk_volatility.append(np.nan)
                
            years.append(year)
        
        ax3.plot(years, chicago_volatility, label='Chicago Volatility', 
                linewidth=2, alpha=0.8, color='red')
        ax3.plot(years, uk_volatility, label='UK Volatility', 
                linewidth=2, alpha=0.8, color='blue')
        
        ax3.set_title('Price Volatility (5-year rolling std dev)')
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Price Standard Deviation')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Decade comparison
        ax4 = axes[1, 1]
        
        # Add decade column
        self.combined_data['decade'] = (self.combined_data['year'] // 10) * 10
        decade_data = self.combined_data.groupby(['country', 'decade'])['grain_price'].mean().reset_index()
        
        decades = sorted(decade_data['decade'].unique())
        x_pos = np.arange(len(decades))
        width = 0.35
        
        chicago_decade = decade_data[decade_data['country'] == 'US']
        uk_decade = decade_data[decade_data['country'] == 'UK']
        
        chicago_prices = [chicago_decade[chicago_decade['decade'] == d]['grain_price'].iloc[0] 
                         if len(chicago_decade[chicago_decade['decade'] == d]) > 0 else 0 for d in decades]
        uk_prices = [uk_decade[uk_decade['decade'] == d]['grain_price'].iloc[0] 
                    if len(uk_decade[uk_decade['decade'] == d]) > 0 else 0 for d in decades]
        
        ax4.bar(x_pos - width/2, chicago_prices, width, label='Chicago', alpha=0.8, color='red')
        ax4.bar(x_pos + width/2, uk_prices, width, label='UK', alpha=0.8, color='blue')
        
        ax4.set_title('Average Prices by Decade')
        ax4.set_xlabel('Decade')
        ax4.set_ylabel('Average Price')
        ax4.set_xticks(x_pos)
        ax4.set_xticklabels([f"{int(d)}s" for d in decades], rotation=45)
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        
        plt.show()
        
    def generate_summary_statistics(self):
        """Generate detailed summary statistics"""
        if self.combined_data.empty:
            print("No data available for summary statistics")
            return
            
        print("\n" + "="*70)
        print("CHICAGO WHEAT vs UK GRAIN PRICE COMPARISON")
        print("="*70)
        
        # Overall statistics
        print(f"\nTotal records: {len(self.combined_data)}")
        print(f"Year range: {self.combined_data['year'].min()} - {self.combined_data['year'].max()}")
        print(f"Countries: {', '.join(self.combined_data['country'].unique())}")
        
        # Country-wise statistics
        print("\nCOUNTRY-WISE STATISTICS:")
        print("-" * 40)
        
        for country in self.combined_data['country'].unique():
            country_data = self.combined_data[self.combined_data['country'] == country]
            print(f"\n{country}:")
            print(f"  Records: {len(country_data)}")
            print(f"  Year range: {country_data['year'].min()} - {country_data['year'].max()}")
            print(f"  Regions: {', '.join(country_data['region'].unique())}")
            print(f"  Average price: {country_data['grain_price'].mean():.2f}")
            print(f"  Price std dev: {country_data['grain_price'].std():.2f}")
            print(f"  Min price: {country_data['grain_price'].min():.2f}")
            print(f"  Max price: {country_data['grain_price'].max():.2f}")
            
        # Period analysis
        print("\nPERIOD ANALYSIS:")
        print("-" * 20)
        
        periods = [
            (1841, 1860, "Pre-Civil War"),
            (1861, 1865, "Civil War"),
            (1866, 1890, "Post-Civil War"),
            (1891, 1914, "Pre-WWI"),
            (1915, 1918, "WWI"),
            (1919, 1929, "Post-WWI"),
            (1930, 1939, "Great Depression"),
            (1940, 1945, "WWII")
        ]
        
        for start_year, end_year, period_name in periods:
            period_data = self.combined_data[
                (self.combined_data['year'] >= start_year) & 
                (self.combined_data['year'] <= end_year)
            ]
            
            if not period_data.empty:
                print(f"\n{period_name} ({start_year}-{end_year}):")
                
                chicago_period = period_data[period_data['country'] == 'US']
                uk_period = period_data[period_data['country'] == 'UK']
                
                if not chicago_period.empty:
                    print(f"  Chicago avg: {chicago_period['grain_price'].mean():.2f}")
                if not uk_period.empty:
                    print(f"  UK avg: {uk_period['grain_price'].mean():.2f}")
                    
        # Correlation analysis
        print("\nCORRELATION ANALYSIS:")
        print("-" * 25)
        
        # Calculate annual averages for correlation
        annual_chicago = self.combined_data[self.combined_data['country'] == 'US'].groupby('year')['grain_price'].mean()
        annual_uk = self.combined_data[self.combined_data['country'] == 'UK'].groupby('year')['grain_price'].mean()
        
        # Find common years
        common_years = set(annual_chicago.index) & set(annual_uk.index)
        if common_years:
            chicago_common = annual_chicago[list(common_years)]
            uk_common = annual_uk[list(common_years)]
            
            correlation = chicago_common.corr(uk_common)
            print(f"Price correlation (annual averages): {correlation:.3f}")
            print(f"Common years analyzed: {len(common_years)}")
        else:
            print("No overlapping years for correlation analysis")
            
    def export_data(self, filename="chicago_uk_grain_prices.csv"):
        """Export combined data to CSV"""
        if not self.combined_data.empty:
            self.combined_data.to_csv(filename, index=False)
            print(f"\nData exported to {filename}")
        else:
            print("No data to export")


def main():
    """Main function to demonstrate the Chicago wheat dataloader"""
    print("Chicago Wheat vs UK Grain Price Comparison")
    print("=" * 50)
    
    # Initialize the dataloader
    loader = ChicagoWheatDataLoader()
    
    # Load Chicago wheat data
    loader.load_chicago_wheat_data()
    
    # Load UK grain data
    loader.load_uk_grain_data()
    
    # Combine data
    loader.combine_data()
    
    # Generate summary statistics
    loader.generate_summary_statistics()
    
    # Create plots
    if not loader.combined_data.empty:
        loader.plot_comparison(save_path="chicago_uk_grain_comparison.png")
        
        # Export data
        loader.export_data()
    else:
        print("No data was successfully loaded.")


if __name__ == "__main__":
    main()
