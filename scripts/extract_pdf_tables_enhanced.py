import pdfplumber
import pandas as pd
import json
import re

def extract_tables_from_pdf(pdf_path):
    """
    Extract all table data from a PDF file using multiple methods
    """
    all_tables = []
    all_text_data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"PDF has {len(pdf.pages)} pages")
        
        for page_num, page in enumerate(pdf.pages):
            print(f"\nProcessing page {page_num + 1}...")
            
            # Method 1: Extract tables using default settings
            tables = page.extract_tables()
            
            if tables:
                print(f"Found {len(tables)} table(s) on page {page_num + 1}")
                
                for table_num, table in enumerate(tables):
                    print(f"  Table {table_num + 1}: {len(table)} rows, {len(table[0]) if table else 0} columns")
                    
                    # Store table with metadata
                    table_data = {
                        'page': page_num + 1,
                        'table_number': table_num + 1,
                        'method': 'default',
                        'data': table
                    }
                    all_tables.append(table_data)
                    
                    # Print first few rows of each table for preview
                    print(f"  Preview of table {table_num + 1}:")
                    for i, row in enumerate(table[:5]):  # Show first 5 rows
                        print(f"    Row {i + 1}: {row}")
                    if len(table) > 5:
                        print(f"    ... and {len(table) - 5} more rows")
            
            # Method 2: Try with different table settings
            table_settings = {
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines",
            }
            tables_alt = page.extract_tables(table_settings)
            
            if tables_alt and not tables:  # Only if default method didn't work
                print(f"Found {len(tables_alt)} table(s) with alternative settings on page {page_num + 1}")
                
                for table_num, table in enumerate(tables_alt):
                    table_data = {
                        'page': page_num + 1,
                        'table_number': table_num + 1,
                        'method': 'lines_strategy',
                        'data': table
                    }
                    all_tables.append(table_data)
            
            # Method 3: Extract raw text and look for tabular patterns
            text = page.extract_text()
            if text:
                all_text_data.append({
                    'page': page_num + 1,
                    'text': text
                })
                
                # Look for potential table patterns in text
                lines = text.split('\n')
                potential_table_lines = []
                
                for line in lines:
                    # Look for lines with multiple numbers/data separated by spaces or tabs
                    if re.search(r'\d+.*\d+.*\d+', line) or len(line.split()) > 3:
                        potential_table_lines.append(line.strip())
                
                if potential_table_lines:
                    print(f"  Found {len(potential_table_lines)} potential table rows in text")
                    print(f"  Sample rows:")
                    for i, line in enumerate(potential_table_lines[:5]):
                        print(f"    {line}")
                    if len(potential_table_lines) > 5:
                        print(f"    ... and {len(potential_table_lines) - 5} more rows")
                    
                    # Try to parse as structured data
                    parsed_table = parse_text_table(potential_table_lines)
                    if parsed_table:
                        table_data = {
                            'page': page_num + 1,
                            'table_number': 1,
                            'method': 'text_parsing',
                            'data': parsed_table
                        }
                        all_tables.append(table_data)
            
            if not tables and not tables_alt and not potential_table_lines:
                print(f"No tables found on page {page_num + 1}")
    
    return all_tables, all_text_data

def parse_text_table(lines):
    """
    Try to parse text lines into a structured table
    """
    if not lines:
        return None
    
    table_data = []
    
    for line in lines:
        # Split by multiple spaces or tabs
        parts = re.split(r'\s{2,}|\t+', line.strip())
        if len(parts) > 1:  # Only include lines with multiple columns
            table_data.append(parts)
    
    # Only return if we have a reasonable number of rows
    if len(table_data) > 2:
        return table_data
    
    return None

def save_tables_to_csv(tables, base_filename="extracted_table"):
    """
    Save extracted tables to CSV files
    """
    for i, table_info in enumerate(tables):
        if table_info['data']:
            # Create DataFrame from table data
            df = pd.DataFrame(table_info['data'])
            
            # Use first row as headers if it looks like headers
            if len(df) > 1:
                # Check if first row contains mostly strings (likely headers)
                first_row_strings = sum(1 for cell in df.iloc[0] if isinstance(cell, str) and cell and not cell.replace('.', '').replace('-', '').isdigit())
                if first_row_strings > len(df.columns) / 2:
                    df.columns = df.iloc[0]
                    df = df.drop(df.index[0]).reset_index(drop=True)
            
            # Save to CSV
            method = table_info.get('method', 'unknown')
            filename = f"{base_filename}_page{table_info['page']}_table{table_info['table_number']}_{method}.csv"
            df.to_csv(filename, index=False)
            print(f"Saved table to {filename}")

def save_text_data(text_data, filename="extracted_text.json"):
    """
    Save all extracted text data
    """
    with open(filename, "w") as f:
        json.dump(text_data, f, indent=2)
    print(f"Saved all text data to {filename}")

def main():
    pdf_path = "data/Agprice_table.pdf"
    
    print(f"Extracting tables from: {pdf_path}")
    print("=" * 50)
    
    try:
        # Extract all tables and text
        tables, text_data = extract_tables_from_pdf(pdf_path)
        
        print(f"\n" + "=" * 50)
        print(f"SUMMARY: Found {len(tables)} table(s) total")
        
        if tables:
            # Save tables to CSV files
            print("\nSaving tables to CSV files...")
            save_tables_to_csv(tables, "agprice_table")
            
            # Also save raw table data as JSON for reference
            with open("agprice_tables_raw.json", "w") as f:
                json.dump(tables, f, indent=2)
            print("Saved raw table data to agprice_tables_raw.json")
        
        # Save text data for manual inspection
        if text_data:
            save_text_data(text_data, "agprice_text_data.json")
            
        if not tables:
            print("\nNo structured tables were found.")
            print("Check agprice_text_data.json for raw text that might contain tabular data.")
            
    except Exception as e:
        print(f"Error processing PDF: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
