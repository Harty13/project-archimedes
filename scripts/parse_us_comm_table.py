import pdfplumber
import pandas as pd
import json
import re

def extract_us_comm_data(pdf_path):
    """
    Extract US commodity price index data from the specific PDF structure
    """
    all_data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"PDF has {len(pdf.pages)} pages")
        
        # Define the expected columns based on the header we saw
        months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
        
        for page_num, page in enumerate(pdf.pages):
            print(f"Processing page {page_num + 1}...")
            
            text = page.extract_text()
            if not text:
                continue
                
            lines = text.split('\n')
            
            for line in lines:
                line = line.strip()
                
                # Skip empty lines, header lines, and table titles
                if not line or 'TABLE 62' in line or 'Base:' in line or 'WHOLESALE COMMODITY' in line:
                    continue
                if 'Year Jan.' in line or 'Continued' in line or line.startswith('iS6'):
                    continue
                
                # Look for lines that start with a year (4 digits)
                if re.match(r'^\d{4}', line):
                    # Split the line by whitespace
                    parts = line.split()
                    
                    if len(parts) >= 2:  # At least has a year and some data
                        try:
                            year = int(parts[0])
                            
                            # Create a row with the year and monthly data
                            row_data = {'Year': year}
                            
                            # Map the remaining parts to months
                            # Skip the year (parts[0]) and map the rest
                            data_parts = parts[1:]
                            
                            for i, month in enumerate(months):
                                if i < len(data_parts):
                                    value = data_parts[i]
                                    # Handle special cases like dots, dashes, or missing values
                                    if value in ['.', '..', '...', '-', '—']:
                                        row_data[month] = None
                                    else:
                                        try:
                                            # Try to convert to float
                                            row_data[month] = float(value)
                                        except ValueError:
                                            # If conversion fails, store as string or None
                                            if value.replace('.', '').isdigit():
                                                row_data[month] = float(value)
                                            else:
                                                row_data[month] = None
                                else:
                                    row_data[month] = None
                            
                            all_data.append(row_data)
                            
                            if len(all_data) % 20 == 0:  # Progress indicator
                                print(f"  Extracted {len(all_data)} rows so far...")
                                
                        except ValueError:
                            # Skip lines where year conversion fails
                            continue
    
    return all_data

def clean_and_validate_data(data):
    """
    Clean and validate the extracted data
    """
    print(f"\nCleaning {len(data)} rows of data...")
    
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(data)
    
    if df.empty:
        print("No data to clean")
        return df
    
    # Sort by year
    df = df.sort_values('Year').reset_index(drop=True)
    
    # Print some statistics
    print(f"Year range: {df['Year'].min()} - {df['Year'].max()}")
    print(f"Total rows: {len(df)}")
    
    # Show data completeness for each month
    print("\nData completeness by month:")
    months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
    for month in months:
        if month in df.columns:
            non_null_count = df[month].notna().sum()
            percentage = (non_null_count / len(df)) * 100
            print(f"  {month:6}: {non_null_count:3d}/{len(df)} ({percentage:5.1f}%)")
    
    return df

def reshape_to_long_format(df):
    """
    Reshape the data from wide format (months as columns) to long format
    """
    if df.empty:
        return df
    
    print("Reshaping data to long format...")
    
    months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
    month_mapping = {
        'Jan.': 1, 'Feb.': 2, 'Mar.': 3, 'Apr.': 4, 'May': 5, 'June': 6,
        'July': 7, 'Aug.': 8, 'Sept.': 9, 'Oct.': 10, 'Nov.': 11, 'Dec.': 12
    }
    
    long_data = []
    
    for _, row in df.iterrows():
        year = row['Year']
        for month_name in months:
            if month_name in df.columns and pd.notna(row[month_name]):
                month_num = month_mapping[month_name]
                long_data.append({
                    'Year': year,
                    'Month': month_num,
                    'Month_Name': month_name.rstrip('.'),
                    'Price_Index': row[month_name],
                    'Date': f"{year}-{month_num:02d}"
                })
    
    long_df = pd.DataFrame(long_data)
    print(f"Reshaped to {len(long_df)} monthly observations")
    
    return long_df

def main():
    pdf_path = "data/US_comm_1730_1860.pdf"
    
    print(f"Extracting US commodity price index data from: {pdf_path}")
    print("=" * 70)
    
    try:
        # Extract the data
        data = extract_us_comm_data(pdf_path)
        
        if data:
            print(f"\nExtracted {len(data)} rows of data")
            
            # Clean and validate
            df_wide = clean_and_validate_data(data)
            
            if not df_wide.empty:
                # Save wide format data
                wide_output_file = "us_comm_price_index_wide.csv"
                df_wide.to_csv(wide_output_file, index=False)
                print(f"\nSaved wide format data to {wide_output_file}")
                
                # Reshape to long format
                df_long = reshape_to_long_format(df_wide)
                
                if not df_long.empty:
                    # Save long format data
                    long_output_file = "us_comm_price_index_long.csv"
                    df_long.to_csv(long_output_file, index=False)
                    print(f"Saved long format data to {long_output_file}")
                
                # Save raw data as JSON for reference
                with open("us_comm_price_index_raw.json", "w") as f:
                    json.dump(data, f, indent=2, default=str)
                print("Saved raw data to us_comm_price_index_raw.json")
                
                # Show sample of the data
                print(f"\nSample of extracted data (first 10 rows):")
                print(df_wide.head(10).to_string(index=False))
                
                print(f"\nSample of long format data (first 15 rows):")
                if not df_long.empty:
                    print(df_long.head(15).to_string(index=False))
                
                # Basic statistics
                if not df_long.empty:
                    print(f"\nBasic Statistics:")
                    print(f"Price Index Range: {df_long['Price_Index'].min():.1f} - {df_long['Price_Index'].max():.1f}")
                    print(f"Average Price Index: {df_long['Price_Index'].mean():.1f}")
                    print(f"Standard Deviation: {df_long['Price_Index'].std():.1f}")
            
        else:
            print("No data was extracted")
            
    except Exception as e:
        print(f"Error processing PDF: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
