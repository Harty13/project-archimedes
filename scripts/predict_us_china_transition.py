#!/usr/bin/env python3
"""
Apply the fitted US-UK Archimedes model to US-China data to predict power transition probabilities
Uses the coefficients from the US-UK model with US-China ratio data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

class USChinaTransitionPredictor:
    def __init__(self):
        # US-UK model coefficients (from fit_archimedes_model.py results)
        self.coefficients = {
            'intercept': 0.0,
            'military': -0.466,      # m_t_lag1 coefficient
            'education': 0.127,      # e_t_lag1 coefficient  
            'volatility': 0.513,     # v_t_lag1 coefficient (food price volatility)
            'exchange': -0.071,      # sigma_fx_t_lag1 coefficient
            'time': 0.219,           # time coefficient
            'time2': 0.044,          # time^2 coefficient
            'time3': 0.051           # time^3 coefficient
        }
        
        # Model training period for time normalization
        self.training_start = 1826
        self.training_end = 1956
        
    def load_data(self):
        """Load US-China datasets"""
        print("Loading US-China datasets...")
        
        # Load main US-China dataset
        main_data = pd.read_csv('data/archimedes_dataset_us_china_1989_2024.csv', comment='#')
        print(f"Loaded main dataset: {len(main_data)} records (1989-2024)")
        
        # Load education data
        education_data = pd.read_csv('data/ratios/US_China/education_enrollment_ratio.csv')
        print(f"Loaded education data: {len(education_data)} records ({education_data['year'].min()}-{education_data['year'].max()})")
        
        return main_data, education_data
    
    def prepare_data(self, main_data, education_data):
        """Prepare and merge datasets for model application"""
        print("\nPreparing data for model application...")
        
        # Merge datasets on year
        merged_data = pd.merge(main_data, education_data, on='year', how='left')
        merged_data = merged_data.rename(columns={'ratio': 'education_ratio'})
        
        # Map variables to model inputs
        model_data = pd.DataFrame({
            'year': merged_data['year'],
            'military_ratio': np.nan,  # Will be filled when military data is available
            'education_ratio': merged_data['education_ratio'],
            'food_volatility_ratio': merged_data['food_volatility_ratio'],
            'exchange_rate_volatility': merged_data['exchange_rate_volatility']
        })
        
        # Take log of ratios (following US-UK model specification)
        # NOTE: Input ratios are China/US, but model expects US/China, so we invert them
        model_data['education_log'] = np.log(1 / model_data['education_ratio'].replace(0, np.nan))
        model_data['food_volatility_log'] = np.log(1 / model_data['food_volatility_ratio'].replace(0, np.nan))
        
        # For missing military data, use neutral value (0 in log space = ratio of 1)
        model_data['military_log'] = 0.0  # Neutral assumption
        
        # Exchange rate volatility - use as is (not a ratio)
        model_data['exchange_volatility'] = model_data['exchange_rate_volatility']
        
        print(f"Prepared data: {len(model_data)} records")
        print(f"Available education data: {model_data['education_log'].notna().sum()} years")
        print(f"Available food volatility data: {model_data['food_volatility_log'].notna().sum()} years")
        
        return model_data
    
    def normalize_time(self, year):
        """Normalize time to [0, 1] range based on original training period"""
        return (year - self.training_start) / (self.training_end - self.training_start)
    
    def sigmoid(self, z):
        """Sigmoid function for logistic regression"""
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))
    
    def predict_transition_probability(self, data):
        """Apply US-UK model to predict US-China transition probabilities"""
        print("\nApplying US-UK Archimedes model to US-China data...")
        
        results = []
        
        for _, row in data.iterrows():
            year = row['year']
            
            # Skip if critical data is missing
            if pd.isna(row['food_volatility_log']) or pd.isna(row['exchange_volatility']):
                continue
            
            # Normalize time features
            t = self.normalize_time(year)
            t2 = t * t
            t3 = t * t * t
            
            # Calculate linear combination using US-UK coefficients
            z = (self.coefficients['intercept'] +
                 self.coefficients['military'] * row['military_log'] +
                 self.coefficients['education'] * (row['education_log'] if not pd.isna(row['education_log']) else 0) +
                 self.coefficients['volatility'] * row['food_volatility_log'] +
                 self.coefficients['exchange'] * row['exchange_volatility'] +
                 self.coefficients['time'] * t +
                 self.coefficients['time2'] * t2 +
                 self.coefficients['time3'] * t3)
            
            # Apply sigmoid to get probability of US advantage, then flip for China overtaking
            prob_us_advantage = self.sigmoid(z)
            probability_china_overtakes = 1 - prob_us_advantage  # Flip to get P(China overtakes US)
            power_score = 2 * probability_china_overtakes - 1  # Convert to [-1, 1] range
            
            results.append({
                'year': year,
                'probability_china_overtakes_us': probability_china_overtakes,
                'power_score': power_score,
                'military_log': row['military_log'],
                'education_log': row['education_log'] if not pd.isna(row['education_log']) else 0,
                'food_volatility_log': row['food_volatility_log'],
                'exchange_volatility': row['exchange_volatility']
            })
        
        results_df = pd.DataFrame(results)
        print(f"Generated predictions for {len(results_df)} years")
        
        return results_df
    
    def extend_predictions(self, historical_results, end_year=2030):
        """Extend predictions beyond 2024 using trend extrapolation"""
        print(f"\nExtending predictions to {end_year}...")
        
        # Get recent trends (last 5 years)
        recent_data = historical_results.tail(5)
        
        # Calculate trends for each variable
        years = recent_data['year'].values
        food_vol_trend = np.polyfit(years, recent_data['food_volatility_log'].values, 1)
        exchange_vol_trend = np.polyfit(years, recent_data['exchange_volatility'].values, 1)
        
        # Extend education data if available
        if recent_data['education_log'].notna().any():
            education_trend = np.polyfit(years, recent_data['education_log'].values, 1)
        else:
            education_trend = [0, 0]  # No trend if no data
        
        extended_results = []
        
        for year in range(2025, end_year + 1):
            # Extrapolate variables using trends (already inverted in historical data)
            food_vol_log = food_vol_trend[0] * year + food_vol_trend[1]
            exchange_vol = exchange_vol_trend[0] * year + exchange_vol_trend[1]
            education_log = education_trend[0] * year + education_trend[1] if education_trend[0] != 0 else 0
            
            # Apply model
            t = self.normalize_time(year)
            t2 = t * t
            t3 = t * t * t
            
            z = (self.coefficients['intercept'] +
                 self.coefficients['military'] * 0.0 +  # Still using neutral military
                 self.coefficients['education'] * education_log +
                 self.coefficients['volatility'] * food_vol_log +
                 self.coefficients['exchange'] * exchange_vol +
                 self.coefficients['time'] * t +
                 self.coefficients['time2'] * t2 +
                 self.coefficients['time3'] * t3)
            
            prob_us_advantage = self.sigmoid(z)
            probability_china_overtakes = 1 - prob_us_advantage  # Flip to get P(China overtakes US)
            power_score = 2 * probability_china_overtakes - 1
            
            extended_results.append({
                'year': year,
                'probability_china_overtakes_us': probability_china_overtakes,
                'power_score': power_score,
                'military_log': 0.0,
                'education_log': education_log,
                'food_volatility_log': food_vol_log,
                'exchange_volatility': exchange_vol,
                'is_projection': True
            })
        
        extended_df = pd.DataFrame(extended_results)
        print(f"Generated projections for {len(extended_df)} years (2025-{end_year})")
        
        return extended_df
    
    def analyze_results(self, results_df, extended_df=None):
        """Analyze transition probability results"""
        print("\n" + "="*60)
        print("US-CHINA TRANSITION PROBABILITY ANALYSIS")
        print("="*60)
        
        # Combine historical and projected data
        if extended_df is not None:
            # Mark historical data
            results_df['is_projection'] = False
            all_results = pd.concat([results_df, extended_df], ignore_index=True)
        else:
            all_results = results_df.copy()
            all_results['is_projection'] = False
        
        # Key statistics
        print(f"\nAnalysis Period: {all_results['year'].min()}-{all_results['year'].max()}")
        print(f"Historical data: {(~all_results['is_projection']).sum()} years")
        if extended_df is not None:
            print(f"Projections: {all_results['is_projection'].sum()} years")
        
        # Find transition points (probability crosses 50%)
        transition_points = []
        for i in range(1, len(all_results)):
            prev_prob = all_results.iloc[i-1]['probability_china_overtakes_us']
            curr_prob = all_results.iloc[i]['probability_china_overtakes_us']
            
            if (prev_prob >= 0.5 and curr_prob < 0.5) or (prev_prob < 0.5 and curr_prob >= 0.5):
                transition_points.append({
                    'year': all_results.iloc[i]['year'],
                    'probability': curr_prob,
                    'direction': 'China→US' if curr_prob < 0.5 else 'US→China'
                })
        
        print(f"\nTransition Points (probability crosses 50%):")
        if transition_points:
            for tp in transition_points:
                print(f"  {tp['year']}: {tp['direction']} (p={tp['probability']:.3f})")
        else:
            print("  No clear transition points found")
        
        # Current status
        latest = all_results.iloc[-1]
        print(f"\nLatest Prediction ({latest['year']}):")
        print(f"  Probability China overtakes US: {latest['probability_china_overtakes_us']:.1%}")
        print(f"  Power score: {latest['power_score']:.3f}")
        print(f"  Interpretation: {'China favored' if latest['power_score'] > 0 else 'US favored'}")
        
        # Trend analysis
        historical_data = all_results[~all_results['is_projection']]
        if len(historical_data) > 5:
            recent_trend = historical_data.tail(5)['probability_china_overtakes_us'].diff().mean()
            print(f"  Recent trend: {'Increasing' if recent_trend > 0 else 'Decreasing'} China overtaking probability")
        
        return all_results
    
    def create_visualizations(self, all_results):
        """Create visualizations of transition probabilities"""
        print("\nCreating visualizations...")
        
        # Ensure plots directory exists
        Path("plots").mkdir(exist_ok=True)
        
        # Create comprehensive plot
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('US-China Power Transition Analysis (Archimedes Model)', fontsize=16, fontweight='bold')
        
        # Separate historical and projected data
        historical = all_results[~all_results['is_projection']]
        projected = all_results[all_results['is_projection']] if 'is_projection' in all_results.columns else pd.DataFrame()
        
        # 1. Transition Probability Over Time
        ax1 = axes[0, 0]
        ax1.plot(historical['year'], historical['probability_china_overtakes_us'], 
                'r-', linewidth=2, label='Historical', alpha=0.8)
        if not projected.empty:
            ax1.plot(projected['year'], projected['probability_china_overtakes_us'], 
                    'r--', linewidth=2, label='Projected', alpha=0.8)
        ax1.axhline(y=0.5, color='black', linestyle='-', alpha=0.5, label='Neutral (50%)')
        ax1.fill_between(historical['year'], 0, historical['probability_china_overtakes_us'], alpha=0.3, color='red')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('P(China Overtakes US)')
        ax1.set_title('China Power Transition Probability Over Time')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Power Score
        ax2 = axes[0, 1]
        colors_hist = ['red' if score < 0 else 'blue' for score in historical['power_score']]
        ax2.scatter(historical['year'], historical['power_score'], c=colors_hist, alpha=0.6, label='Historical')
        if not projected.empty:
            colors_proj = ['red' if score < 0 else 'blue' for score in projected['power_score']]
            ax2.scatter(projected['year'], projected['power_score'], c=colors_proj, alpha=0.6, 
                       marker='s', label='Projected')
        ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5)
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Power Score')
        ax2.set_title('Power Score Over Time\n(Blue=US Favored, Red=China Favored)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # 3. Key Variables Over Time
        ax3 = axes[1, 0]
        ax3.plot(historical['year'], historical['food_volatility_log'], 'g-', label='Food Volatility (log)', alpha=0.7)
        ax3.plot(historical['year'], historical['exchange_volatility']/10, 'orange', label='Exchange Volatility/10', alpha=0.7)
        if historical['education_log'].notna().any():
            ax3.plot(historical['year'], historical['education_log'], 'm-', label='Education (log)', alpha=0.7)
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Variable Values')
        ax3.set_title('Key Model Variables')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Probability Distribution
        ax4 = axes[1, 1]
        ax4.hist(historical['probability_china_overtakes_us'], bins=20, alpha=0.7, 
                color='red', label='Historical')
        if not projected.empty:
            ax4.hist(projected['probability_china_overtakes_us'], bins=10, alpha=0.7, 
                    color='darkred', label='Projected')
        ax4.axvline(x=0.5, color='black', linestyle='--', alpha=0.5, label='Neutral')
        ax4.set_xlabel('Probability China Overtakes US')
        ax4.set_ylabel('Frequency')
        ax4.set_title('Distribution of China Transition Probabilities')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('plots/us_china_transition_analysis.png', dpi=300, bbox_inches='tight')
        print("Visualization saved to 'plots/us_china_transition_analysis.png'")
        plt.show()
    
    def export_results(self, all_results):
        """Export results to CSV"""
        output_file = 'data/us_china_transition_predictions.csv'
        all_results.to_csv(output_file, index=False)
        print(f"\nResults exported to '{output_file}'")
        
        # Create summary statistics
        summary = {
            'total_years': len(all_results),
            'historical_years': (~all_results['is_projection']).sum() if 'is_projection' in all_results.columns else len(all_results),
            'projected_years': all_results['is_projection'].sum() if 'is_projection' in all_results.columns else 0,
            'mean_probability_china_overtakes': all_results['probability_china_overtakes_us'].mean(),
            'latest_probability_china_overtakes': all_results.iloc[-1]['probability_china_overtakes_us'],
            'latest_power_score': all_results.iloc[-1]['power_score'],
            'years_china_favored': (all_results['power_score'] > 0).sum(),
            'years_us_favored': (all_results['power_score'] < 0).sum()
        }
        
        summary_df = pd.DataFrame([summary])
        summary_df.to_csv('data/us_china_transition_summary.csv', index=False)
        print(f"Summary statistics exported to 'data/us_china_transition_summary.csv'")

def main():
    """Main function to run the US-China transition analysis"""
    print("US-CHINA POWER TRANSITION PREDICTION")
    print("Using US-UK Archimedes Model Coefficients")
    print("=" * 50)
    
    # Initialize predictor
    predictor = USChinaTransitionPredictor()
    
    # Load and prepare data
    main_data, education_data = predictor.load_data()
    model_data = predictor.prepare_data(main_data, education_data)
    
    # Generate historical predictions
    historical_results = predictor.predict_transition_probability(model_data)
    
    # Extend predictions to 2030
    extended_results = predictor.extend_predictions(historical_results, end_year=2030)
    
    # Analyze results
    all_results = predictor.analyze_results(historical_results, extended_results)
    
    # Create visualizations
    predictor.create_visualizations(all_results)
    
    # Export results
    predictor.export_results(all_results)
    
    print("\n" + "="*50)
    print("ANALYSIS COMPLETE")
    print("="*50)
    print("Generated files:")
    print("  - plots/us_china_transition_analysis.png")
    print("  - data/us_china_transition_predictions.csv")
    print("  - data/us_china_transition_summary.csv")

if __name__ == "__main__":
    main()
