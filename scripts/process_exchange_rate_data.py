#!/usr/bin/env python3

from dataloaders.exchange_rate_dataloader import ExchangeRateDataLoader
import os

def main():
    # Initialize the exchange rate data loader
    file_path = "data/exchange_rates/EXCHANGEPOUND_1791-2000.csv"
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found!")
        return
    
    # Load and process the data
    print("Loading exchange rate data...")
    loader = ExchangeRateDataLoader(file_path)
    processed_data = loader.load_data()
    
    # Display basic information about the data
    print(f"Data loaded successfully!")
    print(f"Shape: {processed_data.shape}")
    print(f"Years covered: {processed_data['year'].min()} - {processed_data['year'].max()}")
    print(f"Exchange rate range: ${processed_data['usd_per_gbp'].min():.2f} - ${processed_data['usd_per_gbp'].max():.2f}")
    
    # Show first few rows
    print("\nFirst 10 rows:")
    print(processed_data.head(10))
    
    # Show last few rows
    print("\nLast 10 rows:")
    print(processed_data.tail(10))
    
    # Save processed data
    output_path = "data/exchange_rates/processed_exchange_rate_data.csv"
    processed_data.to_csv(output_path, index=False)
    print(f"\nProcessed data saved to: {output_path}")

if __name__ == "__main__":
    main()
