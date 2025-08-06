#!/usr/bin/env python3
"""
War Casualties Histogram Visualization
Creates histogram showing war casualties for UK, US, and China
with inter-country conflicts highlighted in red
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def load_processed_data():
    """Load the processed war data"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'military', 'processed_war_data.csv')
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Processed data file not found at {data_path}")
    
    return pd.read_csv(data_path)

def create_casualties_histogram(data):
    """Create timeline histogram showing war casualties with inter-country conflicts in red"""
    
    # Define colors for each country
    country_colors = {
        'China': '#d62728',           # Red
        'United Kingdom': '#1f77b4',  # Blue  
        'United States of America': '#2ca02c'  # Green
    }
    
    # Color for inter-country conflicts
    inter_country_color = '#ff0000'  # Bright red
    
    # Create single plot with wider figure for timeline
    fig, ax = plt.subplots(1, 1, figsize=(20, 10))
    fig.suptitle('War Casualties Timeline: UK, US, and China (1846-2003)', fontsize=16, fontweight='bold')
    
    # Sort data by time (StartYear) and group by year
    sorted_data = data.sort_values('StartYear').copy()
    
    # Get unique years and create timeline positions
    years = sorted_data['StartYear'].values
    casualties = sorted_data['BattleDeaths'].values
    
    bar_colors = []
    inter_country_annotations = []
    
    # Create bars positioned by actual year
    for i, (_, war) in enumerate(sorted_data.iterrows()):
        # Use red if it's an inter-country conflict, otherwise country color
        if war['IsInterCountryConflict']:
            bar_colors.append(inter_country_color)
            
            # Find who was fighting against whom for inter-country conflicts
            war_participants = data[data['WarNum'] == war['WarNum']]
            
            # Only look at our target countries
            target_countries = ['China', 'United Kingdom', 'United States of America']
            target_participants = war_participants[war_participants['Country'].isin(target_countries)]
            
            sides_info = {}
            for _, participant in target_participants.iterrows():
                side = participant['Side']
                country = participant['Country']
                if side not in sides_info:
                    sides_info[side] = []
                sides_info[side].append(country)
            
            # Create conflict description showing only opposing sides
            if len(sides_info) >= 2:
                side_names = []
                winner_info = ""
                
                # Determine winners and create side descriptions
                outcome_map = {1: 'Win', 2: 'Loss', 3: 'Compromise', 4: 'Unclear'}
                side_outcomes = {}
                
                for _, participant in target_participants.iterrows():
                    side = participant['Side']
                    outcome = outcome_map.get(participant['Outcome'], 'Unknown')
                    country = participant['Country']
                    
                    if side not in side_outcomes:
                        side_outcomes[side] = {'countries': [], 'outcome': outcome}
                    side_outcomes[side]['countries'].append(country)
                
                # Create the conflict description with outcomes
                for side, info in side_outcomes.items():
                    countries_str = " & ".join(info['countries'])
                    if info['outcome'] == 'Win':
                        countries_str += " (Winners)"
                    elif info['outcome'] == 'Loss':
                        countries_str += " (Losers)"
                    elif info['outcome'] in ['Compromise', 'Unclear', 'Unknown']:
                        countries_str += f" ({info['outcome']})"
                    side_names.append(countries_str)
                
                conflict_desc = " vs ".join(side_names)
            else:
                # If all on same side, shouldn't be marked as inter-country conflict
                conflict_desc = f"All on same side - check data"
            
            inter_country_annotations.append({
                'year': war['StartYear'],
                'casualties': war['BattleDeaths'],
                'war_name': war['WarName'],
                'conflict': conflict_desc
            })
        else:
            bar_colors.append(country_colors[war['Country']])
    
    # Create the bars with actual years as x-axis
    bars = ax.bar(years, casualties, color=bar_colors, alpha=0.8, width=1.5)
    
    # Set up the timeline axis
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Battle Deaths', fontsize=12)
    ax.set_title('War Casualties Timeline\n(Red bars = Inter-Country Conflicts with details)', fontsize=14)
    ax.set_yscale('log')  # Log scale for better visibility
    
    # Set x-axis to show years properly
    ax.set_xlim(min(years) - 5, max(years) + 5)
    
    # Add major year ticks
    year_ticks = range(1850, 2010, 20)
    ax.set_xticks(year_ticks)
    ax.set_xticklabels(year_ticks, rotation=45)
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add annotations for inter-country conflicts
    for annotation in inter_country_annotations:
        ax.annotate(
            f"{annotation['war_name']}\n{annotation['conflict']}",
            xy=(annotation['year'], annotation['casualties']),
            xytext=(10, 20), textcoords='offset points',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.8),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'),
            fontsize=9, ha='left'
        )
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=country_colors['China'], label='China'),
        Patch(facecolor=country_colors['United Kingdom'], label='United Kingdom'),
        Patch(facecolor=country_colors['United States of America'], label='United States'),
        Patch(facecolor=inter_country_color, label='Inter-Country Conflicts')
    ]
    ax.legend(handles=legend_elements, loc='upper left')
    
    plt.tight_layout()
    
    # Save the plot
    plots_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'plots')
    os.makedirs(plots_dir, exist_ok=True)
    
    output_path = os.path.join(plots_dir, 'war_casualties_histogram.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    print(f"Timeline histogram saved to: {output_path}")
    
    # Show the plot (commented out to avoid timeout in headless mode)
    # plt.show()
    
    return output_path

def main():
    """Main function to create the histogram"""
    print("Loading processed war data...")
    data = load_processed_data()
    
    print(f"Loaded {len(data)} war participation records")
    print(f"Unique wars: {data['WarNum'].nunique()}")
    print(f"Countries: {', '.join(data['Country'].unique())}")
    print(f"Inter-country conflicts: {data['IsInterCountryConflict'].sum()}")
    
    print("\nCreating histogram visualization...")
    output_path = create_casualties_histogram(data)
    
    print(f"\nVisualization complete! Saved to: {output_path}")

if __name__ == "__main__":
    main()