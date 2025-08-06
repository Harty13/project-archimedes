#!/usr/bin/env python3
"""
Script to extend the education ratio back to 1825 using the first available value
"""

import pandas as pd
import numpy as np

def extend_education_ratio():
    """Extend education ratio back to 1825 using the first available value"""
    print("Extending Education Ratio back to 1825")
    print("=" * 45)
    
    # Load the current education ratio data
    df = pd.read_csv('data/ratios/us_uk_education_ratio.csv')
    
    print(f"Current data range: {df['year'].min()}-{df['year'].max()}")
    print(f"Current records: {len(df)}")
    
    # Get the first value
    first_year = df['year'].min()
    first_value = df['us_to_uk_ratio'].iloc[0]
    
    print(f"First available year: {first_year}")
    print(f"First available value: {first_value:.6f}")
    
    # Create extended data from 1825 to the year before the first available data
    extended_years = list(range(1825, first_year))
    extended_data = []
    
    for year in extended_years:
        extended_data.append({
            'year': year,
            'us_to_uk_ratio': first_value
        })
    
    # Create DataFrame for extended data
    extended_df = pd.DataFrame(extended_data)
    
    # Combine extended data with original data
    combined_df = pd.concat([extended_df, df], ignore_index=True)
    combined_df = combined_df.sort_values('year').reset_index(drop=True)
    
    print(f"\nExtended data:")
    print(f"New range: {combined_df['year'].min()}-{combined_df['year'].max()}")
    print(f"New records: {len(combined_df)}")
    print(f"Added {len(extended_data)} records from {extended_years[0]} to {extended_years[-1]}")
    
    # Save the extended data
    output_file = 'data/ratios/us_uk_education_ratio.csv'
    combined_df.to_csv(output_file, index=False)
    
    print(f"\nExtended education ratio saved to: {output_file}")
    
    # Show sample of extended data
    print(f"\nSample of extended data:")
    print("-" * 30)
    print(combined_df.head(10).to_string(index=False))
    print("...")
    print(combined_df.tail(5).to_string(index=False))
    
    return combined_df

def main():
    """Main function"""
    extended_df = extend_education_ratio()
    
    print(f"\n" + "="*45)
    print("EXTENSION COMPLETE")
    print("="*45)
    print(f"Education ratio now covers: {extended_df['year'].min()}-{extended_df['year'].max()}")
    print(f"Total records: {len(extended_df)}")
    
    return extended_df

if __name__ == "__main__":
    main()
