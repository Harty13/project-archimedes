import matplotlib.pyplot as plt
import pandas as pd
from dataloaders.nmc_dataloader import NMCDataLoader

def plot_military_data():
    loader = NMCDataLoader('data/military/NMC-60-wsupplementary.csv')
    data = loader.load_data()
    
    major_powers = ['United States of America', 'China', 'Russia', 'United Kingdom', 'France', 'Germany']
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Military and Demographic Indicators Over Time', fontsize=16)
    
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']
    
    for i, country in enumerate(major_powers):
        country_data = data[data['country'] == country]
        if country_data.empty:
            continue
        
        color = colors[i % len(colors)]
        
        axes[0, 0].plot(country_data['year'], country_data['milex'], 
                       color=color, label=country, linewidth=2, alpha=0.8)
        axes[0, 1].plot(country_data['year'], country_data['milper'], 
                       color=color, label=country, linewidth=2, alpha=0.8)
        axes[1, 0].plot(country_data['year'], country_data['tpop'], 
                       color=color, label=country, linewidth=2, alpha=0.8)
        axes[1, 1].plot(country_data['year'], country_data['upop'], 
                       color=color, label=country, linewidth=2, alpha=0.8)
    
    axes[0, 0].set_title('Military Expenditures (thousands)')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Military Expenditures')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    axes[0, 1].set_title('Military Personnel (thousands)')
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Military Personnel')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    axes[1, 0].set_title('Total Population (thousands)')
    axes[1, 0].set_xlabel('Year')
    axes[1, 0].set_ylabel('Total Population')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    axes[1, 1].set_title('Urban Population (thousands)')
    axes[1, 1].set_xlabel('Year')
    axes[1, 1].set_ylabel('Urban Population')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('military_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    plot_military_data()