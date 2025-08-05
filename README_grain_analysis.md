# Historical Grain Price Analysis: Chicago Wheat vs UK Grain (1841-1960)

## Overview

This project provides comprehensive dataloaders and analysis tools for comparing historical grain prices between the United States (Chicago wheat) and the United Kingdom from the 18th to 20th centuries.

## Data Sources

### US Data
- **Chicago Wheat Prices (1841-1944)**: Monthly wheat prices from Chicago commodity markets
- **Source**: `data/m04001a_wheat_chicago_1841_1960.dat`
- **Records**: 1,237 monthly observations
- **Price Range**: $33.50 - $300.80 per unit

### UK Data
- **England Grain Prices (1841-1955)**: Monthly grain prices from England
- **Winchester Wheat Prices (1657-1817)**: Historical wheat prices from Winchester
- **Source**: International Institute of Social History dataverse files
- **Records**: 1,504 observations
- **Price Range**: £4.08 - £298.75 per unit

## Key Findings

### Price Correlation
- **Correlation coefficient**: 0.567 (moderate positive correlation)
- **Common analysis period**: 102 overlapping years
- This indicates that US and UK grain markets were moderately integrated, with prices moving in similar directions

### Historical Price Patterns

#### Pre-Civil War (1841-1860)
- Chicago average: $72.54
- UK average: £33.06
- Relatively stable period with UK prices lower than US

#### Civil War Period (1861-1865)
- Chicago average: $106.42 (+47% increase)
- UK average: £33.48 (minimal change)
- War significantly impacted US grain prices while UK remained stable

#### Post-Civil War (1866-1890)
- Chicago average: $111.95
- UK average: £35.49
- Continued high US prices during westward expansion

#### World War I (1915-1918)
- Chicago average: $176.12 (+143% from pre-war)
- UK average: £50.57 (+99% from pre-war)
- Both markets experienced significant wartime inflation

#### Great Depression (1930-1939)
- Chicago average: $86.22 (-43% from 1920s)
- UK average: £5.88 (-87% from 1920s)
- Dramatic price collapse, more severe in UK

### Price Volatility
- **US (Chicago)**: Higher volatility with standard deviation of $42.13
- **UK**: Lower volatility with standard deviation of £17.18
- US markets showed greater price swings, likely due to weather, speculation, and transportation factors

## Technical Implementation

### Files Created
1. **`chicago_wheat_dataloader.py`**: Main dataloader combining US and UK data
2. **`test_grain_dataloader.py`**: UK-only analysis tool
3. **`grain_price_dataloader.py`**: Original comprehensive dataloader
4. **`requirements.txt`**: Python dependencies

### Key Features
- **Data Cleaning**: Handles missing values and different data formats
- **Time Series Analysis**: Monthly and annual price comparisons
- **Statistical Analysis**: Correlation, volatility, and period-based analysis
- **Visualization**: Comprehensive plots showing price trends, volatility, and comparisons
- **Export Functionality**: CSV export for further analysis

### Visualizations Generated
1. **Monthly Price Comparison**: Time series of both markets
2. **Annual Average Prices**: Smoothed trends over time
3. **Price Volatility**: Rolling standard deviation analysis
4. **Decade Comparison**: Bar charts showing average prices by decade

## Usage

### Running the Analysis
```bash
# Install dependencies
pip install -r requirements.txt

# Run Chicago vs UK comparison
python chicago_wheat_dataloader.py

# Run UK-only analysis
python test_grain_dataloader.py
```

### Output Files
- `chicago_uk_grain_comparison.png`: Comprehensive comparison plots
- `chicago_uk_grain_prices.csv`: Combined dataset
- `uk_grain_prices_analysis.png`: UK-only analysis
- `uk_grain_prices_data.csv`: UK dataset

## Historical Context

### Market Integration
The moderate correlation (0.567) between Chicago and UK grain prices suggests:
- **Global market emergence**: By the mid-19th century, grain markets were becoming increasingly integrated
- **Transportation revolution**: Railways and steamships enabled price arbitrage
- **Information flow**: Telegraph communications allowed faster price discovery

### Major Events Impact
1. **American Civil War (1861-1865)**: Disrupted US production and exports
2. **Opening of American West**: Increased US grain production capacity
3. **World Wars**: Government intervention and supply disruptions
4. **Great Depression**: Demand collapse and agricultural overproduction

### Economic Implications
- **Comparative advantage**: US emerged as major grain exporter
- **Price discovery**: Chicago became global price-setting market
- **Risk management**: Price volatility led to development of futures markets

## Data Quality Notes

### Limitations
- **Currency differences**: US prices in cents, UK prices in shillings (not directly comparable)
- **Unit variations**: Different measurement units between markets
- **Missing data**: Some periods have incomplete records
- **Quality differences**: Grain grades and types may vary

### Strengths
- **Long time series**: Over 100 years of overlapping data
- **High frequency**: Monthly observations allow seasonal analysis
- **Multiple sources**: Cross-validation possible with different UK datasets
- **Historical significance**: Covers major economic and political events

## Future Enhancements

### Potential Improvements
1. **Currency conversion**: Implement historical exchange rates
2. **Additional markets**: Include other US and European markets
3. **Seasonal analysis**: Detailed harvest cycle patterns
4. **Economic indicators**: Correlate with GDP, population, weather data
5. **Predictive modeling**: Time series forecasting models

### Research Applications
- **Economic history**: Understanding 19th-century globalization
- **Agricultural economics**: Long-term price trend analysis
- **Financial markets**: Historical volatility and risk patterns
- **Policy analysis**: Impact of wars, tariffs, and regulations

## Conclusion

This analysis reveals the emergence of integrated global grain markets during the 19th and early 20th centuries. The moderate correlation between Chicago and UK prices, combined with the differential impacts of major historical events, provides valuable insights into the development of modern commodity markets and international trade patterns.

The dataloaders and analysis tools created provide a foundation for further research into historical agricultural economics and market development.
