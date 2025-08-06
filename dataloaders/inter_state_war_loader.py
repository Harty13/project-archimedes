import pandas as pd
import numpy as np
import os
from typing import List, Dict

class InterStateWarLoader:
    """
    DataLoader for Inter-State War Data v4.0
    Loads, processes, and saves war data for specified countries (UK, US, China)
    """
    
    def __init__(self, data_path: str = None):
        """Initialize the dataloader with path to the CSV file"""
        if data_path is None:
            # Updated path to military folder
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_path = os.path.join(current_dir, '..', 'data', 'military', 'Inter-StateWarData_v4.0.csv')
        
        self.data_path = data_path
        self.raw_data = None
        self.filtered_data = None
        self.output_dir = os.path.join(os.path.dirname(data_path), '')  # Same as military folder
        
        # Country codes for our analysis
        self.target_countries = {
            'United States of America': 2,
            'United Kingdom': 200, 
            'China': 710,
            'China (PRC)': 710  # Alternative naming
        }
        
    def load_data(self) -> pd.DataFrame:
        """Load the raw Inter-State War data"""
        try:
            self.raw_data = pd.read_csv(self.data_path)
            print(f"Loaded {len(self.raw_data)} records from Inter-State War database")
            return self.raw_data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
    
    def filter_by_countries(self, countries: List[str] = None) -> pd.DataFrame:
        """
        Filter wars involving the specified countries
        
        Args:
            countries: List of country names to filter for
        
        Returns:
            DataFrame with wars involving specified countries
        """
        if self.raw_data is None:
            self.load_data()
            
        if countries is None:
            countries = list(self.target_countries.keys())
        
        # Get country codes for filtering
        country_codes = [self.target_countries.get(country) for country in countries if country in self.target_countries]
        
        # Filter wars where any of our target countries participated
        mask = self.raw_data['ccode'].isin(country_codes)
        relevant_wars = self.raw_data[mask]['WarNum'].unique()
        
        # Get all records for these wars (including other participants)
        self.filtered_data = self.raw_data[self.raw_data['WarNum'].isin(relevant_wars)].copy()
        
        # Consolidate China (PRC) with China for unified representation
        self.filtered_data['StateName'] = self.filtered_data['StateName'].replace('China (PRC)', 'China')
        
        print(f"Found {len(relevant_wars)} wars involving {countries}")
        print(f"Total records: {len(self.filtered_data)} (including all participants)")
        
        return self.filtered_data
    
    def get_war_summary(self) -> pd.DataFrame:
        """Get summary statistics per war"""
        if self.filtered_data is None:
            self.filter_by_countries()
        
        # Group by war and calculate summaries
        war_summary = self.filtered_data.groupby(['WarNum', 'WarName']).agg({
            'StartYear1': 'first',
            'EndYear1': 'first', 
            'BatDeath': 'sum',
            'ccode': 'count',
            'StateName': lambda x: ', '.join(x.unique())
        }).rename(columns={
            'StartYear1': 'StartYear',
            'EndYear1': 'EndYear',
            'BatDeath': 'TotalDeaths',
            'ccode': 'NumParticipants',
            'StateName': 'Participants'
        })
        
        # Calculate war duration
        war_summary['Duration'] = war_summary['EndYear'] - war_summary['StartYear'] + 1
        war_summary['Duration'] = war_summary['Duration'].clip(lower=1)  # Ensure minimum 1 year
        
        return war_summary.reset_index()
    
    def get_country_participation(self) -> pd.DataFrame:
        """Get participation statistics by country"""
        if self.filtered_data is None:
            self.filter_by_countries()
        
        # Focus on our target countries
        target_data = self.filtered_data[
            self.filtered_data['ccode'].isin(self.target_countries.values())
        ].copy()
        
        # Consolidate China data for unified stats
        target_data['StateName'] = target_data['StateName'].replace('China (PRC)', 'China')
        
        country_stats = target_data.groupby('StateName').agg({
            'WarNum': 'nunique',
            'BatDeath': 'sum',
            'StartYear1': 'min',
            'EndYear1': 'max'
        }).rename(columns={
            'WarNum': 'WarsParticipated',
            'BatDeath': 'TotalBattleDeaths',
            'StartYear1': 'FirstWarYear',
            'EndYear1': 'LastWarYear'
        })
        
        return country_stats.reset_index()
    
    def get_timeline_data(self) -> pd.DataFrame:
        """Get timeline data with strength indicators for each country"""
        if self.filtered_data is None:
            self.filter_by_countries()
        
        # Focus on our target countries
        target_data = self.filtered_data[
            self.filtered_data['ccode'].isin(self.target_countries.values())
        ].copy()
        
        # Consolidate China data
        target_data['StateName'] = target_data['StateName'].replace('China (PRC)', 'China')
        
        timeline_data = []
        
        for _, row in target_data.iterrows():
            # Calculate strength indicators
            battle_deaths = row['BatDeath'] if row['BatDeath'] > 0 else 1
            
            # Strength based on multiple factors:
            # 1. Lower casualties relative to enemy = stronger
            # 2. Being initiator = more aggressive/confident 
            # 3. Winning = stronger
            strength_score = 100  # Base strength
            
            # Adjust for being initiator (shows confidence)
            if row['Initiator'] == 1:
                strength_score += 20
            
            # Adjust for outcome (1=win, 2=lose, 3=compromise, 4=unclear)
            if row['Outcome'] == 1:      # Win
                strength_score += 30
            elif row['Outcome'] == 2:    # Lose
                strength_score -= 30
            elif row['Outcome'] == 3:    # Compromise
                strength_score += 5
            
            # Adjust for relative casualties (lower = stronger)
            casualty_factor = max(10, min(100, 100 - np.log10(battle_deaths) * 10))
            strength_score = strength_score * (casualty_factor / 100)
            
            timeline_data.append({
                'Year': row['StartYear1'],
                'Country': row['StateName'],
                'WarName': row['WarName'],
                'BattleDeaths': battle_deaths,
                'Initiator': row['Initiator'],
                'Outcome': row['Outcome'],
                'Side': row['Side'],
                'StrengthScore': max(20, min(180, strength_score))  # Clamp between 20-180
            })
        
        return pd.DataFrame(timeline_data)
    
    def get_outcome_data(self) -> pd.DataFrame:
        """Get win/loss outcome data by country"""
        if self.filtered_data is None:
            self.filter_by_countries()
        
        # Focus on our target countries
        target_data = self.filtered_data[
            self.filtered_data['ccode'].isin(self.target_countries.values())
        ].copy()
        
        # Consolidate China data
        target_data['StateName'] = target_data['StateName'].replace('China (PRC)', 'China')
        
        outcome_data = target_data.groupby(['StateName', 'Outcome']).size().unstack(fill_value=0)
        return outcome_data.reset_index()
    
    def process_and_save(self, countries: List[str] = None) -> str:
        """
        Process all data and save to single CSV file for histogram visualization
        
        Returns:
            Path to saved file
        """
        print("\n=== PROCESSING INTER-STATE WAR DATA ===")
        
        # Load and filter data
        self.filter_by_countries(countries)
        
        # Focus on our target countries for the histogram
        target_data = self.filtered_data[
            self.filtered_data['ccode'].isin(self.target_countries.values())
        ].copy()
        
        # Consolidate China data
        target_data['StateName'] = target_data['StateName'].replace('China (PRC)', 'China')
        
        # Create a comprehensive dataset for histogram visualization
        histogram_data = []
        
        # Get all wars involving our target countries
        for war_num in target_data['WarNum'].unique():
            war_participants = target_data[target_data['WarNum'] == war_num]
            
            # Get basic war info
            first_record = war_participants.iloc[0]
            war_name = first_record['WarName']
            start_year = first_record['StartYear1']
            
            # Check if this is an inter-country conflict (UK vs US, US vs China, UK vs China)
            target_participants = war_participants['StateName'].unique()
            is_inter_country = False
            
            # Check for conflicts between our target countries
            target_set = set(target_participants)
            inter_country_pairs = [
                {'United States of America', 'United Kingdom'},
                {'United States of America', 'China'},
                {'United Kingdom', 'China'}
            ]
            
            # Check if participants are on different sides
            if len(target_participants) >= 2:
                sides = war_participants.groupby('StateName')['Side'].first()
                unique_sides = sides.unique()
                if len(unique_sides) > 1:  # Countries on different sides
                    for pair in inter_country_pairs:
                        if pair.issubset(target_set):
                            # Check if they're actually on opposite sides
                            pair_list = list(pair)
                            if len(pair_list) >= 2:
                                country1_sides = sides[sides.index == pair_list[0]].values
                                country2_sides = sides[sides.index == pair_list[1]].values
                                if len(country1_sides) > 0 and len(country2_sides) > 0:
                                    if country1_sides[0] != country2_sides[0]:
                                        is_inter_country = True
                                        break
            
            # Add each country's participation in this war
            for _, participant in war_participants.iterrows():
                histogram_data.append({
                    'WarNum': war_num,
                    'WarName': war_name,
                    'StartYear': start_year,
                    'Country': participant['StateName'],
                    'BattleDeaths': participant['BatDeath'] if participant['BatDeath'] > 0 else 0,
                    'Side': participant['Side'],
                    'Initiator': participant['Initiator'],
                    'Outcome': participant['Outcome'],
                    'IsInterCountryConflict': is_inter_country
                })
        
        # Convert to DataFrame
        processed_data = pd.DataFrame(histogram_data)
        
        # Save single processed file
        output_path = os.path.join(self.output_dir, 'processed_war_data.csv')
        processed_data.to_csv(output_path, index=False)
        
        # Print summary statistics
        print(f"\n=== DATA PROCESSING COMPLETE ===")
        print(f"Total war participations: {len(processed_data)}")
        print(f"Unique wars: {processed_data['WarNum'].nunique()}")
        print(f"Time span: {processed_data['StartYear'].min()}-{processed_data['StartYear'].max()}")
        print(f"Inter-country conflicts: {processed_data['IsInterCountryConflict'].sum()}")
        
        print(f"\n=== COUNTRY PARTICIPATION ===")
        country_stats = processed_data.groupby('Country').agg({
            'WarNum': 'nunique',
            'BattleDeaths': 'sum',
            'IsInterCountryConflict': 'sum'
        })
        
        for country, stats in country_stats.iterrows():
            print(f"{country}: {stats['WarNum']} wars, {stats['BattleDeaths']:,} deaths, {stats['IsInterCountryConflict']} inter-country conflicts")
        
        print(f"\n=== FILE SAVED ===")
        print(f"processed_war_data.csv: {output_path}")
        
        return output_path

if __name__ == "__main__":
    # Load, process and save data
    loader = InterStateWarLoader()
    output_file = loader.process_and_save(['United States of America', 'United Kingdom', 'China'])
    
    print(f"\nData processing complete. File saved to military folder.")
    print("Run the visualization script to generate plots.")