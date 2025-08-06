import pandas as pd
import numpy as np
import os

def calculate_volatility(data, value_column, window=5, min_periods=3):
    """Calculate rolling volatility (standard deviation) of a data series."""
    data = data.sort_values('year')
    # Calculate year-over-year percentage change
    data['pct_change'] = data[value_column].pct_change() * 100
    # Calculate rolling volatility
    data['volatility'] = data['pct_change'].rolling(window=window, min_periods=min_periods).std()
    return data[['year', 'volatility']].dropna()

def create_china_us_ratio(china_data, us_data, metric_name):
    """Create ratio of China to US for a given metric."""
    # Merge on year
    merged = pd.merge(china_data, us_data, on='year', suffixes=('_china', '_us'))
    
    # Calculate ratio (China / US), handling division by zero
    china_col = f'{metric_name}_china'
    us_col = f'{metric_name}_us'
    
    # Only calculate ratio where both values are positive and non-zero
    valid_mask = (merged[china_col] > 0) & (merged[us_col] > 0) & (merged[china_col].notna()) & (merged[us_col].notna())
    
    merged['ratio'] = np.where(valid_mask, merged[china_col] / merged[us_col], np.nan)
    
    # Remove rows with invalid ratios
    result = merged[['year', 'ratio']].dropna()
    
    return result

# Ensure output directory exists
os.makedirs('data/ratios/US_China', exist_ok=True)

print("Creating US-China Ratios for All Categories")
print("=" * 50)

# 1. Child Mortality Ratios
print("\n1. Processing Child Mortality...")
child_mortality = pd.read_csv('data/child_mortality/child_mortality_china_usa_processed.csv')
china_mortality = child_mortality[child_mortality['country'] == 'China'][['year', 'mortality_rate']].copy()
us_mortality = child_mortality[child_mortality['country'] == 'United States'][['year', 'mortality_rate']].copy()

# Calculate volatility for child mortality
china_mortality_vol = calculate_volatility(china_mortality, 'mortality_rate')
us_mortality_vol = calculate_volatility(us_mortality, 'mortality_rate')

# Create ratio
mortality_ratios = create_china_us_ratio(china_mortality_vol, us_mortality_vol, 'volatility')
mortality_ratios.to_csv('data/ratios/US_China/child_mortality_volatility_ratio.csv', index=False)
print(f"   Created child_mortality_volatility_ratio.csv ({len(mortality_ratios)} records)")

# 2. Education Enrollment Ratios
print("\n2. Processing Education Enrollment...")
education = pd.read_csv('data/education/primary_enrollment_processed.csv')
china_education = education[education['country'] == 'China'][['year', 'enrollment_rate']].copy()
us_education = education[education['country'] == 'United States'][['year', 'enrollment_rate']].copy()

# Create ratio of enrollment rates directly (not volatility)
education_ratios = create_china_us_ratio(china_education, us_education, 'enrollment_rate')
education_ratios.to_csv('data/ratios/US_China/education_enrollment_ratio.csv', index=False)
print(f"   Created education_enrollment_ratio.csv ({len(education_ratios)} records)")

# 3. Exchange Rate Volatility
print("\n3. Processing Exchange Rate...")
exchange_rate = pd.read_csv('data/exchange_rates/cny_usd_exchange_rate_processed.csv')

# Calculate volatility of exchange rate
exchange_vol = calculate_volatility(exchange_rate, 'exchange_rate')
# For exchange rate, we just save the volatility (no ratio needed as it's already CNY/USD)
exchange_vol.to_csv('data/ratios/US_China/exchange_rate_volatility.csv', index=False)
print(f"   Created exchange_rate_volatility.csv ({len(exchange_vol)} records)")

# 4. Food Price Volatility Ratios
print("\n4. Processing Food Price Volatility...")
food_volatility = pd.read_csv('data/food/food_volatility_processed.csv')
china_food = food_volatility[food_volatility['country'] == 'China'][['year', 'volatility']].copy()
us_food = food_volatility[food_volatility['country'] == 'United States'][['year', 'volatility']].copy()

# Create ratio (food volatility is already calculated)
food_ratios = create_china_us_ratio(china_food, us_food, 'volatility')
food_ratios.to_csv('data/ratios/US_China/food_volatility_ratio.csv', index=False)
print(f"   Created food_volatility_ratio.csv ({len(food_ratios)} records)")

# 5. GDP Volatility Ratios
print("\n5. Processing GDP Volatility...")
gdp_volatility = pd.read_csv('data/gdp/gdp_volatility_china_usa_processed.csv')
china_gdp = gdp_volatility[gdp_volatility['country'] == 'China'][['year', 'volatility']].copy()
us_gdp = gdp_volatility[gdp_volatility['country'] == 'United States'][['year', 'volatility']].copy()

# Create ratio (GDP volatility is already calculated)
gdp_ratios = create_china_us_ratio(china_gdp, us_gdp, 'volatility')
gdp_ratios.to_csv('data/ratios/US_China/gdp_volatility_ratio.csv', index=False)
print(f"   Created gdp_volatility_ratio.csv ({len(gdp_ratios)} records)")

print("\n" + "=" * 50)
print("Summary of Created Files:")
print("=" * 50)

# Read and summarize each file
files = [
    ('child_mortality_volatility_ratio.csv', 'Child Mortality Volatility'),
    ('education_enrollment_ratio.csv', 'Education Enrollment Ratio'),
    ('exchange_rate_volatility.csv', 'Exchange Rate Volatility'),
    ('food_volatility_ratio.csv', 'Food Price Volatility'),
    ('gdp_volatility_ratio.csv', 'GDP Volatility')
]

for filename, description in files:
    filepath = f'data/ratios/US_China/{filename}'
    df = pd.read_csv(filepath)
    
    print(f"\n{description}:")
    print(f"   File: {filename}")
    print(f"   Records: {len(df)}")
    print(f"   Year range: {df['year'].min():.0f} - {df['year'].max():.0f}")
    
    if 'ratio' in df.columns:
        print(f"   Ratio range: {df['ratio'].min():.4f} - {df['ratio'].max():.4f}")
        print(f"   Average ratio: {df['ratio'].mean():.4f}")
        print(f"   Latest ratio (China/US): {df['ratio'].iloc[-1]:.4f} in {df['year'].iloc[-1]:.0f}")
    else:
        print(f"   Volatility range: {df['volatility'].min():.4f} - {df['volatility'].max():.4f}")
        print(f"   Average volatility: {df['volatility'].mean():.4f}")
        print(f"   Latest volatility: {df['volatility'].iloc[-1]:.4f} in {df['year'].iloc[-1]:.0f}")

print(f"\nAll ratio files saved to: data/ratios/US_China/")