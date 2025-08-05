import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
import re
from datetime import datetime
import requests
from io import BytesIO

warnings.filterwarnings('ignore')

class GrainPriceDataLoader:
    """
    A comprehensive dataloader for extracting and analyzing grain price data
    from the UK and US historical datasets (18th-20th century)
    """
    
    def __init__(self, data_dir="data/dataverse_files"):
        self.data_dir = Path(data_dir)
        self.uk_data = {}
        self.us_data = {}
        self.combined_data = pd.DataFrame()
        
    def load_uk_grain_data(self):
        """Load UK grain price data from various sources"""
        print("Loading UK grain price data...")
        
        # 1. England Grain Data (1841-1955)
        try:
            # England grain 1841-1929 (barley and oats)
            england1_path = self.data_dir / "England Grain" / "englandgrain1.xls"
            if england1_path.exists():
                df1 = pd.read_excel(england1_path, sheet_name=0)
                df1 = self._clean_england_grain_data(df1, "1841-1929")
                self.uk_data['england_1841_1929'] = df1
                
            # England grain 1929-1955 (wheat, barley, oats)
            england2_path = self.data_dir / "England Grain" / "englandgrain2.xls"
            if england2_path.exists():
                df2 = pd.read_excel(england2_path, sheet_name=0)
                df2 = self._clean_england_grain_data(df2, "1929-1955")
                self.uk_data['england_1929_1955'] = df2
                
        except Exception as e:
            print(f"Error loading England grain data: {e}")
            
        # 2. Winchester data (1657-1817)
        try:
            winchester_path = self.data_dir / "Winchester" / "winchester.xls"
            if winchester_path.exists():
                df_win = pd.read_excel(winchester_path, sheet_name=0)
                df_win = self._clean_winchester_data(df_win)
                self.uk_data['winchester'] = df_win
        except Exception as e:
            print(f"Error loading Winchester data: {e}")
            
        # 3. Cambridge data (1594-1681)
        try:
            cambridge_path = self.data_dir / "Cambridge" / "cambridge.xls"
            if cambridge_path.exists():
                df_cam = pd.read_excel(cambridge_path, sheet_name=0)
                df_cam = self._clean_cambridge_data(df_cam)
                self.uk_data['cambridge'] = df_cam
        except Exception as e:
            print(f"Error loading Cambridge data: {e}")
            
        # 4. Various Towns data (1270-1620)
        try:
            various_path = self.data_dir / "Various Towns" / "varioustowns.xls"
            if various_path.exists():
                df_var = pd.read_excel(various_path, sheet_name=0)
                df_var = self._clean_various_towns_data(df_var)
                self.uk_data['various_towns'] = df_var
        except Exception as e:
            print(f"Error loading Various Towns data: {e}")
            
        print(f"Loaded {len(self.uk_data)} UK datasets")
        
    def load_us_grain_data(self):
        """Load US grain price data from GPIH website"""
        print("Loading US grain price data...")
        
        # US datasets are available from GPIH website
        us_datasets = {
            'massachusetts': 'http://gpih.ucdavis.edu/files/Massachusetts_1630-1883.xls',
            'maryland': 'http://gpih.ucdavis.edu/files/Maryland_1752-1856.xls',
            'chesapeake': 'http://gpih.ucdavis.edu/files/Chesapeake_1733-1827.xls',
            'vermont': 'http://gpih.ucdavis.edu/files/Vermont_1780-1943.xls',
            'west_virginia': 'http://gpih.ucdavis.edu/files/West_Virginia_1788-1860.xls',
            'san_francisco': 'http://gpih.ucdavis.edu/files/San_Francisco_wholesale_prices_1847-1900_and_California_wages_1870-1928.xls'
        }
        
        for name, url in us_datasets.items():
            try:
                print(f"Attempting to load {name} data...")
                response = requests.get(url, timeout=30)
                if response.status_code == 200:
                    df = pd.read_excel(BytesIO(response.content), sheet_name=0)
                    df = self._clean_us_data(df, name)
                    if not df.empty:
                        self.us_data[name] = df
                        print(f"Successfully loaded {name} data")
                else:
                    print(f"Failed to download {name} data (status: {response.status_code})")
            except Exception as e:
                print(f"Error loading {name} data: {e}")
                
        print(f"Loaded {len(self.us_data)} US datasets")
        
    def _clean_england_grain_data(self, df, period):
        """Clean England grain data"""
        try:
            # Look for year and price columns
            df_clean = pd.DataFrame()
            
            # Find year column
            year_col = None
            for col in df.columns:
                if 'year' in str(col).lower() or df[col].dtype in ['int64', 'float64']:
                    if df[col].min() > 1700 and df[col].max() < 2000:
                        year_col = col
                        break
                        
            if year_col is None:
                # Try first column
                year_col = df.columns[0]
                
            # Extract grain price columns
            grain_cols = []
            for col in df.columns:
                col_name = str(col).lower()
                if any(grain in col_name for grain in ['wheat', 'barley', 'oats', 'rye']):
                    grain_cols.append(col)
                    
            if year_col is not None and grain_cols:
                df_clean['year'] = pd.to_numeric(df[year_col], errors='coerce')
                df_clean['country'] = 'UK'
                df_clean['region'] = f'England_{period}'
                
                # Average grain prices
                grain_prices = []
                for col in grain_cols:
                    prices = pd.to_numeric(df[col], errors='coerce')
                    grain_prices.append(prices)
                    
                if grain_prices:
                    df_clean['grain_price'] = np.nanmean(grain_prices, axis=0)
                    df_clean['grain_type'] = 'mixed'
                    
                # Filter valid years (18th-20th century)
                df_clean = df_clean[(df_clean['year'] >= 1700) & (df_clean['year'] <= 2000)]
                df_clean = df_clean.dropna(subset=['year', 'grain_price'])
                
            return df_clean
            
        except Exception as e:
            print(f"Error cleaning England grain data: {e}")
            return pd.DataFrame()
            
    def _clean_winchester_data(self, df):
        """Clean Winchester data (1657-1817)"""
        try:
            df_clean = pd.DataFrame()
            
            # Look for year and wheat/malt price columns
            year_col = None
            for col in df.columns:
                if df[col].dtype in ['int64', 'float64']:
                    if df[col].min() > 1600 and df[col].max() < 1900:
                        year_col = col
                        break
                        
            if year_col is None:
                year_col = df.columns[0]
                
            price_cols = []
            for col in df.columns:
                col_name = str(col).lower()
                if any(grain in col_name for grain in ['wheat', 'malt', 'price']):
                    price_cols.append(col)
                    
            if year_col is not None and price_cols:
                df_clean['year'] = pd.to_numeric(df[year_col], errors='coerce')
                df_clean['country'] = 'UK'
                df_clean['region'] = 'Winchester'
                
                # Average prices
                prices = []
                for col in price_cols:
                    price_data = pd.to_numeric(df[col], errors='coerce')
                    prices.append(price_data)
                    
                if prices:
                    df_clean['grain_price'] = np.nanmean(prices, axis=0)
                    df_clean['grain_type'] = 'wheat_malt'
                    
                df_clean = df_clean[(df_clean['year'] >= 1700) & (df_clean['year'] <= 1900)]
                df_clean = df_clean.dropna(subset=['year', 'grain_price'])
                
            return df_clean
            
        except Exception as e:
            print(f"Error cleaning Winchester data: {e}")
            return pd.DataFrame()
            
    def _clean_cambridge_data(self, df):
        """Clean Cambridge data (1594-1681)"""
        try:
            df_clean = pd.DataFrame()
            
            # Similar cleaning process for Cambridge data
            year_col = None
            for col in df.columns:
                if df[col].dtype in ['int64', 'float64']:
                    if df[col].min() > 1500 and df[col].max() < 1800:
                        year_col = col
                        break
                        
            price_cols = []
            for col in df.columns:
                col_name = str(col).lower()
                if any(grain in col_name for grain in ['wheat', 'barley', 'price']):
                    price_cols.append(col)
                    
            if year_col is not None and price_cols:
                df_clean['year'] = pd.to_numeric(df[year_col], errors='coerce')
                df_clean['country'] = 'UK'
                df_clean['region'] = 'Cambridge'
                
                prices = []
                for col in price_cols:
                    price_data = pd.to_numeric(df[col], errors='coerce')
                    prices.append(price_data)
                    
                if prices:
                    df_clean['grain_price'] = np.nanmean(prices, axis=0)
                    df_clean['grain_type'] = 'wheat_barley'
                    
                df_clean = df_clean[(df_clean['year'] >= 1700) & (df_clean['year'] <= 1800)]
                df_clean = df_clean.dropna(subset=['year', 'grain_price'])
                
            return df_clean
            
        except Exception as e:
            print(f"Error cleaning Cambridge data: {e}")
            return pd.DataFrame()
            
    def _clean_various_towns_data(self, df):
        """Clean Various Towns data (1270-1620)"""
        try:
            df_clean = pd.DataFrame()
            
            # Focus on 18th century data only
            year_col = None
            for col in df.columns:
                if df[col].dtype in ['int64', 'float64']:
                    if df[col].min() > 1200 and df[col].max() < 1700:
                        year_col = col
                        break
                        
            price_cols = []
            for col in df.columns:
                col_name = str(col).lower()
                if any(grain in col_name for grain in ['wheat', 'barley', 'oats', 'price']):
                    price_cols.append(col)
                    
            if year_col is not None and price_cols:
                df_clean['year'] = pd.to_numeric(df[year_col], errors='coerce')
                df_clean['country'] = 'UK'
                df_clean['region'] = 'Various_Towns'
                
                prices = []
                for col in price_cols:
                    price_data = pd.to_numeric(df[col], errors='coerce')
                    prices.append(price_data)
                    
                if prices:
                    df_clean['grain_price'] = np.nanmean(prices, axis=0)
                    df_clean['grain_type'] = 'mixed'
                    
                # Only keep data from 1700 onwards for consistency
                df_clean = df_clean[df_clean['year'] >= 1700]
                df_clean = df_clean.dropna(subset=['year', 'grain_price'])
                
            return df_clean
            
        except Exception as e:
            print(f"Error cleaning Various Towns data: {e}")
            return pd.DataFrame()
            
    def _clean_us_data(self, df, dataset_name):
        """Clean US data from various sources"""
        try:
            df_clean = pd.DataFrame()
            
            # Look for year column
            year_col = None
            for col in df.columns:
                col_name = str(col).lower()
                if 'year' in col_name or 'date' in col_name:
                    year_col = col
                    break
                    
            if year_col is None:
                # Try first column if it contains years
                first_col = df.columns[0]
                if df[first_col].dtype in ['int64', 'float64']:
                    if df[first_col].min() > 1600 and df[first_col].max() < 2000:
                        year_col = first_col
                        
            # Look for grain price columns
            grain_cols = []
            for col in df.columns:
                col_name = str(col).lower()
                if any(grain in col_name for grain in ['wheat', 'corn', 'barley', 'oats', 'rye', 'grain']):
                    if 'price' in col_name or any(unit in col_name for unit in ['bushel', 'lb', 'pound']):
                        grain_cols.append(col)
                        
            if year_col is not None and grain_cols:
                df_clean['year'] = pd.to_numeric(df[year_col], errors='coerce')
                df_clean['country'] = 'US'
                df_clean['region'] = dataset_name
                
                # Average grain prices
                prices = []
                for col in grain_cols:
                    price_data = pd.to_numeric(df[col], errors='coerce')
                    prices.append(price_data)
                    
                if prices:
                    df_clean['grain_price'] = np.nanmean(prices, axis=0)
                    df_clean['grain_type'] = 'mixed'
                    
                # Filter for 18th-20th century
                df_clean = df_clean[(df_clean['year'] >= 1700) & (df_clean['year'] <= 2000)]
                df_clean = df_clean.dropna(subset=['year', 'grain_price'])
                
            return df_clean
            
        except Exception as e:
            print(f"Error cleaning US data for {dataset_name}: {e}")
            return pd.DataFrame()
            
    def combine_data(self):
        """Combine all UK and US data into a single DataFrame"""
        all_data = []
        
        # Add UK data
        for dataset_name, df in self.uk_data.items():
            if not df.empty:
                df_copy = df.copy()
                df_copy['dataset'] = dataset_name
                all_data.append(df_copy)
                
        # Add US data
        for dataset_name, df in self.us_data.items():
            if not df.empty:
                df_copy = df.copy()
                df_copy['dataset'] = dataset_name
                all_data.append(df_copy)
                
        if all_data:
            self.combined_data = pd.concat(all_data, ignore_index=True)
            print(f"Combined data shape: {self.combined_data.shape}")
            print(f"Year range: {self.combined_data['year'].min():.0f} - {self.combined_data['year'].max():.0f}")
        else:
            print("No data to combine")
            
    def plot_grain_prices(self, save_path=None):
        """Create comprehensive plots of grain price data"""
        if self.combined_data.empty:
            print("No data to plot. Please load and combine data first.")
            return
            
        # Set up the plotting style
        try:
            plt.style.use('seaborn-v0_8')
        except:
            plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Historical Grain Prices: UK vs US (18th-20th Century)', fontsize=16, fontweight='bold')
        
        # 1. Time series comparison by country
        ax1 = axes[0, 0]
        uk_data = self.combined_data[self.combined_data['country'] == 'UK']
        us_data = self.combined_data[self.combined_data['country'] == 'US']
        
        if not uk_data.empty:
            uk_grouped = uk_data.groupby('year')['grain_price'].mean().reset_index()
            ax1.plot(uk_grouped['year'], uk_grouped['grain_price'], 
                    label='UK', linewidth=2, alpha=0.8, color='blue')
                    
        if not us_data.empty:
            us_grouped = us_data.groupby('year')['grain_price'].mean().reset_index()
            ax1.plot(us_grouped['year'], us_grouped['grain_price'], 
                    label='US', linewidth=2, alpha=0.8, color='red')
                    
        ax1.set_title('Average Grain Prices Over Time')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Price (normalized units)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Regional comparison within countries
        ax2 = axes[0, 1]
        
        # Plot UK regions
        uk_regions = uk_data['region'].unique()
        colors_uk = plt.cm.Blues(np.linspace(0.4, 0.9, len(uk_regions)))
        
        for i, region in enumerate(uk_regions):
            region_data = uk_data[uk_data['region'] == region]
            if len(region_data) > 1:
                region_grouped = region_data.groupby('year')['grain_price'].mean().reset_index()
                ax2.plot(region_grouped['year'], region_grouped['grain_price'], 
                        label=f'UK-{region}', alpha=0.7, color=colors_uk[i])
                        
        # Plot US regions
        us_regions = us_data['region'].unique()
        colors_us = plt.cm.Reds(np.linspace(0.4, 0.9, len(us_regions)))
        
        for i, region in enumerate(us_regions):
            region_data = us_data[us_data['region'] == region]
            if len(region_data) > 1:
                region_grouped = region_data.groupby('year')['grain_price'].mean().reset_index()
                ax2.plot(region_grouped['year'], region_grouped['grain_price'], 
                        label=f'US-{region}', alpha=0.7, color=colors_us[i])
                        
        ax2.set_title('Regional Price Variations')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Price (normalized units)')
        ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax2.grid(True, alpha=0.3)
        
        # 3. Century-wise comparison
        ax3 = axes[1, 0]
        
        # Add century column
        self.combined_data['century'] = (self.combined_data['year'] // 100) * 100
        century_data = self.combined_data.groupby(['country', 'century'])['grain_price'].mean().reset_index()
        
        centuries = sorted(century_data['century'].unique())
        x_pos = np.arange(len(centuries))
        width = 0.35
        
        uk_century = century_data[century_data['country'] == 'UK']
        us_century = century_data[century_data['country'] == 'US']
        
        uk_prices = [uk_century[uk_century['century'] == c]['grain_price'].iloc[0] 
                    if len(uk_century[uk_century['century'] == c]) > 0 else 0 for c in centuries]
        us_prices = [us_century[us_century['century'] == c]['grain_price'].iloc[0] 
                    if len(us_century[us_century['century'] == c]) > 0 else 0 for c in centuries]
        
        ax3.bar(x_pos - width/2, uk_prices, width, label='UK', alpha=0.8, color='blue')
        ax3.bar(x_pos + width/2, us_prices, width, label='US', alpha=0.8, color='red')
        
        ax3.set_title('Average Prices by Century')
        ax3.set_xlabel('Century')
        ax3.set_ylabel('Average Price')
        ax3.set_xticks(x_pos)
        ax3.set_xticklabels([f"{int(c)}s" for c in centuries])
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Price volatility comparison
        ax4 = axes[1, 1]
        
        # Calculate rolling standard deviation as volatility measure
        uk_volatility = []
        us_volatility = []
        years = []
        
        for year in range(int(self.combined_data['year'].min()) + 10, 
                         int(self.combined_data['year'].max()) - 10, 5):
            year_range = (self.combined_data['year'] >= year - 10) & (self.combined_data['year'] <= year + 10)
            
            uk_subset = self.combined_data[(self.combined_data['country'] == 'UK') & year_range]
            us_subset = self.combined_data[(self.combined_data['country'] == 'US') & year_range]
            
            if len(uk_subset) > 5:
                uk_vol = uk_subset['grain_price'].std()
                uk_volatility.append(uk_vol)
            else:
                uk_volatility.append(np.nan)
                
            if len(us_subset) > 5:
                us_vol = us_subset['grain_price'].std()
                us_volatility.append(us_vol)
            else:
                us_volatility.append(np.nan)
                
            years.append(year)
            
        ax4.plot(years, uk_volatility, label='UK Volatility', linewidth=2, alpha=0.8, color='blue')
        ax4.plot(years, us_volatility, label='US Volatility', linewidth=2, alpha=0.8, color='red')
        
        ax4.set_title('Price Volatility Over Time (20-year rolling window)')
        ax4.set_xlabel('Year')
        ax4.set_ylabel('Price Standard Deviation')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
            
        plt.show()
        
    def generate_summary_statistics(self):
        """Generate summary statistics for the grain price data"""
        if self.combined_data.empty:
            print("No data available for summary statistics")
            return
            
        print("\n" + "="*60)
        print("GRAIN PRICE DATA SUMMARY STATISTICS")
        print("="*60)
        
        # Overall statistics
        print(f"\nTotal records: {len(self.combined_data)}")
        print(f"Year range: {self.combined_data['year'].min():.0f} - {self.combined_data['year'].max():.0f}")
        print(f"Countries: {', '.join(self.combined_data['country'].unique())}")
        
        # Country-wise statistics
        print("\nCOUNTRY-WISE STATISTICS:")
        print("-" * 30)
        
        for country in self.combined_data['country'].unique():
            country_data = self.combined_data[self.combined_data['country'] == country]
            print(f"\n{country}:")
            print(f"  Records: {len(country_data)}")
            print(f"  Year range: {country_data['year'].min():.0f} - {country_data['year'].max():.0f}")
            print(f"  Regions: {len(country_data['region'].unique())}")
            print(f"  Average price: {country_data['grain_price'].mean():.2f}")
            print(f"  Price std dev: {country_data['grain_price'].std():.2f}")
            print(f"  Min price: {country_data['grain_price'].min():.2f}")
            print(f"  Max price: {country_data['grain_price'].max():.2f}")
            
        # Dataset coverage
        print("\nDATASET COVERAGE:")
        print("-" * 20)
        
        dataset_summary = self.combined_data.groupby(['country', 'dataset']).agg({
            'year': ['min', 'max', 'count'],
            'grain_price': ['mean', 'std']
        }).round(2)
        
        print(dataset_summary)
        
    def export_data(self, filename="grain_prices_uk_us.csv"):
        """Export combined data to CSV"""
        if not self.combined_data.empty:
            self.combined_data.to_csv(filename, index=False)
            print(f"Data exported to {filename}")
        else:
            print("No data to export")


def main():
    """Main function to demonstrate the dataloader"""
    print("Historical Grain Price Data Loader")
    print("=" * 40)
    
    # Initialize the dataloader
    loader = GrainPriceDataLoader()
    
    # Load UK data
    loader.load_uk_grain_data()
    
    # Load US data (this will attempt to download from GPIH)
    loader.load_us_grain_data()
    
    # Combine all data
    loader.combine_data()
    
    # Generate summary statistics
    loader.generate_summary_statistics()
    
    # Create plots
    if not loader.combined_data.empty:
        loader.plot_grain_prices(save_path="grain_prices_uk_us_comparison.png")
        
        # Export data
        loader.export_data()
    else:
        print("No data was successfully loaded. Please check data availability.")


if __name__ == "__main__":
    main()
