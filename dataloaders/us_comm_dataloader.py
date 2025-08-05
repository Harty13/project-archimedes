import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from pathlib import Path
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

class USCommDataLoader:
    """
    A dataloader for extracting and analyzing US commodity price index data
    from Charleston wholesale prices (1732-1861)
    Base: 1818-42 = 100
    """
    
    def __init__(self, csv_file_path="us_comm_price_index_long.csv"):
        self.csv_file_path = Path(csv_file_path)
        self.raw_data = None
        self.processed_data = pd.DataFrame()
        
    def load_data(self):
        """Load US commodity price index data from CSV file"""
        print(f"Loading US commodity price index data from {self.csv_file_path}...")
        
        try:
            self.raw_data = pd.read_csv(self.csv_file_path)
            print(f"Successfully loaded {len(self.raw_data)} monthly observations")
            return True
            
        except FileNotFoundError:
            print(f"Error: File {self.csv_file_path} not found")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def process_data(self):
        """Process raw CSV data into a structured DataFrame with additional metrics"""
        if self.raw_data is None:
            print("No raw data available. Please load data first.")
            return
            
        print("Processing US commodity price index data...")
        
        # Start with the raw data
        df = self.raw_data.copy()
        
        # Basic data cleaning
        df = self._clean_data(df)
        
        # Add metadata
        df['source'] = 'Charleston_Wholesale_Prices'
        df['country'] = 'United States'
        df['location'] = 'Charleston, SC'
        df['base_period'] = '1818-1842'
        df['data_type'] = 'Weighted_All_Commodity_Index'
        
        # Calculate derived metrics
        df = self._calculate_derived_metrics(df)
        
        self.processed_data = df
        print(f"Processed data shape: {self.processed_data.shape}")
        print(f"Date range: {self.processed_data['Date'].min()} to {self.processed_data['Date'].max()}")
        
    def _clean_data(self, df):
        """Clean and validate the data"""
        print("Cleaning data...")
        
        # Ensure proper data types
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        df['Month'] = pd.to_numeric(df['Month'], errors='coerce')
        df['Price_Index'] = pd.to_numeric(df['Price_Index'], errors='coerce')
        
        # Remove rows with invalid data
        df = df.dropna(subset=['Year', 'Month', 'Price_Index'])
        
        # Create proper datetime column
        df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(day=1))
        
        # Sort by date
        df = df.sort_values('Date').reset_index(drop=True)
        
        # Filter reasonable price index values (should be positive)
        df = df[df['Price_Index'] > 0]
        
        print(f"Data cleaned. Shape: {df.shape}")
        return df
    
    def _calculate_derived_metrics(self, df):
        """Calculate derived metrics from the price index data"""
        print("Calculating derived metrics...")
        
        # Calculate year-over-year change
        df['YoY_Change'] = df.groupby('Month')['Price_Index'].pct_change(periods=12) * 100
        
        # Calculate month-over-month change
        df['MoM_Change'] = df['Price_Index'].pct_change() * 100
        
        # Calculate rolling averages
        df['Price_Index_3M_MA'] = df['Price_Index'].rolling(window=3, center=True).mean()
        df['Price_Index_12M_MA'] = df['Price_Index'].rolling(window=12, center=True).mean()
        
        # Calculate volatility (rolling standard deviation)
        df['Price_Volatility_12M'] = df['Price_Index'].rolling(window=12, center=True).std()
        
        # Seasonal adjustment (simple detrending)
        monthly_means = df.groupby('Month')['Price_Index'].mean()
        overall_mean = df['Price_Index'].mean()
        seasonal_factors = monthly_means / overall_mean
        df['Seasonal_Factor'] = df['Month'].map(seasonal_factors)
        df['Seasonally_Adjusted_Index'] = df['Price_Index'] / df['Seasonal_Factor']
        
        # Add decade classification
        df['Decade'] = (df['Year'] // 10) * 10
        
        # Add period classifications based on US economic history
        df['Historical_Period'] = df['Year'].apply(self._classify_historical_period)
        
        # Add war period indicators
        df['War_Period'] = df['Year'].apply(self._identify_war_periods)
        
        # Calculate relative to base period (1818-1842)
        base_period_data = df[(df['Year'] >= 1818) & (df['Year'] <= 1842)]
        if not base_period_data.empty:
            base_mean = base_period_data['Price_Index'].mean()
            df['Relative_to_Base'] = df['Price_Index'] / base_mean
        else:
            df['Relative_to_Base'] = df['Price_Index'] / 100  # Assume base = 100
        
        return df
    
    def _classify_historical_period(self, year):
        """Classify years into US historical periods"""
        if year < 1760:
            return 'Colonial_Early'
        elif year < 1776:
            return 'Pre_Revolution'
        elif year < 1789:
            return 'Revolutionary_War_Era'
        elif year < 1812:
            return 'Early_Republic'
        elif year < 1815:
            return 'War_of_1812'
        elif year < 1837:
            return 'Era_of_Good_Feelings'
        elif year < 1841:
            return 'Panic_of_1837'
        elif year < 1861:
            return 'Antebellum'
        else:
            return 'Civil_War_Era'
    
    def _identify_war_periods(self, year):
        """Identify major war periods that might affect prices"""
        if 1775 <= year <= 1783:
            return 'Revolutionary_War'
        elif 1812 <= year <= 1815:
            return 'War_of_1812'
        elif 1846 <= year <= 1848:
            return 'Mexican_American_War'
        elif year >= 1861:
            return 'Civil_War_Beginning'
        else:
            return 'Peacetime'
    
    def get_data_summary(self):
        """Generate comprehensive summary statistics"""
        if self.processed_data.empty:
            print("No processed data available. Please load and process data first.")
            return
        
        print("\n" + "="*70)
        print("US COMMODITY PRICE INDEX DATA SUMMARY")
        print("="*70)
        
        df = self.processed_data
        
        # Basic statistics
        print(f"\nBasic Statistics:")
        print(f"Total monthly observations: {len(df)}")
        print(f"Date range: {df['Date'].min().strftime('%Y-%m')} to {df['Date'].max().strftime('%Y-%m')}")
        print(f"Time span: {df['Year'].max() - df['Year'].min()} years")
        print(f"Base period: {df['base_period'].iloc[0]}")
        
        # Price index statistics
        print(f"\nPrice Index Statistics:")
        print(f"Mean: {df['Price_Index'].mean():.1f}")
        print(f"Median: {df['Price_Index'].median():.1f}")
        print(f"Standard Deviation: {df['Price_Index'].std():.1f}")
        print(f"Range: {df['Price_Index'].min():.1f} - {df['Price_Index'].max():.1f}")
        
        # Data completeness by month
        print(f"\nData Completeness by Month:")
        print("-" * 35)
        monthly_counts = df.groupby('Month_Name').size()
        total_possible = df['Year'].nunique()  # Max possible per month
        
        for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            if month in monthly_counts.index:
                count = monthly_counts[month]
                percentage = (count / total_possible) * 100
                print(f"{month:4}: {count:3d}/{total_possible} ({percentage:5.1f}%)")
        
        # Period-wise statistics
        print(f"\nHistorical Period Statistics:")
        print("-" * 40)
        
        period_stats = df.groupby('Historical_Period').agg({
            'Price_Index': ['count', 'mean', 'std'],
            'Year': ['min', 'max']
        }).round(1)
        
        print(period_stats)
        
        # War vs Peace comparison
        print(f"\nWar vs Peace Period Comparison:")
        print("-" * 35)
        
        war_data = df[df['War_Period'] != 'Peacetime']
        peace_data = df[df['War_Period'] == 'Peacetime']
        
        if not war_data.empty and not peace_data.empty:
            print(f"War periods average: {war_data['Price_Index'].mean():.1f}")
            print(f"Peace periods average: {peace_data['Price_Index'].mean():.1f}")
            print(f"War premium: {((war_data['Price_Index'].mean() / peace_data['Price_Index'].mean()) - 1) * 100:.1f}%")
    
    def plot_price_analysis(self, save_path=None):
        """Create comprehensive plots of US commodity price index data"""
        if self.processed_data.empty:
            print("No processed data available for plotting.")
            return
        
        df = self.processed_data
        
        # Set up plotting style
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('US Commodity Price Index Analysis - Charleston (1732-1861)', 
                    fontsize=16, fontweight='bold')
        
        # 1. Price index over time with trend
        ax1 = axes[0, 0]
        ax1.plot(df['Date'], df['Price_Index'], alpha=0.6, linewidth=1, label='Monthly Index')
        ax1.plot(df['Date'], df['Price_Index_12M_MA'], linewidth=2, color='red', label='12-Month MA')
        
        # Highlight war periods
        war_periods = df[df['War_Period'] != 'Peacetime']
        if not war_periods.empty:
            for war in war_periods['War_Period'].unique():
                war_data = war_periods[war_periods['War_Period'] == war]
                ax1.axvspan(war_data['Date'].min(), war_data['Date'].max(), 
                           alpha=0.2, color='red', label=f'{war}' if war == war_periods['War_Period'].unique()[0] else "")
        
        ax1.set_title('Price Index Over Time (Base: 1818-42 = 100)')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Price Index')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Seasonal patterns
        ax2 = axes[0, 1]
        monthly_avg = df.groupby('Month')['Price_Index'].mean()
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        bars = ax2.bar(range(1, 13), monthly_avg.values, alpha=0.7, color='skyblue')
        ax2.set_title('Average Price Index by Month')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Average Price Index')
        ax2.set_xticks(range(1, 13))
        ax2.set_xticklabels(month_names)
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.0f}', ha='center', va='bottom')
        
        # 3. Historical period comparison
        ax3 = axes[1, 0]
        period_avg = df.groupby('Historical_Period')['Price_Index'].mean().sort_index()
        
        bars = ax3.bar(range(len(period_avg)), period_avg.values, alpha=0.7, color='green')
        ax3.set_title('Average Price Index by Historical Period')
        ax3.set_ylabel('Average Price Index')
        ax3.set_xticks(range(len(period_avg)))
        ax3.set_xticklabels(period_avg.index, rotation=45, ha='right')
        ax3.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.0f}', ha='center', va='bottom')
        
        # 4. Price volatility over time
        ax4 = axes[1, 1]
        volatility_data = df[df['Price_Volatility_12M'].notna()]
        ax4.plot(volatility_data['Date'], volatility_data['Price_Volatility_12M'], 
                color='purple', alpha=0.7, linewidth=2)
        ax4.fill_between(volatility_data['Date'], volatility_data['Price_Volatility_12M'], 
                        alpha=0.3, color='purple')
        
        ax4.set_title('Price Volatility (12-month rolling std)')
        ax4.set_xlabel('Year')
        ax4.set_ylabel('Price Standard Deviation')
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        
        plt.show()
    
    def get_period_analysis(self, period_type='Historical_Period'):
        """Get detailed analysis by historical period"""
        if self.processed_data.empty:
            print("No processed data available.")
            return None
        
        df = self.processed_data
        
        if period_type not in df.columns:
            print(f"Period type '{period_type}' not found in data.")
            return None
        
        analysis = {}
        
        for period in df[period_type].unique():
            period_data = df[df[period_type] == period]
            
            analysis[period] = {
                'observations': len(period_data),
                'year_range': (period_data['Year'].min(), period_data['Year'].max()),
                'avg_price_index': period_data['Price_Index'].mean(),
                'price_volatility': period_data['Price_Index'].std(),
                'min_price': period_data['Price_Index'].min(),
                'max_price': period_data['Price_Index'].max(),
                'avg_yoy_change': period_data['YoY_Change'].mean() if 'YoY_Change' in period_data.columns else None
            }
        
        return analysis
    
    def export_processed_data(self, filename="processed_us_comm_data.csv"):
        """Export processed data to CSV"""
        if not self.processed_data.empty:
            self.processed_data.to_csv(filename, index=False)
            print(f"Processed data exported to {filename}")
        else:
            print("No processed data to export")
    
    def compare_with_modern_baseline(self, modern_baseline=100):
        """Compare historical prices with a modern baseline"""
        if self.processed_data.empty:
            print("No processed data available.")
            return
        
        df = self.processed_data
        
        print(f"\nComparison with Modern Baseline (={modern_baseline}):")
        print("-" * 50)
        
        # Calculate what historical prices would be in modern terms
        # Assuming the base period (1818-42) represents a certain purchasing power
        base_period_avg = df[(df['Year'] >= 1818) & (df['Year'] <= 1842)]['Price_Index'].mean()
        
        if not np.isnan(base_period_avg):
            conversion_factor = modern_baseline / base_period_avg
            
            print(f"Base period (1818-42) average: {base_period_avg:.1f}")
            print(f"Conversion factor: {conversion_factor:.2f}")
            
            # Show some key periods in modern terms
            key_periods = ['Colonial_Early', 'Revolutionary_War_Era', 'War_of_1812', 'Antebellum']
            
            for period in key_periods:
                period_data = df[df['Historical_Period'] == period]
                if not period_data.empty:
                    historical_avg = period_data['Price_Index'].mean()
                    modern_equivalent = historical_avg * conversion_factor
                    print(f"{period:20}: {historical_avg:5.1f} → {modern_equivalent:5.1f}")


def main():
    """Main function to demonstrate the dataloader"""
    print("US Commodity Price Index Data Loader")
    print("=" * 45)
    
    # Initialize the dataloader
    loader = USCommDataLoader()
    
    # Load data
    if loader.load_data():
        # Process data
        loader.process_data()
        
        # Generate summary statistics
        loader.get_data_summary()
        
        # Create plots
        loader.plot_price_analysis(save_path="plots/us_comm_analysis.png")
        
        # Export processed data
        loader.export_processed_data()
        
        # Period analysis
        print("\n" + "="*50)
        print("HISTORICAL PERIOD ANALYSIS")
        print("="*50)
        period_analysis = loader.get_period_analysis()
        if period_analysis:
            for period, stats in period_analysis.items():
                print(f"\n{period}:")
                print(f"  Years: {stats['year_range'][0]}-{stats['year_range'][1]}")
                print(f"  Observations: {stats['observations']}")
                print(f"  Avg Price Index: {stats['avg_price_index']:.1f}")
                print(f"  Price Volatility: {stats['price_volatility']:.1f}")
                if stats['avg_yoy_change'] is not None:
                    print(f"  Avg YoY Change: {stats['avg_yoy_change']:.1f}%")
        
        # Modern comparison
        loader.compare_with_modern_baseline(100)
        
    else:
        print("Failed to load data. Please check the file path and format.")


if __name__ == "__main__":
    main()
