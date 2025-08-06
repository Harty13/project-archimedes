import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

def plot_china_usa_ratio_from_csv():
    # Read the China/USA ratio data from CSV
    df = pd.read_csv('data/ratios/china_usa_military_ratio.csv')
    
    # Filter data from 1990 onwards
    df = df[df['year'] >= 1990]
    
    # Create the plot
    fig, ax = plt.subplots(1, 1, figsize=(15, 8))
    fig.suptitle('China/USA Military Power Ratio (1990-2016)', fontsize=16)
    
    # Plot the ratio
    ax.plot(df['year'], df['ratio'], color='red', linewidth=2, alpha=0.8, label='China/USA Ratio')
    
    # Add horizontal line at y=1 for equal power reference
    ax.axhline(y=1, color='black', linestyle='--', alpha=0.5, label='Equal Power (ratio=1)')
    
    # Formatting
    ax.set_title('China/USA Military Power Ratio (Multiplicative: Expenditure % × Personnel %)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Ratio (China/USA)')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Set y-axis to start from 0
    ax.set_ylim(bottom=0)
    
    # Save the plot
    plt.tight_layout()
    plt.savefig('china_usa_ratio_from_csv.png', dpi=300, bbox_inches='tight')
    print('China/USA ratio plot saved as china_usa_ratio_from_csv.png')
    
    # Print some statistics
    print(f'\nChina/USA Military Power Ratio Statistics (1990-2016):')
    print(f'Data covers {df["year"].min()} to {df["year"].max()}')
    print(f'Total records: {len(df)}')
    print(f'Minimum ratio: {df["ratio"].min():.4f} in {df.loc[df["ratio"].idxmin(), "year"]}')
    print(f'Maximum ratio: {df["ratio"].max():.4f} in {df.loc[df["ratio"].idxmax(), "year"]}')
    
    # All data since we're already filtered to 1990+
    print(f'\nAll ratios (1990-2016):')
    for _, row in df.iterrows():
        print(f'  {int(row["year"])}: {row["ratio"]:.3f}')

if __name__ == "__main__":
    plot_china_usa_ratio_from_csv()