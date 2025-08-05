import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from pathlib import Path
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

class AgPriceDataLoader:
    """
    A dataloader for extracting and analyzing agricultural price data
    from the extracted PDF table data (1209-1914)
    """
    
    def __init__(self, json_file_path="agprice_table_raw.json"):
        self.json_file_path = Path(json_file_path)
        self.raw_data = None
        self.processed_data = pd.DataFrame()
        
    def load_data(self):
        """Load agricultural price data from JSON file"""
        print(f"Loading agricultural price data from {self.json_file_path}...")
        
        try:
            with open(self.json_file_path, 'r') as f:
                self.raw_data = json.load(f)
            
            print(f"Successfully loaded {len(self.raw_data)} records")
            return True
            
        except FileNotFoundError:
            print(f"Error: File {self.json_file_path} not found")
            return False
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format - {e}")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def process_data(self):
        """Process raw JSON data into a structured DataFrame"""
        if self.raw_data is None:
            print("No raw data available. Please load data first.")
            return
            
        print("Processing agricultural price data...")
        
        # Convert JSON data to DataFrame
        df = pd.DataFrame(self.raw_data)
        
        # Basic data cleaning
        df = self._clean_data(df)
        
        # Add metadata
        df['source'] = 'Agprice_table_PDF'
        df['country'] = 'England'  # Based on the historical context
        df['currency'] = 'shillings'
        df['period'] = 'Medieval_to_Modern'
        
        # Calculate derived metrics
        df = self._calculate_derived_metrics(df)
        
        self.processed_data = df
        print(f"Processed data shape: {self.processed_data.shape}")
        print(f"Year range: {self.processed_data['Year'].min()} - {self.processed_data['Year'].max()}")
        
    def _clean_data(self, df):
        """Clean and validate the data"""
        print("Cleaning data...")
        
        # Ensure Year is integer
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        
        # Remove rows with invalid years
        df = df.dropna(subset=['Year'])
        df = df[df['Year'].between(1200, 2000)]  # Reasonable year range
        
        # Convert price columns to numeric, replacing None/null with NaN
        price_columns = ['Wheat', 'Rye', 'Barley', 'Oats', 'Peas', 'Beans', 
                        'Potato', 'Hops', 'Net', 'Straw', 'Mustard', 'Saffron']
        
        for col in price_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Sort by year
        df = df.sort_values('Year').reset_index(drop=True)
        
        print(f"Data cleaned. Shape: {df.shape}")
        return df
    
    def _calculate_derived_metrics(self, df):
        """Calculate derived metrics from the price data"""
        print("Calculating derived metrics...")
        
        # Define grain categories
        grains = ['Wheat', 'Rye', 'Barley', 'Oats']
        legumes = ['Peas', 'Beans']
        other_crops = ['Potato', 'Hops', 'Net', 'Straw', 'Mustard', 'Saffron']
        
        # Calculate average grain price (main cereals)
        grain_cols = [col for col in grains if col in df.columns]
        if grain_cols:
            df['avg_grain_price'] = df[grain_cols].mean(axis=1, skipna=True)
        
        # Calculate average legume price
        legume_cols = [col for col in legumes if col in df.columns]
        if legume_cols:
            df['avg_legume_price'] = df[legume_cols].mean(axis=1, skipna=True)
        
        # Calculate price volatility (rolling standard deviation)
        window = 10  # 10-year rolling window
        if 'avg_grain_price' in df.columns:
            df['grain_price_volatility'] = df['avg_grain_price'].rolling(
                window=window, center=True, min_periods=5
            ).std()
        
        # Calculate price trends (rolling mean)
        if 'avg_grain_price' in df.columns:
            df['grain_price_trend'] = df['avg_grain_price'].rolling(
                window=20, center=True, min_periods=10
            ).mean()
        
        # Calculate relative prices (wheat as base)
        if 'Wheat' in df.columns:
            for col in ['Rye', 'Barley', 'Oats']:
                if col in df.columns:
                    df[f'{col}_relative_to_wheat'] = df[col] / df['Wheat']
        
        # Add century and period classifications
        df['century'] = (df['Year'] // 100) * 100
        df['period_classification'] = df['Year'].apply(self._classify_period)
        
        return df
    
    def _classify_period(self, year):
        """Classify years into historical periods"""
        if year < 1300:
            return 'High_Medieval'
        elif year < 1500:
            return 'Late_Medieval'
        elif year < 1700:
            return 'Early_Modern'
        elif year < 1800:
            return 'Industrial_Revolution'
        elif year < 1900:
            return 'Victorian'
        else:
            return 'Modern'
    
    def get_data_summary(self):
        """Generate comprehensive summary statistics"""
        if self.processed_data.empty:
            print("No processed data available. Please load and process data first.")
            return
        
        print("\n" + "="*60)
        print("AGRICULTURAL PRICE DATA SUMMARY")
        print("="*60)
        
        df = self.processed_data
        
        # Basic statistics
        print(f"\nBasic Statistics:")
        print(f"Total records: {len(df)}")
        print(f"Year range: {df['Year'].min()} - {df['Year'].max()}")
        print(f"Time span: {df['Year'].max() - df['Year'].min()} years")
        
        # Data completeness by commodity
        print(f"\nData Completeness by Commodity:")
        print("-" * 40)
        
        commodities = ['Wheat', 'Rye', 'Barley', 'Oats', 'Peas', 'Beans', 'Potato', 'Hops']
        for commodity in commodities:
            if commodity in df.columns:
                non_null_count = df[commodity].notna().sum()
                percentage = (non_null_count / len(df)) * 100
                print(f"{commodity:12}: {non_null_count:4d}/{len(df)} ({percentage:5.1f}%)")
        
        # Period-wise statistics
        print(f"\nPeriod-wise Statistics:")
        print("-" * 30)
        
        period_stats = df.groupby('period_classification').agg({
            'Year': ['count', 'min', 'max'],
            'avg_grain_price': ['mean', 'std']
        }).round(2)
        
        print(period_stats)
        
        # Price statistics for main commodities
        print(f"\nPrice Statistics (Main Commodities):")
        print("-" * 40)
        
        main_commodities = ['Wheat', 'Rye', 'Barley', 'Oats']
        for commodity in main_commodities:
            if commodity in df.columns and df[commodity].notna().sum() > 0:
                stats = df[commodity].describe()
                print(f"\n{commodity}:")
                print(f"  Mean: {stats['mean']:.3f}")
                print(f"  Std:  {stats['std']:.3f}")
                print(f"  Min:  {stats['min']:.3f}")
                print(f"  Max:  {stats['max']:.3f}")
    
    def plot_price_analysis(self, save_path=None):
        """Create comprehensive plots of agricultural price data"""
        if self.processed_data.empty:
            print("No processed data available for plotting.")
            return
        
        df = self.processed_data
        
        # Set up plotting style
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Historical Agricultural Prices Analysis (1209-1914)', 
                    fontsize=16, fontweight='bold')
        
        # 1. Main grain prices over time
        ax1 = axes[0, 0]
        main_grains = ['Wheat', 'Rye', 'Barley', 'Oats']
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
        
        for i, grain in enumerate(main_grains):
            if grain in df.columns:
                # Plot only non-null values
                grain_data = df[df[grain].notna()]
                if len(grain_data) > 0:
                    ax1.plot(grain_data['Year'], grain_data[grain], 
                            label=grain, alpha=0.7, linewidth=1.5, color=colors[i])
        
        ax1.set_title('Main Grain Prices Over Time')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Price (shillings)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(df['Year'].min(), df['Year'].max())
        
        # 2. Average grain price with trend
        ax2 = axes[0, 1]
        if 'avg_grain_price' in df.columns:
            # Plot average grain price
            avg_data = df[df['avg_grain_price'].notna()]
            ax2.plot(avg_data['Year'], avg_data['avg_grain_price'], 
                    label='Average Grain Price', alpha=0.6, color='blue')
            
            # Plot trend line
            if 'grain_price_trend' in df.columns:
                trend_data = df[df['grain_price_trend'].notna()]
                ax2.plot(trend_data['Year'], trend_data['grain_price_trend'], 
                        label='20-year Trend', linewidth=3, color='red')
        
        ax2.set_title('Average Grain Price and Long-term Trend')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Average Price (shillings)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # 3. Price volatility over time
        ax3 = axes[1, 0]
        if 'grain_price_volatility' in df.columns:
            volatility_data = df[df['grain_price_volatility'].notna()]
            ax3.plot(volatility_data['Year'], volatility_data['grain_price_volatility'], 
                    color='purple', alpha=0.7, linewidth=2)
            ax3.fill_between(volatility_data['Year'], volatility_data['grain_price_volatility'], 
                           alpha=0.3, color='purple')
        
        ax3.set_title('Price Volatility (10-year rolling std)')
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Price Standard Deviation')
        ax3.grid(True, alpha=0.3)
        
        # 4. Period-wise price comparison
        ax4 = axes[1, 1]
        if 'period_classification' in df.columns and 'avg_grain_price' in df.columns:
            period_data = df.groupby('period_classification')['avg_grain_price'].mean().sort_index()
            
            bars = ax4.bar(range(len(period_data)), period_data.values, 
                          alpha=0.7, color='green')
            ax4.set_xticks(range(len(period_data)))
            ax4.set_xticklabels(period_data.index, rotation=45, ha='right')
            
            # Add value labels on bars
            for i, bar in enumerate(bars):
                height = bar.get_height()
                if not np.isnan(height):
                    ax4.text(bar.get_x() + bar.get_width()/2., height,
                           f'{height:.2f}', ha='center', va='bottom')
        
        ax4.set_title('Average Grain Prices by Historical Period')
        ax4.set_ylabel('Average Price (shillings)')
        ax4.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        
        plt.show()
    
    def export_processed_data(self, filename="processed_agprice_data.csv"):
        """Export processed data to CSV"""
        if not self.processed_data.empty:
            self.processed_data.to_csv(filename, index=False)
            print(f"Processed data exported to {filename}")
        else:
            print("No processed data to export")
    
    def get_commodity_analysis(self, commodity):
        """Get detailed analysis for a specific commodity"""
        if self.processed_data.empty:
            print("No processed data available.")
            return None
        
        if commodity not in self.processed_data.columns:
            print(f"Commodity '{commodity}' not found in data.")
            return None
        
        df = self.processed_data
        commodity_data = df[df[commodity].notna()].copy()
        
        if len(commodity_data) == 0:
            print(f"No data available for {commodity}")
            return None
        
        analysis = {
            'commodity': commodity,
            'total_records': len(commodity_data),
            'year_range': (commodity_data['Year'].min(), commodity_data['Year'].max()),
            'price_stats': commodity_data[commodity].describe(),
            'period_averages': commodity_data.groupby('period_classification')[commodity].mean(),
            'century_averages': commodity_data.groupby('century')[commodity].mean()
        }
        
        return analysis
    
    def compare_commodities(self, commodities_list):
        """Compare multiple commodities"""
        if self.processed_data.empty:
            print("No processed data available.")
            return
        
        df = self.processed_data
        
        print(f"\nCommodity Comparison: {', '.join(commodities_list)}")
        print("=" * 50)
        
        comparison_data = {}
        
        for commodity in commodities_list:
            if commodity in df.columns:
                commodity_data = df[df[commodity].notna()]
                if len(commodity_data) > 0:
                    comparison_data[commodity] = {
                        'records': len(commodity_data),
                        'mean_price': commodity_data[commodity].mean(),
                        'std_price': commodity_data[commodity].std(),
                        'min_price': commodity_data[commodity].min(),
                        'max_price': commodity_data[commodity].max(),
                        'year_range': f"{commodity_data['Year'].min()}-{commodity_data['Year'].max()}"
                    }
        
        # Create comparison DataFrame
        comparison_df = pd.DataFrame(comparison_data).T
        print(comparison_df.round(3))
        
        return comparison_df


def main():
    """Main function to demonstrate the dataloader"""
    print("Agricultural Price Data Loader")
    print("=" * 40)
    
    # Initialize the dataloader
    loader = AgPriceDataLoader()
    
    # Load data
    if loader.load_data():
        # Process data
        loader.process_data()
        
        # Generate summary statistics
        loader.get_data_summary()
        
        # Create plots
        loader.plot_price_analysis(save_path="plots/agprice_analysis.png")
        
        # Export processed data
        loader.export_processed_data()
        
        # Example commodity analysis
        print("\n" + "="*50)
        print("WHEAT PRICE ANALYSIS")
        print("="*50)
        wheat_analysis = loader.get_commodity_analysis('Wheat')
        if wheat_analysis:
            print(f"Records: {wheat_analysis['total_records']}")
            print(f"Year range: {wheat_analysis['year_range'][0]}-{wheat_analysis['year_range'][1]}")
            print(f"Average price: {wheat_analysis['price_stats']['mean']:.3f}")
            print(f"Price volatility (std): {wheat_analysis['price_stats']['std']:.3f}")
        
        # Compare main grains
        print("\n" + "="*50)
        print("MAIN GRAINS COMPARISON")
        print("="*50)
        loader.compare_commodities(['Wheat', 'Rye', 'Barley', 'Oats'])
        
    else:
        print("Failed to load data. Please check the file path and format.")


if __name__ == "__main__":
    main()
