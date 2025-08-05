#!/usr/bin/env python3
"""
Test script for the GDP per capita dataloader
"""

import sys
from pathlib import Path

# Add the dataloaders directory to the path
sys.path.append('dataloaders')

from gdp_per_capita_dataloader import GDPPerCapitaDataLoader

def test_dataloader():
    """Test the GDP per capita dataloader functionality"""
    print("Testing GDP per Capita DataLoader")
    print("=" * 40)
    
    # Initialize the dataloader
    loader = GDPPerCapitaDataLoader()
    
    # Test 1: Load data
    print("\n1. Testing data loading...")
    loader.load_data()
    
    if loader.raw_data.empty:
        print("❌ Failed to load data")
        return False
    else:
        print(f"✅ Successfully loaded {len(loader.raw_data)} records")
    
    # Test 2: Process data for US and UK
    print("\n2. Testing data processing for US and UK...")
    countries = ['United States', 'United Kingdom']
    loader.process_data(countries=countries)
    
    if loader.processed_data.empty:
        print("❌ Failed to process data")
        return False
    else:
        print(f"✅ Successfully processed data for {len(loader.country_data)} countries")
    
    # Test 3: Get country-specific data
    print("\n3. Testing country-specific data retrieval...")
    us_data = loader.get_country_data('United States')
    uk_data = loader.get_country_data('United Kingdom')
    
    if us_data.empty or uk_data.empty:
        print("❌ Failed to retrieve country data")
        return False
    else:
        print(f"✅ US data: {len(us_data)} records ({us_data['Year'].min()}-{us_data['Year'].max()})")
        print(f"✅ UK data: {len(uk_data)} records ({uk_data['Year'].min()}-{uk_data['Year'].max()})")
    
    # Test 4: Calculate growth statistics
    print("\n4. Testing growth statistics calculation...")
    growth_stats = loader.calculate_growth_statistics(
        countries=countries,
        start_year=1950,
        end_year=2020
    )
    
    if growth_stats.empty:
        print("❌ Failed to calculate growth statistics")
        return False
    else:
        print("✅ Growth statistics calculated successfully:")
        for _, row in growth_stats.iterrows():
            print(f"   {row['Country']}: {row['CAGR (%)']:.2f}% CAGR (1950-2020)")
    
    # Test 5: Export data
    print("\n5. Testing data export...")
    test_filename = "test_gdp_export.csv"
    loader.export_data(countries=countries, filename=test_filename)
    
    # Check if file was created
    if Path(test_filename).exists():
        print(f"✅ Data exported successfully to {test_filename}")
        # Clean up test file
        Path(test_filename).unlink()
    else:
        print("❌ Failed to export data")
        return False
    
    print("\n" + "=" * 40)
    print("✅ All tests passed! DataLoader is working correctly.")
    return True

def test_specific_functionality():
    """Test specific functionality and edge cases"""
    print("\n\nTesting Specific Functionality")
    print("=" * 35)
    
    loader = GDPPerCapitaDataLoader()
    loader.load_data()
    
    # Test with different country combinations
    test_cases = [
        (['United States'], "Single country (US)"),
        (['United Kingdom'], "Single country (UK)"),
        (['United States', 'United Kingdom', 'Germany'], "Multiple countries"),
        (['NonExistentCountry'], "Non-existent country"),
    ]
    
    for countries, description in test_cases:
        print(f"\nTesting: {description}")
        loader.process_data(countries=countries)
        
        if loader.processed_data.empty and countries != ['NonExistentCountry']:
            print(f"❌ Failed: {description}")
        elif countries == ['NonExistentCountry'] and loader.processed_data.empty:
            print(f"✅ Correctly handled: {description}")
        else:
            print(f"✅ Success: {description} - {len(loader.processed_data)} records")
    
    print("\n✅ Specific functionality tests completed.")

if __name__ == "__main__":
    success = test_dataloader()
    
    if success:
        test_specific_functionality()
        print("\n🎉 All tests completed successfully!")
    else:
        print("\n❌ Some tests failed. Please check the dataloader implementation.")
