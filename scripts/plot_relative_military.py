import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from dataloaders.nmc_dataloader import NMCDataLoader

def calculate_relative_military_scores():
    loader = NMCDataLoader('data/military/NMC-60-wsupplementary.csv')
    data = loader.load_data()
    
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
    
    return data_with_totals

def plot_relative_military_scores():
    data = calculate_relative_military_scores()
    
    # Major military powers throughout history
    major_powers = [
        'United States of America',
        'United Kingdom', 
        'France',
        'Germany',
        'Russia',
        'China'
    ]
    
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))
    fig.suptitle('Relative Military Power of Major Nations (% of Global Total)', fontsize=16)
    
    # Plot military expenditures
    for i, country in enumerate(major_powers):
        country_data = data[data['country'] == country]
        if not country_data.empty:
            # Filter out NaN values
            country_data_clean = country_data.dropna(subset=['milex_pct'])
            if not country_data_clean.empty:
                ax1.plot(country_data_clean['year'], country_data_clean['milex_pct'], 
                        color=colors[i % len(colors)], label=country, linewidth=2, alpha=0.8)
    
    ax1.set_title('Military Expenditures (% of Global Total)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Percentage of Global Military Expenditures')
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(bottom=0)
    
    # Plot military personnel
    for i, country in enumerate(major_powers):
        country_data = data[data['country'] == country]
        if not country_data.empty:
            # Filter out NaN values
            country_data_clean = country_data.dropna(subset=['milper_pct'])
            if not country_data_clean.empty:
                ax2.plot(country_data_clean['year'], country_data_clean['milper_pct'], 
                        color=colors[i % len(colors)], label=country, linewidth=2, alpha=0.8)
    
    ax2.set_title('Military Personnel (% of Global Total)')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Percentage of Global Military Personnel')
    ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(bottom=0)
    
    plt.tight_layout()
    plt.savefig('relative_military_power.png', dpi=300, bbox_inches='tight')
    print('Plot saved as relative_military_power.png')
    
    # Print some statistics
    print('\nTop military spenders by decade (% of global):')
    decades = [1850, 1900, 1950, 2000]
    for decade in decades:
        decade_data = data[(data['year'] >= decade) & (data['year'] < decade + 10)]
        if not decade_data.empty:
            top_spenders = decade_data.groupby('country')['milex_pct'].mean().sort_values(ascending=False).head(5)
            print(f'\n{decade}s:')
            for country, pct in top_spenders.items():
                print(f'  {country}: {pct:.1f}%')

if __name__ == "__main__":
    plot_relative_military_scores()