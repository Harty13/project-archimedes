import pdfplumber
import pandas as pd
import json
import re

def extract_agprice_data(pdf_path):
    """
    Extract agricultural price data from the specific PDF structure
    """
    all_data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"PDF has {len(pdf.pages)} pages")
        
        # Define the expected columns based on the header we saw
        columns = ['Year', 'Wheat', 'Rye', 'Barley', 'Oats', 'Peas', 'Beans', 'Potato', 'Hops', 'Net', 'Straw', 'Mustard', 'Saffron']
        units = ['', '(s./bu.)', '(s./bu.)', '(s./bu.)', '(s./bu.)', '(s./bu.)', '(s./bu.)', '(s./cwt.)', 'Tax', '(s./load)', 'Seed', '(s./lb)', '']
        
        for page_num, page in enumerate(pdf.pages):
            print(f"Processing page {page_num + 1}...")
            
            text = page.extract_text()
            if not text:
                continue
                
            lines = text.split('\n')
            
            for line in lines:
                line = line.strip()
                
                # Skip empty lines and header lines
                if not line or 'Appendix Table' in line or 'Year Wheat' in line or '(s./bu.)' in line:
                    continue
                
                # Look for lines that start with a year (4 digits)
                if re.match(r'^\d{4}', line):
                    # Split the line by whitespace
                    parts = line.split()
                    
                    if len(parts) >= 1:  # At least has a year
                        # Create a row with the year and available data
                        row_data = {'Year': int(parts[0])}
                        
                        # Map the remaining parts to columns
                        # Skip the year (parts[0]) and map the rest
                        data_parts = parts[1:]
                        
                        # Map to commodity columns (skip Year column)
                        commodity_columns = columns[1:]  # All columns except Year
                        
                        for i, value in enumerate(data_parts):
                            if i < len(commodity_columns):
                                try:
                                    # Try to convert to float, if it fails, keep as string
                                    row_data[commodity_columns[i]] = float(value)
                                except ValueError:
                                    row_data[commodity_columns[i]] = value
                        
                        # Fill missing columns with None
                        for col in commodity_columns:
                            if col not in row_data:
                                row_data[col] = None
                        
                        all_data.append(row_data)
                        
                        if len(all_data) % 50 == 0:  # Progress indicator
                            print(f"  Extracted {len(all_data)} rows so far...")
    
    return all_data, columns

def clean_and_validate_data(data):
    """
    Clean and validate the extracted data
    """
    print(f"\nCleaning {len(data)} rows of data...")
    
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(data)
    
    # Sort by year
    df = df.sort_values('Year').reset_index(drop=True)
    
    # Print some statistics
    print(f"Year range: {df['Year'].min()} - {df['Year'].max()}")
    print(f"Total rows: {len(df)}")
    
    # Show data completeness for each column
    print("\nData completeness by column:")
    for col in df.columns:
        non_null_count = df[col].notna().sum()
        percentage = (non_null_count / len(df)) * 100
        print(f"  {col}: {non_null_count}/{len(df)} ({percentage:.1f}%)")
    
    return df

def main():
    pdf_path = "data/Agprice_table.pdf"
    
    print(f"Extracting agricultural price data from: {pdf_path}")
    print("=" * 60)
    
    try:
        # Extract the data
        data, columns = extract_agprice_data(pdf_path)
        
        if data:
            print(f"\nExtracted {len(data)} rows of data")
            
            # Clean and validate
            df = clean_and_validate_data(data)
            
            # Save to CSV
            output_file = "agprice_table_extracted.csv"
            df.to_csv(output_file, index=False)
            print(f"\nSaved data to {output_file}")
            
            # Save raw data as JSON for reference
            with open("agprice_table_raw.json", "w") as f:
                json.dump(data, f, indent=2, default=str)
            print("Saved raw data to agprice_table_raw.json")
            
            # Show sample of the data
            print(f"\nSample of extracted data (first 10 rows):")
            print(df.head(10).to_string(index=False))
            
            print(f"\nSample of extracted data (last 10 rows):")
            print(df.tail(10).to_string(index=False))
            
        else:
            print("No data was extracted")
            
    except Exception as e:
        print(f"Error processing PDF: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
