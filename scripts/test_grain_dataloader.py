import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

def load_and_plot_available_data():
    """Test function to load available grain data and create plots"""
    
    print("Testing Grain Price Data Loader with Available Data")
    print("=" * 50)
    
    data_dir = Path("data/dataverse_files")
    all_data = []
    
    # 1. Load England Grain Data
    print("\n1. Loading England Grain Data...")
    
    # England grain 1841-1929
    england1_path = data_dir / "England Grain" / "englandgrain1.xls"
    if england1_path.exists():
        try:
            df1 = pd.read_excel(england1_path)
            print(f"   England 1841-1929 shape: {df1.shape}")
            print(f"   Columns: {list(df1.columns)}")
            
            # Try to extract year and price data
            if len(df1.columns) >= 2:
                # Assume first column is year, others are prices
                year_col = df1.columns[0]
                price_cols = df1.columns[1:]
                
                # Clean and prepare data
                df_clean = pd.DataFrame()
                df_clean['year'] = pd.to_numeric(df1[year_col], errors='coerce')
                
                # Average all price columns
                price_data = []
                for col in price_cols:
                    prices = pd.to_numeric(df1[col], errors='coerce')
                    price_data.append(prices)
                
                if price_data:
                    df_clean['grain_price'] = np.nanmean(price_data, axis=0)
                    df_clean['country'] = 'UK'
                    df_clean['region'] = 'England_1841_1929'
                    df_clean['dataset'] = 'england_grain_1'
                    
                    # Filter valid data
                    df_clean = df_clean.dropna(subset=['year', 'grain_price'])
                    df_clean = df_clean[(df_clean['year'] >= 1800) & (df_clean['year'] <= 2000)]
                    
                    if not df_clean.empty:
                        all_data.append(df_clean)
                        print(f"   Successfully processed {len(df_clean)} records")
                    
        except Exception as e:
            print(f"   Error loading England 1841-1929 data: {e}")
    
    # England grain 1929-1955
    england2_path = data_dir / "England Grain" / "englandgrain2.xls"
    if england2_path.exists():
        try:
            df2 = pd.read_excel(england2_path)
            print(f"   England 1929-1955 shape: {df2.shape}")
            print(f"   Columns: {list(df2.columns)}")
            
            if len(df2.columns) >= 2:
                year_col = df2.columns[0]
                price_cols = df2.columns[1:]
                
                df_clean = pd.DataFrame()
                df_clean['year'] = pd.to_numeric(df2[year_col], errors='coerce')
                
                price_data = []
                for col in price_cols:
                    prices = pd.to_numeric(df2[col], errors='coerce')
                    price_data.append(prices)
                
                if price_data:
                    df_clean['grain_price'] = np.nanmean(price_data, axis=0)
                    df_clean['country'] = 'UK'
                    df_clean['region'] = 'England_1929_1955'
                    df_clean['dataset'] = 'england_grain_2'
                    
                    df_clean = df_clean.dropna(subset=['year', 'grain_price'])
                    df_clean = df_clean[(df_clean['year'] >= 1800) & (df_clean['year'] <= 2000)]
                    
                    if not df_clean.empty:
                        all_data.append(df_clean)
                        print(f"   Successfully processed {len(df_clean)} records")
                    
        except Exception as e:
            print(f"   Error loading England 1929-1955 data: {e}")
    
    # 2. Load Winchester Data
    print("\n2. Loading Winchester Data...")
    winchester_path = data_dir / "Winchester" / "winchester.xls"
    if winchester_path.exists():
        try:
            df_win = pd.read_excel(winchester_path)
            print(f"   Winchester shape: {df_win.shape}")
            print(f"   Columns: {list(df_win.columns)}")
            
            if len(df_win.columns) >= 2:
                year_col = df_win.columns[0]
                price_cols = df_win.columns[1:]
                
                df_clean = pd.DataFrame()
                df_clean['year'] = pd.to_numeric(df_win[year_col], errors='coerce')
                
                price_data = []
                for col in price_cols:
                    prices = pd.to_numeric(df_win[col], errors='coerce')
                    price_data.append(prices)
                
                if price_data:
                    df_clean['grain_price'] = np.nanmean(price_data, axis=0)
                    df_clean['country'] = 'UK'
                    df_clean['region'] = 'Winchester'
                    df_clean['dataset'] = 'winchester'
                    
                    df_clean = df_clean.dropna(subset=['year', 'grain_price'])
                    df_clean = df_clean[(df_clean['year'] >= 1600) & (df_clean['year'] <= 1900)]
                    
                    if not df_clean.empty:
                        all_data.append(df_clean)
                        print(f"   Successfully processed {len(df_clean)} records")
                    
        except Exception as e:
            print(f"   Error loading Winchester data: {e}")
    
    # 3. Combine and analyze data
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        print(f"\n3. Combined Data Summary:")
        print(f"   Total records: {len(combined_df)}")
        print(f"   Year range: {combined_df['year'].min():.0f} - {combined_df['year'].max():.0f}")
        print(f"   Datasets: {combined_df['dataset'].unique()}")
        print(f"   Regions: {combined_df['region'].unique()}")
        
        # Create plots
        print("\n4. Creating Plots...")
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Historical Grain Prices - UK Data Analysis', fontsize=16, fontweight='bold')
        
        # Plot 1: Time series by dataset
        ax1 = axes[0, 0]
        for dataset in combined_df['dataset'].unique():
            data_subset = combined_df[combined_df['dataset'] == dataset]
            if len(data_subset) > 1:
                data_grouped = data_subset.groupby('year')['grain_price'].mean().reset_index()
                ax1.plot(data_grouped['year'], data_grouped['grain_price'], 
                        label=dataset, linewidth=2, alpha=0.8, marker='o', markersize=3)
        
        ax1.set_title('Grain Prices by Dataset')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Price (original units)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Overall trend
        ax2 = axes[0, 1]
        overall_trend = combined_df.groupby('year')['grain_price'].mean().reset_index()
        ax2.plot(overall_trend['year'], overall_trend['grain_price'], 
                linewidth=3, alpha=0.8, color='darkblue')
        ax2.fill_between(overall_trend['year'], overall_trend['grain_price'], 
                        alpha=0.3, color='lightblue')
        
        ax2.set_title('Overall UK Grain Price Trend')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Average Price')
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: Price distribution by century
        ax3 = axes[1, 0]
        combined_df['century'] = (combined_df['year'] // 100) * 100
        century_data = combined_df.groupby('century')['grain_price'].mean()
        
        centuries = century_data.index
        prices = century_data.values
        
        bars = ax3.bar(range(len(centuries)), prices, alpha=0.7, color='steelblue')
        ax3.set_title('Average Prices by Century')
        ax3.set_xlabel('Century')
        ax3.set_ylabel('Average Price')
        ax3.set_xticks(range(len(centuries)))
        ax3.set_xticklabels([f"{int(c)}s" for c in centuries])
        ax3.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}', ha='center', va='bottom')
        
        # Plot 4: Data coverage
        ax4 = axes[1, 1]
        coverage_data = combined_df.groupby('dataset').agg({
            'year': ['min', 'max', 'count']
        }).round(0)
        
        datasets = coverage_data.index
        start_years = coverage_data[('year', 'min')].values
        end_years = coverage_data[('year', 'max')].values
        counts = coverage_data[('year', 'count')].values
        
        y_pos = np.arange(len(datasets))
        
        # Create horizontal bars showing time coverage
        for i, (start, end, count) in enumerate(zip(start_years, end_years, counts)):
            ax4.barh(i, end - start, left=start, alpha=0.7, 
                    label=f'{datasets[i]} ({int(count)} records)')
        
        ax4.set_title('Dataset Time Coverage')
        ax4.set_xlabel('Year')
        ax4.set_yticks(y_pos)
        ax4.set_yticklabels(datasets)
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save plot
        plt.savefig('uk_grain_prices_analysis.png', dpi=300, bbox_inches='tight')
        print("   Plot saved as 'uk_grain_prices_analysis.png'")
        
        # Export data
        combined_df.to_csv('uk_grain_prices_data.csv', index=False)
        print("   Data exported as 'uk_grain_prices_data.csv'")
        
        plt.show()
        
        # Print detailed statistics
        print("\n5. Detailed Statistics:")
        print("-" * 30)
        
        for dataset in combined_df['dataset'].unique():
            data_subset = combined_df[combined_df['dataset'] == dataset]
            print(f"\n{dataset}:")
            print(f"  Records: {len(data_subset)}")
            print(f"  Year range: {data_subset['year'].min():.0f} - {data_subset['year'].max():.0f}")
            print(f"  Price range: {data_subset['grain_price'].min():.2f} - {data_subset['grain_price'].max():.2f}")
            print(f"  Average price: {data_subset['grain_price'].mean():.2f}")
            print(f"  Price std dev: {data_subset['grain_price'].std():.2f}")
        
    else:
        print("\nNo data could be loaded successfully.")
        print("Please check that the data files exist and are readable.")

if __name__ == "__main__":
    load_and_plot_available_data()
